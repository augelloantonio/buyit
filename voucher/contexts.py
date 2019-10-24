from django.shortcuts import render, redirect
from .views import Voucher
from django.shortcuts import get_object_or_404
from products.models import Product
from voucher.forms import VoucherForm
from decimal import Decimal


def voucher_contents(request):
    cart = request.session.get('cart', {})
    voucher_id = request.session.get('voucher_id', int())

    cart_items = []
    total = 0
    product_count = 0
    new_total = 0

    try:
        code = Voucher.objects.get(id=voucher_id)

    except Voucher.DoesNotExist:
        code = None

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        # Handle bug if voucher_id is not in session
        if code != None:
            discount = (code.price_reducing/Decimal('100'))*total
            new_total = total - discount
        else:
            new_total = total
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity,
                           'product': product})

    voucher_form = VoucherForm(request.POST)

    return {'code': code, 'voucher_id': voucher_id, 'new_total': new_total, 'voucher_form': voucher_form}
