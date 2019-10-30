from django.test import TestCase
from .forms import AddNewVoucher


class TestAddNewVoucher(TestCase):
    '''Test add a new voucher form'''

    def test_add_valid_voucher(self):
        form = AddNewVoucher({
            'code': 'test',
            'amount': 5,
            'active': 'True',
        })
        # check the add form form is valid
        self.assertTrue(form.is_valid())
