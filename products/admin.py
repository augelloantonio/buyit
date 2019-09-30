from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'category', 'in_stock')
    list_filter = ['name', 'category', 'published_date', 'in_stock']
    search_fields = ['name', 'category']
    

admin.site.register(Product, ProductAdmin)