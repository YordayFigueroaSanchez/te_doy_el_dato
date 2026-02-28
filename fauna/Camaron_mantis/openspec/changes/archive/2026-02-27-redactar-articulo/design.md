## Context

El proyecto "Te Doy el Dato" produce artículos de divulgación científica en español sobre fauna. Para el camarón mantis (*Odontodactylus scyllarus*), se dispone de una fuente exhaustiva en `sources/info.md` que cubre taxonomía, biomecánica, visión, hábitat, comportamiento, dieta y conservación. El artículo final debe transformar ese material técnico denso en una pieza accesible y cautivadora sin sacrificar rigor.

El `readme.md` actual contiene un resumen básico del animal. El artículo será una pieza más extensa y completa que existirá como documento independiente.

## Goals / Non-Goals

**Goals:**
- Producir un artículo de divulgación científica completo en español (~2000-3000 palabras).
- Adaptar toda la terminología técnica en inglés a equivalentes descriptivos en español.
- Mantener un tono de asombro científico: fascinante pero verificable.
- Estructurar el contenido en secciones claras con progresión lógica.
- Incluir al menos una tabla comparativa de fuerza de impacto.
- Usar nombres científicos en cursiva según convención.

**Non-Goals:**
- No se traduce literalmente `sources/info.md`; se reescribe para un público general.
- No se crean assets multimedia (imágenes, videos) como parte de este cambio.
- No se modifica la estructura del proyecto ni se añaden dependencias técnicas.
- No se genera contenido en otro idioma que no sea español.

## Decisions

### 1. Estructura del artículo en 8 secciones temáticas
**Decisión:** Organizar el artículo en: Introducción, Ficha Técnica, Biomecánica, Sistema Visual, Hábitat, Comportamiento, Dieta/Conservación y Datos Curiosos.
**Razón:** Refleja la progresión natural del material fuente y permite lectura parcial por secciones. Alternativa descartada: estructura narrativa continua sin secciones — dificulta la consulta rápida.

### 2. Adaptación de términos Smasher/Spearer
**Decisión:** Usar "Triturador" para *Smasher* y "Arponero" para *Spearer*, con el término original en inglés entre paréntesis la primera vez.
**Razón:** Son traducciones descriptivas que comunican la función mecánica. Alternativa descartada: mantener los términos en inglés — excluye al lector que no domina el idioma.

### 3. Tono divulgativo con analogías cotidianas
**Decisión:** Emplear analogías accesibles (bala calibre .22, temperatura del Sol, chalecos antibalas) para explicar magnitudes técnicas.
**Razón:** El público objetivo no es especialista; las analogías anclan conceptos abstractos en experiencias reconocibles.

### 4. Archivo de salida en `docs/articulo.md`
**Decisión:** El artículo final se ubicará en `docs/articulo.md`.
**Razón:** Sigue la convención `docs_dir` del `config.yaml` y mantiene separación entre fuentes y producto final.

## Risks / Trade-offs

- **[Simplificación excesiva]** → Mitigación: Incluir siempre el término científico correcto junto a la explicación simplificada.
- **[Extensión del artículo]** → Mitigación: Limitar a ~3000 palabras; secciones autocontenidas permiten cortar sin perder coherencia.
- **[Precisión de datos numéricos]** → Mitigación: Todos los datos (velocidades, temperaturas, fuerzas) se toman directamente de `sources/info.md` sin modificar valores.
