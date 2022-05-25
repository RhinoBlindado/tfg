#/bin/bash

# How to use... WIP

origin=$1
destiny=$2
numFaces=$3

# If both folders exist...
if [ -d "$origin" -a -d "$destiny" ]; then

    echo ">ORIGIN FOLDER: $origin"
    echo ">DESTINATION FOLDER: $destiny"
    echo ">NUM FACES: $numFaces"

    files=`ls $origin`
    for f in $files
    do
        echo ">>Processing $f..."
        ../../programs/blender/blender --background --python ../../MedMeshCNN/scripts/dataprep/blender_process.py $origin$f $numFaces $destiny$f
        echo "Done."
    done
else
    echo "Not here!"
fi
