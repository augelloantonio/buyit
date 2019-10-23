from django.urls import path, include, re_path
from . import urls_reset
from django.conf import settings
from django.conf.urls.static import static
from .views import register, profile, logout, login, personal_login
from . import views
from django.contrib.auth import views as v

urlpatterns = [
    path('logout/', logout, name="logout"),
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('reset-password/', include(urls_reset))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
