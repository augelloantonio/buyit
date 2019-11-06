from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import contact_us

urlpatterns = [
    path('', views.index, name='index'),
    path('contactus', views.contact_us, name='contact_us')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
