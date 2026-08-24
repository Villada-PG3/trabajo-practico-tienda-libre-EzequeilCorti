from django.contrib import admin
from django.utils.html import format_html
from TiendaLibre.models import Producto
from TiendaLibre.models import Categoria


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):

    list_display = (
        'mostrar_imagen',
        'nombre',
        'marca',
        'precio',
        'stock',
    )

    @admin.display(description='Imagen')
    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" width="70" height="70" style="object-fit: contain;">',
                obj.imagen.url
            )

        return 'Sin imagen'


admin.site.register(Categoria)