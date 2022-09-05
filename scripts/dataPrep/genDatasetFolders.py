"""
 [CASTELLANO]

    Generar un dataset con carpetas a partir de ficheros OBJ etiquetados,
    Asignatura: Trabajo de Fin de Grado
    Autor: Valentino Lugli (Github: @RhinoBlindado)
    2022

 [ENGLISH]

    Generate a folder dataset using tagged OBJ files.
    Course: Bachelor's Thesis
    Author: Valentino Lugli (Github: @RhinoBlindado)
    2022
"""

import meshCollapse
import pandas as pd
import numpy as np
import shutil
import argparse
import os

parser = argparse.ArgumentParser(description='Mesh collapse one file or multiple OBJ files.')

parser.add_argument('--csv_path', required=True, help='Path to CSV tag file.')
parser.add_argument('--raw_data_path', required=True, help='Path to the OBJ data.')
parser.add_argument('--dataset_path', required=True, help='Path to the new dataset folder')
parser.add_argument('--test_size', default=0.2, type=float, help='Proportion of samples to use in test set.')
parser.add_argument('--reduce_edges', default=-1, type=int, help='If set, reduce the edges to this amount in the generated dataset.')
parser.add_argument('--tag_names', nargs='+', type=str, default=None, help='If used, this sets the names of the tags.')

args = parser.parse_args()

originalPath = args.raw_data_path
dataPath = args.dataset_path

reduceEdges = False
if(args.reduce_edges > 0):
    edgeCount = args.reduce_edges
    reduceEdges = True

testProp = args.test_size

usingLabels = False
tagDict = {}
if(args.tag_names is not None):
    tagDict = dict(list(enumerate(args.tag_names)))
    usingLabels = True
    print(tagDict)

# Read the tags
dataset = pd.read_csv(args.csv_path, sep=",", header=None)

tagNames = np.unique(dataset[dataset.keys()[1]])

dataset = dataset.to_numpy()

np.random.shuffle(dataset)

testSize = int(np.ceil(testProp * len(dataset)))

test = np.vstack((dataset[np.where(dataset[:,1] == 0)][:testSize//2], 
                  dataset[np.where(dataset[:,1] == 1)][:testSize//2]))

train = np.vstack((dataset[np.where(dataset[:,1] == 0)][testSize//2:], 
                  dataset[np.where(dataset[:,1] == 1)][testSize//2:]))


print("Test size: {}, Train size: {}".format(len(test), len(train)))

# Make the folder for the dataset

os.mkdir(dataPath)

for t in tagNames:
    if(usingLabels):
        os.mkdir(dataPath+"{}".format(str(tagDict[t])))
        os.mkdir(dataPath+"{}/train".format(str(tagDict[t])))
        os.mkdir(dataPath+"{}/test".format(str(tagDict[t])))
    else:
        os.mkdir(dataPath+"{}".format(str(t)))
        os.mkdir(dataPath+"{}/train".format(str(t)))
        os.mkdir(dataPath+"{}/test".format(str(t)))


print("Procesing training set...")
for sample in train:
    if(reduceEdges):
        meshCollapse.collapse(originalPath+sample[0]+".obj", dataPath+"{}/train/{}.obj".format(str(tagDict[sample[1]]), sample[0]), edgeCount)
    else:
        shutil.copy2(originalPath+sample[0]+".obj", dataPath+"{}/train".format(str(tagDict[sample[1]])))

print("Done.")

print("Procesing test set...")
for sample in test:

    if(reduceEdges):
        meshCollapse.collapse(originalPath+"{}.obj".format(sample[0]), dataPath+"{}/test/{}.obj".format(str(tagDict[sample[1]]), sample[0]), edgeCount)
    else:
        shutil.copy2(originalPath+sample[0]+".obj", dataPath+"{}/test".format(str(tagDict[sample[1]])))

print("Done.")
