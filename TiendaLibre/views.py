from django.shortcuts import render
from django.views.generic import TemplateView

from django.views.generic import ListView
from .models import Producto

class ProductosTemplateView(ListView):
    model = Producto
    template_name = "productos.html"
    context_object_name = "productos"
# Create your views here.
