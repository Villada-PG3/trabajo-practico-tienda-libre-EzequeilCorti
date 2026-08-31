from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto


class ProductosTemplateView(ListView):
    model = Producto
    template_name = "productos.html"
    context_object_name = "productos"


def home(request):
    productos_destacados = [
         {"nombre": "Auriculares Bluetooth", "precio": 15999, "stock": 32},
            {"nombre": "Mouse inalámbrico", "precio": 8499, "stock": 18},
            {"nombre": "Teclado mecánico", "precio": 24999, "stock": 7},
            {"nombre": "Webcam HD", "precio": 12999, "stock": 4},
            {"nombre": "Pendrive 64GB", "precio": 5999, "stock": 1},
            {"nombre": "Hub USB-C", "precio": None, "stock": 0},
    ]

    context = {
        'titulo': 'Productos de la semana',
        'productos': productos_destacados,
        'usuario_logueado': True
    }

    return render(request, 'home.html', context)


def home_1(request):
    return home(request)


def acerca_de_mi(request):
    return render(request, 'acerca-de-mi.html')