"""Genera la versión en inglés (carpeta en/) a partir de las páginas en español.

Las páginas en español son el ORIGINAL: cambia siempre esas y luego ejecuta
    python traducir.py
Si cambias o añades un texto en español, añade su traducción aquí abajo.
El script avisa si un texto ya no aparece o si queda algo sin traducir en inglés.
También pone el botón EN/ES y versiona el CSS (llama a versionar.py)."""
import os, re, subprocess, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PAGES = ['index.html', 'tourist-trap.html', 'quienes-somos.html', 'contacto.html', 'gracias.html']
SITE = 'https://yalosegames.github.io'

# ---------------------------------------------------------------- Traducciones
COMUN = [
    ('<html lang="es">', '<html lang="en">'),
    ('aria-label="Modo noche"', 'aria-label="Night mode"'),
    ('aria-label="Principal"', 'aria-label="Main"'),
    ('title="¿Día o noche?"', 'title="Day or night?"'),
    ('>Inicio</a>', '>Home</a>'),
    ('>Quiénes somos</a>', '>About us</a>'),
    ('>Contacto</a>', '>Contact</a>'),
    ('Web en construcción', 'Site under construction'),
    ('aria-label="Redes sociales"', 'aria-label="Social media"'),
]

POR_PAGINA = {
    'index.html': [
        ('<title>YaloséGames — Estudio indie</title>', '<title>YaloséGames — Indie game studio</title>'),
        ('content="YaloséGames — Estudio indie"', 'content="YaloséGames — Indie game studio"'),
        ('YaloséGames, estudio indie de videojuegos. Nuestro primer juego: Tourist Trap, un simulador de cocina tycoon en un chiringuito andaluz.',
         'YaloséGames, an indie video game studio. Our first game: Tourist Trap, a cooking tycoon sim set in an Andalusian beach bar.'),
        ('Estudio indie de videojuegos', 'Indie video game studio'),
        ('Nuestro primer juego: <strong>Tourist Trap</strong>, un simulador de cocina tycoon en un chiringuito andaluz.',
         'Our first game: <strong>Tourist Trap</strong>, a cooking tycoon sim set in an Andalusian beach bar.'),
        ('▶ Ver gameplay', '▶ Watch gameplay'),
        ('Descubre el juego', 'Discover the game'),
        ('alt="Arte principal de Tourist Trap"', 'alt="Tourist Trap key art"'),
        ('>En desarrollo<', '>In development<'),
        ('Simulador de Cocina Tycoon: lleva tu propio chiringuito andaluz, cocina a base de minijuegos y sobrevive a los clientes hambrientos.',
         'Cooking Tycoon Sim: run your own Andalusian beach bar, cook your way through minigames and survive hungry customers.'),
        ('Ver el juego →', 'See the game →'),
        ('<h2>Quiénes somos</h2>', '<h2>About us</h2>'),
        ('Siete personas entre programación, 3D y 2D haciendo nuestro primer juego.',
         'Seven people across programming, 3D and 2D making our first game.'),
        ('Conoce al equipo →', 'Meet the team →'),
        ('<h2>¿Hablamos?</h2>', '<h2>Let’s talk!</h2>'),
        ('Prensa, festivales, testers o simplemente saludar.', 'Press, festivals, playtesters or just saying hi.'),
        ('Contactar →', 'Get in touch →'),
    ],
    'tourist-trap.html': [
        ('Simulador de Cocina Tycoon: lleva tu propio chiringuito andaluz y sobrevive a los clientes hambrientos.',
         'Cooking Tycoon Sim: run your own Andalusian beach bar and survive hungry customers.'),
        ('Simulador de Cocina Tycoon · En desarrollo', 'Cooking Tycoon Sim · In development'),
        ('alt="Arte principal de Tourist Trap"', 'alt="Tourist Trap key art"'),
        ('>En desarrollo<', '>In development<'),
        ('>Simulador de Cocina Tycoon<', '>Cooking Tycoon Sim<'),
        ('Lleva tu propio chiringuito andaluz, cocina a base de minijuegos y sobrevive a los clientes hambrientos.',
         'Run your own Andalusian beach bar, cook your way through minigames and survive hungry customers.'),
        ('Gestión + Cocina en tiempo real', 'Management + real-time cooking'),
        ('Minijuegos Variados de Cocina', 'Lots of different cooking minigames'),
        ('Eventos caóticos: gaviotas, incendios, tsunamis…', 'Chaotic events: seagulls, fires, tsunamis…'),
        ('<!-- La historia, con viñeta del chef -->', '<!-- The story, with the chef comic panel -->'),
        ('alt="Viñeta del chef de Tourist Trap, agobiado con una llave inglesa"',
         'alt="Comic panel of the Tourist Trap chef, stressed out and holding a wrench"'),
        ('>La historia<', '>The story<'),
        ('Compras un «Rasca y gana» en la gasolinera y te toca… un chiringuito. Mala suerte: era un «Rasca y paga». El chiringuito está en ruinas, viene con deuda y tu tío Rogelio Chiringelio sueña con verlo algún día en las 5 estrellas.',
         'You buy a scratch card at the petrol station and win… a beach bar. Bad luck: it was a “scratch and pay”. The beach bar is in ruins, comes with debt, and your uncle Rogelio Chiringelio dreams of one day seeing it reach 5 stars.'),
        ('aria-label="5 estrellas"', 'aria-label="5 stars"'),
        ('Cada día tiene tres fases: preparas el local y compras mejoras, sirves en tiempo real antes de que se agote la paciencia de los clientes y, al cierre, recibes una nota que sube o baja tu reputación. Todo mientras las gaviotas lo llenan todo de «regalitos», se incendia la cocina o aparecen clientes como Karen, Poseidón o tres gaviotas dentro de una gabardina.',
         'Each day has three phases: you get the place ready and buy upgrades, serve in real time before customers run out of patience and, at closing time, get a rating that raises or lowers your reputation. All while seagulls leave their little “gifts” everywhere, the kitchen catches fire, or customers like Karen, Poseidon or three seagulls in a trench coat walk in.'),
        ('<!-- La carta del chiringuito -->', '<!-- The beach bar menu -->'),
        ('>La carta del chiringuito<', '>The beach bar menu<'),
        ('<span>Boquerones</span>', '<span>Fried anchovies</span>'),
        ('<span>Calamares</span>', '<span>Calamari</span>'),
        ('<span>Tomate aliñado</span>', '<span>Tomato salad</span>'),
        ('<span>Berenjenas</span>', '<span>Fried aubergine</span>'),
        ('<!-- La pizarra del chiringuito (portada del GDD) -->', '<!-- The beach bar chalkboard (GDD cover) -->'),
        ('alt="Pizarra «Cómo pedir un cafelito»: un pez profesor con un puntero explica los cafés de Málaga, del solo a la nube"',
         'alt="Chalkboard “Cómo pedir un cafelito” (how to order a coffee): a fish teacher with a pointer explains the coffees of Málaga, from solo to nube"'),
        ('Cómo pedir un cafelito en nuestro Chiringuito', 'How to order a cafelito at our beach bar'),
        ('>Capturas<', '>Screenshots<'),
        ('alt="La playa desde arriba"', 'alt="The beach from above"'),
        ('alt="El chiringuito"', 'alt="The beach bar"'),
        ('alt="Servicio en tiempo real"', 'alt="Real-time service"'),
        ('alt="Minijuego de la sartén"', 'alt="Frying pan minigame"'),
        ('alt="Minijuego de los espetos"', 'alt="Sardine skewer minigame"'),
        ('alt="Arte conceptual de personajes"', 'alt="Character concept art"'),
        ('>Minijuegos de cocina<', '>Cooking minigames<'),
        ('alt="Minijuego del horno"', 'alt="Oven minigame"'),
        ('alt="Minijuego de la tabla de cortar"', 'alt="Chopping board minigame"'),
        ('<figcaption>Horno</figcaption>', '<figcaption>Oven</figcaption>'),
        ('<figcaption>Tabla de cortar</figcaption>', '<figcaption>Chopping board</figcaption>'),
        ('<figcaption>Sartén</figcaption>', '<figcaption>Frying pan</figcaption>'),
        ('<figcaption>Espetos</figcaption>', '<figcaption>Sardine skewers</figcaption>'),
        ('alt="Servicio en sala"', 'alt="Serving the tables"'),
        ('alt="Clientes bajo el toldo"', 'alt="Customers under the awning"'),
        ('alt="La tienda Chiripop en el móvil"', 'alt="The Chiripop shop on the phone"'),
        ('alt="Resultados del día"', 'alt="End-of-day results"'),
        ('<!-- Los minijuegos de cocina, en movimiento -->', '<!-- The cooking minigames, in motion -->'),
    ],
    'quienes-somos.html': [
        ('<title>Quiénes somos — YaloséGames</title>', '<title>About us — YaloséGames</title>'),
        ('content="Quiénes somos — YaloséGames"', 'content="About us — YaloséGames"'),
        ('YaloséGames es un estudio indie de Málaga. Conoce al equipo de Tourist Trap.',
         'YaloséGames is an indie studio from Málaga. Meet the Tourist Trap team.'),
        ('<h1 class="page-title">Quiénes somos</h1>', '<h1 class="page-title">About us</h1>'),
        ('El equipo detrás del chiringuito', 'The team behind the beach bar'),
        ('alt="Viñeta del chef de Tourist Trap"', 'alt="Comic panel of the Tourist Trap chef"'),
        ('Somos un estudio indie de Málaga formado por siete personas: tres de programación, dos de 3D y dos de 2D.',
         'We are an indie studio from Málaga made up of seven people: three in programming, two in 3D and two in 2D.'),
        ('Tourist Trap es nuestro primer juego, un simulador de cocina tycoon ambientado en un chiringuito andaluz, con mucho humor, gaviotas y clientes imposibles.',
         'Tourist Trap is our first game, a cooking tycoon sim set in an Andalusian beach bar, full of humour, seagulls and impossible customers.'),
        ('>El equipo<', '>The team<'),
        ('<span>Programación</span>', '<span>Programming</span>'),
    ],
    'contacto.html': [
        ('<title>Contacto — YaloséGames</title>', '<title>Contact — YaloséGames</title>'),
        ('content="Contacto — YaloséGames"', 'content="Contact — YaloséGames"'),
        ('Contacta con YaloséGames: prensa, festivales, testers o simplemente saludar.',
         'Get in touch with YaloséGames: press, festivals, playtesters or just saying hi.'),
        ('Contactar con nosotros', 'Get in touch'),
        ('Prensa, festivales, testers o simplemente saludar', 'Press, festivals, playtesters or just saying hi'),
        ('>Escríbenos<', '>Write to us<'),
        ('Cuéntanos qué necesitas y te respondemos al correo que nos dejes.',
         'Tell us what you need and we’ll reply to the email you leave us.'),
        ('<!-- Ajustes de FormSubmit -->', '<!-- FormSubmit settings -->'),
        # El correo que te llega sigue en español, con «(EN)» para saber de qué versión viene
        ('Nuevo mensaje desde yalosegames.github.io"', 'Nuevo mensaje desde yalosegames.github.io (EN)"'),
        ('value="Web de YaloséGames · yalosegames.github.io"', 'value="Web de YaloséGames (inglés) · yalosegames.github.io/en"'),
        (f'value="{SITE}/gracias.html"', f'value="{SITE}/en/gracias.html"'),
        ('<span>Nombre</span>', '<span>Name</span>'),
        ('<span>Correo</span>', '<span>Email</span>'),
        ('title="Escribe un correo válido, por ejemplo nombre@dominio.com"', 'title="Enter a valid email, e.g. name@domain.com"'),
        ('Por ejemplo: nombre@dominio.com', 'For example: name@domain.com'),
        ('<span>Motivo</span>', '<span>Reason</span>'),
        ('Elige uno…', 'Choose one…'),
        ('<option>Prensa</option>', '<option>Press</option>'),
        ('<option>Festival o evento</option>', '<option>Festival or event</option>'),
        ('<option>Quiero probar el juego</option>', '<option>I want to playtest the game</option>'),
        ('<option>Colaboración</option>', '<option>Collaboration</option>'),
        ('<option>Otro</option>', '<option>Other</option>'),
        ('<span>Mensaje</span>', '<span>Message</span>'),
        ('Usaremos tus datos solo para responderte.', 'We’ll only use your details to reply to you.'),
        ('Enviar mensaje', 'Send message'),
        ('>Kit de prensa<', '>Press kit<'),
        ('Logo, key art, capturas y el gameplay alpha de Tourist Trap están en la página del juego.',
         'Logo, key art, screenshots and the Tourist Trap alpha gameplay are on the game page.'),
        ('Ir a Tourist Trap', 'Go to Tourist Trap'),
        ('>También en<', '>Also on<'),
    ],
    'gracias.html': [
        ('<title>¡Gracias! — YaloséGames</title>', '<title>Thank you! — YaloséGames</title>'),
        ('content="Contacto — YaloséGames"', 'content="Contact — YaloséGames"'),
        ('Contacta con YaloséGames: prensa, festivales, testers o simplemente saludar.',
         'Get in touch with YaloséGames: press, festivals, playtesters or just saying hi.'),
        ('¡Mensaje enviado!', 'Message sent!'),
        ('Gracias por escribirnos', 'Thanks for writing to us'),
        ('Hemos recibido tu mensaje y te responderemos lo antes posible.',
         'We’ve received your message and will get back to you as soon as we can.'),
        ('Volver al inicio', 'Back to home'),
        ('Ver Tourist Trap', 'See Tourist Trap'),
    ],
}

