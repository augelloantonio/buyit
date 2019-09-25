from django.db import models
from django.utils import timezone

categories_list = (
    ('category_1', 'Category 1'),
    ('category_2', 'Category 2'),
)


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    categories = models.CharField(
        max_length=100, choices=categories_list)

    def __str__(self):
        return self.name
