#!/bin/bash

# [CASTELLANO]
#
#    Plantilla para trabajos con SLURM
#    Asignatura: Trabajo de Fin de Grado
#    Autor: Valentino Lugli (Github: @RhinoBlindado)
#    2022
#
# [ENGLISH]
#
#    Template for SLURM jobs
#    Course: Bachelor's Thesis
#    Author: Valentino Lugli (Github: @RhinoBlindado)
#    2022

# Job name
#SBATCH --job-name=

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

# Basic parameters
##################
trainPath=("./networks/MeshCNNPlus/development/meshcnn/train.py")
testPath=("./networks/MeshCNNPlus/development/meshcnn/test.py")
dataPath=("./data/datasets/Nodule-98-30K")
testName=("Nodule-98-30K-7rev")

basicParams=("${trainPath} --csv --dataroot ${dataPath} --name ${testName} --num_threads 2  --seed 16 --ninput_edges 30000")
basicTrainParams=("--print_freq 9999 --run_test_freq 9999 --validation --verbose_train")

# Network architecture
######################
optimizer=("adam")

batchSize=("1")
epochs=("X")
epochsWithLRDecay=("X")

conv=("X")
pool=("X")
resBlocks=("X")
normalization=("batch")

dense=("X")
dropout=("X")

netArch=("--amsgrad --arch mconvnet --batch_size ${batchSize} --dropout ${dropout} --fc_n ${dense} --gpu_ids 0 --ncf ${conv} --niter ${epochs} --niter_decay ${epochsWithLRDecay} --norm ${normalization} --num_groups 1  --optimizer ${optimizer} --pool_res ${pool} --resblocks ${resBlocks}")

# Data augmentation
###################
edgeFlip=("X")
numAug=("X")
slideVerts=("X")

dataAug=("--flip_edges ${edgeFlip} --num_aug ${numAug} --slide_verts ${slideVerts}")

# Training
##########
python $basicParams $basicTrainParams $netArch $dataAug

# Test
######
python $testPath $basicParams $netArch --verbose --confusion_matrix --export_folder meshes 

# Notify
########
#mail -s "Entrenamiento ${testName} finalizado" valentinolugli@correo.ugr.es <<< "Hora finalización: $(date)"
