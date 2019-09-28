from django.urls import path, re_path
from .views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    path('', view_cart, name='view_cart'),
    re_path('add/(?P<id>\d+)', add_to_cart, name="add_to_cart"),
    re_path('adjust/(?P<id>\d+)', adjust_cart, name="adjust_cart"),
]