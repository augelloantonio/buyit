from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import all_products, product_detail

urlpatterns = [
    path('', all_products, name='products'),
    path('<int:pk>', views.product_detail, name="product_detail"),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
