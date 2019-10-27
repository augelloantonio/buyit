from django.test import TestCase
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User, AnonymousUser
from products.models import Product
from .models import Review
from .forms import ReviewForm


class TestPostReviewView(TestCase):
    ''' Test Add A review With Post method '''

    def test_post_review_(self):
        ''' test post a review'''

        # create a user
        user = User.objects.create_user(username='username',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')

        # create product
        product = Product.objects.create(name='product', price='2')
        id = product.id

        # add a review and post it
        page = self.client.post(
            "/review/addreview/product/{0}".format(id),
            {'review_summary': 'summary',
             'rating': '4',
             'pub_date': '2019-10-21 19:47:27.674081',
             'comment': 'test comment'},
            follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "productdetail.html")


class TestGetAddReviewView(TestCase):
    ''' Test Get Add Review Page '''

    def test_get_page_add_review_if_user_is_logged(self):
        '''Test get the page Add Review if user is logged'''

        # create product
        product = Product.objects.create(name='product', price='2')
        id = product.id

        # create a user
        user = User.objects.create_user(username='username',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')

        # Get the add review page
        page = self.client.get(
            "/review/addreview/product/{0}".format(id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "addreview.html")


class TestUserAlreadyReviewedAProduct(TestCase):
    '''Test if a user already reviewed a product'''

    def test_add_new_review_if_review_with_same_user_exist_already(self):
        # create a user
        user = User.objects.create_user(username='username',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')

        product = Product.objects.create(name='test product', price='2')
        # Create a review
        review = Review(
            rating='4',
            review_summary='testing summary',
            pub_date='2019-10-21 19:47:27.674081',
            comment='test comment'
        )

        # Assign product id to the review
        review.product_id = product.id
        # Assign user id to the review
        review.user_id = user.id
        # Save review
        review.save()

        page = self.client.get(
            "/review/addreview/product/{0}".format(product.id), follow=True)
        # Test that the user is redirect back to the product page
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "productdetail.html")
