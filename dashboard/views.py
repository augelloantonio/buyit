from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from orders.models import OrderLineItem, Order
from products.models import Product


@login_required
def dashboard(request):
    orders = Order.objects.all()
    return render(request, "dashboard.html", {"orders": orders})


@login_required
def dashboard_orders(request):
    orders = Order.objects.all()
    order_info = OrderLineItem.objects.all()
    product = Product.objects.all()
    
    return render(request, "dashboardorders.html", {"order_info": order_info, "orders": orders, 'product':product})

@login_required
def dashboard_order_details(request, id):
    orders = Order.objects.all()
    order_info = OrderLineItem.objects.all()
    order = get_object_or_404(Order, id=id)
    
    return render(request, "dashboardordersdetails.html", {"order_info": order_info, "orders": orders, 'order':order})
