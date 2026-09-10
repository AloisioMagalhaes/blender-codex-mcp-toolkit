# Blender Codex MCP Toolkit

Bridge local para controlar o Blender por HTTP a partir de ChatGPT/Codex, com exemplos de workflows para modelagem, materiais, Texture Paint, render e exportação.

## Instalação em outro computador

1. Instale Blender 4.x.
2. Abra `Edit > Preferences > Add-ons > Install...`.
3. Selecione a pasta `addon` deste repositório ou compacte-a como ZIP.
4. Ative **Local Blender MCP Bridge**.
5. No Console Python do Blender, confirme:

```python
import bpy
print(bpy.context.preferences.addons.get("blender_mcp_addon"))
```

6. Teste o servidor no PowerShell:

```powershell
Invoke-RestMethod http://127.0.0.1:9876/health
```

O servidor expõe `GET /health`, `GET /scene_info`, `GET /collections` e `POST /execute` com `{ "code": "..." }`.

## Uso com ChatGPT/Codex

Mantenha o Blender aberto e peça ao agente para executar operações no Blender MCP. O bridge executa scripts Python na thread principal do Blender. Use somente em ambiente local confiável; não exponha a porta 9876 à rede.

## Workflows Blender

O pacote documenta e suporta workflows para as skills Blender disponíveis: modelagem e hard surface, geometry nodes, materiais, UV, Texture Paint, iluminação, render, otimização, validação, impressão 3D e exportação para Unity, Unreal e Godot. As skills são instruções de trabalho; recursos externos como GPU, Ollama, APIs e plugins continuam sendo dependências opcionais.

## Conteúdo

- `addon/`: bridge Blender MCP.
- `assets/`: exemplo Blender com Suzanne usando material procedural de água.
- `docs/`: notas de integração e troubleshooting.
