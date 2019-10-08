from django.urls import path
from .views import get_voucher

urlpatterns = [
    path('', get_voucher, name='voucher'),
]

