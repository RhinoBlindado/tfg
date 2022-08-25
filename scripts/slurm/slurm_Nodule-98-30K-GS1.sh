#!/bin/bash

# [CASTELLANO]
#
#    Grid search para el dataset Nodule-98-30K
#    Asignatura: Trabajo de Fin de Grado
#    Autor: Valentino Lugli (Github: @RhinoBlindado)
#    2022
#
# [ENGLISH]
#
#    Grid search for the Nodule-98-30K dataset
#    Course: Bachelor's Thesis
#    Author: Valentino Lugli (Github: @RhinoBlindado)
#    2022

# Job name
#SBATCH --job-name=MESHGS1

# Assign job to a queue
#SBATCH --partition=dios

# Use GPU
#SBATCH --gres=gpu:1

# Assign job to a particular node
#SBATCH --nodelist=dionisio

# Default configs for NGPU
export PATH="/opt/anaconda/anaconda3/bin:$PATH"
export PATH="/opt/anaconda/bin:$PATH"
eval "$(conda shell.bash hook)"
export TFHUB_CACHE_DIR=.

# Activating conda enviroment
conda activate /mnt/homeGPU/vlugli/condaEnvs/meshcnnplus

# Calling the main script
python ./scripts/slurm/Nodule-98-30K-GS-Main.py --tests 0 1 2 3 4 5
