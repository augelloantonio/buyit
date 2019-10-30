from django.apps import apps
from django.test import TestCase
from .apps import VoucherConfig


class VoucherConfig(TestCase):

    def test_app(self):
        self.assertEqual(apps.get_app_config('voucher').name, 'voucher')
