#!/bin/bash

# Ordenes para el Gestor de carga de trabajo:
# 1. Asigna al trabajo un nombre
#SBATCH --job-name=BONES

# 2. Asignar el trabajo a una partición (cola)
#SBATCH --partition=dios

# 3. Asignar el trabajo a un GPU
##SBATCH --nodes=2
##SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1
##SBATCH --mem=16GB

# 4. Asignar el trabajo a un nodo en particular.
#SBATCH --nodelist=dionisio

# Configuraciones por defecto de NGPU:
export PATH="/opt/anaconda/anaconda3/bin:$PATH"
export PATH="/opt/anaconda/bin:$PATH"
eval "$(conda shell.bash hook)"
export TFHUB_CACHE_DIR=.

# Activando el enviroment de Conda:
conda activate /mnt/homeGPU/vlugli/condaEnvs/meshcnnplus

python ./networks/MeshCNNPlus/development/meshcnn/train.py \
--dataroot ./data/datasets/Nodule-98-30K \
--name Nodule-50-98-30K \
--ninput_edges 30000 \
--ncf 16 16 32 64  \
--pool_res 20000 15000 8000 7500 \
--norm group \
--num_groups 1 \
--res_blocks 0 \
--fc_n 100 \
--flip_edges 0.2 \
--slide_verts 0.2 \
--num_aug 2 \
--niter 50 \
--niter_decay 10 \
--num_threads 2 \
--batch_size 1 \
--gpu_ids 0 \
--plus False \
--amsgrad False \

# Correo para avisarme:
# mail -s "Proceso finalizado" valentinolugli@correo.ugr.es <<< "El proceso ha finalizado"
