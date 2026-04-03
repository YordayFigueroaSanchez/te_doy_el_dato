## ADDED Requirements

### Requirement: El artículo DEBE incluir una tabla comparativa de fuerza de impacto

El artículo SHALL contener una tabla en formato Markdown que compare la fuerza de impacto del camarón mantis con otros referentes conocidos (por ejemplo: golpe humano, peso del animal, bala calibre .22).

#### Scenario: Tabla comparativa presente con al menos 3 filas

- **WHEN** se revisa el artículo
- **THEN** existe una tabla Markdown de comparación de fuerza con al menos 3 filas de datos

#### Scenario: Tabla incluye unidades y fuentes coherentes

- **WHEN** se leen los valores de la tabla
- **THEN** cada fila incluye magnitud numérica y unidad (Newtons, m/s, o g)

### Requirement: Los datos numéricos destacados DEBEN resaltarse con formato especial

Los datos que generan impacto (velocidades, temperaturas, fuerzas) SHALL presentarse en **negrita** o en un bloque destacado para facilitar el escaneo visual del lector.

#### Scenario: Dato de temperatura de cavitación en negrita

- **WHEN** se menciona la temperatura de 4,400 °C
- **THEN** el valor aparece en **negrita** o dentro de un callout/bloque destacado

### Requirement: El artículo DEBE usar encabezados jerárquicos consistentes

La estructura del artículo SHALL usar encabezados Markdown jerárquicos: `#` para el título, `##` para secciones principales, `###` para subsecciones.

#### Scenario: Jerarquía de encabezados correcta

- **WHEN** se analiza la estructura de encabezados del artículo
- **THEN** hay exactamente un `#` (título), múltiples `##` (secciones), y `###` opcionales (subsecciones), sin saltos de nivel
