import bpy

bl_info = {
 "name": "Blender to Unity",
 "author": "nomand",
 "version": (1, 0, 0),
 "blender": (2, 80, 0),
 "location": "3D View > Object Mode > Object Context Menu",
 "description": "Prepares object hierarchy for export to Unity",
 "warning": "",
 "wiki_url": "https://github.com/nomand/BlenderToUnity",
 "tracker_url": "",
 "category": "Object"}

def NMND_MT_DRAW_MENU(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(NMND_SELECT_HIERARCHY.bl_idname)
    layout.operator(NMND_EXPORT_PREP.bl_idname)

class NMND_MT_APPEND_MENU(bpy.types.Menu):
    bl_label = "Template"
    def draw(self, context):
        pass

class NMND_EXPORT_PREP(bpy.types.Operator):
    bl_label = "Blender to Unity"
    bl_description = "Clears transforms on mesh hierarchy and fixes rotation for export."
    bl_idname = "object.nmnd_prep_for_export"
    
    def execute(self, context):        
        bpy.ops.object.nmnd_select_hierarchy('INVOKE_DEFAULT')
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False, properties=False)
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.active_object.select_set(state=True)
        bpy.ops.object.nmnd_fix_hierarchy('INVOKE_DEFAULT')
        bpy.ops.object.nmnd_select_hierarchy('INVOKE_DEFAULT')
        return {'FINISHED'}
    
class NMND_SELECT_HIERARCHY(bpy.types.Operator):
    
    bl_label = "Select Hierarchy"
    bl_description = "Select all children"
    bl_idname = "object.nmnd_select_hierarchy"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        selection = bpy.context.active_object
        bpy.ops.object.select_grouped(type='CHILDREN_RECURSIVE')
        selection.select_set(state=True)
        return {'FINISHED'}    

class NMND_FIX_HIERARCHY(bpy.types.Operator):

    bl_description = "Fix rotations in hierarchies for Unity"
    bl_label = "Fix Hierarchy"
    bl_idname = "object.nmnd_fix_hierarchy"
    bl_options = {'REGISTER', 'UNDO'}
    
    def Iterate(self, Object):
        for obj in Object:
            self.Apply90(obj)

    def Apply90(self, Object):
        Object.select_set(state=True)
        
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False, properties=False)
        bpy.ops.transform.rotate(value = 1.5708, orient_axis='X', constraint_axis = (True, False, False), orient_type='GLOBAL')
        
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False, properties=False)
        bpy.ops.transform.rotate(value = -1.5708, orient_axis='X', constraint_axis = (True, False, False), orient_type='GLOBAL')
        
        Object.select_set(state=False)
        
        for child in Object.children:
            self.Apply0(child)
        
    def Apply0(self, Object):        
        Object.select_set(state=True)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False, properties=False)
        Object.select_set(state=False)
        
        if len(Object.children):
            self.Iterate(Object.children)
    
    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT' and context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        self.Iterate(bpy.context.selected_objects)
        return {'FINISHED'}

classes = (NMND_MT_APPEND_MENU, NMND_EXPORT_PREP, NMND_SELECT_HIERARCHY, NMND_FIX_HIERARCHY)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_object_context_menu.append(NMND_MT_DRAW_MENU)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_object_context_menu.remove(NMND_MT_DRAW_MENU)

if __name__ == "__main__":
    register()