
from django.test import TestCase
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from orders.models import Order
from voucher.models import Voucher
from products.models import Product

class TestCheckoutView(TestCase):
    '''Test Checkout views'''

    def test_get_checkout_page(self):

        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')

        # checkout url
        page = self.client.get("/order/", follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is checkout.html page
        self.assertTemplateUsed(page, "checkout.html")

    def test_post_valid_order(self):
        '''Test a valid order'''
        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')

        # create an item
        item = Product.objects.create(name='product', price='2')

        # add item to cart
        self.client.post("/cart/add/{0}".format(item.id),
                         data={'quantity': '2'},
                         follow=True)

        # get the stripe publisable key
        stripe_id = 'tok_visa'

        # send the order
        page = self.client.post("/order/",
                                {'full_name': 'name',
                                 'phone_number': '000',
                                 'email_address': 'test@test.com',
                                 'street_address1': 'address 1',
                                 'street_address2': 'address 2',
                                 'town_or_city': 'city',
                                 'county': 'county',
                                 'country': 'country',
                                 'postcode': 'code13',
                                 'credit_card_number': '4242424242424242',
                                 'cvv': '123',
                                 'expiry_month': '2',
                                 'expiry_year': '2022',
                                 'stripe_id': stripe_id},
                                follow=True)
        messages = list(page.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'You have successfully paid. Your order will be processed soon.')

        # check the page status is ok
        self.assertEqual(page.status_code, 200)
        # check Template Used is cart.html page
        self.assertTemplateUsed(page, "profile.html")

    def test_post_valid_order_with_wrong_card(self):
        ''' Test order where card is not valid'''
        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')

        # create an item
        item = Product.objects.create(name='product', price='2')

        self.client.post("/cart/add/{0}".format(item.id),
                         data={'quantity': '2'},
                         follow=True)

        # get the stripe publisable key
        stripe_id = 'tok_chargeDeclined'

        page = self.client.post("/order/",
                                {'full_name': 'name',
                                 'phone_number': '000',
                                 'email_address': 'test@test.com',
                                 'street_address1': 'address 1',
                                 'street_address2': 'address 2',
                                 'town_or_city': 'city',
                                 'county': 'county',
                                 'country': 'country',
                                 'postcode': 'code13',
                                 'credit_card_number': '4000000000000002',
                                 'cvv': '123',
                                 'expiry_month': '2',
                                 'expiry_year': '2022',
                                 'stripe_id': stripe_id},
                                follow=True)

        # Test that the messages are send
        messages = list(page.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Your card was declined! Pleace check that the payment details are correct and try again.')

        # check the page status is ok
        self.assertEqual(page.status_code, 200)
        # check Template Used is cart.html page
        self.assertTemplateUsed(page, "checkout.html")

    def test_post_valid_order_with_validation_form_invalid(self):
        ''' Test order where validation form is invalid '''
        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')

        # create an item
        item = Product.objects.create(name='product', price='2')

        self.client.post("/cart/add/{0}".format(item.id),
                         data={'quantity': '2'},
                         follow=True)

        # get the stripe publisable key
        stripe_id = 'tok_visa'

        page = self.client.post("/order/",
                                {'full_name': '',
                                 'phone_number': '',
                                 'email_address': 'test@test.com',
                                 'street_address1': 'address 1',
                                 'street_address2': 'address 2',
                                 'town_or_city': 'city',
                                 'county': 'county',
                                 'country': 'country',
                                 'postcode': 'code13',
                                 'credit_card_number': '4000000000000002',
                                 'cvv': '123',
                                 'expiry_month': '4',
                                 'expiry_year': '2023',
                                 'stripe_id': stripe_id},
                                follow=True)

        # Test that the messages are send
        messages = list(page.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Ops, something went wrong, check that all the info are correct.')

        # check the page status is ok
        self.assertEqual(page.status_code, 200)
        # check Template Used is cart.html page
        self.assertTemplateUsed(page, "checkout.html")

    def test_post_valid_order_with_coupon_code(self):
        ''' Test order having a coupon code'''
        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')

        # create an item
        item = Product.objects.create(name='product', price='2')

        self.client.post("/cart/add/{0}".format(item.id),
                         data={'quantity': '2'},
                         follow=True)

        # create a voucher
        voucher = Voucher.objects.create(code='test', amount=5, active=True)
        voucher.save()

        # assign the voucher code to code variable
        voucher_id = voucher.id

        # create a new voucher session
        session = self.client.session
        session['voucher_id'] = voucher_id
        session.save()

        code = voucher.code

        # get the stripe publisable key
        stripe_id = 'tok_visa'

        page = self.client.post("/order/",
                                {'full_name': 'name',
                                 'phone_number': '000',
                                 'email_address': 'test@test.com',
                                 'street_address1': 'address 1',
                                 'street_address2': 'address 2',
                                 'town_or_city': 'city',
                                 'county': 'county',
                                 'country': 'country',
                                 'postcode': 'code13',
                                 'credit_card_number': '4242 4242 4242 4242',
                                 'cvv': '123',
                                 'expiry_month': '4',
                                 'expiry_year': '2023',
                                 'stripe_id': stripe_id,
                                 'code': code},
                                follow=True)

        # check the page status is ok
        self.assertEqual(page.status_code, 200)
        # check Template Used is cart.html page
        self.assertTemplateUsed(page, "profile.html")
        # Test that the code exist
        self.assertEqual(code, 'test')

    def test_post_valid_order_withoout_voucher(self):
        ''' Test order where voucher does not exist'''
        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')

        # create an item
        item = Product.objects.create(name='product', price='2')

        self.client.post("/cart/add/{0}".format(item.id),
                         data={'quantity': '2'},
                         follow=True)

        # create a voucher
        voucher = Voucher.objects.create(code='test', amount=5, active=True)
        voucher.save()

        # assign the voucher code to code variable
        voucher_id = None

        # create a new voucher session
        session = self.client.session
        session['voucher_id'] = voucher_id
        session.save()

        code = session['voucher_id']

        # get the stripe publisable key
        stripe_id = 'tok_visa'
        stripe.secret = settings.STRIPE_SECRET

        page = self.client.post("/order/",
                                {'full_name': 'name',
                                 'phone_number': '000',
                                 'email_address': 'test@test.com',
                                 'street_address1': 'address 1',
                                 'street_address2': 'address 2',
                                 'town_or_city': 'city',
                                 'county': 'county',
                                 'country': 'country',
                                 'postcode': 'code13',
                                 'credit_card_number': '4242 4242 4242 4242',
                                 'cvv': '123',
                                 'expiry_month': '4',
                                 'expiry_year': '2023',
                                 'stripe_id': stripe_id,
                                 },
                                follow=True)

        # check the page status is ok
        self.assertEqual(page.status_code, 200)
        # check Template Used is cart.html page
        self.assertTemplateUsed(page, "profile.html")
        # Test that the code exist
        self.assertEqual(code, None)

    def test_order_with_free_delivery(self):
        ''' Test that the delivery are free if item price grather than 50'''
        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')

        # create an item
        item = Product.objects.create(name='product', price='50')

        self.client.post("/cart/add/{0}".format(item.id),
                         data={'quantity': '1'},
                         follow=True)

        # get the stripe publisable key
        stripe_id = 'tok_visa'

        page = self.client.post("/order/",
                                {'full_name': 'name',
                                 'phone_number': '000',
                                 'email_address': 'test@test.com',
                                 'street_address1': 'address 1',
                                 'street_address2': 'address 2',
                                 'town_or_city': 'city',
                                 'county': 'county',
                                 'country': 'country',
                                 'postcode': 'code13',
                                 'credit_card_number': '4242 4242 4242 4242',
                                 'cvv': '123',
                                 'expiry_month': '4',
                                 'expiry_year': '2023',
                                 'stripe_id': stripe_id},
                                follow=True)

        # check the page status is ok
        self.assertEqual(page.status_code, 200)
        # check Template Used is cart.html page
        self.assertTemplateUsed(page, "profile.html")

class OrderDashboardChangeStatus(TestCase):
    '''Test change order status'''

    def test_change_order_status(self):
        '''Test change order status '''

        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)

        # login the user
        self.client.login(username='username',
                        password='password')

        # Create an order
        order = Order(full_name='name',
                        email_address='email@email.com',
                        phone_number='0000',
                        town_or_city='city',
                        street_address1='street sddress 1',
                        street_address2='street sddress 2',
                        country='country',
                        county='county',
                        postcode='postcode',
                        order_status='Order Received')

        # add the user and the code to the order
        order.user_id = user.id
        order.save()

        id = order.id

        page = self.client.post("/dashboard/changeorderstatus/{0}".format(id),
                             {'order_status': 'Delivered'}, follow=True)

        # check the page status is ok
        self.assertEqual(page.status_code, 200)
        # check Template Used is cart.html page
        self.assertTemplateUsed(page, "dashboardordersdetails.html")
        order = get_object_or_404(Order, pk=id)
        self.assertEqual(order.order_status, 'Delivered')
