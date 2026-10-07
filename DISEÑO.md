# DISEÑO — YaloséGames

Ficha del sistema de diseño de la web del estudio. **Léela antes de tocar cualquier página o `style.css`**, y actualízala si cambias algo de lo que aquí se describe.

---

## 1. Personalidad

Un **chiringuito de playa malagueño dibujado a mano**, sacado de Tourist Trap: toldo de rayas, azulejo andaluz, cielo, sol que gira, platos del juego.
Cálido, gamberro y artesanal. Todo tiene **contorno grueso chocolate y sombra dura**, como las letras del logo.

Si dudas entre «limpio y moderno» y «parece del juego», gana **parece del juego**.

---

## 2. Color

Todo color va como **variable** en `:root`. Así funciona el modo noche: cambia las variables y la página entera se repinta.

| Variable | Día | Noche | Uso |
|---|---|---|---|
| `--cream` | `#fffaeb` | `#121a33` | Fondo de página, relleno de letras grandes, campos de formulario |
| `--foam` | `#eaf3f1` | `#1c2748` | Fondo de tarjetas secundarias (contacto, carta) |
| `--choco` | `#3e130f` | `#fff5dc` | Texto, **todos los bordes**, sombras duras |
| `--brown` | `#632f22` | `#f0bc5e` | Títulos de sección, párrafos largos, etiquetas de campo |
| `--terra` | `#905d55` | — | Reserva (casi sin uso) |
| `--peach` | `#ebb38c` | `#e38b5a` | Arena: toldo, sombras de color, pegatinas, hover del menú |
| `--sky` | `#8ad6e3` | `#1f3263` | Cielo: cabeceras, tarjeta de Tourist Trap, prensa |
| `--sea` | `#1f6f8b` | `#f0bc5e` | Mar: botón principal, foco de campos |

Colores fijos, fuera de la paleta:
- **Error:** `#c4122f`. Solo en campos mal rellenados.
- **Pie en modo noche:** `#0b1224`.
- **Estrellas nocturnas:** `#fff5dc` y `#f0bc5e`.

**Reglas:**
- Nunca escribas un hex suelto en una regla nueva: usa la variable.
- Si de verdad necesitas un color fijo, añade también su versión en `#night:checked ~ .page …`.
- Las sombras de color van con los tonos de playa (`--peach`, `--sky`). El chocolate se reserva para botones y tarjetas principales.

---

## 3. Tipografía

| Fuente | Pesos | Dónde |
|---|---|---|
| **Lilita One** | 400 (única) | Títulos, menú, botones, etiquetas de campo, nombre del equipo, pegatinas, logo de texto, pie |
| **Inter** | 500 · 600 · 700 · 800 | Todo el texto corrido, campos de formulario, notas |

Las dos son de Google Fonts y tienen licencia libre (OFL). Se cargan con `@import` en la primera línea de `style.css`.

⚠️ **Prohibido:**
- **Malacitana**, por temas legales.
- **Las fuentes del juego**, por licencia.

Si hace falta otra fuente, que sea de Google Fonts con licencia OFL, y hay que añadir su dominio a la CSP.

**Escala:**

| Elemento | Tamaño |
|---|---|
| Nombre del estudio en portada | `min(9.5vw, 19vh)`, `line-height: 0.9`, girado `-3deg` |
| Título de página (`.page-title`) | `clamp(40px, 6vw, 88px)` |
| Título de sección | `clamp(32px, 5vw, 64px)`, MAYÚSCULAS |
| Título de bloque | `clamp(20px, 1.8vw, 28px)`, MAYÚSCULAS, `letter-spacing: 0.03em` |
| Texto corrido | 17–18px, `line-height: 1.6–1.7`, peso 500, color `--brown` |
| Etiquetas pequeñas | 12–13px, peso 800, MAYÚSCULAS, `letter-spacing: 0.05–0.1em` |

**Letras «de logo»** (títulos grandes sobre el cielo): relleno `--cream`, contorno `-webkit-text-stroke: 0.05em var(--choco)`, `paint-order: stroke fill` y `text-shadow: 0.05em 0.06em 0 var(--brown)`.

---

## 4. Forma

- **Bordes:** siempre `3px solid var(--choco)`. Ni 1px ni 2px.
- **Esquinas:** **cuadradas** (`border-radius: 0`). Nada redondeado, salvo el foco del sol o la luna.
- **Sombras:** **duras y desplazadas, nunca difuminadas**.

