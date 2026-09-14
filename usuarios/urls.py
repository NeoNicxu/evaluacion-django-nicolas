from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_perfil, name='usuarios_perfil'),
    path('registro/', views.vista_registro, name='usuarios_registro'),
]