"""
=====================================================
  TecnoStore UTC - URLs principales del proyecto
=====================================================
Aquí conectamos las URLs del proyecto con nuestra app.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Panel de administración de Django
    path('admin/', admin.site.urls),
    # Todas las URLs de nuestra tienda
    path('', include('tienda.urls')),
]

# Manejador de error 404 personalizado
handler404 = 'tienda.views.error_404'

# Servir archivos estáticos en desarrollo
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
