"""
WSGI config for tecnostore_utc project.
"""
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tecnostore_utc.settings')
application = get_wsgi_application()
