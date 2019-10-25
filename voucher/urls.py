from django.urls import path
from .views import add_voucher, delete_voucher
from . import views

urlpatterns = [
    path('', views.add_voucher, name='voucher'),
    path('deletevoucher/<int:pk>', views.delete_voucher, name="delete_voucher"),
]

