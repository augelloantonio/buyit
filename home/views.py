from django.shortcuts import render
from products.models import Product
from products.views import all_products


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})