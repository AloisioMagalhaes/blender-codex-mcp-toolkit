import bpy
from mathutils import Vector
src=r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\blender\delta_parnaiba_tile_00_final.blend'
out=r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\blender\delta_parnaiba_tile_00_layers.blend'
bpy.ops.wm.open_mainfile(filepath=src)
def col(n):
 c=bpy.data.collections.get(n) or bpy.data.collections.new(n)
 if c.name not in bpy.context.scene.collection.children: bpy.context.scene.collection.children.link(c)
 return c
water=col('WATER'); roads=col('ROADS'); veg=col('VEGETATION')
def mat(n,c):
 m=bpy.data.materials.get(n) or bpy.data.materials.new(n); m.diffuse_color=(*c,1); return m
mwater=mat('MAT_Water',(0.02,.16,.22)); mroad=mat('MAT_Road',(.16,.12,.08)); mveg=mat('MAT_Vegetation',(.08,.24,.07))
terrain=bpy.data.objects.get('TERRAIN_DeltaParnaiba_512m_00'); z=sum(v.co.z for v in terrain.data.vertices)/len(terrain.data.vertices) if terrain else 0
bpy.ops.mesh.primitive_plane_add(size=180, location=(110,80,z+.4)); w=bpy.context.view_layer.objects.active; w.name='WATER_Estuary_Indicative'; w.data.materials.append(mwater); [c.objects.unlink(w) for c in list(w.users_collection) if c!=water]; water.objects.link(w)
curve=bpy.data.curves.new('ROAD_Trail_Curve','CURVE'); curve.dimensions='3D'; curve.bevel_depth=2.2; spl=curve.splines.new('BEZIER'); spl.bezier_points.add(3)
for p,co in zip(spl.bezier_points,[(-230,-180,z+1),(-80,-60,z+2),(90,40,z+1),(230,180,z+2)]): p.co=co; p.handle_left_type=p.handle_right_type='AUTO'
r=bpy.data.objects.new('ROAD_Trail_Indicative',curve); roads.objects.link(r); r.data.materials.append(mroad)
for i in range(36):
 x=-240+(i*83)%480; y=-220+((i*137)%440); bpy.ops.mesh.primitive_cone_add(vertices=8,radius1=3.5,radius2=.4,depth=10,location=(x,y,z+5)); t=bpy.context.view_layer.objects.active; t.name=f'VEG_Mangrove_{i+1:03d}'; t.data.materials.append(mveg); [c.objects.unlink(t) for c in list(t.users_collection) if c!=veg]; veg.objects.link(t)
bpy.context.scene['layers_status']='Indicative placeholders; replace with licensed vector data'; bpy.ops.wm.save_as_mainfile(filepath=out); print('SAVED',out)
