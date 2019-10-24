from django.db import models
from products.models import Product
from django.conf import settings
from cart.contexts import cart_contents
from datetime import datetime
from django.contrib.auth.models import User
from voucher.models import Voucher

ORDER_STATUS = (
    ('Order Received', 'Order Received'),
    ('Delivered', 'Delivered'),
)

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, unique=False,
                             on_delete=models.CASCADE, default=1)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    email_address = models.CharField(max_length=100, blank=False, default="")
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField(null=True)
    voucher = models.ForeignKey(Voucher, null=True, blank=True, on_delete=models.SET_NULL)
    order_status = models.CharField(
        choices=ORDER_STATUS, max_length=50, default='Order Received', blank=True)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    user = models.ForeignKey(User, unique=False,
                             on_delete=models.DO_NOTHING, default=1)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, null=False)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=False)
    quantity = models.IntegerField(blank=False)
    total = models.DecimalField(
        blank=False, default=0, max_digits=4, decimal_places=2)
    date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return "{0} {1} {2} @ {3}".format(self.quantity, self.product.name, self.product.price, self.total)
