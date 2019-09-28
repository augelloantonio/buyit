from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import all_products, product_detail, add_a_product, remove_product

urlpatterns = [
    path('', all_products, name='products'),
    path('<int:pk>', views.product_detail, name="product_detail"),
    path('addproduct', views.add_a_product, name="add_a_product"),
    path('deleteproduct/<int:pk>', views.remove_product, name="remove_product"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
