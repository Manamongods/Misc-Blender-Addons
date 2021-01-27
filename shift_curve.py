bl_info = {
    "name" : "Shift Curve Points",
    "description" : "Shifts curve points",
    "author" : "Steffen Vetne",
    "blender" : (2, 80, 0),
    "category" : "Custom"
    }

import bpy


class SelectEmpty(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "custom.select_empty_curves"
    bl_label = "Select Empty Curves"

    def execute(self, context):
        
        bpy.ops.object.select_all(action='DESELECT')

        for o in context.blend_data.objects:
            if o.type == "CURVE":
                if len(o.data.splines) == 0: #len(o.data.splines.active.points) == 0:
                    o.select_set(True)

        return {'FINISHED'}



class ShiftPoints(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "custom.shift_curve_points"
    bl_label = "Shift Curve Points"

    def execute(self, context):
        
        o = bpy.context.object
        if o.type == "CURVE":
        
            bpy.ops.object.mode_set(mode='OBJECT')
            
            ps = o.data.splines.active.points
            olds = []
            for p in ps:
                olds.append(p.co.copy())
                
            l = len(ps)
            id = 1
            for p in ps:
                p.co = olds[id % l]
                id += 1
                
            bpy.ops.object.mode_set(mode='EDIT')

        return {'FINISHED'}


def register() :
    bpy.utils.register_class(ShiftPoints)
    bpy.utils.register_class(SelectEmpty)
    
def unregister():
    bpy.utils.unregister_class(ShiftPoints)
    bpy.utils.unregister_class(SelectEmpty)
    
    
if __name__ == "__main__":
    register()
    