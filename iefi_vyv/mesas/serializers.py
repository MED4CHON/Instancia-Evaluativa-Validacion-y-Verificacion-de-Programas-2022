"""
serializers.py

Permiten convertir datos complejos, como conjuntos de consultas e instancias de modelos,
en tipos de datos nativos de Python que luego se pueden representar fácilmente en JSON, XML u otros tipos de contenido.

Para obtener más información sobre este archivo, consulte:
https://www.django-rest-framework.org/api-guide/serializers/
"""

from django.conf import settings

from rest_framework import serializers

from .models import mesas

class mesasSerializer(serializers.ModelSerializer):
    """Serializador de 'mesas'. Convierte las instancias del modelo 'mesas' en formato JSON.

    Args:
        serializers (ModelSerializer): Proporciona un atajo que permite crear automáticamente
        una clase Serializer con campos que corresponden a los campos del modelo seleccionado.

    Parameters:
        idFecha (DateTimeField): Una representación de fecha de cuando se realiza la mesa.
    """
    # Si su <field_name> se declara en su serializador con el parámetro required=False
    # Entonces este paso de validación no tendrá lugar si el campo no está incluido.
    idFecha = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False)

    class Meta:
        """Metadatos de 'mesasSerializer'

        Parameters:
            model: Selección del modelo que sera invocado.
            fields (str): Selección de los campos del modelo que seran llamados.
        """
        model = mesas
        fields = "__all__"
