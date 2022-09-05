"""
 [CASTELLANO]

    Obtener estadísticas de uno o varios ficheros OBJ.
    Asignatura: Trabajo de Fin de Grado
    Autor: Valentino Lugli (Github: @RhinoBlindado)
    2022

 [ENGLISH]

    Get stats for one or multiple OBJ files.
    Course: Bachelor's Thesis
    Author: Valentino Lugli (Github: @RhinoBlindado)
    2022
"""

import bpy
import os
import sys
import glob 

def loadObj(objPath):
    bpy.ops.import_scene.obj(filepath=objPath, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_edges=True,
                                 use_smooth_groups=True, use_split_objects=False, use_split_groups=False,
                                 use_groups_as_vgroups=False, use_image_search=True, split_mode='ON')
    ob = bpy.context.selected_objects[0]
    return ob

path = sys.argv[-1]

if (os.path.isfile(path)):
    model = loadObj(path)
    print("Model: {}".format(model.data.name))
    print("Vertices: {}, Triangles: {}, Edges: {}".format(len(model.data.vertices), len(model.data.polygons), len(model.data.edges)))
    exit(0)
elif os.path.isdir(path):
    files = glob.glob("{}*.obj".format(path))

    totVerts = 0
    totTrigs = 0
    totEdges = 0

    for i, f in enumerate(files):
        print("Processing file {}/{}".format(i+1, len(files)))
        
        tempModel = loadObj(f)
        totVerts += len(tempModel.data.vertices)/len(files)
        totTrigs += len(tempModel.data.polygons)/len(files)
        totEdges += len(tempModel.data.edges)/len(files)
        del tempModel

    print("Average stats for {} models".format(len(files)))
    print("Vertices: {:.4f}, Triangles: {:.4f}, Edges: {:.4f}".format(totVerts, totTrigs, totEdges))

    exit(0)
else:
    exit(-1)