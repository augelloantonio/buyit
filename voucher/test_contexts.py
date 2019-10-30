from django.test import TestCase
from decimal import Decimal
from .models import Voucher
from products.models import Product


class TestVoucherContexts(TestCase):
    '''Test voucher context'''

    def test_add_in_session_a_voucher(self):
        # create a voucher
        voucher = Voucher.objects.create(code='test', amount=5)
        voucher.save()

        # assign the voucher code to code variable
        code = voucher.code

        # create a new voucher session
        session = self.client.session
        session['voucher'] = code
        session.save()

        # check if the code in session is the voucher code
        self.assertEqual(session['voucher'], "test")

    def test_total_price_if_code_exist(self):
        ''' Test the total price if code exist'''
        # create a product
        product = Product.objects.create(name='product', price=2)
        product.save()
        # create a total price
        quantity = 2
        total = product.price * quantity

        # create a voucher
        voucher = Voucher.objects.create(code='test', amount=5)
        voucher.save()

        code = voucher.code
        discount = 0

        amount = voucher.amount

        # calculate the quantity to reduce
        if code != None:
            discount = (amount/100)*total

        # subtract the discount from the total
        new_total = total - discount

        self.assertEqual(new_total,  3.8)
