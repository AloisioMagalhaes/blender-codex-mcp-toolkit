# Ativação em um novo chat

Cole este texto no início de uma conversa nova:

```text
O Blender está aberto com o addon Local Blender MCP Bridge ativo.
Use http://127.0.0.1:9876 para consultar e editar a cena.
Antes de qualquer mudança, consulte /health e /scene_info.
Liste os objetos antes de editar ou remover.
Execute comandos no Blender e valide o resultado depois.
Use as skills Blender3D relevantes para modelagem, hard surface, materiais,
UV, Texture Paint, renderização, otimização, validação e exportação.
Não responda apenas com instruções: execute a operação na cena aberta.
```

O bridge não carrega skills dentro do Blender. As skills são workflows usados pelo agente para decidir como executar comandos Python no Blender.
