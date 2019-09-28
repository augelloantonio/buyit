from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.


def all_products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, "products.html", {"products": products})


def product_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, "productdetail.html", {'product': product})

    def create_or_edit_product(request, pk=None):
        """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    product = get_object_or_404(Product, pk=pk) if pk else None
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect(product_detail, product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'productform.html', {'form': form})
