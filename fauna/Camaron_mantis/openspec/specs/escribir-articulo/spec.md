## Especificación: Contenido del artículo (formato “guion.md”)

Este documento define **cómo debe generarse el guion/artículo en Markdown** para el camarón mantis, con el mismo estilo y legibilidad que los ejemplos:

- [example/narval.md](../../../example/narval.md)
- [example/salmon.md](../../../example/salmon.md)

La salida esperada es un texto divulgativo en español, listo para publicarse como artículo o narrarse como guion.

---

## 0) Entradas y salida (fuente de verdad)

### 0.1 Fuente base (obligatoria)

El contenido del artículo **DEBE** tomar como base la información disponible en:

- [fauna/Camaron_mantis/sources/info.md](fauna/Camaron_mantis/sources/info.md)

Reglas:

- No inventar datos que contradigan la fuente.
- Si la fuente no especifica un detalle (por ejemplo, especie exacta), se permite escribir de forma general (género/familia) y dejarlo claro, sin “rellenar” con precisión falsa.

### 0.2 Archivo de salida (obligatorio)

El sistema que genera el contenido **DEBE** escribir el artículo final en:

- [fauna/Camaron_mantis/guion.md](fauna/Camaron_mantis/guion.md)

---

## 1) Formato de salida (Markdown)

### 1.1 Portada (obligatoria)

La primera línea del documento **DEBE** ser una imagen Markdown de portada, igual que en los guiones existentes:

`![alt text](NOMBRE_DEL_ARCHIVO_DE_PORTADA)`

Reglas:

- **NOMBRE_DEL_ARCHIVO_DE_PORTADA** debe ser el nombre real de un archivo de imagen disponible para este animal (por ejemplo `.png` o `.jpg`).
- Si no se provee un nombre concreto, usar el default `camaron_mantis_portada_001.png` (y el sistema que consuma el guion deberá generar/colocar esa imagen).

### 1.2 Encabezados

Para replicar el estilo del guion de salmón, la opción preferida es:

- Usar **encabezados `###`** para cada sección principal.

Compatibilidad:

- Si el pipeline del proyecto u otras specs requieren jerarquía, se permite usar `#` (título único) y `##` (secciones), **siempre que** los títulos de sección y su orden se mantengan.
- En ese caso, la imagen de portada va primero y el `# Título` puede ir inmediatamente después.

### 1.3 Tablas

Las tablas (por ejemplo, la ficha técnica) se entregan como **tabla Markdown**.

### 1.4 Listas

Evitar listas con viñetas en el cuerpo del artículo.

- Se permite lista **solo** si es estrictamente necesaria para claridad.
- La sección “Datos curiosos” debe ser narrativa (en párrafos) o, si se usa lista, que sea corta (máximo 5 ítems) y con frases completas.

---

## 2) Estilo de escritura (como narval/salmón)

El guion **DEBE**:

- Estar en **español neutro**, tono divulgativo, dinámico, con preguntas retóricas ocasionales.
- Usar párrafos cortos (2–5 frases) y transiciones claras.
- Explicar conceptos técnicos con analogías simples sin perder rigor.
- Mantener un hilo narrativo: “belleza” (colores, visión) vs “letalidad” (golpe, cavitación).

El guion **NO DEBE**:

- Incluir citas formales, bibliografía, URLs o notas al pie.
- Incluir marcadores tipo “TODO”, “(inserta aquí…)”, o texto de sistema.

---

## 3) Longitud

El artículo final **DEBE** tener entre **2000 y 3500 palabras**.

---

## 4) Estructura obligatoria (secciones y orden)

El guion **DEBE** incluir estas secciones, en este orden. Cada una debe aparecer como encabezado Markdown (preferentemente `###`, o `##` si se usa jerarquía):

