## Context

El artículo `docs/articulo.md` ya aplica adaptaciones terminológicas para los términos principales (Smasher → Triturador, Spearer → Arponero, LaMSA expandido). Sin embargo, varios términos técnicos en inglés aparecen con formato inconsistente: algunos usan el patrón "español (*inglés*)" y otros no. La spec `adaptacion-terminologica` actual solo formaliza 4 requisitos y no cubre términos como *herringbone*, *saddle spring*, *midband*, *Dear Enemy* ni la expansión de *Latch-Mediated Spring Actuation*.

Estado actual de los términos en el artículo:

- `espiga (*herringbone*)` — ya adaptado inline, sin regla formal
- `silla de montar (*saddle spring*)` — ya adaptado inline, sin regla formal
- `banda media (*midband*)` — ya adaptado inline, sin regla formal
- `"*Dear Enemy*" (enemigo querido)` — adaptado con formato distinto al patrón estándar
- `Actuación de Resorte Mediada por Pestillo (LaMSA...)` — expandido, ya cubierto parcialmente

## Goals / Non-Goals

**Goals:**

- Formalizar en la spec todos los términos técnicos inglés→español que aparecen en el artículo.
- Establecer un patrón de formato único y consistente: traducción en español seguida de (*original en inglés*) en la primera mención.
- Normalizar el formato de "Dear Enemy" para que siga el mismo patrón que los demás términos.
- Asegurar que futuras ediciones del artículo mantengan la consistencia terminológica.

**Non-Goals:**

- No se añade contenido nuevo al artículo; solo se ajusta el formato de los términos existentes.
- No se modifican los requisitos existentes de Smasher/Spearer, cursivas, LaMSA ni unidades SI.
- No se crea un glosario independiente (eso sería un cambio distinto).

## Decisions

### 1. Patrón único: "Español (*English*)"

**Decisión:** Todos los términos técnicos adaptados seguirán el patrón `Traducción español (*término inglés*)` en su primera aparición. Las menciones subsiguientes usarán solo el término en español.
**Razón:** Es el patrón que ya usa la mayoría de los términos (espiga, silla de montar, banda media). Unificar "Dear Enemy" a este formato elimina la excepción actual. Alternativa descartada: usar comillas españolas en lugar de cursiva — no es consistente con el resto del artículo.

### 2. Añadir requisitos como ADDED, no MODIFIED

**Decisión:** Los nuevos términos se añaden como requisitos ADDED a la spec, ya que no cambian el comportamiento de ningún requisito existente — solo amplían la cobertura.
**Razón:** Los 4 requisitos existentes permanecen intactos. Usar MODIFIED implicaría reescribirlos sin necesidad.

## Risks / Trade-offs

- **[Formato de "Dear Enemy" cambia]** → Mitigación: El cambio es menor (reordenar la presentación del término). El significado no cambia.
- **[Lista de términos incompleta]** → Mitigación: Se cubren todos los términos en inglés identificados actualmente en el artículo. Si aparecen nuevos en futuras ediciones, se puede extender la spec.
