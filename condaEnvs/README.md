# `condaEnvs`
## Information
- Folder used to store the Anaconda environments, not strictly necessary but Slurm scripts reference this folder.
- The `.yml` files included contain the libraries used for each framework.
   - For MeshCNN and MeshCNNPLus: `enviroment_meshcnn_and_plus.yml`
   - For MedMeshCNN: `enviroment_medmesh.yml`
- Can be installed in this folder with `conda env create -f ENV.yml -p PATH`, with `PATH` being `./tfg/condaEnvs/meshcnn_plus` for example.
- Can be installed in the default folder with `conda env create -n ENVNAME --file ENV.yml`
