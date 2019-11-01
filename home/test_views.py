from django.test import TestCase
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from products.models import Product


class TestHomeView(TestCase):
    '''Test home views'''

    def test_get_home_views_with_logged_user(self):
        '''Test home page view with logged user'''
        # create a user
        user = User.objects.create_user(username='username',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')

        page = self.client.get("/home", follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_get_home_views_with_no_logged_user(self):
        '''Test home page view with no logged user'''
        page = self.client.get("/home", follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
