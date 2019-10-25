from django.urls import path, re_path
from .views import do_search

urlpatterns = [
    path('', do_search, name='search'),
]