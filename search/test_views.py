from django.apps import apps
from django.test import TestCase
from products.models import Product


class TestSearchView(TestCase):
    '''Test the search view'''

    def test_do_search_view_with_not_existing_query(self):
        '''test the search view'''
        page = self.client.get("/search/", {'q': 'q'}, follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "search_product.html")

    def test_do_search_view_with_existing_query(self):
        '''test the search view'''
        # create a product
        # create product
        product = Product.objects.create(name='product', price='2')
        query = 'product'
        page = self.client.get("/search/", {'q': query}, follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "search_product.html")
