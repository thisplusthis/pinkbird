# pinkbird/meter/urls.py

from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('readings/', views.ReadingsChartData.as_view())
]
