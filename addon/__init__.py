bl_info = {
    'name': 'Local Blender MCP Bridge',
    'author': 'Codex',
    'version': (0, 2, 0),
    'blender': (3, 0, 0),
    'location': 'Preferences > Add-ons',
    'category': 'Interface',
    'description': 'Local HTTP bridge for safe Blender automation from MCP clients.',
}

import bpy, json, threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

_server = None
_queue = []
_lock = threading.Lock()

def _scene_info():
    return {'scene': bpy.context.scene.name,
            'objects': len(bpy.context.scene.objects),
            'meshes': sum(1 for o in bpy.context.scene.objects if o.type == 'MESH'),
            'filepath': bpy.data.filepath}

def _collections():
    return [{'name': c.name, 'objects': [o.name for o in c.objects]} for c in bpy.data.collections]

def _run_pending():
    with _lock:
        jobs = _queue[:]
        _queue.clear()
    for job in jobs:
        try:
            ns = {'bpy': bpy}
            exec(job['code'], ns, ns)
            job['result'] = ns.get('result', 'ok')
            job['status'] = 200
        except Exception as e:
            job['result'] = 'Error: ' + repr(e)
            job['status'] = 500
        job['done'].set()
    return 0.05

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_): pass
    def _send(self, status, payload):
        raw = json.dumps(payload, default=str).encode()
        self.send_response(status); self.send_header('Content-Type','application/json')
        self.send_header('Content-Length', str(len(raw))); self.end_headers(); self.wfile.write(raw)
    def do_GET(self):
        if self.path == '/scene_info': self._send(200, _scene_info())
        elif self.path == '/health': self._send(200, {'ok': True, 'addon': bl_info['name'], 'version': '.'.join(map(str, bl_info['version'])), 'port': 9876})
        elif self.path == '/collections': self._send(200, _collections())
        else: self._send(404, {'error':'not found'})
    def do_POST(self):
        if self.path != '/execute': self._send(404, {'error':'not found'}); return
        n = int(self.headers.get('Content-Length','0')); body = json.loads(self.rfile.read(n) or '{}')
        import threading as th
        job = {'code': body.get('code',''), 'done': th.Event(), 'status': 500, 'result': None}
        with _lock: _queue.append(job)
        if not job['done'].wait(120): self._send(504, {'error':'timeout'}); return
        self._send(job['status'], {'result': job['result']})

def start_server():
    global _server
    if _server: return
    _server = ThreadingHTTPServer(('127.0.0.1', 9876), Handler)
    threading.Thread(target=_server.serve_forever, daemon=True).start()
    bpy.app.timers.register(_run_pending, first_interval=0.05, persistent=True)

def stop_server():
    global _server
    if _server: _server.shutdown(); _server.server_close(); _server = None

def register(): start_server()
def unregister(): stop_server()

class MCPBridgePanel(bpy.types.Panel):
    bl_label = 'Local Blender MCP Bridge'
    bl_idname = 'VIEW3D_PT_local_blender_mcp_bridge'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'MCP Bridge'
    def draw(self, context):
        layout = self.layout
        layout.label(text='Servidor: 127.0.0.1:9876')
        layout.label(text='Status: ativo' if _server else 'Status: parado')
        layout.label(text=f'Objetos: {len(bpy.context.scene.objects)}')

_old_register, _old_unregister = register, unregister
def register():
    _old_register()
    bpy.utils.register_class(MCPBridgePanel)
def unregister():
    if hasattr(bpy.types, 'MCPBridgePanel'): pass
    try: bpy.utils.unregister_class(MCPBridgePanel)
    except RuntimeError: pass
    _old_unregister()

if __name__ == '__main__': register()