# ---------------------------------------------------------------- Botón e idiomas
NAV_SKY = '    <label for="night" class="nav-sky"'

def boton(href, code, lang, label):
    return f'    <a class="lang-switch" href="{href}" hreflang="{lang}" lang="{lang}" aria-label="{label}">{code}</a>\n'

def alternates(page):
    path = '' if page == 'index.html' else page
    return (f'<link rel="alternate" hreflang="es" href="{SITE}/{path}">\n'
            f'<link rel="alternate" hreflang="en" href="{SITE}/en/{path}">\n')

def poner_idiomas(html, page, es):
    html = re.sub(r'    <a class="lang-switch"[^\n]*\n', '', html)
    html = re.sub(r'<link rel="alternate" hreflang="[a-z]+"[^\n]*\n', '', html)
    sw = boton(f'en/{page}', 'EN', 'en', 'Read this page in English') if es else \
         boton(f'../{page}', 'ES', 'es', 'Leer esta página en español')
    assert NAV_SKY in html, page
    html = html.replace(NAV_SKY, sw + NAV_SKY, 1)
    return html.replace('<meta name="twitter:card"', alternates(page) + '<meta name="twitter:card"', 1)

# Restos en español que delatan un texto sin traducir (se ignoran nombres propios y marcas)
PERMITIDO = ['YaloséGames', 'Málaga', 'Domínguez', 'Cascales Valentín', 'Poseidón', 'Chiringelio',
             'Nuevo mensaje desde', 'Web de YaloséGames (inglés)', 'Leer esta página en español',
             'Día / noche sin JavaScript', 'Patatas bravas', 'Paella', 'Gazpacho', 'Pinchitos']

