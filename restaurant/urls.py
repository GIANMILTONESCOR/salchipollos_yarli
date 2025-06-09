# restaurant/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('nosotros/', views.nosotros, name='nosotros'),
]