"""
admin.py

Se encarga de leer los metadatos de sus modelos para proporcionar una interfaz rápida y
centrada en el modelo donde los usuarios de confianza pueden administrar el contenido de su sitio.
El uso recomendado por el administrador se limita a la herramienta de gestión interna de una organización.

Para obtener más información sobre este archivo, consulte:
https://docs.djangoproject.com/en/4.1/ref/contrib/admin/
"""

from django.contrib import admin

# Register your models here.
from .models import mesas

admin.site.register(mesas)