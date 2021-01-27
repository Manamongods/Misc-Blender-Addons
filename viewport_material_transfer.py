bl_info = {
    "name" : "Transfer Viewport Materials",
    #"description" : "",
    "author" : "Steffenvy",
    "blender" : (2, 80, 0),
    "category" : "Custom"
    }

import bpy
    
class TransferViewportMaterials(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "custom.transfer_viewport_materials"
    bl_label = "Transfer Viewport Materials"

    def execute(self, context):

        for m in context.blend_data.materials:
        
            col = m.diffuse_color
           
           
            nodes = m.node_tree.nodes
            nodes["Principled BSDF"].inputs[7].default_value = m.roughness
            nodes["Principled BSDF"].inputs[4].default_value = m.metallic

            
            if m.cycles.id_data.node_tree != None:
                for node in m.cycles.id_data.node_tree.nodes:
                  for nodeInput in node.inputs:
                    if nodeInput.type == 'RGBA':

                        nodeInput.default_value[0] = col[0]
                        nodeInput.default_value[1] = col[1]
                        nodeInput.default_value[2] = col[2]

                        break
            
        return {'FINISHED'}


def register() :
    bpy.utils.register_class(TransferViewportMaterials)
    
def unregister():
    bpy.utils.unregister_class(TransferViewportMaterials)
    
    
if __name__ == "__main__":
    register()
    