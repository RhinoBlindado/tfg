#!/bin/bash

# Asigna al trabajo un nombre
#SBATCH --job-name=MESHCNN-1

# Asignar el trabajo a una partición (cola)
#SBATCH --partition=dios

# Asignar el trabajo a un GPU
#SBATCH --gres=gpu:1

# Asignar el trabajo a un nodo en particular.
#SBATCH --nodelist=dionisio,hera

# Configuraciones por defecto de NGPU
export PATH="/opt/anaconda/anaconda3/bin:$PATH"
export PATH="/opt/anaconda/bin:$PATH"
eval "$(conda shell.bash hook)"
export TFHUB_CACHE_DIR=.

# Activando el enviroment de Conda
conda activate /mnt/homeGPU/vlugli/condaEnvs/meshcnnplus

#####################
## MESH CNN CONFIG ##
#####################

# STATIC PARAMS
###############
trainPath=("./networks/MeshCNNPlus/development/meshcnn/train.py")
testPath=("./networks/MeshCNNPlus/development/meshcnn/test.py")
dataPath=("./data/datasets/Nodule-98-30K")

epochs=("30")
epochsWithLRDecay=("10")
batchSize=("1")

# VARIABLE PARAMS
#################

LOOP1=0
LOOP2=0

# Network architecture
######################

optimizer=("adam" "rmsprop")
initType=("xavier" "kaiming")

conv=("32 64 256 256" "256 128 64 32")
pool=("20000 15000 10000 5000")
resBlocks=("0")
normalization=("batch")

dense=("2042 512 128" "1024 512 128")
dropout=("0.25 0.25 0.25" "0.5 0.25 0.125")

lr=("0.0002" "0.001" "0.00001")

# Data augmentation
###################

edgeFlip=("0.2" "0.4")
numAug=("20" "40")
slideVerts=("0.2" "0.4")
scaleVerts=("" "--scale_verts")

# GRID SEARCH
#############

for (( i=$LOOP1; i<${#optimizer[@]}; i+=1 ))
do
    for (( j=$LOOP2; j<${#initType[@]}; j+=1 ))
    do
        for (( k=0; k<${#conv[@]}; k+=1 ))
        do
            for (( l=0; l<${#dense[@]}; l+=1 ))
            do
                for (( m=0; m<${#edgeFlip[@]}; m+=1 ))
                do
                    DATE=`date  +%Y_%m_%d__%H_%M_%S`
                    testName=("Nodule-98-30K-GS-${DATE}")

                    basicParams=("${trainPath} --csv --dataroot ${dataPath} --name ${testName} --init_type ${initType[$j]} --seed 16 --num_threads 2")
                    basicTrainParams=("--print_freq 9999 --run_test_freq 9999 --validation --verbose_train")
                    netArch=("--arch mconvnet --batch_size ${batchSize} --dropout ${dropout[$l]} --fc_n ${dense[$l]} --ncf ${conv[$k]} --niter ${epochs} --niter_decay ${epochsWithLRDecay} --norm ${normalization} --optimizer ${optimizer[$i]} --pool_res ${pool} --resblocks ${resBlocks}")
                    dataAug=("--flip_edges ${edgeFlip[$m]} --num_aug ${numAug[$m]} --slide_verts ${slideVerts[$m]} ${scaleVerts[$m]}")

                    python $basicParams $basicTrainParams $netArch $dataAug
                    python $testPath $basicParams $netArch --verbose --confusion_matrix --export_folder meshes 
                done
            done
        done
        break 2
    done

done