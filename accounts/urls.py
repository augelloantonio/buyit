from django.urls import path, include
from . import urls_reset
from django.conf import settings
from django.conf.urls.static import static
from .views import index, register, profile, logout, login

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('reset-password/', include(urls_reset))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
