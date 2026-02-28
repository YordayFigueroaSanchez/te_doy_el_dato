## ADDED Requirements

### Requirement: El artículo DEBE cubrir todas las secciones temáticas
El artículo SHALL incluir las siguientes secciones en orden: Introducción y contexto evolutivo, Ficha Técnica (tabla taxonómica), Biomecánica (estructura Bouligand, mecanismo LaMSA, cavitación), Sistema Visual, Hábitat y Distribución, Comportamiento e Inteligencia, Dieta y Estrategias de Caza, Conservación, y Datos Curiosos.

#### Scenario: Artículo completo contiene todas las secciones
- **WHEN** se genera el artículo final
- **THEN** el documento contiene encabezados para cada una de las 8+ secciones temáticas definidas

### Requirement: La introducción DEBE contextualizar evolutivamente al animal
El artículo SHALL comenzar con una introducción que sitúe al camarón mantis en su contexto evolutivo (linaje desde el Devónico) y establezca la dualidad estética-letalidad como hilo conductor.

#### Scenario: El lector entiende la relevancia evolutiva desde el primer párrafo
- **WHEN** un lector lee la introducción
- **THEN** encuentra referencia al linaje antiguo del animal y una descripción de su doble naturaleza (belleza y poder)

### Requirement: La ficha técnica DEBE presentarse en formato tabla
El artículo SHALL incluir una tabla con la clasificación taxonómica completa: Nombre Científico, Clase, Subclase, Orden, Familia y Suborden.

#### Scenario: Tabla taxonómica presente y completa
- **WHEN** se revisa la sección de ficha técnica
- **THEN** existe una tabla Markdown con al menos 6 filas de clasificación taxonómica

### Requirement: La sección de biomecánica DEBE explicar cavitación de forma accesible
El artículo SHALL explicar el fenómeno de cavitación usando analogías comprensibles para un lector sin formación en física, mencionando las temperaturas alcanzadas y el efecto de sonoluminiscencia.

#### Scenario: Explicación de cavitación accesible
- **WHEN** un lector no especialista lee la sección de biomecánica
- **THEN** encuentra una explicación de la cavitación con al menos una analogía cotidiana y datos de temperatura (4,400 °C)

### Requirement: El artículo DEBE tener entre 2000 y 3500 palabras
El artículo SHALL tener una extensión de entre 2000 y 3500 palabras para equilibrar profundidad y legibilidad.

#### Scenario: Extensión dentro del rango
- **WHEN** se cuenta el número de palabras del artículo
- **THEN** el total está entre 2000 y 3500 palabras
