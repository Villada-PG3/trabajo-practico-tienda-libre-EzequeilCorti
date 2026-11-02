from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Producto, Categoria
from .forms import ContactoForm
from django.contrib import messages


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

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Procesamos los datos limpios (cleaned_data)
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            # Simulamos el envío del mensaje con un aviso de éxito
            messages.success(request, f'¡Gracias {nombre}! Tu mensaje ha sido enviado con éxito.')
            return redirect('TiendaLibre:contacto')
    else:
        # Petición GET: mostramos el formulario vacío
        form = ContactoForm()

    return render(request, 'contacto.html', {'form': form})