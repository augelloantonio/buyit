from django.db import models
from django.utils import timezone
from products.models import Product


class Review(models.Model):

    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    review_summary = models.CharField(max_length=254, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    pub_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.review_summary
