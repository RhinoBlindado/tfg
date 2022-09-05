'''
Simplifies mesh to target number of edges
Requires Blender 2.8

Original Author: Rana Hanocka
Additional modifications by: Valentino Lugli

@input: 
    <obj_file>
    <target_edges> number of target edges
    <outfile> name of simplified .obj file

@output:
    simplified mesh .obj
    to run it from cmd line:
    /opt/blender/blender --background --python blender_process.py /home/rana/koala.obj 1000 /home/rana/koala_1000.obj
'''

import bpy
import os
import sys

class Process:
        
    def __init__(self, obj_file, target_faces, export_name):
        mesh = self.load_obj(obj_file)
        self.simplify(mesh, target_faces)
        self.export_obj(mesh, export_name)

    def load_obj(self, obj_file):
        bpy.ops.import_scene.obj(filepath=obj_file, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_edges=True,
                                 use_smooth_groups=True, use_split_objects=False, use_split_groups=False,
                                 use_groups_as_vgroups=False, use_image_search=True, split_mode='ON')
        ob = bpy.context.selected_objects[0]
        return ob

    def subsurf(self, mesh):
        # subdivide mesh
        bpy.context.view_layer.objects.active = mesh
        mod = mesh.modifiers.new(name='Subsurf', type='SUBSURF')
        mod.subdivision_type = 'SIMPLE'
        bpy.ops.object.modifier_apply(modifier=mod.name)
        # now triangulate
        mod = mesh.modifiers.new(name='Triangluate', type='TRIANGULATE')
        bpy.ops.object.modifier_apply(modifier=mod.name)

    def simplify(self, mesh, target_faces):
        bpy.context.view_layer.objects.active = mesh
        
        mod = mesh.modifiers.new(name='Decimate', type='DECIMATE')
        bpy.context.object.modifiers['Decimate'].use_collapse_triangulate = True
        
        nfaces = len(mesh.data.edges)
        print("Actual number of edges: {}, target edge count: {}".format(nfaces, target_faces))
        
        if nfaces < target_faces:
            self.subsurf(mesh)
            nfaces = len(mesh.data.edges)
            
        ratio = target_faces / float(nfaces)
        mod.ratio = float('%s' % ('%.6g' % (ratio)))
        print("Colapsing edges...")
        bpy.ops.object.modifier_apply(modifier=mod.name)

        bpy.ops.object.mode_set(mode='EDIT')
        print("Removing degenerate geometry...")
        bpy.ops.mesh.dissolve_degenerate()
        bpy.ops.object.mode_set(mode='OBJECT')

        print('Final edge count:', int(len(mesh.data.edges)))


    def export_obj(self, mesh, export_name):
        outpath = os.path.dirname(export_name)
        if not os.path.isdir(outpath): os.makedirs(outpath)
        print('EXPORTING', export_name)
        bpy.ops.object.select_all(action='DESELECT')
        mesh.select_set(state=True)
        bpy.ops.export_scene.obj(filepath=export_name, check_existing=False, filter_glob="*.obj;*.mtl",
                                 use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True,
                                 use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True,
                                 use_uvs=False, use_materials=False, use_triangles=True, use_nurbs=False,
                                 use_vertex_groups=False, use_blen_objects=True, group_by_object=False,
                                 group_by_material=False, keep_vertex_order=True, global_scale=1, path_mode='AUTO',
                                 axis_forward='-Z', axis_up='Y')
    

obj_file = sys.argv[-3]
target_faces = int(sys.argv[-2])
export_name = sys.argv[-1]

blender = Process(obj_file, target_faces, export_name)

exit(0)