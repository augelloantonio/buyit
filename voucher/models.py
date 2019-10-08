from django.db import models
from datetime import datetime, date


class Voucher(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField(default=0)
    price_reducing = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    date_from = models.DateTimeField(default=datetime.now())
    date_to = models.DateTimeField(default=datetime.now())


def __str__(self):
    return self.code
