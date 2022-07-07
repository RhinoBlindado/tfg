#!/bin/bash

# Asigna al trabajo un nombre
#SBATCH --job-name=MESHGS

# Asignar el trabajo a una partición (cola)
#SBATCH --partition=dios

# Asignar el trabajo a un GPU
#SBATCH --gres=gpu:1

# Asignar el trabajo a un nodo en particular.
#SBATCH --nodelist=hera

# Configuraciones por defecto de NGPU
export PATH="/opt/anaconda/anaconda3/bin:$PATH"
export PATH="/opt/anaconda/bin:$PATH"
eval "$(conda shell.bash hook)"
export TFHUB_CACHE_DIR=.

# Activando el enviroment de Conda
conda activate /mnt/homeGPU/vlugli/condaEnvs/meshcnnplus

python ./scripts/GS_addon.py --tests 0 1 3 5 6 7
