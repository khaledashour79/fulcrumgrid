# -*- coding: utf-8 -*-
"""Regenerate sitemap.xml for every language.

Authoritative, full-rewrite generator: enumerates every public page from
loc_catalog.PAGES (the same registry that drives localization) and emits one
<url> per language (en, ar, fr, de, es, it, nl), each carrying the complete
xhtml:link hreflang cluster + x-default. Runs last in build.py, after the
localized trees exist.
"""
import os, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import i18n
from loc_catalog import PAGES

ROOT = os.environ.get('FG_ROOT') or os.path.abspath(os.path.join(HERE, '..', '..'))
TODAY = datetime.date.today().isoformat()

# Section indexes change more often than leaf pages.
WEEKLY = {'/', '/products/', '/pricing/', '/regions/', '/blog/'}


def meta(canon):
    depth = 0 if canon == '/' else canon.strip('/').count('/') + 1
    priority = {0: '1.0', 1: '0.8'}.get(depth, '0.6')
    changefreq = 'weekly' if canon in WEEKLY else 'monthly'
    return priority, changefreq


def alternates(canon):
    lines = []
    for l in i18n.LANGS:
        lines.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s%s" />'
                     % (l['code'], i18n.BASE, i18n.alt_href(l['code'], canon)))
    lines.append('    <xhtml:link rel="alternate" hreflang="x-default" href="%s%s" />'
                 % (i18n.BASE, i18n.alt_href('en', canon)))
    return '\n'.join(lines)


def file_for(canon, code):
    prefix = '' if code == 'en' else code + '/'
    if canon == '/':
        rel = 'index.html'
    elif canon.endswith('.html'):
        rel = canon.lstrip('/')
    else:
        rel = canon.strip('/') + '/index.html'
    return os.path.join(ROOT, prefix + rel)


def main():
    canons = [c for c in PAGES if c != '/404.html']
    if '/' not in canons:
        canons.append('/')  # home is always in the sitemap even when its localization is paused
    # Stable, readable order: home first, then alphabetical.
    canons.sort(key=lambda c: (c != '/', c))
    urls = []
    for canon in canons:
        priority, changefreq = meta(canon)
        alts = alternates(canon)
        for l in i18n.LANGS:
            if not os.path.exists(file_for(canon, l['code'])):
                continue  # language not generated (yet) — don't advertise a 404
            loc = i18n.BASE + i18n.alt_href(l['code'], canon)
            urls.append('  <url>\n    <loc>%s</loc>\n%s\n    <lastmod>%s</lastmod>\n'
                        '    <changefreq>%s</changefreq>\n    <priority>%s</priority>\n  </url>'
                        % (loc, alts, TODAY, changefreq, priority))
    doc = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + '\n'.join(urls) + '\n</urlset>\n')
    out = os.path.join(ROOT, 'sitemap.xml')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(doc)
    print('gen_sitemap: wrote %d urls across %d pages' % (len(urls), len(canons)))


if __name__ == '__main__':
    main()
