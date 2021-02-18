from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('variants/', views.Variantpage, name='Variantpage'),
    path('add/', views.InputForm, name='Input'),
]
