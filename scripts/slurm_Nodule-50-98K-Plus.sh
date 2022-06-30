#!/bin/bash

#SBATCH --partition=dios
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:2            # 2 GPUs anfordern
#SBATCH --mem=16GB              # 16GiB resident memory pro node

# Configuraciones por defecto de NGPU:
export PATH="/opt/anaconda/anaconda3/bin:$PATH"
export PATH="/opt/anaconda/bin:$PATH"
eval "$(conda shell.bash hook)"
export TFHUB_CACHE_DIR=.

#We want names of master and slave nodes
MASTER=`/bin/hostname -s`
SLAVES=`scontrol show hostnames $SLURM_JOB_NODELIST | grep -v $MASTER`
#Make sure this node (MASTER) comes first
HOSTLIST="$MASTER $SLAVES"
echo "Master: $MASTER"
echo "Slaves: $SLAVES"

MPORT=$(python -c 'import socket; s=socket.socket(); s.bind(("", 0)); print(s.getsockname()[1]); s.close()');
echo "Master port: $MPORT"

COMMAND="python ./networks/MeshCNNPlus/development/train.py --dataroot ./data/datasets/Nodule-50-30K --name Nodule-50-30K --ninput_edges 30000 --ncf 32 64 128 256 512 --pool_res 25000 20000 15000 8000 7500 --norm group --resblocks 1 --flip_edges 0.2 --slide_verts 0.2 --num_aug 2 --niter 50 --niter_decay 50 --num_threads 2 --batch_size 10 --gpu_ids 0,1 --plus True"

#Launch the pytorch processes, first on master (first in $HOSTLIST) then
#on the slaves
RANK=0
set -x
for node in $HOSTLIST; do
        srun -N 1 -n 1 --nodelist=$node \
                python -m torch.distributed.launch \
                --nproc_per_node 2 \
                --nnodes $SLURM_JOB_NUM_NODES \
                --node_rank $RANK \
                --master_addr "$MASTER" --master_port "$MPORT" --use_env \
                $COMMAND &
        RANK=$((RANK+1))
done
wait
exitCode=$?
echo "done training. Exit code was $exitCode"
