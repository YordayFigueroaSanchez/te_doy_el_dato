## ADDED Requirements

### Requirement: Los términos Smasher y Spearer DEBEN adaptarse al español
El artículo SHALL usar "Triturador" como equivalente de *Smasher* y "Arponero" como equivalente de *Spearer*. La primera aparición de cada término MUST incluir el original en inglés entre paréntesis.

#### Scenario: Primera mención de Smasher incluye traducción y original
- **WHEN** el término "Smasher" aparece por primera vez en el artículo
- **THEN** se presenta como "Triturador (*Smasher*)" o formato equivalente que incluya ambos términos

#### Scenario: Primera mención de Spearer incluye traducción y original
- **WHEN** el término "Spearer" aparece por primera vez en el artículo
- **THEN** se presenta como "Arponero (*Spearer*)" o formato equivalente que incluya ambos términos

### Requirement: Los nombres científicos DEBEN escribirse en cursiva
Todos los nombres científicos (género, especie, orden, etc.) SHALL presentarse en formato cursiva Markdown (*cursiva*).

#### Scenario: Nombre de especie en cursiva
- **WHEN** se menciona "Odontodactylus scyllarus" en el artículo
- **THEN** aparece como *Odontodactylus scyllarus* (en cursiva)

#### Scenario: Nombre de orden en cursiva
- **WHEN** se menciona "Stomatopoda" en el artículo
- **THEN** aparece como *Stomatopoda* (en cursiva)

### Requirement: Los acrónimos técnicos DEBEN explicarse en su primera aparición
Acrónimos como LaMSA SHALL expandirse y explicarse en español la primera vez que se usan. Ejemplo: "Actuación de Resorte Mediada por Pestillo (LaMSA, por sus siglas en inglés)."

#### Scenario: LaMSA se explica en primera mención
- **WHEN** el acrónimo LaMSA aparece por primera vez
- **THEN** va acompañado de su expansión en español y la nota de que son siglas en inglés

### Requirement: Las unidades de medida DEBEN usar el sistema métrico
Todas las magnitudes SHALL expresarse en unidades del Sistema Internacional (m/s, °C, Newtons, g). Las conversiones informales (como "bala calibre .22") pueden usarse como analogías complementarias pero no como unidad principal.

#### Scenario: Velocidad del golpe en unidades métricas
- **WHEN** se describe la velocidad del golpe del camarón
- **THEN** se presenta en m/s (23 m/s) antes o en lugar de cualquier analogía informal

### Requirement: El término herringbone DEBE adaptarse al español
El artículo SHALL usar "espiga" como equivalente de *herringbone*. La primera aparición MUST incluir el original en inglés en cursiva entre paréntesis.

#### Scenario: Primera mención de herringbone incluye traducción y original
- **WHEN** el término "herringbone" aparece por primera vez en el artículo
- **THEN** se presenta como "espiga (*herringbone*)" o formato equivalente que incluya ambos términos

### Requirement: El término saddle spring DEBE adaptarse al español
El artículo SHALL usar "silla de montar" como equivalente descriptivo de *saddle spring*. La primera aparición MUST incluir el original en inglés en cursiva entre paréntesis.

#### Scenario: Primera mención de saddle spring incluye traducción y original
- **WHEN** el término "saddle spring" aparece por primera vez en el artículo
- **THEN** se presenta como "silla de montar (*saddle spring*)" o formato equivalente que incluya ambos términos

### Requirement: El término midband DEBE adaptarse al español
El artículo SHALL usar "banda media" como equivalente de *midband*. La primera aparición MUST incluir el original en inglés en cursiva entre paréntesis.

#### Scenario: Primera mención de midband incluye traducción y original
- **WHEN** el término "midband" aparece por primera vez en el artículo
- **THEN** se presenta como "banda media (*midband*)" o formato equivalente que incluya ambos términos

### Requirement: El término Dear Enemy DEBE adaptarse al español con formato consistente
El artículo SHALL usar "Enemigo Querido" como equivalente de *Dear Enemy*. La primera aparición MUST seguir el mismo patrón que los demás términos adaptados: traducción en español seguida del original en inglés en cursiva entre paréntesis.

#### Scenario: Primera mención de Dear Enemy sigue el patrón estándar
- **WHEN** el término "Dear Enemy" aparece por primera vez en el artículo
- **THEN** se presenta como "Enemigo Querido (*Dear Enemy*)" o formato equivalente que siga el patrón español (*inglés*)

#### Scenario: El encabezado de sección usa el término adaptado
- **WHEN** existe un encabezado de sección que referencia este efecto
- **THEN** el encabezado incluye la traducción en español, no solo el término en inglés

### Requirement: La expansión de Latch-Mediated Spring Actuation DEBE formalizarse
El artículo SHALL incluir la expansión completa "Actuación de Resorte Mediada por Pestillo" como equivalente de *Latch-Mediated Spring Actuation* en su primera mención, junto al acrónimo LaMSA y la nota de que son siglas en inglés.

#### Scenario: Expansión completa presente en primera mención
- **WHEN** el mecanismo LaMSA se describe por primera vez
- **THEN** aparece la traducción completa en español, el acrónimo LaMSA, y la expansión original en inglés en cursiva
