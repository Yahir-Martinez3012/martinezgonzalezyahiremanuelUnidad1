"""
=====================================================
  TecnoStore UTC - Configuración principal de Django
  Proyecto: MartinezGonzalezYahirEmanuelUnidad1
=====================================================
"""

from pathlib import Path
import os

# Directorio raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta (en producción cámbiala y ponla en variables de entorno)
SECRET_KEY = 'django-insecure-tecnostore-yahir-2024-clave-secreta'

# En desarrollo DEBUG=True muestra errores detallados
DEBUG = True

# Hosts permitidos (en producción pon tu dominio)
ALLOWED_HOSTS = ['*']

# -------------------------------------------------------
# Aplicaciones instaladas en el proyecto
# -------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',          # Panel de administración
    'django.contrib.auth',           # Sistema de usuarios
    'django.contrib.contenttypes',
    'django.contrib.sessions',       # Sesiones (para login)
    'django.contrib.messages',       # Mensajes flash
    'django.contrib.staticfiles',    # Archivos estáticos (CSS, JS)
    'tienda',                        # Nuestra aplicación principal
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tecnostore_utc.urls'

# -------------------------------------------------------
# Configuración de plantillas HTML
# -------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # carpeta templates en la raíz
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tecnostore_utc.wsgi.application'

# -------------------------------------------------------
# Base de datos SQLite (muy fácil, no necesita instalación)
# -------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------------------------------------
# Validación de contraseñas
# -------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Idioma y zona horaria
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

# -------------------------------------------------------
# Archivos estáticos (CSS, JavaScript, imágenes)
# -------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Redireccionamiento al iniciar/cerrar sesión
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
