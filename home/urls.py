from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('/home', index, name='index'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
