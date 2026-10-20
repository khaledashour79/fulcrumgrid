# -*- coding: utf-8 -*-
"""Cache-bust selected /assets/ references in the built HTML.

GitHub Pages serves static assets with `Cache-Control: max-age=600` and no
content hash in the filename, so a browser keeps serving an old JS/CSS file for
up to ten minutes after a deploy. For the interactive homepage scripts that we
iterate on (the orbit sphere, the explorer), that stale window is confusing.

This step appends a short content-hash query (`?v=<hash>`) to those references
across every built HTML page, so the URL changes whenever the file's bytes
change and the browser is forced to refetch. It is idempotent: any existing
`?v=...` is stripped and replaced with the current hash, so rebuilding with an
unchanged asset yields identical output.

Runs after all HTML is generated (loc_static / gen_daily / gen_concierge) so it
versions the European and concierge-injected pages too. Add an asset path to
ASSETS to have it versioned.
"""
import os, re, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get('FG_ROOT') or os.path.abspath(os.path.join(HERE, '..', '..'))

# Site-root-relative asset paths to version. Keep this to the scripts that
# actually change and whose staleness is user-visible; site-wide infra assets
# (fg2.css, consent.js) are stable and left alone to avoid churning every page.
ASSETS = [
    'assets/js/hero-orbit.js',
    'assets/js/explorer.js',
]

SKIP_DIRS = ('/.git', '/node_modules', '/scripts', '/content', '/workers', '/og_out', '/og_out2')


def _hash(path):
    with open(path, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()[:8]


def main():
    vers = {}
    for a in ASSETS:
        p = os.path.join(ROOT, a)
        if os.path.exists(p):
            vers[a] = _hash(p)
    if not vers:
        print('cachebust: no assets found, nothing to do')
        return

    pats = [(re.compile(r'(src="/' + re.escape(a) + r')(\?v=[0-9a-f]+)?(")'), v)
            for a, v in vers.items()]

    changed = 0
    for dirpath, dirs, files in os.walk(ROOT):
        if any(seg in dirpath for seg in SKIP_DIRS):
            dirs[:] = []
            continue
        for fn in files:
            if not fn.endswith('.html'):
                continue
            fp = os.path.join(dirpath, fn)
            with open(fp, encoding='utf-8') as f:
                s = f.read()
            orig = s
            for pat, v in pats:
                s = pat.sub(r'\1?v=' + v + r'\3', s)
            if s != orig:
                with open(fp, 'w', encoding='utf-8') as f:
                    f.write(s)
                changed += 1
    print('cachebust: versioned %d asset(s) across %d page(s)' % (len(vers), changed))


if __name__ == '__main__':
    main()
