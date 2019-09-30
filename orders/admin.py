from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem    


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )
    list_filter = ['date']
    search_fields = ['orderlineitem__product__name']


admin.site.register(Order, OrderAdmin)
