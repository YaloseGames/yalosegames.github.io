"""Pon una versión al style.css en todas las páginas para que el navegador no use uno viejo.
Ejecútalo después de cambiar style.css:  python versionar.py  → luego Push origin."""
import glob, hashlib, os, re

os.chdir(os.path.dirname(os.path.abspath(__file__)))
v = hashlib.md5(open('style.css', 'rb').read()).hexdigest()[:8]
for page in glob.glob('*.html') + glob.glob('en/*.html') + glob.glob('_layouts/*.html'):
    html = open(page, encoding='utf8').read()
    new = re.sub(r'href="((?:/|\.\./)?)style\.css(?:\?v=[0-9a-f]+)?"', lambda m: f'href="{m.group(1)}style.css?v={v}"', html)
    if new != html:
        open(page, 'w', encoding='utf8').write(new)
print('style.css?v=' + v)
