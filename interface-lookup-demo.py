bl_info = {
	"name": "Interface lookup demos",
	"author": "Patrick W. Crawford (TheDuckCow)",
	"version": (0, 1),
	"blender": (2, 78, 0),
	"location": "Properties > Render > Interface demo panel",
	"description": "Showcase of different interfaces possible with blender",
	"warning": "In development",
	"wiki_url": "",
	"category": "System",
	}


import bpy


# -----------------------------------------------------------------------------
# Primary panel registration, points to each example
# -----------------------------------------------------------------------------

# Lookup panel definition, hosts section for all UI-types
class InterfaceLookupPanel(bpy.types.Panel):
	"""Creates a Panel in the properties/render window"""
	bl_label = "Interface Lookup Demo"
	bl_idname = "SYSTEM_PT_interfacedemo"
	bl_space_type = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context = "render"

	def draw(self, context):
		layout = self.layout
		row = layout.row(align=True)
		row.operator("wm.url_open", text="Helper website").url="http://theduckcow.com/"
		row.operator("wm.url_open", text="View source code").url="https://github.com/TheDuckCow/blender-interface-lookups"
		layout.label("Select a demo from the dropdown below")
		layout.prop(context.scene,"interface_demo_enum", text="")

		# run the draw function on that enum value if found
		try:
			atr = addon_updater_install_popup.bl_idname.split(".")
			getattr(__name__, context.scene.interface_demo_enum )()
		except:
			col = layout.column()
			col.scale_y = 0.7
			col.label("Error: could not find draw function", icon="ERROR")
			col.label("Addon is a work in progress!")


# List of items for enum dropdown
def enumItems(self, context):
	enum=[
		("properties","Properties","Properties demo"),
		("operators","Operators","operators demo"),
	]

	return enum


# -----------------------------------------------------------------------------
# Now, the individual examples of interface demos
# -----------------------------------------------------------------------------

def properties_draw(self,context):
	self




# -----------------------------------------------------------------------------
# Registration
# -----------------------------------------------------------------------------


def register():
	bpy.utils.register_class(InterfaceLookupPanel)

	# Enum property definition, allowing you to select which demo to view
	bpy.types.Scene.interface_demo_enum = bpy.props.EnumProperty(
		name="Interface demos",
		items=enumItems)


def unregister():
	bpy.utils.unregister_class(InterfaceLookupPanel)


if __name__ == "__main__":
	register()
