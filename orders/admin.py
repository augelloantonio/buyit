from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineAdminInline(admin.ModelAdmin):
    model = OrderLineItem    
    list_display = ('product', 'order', 'date', 'user', 'total')
    list_filter = ['date', 'user', 'order']
    search_fields = ['order', 'user']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'voucher', 'order_status')
    list_filter = ['date', 'order_status']
    search_fields = ['orderlineitem__product__name']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLineItem, OrderLineAdminInline)


