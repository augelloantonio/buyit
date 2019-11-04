from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product
from django.shortcuts import get_object_or_404


class TestDashboardView(TestCase):
    '''Test dashboard View'''

    def test_view_dashboard_home(self):
        '''Test dashboard home view'''
        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)

        # login the user
        self.client.login(username='username',
                          password='password')

        page = self.client.get("/dashboard/", follow=True)

        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is checkout.html page
        self.assertTemplateUsed(page, "dashboard.html")

    def test_view_dashboard_orders(self):
        '''Test dashboard orders view'''
        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)

        # login the user
        self.client.login(username='username',
                          password='password')

        page = self.client.get("/dashboard/dashboardorders", follow=True)

        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is checkout.html page
        self.assertTemplateUsed(page, "dashboardorders.html")

    def test_view_dashboard_products(self):
        '''Test dashboard products view'''
        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)

        # login the user
        self.client.login(username='username',
                          password='password')

        page = self.client.get("/dashboard/dashboardproducts", follow=True)

        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is checkout.html page
        self.assertTemplateUsed(page, "dashboardproducts.html")

    def test_view_dashboard_users(self):
        '''Test dashboard users view'''
        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)

        # login the user
        self.client.login(username='username',
                          password='password')

        page = self.client.get("/dashboard/dashboardusers", follow=True)

        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is checkout.html page
        self.assertTemplateUsed(page, "dashboardusers.html")

    def test_view_dashboard_add_a_product(self):
        '''Test dashboard add a product view'''
        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)

        # login the user
        self.client.login(username='username',
                          password='password')

        page = self.client.get("/dashboard/dashboardaddproduct", follow=True)

        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is checkout.html page
        self.assertTemplateUsed(page, "dashboardaddproduct.html")

    def test_view_dashboard_add_a_category(self):
        '''Test dashboard add a category view'''
        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)

        # login the user
        self.client.login(username='username',
                          password='password')

        page = self.client.get("/dashboard/dashboardaddcategory", follow=True)

        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is checkout.html page
        self.assertTemplateUsed(page, "dashboardaddcategory.html")

    def test_view_dashboard_add_a_voucher(self):
        '''Test dashboard add a voucher view'''
        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)

        # login the user
        self.client.login(username='username',
                          password='password')

        page = self.client.get("/dashboard/dashboardaddvoucher", follow=True)

        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is checkout.html page
        self.assertTemplateUsed(page, "dashboardaddavouchercode.html")


class TestAddCategory(TestCase):
    '''Test Adding a category'''

    def test_add_a_category(self):
        '''Test add a category'''
        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)

        # login the user
        self.client.login(username='username',
                          password='password')

        page = self.client.post("/dashboard/dashboardaddcategory", {'name':'category'}, follow=True)

        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is checkout.html page
        self.assertTemplateUsed(page, "dashboardproducts.html")
