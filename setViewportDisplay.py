bl_info = {
    "name": "Set Viewport Display",
    "author": "Loíc \"L0Lock\" Dautry",
    "version": (1, 0),
    "blender": (3, 1, 0),
    "location": "View3D > Object > Set Viewport Display",
    "description": "Set the viewport display",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}


import bpy
from bpy.types import (Operator, Panel, Menu, AddonPreferences, PropertyGroup, PointerProperty)
from bpy.props import StringProperty

#class SVD_Props(PropertyGroup):
#    def update_keymap_cb(self, context):
#        unregister_keymap()
#        register_keymap()
#    
#    keymap_key: StringProperty(default='D', update=update_keymap_cb)

class OBJECT_OT_setVDisplayBounds(Operator):
    """Tooltip"""
    bl_idname = "object.set_display_bounds"
    bl_label = "Set Viewport Display: Bounds"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        for object in bpy.context.selected_objects:
            object.display_type = 'BOUNDS'
        return {'FINISHED'}
    
class OBJECT_OT_setVDisplayWire(Operator):
    """Tooltip"""
    bl_idname = "object.set_display_wire"
    bl_label = "Set Viewport Display: Wire"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        for object in bpy.context.selected_objects:
            object.display_type = 'WIRE'
        return {'FINISHED'}
    
class OBJECT_OT_setVDisplaySolid(Operator):
    """Tooltip"""
    bl_idname = "object.set_display_solid"
    bl_label = "Set Viewport Display: Solid"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        for object in bpy.context.selected_objects:
            object.display_type = 'SOLID'
        return {'FINISHED'}
    
class OBJECT_OT_setVDisplayTextured(Operator):
    """Tooltip"""
    bl_idname = "object.set_display_textured"
    bl_label = "Set Viewport Display: Textured"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        for object in bpy.context.selected_objects:
            object.display_type = 'TEXTURED'
        return {'FINISHED'}

#class SVD_AddonPreferences(AddonPreferences, Panel):
#    # this must match the addon name, use '__package__'
#    # when defining this in a submodule of a python package.
#    bl_idname = __name__
#
#    def update_keymap_cb(self, context):
#        unregister_keymap()
#        register_keymap()
#    
#    keymap_key: StringProperty(default='D', update=update_keymap_cb)
#    
#    def draw(self, context):
#        layout = self.layout
#        SVD_Properties = bpy.context.window_manager.SVD_Properties
#
#        col = layout.column()
#        
#        col.prop(self, "SVD_Properties.keymap_key", text="Menu key:")
    
# UI

class OBJECT_MT_svdMenu(Menu):
    bl_label = "Set Viewport Display Menu"
    bl_idname = "OBJECT_MT_svd_menu"
    
    @classmethod
    def poll(cls, context):
        return True

    def draw(self, context):
        layout = self.layout
        layout.label(text="Set Viewport Display Menu")

        layout.operator("object.set_display_bounds")
        layout.operator("object.set_display_wire")
        layout.operator("object.set_display_solid")
        layout.operator("object.set_display_textured")

def draw_menu(self, context):
    if context.mode == 'OBJECT':
        layout = self.layout
        layout.menu(OBJECT_MT_svdMenu.bl_idname)

# Registration

classes = (
    OBJECT_OT_setVDisplayBounds,
    OBJECT_OT_setVDisplayWire,
    OBJECT_OT_setVDisplaySolid,
    OBJECT_OT_setVDisplayTextured,
    OBJECT_MT_svdMenu,
)

#addon_keymaps = []
#    
#def register_keymap():
#    # register keymaps

#    wm = bpy.context.window_manager
#    kc = wm.keyconfigs.addon
#    SVD_Properties = bpy.context.window_manager.SVD_Properties
#    
#    if kc:
#        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
#        kmi = km.keymap_items.new('wm.call_menu', SVD_Properties.keymap_key, 'PRESS', ctrl=False, shift=False, alt=False)
#        kmi.properties.name =  OBJECT_MT_svdMenu.bl_idname
#        addon_keymaps.append((km, kmi))
    
#    km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
#    kmi = km.keymap_items.new(OBJECT_MT_svd_menu.bl_idname, SVD_AddonPreferences.keymap_key, 'PRESS')

#def unregister_keymap():
#    wm = bpy.context.window_manager
#    km = wm.keyconfigs.addon.keymaps['3D View']
#    km.keymap_items.remove(km.keymap_items[OBJECT_MT_svdMenu.bl_idname])

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_object.append(draw_menu)
#    register_keymap()
#    bpy.context.window_manager.SVD_Properties = bpy.props.PointerProperty(type=SVD_Props)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_object.remove(draw_menu)
#    unregister_keymap()
    
