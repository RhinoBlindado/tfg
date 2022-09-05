"""
 [CASTELLANO]

    Generar un dataset con CSV a partir de ficheros OBJ etiquetados,
    Asignatura: Trabajo de Fin de Grado
    Autor: Valentino Lugli (Github: @RhinoBlindado)
    2022

 [ENGLISH]

    Generate a CSV dataset using tagged OBJ files.
    Course: Bachelor's Thesis
    Author: Valentino Lugli (Github: @RhinoBlindado)
    2022
"""

import os
import glob
import sklearn.model_selection as skms
import numpy as np
import argparse 

parser = argparse.ArgumentParser(description='Generate .csv file from folder structure')

parser.add_argument('--path', required=True, help='Path to dataset.')
parser.add_argument('--validation', type=float, default=0.15, help='Proportion of the training set to be used as validation.')

args = parser.parse_args() 

pathRaw = args.path

os.chdir(pathRaw)

fName = os.listdir()
files = glob.glob("./*/*/*.obj")

trainData = []
trainClass = []
testData = []
testClass = []

for f in files:
    if(f.split("/")[2] == 'train'):
        trainData.append(f)
        trainClass.append(f.split("/")[1])
    else:
        testData.append(f)
        testClass.append(f.split("/")[1])
        
trainData = np.asarray(trainData)
trainClass = np.asarray(trainClass)

x_train, x_val, y_train, y_val = skms.train_test_split(trainData, 
                                                       trainClass, 
                                                       stratify=trainClass,
                                                       test_size=args.validation,
                                                       random_state=16)

trainFile = open('train.csv', 'w')

for i,j in zip(x_train, y_train):
    trainFile.write("{},{}\n".format(i[2:],j))
    
trainFile.close()

valFile = open('val.csv', 'w')

for i,j in zip(x_val, y_val):
    valFile.write("{},{}\n".format(i[2:],j))
    
valFile.close()

testFile = open('test.csv', 'w')
for i,j in zip(testData, testClass):
    testFile.write("{},{}\n".format(i[2:],j))
    
testFile.close()
