from django.db import models
from datetime import datetime, date


class Voucher(models.Model):
    code = models.CharField(max_length=15)
    active = models.BooleanField(default=False)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.code
