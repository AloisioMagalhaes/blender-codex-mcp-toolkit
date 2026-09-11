import bpy, os
obj=bpy.data.objects.get('TERRAIN_DeltaParnaiba_512m_00')
if not obj: raise RuntimeError('Terrain object not found')
if not obj.data.uv_layers: bpy.context.view_layer.objects.active=obj; obj.select_set(True); bpy.ops.object.mode_set(mode='EDIT'); bpy.ops.mesh.select_all(action='SELECT'); bpy.ops.uv.smart_project(island_margin=.02); bpy.ops.object.mode_set(mode='OBJECT')
img=bpy.data.images.get('tile_00_satellite.png')
if img: img.pack()
mat=bpy.data.materials.get('MAT_Satellite_Terrain'); mat.use_nodes=True
if mat.node_tree.nodes.get('Image Texture') is None:
    tex=mat.node_tree.nodes.new('ShaderNodeTexImage'); tex.name='Image Texture'; tex.image=img
    bs=next((n for n in mat.node_tree.nodes if n.type=='BSDF_PRINCIPLED'),None) or mat.node_tree.nodes.new('ShaderNodeBsdfPrincipled'); out=next((n for n in mat.node_tree.nodes if n.type=='OUTPUT_MATERIAL'),None) or mat.node_tree.nodes.new('ShaderNodeOutputMaterial'); mat.node_tree.links.new(tex.outputs['Color'],bs.inputs['Base Color']); mat.node_tree.links.new(bs.outputs['BSDF'],out.inputs['Surface'])
sc=bpy.context.scene; sc.render.engine='BLENDER_EEVEE_NEXT'; sc.render.resolution_x=1024; sc.render.resolution_y=768; sc.render.resolution_percentage=100
for o in list(bpy.data.objects):
    if o.type=='CAMERA': bpy.data.objects.remove(o,do_unlink=True)
bpy.ops.object.camera_add(location=(0,-620,480)); cam=bpy.context.object; cam.name='CAM_Terrain_Overview'; sc.camera=cam
def track(o,pt): o.rotation_euler=(Vector(pt)-o.location).to_track_quat('-Z','Y').to_euler()
from mathutils import Vector
track(cam,(0,0,0)); cam.data.lens=48
bpy.ops.object.light_add(type='SUN', location=(0,0,500)); sun=bpy.context.object; sun.name='SUN_Terrain'; sun.data.energy=3.0; sun.rotation_euler=(.35,-.5,-.3)
bpy.ops.object.light_add(type='AREA', location=(0,-200,300)); area=bpy.context.object; area.data.energy=1200; area.data.shape='DISK'; area.data.size=400; track(area,(0,0,0))
sc.render.filepath=r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\blender\tile_00_preview.png'; bpy.ops.render.render(write_still=True)
out=r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\blender\delta_parnaiba_tile_00_final.blend'; bpy.ops.wm.save_as_mainfile(filepath=out); print('SAVED',out,'UV',len(obj.data.uv_layers),'IMAGE_PACKED',bool(img and img.packed_file))
