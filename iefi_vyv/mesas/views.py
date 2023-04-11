"""
views.py

Son funciones de Python que toman solicitudes HTTP, y devuelven respuestas HTTP como documentos HTML.

Para obtener más información sobre este archivo, consulte:
https://docs.djangoproject.com/en/4.1/intro/tutorial03/
"""

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets, status

from .serializers import mesasSerializer
from .models import mesas, query_mesas_by_args

def index(request):
    """Esta función se encarga de renderizar la página index entregandoles los argumentos a la plantilla 'index.html'.

    Args:
        request (object): Sirve para entregar los objetos que contienen los metadatos de la solicitud que van a ser enviado a la plantilla.

    Returns:
        Se renderiza la página con los argumentos pasados en la plantilla 'index.html'
    """
    return render(request, 'index.html')

class mesasViewSet(viewsets.ModelViewSet):
    """ Un ViewSet para listar mesas.

    Args:
        viewsets (ModelViewSet): Heredable de GenericAPIView, incluye implementaciones para
        varias acciones, mezclando el comportamiento de las distintas clases mixtas.

    Parameters:
        queryset (object): Contiene todos los objetos 'mesas' en la base de datos.
        serializer_class (object): Define la clase del Serializador a 'mesasSerializer'.
    """
    queryset = mesas.objects.all()
    serializer_class = mesasSerializer

    def list(self, request, **kwargs):
        """Lista los objetos de 'mesas' en base a los parametros pasados. Esta funciona en base a que filtra a las mesas mediante
        un sistema de busqueda, en el cual hacemos uso del queryset para que se filtran las mesas de la lista correspondiente y
        se muestran aquellos resultados que coinciden con lo que se especifica en la busqueda.

        Args:
            self (object): Representa la instancia de la clase. Con esta podemos acceder a los atributos y métodos.
            de la clase en Python ya que vincula los atributos con los argumentos dado.
            request (object): Sirve para entregar los objetos que contienen los metadatos de la solicitud que van a ser enviado a la plantilla.
            **kwargs (dict): Se usa para pasar un número variable de argumentos con nombre.

        Parameters:
            mesas (dict): Dibujar el listado de 'mesas'.
            serializer (object): Serializador de 'mesas'.
            result (dict): Diccionario que contiene el dibujo del listado del modelo, junto con la data del serializador,
            el conteo del total de los mesas y el conteo de los mesas filtrados.

        Returns:
            En el caso exitoso se retorna 'result' junto con su contenido, y tambien un código de respuesta HTTP 200 (OK).
            En el caso contrario se retorna un Exception junto a un código de respuesta HTTP 404 (Not Found).
        """
        try:
            mesas = query_mesas_by_args(**request.query_params)
            serializer = mesasSerializer(mesas['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = mesas['draw']
            result['record Total'] = mesas['total']
            result['recordsFiltered'] = mesas['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)