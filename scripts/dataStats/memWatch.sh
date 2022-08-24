
for i in {1..300}
do
   nvidia-smi --query-gpu=utilization.gpu,utilization.memory,memory.total,memory.free,memory.used --format=csv >> memWatch_$1.txt
   sleep 1
done
