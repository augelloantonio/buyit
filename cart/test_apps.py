from django.apps import apps
from django.test import TestCase
from .apps import CartConfig


class TestCartApp(TestCase):
    ''' test the app name is cart '''

    def test_app(self):
        self.assertEqual("cart", CartConfig.name)