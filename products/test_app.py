from django.apps import apps
from django.test import TestCase
from .apps import ProductsConfig, CategoryConfig


class TestProductConfig(TestCase):

    def test_app(self):
        self.assertEqual("products", ProductsConfig.name)
        self.assertEqual("products", apps.get_app_config("products").name)


class TestCategoryConfig(TestCase):

    def test_app(self):
        self.assertEqual("category", CategoryConfig.name)
        self.assertEqual("products", apps.get_app_config("products").name)
