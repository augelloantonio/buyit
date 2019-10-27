from django.db.models import Avg, F, Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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

    # pagination
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    pagination_products = paginator.get_page(page)

    return render(request, "products.html", {'pagination_products': pagination_products, "products": products, "product_reviews": product_reviews,
                                             'categories': categories})


def products_by_category(request, category_id=None):
    product = Product.objects.all()
    product_reviews = product.annotate(avg_rating=Avg('review__rating'),
                                       product_id=F("id"))
    reviews = Review.objects.all()
    categories = Category.objects.all()
    product_category = categories.filter(id=category_id)

    if not product_category:
        products = product.all()
        paginator = Paginator(products, 12)
        page = request.GET.get('page')
        pagination_products = paginator.get_page(page)
    else:
        print('category id')
        products = product.filter(product_category=category_id)
        # pagination
        paginator = Paginator(products, 12)
        page = request.GET.get('page')
        pagination_products = paginator.get_page(page)

    return render(request, "products.html", {'pagination_products': pagination_products, "products": products, "product_reviews": product_reviews,
                                             'categories': categories, 'product_category': product_category})


def product_detail(request, pk):
    """
    Product views
    """
    product = get_object_or_404(Product, pk=pk)
    product_reviews = Product.objects.annotate(avg_rating=Avg('review__rating'),
                                               product_id=F("id"))
    reviews = Review.objects.all()
    review_list = []
    n_reviews = 0

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


@login_required
def edit_a_product(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(dashboard_product)
    else:
        form = ProductForm(instance=product)
    return render(request, "dashboardaddproduct.html", {'form': form})


@login_required
def remove_product(request, pk):
    item = get_object_or_404(Product, pk=pk)
    item.delete()
    return redirect(dashboard_product)


@login_required
def confirm_delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "confirmdeleteproduct.html", {"product": product})


def toggle_status(request, id):
    product = get_object_or_404(Product, id=id)
    product.in_stock = not product.in_stock
    product.save()
    return redirect(dashboard_product)


@login_required
def add_a_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(dashboard_product)
    else:
        form = ProductForm()

    return render(request, "dashboardaddproduct.html", {'form': form})


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