1. `### Introducción y contexto evolutivo`
2. `### Ficha Técnica`
3. `### Biomecánica: el golpe (Bouligand + LaMSA + cavitación)`
4. `### Sistema Visual`
5. `### Hábitat y Distribución`
6. `### Comportamiento e Inteligencia`
7. `### Dieta y Estrategias de Caza`
8. `### Conservación`
9. `### Datos Curiosos`

Además:

- Terminar con un **cierre** de 2–4 frases que invite a seguir leyendo/ver más contenido (como el cierre del guion de salmón).

---

## 5) Contenido mínimo por sección

### 5.1 Introducción y contexto evolutivo

Debe lograr un “gancho” como en narval/salmón y cumplir:

- Mencionar que el linaje es antiguo (referencia al **Devónico**).
- Presentar la idea central: un animal visualmente espectacular con un mecanismo de golpe extraordinario.

### 5.2 Ficha Técnica (tabla obligatoria)

Debe incluir una **tabla Markdown de 2 columnas** (`Campo` | `Valor`) con, como mínimo, estos campos:

- Nombre común
- Nombre científico
- Clase
- Subclase
- Orden
- Suborden
- Familia

Notas:

- Si la especie exacta no se especifica, se permite indicar el género/familia (dejándolo claro), pero el nombre científico no debe inventarse.

### 5.3 Biomecánica: el golpe (Bouligand + LaMSA + cavitación)

Debe explicar en lenguaje accesible:

- Qué es la **estructura de Bouligand** (por qué resiste fracturas).
- Qué es el mecanismo **LaMSA** y por qué permite liberar energía tan rápido.
- Qué es la **cavitación** y cómo se produce con el golpe.
- Incluir el dato de temperatura aproximada **4,400 °C** y mencionar **sonoluminiscencia**.

Reglas de claridad:

- Usar al menos **una analogía cotidiana** (p. ej., “como un látigo”, “como una resortera”, “como burbujas que colapsan”).

### 5.4 Sistema Visual

Debe cubrir:

- Por qué su visión es inusual (canales/polarización/colores) sin caer en tecnicismos innecesarios.
- Conectar la visión con su comportamiento (caza, reconocimiento, comunicación).

### 5.5 Hábitat y Distribución

Debe incluir:

- Dónde vive (arrecifes/zonas costeras tropicales/subtropicales, madrigueras).
- Cómo el hábitat influye en su estrategia (emboscada, territorio).

### 5.6 Comportamiento e Inteligencia

Debe incluir:

- Territorialidad y uso de refugios.
- Alguna conducta destacable (aprendizaje, reconocimiento, rituales de amenaza).

### 5.7 Dieta y Estrategias de Caza

Debe incluir:

- Qué come (crustáceos, moluscos, peces pequeños; variar según tipo “smasher/spearer” si se menciona).
- Cómo caza y cómo usa el golpe/arma.

### 5.8 Conservación

Debe incluir:

- Amenazas típicas (pérdida de hábitat, contaminación, captura incidental, comercio/acuariofilia si aplica).
- Un cierre sobrio (sin catastrofismo gratuito) sobre por qué importa conservarlo.

### 5.9 Datos Curiosos

Debe incluir 3–6 datos curiosos relevantes y verificables, manteniendo el tono del guion.

---

## 6) Plantilla mínima (solo como guía)

La salida **DEBE** seguir esta forma general:

`![alt text](camaron_mantis_portada_001.png)`

`### Introducción y contexto evolutivo`
(párrafos)

`### Ficha Técnica`
(tabla)

`### Biomecánica: el golpe (Bouligand + LaMSA + cavitación)`
(párrafos)

`### Sistema Visual`
(párrafos)

`### Hábitat y Distribución`
(párrafos)

`### Comportamiento e Inteligencia`
(párrafos)

`### Dieta y Estrategias de Caza`
(párrafos)

`### Conservación`
(párrafos)

`### Datos Curiosos`
(párrafos o lista corta)

(cierre con invitación a seguir explorando el canal/serie)
