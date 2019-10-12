from django.shortcuts import get_object_or_404
from products.models import Product
from voucher.models import Voucher
from voucher.forms import VoucherForm
from decimal import Decimal


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    # Handle bug if voucher_id is not in session
    code = None

    if 'voucher_id':
        voucher_id = request.session.get('voucher_id')
        try:
            code = Voucher.objects.get(id=voucher_id)
        except Voucher.DoesNotExist:
            code = None
    else:
        None

    cart_items = []
    total = 0
    product_count = 0
    new_total = 0

    for id, quantity in cart.items():
        user = request.user
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        # Handle bug if voucher_id is not in session
        if code != None:
            discount = (code.price_reducing/Decimal('100'))*total
            new_total = total - discount
        else:
            new_total = total
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product,
                           'user': user})


    voucher_form = VoucherForm(request.POST)

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count, 'voucher_form': voucher_form,
            'new_total': new_total}
