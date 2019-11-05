from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product


class TestCartView(TestCase):
    '''Test cart View'''

    def test_view_cart(self):
        '''Test cart rendering page'''
        page = self.client.get("/cart/", follow=True)

        self.assertEqual(page.status_code, 200)
        # check Template Used is checkout.html page
        self.assertTemplateUsed(page, "cart.html")

    def test_add_to_cart_view(self):
        ''' test add to cart '''

        # create a Product
        item = Product(name="Product", price=2)
        # save the product
        item.save()

        # post product and quantity to cart
        page = self.client.post("/cart/add/{0}".format(item.id),
                                data={'quantity': 2},
                                follow=True)

        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is products.html
        self.assertTemplateUsed(page, "index.html")

    def test_add_to_cart_when_product_is_already_in_the_cart(self):
        ''' test add to cart when the product
        is already in the cart '''

        # create a Product
        item = Product(name="Product", price=2)
        # save the product
        item.save()

        # post product and quantity to cart
        page = self.client.post("/cart/add/{0}".format(item.id),
                                data={'quantity': '2'},
                                follow=True)

        # post same product and quantity to cart
        page = self.client.post("/cart/add/{0}".format(item.id),
                                data={'quantity': '1'},
                                follow=True)

        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is products.html
        self.assertTemplateUsed(page, "index.html")

    def test_adjust_cart_view(self):
        ''' test adjusting the quantity in the cart '''

        # create an item
        item = Product(name="Product", price=2)

        # save the item
        item.save()
        # post the product id and ammended quantity
        page = self.client.post("/cart/adjust/{0}".format(item.id),
                                data={"quantity": 4},
                                follow=True)

        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        #  # check Template Used is cart.html page
        self.assertTemplateUsed(page, "cart.html")

    def test_remove_item_from_cart_if_quantity_is_zero(self):
        ''' test adjusting the quantity in the cart '''

        # create an item
        item = Product(name="Product", price=2)

        # save the item
        item.save()
        # post the product id and ammended quantity
        page = self.client.post("/cart/adjust/{0}".format(item.id),
                                data={"quantity": 2},
                                follow=True)

        # post same product and quantity to cart
        page = self.client.post("/cart/adjust/{0}".format(item.id),
                                data={'quantity': '0'},
                                follow=True)

        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        #  # check Template Used is cart.html page
        self.assertTemplateUsed(page, "cart.html")

    def test_remove_item_cart(self):
        ''' test remove item from cart '''

        # create an item
        item = Product(name="Product", price=2)

        # save the item
        item.save()
        # post the product id and ammended quantity
        page = self.client.post("/cart/add/{0}".format(item.id),
                                data={"quantity": 2},
                                follow=True)

        # post same product and quantity to cart
        page = self.client.post("/cart/remove/{0}".format(item.id),
                                follow=True)

        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        #  # check Template Used is cart.html page
        self.assertTemplateUsed(page, "cart.html")
