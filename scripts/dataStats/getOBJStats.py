"""
 [CASTELLANO]

    Obtener estadísticas de uno o varios ficheros OBJ. Wrapper para script de Blender
    Asignatura: Trabajo de Fin de Grado
    Autor: Valentino Lugli (Github: @RhinoBlindado)
    2022

 [ENGLISH]

    Get stats for one or multiple OBJ files. Wrapper for Blender script.
    Course: Bachelor's Thesis
    Author: Valentino Lugli (Github: @RhinoBlindado)
    2022
"""

import argparse
import os

BLENDER_OBJ = "./programs/blender/blender --background --python ./scripts/dataStat/blender_getOBJStats.py"

parser = argparse.ArgumentParser(description='Get stats for one or multiple OBJ files.')

parser.add_argument('--input', required=True, help='Path to OBJ file or folder.')

args = parser.parse_args()

os.system("{} {}".format(BLENDER_OBJ, args.input))