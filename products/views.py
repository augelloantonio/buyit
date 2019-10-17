from django.db.models import Avg, F
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import ProductForm
from home.views import index
from dashboard.views import dashboard_product
from reviews.models import Review
from django.core.paginator import Paginator


def all_products(request, category_id=None):

    categories = Category.objects.all()

    product_reviews = Product.objects.annotate(avg_rating=Avg('review__rating'),
                                               product_id=F("id"))
    reviews = Review.objects.all()
    products = Product.objects.all()

    return render(request, "products.html", {"products": products, "product_reviews": product_reviews,
                                             'categories': categories})


def products_by_category(request, category_id=None):

    product_reviews = Product.objects.annotate(avg_rating=Avg('review__rating'),
                                               product_id=F("id"))
    reviews = Review.objects.all()
    categories = Category.objects.all()

    if not category_id:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(product_category=category_id)

    return render(request, "products.html", {"products": products, "product_reviews": product_reviews,
                                             'categories': categories})


def product_detail(request, pk):
    """
    Product view
    """
    product = get_object_or_404(Product, pk=pk)
    product_reviews = Product.objects.annotate(avg_rating=Avg('review__rating'),
                                               product_id=F("id"))
    reviews = Review.objects.all()
    review_list = []

    for review in reviews:
        review_list = Review.objects.all().order_by(
            '-pub_date').filter(product__id=product.pk)
        n_reviews = review_list.count()

    # pagination
    paginator = Paginator(review_list, 6)
    page = request.GET.get('page')
    pagination_reviews = paginator.get_page(page)

    return render(request, "productdetail.html", {'product': product, 'reviews': reviews,
                                                  'review_list': review_list, 'product_reviews': product_reviews,
                                                  'n_reviews': n_reviews, 'pagination_reviews': pagination_reviews})


def edit_product(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(product_detail)
    else:
        form = ItemForm(instance=item)
    return render(request, "item_form.html", {'form': form})


def remove_product(request, pk):
    item = get_object_or_404(Product, pk=pk)
    item.delete()
    return redirect(dashboard_product)


def toggle_status(request, id):
    product = get_object_or_404(Product, id=id)
    product.in_stock = not product.in_stock
    product.save()
    return redirect(dashboard_product)


def product_avg_rating(request, id):
    product = get_object_or_404(Product, id=id)
    reviews = Review.objects.all()
    rating_list = list()
    if review_list:
        for review in reviews:
            rating_list = review["rating"]
        return rating_list
    for num in rating_list:
        sum = num + num
    rating_avg = sum/len(review_list)
    print(rating_avg)
    return render({"rating_avg": rating_avg})
