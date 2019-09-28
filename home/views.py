from django.shortcuts import render, redirect
from products.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})