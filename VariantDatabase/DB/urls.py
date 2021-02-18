from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('variants/', views.Variantpage, name='Variantpage'),
    path('datainput/', views.Datainputpage, name='Datainputpage'),
    path('bulkinput/', views.Bulkinputpage, name='Bulkinputpage'),
]
