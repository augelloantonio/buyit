from django.urls import path, include
from . import urls_reset
from .views import index, register, profile, logout, login

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('reset-password/', include(urls_reset))
]