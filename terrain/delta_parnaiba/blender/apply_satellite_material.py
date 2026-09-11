import bpy, os
path=r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\textures\tile_00_satellite.png'
obj=bpy.data.objects.get('TERRAIN_DeltaParnaiba_512m_00')
if obj:
    bpy.context.view_layer.objects.active=obj; obj.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT'); bpy.ops.mesh.select_all(action='SELECT'); bpy.ops.uv.smart_project(island_margin=.02); bpy.ops.object.mode_set(mode='OBJECT')
    mat=bpy.data.materials.get('MAT_Satellite_Terrain') or bpy.data.materials.new('MAT_Satellite_Terrain'); mat.use_nodes=True
    nt=mat.node_tree; nt.nodes.clear(); out=nt.nodes.new('ShaderNodeOutputMaterial'); bs=nt.nodes.new('ShaderNodeBsdfPrincipled'); tex=nt.nodes.new('ShaderNodeTexImage'); tex.image=bpy.data.images.load(path,check_existing=True); bs.inputs['Roughness'].default_value=.9; nt.links.new(tex.outputs['Color'],bs.inputs['Base Color']); nt.links.new(bs.outputs['BSDF'],out.inputs['Surface']); obj.data.materials.clear(); obj.data.materials.append(mat)
for n in ['WATER','ROADS','VEGETATION']:
    if not bpy.data.collections.get(n): c=bpy.data.collections.new(n); bpy.context.scene.collection.children.link(c)
sc=bpy.context.scene; sc['satellite_source']='Esri World Imagery export'; sc['satellite_license_note']='Attribution required; verify terms before commercial redistribution'; sc['tile_texture']='tile_00_satellite.png'; out=r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\blender\delta_parnaiba_tile_00_textured.blend'; bpy.ops.wm.save_as_mainfile(filepath=out); print('SAVED',out)
