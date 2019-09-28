from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    path('', view_cart, name='view_cart'),
    re_path('add/(?P<id>\d+)', add_to_cart, name="add_to_cart"),
    re_path('adjust/(?P<id>\d+)', adjust_cart, name="adjust_cart"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
