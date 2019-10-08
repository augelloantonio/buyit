from django.shortcuts import get_object_or_404
from products.models import Product
from voucher.models import Voucher
from voucher.forms import VoucherForm


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})
    voucher_id = request.session.get('voucher_id')

    cart_items = []
    total = 0
    product_count = 0
    new_total = 0

    code = Voucher.objects.get(id=voucher_id)
   

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        new_total = total - code.price_reducing
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})

    voucher_form = VoucherForm(request.POST)
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count, 'voucher_form':voucher_form,
    'new_total':new_total}
