from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from orders.models import OrderLineItem, Order
from products.models import Product
from django.db.models import Count, Sum, Q
from products.forms import ProductForm
from reviews.models import Review
from django.db.models.functions import TruncMonth, TruncYear


@login_required
def dashboard(request):
    orders = Order.objects.all()
    order_info = OrderLineItem.objects.all()
    product = Product.objects.all()
    reviews = Review.objects.all()

    total_orders_earning = sum(items.total for items in order_info)
    monthly_orders_earning = (total_orders_earning / 12)
    total_orders = orders.count()
    total_product_sold = 0
    total_products = product.count()
    total_products_in_stock = product.exclude(in_stock=False).count()
    total_products_not_stock = product.exclude(in_stock=True).count()
    total_reviews = reviews.count()


    for items in order_info:
        total_product_sold = sum(items.quantity for items in order_info)

    order_by_date = order_info.filter(order__date__year='2019').values_list(
        'order__date__month').annotate(total_order_price=Count('total'))

    dataset = OrderLineItem.objects.annotate(month=TruncMonth(
        'date')).values('total').annotate(order_sum=(Sum('total')))

    # Calculate percentage of products stok/not stock
    perc_stock_prod = (total_products_in_stock/total_products)*100
    perc_not_stock_prod = (total_products_not_stock/total_products)*100

    context = {"orders": orders, "total_orders_earning": total_orders_earning,
               "total_orders": total_orders, "total_product_sold": total_product_sold, "monthly_orders_earning": monthly_orders_earning,
               "total_products": total_products, "total_products_in_stock": total_products_in_stock,
               "total_products_not_stock": total_products_not_stock, "total_reviews": total_reviews,
               'dataset': dataset, 'perc_stock_prod': perc_stock_prod, 'perc_not_stock_prod': perc_not_stock_prod,}

    return render(request, "dashboard.html", context)


@login_required
def dashboard_orders(request):
    orders = Order.objects.all()
    order_info = OrderLineItem.objects.all()
    product = Product.objects.all()

    return render(request, "dashboardorders.html", {"order_info": order_info, "orders": orders, 'product': product})


def dashboard_order_details(request, id):
    orders = Order.objects.all()
    order_info = OrderLineItem.objects.all()
    order = get_object_or_404(Order, id=id)
    total_order_price = sum(
        items.total for items in order_info if order.id == items.order.id)

    return render(request, "dashboardordersdetails.html", {"order_info": order_info, "orders": orders, 'order': order,
                                                           "total_order_price": total_order_price})


def dashboard_product(request):
    products = Product.objects.all()

    return render(request, "dashboardproducts.html", {"products": products})


def confirm_delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "confirmdeleteproduct.html", {"product": product})


def add_a_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(dashboard_product)
    else:
        form = ProductForm()

    return render(request, "dashboardaddproduct.html", {'form': form})
