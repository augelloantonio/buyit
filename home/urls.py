from django.urls import path
from django.conf import settings
from django.conf.urls.static import static, url
from .views import latest
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
