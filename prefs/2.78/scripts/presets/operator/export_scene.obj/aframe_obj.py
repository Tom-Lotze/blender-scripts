import bpy
op = bpy.context.active_operator

op.filepath = 'Y:\\mozvr\\git\\a-painter\\models\\ui_test.obj'
op.axis_forward = '-Z'
op.axis_up = 'Y'
op.use_selection = False
op.use_animation = False
op.use_mesh_modifiers = True
op.use_edges = True
op.use_smooth_groups = False
op.use_smooth_groups_bitflags = False
op.use_normals = True
op.use_uvs = True
op.use_materials = True
op.use_triangles = True
op.use_nurbs = False
op.use_vertex_groups = False
op.use_blen_objects = True
op.group_by_object = False
op.group_by_material = False
op.keep_vertex_order = False
op.global_scale = 1.0
op.path_mode = 'AUTO'
