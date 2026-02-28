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
