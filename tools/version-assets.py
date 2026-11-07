"""Add ?v=<hash> to assets/site.css and assets/site.js links so browsers fetch new versions.
Run from the repo root after editing anything in assets/:  python3 tools/version-assets.py"""
import glob, hashlib, re
for name in ["site.css", "site.js"]:
    h = hashlib.sha1(open("assets/" + name, "rb").read()).hexdigest()[:8]
    for f in glob.glob("*.html") + glob.glob("cursos/*.html"):
        s = open(f).read()
        t = re.sub(r'(assets/%s)(\?v=[0-9a-f]+)?"' % re.escape(name), r'\1?v=%s"' % h, s)
        if t != s: open(f, "w").write(t)
print("ok")
