"""
 [CASTELLANO]

    Extraer el fichero OBJ de la estructura de carpetas original.
    Asignatura: Trabajo de Fin de Grado
    Autor: Valentino Lugli (Github: @RhinoBlindado)
    2022

 [ENGLISH]

    Extract OBJ file from original file structure.
    Course: Bachelor's Thesis
    Author: Valentino Lugli (Github: @RhinoBlindado)
    2022
"""

import os
import glob
import shutil
import argparse

parser = argparse.ArgumentParser(description='Extract OBJ file from original file structure.')

parser.add_argument('--path_raw', required=True, help='Path to the main raw folder')
parser.add_argument('--path_ready', required=True, help='Path to copy the OBJ files to.')
parser.add_argument('--path_structure', default=None, help="If present, define the regex structure to find the OBJ file, default is './*/Izq/*.obj'")

args = parser.parse_args() 

pathRaw = args.path_raw
pathRdy = args.path_ready

os.chdir(pathRaw)

fName = os.listdir()

if(args.path_structure is not None):
    pathStruct = args.path_structure
else:
    pathStruct = "./*/Izq/*.obj"

files = glob.glob(pathStruct)

for i, obj in enumerate(files):
    nPath = shutil.copy2(obj, "../"+pathRdy)
    os.rename(nPath, "../"+pathRdy+"/"+fName[i]+"-Izq.obj")
    print("Processing file ", fName[i])
