from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Producto


class ProductosTemplateView(ListView):
    model = Producto
    template_name = "productos.html"
    context_object_name = "productos"


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "detalle_producto.html"
    context_object_name = "producto"


def home(request):
    productos = Producto.objects.filter(activo=True).order_by('-fecha_creacion')[:3]

    context = {
        'productos': productos,
        'titulo': 'Ultimos productos agregados',
        'usuario_logueado': True
    }

    return render(request, 'home.html', context)


def home_1(request):
    return home(request)


def acerca_de_mi(request):
    return render(request, 'acerca-de-mi.html')


def catalogo(request):
    productos = Producto.objects.all()

    context = {
        'productos': productos
    }

    return render(request, 'productos.html', context)