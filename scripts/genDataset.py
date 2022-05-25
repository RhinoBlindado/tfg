import sys
import os
import pandas as pd
import numpy as np
import shutil

TAGNAME = "tags.csv"
BLENDER_REDUCE = "./programs/blender/blender --background --python ./scripts/blender_process.py"

# Ruta dataset, ruta datos originales, numero de aristas

# dataPath = DATAPATH + sys.argv[1]
# originalPath = sys.argv[2]
# edgeCount = int(sys.argv[3])
# testTrainProp = int(sys.argv[4])


def reduceFaces(origin, faces, destiny):
    os.system(BLENDER_REDUCE +" {} {} {}".format(origin, faces, destiny))


dataPath = "./data/datasets/Nodule-50-50K/"
originalPath = "./data/original/Nodule-50-FullK-Orig/"
edgeCount = 50000
testProp = 0.2
# rootPath = os.getcwd()

# Read the tags
dataset = pd.read_csv(originalPath + TAGNAME, sep=",", header=0)

tagNames = np.unique(dataset[dataset.keys()[1]])

dataset = dataset.to_numpy()

np.random.shuffle(dataset)

testSize = round(testProp * len(dataset))

test = np.vstack((dataset[np.where(dataset[:,1] == 0)][:testSize//2], 
                  dataset[np.where(dataset[:,1] == 1)][:testSize//2]))

train = np.vstack((dataset[np.where(dataset[:,1] == 0)][testSize//2:], 
                  dataset[np.where(dataset[:,1] == 1)][testSize//2:]))


# Make the folder for the dataset

os.mkdir(dataPath)

for t in tagNames:
    os.mkdir(dataPath+"{}".format(str(t)))
    os.mkdir(dataPath+"{}/train".format(str(t)))
    os.mkdir(dataPath+"{}/test".format(str(t)))


for sample in train:
    # shutil.copy2(originalPath+sample[0]+".obj", dataPath+"{}/train".format(str(sample[1])))
    reduceFaces(originalPath+"{}.obj".format(sample[0]), round(edgeCount / 1.5), 
                dataPath+"{}/train/{}.obj".format(str(sample[1]), sample[0]))

for sample in test:
    # shutil.copy2(originalPath+sample[0]+".obj", dataPath+"{}/test".format(str(sample[1])))
    reduceFaces(originalPath+"{}.obj".format(sample[0]), round(edgeCount / 1.5), 
                dataPath+"{}/test/{}.obj".format(str(sample[1]), sample[0]))
