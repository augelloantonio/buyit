from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import add_review, review_detail

urlpatterns = [
    path('review/<int:review_id>', views.review_detail, name='review_detail'),
    path('addreview/product/<int:product_id>', views.add_review, name='add_review'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
