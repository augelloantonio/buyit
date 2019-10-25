import django_filters
from orders.models import OrderLineItem, Order

class OrdersFilter(django_filters.FilterSet):
    
    class Meta:
        model = OrderLineItem
        fields = {'order__date', 'order__id', 'order__order_status'}