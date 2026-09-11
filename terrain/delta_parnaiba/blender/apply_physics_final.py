import bpy
src=r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\blender\delta_parnaiba_tile_00_gpu_render.blend'
out=r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\blender\delta_parnaiba_tile_00_physics.blend'
bpy.ops.wm.open_mainfile(filepath=src); sc=bpy.context.scene
terrain=bpy.data.objects.get('TERRAIN_DeltaParnaiba_512m_00')
if terrain and not terrain.modifiers.get('Collision_Terrain'): terrain.modifiers.new('Collision_Terrain','COLLISION')
water=bpy.data.objects.get('WATER_Estuary_Indicative')
if water:
 sub=water.modifiers.get('Subdivision_Water') or water.modifiers.new('Subdivision_Water','SUBSURF'); sub.levels=2; sub.render_levels=2
 if not water.modifiers.get('Cloth_Water'): water.modifiers.new('Cloth_Water','CLOTH')
 cloth=water.modifiers.get('Cloth_Water').point_cache; cloth.frame_start=1; cloth.frame_end=40
sc.frame_set(30); sc['physics_setup']='Terrain collision, cloth water, wind field'; sc['physics_frame']=30; sc.render.filepath=r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\blender\tile_00_physics_render.png'; bpy.ops.render.render(write_still=True); bpy.ops.wm.save_as_mainfile(filepath=out); print('SAVED',out)
bpy.ops.object.effector_add(type='WIND', location=(0,-100,80)); wind=bpy.context.view_layer.objects.active; wind.name='PHYS_Wind_Field'; wind.field.strength=12; wind.field.noise=1.5
