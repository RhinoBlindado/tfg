#!/bin/bash

# [CASTELLANO]
#
#    Prueba de MeshCNN con diferentes resoluciones de entrada
#    Asignatura: Trabajo de Fin de Grado
#    Autor: Valentino Lugli (Github: @RhinoBlindado)
#    2022
#
# [ENGLISH]
#
#    MeshCNN test for different input resolutions
#    Course: Bachelor's Thesis
#    Author: Valentino Lugli (Github: @RhinoBlindado)
#    2022

# Job name
#SBATCH --job-name=MCNNRES

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

# Network architecture
######################
optimizer=("adam")

batchSize=("1")
epochs=("3")
epochsWithLRDecay=("0")

conv=("64 128 256 256")
resBlocks=("0")
normalization=("batch")

dense=("100")
dropout=("0")

# Data augmentation
###################
edgeFlip=("0")
numAug=("1")
slideVerts=("0")

dataAug=("--flip_edges ${edgeFlip} --num_aug ${numAug} --slide_verts ${slideVerts}")

# Training
##########

# 30K Edges

dataPath=("./data/datasets/ResTest-30K")
testName=("MeshCN-ResTest-30K")

basicParams=("${trainPath} --csv --dataroot ${dataPath} --name ${testName} --num_threads 2  --seed 16 --ninput_edges 30000")
basicTrainParams=("--print_freq 9999 --run_test_freq 9999 --validation --verbose_train")

pool=("24000 18000 12000 7200")

netArch=("--amsgrad --arch mconvnet --batch_size ${batchSize} --dropout ${dropout} --fc_n ${dense} --gpu_ids 0 --ncf ${conv} --niter ${epochs} --niter_decay ${epochsWithLRDecay} --norm ${normalization} --num_groups 1  --optimizer ${optimizer} --pool_res ${pool} --resblocks ${resBlocks}")

python $basicParams $basicTrainParams $netArch $dataAug

# 50K Edges

dataPath=("./data/datasets/ResTest-50K")
testName=("MeshCN-ResTest-50K")

basicParams=("${trainPath} --csv --dataroot ${dataPath} --name ${testName} --num_threads 2  --seed 16 --ninput_edges 50000")
basicTrainParams=("--print_freq 9999 --run_test_freq 9999 --validation --verbose_train")

pool=("40000 30000 20000 12000")

netArch=("--amsgrad --arch mconvnet --batch_size ${batchSize} --dropout ${dropout} --fc_n ${dense} --gpu_ids 0 --ncf ${conv} --niter ${epochs} --niter_decay ${epochsWithLRDecay} --norm ${normalization} --num_groups 1  --optimizer ${optimizer} --pool_res ${pool} --resblocks ${resBlocks}")

python $basicParams $basicTrainParams $netArch $dataAug


# 100K Edges

dataPath=("./data/datasets/ResTest-100K")
testName=("MeshCN-ResTest-100K")

basicParams=("${trainPath} --csv --dataroot ${dataPath} --name ${testName} --num_threads 2  --seed 16 --ninput_edges 100000")
basicTrainParams=("--print_freq 9999 --run_test_freq 9999 --validation --verbose_train")

pool=("80000 60000 40000 24000")

netArch=("--amsgrad --arch mconvnet --batch_size ${batchSize} --dropout ${dropout} --fc_n ${dense} --gpu_ids 0 --ncf ${conv} --niter ${epochs} --niter_decay ${epochsWithLRDecay} --norm ${normalization} --num_groups 1  --optimizer ${optimizer} --pool_res ${pool} --resblocks ${resBlocks}")

python $basicParams $basicTrainParams $netArch $dataAug

# Test
######
# python $testPath $basicParams $netArch --verbose --confusion_matrix --export_folder meshes

# Notify
########
#mail -s "Entrenamiento ${testName} finalizado" valentinolugli@correo.ugr.es <<< "Hora finalización: $(date)"