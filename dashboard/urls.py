from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import dashboard, dashboard_orders, dashboard_order_details

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboardorders', views.dashboard_orders, name='dashboard_orders'),
    path('dashboardorder/<int:id>', views.dashboard_order_details, name='dashboard_order_details'),
    path('dashboardproducts', views.dashboard_product, name='dashboard_product'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
