from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_inicio, name='catalogo_inicio'),
    path('detalle/', views.vista_detalle, name='catalogo_detalle'),
]