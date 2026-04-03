## Context

El proyecto "te_doy_el_dato" produce artículos divulgativos en español sobre fauna, estructurados como guiones en Markdown. Ya existen artículos de referencia para narval y salmón (`example/narval.md`, `example/salmon.md`) que definen el estilo y tono esperado.

Para el camarón mantis pavo real (*Odontodactylus scyllarus*), se cuenta con:

- Una fuente de datos completa en `sources/info.md`.
- Un borrador inicial en `docs/articulo.md` que cubre la estructura pero aún no cumple todas las specs.
- Tres specs activas: `escribir-articulo` (estructura y contenido), `adaptacion-terminologica` (localización de términos técnicos al español) y `elementos-visuales` (formato, tablas y jerarquía de encabezados).

El entregable es un archivo `guion.md` en la raíz del proyecto que integre todos los requisitos.

## Goals / Non-Goals

**Goals:**

- Producir `guion.md` cumpliendo las 3 specs simultáneamente.
- Respetar la estructura de 9 secciones obligatorias en el orden definido por `escribir-articulo`.
- Aplicar todas las adaptaciones terminológicas (Triturador, Arponero, espiga, silla de montar, banda media, Enemigo Querido, LaMSA expandido).
- Incluir los elementos visuales requeridos (tabla comparativa de fuerza, datos en negrita, jerarquía `#`/`##`/`###`).
- Mantener el rango de 2000–3500 palabras.
- Usar `sources/info.md` como fuente de verdad sin inventar datos contradictorios.

**Non-Goals:**

- No se modifica ninguna spec existente.
- No se generan imágenes ni recursos multimedia.
- No se cambia la estructura del repositorio.
- No se produce contenido en idiomas distintos al español.

## Decisions

### 1. Archivo de salida: `guion.md` en la raíz

**Decisión**: El artículo se escribe en `guion.md` (raíz del proyecto), no en `docs/articulo.md`.
**Razón**: La spec `escribir-articulo` define explícitamente `guion.md` como ruta de salida. El archivo `docs/articulo.md` es un borrador previo y no el entregable final.

### 2. Jerarquía de encabezados: `#` título + `##` secciones

**Decisión**: Usar `#` para el título único del artículo y `##` para las 9 secciones principales, con `###` para subsecciones internas.
**Razón**: La spec `elementos-visuales` requiere jerarquía consistente (`#` → `##` → `###`). La spec `escribir-articulo` permite esta variante siempre que se mantengan los títulos y el orden de secciones. Esto da mejor estructura semántica que usar solo `###`.

### 3. Imagen de portada con nombre por defecto

**Decisión**: Usar `camaron_mantis_portada_001.png` como nombre del archivo de portada.
**Razón**: La spec indica usar este nombre por defecto cuando no se provee uno concreto.

### 4. Tono y estilo basado en los ejemplos existentes

**Decisión**: Seguir el patrón de narval.md: párrafos cortos, gancho inicial con pregunta retórica, transiciones narrativas, cierre con invitación.
**Razón**: La spec `escribir-articulo` define explícitamente que los ejemplos son la referencia de estilo.

### 5. Tabla comparativa de fuerza dentro de la sección de Biomecánica

**Decisión**: Ubicar la tabla comparativa de fuerza de impacto (requerida por `elementos-visuales`) dentro de la sección "Biomecánica: el golpe".
**Razón**: Es la sección temáticamente más relevante. La tabla aporta contexto inmediato a la explicación del mecanismo de golpe.

### 6. Datos curiosos en formato narrativo

**Decisión**: Redactar los datos curiosos como párrafos cortos (no lista con viñetas).
**Razón**: La spec `escribir-articulo` indica que la sección debe ser preferiblemente narrativa, y el artículo debe evitar listas con viñetas en el cuerpo.

## Risks / Trade-offs

- **[Conteo de palabras fuera de rango]** → Verificar conteo al final y ajustar secciones si es necesario. El rango 2000–3500 da margen suficiente.
- **[Datos faltantes en la fuente]** → Para detalles no cubiertos por `sources/info.md`, usar información general del género/familia sin inventar precisión falsa, como indica la spec.
- **[Conflicto entre specs de encabezados]** → La spec `escribir-articulo` prefiere `###` pero permite `##` si se mantiene consistencia. La spec `elementos-visuales` requiere jerarquía `#`/`##`/`###`. Se resuelve a favor de la jerarquía completa, que satisface ambas.
- **[Nombre de portada sin imagen real]** → El archivo `camaron_mantis_portada_001.png` puede no existir aún. Esto es aceptable según la spec, que indica que el sistema consumidor deberá generar/colocar la imagen.
