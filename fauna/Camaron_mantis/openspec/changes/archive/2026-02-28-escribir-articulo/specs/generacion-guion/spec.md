## ADDED Requirements

### Requirement: El guion DEBE generarse en el archivo guion.md en la raíz del proyecto
El sistema SHALL escribir el artículo final en `guion.md` ubicado en la raíz del proyecto (`fauna/Camaron_mantis/guion.md`).

#### Scenario: Archivo de salida existe en la ruta correcta
- **WHEN** se completa la generación del artículo
- **THEN** el archivo `guion.md` existe en la raíz del proyecto

### Requirement: El guion DEBE basarse exclusivamente en sources/info.md como fuente de datos
El contenido factual del artículo SHALL derivarse de `sources/info.md`. No se MUST inventar datos que contradigan la fuente. Si un detalle no está especificado, se permite escribir de forma general sin precisión falsa.

#### Scenario: Datos factuales consistentes con la fuente
- **WHEN** se revisa cualquier dato factual del artículo (velocidades, temperaturas, clasificación taxonómica)
- **THEN** dicho dato es verificable en `sources/info.md` o es una generalización explícita

### Requirement: El guion DEBE contener entre 2000 y 3500 palabras
El artículo final SHALL tener una extensión mínima de 2000 palabras y máxima de 3500 palabras.

#### Scenario: Conteo de palabras dentro del rango
- **WHEN** se cuenta el total de palabras del archivo `guion.md`
- **THEN** el resultado está entre 2000 y 3500 palabras

### Requirement: El guion DEBE incluir imagen de portada como primera línea
La primera línea del documento SHALL ser una imagen Markdown de portada con el formato `![alt text](camaron_mantis_portada_001.png)`.

#### Scenario: Imagen de portada presente al inicio
- **WHEN** se lee la primera línea del archivo `guion.md`
- **THEN** contiene una referencia de imagen Markdown con nombre de archivo válido

### Requirement: El guion DEBE seguir la estructura de 9 secciones en orden
El artículo SHALL incluir las siguientes secciones en este orden exacto: Introducción y contexto evolutivo, Ficha Técnica, Biomecánica (Bouligand + LaMSA + cavitación), Sistema Visual, Hábitat y Distribución, Comportamiento e Inteligencia, Dieta y Estrategias de Caza, Conservación, Datos Curiosos. Cada sección MUST aparecer como encabezado `##`.

#### Scenario: Todas las secciones presentes en orden
- **WHEN** se extraen los encabezados `##` del artículo
- **THEN** aparecen las 9 secciones obligatorias en el orden especificado

### Requirement: El guion DEBE terminar con un cierre narrativo
El artículo SHALL concluir con un párrafo de 2–4 frases que invite al lector a seguir explorando contenido, similar al cierre del guion de narval.

#### Scenario: Cierre presente tras la última sección
- **WHEN** se lee el contenido después de la sección "Datos Curiosos"
- **THEN** existe un párrafo de cierre con invitación a seguir leyendo

### Requirement: El guion DEBE incluir la Ficha Técnica como tabla Markdown
La sección Ficha Técnica SHALL contener una tabla Markdown de 2 columnas con al menos los campos: Nombre común, Nombre científico, Clase, Subclase, Orden, Suborden, Familia.

#### Scenario: Tabla con campos mínimos presentes
- **WHEN** se revisa la sección Ficha Técnica
- **THEN** existe una tabla Markdown con al menos 7 filas de datos taxonómicos

### Requirement: El guion DEBE integrar las adaptaciones terminológicas de la spec adaptacion-terminologica
El artículo SHALL aplicar todas las adaptaciones de términos definidas en la spec `adaptacion-terminologica`: Triturador (*Smasher*), Arponero (*Spearer*), espiga (*herringbone*), silla de montar (*saddle spring*), banda media (*midband*), Enemigo Querido (*Dear Enemy*), y la expansión de LaMSA.

#### Scenario: Primera mención de cada término adaptado incluye original en inglés
- **WHEN** aparece por primera vez cualquiera de los términos adaptados
- **THEN** incluye la traducción española seguida del original en inglés en cursiva entre paréntesis

#### Scenario: Nombres científicos en cursiva
- **WHEN** aparece un nombre científico en el artículo
- **THEN** está formateado en cursiva Markdown

### Requirement: El guion DEBE integrar los elementos visuales de la spec elementos-visuales
El artículo SHALL incluir una tabla comparativa de fuerza de impacto, datos numéricos destacados en negrita, y encabezados jerárquicos consistentes (`#`/`##`/`###`).

#### Scenario: Tabla comparativa de fuerza presente
- **WHEN** se revisa la sección de Biomecánica
- **THEN** existe una tabla Markdown comparando la fuerza del camarón mantis con al menos 3 referentes

#### Scenario: Datos numéricos destacados en negrita
- **WHEN** se mencionan datos de impacto (velocidad, temperatura, fuerza)
- **THEN** los valores numéricos aparecen en **negrita**

### Requirement: El guion DEBE usar tono divulgativo con preguntas retóricas y analogías
El estilo del artículo SHALL ser español neutro, divulgativo y dinámico, con párrafos cortos (2–5 frases), preguntas retóricas ocasionales y al menos una analogía cotidiana para conceptos técnicos.

#### Scenario: Analogía presente en la sección de Biomecánica
- **WHEN** se explica el mecanismo de golpe o la cavitación
- **THEN** se usa al menos una analogía cotidiana para facilitar la comprensión

#### Scenario: Artículo libre de marcadores de sistema
- **WHEN** se revisa el texto completo del artículo
- **THEN** no contiene marcadores TODO, texto de sistema, citas formales ni URLs
