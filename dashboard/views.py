from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from orders.models import OrderLineItem, Order


@login_required
def dashboard(request):
    orders = Order.objects.all()
    return render(request, "dashboard.html", {"orders": orders})

@login_required
def dashboard_orders(request):
    orders = Order.objects.all()
    return render(request, "dashboardorders.html", {"orders": orders})

