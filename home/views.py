from django.shortcuts import render, redirect
from products.models import Product, Category
from django.db.models import Avg, F, Count


def index(request):
    products = Product.objects.all()
    product_reviews = products.annotate(avg_rating=Avg('review__rating'),
                                        product_id=F("id"))

    # Make a list of products ordered by added date
    products_latest = products.order_by('-published_date')[:9]

    # Order products by quantity sold
    products_bestsellers = products.order_by('-quantity_sold')

    return render(request, "index.html", {"products": products, "product_reviews": product_reviews,
                                          'products_latest': products_latest, 'products_bestsellers': products_bestsellers})
   