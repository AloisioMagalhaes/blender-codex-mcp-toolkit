import bpy, os, struct, math

HGT = r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\dem\S03W042.hgt'
OUT = r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\blender\delta_parnaiba_tile_00.blend'
N=3601
lat_center=-2.8653; lon_center=-41.8542
lat0=-3.0; lon0=-42.0
row=int(round((lat_center-lat0)*3600))
col=int(round((lon_center-lon0)*3600))
half=16; step=16
with open(HGT,'rb') as f: raw=f.read()
def elev(r,c):
    r=max(0,min(N-1,r)); c=max(0,min(N-1,c)); v=struct.unpack_from('>h',raw,2*(r*N+c))[0]; return 0 if v==-32768 else float(v)
verts=[]; faces=[]; size=512.0; count=33
for j in range(count):
    for i in range(count):
        x=(i/(count-1)-.5)*size; y=(j/(count-1)-.5)*size; z=elev(row+(half-j)*step,col+(i-half)*step)
        verts.append((x,y,z))
for j in range(count-1):
    for i in range(count-1):
        a=j*count+i; faces.append((a,a+1,a+1+count,a+count))
mesh=bpy.data.meshes.new('DEM_Tile_512m_Mesh'); mesh.from_pydata(verts,[],faces); mesh.update()
obj=bpy.data.objects.new('TERRAIN_DeltaParnaiba_512m_00',mesh); bpy.context.collection.objects.link(obj)
for p in mesh.polygons: p.use_smooth=True
bev=obj.modifiers.new('Terrain_Soften','BEVEL'); bev.width=.15; bev.segments=1
sc=bpy.context.scene; sc.unit_settings.system='METRIC'; sc.unit_settings.length_unit='METERS'; sc['terrain_source']='SRTM 1 arc-second / AWS Terrain Tiles'; sc['tile_size_m']=512; sc['center_lat']=lat_center; sc['center_lon']=lon_center; sc['sample_grid']='33x33'; sc['vertical_units']='meters'
bpy.ops.wm.save_as_mainfile(filepath=OUT)
print('SAVED',OUT,'VERTICES',len(verts),'FACES',len(faces),'ELEV_RANGE',min(v[2] for v in verts),max(v[2] for v in verts))
