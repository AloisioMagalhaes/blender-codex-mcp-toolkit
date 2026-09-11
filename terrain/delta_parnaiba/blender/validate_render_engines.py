import bpy, os, time
src=r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\blender\delta_parnaiba_tile_00_physics.blend'
root=r'C:\Users\educa\Desktop\prj\blender-codex-mcp-toolkit\terrain\delta_parnaiba\blender'
bpy.ops.wm.open_mainfile(filepath=src); sc=bpy.context.scene; sc.render.resolution_x=640; sc.render.resolution_y=360; sc.render.resolution_percentage=100
results=[]
for engine,label in [('BLENDER_EEVEE_NEXT','eevee'),('BLENDER_WORKBENCH','workbench'),('CYCLES','cycles')]:
 try:
  sc.render.engine=engine; sc.render.filepath=os.path.join(root,'validation_'+label+'.png'); t=time.time(); bpy.ops.render.render(write_still=True); results.append(f'{label}: OK {time.time()-t:.2f}s {sc.render.filepath}')
 except Exception as e: results.append(f'{label}: ERROR {e}')
sc.render.engine='BLENDER_EEVEE_NEXT'; report=os.path.join(root,'render_validation.txt'); open(report,'w',encoding='utf8').write('\n'.join(results)); bpy.ops.wm.save_as_mainfile(filepath=os.path.join(root,'delta_parnaiba_render_validated.blend')); print('\n'.join(results))
