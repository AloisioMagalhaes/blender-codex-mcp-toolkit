# Delta do Parnaíba — workflow DEM para Blender/Godot

Área inicial: `lat -3.0833..-2.6167`, `lon -42.4833..-41.1500`.
Centro operacional: `-2.8653, -41.8542`. Raio aproximado: 78 km.

## Dados baixados

Os seis tiles SRTM 1 arc-second (`S02/S03W041..W043`) estão em `dem/` em formato HGT. A fonte é o espelho público AWS Terrain Tiles, derivado do Shuttle Radar Topography Mission. O HGT é mantido sem alteração para permitir auditoria e reproces-samento.

## Convenções Godot 4.5+

- tiles de terreno: 512 x 512 m;
- heightmap por tile: 257 x 257 amostras;
- textura de terreno: 2048 x 2048 px;
- LODs: 1.0, 0.5 e 0.25;
- colisão separada e simplificada;
- água, estradas e vegetação em camadas independentes.

O SRTM fornece o relevo-base. Fotogrametria, LiDAR ou escaneamento local devem substituir/refinar somente tiles prioritários, pois não há cobertura uniforme de alta resolução para toda a área.

Fontes: [SRTM/AWS Terrain Tiles](https://registry.opendata.aws/terrain-tiles/), [KBA Delta do Parnaíba](https://www.keybiodiversityareas.org/en/site/factsheet/22227), [SGB Geodiversidade](https://rigeo.sgb.gov.br/items/58d5aba0-f1db-46da-af8d-8aef7591b2a0).
