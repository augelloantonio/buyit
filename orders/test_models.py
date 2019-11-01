
from django.test import TestCase
from django.contrib.auth.models import User
from orders.models import Order

'''
class TestCheckoutView(TestCase):
    Test Checkout views

    def test_get_checkout_page(self):

        #  create a user
        user = User.objects.create_user(username='username',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')
'''


"""
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
        """
