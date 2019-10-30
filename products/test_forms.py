from django.test import TestCase
from .forms import ProductForm, CategoryForm
from .models import Category, Product


class Test_Add_Valid_Category(TestCase):
    '''Test add category'''

    def test_to_add_valid_category(self):
        form = CategoryForm({
            'name': 'test category'
        })
        # check the add category form is valid
        self.assertTrue(form.is_valid())


"""
class Test_Add_Valid_Product(TestCase):
    '''Test add product Form'''

    def test_to_add_valid_product(self):

        form = ProductForm({'name': 'product',
                            'description': 'test description',
                            'price': 2,
                            'image': 'img.jpg',
                            'published_date': '2019-10-21 19:47:27.674081',
                            'in_stock': True,
                            'product_category': '',
                            })
        # check the add product form is valid
        self.assertTrue(form.is_valid())
"""
