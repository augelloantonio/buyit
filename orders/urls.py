from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import checkout

urlpatterns = [
    path('', views.checkout, name='checkout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
