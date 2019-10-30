from django.test import TestCase
from .models import Voucher


class Test_Voucher_model(TestCase):
    '''Test Voucher Model'''

    def test_review_model(self):
        # Create review
        voucher = Voucher(
            code='test',
            active=True,
            amount=5
        )

        voucher.save()
        # check to see that the review summary equal the saved review value
        self.assertEqual(voucher.code, "test")
        self.assertEqual(voucher.active, True)
        self.assertEqual(voucher.amount, 5)

        ''' Test review as string'''
        self.assertEqual('test', str(voucher))
