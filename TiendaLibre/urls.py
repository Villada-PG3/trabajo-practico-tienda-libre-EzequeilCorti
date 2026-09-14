from django.urls import path

from . import views

app_name = 'TiendaLibre'

urlpatterns = [
    path('', views.home_1, name='home'),
    path('inicio/', views.home_1, name='inicio'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('catalogo/<int:pk>/', views.ProductoDetailView.as_view(), name='detalle_producto'),
]