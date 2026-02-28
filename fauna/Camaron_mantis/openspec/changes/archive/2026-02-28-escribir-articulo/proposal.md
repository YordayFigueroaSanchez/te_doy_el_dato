## Why

El proyecto necesita generar el artículo divulgativo final (`guion.md`) sobre el camarón mantis pavo real, siguiendo el estilo narrativo de los ejemplos existentes (narval, salmón). Actualmente se cuenta con la fuente base (`sources/info.md`), las specs de contenido, adaptación terminológica y elementos visuales, pero falta producir el artículo definitivo que integre todos estos requisitos en un texto cohesivo de 2000–3500 palabras, listo para publicación o narración.

## What Changes

- Crear el archivo `guion.md` en la raíz del proyecto con el artículo completo del camarón mantis pavo real.
- Integrar las adaptaciones terminológicas definidas en la spec `adaptacion-terminologica` (Triturador/Arponero, cursivas en nombres científicos, expansión de LaMSA, adaptación de herringbone, saddle spring, midband, Dear Enemy).
- Aplicar los elementos visuales definidos en la spec `elementos-visuales` (tabla comparativa de fuerza, datos numéricos en negrita, jerarquía de encabezados consistente).
- Seguir la estructura de 9 secciones obligatorias definida en la spec `escribir-articulo`.
- Mantener el tono divulgativo, dinámico y con preguntas retóricas, consistente con los ejemplos de narval y salmón.

## Capabilities

### New Capabilities
- `generacion-guion`: Generación del artículo/guion final en Markdown integrando todas las specs existentes, la fuente base y el estilo de los ejemplos.

### Modified Capabilities
<!-- No se modifican requisitos de specs existentes; se implementan tal como están definidas. -->

## Impact

- Se crea un nuevo archivo `guion.md` en la raíz del proyecto.
- El artículo depende de `sources/info.md` como fuente de verdad para datos factuales.
- Debe cumplir simultáneamente las tres specs existentes: `escribir-articulo`, `adaptacion-terminologica` y `elementos-visuales`.
- No hay cambios en APIs, dependencias ni sistemas externos.
