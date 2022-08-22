#!/bin/bash

# [CASTELLANO]
#
#    Entrenamiento de modelo Nodule-50-30K-4
#    Asignatura: Trabajo de Fin de Grado
#    Autor: Valentino Lugli (Github: @RhinoBlindado)
#    2022
#
# [ENGLISH]
#
#    Training for model Nodule-50-30K-4
#    Course: Bachelor's Thesis
#    Author: Valentino Lugli (Github: @RhinoBlindado)
#    2022

# Job name
#SBATCH --job-name=N50-30K-4

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
dataPath=("./data/datasets/Nodule-50-30K")
testName=("Nodule-50-30K-4")

basicParams=("${trainPath} --csv --dataroot ${dataPath} --name ${testName} --num_threads 2  --seed 16 --ninput_edges 30000")
basicTrainParams=("--print_freq 9999 --run_test_freq 9999 --validation --verbose_train")

# Network architecture
######################
optimizer=("adam")

batchSize=("1")
epochs=("50")
epochsWithLRDecay=("50")

conv=("16 16 32 32 64")
pool=("20000 15000 13000 8000 7500")
resBlocks=("0")
normalization=("group")

dense=("100")
dropout=("0")

netArch=("--amsgrad --arch mconvnet --batch_size ${batchSize} --dropout ${dropout} --fc_n ${dense} --gpu_ids 0 --ncf ${conv} --niter ${epochs} --niter_decay ${epochsWithLRDecay} --norm ${normalization} --num_groups 1  --optimizer ${optimizer} --pool_res ${pool} --resblocks ${resBlocks}")

# Data augmentation
###################

edgeFlip=("0.2")
numAug=("2")
slideVerts=("0.2")

dataAug=("--flip_edges ${edgeFlip} --num_aug ${numAug} --slide_verts ${slideVerts}")

# Training
##########
python $basicParams $basicTrainParams $netArch $dataAug

# Test
######
python $testPath $basicParams $netArch --verbose --confusion_matrix --export_folder meshes

# Notify
########
# - Not working right now
#mail -s "Entrenamiento ${testName} finalizado" valentinolugli@correo.ugr.es <<< "Hora finalización: $(date)"
