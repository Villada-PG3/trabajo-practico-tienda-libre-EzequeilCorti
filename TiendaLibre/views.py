from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Producto

class ProductosTemplateView(ListView):
    model = Producto
    template_name = "productos.html"
    context_object_name = "productos"
# Create your views here.

def home(request):
    return render(request, 'home.html')

def home_1(request):
    return render(request, 'home.html')

def acerca_de_mi(request):
    return render(request, 'acerca-de-mi.html')
