#!/bin/bash

# [CASTELLANO]
#
#    Plantilla para trabajos locales
#    Asignatura: Trabajo de Fin de Grado
#    Autor: Valentino Lugli (Github: @RhinoBlindado)
#    2022
#
# [ENGLISH]
#
#    Template for local training
#    Course: Bachelor's Thesis
#    Author: Valentino Lugli (Github: @RhinoBlindado)
#    2022

# Basic parameters
##################
trainPath=("./networks/MeshCNNPlus/development/meshcnn/train.py")
testPath=("./networks/MeshCNNPlus/development/meshcnn/test.py")
dataPath=("./data/datasets/X")
testName=("X")

basicParams=("${trainPath} --csv --dataroot ${dataPath} --name ${testName} --num_threads 2  --seed 16 --ninput_edges X")
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
