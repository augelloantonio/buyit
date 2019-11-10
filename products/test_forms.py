from django.test import TestCase
from .forms import ProductForm, CategoryForm
from .models import Category, Product
import tempfile
from django.core.files.uploadedfile import SimpleUploadedFile


class Test_Add_Valid_Category(TestCase):
    '''Test add category'''

    def test_to_add_valid_category(self):
        # create category from form
        form = CategoryForm({
            'name': 'test category'
        })
        # check the add category form is valid
        self.assertTrue(form.is_valid())


class Test_Add_Valid_Product(TestCase):
    '''Test add product Form'''

    def test_to_add_valid_product(self):

        # create file data to upload image
        data_file = {'image': SimpleUploadedFile(name='foo.gif',
                                                 content=b'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00ccc,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00'),
                     }

        # create product in the form
        form = ProductForm({'name': 'product',
                            'description': 'test description',
                            'price': 2.00,
                            'in_stock': True,
                            'product_category': '',
                            }, data_file)

        # check the add product form is valid
        self.assertTrue(form.is_valid())
