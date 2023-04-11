# IEFI - Validación y Verificación de Programas

![Badge de estado](https://img.shields.io/badge/Estado-En%20Desarrollo-brightgreen)
![Badge de versionamiento](https://img.shields.io/badge/Version-0.1-blue)
![Badge de tamaño](https://img.shields.io/badge/Tama%C3%B1o-536%20KB-blue)
![Badge de plataforma](https://img.shields.io/badge/Plataforma-Windows-lightgrey)
![Badge de licencia](https://img.shields.io/badge/Licencia-GPL-green)

El repositorio es parte de un proyecto de desarrollo para la catedra de **Validación y Verificación de Programas** de la carrera de **Tecnicatura Superior en Desarrollo de Software** del **Instituto Superior Dr. Carlos Maria Carena** de la localidad de Mina Clavero, en la provincia de Córdoba, Argentina. Este mismo sirve como parte de una base de datos para la institución para la generación de un turnero para las semanas de examenes, siendo que en este se ve la confección de la sección de las mesas correspondientes para dicha instancia.

Este mismo se encuentra en fase de desarrollo, por lo que no es una versión estable del sistema. Y por cuestiones educativos siendo comprobante de la actividad correspondiente a la Instancia Evaluativa Final Integradora **(IEFI)** solo se realizaron las series pasos dispuestos por el documento compartido por el profesor **[Carlos Murúa](https://gitlab.com/carlosmurua)**.

## Descripción del proyecto 📋

Este proyecto permite el ingreso de fechas para mesas de examen correspondientes a un curso en especifico, y su carrera.
Funciona de manera similar a un turnero donde se ingresa la fecha donde se quiere realizar el examen, y se le asigna o escribe (dependiendo la versión del repositorio) a esta una de las posibles catedras que se dan en la institución y a la carrera que corresponde esta misma.

## Tecnologías utilizadas 🛠️

* **`Python`**: Es el lenguaje de programación que utilizaremos para la codificación de funciones y objetos que seran llamados para la creación y estructuración desde la parte del servidor WEB.
* **`Django`**: Es un framework web de alto nivel de Python que se encarga del rápido desarrollo y el diseño limpio y pragmático de páginas WEB.
* **`Django Rest Framework`**: Es un framework que cuenta con un kit de herramientas potente y flexible para la construcción de API's web.
* **`HTML`**: Para el estructurado de los contenidos de la página WEB.
* **`CSS`**: Para el manejo de estilos de los contenidos de la página WEB
* **`Javascript`**: Para uso de scripts y el manejo de comportamientos dentro de los contenidos de la página WEB.
* **`Ajax`**: Es una técnica programática que utiliza JS para objetar el intercambio de datos entre un navegador WEB (Cliente) y el servidor WEB.
* **`SQLite3`**: Como base de datos relacional por defecto que viene vinculada a los proyectos de Django.

## Instalación 🔧

Para hacer uso de este repositorio es recomendable seguir los siguientes pasos, y en caso de que ya se cuente con el mismo instalado se puede saltear.

* **Paso 1**: Instalación de Python. Para esto puede dirigirse a este link. https://www.python.org/downloads/

* **Paso 2**: Una vez instalado, ingresar a la carpeta del repositorio y abrir el CMD. Una vez abierta la consola escribiremos a continuación lo siguiente, esto nos servira para tener un entorno de trabajo que contenga los requerimientos del sistema:

```
python -m venv <Nombre del Entorno Virtual>
```

* **Paso 3**: Posicionarse en el nuevo directorio y entrar a la carpeta de scripts, para asi activar el entorno.

```
cd <Nombre del Entorno Virtual>
cd scripts
activate
```

* **Paso 4**: Volver hacia la carpeta principal del repositorio, e ingresar a la misma para descargar todos los requerimientos del proyecto.

```
cd ..
cd ..
cd iefi_vyv
pip install -r requirements.txt
```

* **Paso 5**: Ya instalada todas las dependencias. Ingresar la siguiente linea de comando para inicializar el servidor local:

```
python manage.py runserver
```

* **Paso 6**: Ingresar al navegador WEB y escribir la siguiente dirección para entrar a la página WEB:

```
127.0.0.1:8000
```

Ya a partir de este punto puede utilizar sin problemas el repositorio.

## Autor ✒️

Este repositorio ha sido construido por:

* **[Matías J. Meda](https://github.com/MED4CHON)**

## Licencia 📄

Este proyecto está bajo la Licencia (GPL). Esta es una licencia de software libre copyleft donde cualquiera de los usuarios de un programa con licencia GPL pueden libres de usar y acceder al código fuente de este repositorio, y realizar modificaciones y poder distribuir los cambios siempre que redistribuya el programa completo (modificado o no modificado) bajo esta misma licencia.
