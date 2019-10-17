from django.shortcuts import render, redirect
from products.models import Product, Category
from django.db.models import Avg, F, Count


def index(request):
    products = Product.objects.all()
    product_reviews = Product.objects.annotate(avg_rating=Avg('review__rating'),
                                               product_id=F("id"))

    # Made a list of product with category latest
    category_id_latest = Category.objects.get(id=1)
    products_latest = Product.objects.filter(
        product_category=category_id_latest).order_by('-published_date')[:9]

    # Made a list of product with category bestsellers

    products_bestsellers = products.order_by('-quantity_sold')


    return render(request, "index.html", {"products": products, "product_reviews": product_reviews,
                                          'products_latest': products_latest, 'products_bestsellers': products_bestsellers})
