from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from products.models import Product
from .models import Review
import datetime


def review_list(request):
    reviews = Review.objects.all()
    product = Product.objects.all()
    for review in reviews:
        if review.product_id == product.id:
            review_list = Review.objects.all().order_by('-pub_date')[:9]
    return ({"review_list": review_list})


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = request.user
        review = Review()
        review.product_id = product.id
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        return HttpResponseRedirect(reverse('product_detail', args=(product.id,)))

    return render(request, "addreview.html", {'form': form, 'product': product})
