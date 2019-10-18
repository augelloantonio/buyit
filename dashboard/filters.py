import django_filters
from orders.models import OrderLineItem, Order

class OrdersFilter(django_filters.FilterSet):
    
    class Meta:
        model = Order
        fields = {'date', 'id', 'order_status'}