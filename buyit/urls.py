"""buyit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views import static
from .settings import MEDIA_ROOT
from accounts import urls as urls_accounts
from products import urls as urls_products
from cart import urls as urls_cart
from orders import urls as urls_orders
from dashboard import urls as urls_dashboard
from reviews import urls as urls_review
from voucher import urls as urls_voucher
from home import urls as urls_home
from api import urls as urls_api
from search import urls as urls_search
from home.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include(urls_accounts)),
    path('products/', include(urls_products)),
    path('cart/', include(urls_cart)),
    path('order/', include(urls_orders)),
    path('dashboard/', include(urls_dashboard)),
    path('review/', include(urls_review)),
    path('voucher/', include(urls_voucher)),
    path('home/', include(urls_home)),
    path('api/', include(urls_api)),
    path('search/', include(urls_search)),
    re_path(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