| Elemento | Sombra |
|---|---|
| Campo de formulario | `4px 4px 0 var(--peach)` → foco: `var(--sea)` |
| Botón / pegatina | `5px 5px 0 var(--choco)` |
| Tarjeta principal | `8px 8px 0 var(--choco)` |
| Tarjeta secundaria / vídeo / carta | `8px 8px 0 var(--peach)` o `var(--sky)` |
| Galería | `5px 5px 0 var(--peach)` |

- **Al pasar el ratón**, el elemento sube y la sombra crece en la misma medida: `translate(-2px, -2px)` con sombra `7px`, o en tarjetas `-3px` con sombra `11px`.
- **Pegatinas** (`.sticker`, `.badge`, `.wip`, `.feature-label`): fondo sólido, MAYÚSCULAS y **giradas entre −3° y 5°**.

---

## 5. Espaciado y maquetación

- **Contenido:** `main` con `max-width: 1400px`.
- **Secciones:** `padding: 90px 64px 20px`; en móvil, `60px 20px 10px`.
- **Huecos entre tarjetas:** 16–28px.
- **Puntos de corte:**
  - `1000px`: las rejillas pasan a una columna.
  - `800px`: menú en dos filas y portada apilada.
  - `600px`: campos del formulario en una columna.

**Esqueleto de cada página**, en este orden:
1. `#night` (checkbox)
2. `.page`
3. `.topbar`, que lleva logo, `.nav` y el sol o la luna (`.nav-sky`)
4. Cabecera:
   - en la portada, `.hero`;
   - en las subpáginas, `.page-hero` con el toldo, las nubes y el título.
5. `.tiles-band`
6. `main`
7. `.tiles-band`
8. `.footer`

---

## 6. Componentes

| Componente | Clase | Notas |
|---|---|---|
| Botón principal | `.btn.btn-sea` | Fondo mar y texto crema. En noche, el texto pasa a `#121a33` |
| Botón secundario | `.btn.btn-line` | Fondo crema y texto chocolate |
| Enlace activo del menú | `.nav a.is-active` + `aria-current="page"` | Subrayado chocolate de 3px |
| Botón de idioma | `.lang-switch` | Pegatina crema «EN» / «ES» junto al sol. La pone `traducir.py` |
| Botón «Contacto» del menú | `.nav-cta` | Botón mar con sombra 4px; cuando está activo pasa a melocotón |
| Tarjeta de portada | `.teaser` + `.teaser-tt` / `-team` / `-contact` | Cielo / melocotón / espuma. Dibujo del juego asomando abajo a la derecha |
| Tarjeta de contenido | `.contact-card` | Espuma, sombra melocotón. Variante `.contact-press` en cielo |
| Título con puntos | `.section-head` = `.section-title` + `.head-dots` | Línea de puntos melocotón a la altura de las mayúsculas |
| Miembro del equipo | `.team li.c0/.c1/.c2` | Alterna cielo / melocotón / espuma |
| Campo | `label.field` > `span` + `input` | Etiqueta en Lilita, campo crema con sombra melocotón |
| Pista de campo | `small.field-help` | Se pone roja si el campo es inválido |
| Tarjeta de post | `.post-card.post-card-c0/c1/c2` | Cielo / melocotón / espuma. La más reciente ocupa todo el ancho |
| Pegatinas de post | `.post-num` + `.post-date` | «BLOG #N» en chocolate y fecha en crema, giradas |
| Cuerpo de post | `.post-body` | Ancho de 860px e Inter de 18px. Imágenes con sombra melocotón, `>` como tarjeta y `---` como línea de puntos |
| Pareja de imágenes | `.post-pair` | Dos imágenes lado a lado, giradas −2° y 2°; en móvil, una debajo de otra |
| Vídeo vertical | `video.video-vertical` | Centrado y a 400px como máximo de ancho |

**Formularios:** van a FormSubmit. Llevan los campos ocultos `_subject`, `Origen`, `_next` (que apunta a `gracias.html`) y `_template=table`, más el señuelo `_honey`.

**Validación:** solo HTML (`required`, `type`, `pattern` y `title`), más `:user-invalid` para marcar en rojo.

---

## 7. Decoración

Todo sale de los assets del juego (`assets/img/deco/`): sol, luna, nubes, estrella, espeto, sombrilla, chefs, platos, azulejo y logos.

**Props de Dani y Ernesto** (`assets/img/deco/props/`), recortados de sus láminas del Trello del equipo. Solo se usan los que están **a color**, no los bocetos grises.

