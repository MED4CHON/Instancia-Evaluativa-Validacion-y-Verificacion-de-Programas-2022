"""
models.py

Es la fuente única y definitiva de información sobre sus datos. Contiene los campos y comportamientos
esenciales de los datos que está almacenando.

Para obtener más información sobre este archivo, consulte:
https://docs.djangoproject.com/en/4.1/topics/db/models/
"""

from django.db import models
from django.db.models import Q
from model_utils import Choices

ORDER_COLUMN_CHOICES = Choices(
    ('0', 'id'),
    ('1', 'idFecha'),
    ('2', 'idAsignatura'),
    ('3', 'idCarrera'),
)

class mesas(models.Model):
    """Modelo nombrado como 'mesas' con sus respectivos parametros.

    Args:
        models (Model): Significa que 'mesas' es un modelo de Django, por lo que Django lo guarda en la base de datos.

    Parameters:
        idFecha (DateTimeField): Fecha donde se realiza la mesa correspondiente.
        idAsignatura (CharField): Asignatura vinculada a la mesa correspondiente.
        idCarrera (CharField): Carrera vinculada a la mesa correspondiente.
    """
    idFecha = models.DateTimeField()
    idAsignatura = models.CharField(max_length=255)
    idCarrera= models.CharField(max_length=255)

    class Meta:
        """Metadatos del modelo 'mesas'.

        Parameters:
            db_table (str): Especifica el nombre de tabla en la base de datos.
            ordering (tuple): Ordena la lista de los objetos del modelo.
            verbose_name (str): Nombre del modelo.
            verbose_name_plural (str): Nombre en plural del modelo.
        """
        db_table = 'mesas'
        ordering = ("idFecha",)
        verbose_name = "mesa"
        verbose_name_plural = "mesas"

    def __str__(self):
        """Se encarga de convertir el objeto de la clase seleccionada en una cadena.

        Args:
            self (object): Representa la instancia de la clase. Con esta podemos acceder a los atributos y métodos.

        Returns:
            Se retorna mediante su propia instancia de la clase basada en el atributo 'idCarrear' de la clase 'mesas'.
        """
        return self.idCarrera

def query_mesas_by_args(**kwargs):
    """Sirve para consultar el listado de mesas segun los parametros que se les especifique.

    Args:
        **kwargs (dict): Se usa para pasar un número variable de argumentos con nombre.

    Parameters:
        draw (int): Valor de dibujo del listado.
        length (int): Longitud del listado.
        start (int): Inicio del listado.
        search_value: Buscar el valor dentro de los objetos del modelo.
        order: Ordenamiento de los objetos que se van creando.
        order_column: Ordenamiento de los objetos segun las opciones que se seleccionan.
        queryset (object): Contiene todos los objetos 'mesas' en la base de datos.
        total (int): Contador de todos los objetos del modelo 'mesas'.
        count (int): Contador de los objetos del modelo 'mesas', para asignar valor a los nuevos objetos.

    Returns:
        Retorna los objetos junto con los campos 'items', 'count', 'total' y 'draw'.
    """
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]

    order_column = ORDER_COLUMN_CHOICES[order_column]
    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    queryset = mesas.objects.all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(id__icontains=search_value) |
                                        Q(idFecha__icontains=search_value) |
                                        Q(idAsignatura__icontains=search_value) |
                                        Q(idCarrera__icontains=search_value))

    count = queryset.count()

    if length == -1:
        queryset = queryset.order_by(order_column)
    else:
        queryset = queryset.order_by(order_column)[start: start + length]

    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }
