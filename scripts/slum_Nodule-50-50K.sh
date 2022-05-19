#!/bin/bash

# Ordenes para el Gestor de carga de trabajo:
# 1. Asigna al trabajo un nombre
#SBATCH --job-name=NERV-001

# 2. Asignar el trabajo a una partición (cola)
#SBATCH --partition=dios

# 3. Asignar el trabajo a un GPU
#SBATCH --gres=gpu:1

# 4. Asignar el trabajo a un nodo en particular.
##SBATCH --nodelist=dionisio

# Configuraciones por defecto de NGPU:
export PATH="/opt/anaconda/anaconda3/bin:$PATH"
export PATH="/opt/anaconda/bin:$PATH"
eval "$(conda shell.bash hook)"
export TFHUB_CACHE_DIR=.

# Activando el enviroment de Conda:
conda activate /mnt/homeGPU/vlugli/condaEnvs/meshcnnplus

# Entrenar la red con el dataset:
python ./networks/MeshCNNPlus/development/train.py \
--dataroot ./data/datasets/Nodule-50-50K \
--name Nodule-50-50K \
--ninput_edges 50000 \
--ncf 32 64 256 256 64  \
--pool_res 30000 20000 15000 10000 6000 \
--batch_size 10 \
--norm group \
--resblocks 1 \
--flip_edges 0.2 \
--slide_verts 0.2 \
--num_aug 20 \
--niter 10 \
--niter_decay 10 \
--num_threads 2 \
--gpu_ids 0 \

# Correo para avisarme:
# mail -s "Proceso finalizado" valentinolugli@correo.ugr.es <<< "El proceso ha finalizado"
