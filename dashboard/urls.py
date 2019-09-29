from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import dashboard, dashboard_orders


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboardorders', views.dashboard_orders, name='dashboard_orders'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
