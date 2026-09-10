# Troubleshooting

Se o addon aparecer ativado mas não houver resposta:

```python
import bpy, blender_mcp_addon
print(bpy.context.preferences.addons.get("blender_mcp_addon"))
print(blender_mcp_addon._server)
```

Depois teste:

```powershell
Test-NetConnection 127.0.0.1 -Port 9876
Invoke-RestMethod http://127.0.0.1:9876/scene_info
```

Se o Blender reportar módulos duplicados, remova pastas de backup com pontos do diretório de addons. O diretório deve conter somente uma instalação do módulo `blender_mcp_addon`.
