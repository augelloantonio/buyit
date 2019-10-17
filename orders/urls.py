from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import checkout, all_orders, order_detail, change_order_status

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('orders', all_orders, name='all_orders'),
    path('order_detail/<int:id>', views.order_detail, name="order_detail"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
