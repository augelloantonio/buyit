from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total_product = 0
    product_count = 0
    shipping_costs = 0
    total = 0

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total_product += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity,
                           'product': product})

    if total_product >= 50:
        shipping_costs = 0
        total += shipping_costs + total_product
    else:
        shipping_costs = 10
        total += shipping_costs + total_product

    return {'cart_items': cart_items, 'total': total, 'total_product': total_product, 'product_count': product_count, 'shipping_costs': shipping_costs}
