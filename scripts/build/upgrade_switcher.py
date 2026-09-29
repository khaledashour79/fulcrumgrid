# -*- coding: utf-8 -*-
"""Upgrade the existing English + Arabic static pages to the shared 7-language
switcher, the full hreflang cluster, and the localized og:locale block.

These pages predate the European languages: they carry a 2-item pill switcher
(EN / ع) and a 3-line hreflang block. This rewrites both, in place, using the
same i18n.py primitives the generated pages use, so every page — old and new —
advertises the same set of languages.

Usage:  python3 upgrade_switcher.py <canon> [<canon> ...]
        e.g.  python3 upgrade_switcher.py / /about/ /products/
Only the canonical paths given are touched (both their EN and AR files).
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import i18n

ROOT = os.environ.get('FG_ROOT') or os.path.abspath(os.path.join(HERE, '..', '..'))

SW_RE = re.compile(r'<div class="lang-switch"[^>]*>.*?</div>', re.S)
HREFLANG_RE = re.compile(r'[ \t]*<link rel="alternate" hreflang="en"[^>]*>\s*'
                         r'<link rel="alternate" hreflang="ar"[^>]*>\s*'
                         r'<link rel="alternate" hreflang="x-default"[^>]*>')
# og:locale line plus however many og:locale:alternate lines follow it.
OGLOCALE_RE = re.compile(r'[ \t]*<meta property="og:locale" content="[^"]*" />'
                         r'(?:\s*<meta property="og:locale:alternate" content="[^"]*" />)+')


def canon_to_file(canon, code):
    prefix = '' if code == 'en' else 'ar/'
    if canon == '/':
        rel = 'index.html'
    elif canon.endswith('.html'):
        rel = canon.lstrip('/')
    else:
        rel = canon.strip('/') + '/index.html'
    return os.path.join(ROOT, prefix + rel)


def upgrade(canon, code):
    path = canon_to_file(canon, code)
    if not os.path.exists(path):
        print(f'  - skip (absent): {path.replace(ROOT + "/", "")}')
        return
    with open(path, encoding='utf-8') as f:
        html = f.read()
    before = html
    html = SW_RE.sub('@@SWITCH@@', html)
    html = HREFLANG_RE.sub('@@HREFLANG@@', html, count=1)
    html = OGLOCALE_RE.sub('@@OGLOCALE@@', html, count=1)
    html = html.replace('@@HREFLANG@@', i18n.hreflang_block(canon))
    html = html.replace('@@OGLOCALE@@', i18n.og_locale_block(code))
    html = html.replace('@@SWITCH@@', i18n.lang_switch(code, canon))
    if html == before:
        print(f'  = unchanged: {path.replace(ROOT + "/", "")}')
        return
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  ✓ {code}  {path.replace(ROOT + "/", "")}')


def main():
    canons = sys.argv[1:]
    if not canons:
        from loc_catalog import PAGES  # all registered pages (static + generated)
        canons = sorted(PAGES)
    for canon in canons:
        for code in ('en', 'ar'):
            upgrade(canon, code)


if __name__ == '__main__':
    main()
