import bpy, os
src=r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\blender\delta_parnaiba_tile_00_physics.blend'
out=r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\blender\delta_parnaiba_tile_00_godot.blend'
glb=r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\godot\delta_parnaiba_tile_00.glb'
bpy.ops.wm.open_mainfile(filepath=src); terrain=bpy.data.objects.get('TERRAIN_DeltaParnaiba_512m_00')
if terrain:
 for name,ratio in [('LOD1',.5),('LOD2',.2)]:
  o=terrain.copy(); o.data=terrain.data.copy(); o.name='TERRAIN_DeltaParnaiba_512m_00_'+name; bpy.context.collection.objects.link(o); m=o.modifiers.new('Decimate_'+name,'DECIMATE'); m.ratio=ratio
 col=bpy.data.collections.get('COLLISION') or bpy.data.collections.new('COLLISION'); bpy.context.scene.collection.children.link(col)
 c=terrain.copy(); c.data=terrain.data.copy(); c.name='COL_Terrain_00'; col.objects.link(c); d=c.modifiers.new('Collision_Decimate','DECIMATE'); d.ratio=.08
sc=bpy.context.scene; sc['godot_export']='GLB'; sc['lods']='LOD0,LOD1,LOD2'; sc['collision']='COL_Terrain_00'; os.makedirs(os.path.dirname(glb),exist_ok=True)
for o in bpy.data.objects: o.select_set(o.name.startswith(('TERRAIN_','WATER_','ROAD_','VEG_','COL_')))
bpy.ops.wm.save_as_mainfile(filepath=out); print('SAVED',out)
