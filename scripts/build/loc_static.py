# -*- coding: utf-8 -*-
"""Localize the hand-authored (non-generator) static pages into the European
languages (fr, de, es, it, nl).

Structure — <html lang>, hreflang cluster, og:locale, canonical/og:url, the
language switcher, and internal-link prefixing — is applied mechanically by
i18n.py, so it is identical and correct on every page. The visible text comes
from hand-written catalogs (loc_catalog.py): a COMMON catalog for chrome that
repeats on every page (nav, footer, buttons) plus a per-page catalog for that
page's own copy.

English and Arabic pages already exist and are the source of truth for layout;
this script never writes to them (their switcher/hreflang are upgraded
separately by migrate_switcher.py).

Idempotent: regenerates the committed localized HTML from the EN source.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import i18n
from loc_catalog import COMMON, PAGES

ROOT = os.environ.get('FG_ROOT') or os.path.abspath(os.path.join(HERE, '..', '..'))

SW_RE = re.compile(r'<div class="lang-switch"[^>]*>.*?</div>', re.S)
HREFLANG_RE = re.compile(r'[ \t]*<link rel="alternate" hreflang="en"[^>]*>\s*'
                         r'<link rel="alternate" hreflang="ar"[^>]*>\s*'
                         r'<link rel="alternate" hreflang="x-default"[^>]*>')
OGLOCALE_RE = re.compile(r'[ \t]*<meta property="og:locale" content="en_US" />\s*'
                         r'<meta property="og:locale:alternate" content="ar_AR" />')


def apply_catalog(html, catalog, lang, strict):
    """Replace EN text segments with their `lang` translation, longest first.

    strict=True (per-page catalogs) errors if a declared segment is missing, to
    catch drift between the catalog and the EN source. strict=False (the shared
    COMMON catalog) silently skips segments a given page doesn't contain.
    """
    for en in sorted(catalog, key=len, reverse=True):
        tr = catalog[en].get(lang)
        if tr is None:
            continue
        if en not in html:
            if strict:
                raise SystemExit(f'  ! segment not found in source: {en[:70]!r}')
            continue
        html = html.replace(en, tr)
    return html


def localize(canon, src_rel, lang):
    src = os.path.join(ROOT, src_rel)
    with open(src, encoding='utf-8') as f:
        html = f.read()

    # 1. Protect structural blocks from link-prefixing / text replacement.
    html = SW_RE.sub('@@SWITCH@@', html, count=2)
    html = HREFLANG_RE.sub('@@HREFLANG@@', html, count=1)
    html = OGLOCALE_RE.sub('@@OGLOCALE@@', html, count=1)

    # 2. <html lang="en"> -> localized (all new langs are LTR).
    html = html.replace('<html lang="en">', f'<html lang="{lang}">', 1)

    # 3. canonical + og:url -> localized absolute URL.
    url = i18n.BASE + i18n.alt_href(lang, canon)
    html = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), html, count=1)
    html = re.sub(r'(<meta property="og:url" content=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), html, count=1)

    # 4. Translate chrome + page copy (before link-prefixing, so catalog keys
    #    match the original English text; translations carry no hrefs).
    html = apply_catalog(html, COMMON, lang, strict=False)
    html = apply_catalog(html, PAGES.get(canon, {}).get('t', {}), lang, strict=True)

    # 5. Prefix internal links (skips assets, external, anchors, mailto).
    html = i18n.prefix_links(html, lang)

    # 6. Swap structural placeholders for final localized markup.
    html = html.replace('@@HREFLANG@@', i18n.hreflang_block(canon))
    html = html.replace('@@OGLOCALE@@', i18n.og_locale_block(lang))
    html = html.replace('@@SWITCH@@', i18n.lang_switch(lang, canon))

    # 7. Write to /<lang>/<path>/index.html (or /<lang>/404.html etc).
    out_rel = src_rel if src_rel.endswith('.html') and '/' not in src_rel else src_rel
    out = os.path.join(ROOT, lang, src_rel)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    return out


def main():
    only = set(sys.argv[1:])  # optional: canonical paths to build
    langs = i18n.NEW_CODES
    n = 0
    for canon, meta in PAGES.items():
        if only and canon not in only:
            continue
        for lang in langs:
            out = localize(canon, meta['src'], lang)
            n += 1
            print(f'  {lang}  {out.replace(ROOT + "/", "")}')
    print(f'loc_static: wrote {n} pages')


if __name__ == '__main__':
    main()
