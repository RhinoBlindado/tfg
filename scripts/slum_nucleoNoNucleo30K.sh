#!/bin/bash

# Ordenes para el Gestor de carga de trabajo:
# 1. Asigna al trabajo un nombre
#SBATCH --job-name=MeshCNN_NNN30K

# 2. Asignar el trabajo a una partición (cola)
#SBATCH --partition=dios

# 3. Asignar el trabajo a un GPU
#SBATCH --gres=gpu:1

# 4. Asignar el trabajo a un nodo en particular.
#SBATCH --nodelist=dionisio

# Configuraciones por defecto de NGPU:
export PATH="/opt/anaconda/anaconda3/bin:$PATH"
export PATH="/opt/anaconda/bin:$PATH"
eval "$(conda shell.bash hook)"
export TFHUB_CACHE_DIR=.

# Activando el enviroment de Conda:
conda activate /mnt/homeGPU/vlugli/condaEnvs/meshcnn

# Entrenar la red con el dataset:
python train.py \
--dataroot datasets/nucleoNoNucleo30K \
--name nucleoNoNucleo30K \
--ninput_edges 30000 \
--ncf 64 128 256 256 \
--pool_res 20000 15000 8000 3000 \
--norm group \
--resblocks 1 \
--niter_decay -90 \
--num_threads 2 \

# Probar luego de entrenamiento:
python test.py \
--dataroot datasets/nucleoNoNucleo30K \
--name nucleoNoNucleo30K \
--ninput_edges 30000 \
--ncf 64 128 256 256 \
--pool_res 20000 15000 8000 3000 \
--norm group \
--resblocks 1 \
--export_folder meshes \

# Correo para avisarme:
# mail -s "Proceso finalizado" valentinolugli@correo.ugr.es <<< "El proceso ha finalizado"
