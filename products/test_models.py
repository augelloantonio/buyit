from django.test import TestCase
from .models import Category, Product
from django.utils import timezone


class Test_Category_model(TestCase):
    '''Test Category Model'''

    def test_category_model(self):
        # Create category
        category = Category(name='test_category')
        # Save category
        category.save()
        # check to see that the product fields equal the saved products values
        self.assertEqual(category.name, "test_category")

    def test_category_as_string(self):
        category = Category(name='test')
        category.save()
        self.assertEqual('test', str(category))


class TestProductModel(TestCase):
    ''' test the Product Model '''

    def test_product_model(self):
        ''' test the product model is working '''

        # create a category
        category = Category.objects.create(name='category')
        # create a product
        product = Product(name='test product',
                          description='test description',
                          price='24.00',
                          image='img.jpg',
                          published_date='2019-10-15 12:50:09',
                          in_stock='True',
                          quantity_sold='2')
        # save product
        product.category_id = category.id
        product.save()
        # check to see that the product fields equal the saved products values
        self.assertEqual(product.name, "test product")
        self.assertEqual(product.description, "test description")
        self.assertEqual(product.price, "24.00")
        self.assertEqual(product.image, "img.jpg")
        self.assertEqual(product.published_date, "2019-10-15 12:50:09")
        self.assertEqual(product.in_stock, "True")
        self.assertEqual(product.quantity_sold, "2")
        self.assertEqual(product.category_id, 1)
