from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin
from .views import ChartData

urlpatterns = [
    path('chart/data', ChartData.as_view()),
]
