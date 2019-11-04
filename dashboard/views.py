from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from orders.models import OrderLineItem, Order
from products.models import Product, Category
from django.db.models import Count, Sum, Q
from django.contrib.auth.models import User
from products.forms import ProductForm, CategoryForm
from reviews.models import Review
from django.db.models.functions import TruncMonth, TruncYear
from datetime import date
from orders.filters import OrdersFilter
from orders.forms import OrderStatus


@login_required
def dashboard(request):
    orders = Order.objects.all()
    order_info = OrderLineItem.objects.all()
    product = Product.objects.all()
    reviews = Review.objects.all()

    today = date.today()

    total_orders = orders.count()
    total_product_sold = 0
    total_products = product.count()
    total_products_in_stock = product.exclude(in_stock=False).count()
    total_products_not_stock = product.exclude(in_stock=True).count()
    total_reviews = reviews.count()

    if order_info:
        total_orders_earning = sum(items.total for items in order_info)
        today_orders_earning = sum(
            items.total for items in order_info.filter(date__day=today.day))
        for items in order_info:
            total_product_sold = sum(items.quantity for items in order_info)
    else:
        total_product_sold = 0
        total_orders_earning = 0
        today_orders_earning = 0

    order_by_date = order_info.filter(order__date__year='2019').values_list(
        'order__date__month').annotate(total_order_price=Count('total'))

    dataset = OrderLineItem.objects.annotate(month=TruncMonth(
        'date')).values('total').annotate(order_sum=(Sum('total')))

    # Calculate percentage of products stok/not stock

    if total_products != 0:
        perc_stock_prod = (total_products_in_stock/total_products)*100
        perc_not_stock_prod = (total_products_not_stock/total_products)*100
    else:
        perc_stock_prod = 0
        perc_not_stock_prod = 0

    context = {"orders": orders, "total_orders_earning": total_orders_earning,
               "total_orders": total_orders, "total_product_sold": total_product_sold, "today_orders_earning": today_orders_earning,
               "total_products": total_products, "total_products_in_stock": total_products_in_stock,
               "total_products_not_stock": total_products_not_stock, "total_reviews": total_reviews,
               'dataset': dataset, 'perc_stock_prod': perc_stock_prod, 'perc_not_stock_prod': perc_not_stock_prod, }

    return render(request, "dashboard.html", context)


@login_required
def dashboard_orders(request):
    orders = Order.objects.all().order_by('-id')
    order_info = OrderLineItem.objects.all()
    product = Product.objects.all()

    filter_orders = OrdersFilter(request.GET, queryset=orders)

    return render(request, "dashboardorders.html", {"order_info": order_info, "orders": orders,
                                                    'product': product, 'filter': filter_orders})


@login_required
def dashboard_order_details(request, id):
    orders = Order.objects.all()
    order_info = OrderLineItem.objects.all()
    order = get_object_or_404(Order, id=id)
    total_order_price = sum(
        items.total for items in order_info if order.id == items.order.id)

    form = OrderStatus(request.POST)

    return render(request, "dashboardordersdetails.html", {"order_info": order_info, "orders": orders, 'order': order,
                                                           "total_order_price": total_order_price, 'form': form})


@login_required
def dashboard_product(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, "dashboardproducts.html", {"products": products, 'categories': categories})


@login_required
def add_a_category(request):
    if request.method == "POST":
        category_form = CategoryForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return redirect(dashboard_product)
    else:
        category_form = CategoryForm()
    return render(request, "dashboardaddcategory.html", {'category_form': category_form})


@login_required
def users_info(request):
    users = User.objects.all()
    total_user = users.count()
    return render(request, "dashboardusers.html", {'users': users, 'total_user': total_user})
