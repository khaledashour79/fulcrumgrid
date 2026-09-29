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

SW_RE = re.compile(r'<details class="lang-dd">.*?</details>'
                   r'|<div class="lang-switch"[^>]*>.*?</div>'
                   r'|<details class="lang-menu">.*?</details>', re.S)
HREFLANG_RE = re.compile(r'[ \t]*<link rel="alternate" hreflang="en"[^>]*>\s*'
                         r'<link rel="alternate" hreflang="ar"[^>]*>\s*'
                         r'<link rel="alternate" hreflang="x-default"[^>]*>')
OGLOCALE_RE = re.compile(r'[ \t]*<meta property="og:locale" content="[^"]*" />'
                         r'(?:\s*<meta property="og:locale:alternate" content="[^"]*" />)*')


MISSING = []


def apply_catalog(html, catalog, lang, strict, canon=None, word_boundary=False):
    """Replace EN text segments with their `lang` translation, longest first.

    strict=True (per-page catalogs) records any declared segment missing from
    the EN source into MISSING, to catch drift. strict=False (the shared COMMON
    catalog) silently skips segments a given page doesn't contain.

    word_boundary=True (COMMON chrome) only replaces a segment when it is not
    flanked by ASCII letters, so a chrome word like "Contact" never rewrites a
    larger token such as the JSON-LD `"@type":"ContactPage"`.
    """
    for en in sorted(catalog, key=len, reverse=True):
        tr = catalog[en].get(lang)
        if tr is None:
            continue
        if en not in html:
            if strict and (canon, en) not in MISSING:
                MISSING.append((canon, en))
            continue
        if word_boundary:
            html = re.sub(r'(?<![A-Za-z])' + re.escape(en) + r'(?![A-Za-z])', lambda m: tr, html)
        else:
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

    # 2b. Some source pages reference assets with root-relative paths
    #     (href="assets/...") which only resolve at the site root; under a
    #     language subdirectory (/fr/...) they 404. Make them absolute.
    html = re.sub(r'(href|src)="assets/', r'\1="/assets/', html)

    # 3. canonical + og:url -> localized absolute URL.
    url = i18n.BASE + i18n.alt_href(lang, canon)
    html = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), html, count=1)
    html = re.sub(r'(<meta property="og:url" content=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), html, count=1)

    # 4. Translate page copy + chrome (before link-prefixing, so catalog keys
    #    match the original English text; translations carry no hrefs).
    #    Per-page copy is applied FIRST (strict, longest-first) so a long page
    #    phrase like "Get started with FulcrumGrid in three steps" is translated
    #    whole before the shorter COMMON chrome key "Get started" could rewrite
    #    a fragment of it. COMMON then mops up standalone chrome occurrences.
    html = apply_catalog(html, PAGES.get(canon, {}).get('t', {}), lang, strict=True, canon=canon)
    html = apply_catalog(html, COMMON, lang, strict=False, word_boundary=True)

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
    if MISSING:
        print(f'\n  {len(MISSING)} declared segment(s) not found in source:')
        for canon, en in MISSING:
            print(f'    [{canon}] {en[:90]!r}')
        sys.exit(1)


if __name__ == '__main__':
    main()
