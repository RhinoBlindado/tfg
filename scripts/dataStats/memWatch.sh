# [CASTELLANO]
#
#    Obtener la carga de memoria VRAM mientras se entrena el modelo.
#    Asignatura: Trabajo de Fin de Grado
#    Autor: Valentino Lugli (Github: @RhinoBlindado)
#    2022
#
# [ENGLISH]
#
#    Get the VRAM load meanwhile the model is training.
#    Course: Bachelor's Thesis
#    Author: Valentino Lugli (Github: @RhinoBlindado)
#    2022


for i in {1..300}
do
   nvidia-smi --query-gpu=utilization.gpu,utilization.memory,memory.total,memory.free,memory.used --format=csv >> memWatch_$1.txt
   sleep 1
done
