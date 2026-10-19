from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Producto


# 1 y 5. Vista Home reescrita como TemplateView
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtenemos los últimos 3 productos activos
        context['productos'] = Producto.objects.filter(activo=True).order_by('-fecha_creacion')[:3]
        context['titulo'] = 'Últimos productos agregados'
        context['usuario_logueado'] = True
        return context


# 3. Vista Catalogo reescrita como ListView
class CatalogoView(ListView):
    model = Producto
    template_name = "productos.html"
    context_object_name = "productos"


# Vistas existentes que se mantienen
def acerca_de_mi(request):
    return render(request, 'acerca-de-mi.html')


def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    context = {
        'producto': producto
    }
    return render(request, 'detalle_producto.html', context)