"""
 [CASTELLANO]

    Chequear si en una carpeta se encuentran los huesos presentes en un CSV
    Asignatura: Trabajo de Fin de Grado
    Autor: Valentino Lugli (Github: @RhinoBlindado)
    2022

 [ENGLISH]

    Check if bone is present in directory.
    Course: Bachelor's Thesis
    Author: Valentino Lugli (Github: @RhinoBlindado)
    2022
"""

import pandas as pd
import glob

parser = argparse.ArgumentParser(description='Check if bone is present in directory.')

parser.add_argument('--csv', type=str, help='Path to CSV file.')
parser.add_argument('--data_path', type=str, help='Path to directory.')

args = parser.parse_args() 

csvPath = args.csv

files = glob.glob("{}*".format(args.data_path))
csvLst = pd.read_csv(csvPath, sep=",", header=None)


downFiles = []
csvFiles  = []

for i in files:
    downFiles.append(i.split("/")[-1])

for i in csvLst[0]:
    csvFiles.append(i + ".obj")

for file in csvFiles:
    if file not in downFiles:
        print("File {} missing.".format(file))