from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm, OrderStatus
from voucher.forms import VoucherForm
from .models import OrderLineItem, Order
from django.conf import settings
from django.utils import timezone
from products.models import Product
from voucher.models import Voucher
from decimal import Decimal
import stripe
import datetime


stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        code = None
        # Handle bug if voucher_id is not in session
        if 'voucher_id' in request.session:
            voucher_id = request.session['voucher_id']
            try:
                code = Voucher.objects.get(id=voucher_id)
            except Voucher.DoesNotExist:
                code = None
        else:
            None
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = datetime.datetime.now()

            order.save()

            cart = request.session.get('cart', {})
            total = 0
            new_total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                product_sold_quantity = product.quantity_sold + quantity
                if code != None:
                    discount = (code.price_reducing/Decimal('100'))*total
                    new_total = total - discount
                else:
                    new_total = total
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity,
                    total=new_total,
                )
                order_line_item.save()
                Product.objects.filter(id=id).update(quantity_sold=product_sold_quantity)
                request.session['voucher_id'] = None
            try:
                customer = stripe.Charge.create(
                    amount=int(new_total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.warning(request, "Your card was declined! Pleace check that the payment details are correct and try again.")
                return redirect('profile')
            if customer.paid:
                messages.success(request, "You have successfully paid. Your order will be processed soon.")
                # empty session cart
                request.session['cart'] = {}
                # Remove voucher from session
                request.session['voucher'] = None
                return redirect('profile')
            else:
                messages.warning(request, "We were unable to take payment, we are sorry for the inconvenient, please, try again")
                return redirect('profile')
        else:
            print(payment_form.errors)
            messages.warning("We were unable to take a payment with that card!")
            request ('profile')
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})


def all_orders(request):
    orders = Order.objects.all()
    return render(request, "orders.html", {"orders": orders})


def order_detail(request, id):
    """
    Order details view
    """
    order = get_object_or_404(Order, id=id)
    return render(request, "orderdetails.html", {'order': order})


def change_order_status(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == "POST":
        form = OrderStatus(request.POST)
        if form.is_valid():
            order_status = form.cleaned_data['order_status']
            Order.objects.filter(id=id).update(order_status=order_status)
            return HttpResponseRedirect(reverse('dashboard'))
    return redirect('dashboard')