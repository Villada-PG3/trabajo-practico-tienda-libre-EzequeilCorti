from django.urls import path
from . import views


app_name = 'TiendaLibre'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('inicio/', views.HomeView.as_view(), name='inicio'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),
    path('catalogo/', views.CatalogoView.as_view(), name='catalogo'),
    path('catalogo/<int:pk>/', views.detalle_producto, name='detalle_producto'),
]