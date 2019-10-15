from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import all_products, product_detail, remove_product, all_products, products_by_category

urlpatterns = [
    path('', all_products, name='products'),
    path('<int:pk>', views.product_detail, name="product_detail"),
    path('deleteproduct/<int:pk>', views.remove_product, name="remove_product"),
    path('<int:category_id>/', views.products_by_category, name="products_by_category"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
