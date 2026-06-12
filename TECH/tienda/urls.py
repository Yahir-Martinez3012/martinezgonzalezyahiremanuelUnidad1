"""
=====================================================
  TecnoStore UTC - URLs de la tienda
=====================================================
Aquí mapeamos cada URL a su vista correspondiente.
"""

from django.urls import path
from . import views

urlpatterns = [
    # --- Páginas principales ---
    path('', views.inicio, name='inicio'),
    path('productos/', views.productos, name='productos'),
    path('productos/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('ofertas/', views.ofertas, name='ofertas'),

    # --- Autenticación ---
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('recuperar/', views.recuperar, name='recuperar'),

    # --- Funcionalidades ---
    path('buzon/', views.buzon, name='buzon'),
    path('chat/', views.chat, name='chat'),
    path('chat/enviar/', views.chat_enviar, name='chat_enviar'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('contacto/', views.contacto, name='contacto'),

    # --- Navegación ---
    path('mapa-sitio/', views.mapa_sitio, name='mapa_sitio'),
    path('buscar/', views.buscar, name='buscar'),

    # --- Página de error 404 con diseño completo ---
    # Accesible desde el menú sin necesitar DEBUG=False
    path('404/', views.demo_404, name='demo_404'),
]
