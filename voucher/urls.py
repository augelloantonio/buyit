from django.urls import path
from .views import get_voucher
from . import views

urlpatterns = [
    path('', views.get_voucher, name='voucher'),
]

