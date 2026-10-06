# Cómo escribir en el Devlog

El blog lo construye **GitHub Pages con Jekyll** cada vez que haces push. No tienes que ejecutar nada.

- Lista de entradas: `https://yalosegames.github.io/blog/`
- Cada entrada: `https://yalosegames.github.io/blog/<nombre-del-archivo-sin-fecha>/`

Ahora mismo está **oculto**: no sale en el menú y lleva `noindex`, así que Google no lo muestra. Solo entra quien tenga el enlace.

---

## Escribir un post nuevo

### Opción 1: desde el navegador (también desde el móvil)

1. Entra en el repo en github.com y abre la carpeta `_posts`.
2. Pulsa **Add file → Create new file**.
3. Nómbralo `AAAA-MM-DD-titulo-corto.md`, por ejemplo `2026-10-20-devlog-1-la-sarten.md`.
   - La fecha manda en el orden de la lista.
   - El resto del nombre será la dirección.
   - Todo en minúsculas, sin tildes ni espacios.
4. Copia dentro el contenido de `_plantillas/post.md` y rellénalo.
5. Pulsa **Commit changes**. En uno o dos minutos está en la web.

### Opción 2: desde tu PC

Haz lo mismo en la carpeta `_posts/` y luego commit y **Push origin** en GitHub Desktop.

---

## La cabecera de cada post

```yaml
---
layout: post                 # no lo cambies
title: La sartén             # título grande
numero: 1                    # sale como «DEVLOG #1»
autor: Pepe                  # opcional
resumen: Una o dos frases.   # sale en la lista y al compartir el enlace
portada: /assets/blog/devlog-1/portada.jpg   # opcional, imagen 16:9
etiquetas: [Diseño, Minijuegos]              # opcional
---
```

## Qué puedes poner dentro

| Quieres… | Escribe |
|---|---|
| Subtítulo | `## Subtítulo` |
| Negrita / cursiva | `**negrita**` / `*cursiva*` |
| Enlace | `[texto](https://…)` |
| Imagen | `![descripción](/assets/blog/devlog-1/foto.jpg)` |
| Pie de foto | Una línea entera en cursiva justo debajo: `*El pie de foto.*` |
| Lista | `- cosa` (cuadraditos) o `1. paso` (números) |
| Nota destacada | `> texto` (sale como tarjeta) |
| Separador | `---` (línea de puntos) |
| Vídeo | `<video controls playsinline preload="none" src="/assets/blog/devlog-1/clip.mp4"></video>` |

**Imágenes y vídeos:**
- Van en `assets/blog/devlog-N/`, una carpeta por post.
- Usa `.jpg` o `.webp` de menos de ~500 KB, y vídeos `.mp4` cortos.
- **YouTube no funciona:** la seguridad de la web (CSP) bloquea vídeos externos. Usa `.mp4` o un GIF.

## Borradores

- Si añades `published: false` en la cabecera, GitHub **no lo publica**.
- ⚠️ El repo es **público**: cualquiera puede leer los borradores en github.com. Si algo es secreto, no lo subas hasta que vaya a salir.

---

## Abrir el blog al público

1. En `_config.yml`, cambia `blog_publico: false` por `true`. Así se quita el `noindex` y sale «Blog» en el menú de las páginas del blog.
2. Añade `<a href="blog/">Blog</a>` al menú (`.nav`) de `index.html`, `tourist-trap.html`, `quienes-somos.html`, `contacto.html` y `gracias.html`, justo antes de Contacto.
3. Si quieres, añade también una tarjeta en la portada.

## Si cambias el diseño

- Los estilos del blog están al final de `style.css`, en la sección «Blog / Devlog».
- Las plantillas están en `_layouts/` (`base.html` y `post.html`) y la lista en `blog/index.html`.
- Después de tocar `style.css`, ejecuta `python versionar.py`, que también actualiza `_layouts/`.
