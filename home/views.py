from django.shortcuts import render, redirect
from products.models import Product
from django.db.models import Avg, F


def index(request):
    products = Product.objects.all()
    product_reviews = Product.objects.annotate(avg_rating=Avg('review__rating'),
                                               product_id=F("id"))

    return render(request, "index.html", {"products": products, "product_reviews": product_reviews})


def latest(request):
    """
    Calling all products with category_name of latest
    """
    products = Product.objects.filter(category__name='latest')

    return redirect(request, "latest_carousel.html", {'products': products}).order_by('-date')[:9]


def latest(request):
    """
    Calling all products with category_name of bestsellers
    """
    products = Product.objects.filter(
        category__name='bestsellers').order_by('-date')[:9]

    return redirect(request, "bestsellers_carousel.html", {'products': products})
