from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
import datetime
from .forms import ReviewForm
from products.models import Product
from .models import Review


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review.html', {'review': review})


@login_required()
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm(request.POST)
    user = request.user

    if Review.objects.filter(product_id=product, user__username=user):
        messages.warning(request, "We are sorry, but you can't review twice!")
        return HttpResponseRedirect(reverse('product_detail', args=(product.id,)))
    else:
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
