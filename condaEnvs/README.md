# `condaEnvs`
- Se utilizó para almacenar los _enviroments_ de Anaconda junto con el resto del trabajo, no es estrictamente necesario.
- Se incluyen los ficheros `enviroment_meshcnn_and_plus.yml` y `enviroment_medmesh.yml` que contienen las librerías utilizadas para ejecutar los _frameworks_ MeshCNN junto a MeshCNNPlus y MedMeshCNN respectivamente.
- Se pueden instalar con el comando `conda env create -f ENV.yml -p PATH` siendo `ENV` el nombre del fichero y `PATH` la ruta deseada, por ejemplo, `./condaEnvs/meshcnn_and_plus`. 
    - Alternativamente se puede instalar como `conda env create -n ENVNAME --file ENV.yml` siendo `ENVNAME` el nombre del _enviroment_.