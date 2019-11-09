from django.apps import apps
from django.test import TestCase
from .apps import ApiConfig


class ApiConfig(TestCase):

    def test_app(self):
        self.assertEqual(apps.get_app_config('api').name, 'api')
