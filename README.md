[:es: Español](#trabajo-de-fin-de-grado) | [:gb: English](#bachelors-thesis)

---
# Trabajo de Fin de Grado #
## :books: Curso 2021-2022, Grado en Ingeniería Informática, ETSIIT UGR.
### :pushpin: Introducción
Repositorio del Trabajo de Fin de Grado titulado _Clasificación automática de criterios morfológicos para estimación de la edad a partir de modelos 3D de la sínfisis del pubis_ en donde se desarrolló un modelo de una red neuronal convolucional denominada `Nodule-98-30K-GS-25` capaz de procesar mallas 3D de huesos de la sínfisis del pubis escaneados directamente utilizando el _framework_  MeshCNN y que obtiene un _accuracy_ de 70% en los datos de prueba, así como una métrica F1 de 0.70. 

### :gear: Instalación
Para la instalación, es necesario tener instalado Anaconda y haber descargado el repositorio. Posteriormente se puede utilizar el fichero `enviroment.yml` para instalar el _enviroment_ con las librerías necesarias localmente. Realizado esto se tiene el repositiorio instalado.

### :link: Contenido


### :link: Pruebas
Los datos de la sínfisis del pubis, denominados Nodule-50-30K y Nodule-98-30K, no están disponibles públicamente por motivos de confidencialidad.

Aún así, se tienen disponible públicamente para su descarga los _datasets_ de [SHREC16](https://drive.google.com/file/d/1ZqA2cuNx5GiwGrcqzPL-pRy_YTV0NJld/view?usp=sharing) y [SphereCubes](https://drive.google.com/file/d/1H4MwTY-irFiqZfDfcIZ_gyTAS3HJjWWc/view?usp=sharing). Una vez descargados, deben descomprimirse en la ruta `/data/datasets/`. 

Para ejecutar un entrenamiento es necesario activar el _enviroment_ de Anaconda y luego escribir alguno los siguientes comandos:

>`python ./scripts/local_shrec16.sh`

>`python ./scripts/local_sphereCubes.sh`

Esto iniciará un entrenamiento de un modelo sobre el _framework_ de MeshCNN que al finalizar también obtendrá las estadísticas del modelo en el conjunto de test.

---
# Bachelor's Thesis #
## :books: 2021-2022 Course, Computer Science Degree, ETSIIT UGR.
### :pushpin: Introduction
Repository for the bachelor's thesis titled _Automatic classification of morphological criteria for age estimation using 3D scans of the pubic symphysis_.

### :gear: Compilation

### :link: Contents
