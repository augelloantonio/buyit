from django.db import models
from django.utils import timezone
from django.conf import settings
from products.models import Product
from django.contrib.auth.models import User


class Review(models.Model):

    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    user = models.OneToOneField(User, unique=False,
                             on_delete=models.PROTECT, default=1)
    review_summary = models.CharField(max_length=75, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    pub_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    comment = models.CharField(max_length=200)
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    user_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.review_summary
