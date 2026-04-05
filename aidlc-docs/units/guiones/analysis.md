# Análisis inicial del proyecto de guiones para videos

Fecha: 2026-04-03

Resumen ejecutivo

- Se han detectado 27 archivos de guiones tipo `short.txt` en `fauna/*/short.txt`.
- El contenido está mayoritariamente en español, con tono educativo y amigable, y uso frecuente de emojis en títulos.

Hallazgos principales

- Estructura común: referencias a archivos multimedia, enlaces (YouTube/Facebook), bloques numerados `short_###`, y listas `titles` o `titles:` con múltiples opciones.
- Variabilidad: no existe un frontmatter o esquema uniforme; algunos archivos incluyen campos `media`, `return`, `titles`, `resumen para los videos` y otros no.
- Contenido: muchos textos son suficientemente largos para más de 30s; varios ya incluyen títulos alternativos y resumenes, lo que facilita la estandarización.

Oportunidades y recomendaciones inmediatas

1. Estandarizar metadatos mediante un YAML frontmatter al inicio de cada guion. Campos sugeridos:
   - `id`, `species`, `language`, `duration_target`, `platforms`, `source_media`, `canonical_title`, `title_options`, `hashtags`, `tags`.
2. Adoptar una plantilla para Shorts (ejemplo):
   - Hook (1 línea), 3 hechos rápidos (1 oración cada uno), CTA (1 línea), caption sugerida, hashtags.
3. Generar un `manifest.csv` con una fila por archivo: `path,canonical_title,word_count,has_link,platforms,tags` para facilitar publicación masiva.
4. Crear un script `tools/parse_guiones.py` que extraiga metadata, calcule estimaciones de duración y produzca versiones condensadas (30s/60s).
5. Revisar y reducir los guiones que excedan la duración objetivo: priorizar frases cortas y etiquetas de tiempo para edición.

Próximos pasos (elige una o varias opciones)

- [A] Generar `manifest.csv` con metadatos extraídos de los 27 archivos.
- [B] Normalizar un ejemplo (por ejemplo `fauna/aguila_real/short.txt`) añadiendo YAML frontmatter y versión 30s/60s.
- [C] Crear `tools/parse_guiones.py` que automatice extracción y normalización.
- [D] Nada por ahora — dame recomendaciones de edición y formato solamente.

Si me indicas la opción(s) que prefieres, las ejecuto y actualizaré los archivos correspondientes.