avisos = 0
for page in PAGES:
    es_html = open(page, encoding='utf8').read()
    es_new = poner_idiomas(es_html, page, es=True)
    if es_new != es_html:
        open(page, 'w', encoding='utf8').write(es_new)

    en = poner_idiomas(es_new, page, es=False)
    for a, b in COMUN + POR_PAGINA[page]:
        if a not in en:
            if a in ('>Inicio</a>', '>Quiénes somos</a>', '>Contacto</a>'):
                continue
            print(f'⚠️  {page}: ya no encuentro «{a[:70]}»'); avisos += 1
        en = en.replace(a, b)
    # Rutas: en/ está una carpeta más abajo
    en = re.sub(r'(src|href)="(assets/|style\.css|favicon\.png|apple-touch-icon\.png)', r'\1="../\2', en)
    en = en.replace('<meta property="og:type"', '<meta property="og:locale" content="en_GB">\n<meta property="og:type"', 1)

    for linea in en.splitlines():
        texto = re.sub(r'<[^>]+>', ' ', linea)
        for p in PERMITIDO:
            texto = texto.replace(p, '')
        if re.search(r'[áéíóúñ¿¡]', texto) or re.search(r'\b(el|la|los|las|del|para|con|una?)\b', texto):
            print(f'⚠️  en/{page}: ¿sin traducir? {linea.strip()[:110]}'); avisos += 1

    os.makedirs('en', exist_ok=True)
    open(f'en/{page}', 'w', encoding='utf8').write(en)

subprocess.run([sys.executable, 'versionar.py'], check=True)
print(f'en/ generado ({len(PAGES)} páginas)' + (f' con {avisos} aviso(s)' if avisos else ', sin avisos'))
