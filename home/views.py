from django.shortcuts import render, redirect
from products.models import Product
from django.db.models import Avg, F

# Create your views here.


def index(request):
    products = Product.objects.all()
    product_reviews = Product.objects.annotate(avg_rating=Avg('review__rating'),
                                               product_id=F("id"))

    return render(request, "index.html", {"products": products, "product_reviews": product_reviews})
