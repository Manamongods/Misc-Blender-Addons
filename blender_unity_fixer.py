bl_info = {
    "name" : "Prepare Unity Binary",
    "description" : "Prepares file for unity binary-fbx",
    "author" : "Steffenvy",
    "blender" : (2, 80, 0),
    "category" : "Custom"
    }

import bpy


def rename(name):
    return name.replace(" ", "_").replace(".", "_")
    
    
class PrepareUnityBinary(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "custom.prepare_unity_binary"
    bl_label = "Prepare Unity Binary"

    def execute(self, context):
    
        #Target Converter
        try:
            bpy.ops.target_converter.upgrade()
        except:
            pass
            
        for object in context.blend_data.objects:
        
            #Object
            object.name = rename(object.name)
            
            #Bones
            if object.type == "ARMATURE":
                bones = object.data.bones
                for b in bones:
                    b.name = rename(b.name)

            #Curve Converter
            if "names" in object.keys():
                object["names"] = rename(object["names"])
                
        return {'FINISHED'}


def register() :
    bpy.utils.register_class(PrepareUnityBinary)
    
def unregister():
    bpy.utils.unregister_class(PrepareUnityBinary)
    
    
if __name__ == "__main__":
    register()
    