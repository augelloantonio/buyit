from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import view_chart, get_data 

urlpatterns = [
    path('', views.view_chart, name='view_chart'),
    path('data/', views.get_data, name='get_data'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

