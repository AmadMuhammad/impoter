bl_info = {
    "name": "Rhino_CAD(fbx) Batch Impoter",
    "description": "Batch imports fbx exported form Rhino",
    "author": "Amad_Muhammad, twitter: @AmadMuhammad17",
    "version": (0, 0, 1),
    "blender": (2, 83, 7),
    "location": "search menu",
}

import bpy
import pathlib

class IMPORT_SCENE_OT_batch_fbx(bpy.types.Operator):
    """Batch import Rhino fbx as collections"""
    bl_idname = "import_scene.batch_fbx"
    bl_label = "Batch_fbx"

    path_to_fbx: bpy.props.StringProperty(
        name='Path',
        description='Path to the directory were the fbx are located',
        subtype='DIR_PATH'
    )

    def execute(self, context):
        p = pathlib.Path(self.path_to_fbx)

        bpy.ops.object.select_all(action='DESELECT')

        for fbx in p.glob('*.fbx'):
            bpy.ops.import_scene.fbx(filepath=str(fbx))
            bpy.ops.collection.create(name = str(fbx.stem))
            bpy.ops.object.delete()
            break








def register():
    bpy.utils.register_class(IMPORT_SCENE_OT_batch_fbx)


def unregister():
    bpy.utils.unregister_class(IMPORT_SCENE_OT_batch_fbx)

    



#bpy.context.collection.children.link(str(p.stem))