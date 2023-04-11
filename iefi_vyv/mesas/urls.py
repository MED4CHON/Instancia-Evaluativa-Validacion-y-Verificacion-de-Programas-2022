"""
libros/urls.py

Permite configurar las acciones a realizar ingresada una URL en nuestro proyecto web creado con Django.
La lista `urlpatterns` enruta las URL a las vistas.

Para obtener más información sobre este archivo, consulte:
https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from mesas.views import index, mesasViewSet

router = DefaultRouter()
router.register(r'mesas', mesasViewSet, basename='mesas')

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]
