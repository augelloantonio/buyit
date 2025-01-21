from django.shortcuts import render
from products.models import Product
from utils import languageUtils

# Create your views here.

def do_search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query)
    
    translations = languageUtils.load_translations()
    return render(request, 'search_product.html', {'products': products, 'query':query, 'translations':translations})