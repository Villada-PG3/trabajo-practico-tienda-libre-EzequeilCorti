from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Producto, Categoria


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.filter(activo=True).order_by('-fecha_creacion')[:3]
        context['titulo'] = 'Últimos productos agregados'
        context['usuario_logueado'] = True
        return context


class CatalogoView(ListView):
    model = Producto
    template_name = "productos.html"
    context_object_name = "productos"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset().filter(activo=True)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(nombre__icontains=query)
        return queryset


class CategoriaView(ListView):
    model = Producto
    template_name = "productos.html"
    context_object_name = "productos"
    paginate_by = 6

    def get_queryset(self):
        return Producto.objects.filter(
            activo=True,
            categoria__slug=self.kwargs['slug']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_slug = self.kwargs['slug']
        context['categoria_actual'] = Categoria.objects.filter(slug=categoria_slug).first()
        return context


class DetalleProductoView(DetailView):
    model = Producto
    template_name = "detalle_producto.html"
    context_object_name = "producto"


def acerca_de_mi(request):
    return render(request, 'acerca-de-mi.html')