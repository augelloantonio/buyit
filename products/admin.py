from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'product_category', 'in_stock')
    list_filter = ['name', 'product_category', 'published_date', 'in_stock']
    search_fields = ['name', 'product_category']


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
