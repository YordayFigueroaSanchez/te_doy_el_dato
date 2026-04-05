# Análisis del guion: Camarón mantis

Fecha: 2026-04-03

Archivo origen: [fauna/Camaron_mantis/guion.md](fauna/Camaron_mantis/guion.md)

Resumen ejecutivo

- Lenguaje: Español. Tono: educativo, descriptivo y divulgativo.
- Estructura: Introducción, Anatomía, Golpe/Cavitación, Sistema visual, Hábitat, Comportamiento, Dieta, Amenazas, Datos curiosos y cierre.
- Extensión estimada: ~900 palabras (aprox.). Duración estimada lectura natural (~150 wpm): ~6 minutos — demasiado larga para un Short.

Fortalezas

- Excelente uso de imágenes y metáforas ("Guerrero invisible", colores eléctricos).
- Buen equilibrio entre detalle técnico y lenguaje divulgativo.
- Contiene nombre científico (*Odontodactylus scyllarus*), datos medibles (23 m/s, cavitación, fuerzas), y contexto ecológico.

Oportunidades de mejora para Shorts

- Fragmentar en micro-historias (cada sección puede ser un Short distinto).
- Reducir longitud y preferir frases cortas para 30s/60s.
- Añadir YAML frontmatter estandarizado y un `resumen_for_edit` para edición rápida.

Ejemplo de YAML frontmatter sugerido

```yaml
---
id: camaron_mantis_001
language: es
species: Odontodactylus scyllarus
duration_targets: [30, 60, 360]
platforms: [youtube_shorts, instagram_reels, tiktok, youtube_long]
canonical_title: "El Guerrero Invisible del Arrecife"
title_options:
  - "El Guerrero Invisible del Arrecife"
  - "El Golpe Mortal del Camarón Mantis"
  - "Cómo un camarón rompe conchas y vidrio"
hashtags: ["#camarónmantis", "#curiosidades", "#oceanografía"]
tags: [fauna, marine, mantis-shrimp, curiosidades]
source_media: fauna/Camaron_mantis/camaron_mantis_portada_001.png
credits: "Texto: equipo; Imagen: autor/archivo"
resumen_for_edit: "Hook + 3 hechos: golpe, cavitación, visión extraordinaria."
---
```

Versión Short — 30s (≈75 palabras)

El camarón mantis, del tamaño de tu mano, concentra su fuerza como una resortera y lanza el golpe más rápido del océano. Ese impacto produce cavitación: burbujas que colapsan y añaden un segundo golpe. Sus apéndices pueden romper conchas y hasta vidrio, y sus ojos, con más de una docena de receptores, ven colores y luz polarizada que nosotros no podemos. Sigue para más curiosidades del mar.

Timestamps sugeridos (30s)

- 0–3s: Hook visual + frase de apertura
- 3–12s: Hecho 1 — fuerza y resortera
- 12–22s: Hecho 2 — cavitación y segundo golpe
- 22–28s: Hecho 3 — visión extraordinaria
- 28–30s: CTA (seguir/like)

Versión Short — 60s (≈150 palabras)

En los arrecifes habita un pequeño guerrero que redefine la fuerza: el camarón mantis pavo real. Mide hasta 15 cm, pero sus apéndices funcionan como mazas que acumulan energía y la liberan en milisegundos, alcanzando 23 m/s y provocando cavitación; la burbuja que colapsa genera un segundo golpe invisible, capaz de romper conchas y vidrio. Sus ojos, independientes y extremadamente complejos, detectan hasta 16 tipos de receptor, incluyendo luz ultravioleta y polarizada. Algunas especies son trituradoras, otras arponeras; todas cazan por emboscada desde madrigueras. La degradación de arrecifes y la acidificación amenazan su hábitat. Conservémoslos: son indicadores de arrecifes sanos.

Title options (sugeridos)

- El Guerrero Invisible del Arrecife
- El Golpe Mortal del Camarón Mantis
- ¿Cómo rompe un camarón el vidrio?

Hashtags sugeridos

- #camarónmantis #curiosidades #oceanografía

Checklist rápida para edición

- Añadir YAML frontmatter.
- Generar resumen_for_edit (voz en off) y caption corta.
- Crear versiones 30s/60s y marcar timestamps.
- Verificar cifras y fuentes (23 m/s, 1,500 N, especies).
- Añadir subtítulos `.srt` y créditos de media.

Próximos pasos recomendados

1. Crear `manifest.csv` con `path,canonical_title,word_count,duration_target,has_link,platforms,tags` para todo el conjunto de guiones.
2. Normalizar un ejemplo (p. ej. este) añadiendo YAML y las versiones 30s/60s en archivos separados.
3. (Opcional) Implementar `tools/parse_guiones.py` para extracción masiva y generación automatizada de versiones condensadas.

Archivo de referencia creado: `aidlc-docs/units/guiones/Camaron_mantis/analysis.md` (este archivo).
