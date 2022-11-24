[:es: Español](#trabajo-de-fin-de-grado) | [:gb: English](#bachelors-thesis)

---
# Trabajo de Fin de Grado #
## :books: Curso 2021-2022, Grado en Ingeniería Informática, ETSIIT UGR.
### _Clasificación automática de criterios morfológicos para estimación de la edad a partir de modelos 3D de la sínfisis del pubis_

**Autor**
- Valentino Lugli

**Directores**
- Dr. Sergio Damas Arroyo
- Dr. Pablo Mesejo Santiago

### :pushpin: Introducción
En este TFG se desarrolló un modelo de una red neuronal convolucional capaz de procesar directamente mallas 3D de huesos de la sínfisis del pubis, hueso ubicado en la pelvis. La red se desarrolló utilizando el _framework_  MeshCNN y obtiene un _accuracy_ de 70% en los datos de prueba, así como una métrica F1 de 0.70. 

La memoria se encuentra disponible para su lectura [aquí](https://github.com/RhinoBlindado/tfg/blob/main/docs/TFG___Memoria.pdf).

### :gear: Instalación
Se requiere tener Anaconda instalado.

Una vez descargado el repositorio, se debe crear un _enviroment_ de Anaconda para las librerías. Dos ficheros `.yml` se encuentran en `condaEnvs` y contienen las librerías necesarias para el funcionamiento de los _frameworks_.

### :file_cabinet: Datos
Para los experimentos se utilizaron los siguientes _datasets_:
    
- SHREC16
    - 700 mallas: 384 para entrenamiento, 96 para validación y 120 para test.
    - 20 categorías.
    - _Dataset_ balanceado.
    - Resolución máxima de 750 aristas.
- SphereCubes 
    - 20 mallas: 6 para entrenamiento, 2 para validación y 2 para test.
    - 2 categorías, esfera y cubo.
    - _Dataset_ balanceado.
    - Resolución máxima de 1440 aristas.
- Nodule-50-30K
    - 50 mallas: 34 para entrenamiento, 6 para validación y 10 para test
    - 2 categorías, existencia o ausencia de nódulo óseo en la superficie de la sínfisis del pubis. 
    - _Dataset_ balanceado.
    - Resolución máxima de 30 000 aristas.
- Nodule-98-30K
    - 98 mallas: 66 para entrenamiento, 10 para validación y 20 para test.
    - 2 categorías, existencia o ausencia de nódulo óseo en la superficie de la sínfisis del pubis.
    - _Dataset_ balanceado.
    - Resolución máxima de 30 000 aristas.

Los _datasets_ SHREC16 y SphereCubes se encuentran disponibles en `/data/datasets/` en formato ZIP que debe ser descomprimido previamente a utilizarse.

Los _datasets_ Nodule-50-30K y Nodule-98-30K no se encuentran disponibles debido a un acuerdo de confidencialidad con la Universidad de Granada.

### :nut_and_bolt: Ejecución

Una lista de los parámetros que utiliza MeshCNN y sus derivados se puede observar [aquí](https://github.com/RhinoBlindado/tfg/blob/main/docs/networkParameters.md). 

Debido a que se utilizó principalmente MeshCNN para los experimentos, existen parámetros o funcionalidades que no se encuentran disponibles en los _frameworks_ restantes.

#### Entrenamiento

Para realizar un entrenamiento, es necesario ejecutar el fichero `train.py` del _framework_ seleccionado. Debido a la cantidad de parámetros que contiene el _framework_, es mejor utilizar ficheros de Bash que contengan los parámetros necesarios.

#### Test

Para realizar una ejecución de la red con los datos de test, se debe ejecutar el fichero `test.py` del _framework_ seleccionado. Se recomienda igualmente utilizar ficheros Bash.

#### Ejemplos

Se tienen dos ejemplos preparados para su ejecución

`$> bash ./scripts/local_SHREC16.sh`, o

`$> bash ./scripts/local_SphereCubes.sh`

Esto iniciará un entrenamiento de un modelo sobre el _framework_ de MeshCNN que al finalizar también obtendrá las estadísticas del modelo en el conjunto de test.

Se incluye una plantilla para ejecuciones locales, ejecuciones en Google Colab y Slurm en sus respectivas carpetas dentro de `scripts`.

### :building_construction: _Frameworks_

En este trabajo se utilizaron los _frameworks_ de [MeshCNN](https://github.com/ranahanocka/MeshCNN), [MedMeshCNN](https://github.com/LSnyd/MedMeshCNN) y [MeshCNNPlus](https://github.com/atomicsulfate/meshcnn-4-cadseg).

---
# Bachelor's Thesis #
## :books: 2021-2022 Course, Computer Science Degree, ETSIIT UGR.
### _Automatic classification of morphological criteria for age estimation using 3D scans of the pubic symphysis_.

**Author**
- Valentino Lugli

**Directors**
- Dr. Sergio Damas Arroyo
- Dr. Pablo Mesejo Santiago

### :pushpin: Introduction
In this Bachelor's Thesis a neural network model was developed capable of processing 3D meshes of scanned pubic symphyses, a bone located in the pelvis.
It uses the MeshCNN framework and has an accuracy of 70% with a F1 metric of 0.7 in test data.
 
The report is available to be read [here](https://github.com/RhinoBlindado/tfg/blob/main/docs/TFG___Memoria.pdf) (Spanish).
 
### :gear: Installation
Requires Anaconda.
 
Once the repository has been downloaded, an Anaconda environment must be created for the libraries. Two `.yml` files located in `condaEnvs` contain the needed libraries for the frameworks.
 
### :file_cabinet: Data
For the experiments, the following datates were used:
  
- SHREC16
   - 700 meshes: 384 for training, 96 for validation and 120 for test.
   - 20 categories.
   - Balanced dataset.
   - 750 edges max resolution.
- SphereCubes
   - 20 meshes: 6 for training, 2 for validation and 2 for test.
   - 2 categories, sphere and cube.
   - Balanced dataset.
   - 1440 edges max resolution.
- Nodule-50-30K
   - 50 meshes: 34 for training, 6 for validation and 10 for test.
   - 2 categories, existence or absence of bony nodule in the surface of the pubic symphysis.
   - Balanced dataset.
   - 30 000 edges max resolution.
- Nodule-98-30K
   - 98 Meshes: 66 for training, 10 for validation and 20 for test.
   - 2 categories, existence or absence of bony nodule in the surface of the pubic symphysis.
   - Balanced dataset.
   - 30 000 edges max resolution.
 
The SHREC16 and SphereCubes datasets are available in ZIP format at `/data/datasets/`. These need to be uncompressed before being used.
 
The Nodule-50-30K and Nodule-98-30K are not available due to a confidentiality agreement with the University of Granada.
 
### :nut_and_bolt: Execution
A list of parameters for MeshCNN and derivatives is available [here](https://github.com/RhinoBlindado/tfg/blob/main/docs/networkParameters.md).
 
Due to the fact that MeshCNN was used for the experiments, some parameters or functionalities are not available in the other frameworks.
 
#### Training
To train a model, run `train.py` of the desired framework. Due to the huge amount of parameters that the script takes, it's recommended to use a Bash script with the necessary parameters.
 
#### Test
 
To use the model on test data, run `test.py` of the desired framework. It's also recommended to use a Bash script too.
 
#### Examples
 
There are two training and test examples available, and can be run with:
 
`$> bash ./scripts/local_SHREC16.sh`, or
 
`$> bash ./scripts/local_SphereCubes.sh`
 
This will start training the model in the MeshCNN framework. After finishing it will also run on the test data, printing relevant statistics for the model.
 
A template is included for local, Google Colab or Slurm executions in their respective folders inside `scripts`.
 
### :building_construction: Frameworks
In this work the following frameworks were used: [MeshCNN](https://github.com/ranahanocka/MeshCNN), [MedMeshCNN](https://github.com/LSnyd/MedMeshCNN) and[MeshCNNPlus](https://github.com/atomicsulfate/meshcnn-4-cadseg).
