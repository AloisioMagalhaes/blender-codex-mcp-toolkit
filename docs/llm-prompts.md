# Prompts especializados por LLM e skill

Este catálogo torna explícito qual modelo usar e qual instrução enviar ao Codex conectado ao Blender MCP.

## Regra rápida de seleção

- **GPT-6 Astra**: modelagem hard-surface, personagens, escultura, retopologia, rigging, revisão visual, referências, exportação e tarefas que exigem várias etapas.
- **GPT-5.6 Sol**: materiais, nodes, UV, iluminação, organização de cena, correções e scripts repetitivos.
- **GPT-5.6 Luna**: operações curtas e determinísticas: criar primitivas, renomear, mover, aplicar escala, salvar e consultar a cena.

## Prompt-base

```text
Use o Blender MCP conectado à instância ativa. Antes de editar, inspecione a cena, unidades, coleções e objetos selecionados. Execute a tarefa em etapas verificáveis, mantendo operações idempotentes. Use Python bpy quando isso for mais preciso que a UI. Após cada etapa, valide nomes, transformações, escala aplicada, normais, malha fechada e ausência de geometria não manifold. Salve o arquivo Blender no caminho informado e relate o que foi alterado, o que foi inferido e qualquer limitação.
```

## Matriz de prompts

### blender3d / blender-director — Astra

```text
Atue como diretor técnico de Blender. Analise o objetivo, decomponha-o em etapas de referência, blockout, modelagem, validação e entrega. Coordene coleções, nomes, unidades e dependências. Não avance para detalhes antes de validar escala e silhueta. Use o Blender MCP e produza um relatório de verificação ao final.
```

### blender-modeler / hard-surface / prop-artist — Astra

```text
Modele o objeto como hard-surface fabricável. Comece pelas dimensões principais, aplique escala, use bevels controlados, normais ponderadas e booleans limpos. Preserve espessuras plausíveis, raios de fabricação e separação por peças. Valide caixa delimitadora, manifold, normais e nomes antes de salvar.
```

### character-artist / sculpting / stylized-style — Astra

```text
Crie o personagem em fases: referências e proporção, blockout com Mirror, silhueta, formas secundárias, escultura, retopologia, UV, materiais, rig e testes de deformação. Mantenha a identidade visual observada separada das inferências. Não invente detalhes ocultos sem marcá-los como reconstruídos.
```

### blender3d-references / environment-artist — Astra

```text
Organize referências por vista e licença. Alinhe frontal, traseira, laterais, superior e inferior a um mesmo eixo e escala. Registre observações, inferências e incertezas. Use as imagens apenas como guia e construa uma cena coerente, verificando proporções entre todas as vistas.
```

### materials / texture-workflow / lookdev — Sol

```text
Crie materiais Principled compatíveis com glTF. Separe Base Color, Roughness, Metallic, Normal e AO quando apropriado. Use nós simples, nomeados e exportáveis. Verifique UV, escala de textura, repetição e aparência no viewport Material Preview e em render.
```

### geometry-nodes / procedural-modeling — Astra

```text
Construa o sistema procedural com parâmetros expostos e nomes claros. Use Geometry Nodes apenas onde reduz repetição ou mantém controle paramétrico. Crie uma versão aplicada para exportação e valide limites, instâncias, orientação e desempenho.
```

### rigging / animation / physics-sim — Astra

```text
Monte uma armature limpa, hierarquia previsível e deformação testável. Faça weight paint por regiões, teste extremos de pose e aplique física somente a elementos flexíveis. Nomeie ações, ossos e colisões para o destino final e registre falhas de deformação.
```

### uv-workflow / retopology / asset-optimization — Astra

```text
Prepare o modelo para produção: aplique transformações, corrija normais, faça retopologia nas áreas de deformação, abra UVs sem sobreposição indevida e crie LODs coerentes. Relate polígonos, materiais, ilhas UV e problemas restantes.
```

### godot-export / unity-export / unreal-export — Astra

```text
Prepare exportação para o motor indicado. Use nomes estáveis, escala correta, root simples, materiais compatíveis, colisões COL_ e animações AN_. Exporte uma cópia de teste, reimporte quando possível e valide dimensões, armature, materiais, animações e colisões.
```

### rendering / lighting / camera-cinematography — Sol

```text
Configure câmera, iluminação e render para comunicar claramente a forma. Use uma câmera de inspeção ortográfica e uma câmera de apresentação. Nomeie luzes, defina resolução e salve renders de validação sem alterar a geometria.
```

### qa-review / export-pipeline — Sol

```text
Faça uma revisão técnica sem remodelar silenciosamente. Verifique escala, unidades, transforms, manifold, normais, materiais, coleções, nomes, bounding boxes e arquivos de saída. Liste cada problema com objeto, causa, severidade e correção aplicada.
```

### operações rápidas — Luna

```text
Na cena ativa, execute somente esta operação: [descreva a ação]. Não altere outros objetos. Confirme o objeto afetado, transformação resultante e caminho de salvamento.
```

## Fluxo recomendado

1. Astra: referências, planejamento, blockout e modelagem estrutural.
2. Sol: materiais, UV, iluminação e limpeza de cena.
3. Astra: escultura, rigging, retopologia e exportação de personagem.
4. Sol: QA final e relatório.
5. Luna: pequenas correções determinísticas durante a revisão.
