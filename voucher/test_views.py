from django.test import TestCase
from decimal import Decimal
from django.shortcuts import get_object_or_404
from .models import Voucher
from django.contrib.auth.models import User
from orders.models import Order


class TestInsertVoucherView(TestCase):
    '''Test insert voucher view'''

    def test_add_a_voucher_with_user_logged(self):
        # create a user
        user = User.objects.create_user(username='username',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')

        # create a voucher
        voucher = Voucher.objects.create(code='test', amount=5, active=True)
        voucher.save()

        # create a new voucher session
        session = self.client.session
        session['voucher'] = voucher.id
        session.save()

        # assign the voucher code to code variable
        code = session['voucher']

        # check if the code in session is the voucher code
        self.assertEqual(session['voucher'], 1)
        page = self.client.post("/voucher/", {'code': code},
                                follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")

    def test_voucher_does_not_exist(self):

        # create a user
        user = User.objects.create_user(username='username',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')

        # create a voucher
        voucher = Voucher.objects.create(code='test', amount=5, active=True)
        voucher.save()

        page = self.client.post("/voucher/", {'code': 'some code'},
                                follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")

    def test_add_coupon_user_not_logged(self):

        page = self.client.post("/voucher/", {'code': 'some code'},
                                follow=True)

        # Test that the messages are send
        messages = list(page.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'You must be logged in to add a coupon.')

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")

    def test_user_used_already_coupon(self):
        ''' Test if user has used the voucher code already'''

        # create a user
        user = User.objects.create_user(username='username',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')

        # create a voucher
        voucher = Voucher.objects.create(code='test', amount=5, active=True)
        voucher.save()

        code = voucher.code

        # Create an order
        order = Order(full_name='name',
                      email_address='email@email.com',
                      phone_number='0000',
                      town_or_city='city',
                      street_address1='street sddress 1',
                      street_address2='street sddress 2',
                      country='country',
                      county='county',
                      postcode='postcode')

        # add the user and the code to the order
        order.voucher = code
        order.user_id = user.id
        order.save()

        page = self.client.post("/voucher/", {'code': code},
                                follow=True)

        # Test that the messages are send
        messages = list(page.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Ops, you cannot use this voucher twice.')

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")


class DashboardVoucherView(TestCase):
    '''Test the voucher view in the dashboard'''

    def test_dashboard_voucher_view_for_superuser(self):
        # create a user
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)

        # login the user
        self.client.login(username='username',
                          password='password')

        # get the voucher page
        page = self.client.get("/dashboard/dashboardvouchers", follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "dashboardvouchers.html")

    def test_add_voucher_view(self):
        '''Test the add voucher view'''
        # create a user
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)

        # login the user
        self.client.login(username='username',
                          password='password')

        # get the voucher page
        page = self.client.get("/dashboard/dashboardaddvoucher",
                               follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "dashboardaddavouchercode.html")

    def test_add_voucher(self):
        '''test add voucher post function'''
        # create a user
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)

        # login the user
        self.client.login(username='username',
                          password='password')

        # get the voucher page
        page = self.client.post("/dashboard/dashboardaddvoucher",
                                {'code': 'test code',
                                 'amount': 5,
                                 'active': True},
                                follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "dashboardvouchers.html")

    def test_an_invalid_add_voucher_form(self):
        '''test invalid add form'''
        # create a user
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)

        # login the user
        self.client.login(username='username',
                          password='password')

        # get the voucher page
        page = self.client.post("/dashboard/dashboardaddvoucher",
                                {'code': '',
                                 'amount': 5,
                                 },
                                follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "dashboardaddavouchercode.html")

    def test_get_edit_voucer_page(self):
        ''' test get edit voucher view page'''
        # create a user
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)

        # login the user
        self.client.login(username='username',
                          password='password')

        voucher = Voucher.objects.create(code='test code',
                                         amount=5,
                                         active=True)
        voucher.save()

        # get the voucher page
        page = self.client.post("/dashboard/dashboardeditvoucher/{0}".format(voucher.id),
                                follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "dashboardaddavouchercode.html")

    def test_edit_a_voucher(self):
        '''test edit voucher'''
        # create a user
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)

        # login the user
        self.client.login(username='username',
                          password='password')

        voucher = Voucher.objects.create(code='test code',
                                         amount=5,
                                         active=True)
        voucher.save()
        id = voucher.id

        # get the voucher page
        page = self.client.post("/dashboard/dashboardeditvoucher/{0}".format(id),
                                {'code': 'new test code',
                                 'amount': 5,
                                 'active': True},
                                follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "dashboardvouchers.html")

        voucher = get_object_or_404(Voucher, pk=id)
        # check if voucher was edited
        self.assertEqual(voucher.code, 'new test code')

    def test_delete_voucher(self):
        '''test delete voucher'''
        # create a user
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)

        # login the user
        self.client.login(username='username',
                          password='password')

        voucher = Voucher.objects.create(code='test code',
                                         amount=5,
                                         active=True)
        voucher.save()
        id = voucher.id

        # get the voucher page
        page = self.client.post("/voucher/deletevoucher/{0}".format(id),
                                follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "dashboardvouchers.html")
