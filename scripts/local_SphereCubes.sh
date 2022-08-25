#!/bin/bash

# [CASTELLANO]
#
#    Entrenamiento de modelo SphereCubes
#    Asignatura: Trabajo de Fin de Grado
#    Autor: Valentino Lugli (Github: @RhinoBlindado)
#    2022
#
# [ENGLISH]
#
#    Training for model SphereCubes
#    Course: Bachelor's Thesis
#    Author: Valentino Lugli (Github: @RhinoBlindado)
#    2022

# Basic parameters
##################
trainPath=("./networks/MeshCNNPlus/development/meshcnn/train.py")
testPath=("./networks/MeshCNNPlus/development/meshcnn/test.py")
dataPath=("./data/datasets/SphereCubes")
testName=("SphereCubes")

basicParams=("${trainPath} --csv --dataroot ${dataPath} --name ${testName} --num_threads 2 --ninput_edges 1440")
basicTrainParams=("--print_freq 9999 --run_test_freq 9999 --validation --verbose_train")

# Network architecture
######################
optimizer=("adam")

batchSize=("2")
epochs=("5")
epochsWithLRDecay=("5")

conv=("64 128 256 256")
pool=("900 675 400 240")
resBlocks=("1")
normalization=("group")

dense=("100")
dropout=("0")

netArch=("--arch mconvnet --batch_size ${batchSize} --dropout ${dropout} --fc_n ${dense} --gpu_ids 0 --ncf ${conv} --niter ${epochs} --niter_decay ${epochsWithLRDecay} --norm ${normalization} --num_groups 2  --optimizer ${optimizer} --pool_res ${pool} --resblocks ${resBlocks}")

# Data augmentation
###################
edgeFlip=("0.2")
numAug=("20")
slideVerts=("0.2")

dataAug=("--flip_edges ${edgeFlip} --num_aug ${numAug} --slide_verts ${slideVerts}")

# Training
##########
python $basicParams $basicTrainParams $netArch $dataAug

# Test
######
python $testPath $basicParams $netArch --verbose --confusion_matrix --export_folder meshes
