
from django.test import TestCase
from django.conf import settings
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
        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')

        # create an item
        item = Product.objects.create(name='product', price='2')

        # get the stripe publisable key
        stripe_id = settings.STRIPE_PUBLISHABLE

        page = self.client.post("/order/",
                                {'full_name': 'name',
                                 'phone_number': '000',
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

        # check the page status is ok
        self.assertEqual(page.status_code, 200)
        # check Template Used is cart.html page
        self.assertTemplateUsed(page, "profile.html")

    def test_get_voucher_in_checkout_view(self):

        #  create a user
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
        session['voucher_id'] = voucher.id
        session.save()

        voucher_id = session['voucher_id']

        code = voucher_id

        page = self.client.get("/order/", {'code': code},
                               follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")


'''
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
        order.user_id = user.id
        order.save()
        '''