| Dónde | Props |
|---|---|
| Tourist Trap | Guirnalda de bombillas sobre la carta; Poseidón junto a la historia; gramófono junto a la pizarra; altavoz sobre el vídeo |
| Quiénes somos | Servilletero «CHIRINGELIOS», cerveza, copa y cubata |
| Contacto | Radio en «Kit de prensa»; pecera en «También en» |
| Gracias | Trofeo de oro |
| Blog | Tele en la cabecera y guirnalda de banderines |

Probados y descartados por recargar demasiado: la playa de props en la portada y la guirnalda del Guirilencia sobre el equipo. Hay más en la carpeta, sin usar todavía: trofeos de bronce y plata, banderines sueltos, lámpara roja, caracolas, palmera baja.

- **Toldo** (`.awning`): rayas melocotón y crema de 64px, con el borde festoneado hecho con `radial-gradient`.
- **Azulejo** (`.tiles-band`): franja de 56px con borde chocolate arriba y abajo. Va antes y después del contenido.
- **Nubes:** cruzan despacio (55–75s) por encima o por debajo del texto, nunca encima.
- **Sol:** gira (40s). Pulsarlo cambia a modo noche; la luna entra girando.
- **Dibujos sueltos:** girados entre −10° y −3°, asomando por una esquina de la tarjeta (`overflow: hidden`).
- **Imágenes grandes:** con borde de 3px y sombra dura; en modo noche se oscurecen con `filter`.

No metas iconos genéricos, emojis ni ilustraciones que no sean del juego.

---

## 8. Movimiento

- **Hover:** `0.15–0.2s ease`.
- **Cambio de paleta día/noche:** `0.6s ease` sobre fondo, color, borde y sombra. Si añades un bloque con fondo propio, inclúyelo en esa lista de `transition`.
- **Rebote del sol y la luna:** `cubic-bezier(0.34, 1.4, 0.64, 1)`.
- **Todo lo que se mueva solo** (nubes, sol, estrellas) se apaga con `prefers-reduced-motion: reduce`.

---

## 9. Reglas técnicas

- **Inglés:** las páginas en español son el original y `en/` se **genera** con `python traducir.py`. Si cambias un texto en español, añade su traducción en `traducir.py` y vuelve a ejecutarlo. Nunca edites `en/` a mano, porque se sobrescribe. El script avisa si algo queda sin traducir. El blog solo está en español.
- **Blog con Jekyll:** GitHub Pages construye `_posts/`, `_layouts/` y `blog/index.html`. Las `.html` sin cabecera YAML se copian tal cual. Cómo se escribe un post: en `BLOG.md`. En las plantillas del blog las rutas son absolutas (`/style.css`, `/assets/…`). **No vuelvas a crear `.nojekyll`**, porque apagaría el blog.
- **Cero JavaScript.** La CSP tiene `script-src 'none'`. El modo noche es un checkbox (`#night`) con el selector `#night:checked ~ .page`. **No uses `:root:has()`**, porque Chrome no repinta los fondos.
- **CSP** en cada `.html`: solo `self`, Google Fonts y `form-action https://formsubmit.co`.
- **Caché:** si cambias `style.css`, ejecuta `python versionar.py` antes de subir. También actualiza `_layouts/`.
- **HTML bien anidado:** un `</div>` de más ya dejó la portada sin imagen una vez.
- **Página nueva:** copia el esqueleto de una existente, con su CSP, sus metas OG y el enlace activo en `.nav`.

---

## 10. Sí / No

| ✅ Sí | ❌ No |
|---|---|
| Bordes de 3px chocolate | Bordes finos o grises |
| Sombras duras desplazadas | `box-shadow` con desenfoque |
| Esquinas cuadradas | `border-radius` |
| Pegatinas giradas | Etiquetas en píldora redondeada |
| Colores por variable | Hex sueltos sin versión noche |
| Dibujos del juego | Iconos de librería, emojis, stock |
| Lilita One + Inter | Malacitana, fuentes del juego |
| Español de España y su copia en `en/` | Textos mezclados ES/EN en una misma página |

---

## 11. Antes de subir

1. Mírala de **día y de noche**.
2. Mírala en **móvil** (375px) y en monitor ancho.
3. Ejecuta `python traducir.py` si tocaste alguna página (ya llama a `versionar.py`). Si solo tocaste el CSS, basta con `python versionar.py`.
4. Pasa la validación de HTML (sin etiquetas sin cerrar).
5. Haz commit y luego **Push origin** en GitHub Desktop.
