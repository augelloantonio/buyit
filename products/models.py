from django.db import models
from django.utils import timezone

categories_list = (
    ('bestseller', 'Bestseller'),
    ('latest', ' Latest'),
)


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    category = models.CharField(max_length=100, choices=categories_list, null=True, blank=True)
    in_stock = models.BooleanField(blank=False, default=True)
    quantity_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.name
        
