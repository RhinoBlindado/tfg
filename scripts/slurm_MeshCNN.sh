#!/bin/bash

# Asigna al trabajo un nombre
#SBATCH --job-name=MESHCNN

# Asignar el trabajo a una partición (cola)
#SBATCH --partition=dios

# Asignar el trabajo a un GPU
#SBATCH --gres=gpu:1

# Asignar el trabajo a un nodo en particular.
#SBATCH --nodelist=dionisio

# Configuraciones por defecto de NGPU
export PATH="/opt/anaconda/anaconda3/bin:$PATH"
export PATH="/opt/anaconda/bin:$PATH"
eval "$(conda shell.bash hook)"
export TFHUB_CACHE_DIR=.

# Activando el enviroment de Conda
conda activate /mnt/homeGPU/vlugli/condaEnvs/meshcnnplus

# Basic parameters
##################

trainPath=("./networks/MeshCNNPlus/development/meshcnn/train.py")
testPath=("./networks/MeshCNNPlus/development/meshcnn/test.py")
dataPath=("./data/datasets/Nodule-98-30K")
testName=("Nodule-98-30K-5rev")

basicParams=("${trainPath} --csv --dataroot ${dataPath} --name ${testName}  --seed 16")
basicTrainParams=("--print_freq 9999 --run_test_freq 9999 --validation --verbose_train")

# Network architecture
######################

optimizer=("adam")

batchSize=("1")
epochs=("50")
epochsWithLRDecay=("10")

conv=("32 64 256 256")
pool=("20000 15000 10000 5000")
resBlocks=("3")
normalization=("batch")

dense=("2042 512 128")
dropout=("0.25 0.25 0.25")

netArch=("--amsgrad --arch mconvnet --batch_size ${batchSize} --dropout ${dropout} --fc_n ${dense} --gpu_ids 0 --ncf ${conv} --niter ${epochs} --niter_decay ${epochsWithLRDecay} --norm ${normalization} --optimizer ${optimizer} --pool_res ${pool} --resblocks ${resBlocks}")

# Data augmentation
###################

edgeFlip=("0.2")
numAug=("20")
slideVerts=("0.2")

dataAug=("--flip_edges ${edgeFlip} --num_aug ${numAug} --slide_verts ${slideVerts}")

# Training
##########

python $basicParams $basicTrainParams $netArch #$dataAug

# Test
######
python $testPath $basicParams $netArch --verbose --confusion_matrix

# Avisar por correo de la finalización
mail -s "Entrenamiento ${testName} finalizado" valentinolugli@correo.ugr.es <<< "Hora finalización: $(date)"
