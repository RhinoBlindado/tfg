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

import pymeshlab
import argparse
import glob
import os 


parser = argparse.ArgumentParser(description='Calculate the Hausdorff Distance between one or more meshes.')

parser.add_argument('--base', type=str, help='Path to base file or directory.')
parser.add_argument('--sample', type=str, help='Path to sample file or directory.')
parser.add_argument('--is_dir', action='store_true')

args = parser.parse_args() 

ms = pymeshlab.MeshSet()

haufDict = {
            'RMS' : 0,
            'diag_mesh_0' : 0,
            'diag_mesh_1' : 0,
            'max' : 0,
            'min' : 0,
            'mean': 0
           }

if(args.is_dir):
    bases = glob.glob("{}*.obj".format(args.base))
    samples = glob.glob("{}*.obj".format(args.sample))

    bases.sort()
    samples.sort()

    for i,j in zip(bases, samples):
        
        print("Loading mesh {} and {}".format(i,j))
        ms.load_new_mesh(j)
        ms.load_new_mesh(i)

        tempHauf_i = ms.hausdorff_distance()
        ms.clear()

        print("Stats: {}".format(tempHauf_i))

        haufDict['RMS'] += tempHauf_i['RMS']
        haufDict['diag_mesh_0'] += tempHauf_i['diag_mesh_0']
        haufDict['diag_mesh_1'] += tempHauf_i['diag_mesh_1']
        haufDict['max'] += tempHauf_i['max']
        haufDict['min'] += tempHauf_i['min']
        haufDict['mean'] += tempHauf_i['mean']

    print("Overall stats: ")
    haufDict['RMS'] /= len(bases)
    haufDict['diag_mesh_0'] += tempHauf_i['diag_mesh_0']
    haufDict['diag_mesh_1'] += tempHauf_i['diag_mesh_1']
    haufDict['max'] /= len(bases)
    haufDict['min'] /= len(bases)
    haufDict['mean'] /= len(bases)

    print(haufDict)

else:
    base = glob.glob("{}".format(args.base))
    sample = glob.glob("{}".format(args.sample))

    ms.load_new_mesh(sample[0])
    ms.load_new_mesh(base[0])

    print(ms.hausdorff_distance())