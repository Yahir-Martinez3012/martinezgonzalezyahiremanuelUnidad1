"""
=====================================================
  TecnoStore UTC - Configuración del panel admin
=====================================================
Aquí registramos los modelos para poder
verlos y editarlos desde /admin/
"""

from django.contrib import admin
from .models import Categoria, Producto, MensajeBuzon, MensajeContacto, MensajeChat


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'icono']
    search_fields = ['nombre']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'precio_oferta', 'es_oferta', 'destacado', 'stock']
    list_filter = ['categoria', 'es_oferta', 'destacado']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['es_oferta', 'destacado', 'stock']


@admin.register(MensajeBuzon)
class MensajeBuzonAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'asunto', 'fecha_envio', 'leido']
    list_filter = ['leido']
    search_fields = ['asunto', 'usuario__username']


@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'asunto', 'fecha_envio']
    search_fields = ['nombre', 'email', 'asunto']


@admin.register(MensajeChat)
class MensajeChatAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'mensaje', 'fecha', 'sesion_id']
    list_filter = ['tipo']

# Personalizar el título del panel admin
admin.site.site_header = 'TecnoStore UTC - Administración'
admin.site.site_title = 'TecnoStore UTC'
admin.site.index_title = 'Panel de Control'
