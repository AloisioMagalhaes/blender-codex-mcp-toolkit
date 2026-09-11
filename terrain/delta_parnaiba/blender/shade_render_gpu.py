import bpy
from mathutils import Vector
src=r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\blender\delta_parnaiba_tile_00_layers.blend'
out=r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\blender\delta_parnaiba_tile_00_gpu_render.blend'
bpy.ops.wm.open_mainfile(filepath=src)
def shader(name,color,rough=.6,trans=0):
 m=bpy.data.materials.get(name) or bpy.data.materials.new(name); m.use_nodes=True; n=m.node_tree.nodes; n.clear(); o=n.new('ShaderNodeOutputMaterial'); b=n.new('ShaderNodeBsdfPrincipled'); b.inputs['Base Color'].default_value=(*color,1); b.inputs['Roughness'].default_value=rough
 if trans: b.inputs['Transmission Weight'].default_value=trans; b.inputs['IOR'].default_value=1.333
 m.node_tree.links.new(b.outputs['BSDF'],o.inputs['Surface']); return m
for name,col,rough,tr in [('MAT_Water_Shaded',(.015,.12,.2),.12,.35),('MAT_Road_Shaded',(.12,.08,.045),.95,0),('MAT_Vegetation_Shaded',(.035,.18,.025),.88,0)]:
 m=shader(name,col,rough,tr)
 for o in bpy.data.objects:
  if (name.startswith('MAT_Water') and o.name.startswith('WATER_')) or (name.startswith('MAT_Road') and o.name.startswith('ROAD_')) or (name.startswith('MAT_Vegetation') and o.name.startswith('VEG_')): o.data.materials.clear(); o.data.materials.append(m)
sc=bpy.context.scene; gpu='EEVEE_FALLBACK'; sc.render.engine='BLENDER_EEVEE_NEXT'
try:
 p=bpy.context.preferences.addons['cycles'].preferences; p.compute_device_type='OPTIX'; p.get_devices()
 if any(d.type!='CPU' for d in p.devices): gpu='OPTIX_AVAILABLE'
except: pass
sc['render_device']=gpu; sc.render.resolution_x=1280; sc.render.resolution_y=720; sc.render.resolution_percentage=100; sc.render.image_settings.file_format='PNG'; sc.render.filepath=r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\blender\tile_00_gpu_shaded.png'
bpy.ops.render.render(write_still=True); bpy.ops.wm.save_as_mainfile(filepath=out); print('SAVED',out,'DEVICE',gpu)
