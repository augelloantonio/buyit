from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Product, Category
from .forms import ProductForm
from reviews.models import Review
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import get_object_or_404

class TestAllProductsViews(TestCase):
    '''Test all the products page'''

    def test_get_all_products_page(self):
        '''Test view al products page'''

        page = self.client.get("/products/", follow=True)

        # check page status
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_get_product_by_category_if_category(self):
        '''Test get products by category if category exist'''
        category = Category.objects.create(name='category')
        id = category.id
        product = Product.objects.create(name='test product', price='2')
        product.product_category_id = id
        product.save()

        page = self.client.get(
            "/products/{0}/".format(id), follow=True)
        # check page status
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_get_product_by_category_if_no_category(self):
        '''Test to check if products are displayed if not category'''

        product = Product.objects.create(name='test product', price='2')

        # Get page with id that not exist
        page = self.client.get(
            "/products/5/", follow=True)
        # check page status
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")


class TestProductPageViews(TestCase):
    '''Test the product page'''

    def test_get_product_detail(self):
        '''Test get the requested product page'''

        # Create a product
        product = Product.objects.create(name='test product', price='2')

        page = self.client.get(
            "/products/{0}".format(product.id))

        # check the page status
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "productdetail.html")


class TestProductInAdminDashboard(TestCase):
    '''test the product function admin dashboard'''

    def test_get_add_product(self):
        '''Test get add product page'''

        # create a user
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)
        # login the user
        self.client.login(username='username',
                          password='password',)

        page = self.client.get("/dashboard/dashboardaddproduct", follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "dashboardaddproduct.html")

    def test_add_a_product_invalid_form(self):
        ''' test add a product with invalid form'''

        # create a seuperuser
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)
        # login the user
        self.client.login(username='username',
                          password='password')

        # add a product and post it
        page = self.client.post("/dashboard/dashboardaddproduct",
                                {'name': '',
                                 'description': 'test description',
                                 'price': 2.00,
                                 'in_stock': True,
                                 },
                                follow = True)
        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        # check that the page used is dashboardaddproduct.html
        self.assertTemplateUsed(page, "dashboardaddproduct.html")

    def test_get_page_edit_a_product(self):
        '''Test edit a product'''
        # create a user
        user=User.objects.create_user(username = 'username',
                                        password = 'password',
                                        is_superuser = True)
        # login user
        self.client.login(username = 'username',
                          password='password')

        # create a product
        product = Product(name='name',
                          price='4')
        # save the product
        product.save()
        # edit product with product id url
        page = self.client.get("/dashboard/dashboardeditproduct/{0}".format(product.id),
                               follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used dashboardaddreview.html
        self.assertTemplateUsed(page, "dashboardaddproduct.html")

    def test_edit_product_form_with_valid_form(self):
        ''' test edit a product with valid form'''

        # create a seuperuser
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)
        # login the user
        self.client.login(username='username',
                          password='password')

        # create a product
        product = Product(name='test product',
                          description='product description',
                          price='5.99',
                          image='img.jpg',
                          in_stock=True,
                          )
        product.save()
        id = product.id

        # add a product and post it
        page = self.client.post("/dashboard/dashboardeditproduct/{0}".format(id),
                                {'name': 'new name',
                                 'description': 'product description',
                                 'price': '5.99',
                                 'image': 'img.jpg',
                                 'in_stock': 'True',
                                 },
                                follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)

        # get the new product and check if the new name is the same of the product in database
        product = get_object_or_404(Product, pk=id)
        self.assertEqual("new name", product.name)

    def test_edit_product_form_with_not_valid_form(self):
        ''' test edit a product with invalid form'''

        # create a seuperuser
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)
        # login the user
        self.client.login(username='username',
                          password='password')

        # create a product
        product = Product(name='test product',
                          description='product description',
                          price='5.99',
                          image='img.jpg',
                          in_stock=True,
                          )
        product.save()
        id = product.id

        # add a product and post it
        page = self.client.post("/dashboard/dashboardeditproduct/{0}".format(id),
                                {'name': '',
                                 'description': 'product description',
                                 'price': '5.99',
                                 'image': 'img.jpg',
                                 'in_stock': 'True',
                                 },
                                follow=True)

        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "dashboardaddproduct.html")

    def test_confirm_delete_a_product_view(self):
        ''' test confirm delete a product view'''

        # create a seuperuser
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)
        # login the user
        self.client.login(username='username',
                          password='password')

        # create a product
        product = Product(name='test product',
                          price='5.99',
                          )
        product.save()
        id = product.id

        # delete product
        page = self.client.get(
            "/dashboard/dashboardproducts/confirmdeleteproduct/{0}".format(id), follow=True)
        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "confirmdeleteproduct.html")

    def test_delete_product(self):
        ''' test delete a product'''

        # create a seuperuser
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)
        # login the user
        self.client.login(username='username',
                          password='password')

        # create a product and save it
        product = Product(name='test product',
                          price='5.99',
                          )
        product.save()
        id = product.id

        # delete the product
        page = self.client.get(
            "/products/deleteproduct/{0}".format(id), follow=True)
        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        # Check the page after deleting a product is the dashboard product
        self.assertTemplateUsed(page, "dashboardproducts.html")


class ToggleProductStockStatus(TestCase):
    ''' Test toggle stock status'''

    def test_toggle_status_valid_form(self):
        ''' test toggle product stock status with valid input'''

        # create a seuperuser
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)
        # login the user
        self.client.login(username='username',
                          password='password')

        # create a product and save it
        product = Product(name='test product',
                          price='5.99',
                          in_stock=True
                          )
        product.save()
        id = product.id

        # delete the product
        page = self.client.post(
            "/dashboard/toggle_status/{0}".format(id), {'name': 'test product',
                                                        'price': '5.99',
                                                        'in_stock': False}, follow=True)
        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        # Check the page after deleting a product is the dashboard product
        self.assertTemplateUsed(page, "dashboardproducts.html")
        product = get_object_or_404(Product, pk=id)
        self.assertEqual(product.in_stock, False)

    def test_toggle_status_invalid_valid_form(self):
        ''' test toggle product stock status with invalid input'''

        # create a seuperuser
        user = User.objects.create_user(username='username',
                                        password='password',
                                        is_superuser=True)
        # login the user
        self.client.login(username='username',
                          password='password')

        # create a product and save it
        product = Product(name='test product',
                          price='5.99',
                          in_stock=True
                          )
        product.save()
        id = product.id

        # delete the product
        page = self.client.post(
            "/dashboard/toggle_status/{0}".format(id), {'name': '',
                                                        'price': '5.99',
                                                        'in_stock': ''}, follow=True)
        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        # Check the page after deleting a product is the dashboard product
        self.assertTemplateUsed(page, "dashboardproducts.html")
        product = get_object_or_404(Product, pk=id)
        self.assertEqual(product.in_stock, False)
