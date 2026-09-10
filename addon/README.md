# Local Blender MCP Bridge

Instale a pasta `blender_mcp_addon` em `Edit > Preferences > Add-ons > Install...` (compacte-a como ZIP se necessário), ative o addon e reinicie o Blender. O bridge escuta `127.0.0.1:9876`.

Endpoints:

- `GET /scene_info`
- `POST /execute` com JSON `{\"code\": \"...\"}`

O código é executado na thread principal do Blender por meio de uma fila; use somente clientes locais confiáveis.
