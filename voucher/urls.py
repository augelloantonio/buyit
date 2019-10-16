from django.urls import path
from .views import add_voucher
from . import views

urlpatterns = [
    path('', views.add_voucher, name='voucher')
]

