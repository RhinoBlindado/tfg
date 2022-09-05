"""
 [CASTELLANO]

    Calcular la distancia Hausdorff de una o varias mallas.
    Asignatura: Trabajo de Fin de Grado
    Autor: Valentino Lugli (Github: @RhinoBlindado)
    2022

 [ENGLISH]

    Calculate the Hausdorff Distance between one or more meshes
    Course: Bachelor's Thesis
    Author: Valentino Lugli (Github: @RhinoBlindado)
    2022
"""
import matplotlib.pyplot as plt
import pandas as pd
import argparse 
import csv

parser = argparse.ArgumentParser(description='Plot bone characteristics')

parser.add_argument('--file', required=True, help='Path to .csv file.')
parser.add_argument('--out', type=str, default=None, help='Optional, output path')

args = parser.parse_args() 

file = args.file

out = "./"
if args.out is not None:
    out = args.out

boneChars = open(file, newline='')

boneCharsP = csv.DictReader(boneChars)

toddChars = \
{
    "ArticularFace": { "0" : 0, "1" : 0, "2" : 0, "3" : 0, "4" : 0 },
    "IrregularPorosity": { "0" : 0, "1" : 0, "2" : 0 },
    "UpperSymphysialExtremity": { "0" : 0, "1" : 0 },
    "BonyNodule": { "0" : 0, "1" : 0 },
    "LowerSymphysialExtremity" : { "0" : 0 , "1" : 0 },
    "DorsalMargin": { "0" : 0 , "1" : 0 },
    "DorsalPlateau": { "0" : 0, "1" : 0 },
    "VentralBevel": { "0" : 0, "1" : 0, "2" : 0},
    "VentralMargin": { "0" : 0, "1" : 0, "2" : 0, "3" : 0, "4" : 0 },
    "Phase": { "0" : 0, "1": 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0}
}

toddStr = \
{
    "ArticularFace": { "0" : "RegularPorosity", "1" : "RidgesAndGrooves", "2" : "GroovesShallow", "3" : "GroovesRest", "4" : "NoGrooves" },
    "IrregularPorosity": { "0" : "Absence", "1" : "Medium", "2" : "Much" },
    "UpperSymphysialExtremity": { "0" : "NotDefined", "1" : "Defined" },
    "BonyNodule": { "0" : "Absent", "1" : "Present" },
    "LowerSymphysialExtremity" : { "0" : "NotDefined" , "1" : "Defined" },
    "DorsalMargin": { "0" : "Absent" , "1" : "Present" },
    "DorsalPlateau": { "0" : "Absent", "1" : "Present" },
    "VentralBevel": { "0" : "Absent", "1" : "InProcess", "2" : "Present" },
    "VentralMargin": { "0" : "Absent", "1" : "PartiallyFormed", "2" : "FormedWithoutRarefactions", "3" : "FormedWitFewRarefactions", "4" : "FormedWithLotRecessesAndProtrusions" }
}

stringVect = ["ArticularFace", "IrregularPorosity", "UpperSymphysialExtremity", "BonyNodule", "LowerSymphysialExtremity", "DorsalMargin", "DorsalPlateau",
             "VentralBevel", "VentralMargin", "Phase"]


stringVectESP = ["Crestas y Surcos", "Porocidad Regular", "Borde Superior", "Nódulo Óseo", "Borde Inferior", "Borde Dorsal", "Plataforma Dorsal",
             "Bisel Ventral", "Borde Ventral", "Fase"]
invalid = 0

for item in boneCharsP:
    if item['Excluidos'] == '' and item['lateralidad'] == '0':
        for i in stringVect:
            try:
                toddChars[i][item[i]] += 1
            except KeyError:
                invalid += 1
                continue

dataFile = open('toddChars.txt', 'w')

for key in toddChars.keys():
    dataFile.write("{}: \n".format(key))
    for subkey in toddChars[key].keys():
        dataFile.write("{} : {}\n".format(subkey, toddChars[key][subkey]))

dataFile.close()