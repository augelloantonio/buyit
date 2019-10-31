from django.apps import apps
from django.test import TestCase
from .apps import SearchConfig


class SearchConfig(TestCase):

    def test_app(self):
        self.assertEqual("search", apps.get_app_config("search").name)
