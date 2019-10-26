from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import add_review

urlpatterns = [
    path('addreview/product/<int:product_id>',
         views.add_review, name='add_review'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
