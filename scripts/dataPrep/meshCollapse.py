"""
 [CASTELLANO]

    Simplificar uno o varios archivos OBJ a cierta cantidad de aristas.
    Asignatura: Trabajo de Fin de Grado
    Autor: Valentino Lugli (Github: @RhinoBlindado)
    2022

 [ENGLISH]

    Simplify one or many OBJ files to a edge count.
    Course: Bachelor's Thesis
    Author: Valentino Lugli (Github: @RhinoBlindado)
    2022
"""

import argparse
import glob
import os

BLENDER_REDUCE = "./programs/blender/blender --background --python ./scripts/dataPrep/blender_meshCollapse.py"

def collapse(source, destination, numEdges):
    os.system("{} {} {} {}".format(BLENDER_REDUCE, source, numEdges, destination))

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(description='Mesh collapse one file or multiple OBJ files.')

    parser.add_argument('--input', required=True, help='Path to OBJ file or folder.')
    parser.add_argument('--output', required=True, help='Output destination folder.')
    parser.add_argument('--edges', required=True, type=int, help='Reduce the number of edges to this amount or less.')

    args = parser.parse_args()

    if(os.path.isdir(args.input) and os.path.isdir(args.output)):
        input = glob.glob("{}*.obj".format(args.input))
        output = args.output

        for i, mesh in enumerate(input):
            print("Processing mesh {}, {}/{}".format(mesh.split("/")[-1], i+1, len(input)))
            collapse(mesh, "{}{}".format(output, mesh.split("/")[-1]), args.edges)

    elif (os.path.isfile(args.input)):
        collapse(args.input, args.output, args.edges)
    else:
        print("Error: Incorrect paths")