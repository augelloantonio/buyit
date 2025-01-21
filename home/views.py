from django.shortcuts import render, redirect
from products.models import Product, Category
from django.db.models import Avg, F, Count
from django.utils.translation import get_language
from utils import languageUtils

def index(request):
    products = Product.objects.all()
    product_reviews = products.annotate(avg_rating=Avg('review__rating'),
                                        product_id=F("id"))

    # Make a list of products ordered by added date
    products_latest = products.order_by('-published_date')[:9]

    # Order products by quantity sold
    products_bestsellers = products.order_by('-quantity_sold')
    
    translations = languageUtils.load_translations()
    
    selected_language = request.LANGUAGE_CODE  # Get the current language
    
    return render(request, "index.html", {"products": products, "product_reviews": product_reviews,
                                          'products_latest': products_latest, 'products_bestsellers': products_bestsellers, "translations": translations})


def contact_us(request):
    '''Contact Us view'''
    
    translations = languageUtils.load_translations()

    return render(request, 'contact.html', {'translations', translations})
