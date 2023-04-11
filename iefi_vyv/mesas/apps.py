"""
apps.py

Es un registro de aplicaciones instaladas que almacena la configuración y proporciona introspección.
También mantiene una lista de modelos disponibles.

Para obtener más información sobre este archivo, consulte:
https://docs.djangoproject.com/en/4.1/ref/applications/
"""

from django.apps import AppConfig


class MesasConfig(AppConfig):
    """Aplicación de Mesas con su respectiva configuración.

    Args:
        AppConfig: Representa la aplicación Django correspondiente y su respectiva configuración.

    Parameters:
        default_auto_field (str): Campo automático predeterminado.
        name: Nombre de la aplicación
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mesas'
