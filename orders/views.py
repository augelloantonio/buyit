from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from voucher.forms import VoucherForm
from .models import OrderLineItem, Order
from django.conf import settings
from django.utils import timezone
from products.models import Product
from voucher.models import Voucher
from decimal import Decimal
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method == "POST":

        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        # Handle bug if voucher_id is not in session
        if request.session['voucher_id'] != None:
            voucher_id = request.session.get('voucher_id')
            code = Voucher.objects.get(id=voucher_id)
        else:
            None
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()

            order.save()

            cart = request.session.get('cart', {})
            total = 0
            new_total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                if request.session['voucher_id'] != None:
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
                product.quantity_sold == quantity
                product.save()
            try:
                customer = stripe.Charge.create(
                    amount=int(new_total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                # empty session cart
                request.session['cart'] = {}
                # Remove voucher from session
                request.session['voucher_id'] = None
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
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
