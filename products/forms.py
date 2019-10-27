from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image',
                  'published_date', 'in_stock', 'product_category')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', )
