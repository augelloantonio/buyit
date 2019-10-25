from django.shortcuts import render
from products.models import Product

# Create your views here.

def do_search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'search_product.html', {'products': products, 'query':query})