from django.apps import apps
from django.test import TestCase
from .apps import CheckoutConfig


class CheckoutConfig(TestCase):

    def test_app(self):
        self.assertEqual("orders", apps.get_app_config("orders").name)
