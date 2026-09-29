# -*- coding: utf-8 -*-
"""Shared i18n primitives for the FulcrumGrid site.

Single source of truth for the language list and for the structural markup that
must be identical on every page in every language: the header/footer language
switcher, the <link rel="alternate" hreflang> cluster, the og:locale tags, and
internal-link prefixing (e.g. /products/ -> /fr/products/).

Text translation is NOT handled here — that lives in per-page catalogs. This
module only owns the parts that are mechanical and must never be wrong.
"""
import re

BASE = 'https://fulcrumgrid.com'

# Order controls switcher + hreflang order. English first, Arabic second
# (existing convention), then the European languages.
LANGS = [
    {'code': 'en', 'prefix': '',    'native': 'English',    'short': 'EN', 'locale': 'en_US', 'dir': 'ltr', 'word': 'Language'},
    {'code': 'ar', 'prefix': '/ar', 'native': 'العربية',    'short': 'ع',  'locale': 'ar_AR', 'dir': 'rtl', 'word': 'اللغة'},
    {'code': 'fr', 'prefix': '/fr', 'native': 'Français',   'short': 'FR', 'locale': 'fr_FR', 'dir': 'ltr', 'word': 'Langue'},
    {'code': 'de', 'prefix': '/de', 'native': 'Deutsch',    'short': 'DE', 'locale': 'de_DE', 'dir': 'ltr', 'word': 'Sprache'},
    {'code': 'es', 'prefix': '/es', 'native': 'Español',    'short': 'ES', 'locale': 'es_ES', 'dir': 'ltr', 'word': 'Idioma'},
    {'code': 'it', 'prefix': '/it', 'native': 'Italiano',   'short': 'IT', 'locale': 'it_IT', 'dir': 'ltr', 'word': 'Lingua'},
    {'code': 'nl', 'prefix': '/nl', 'native': 'Nederlands', 'short': 'NL', 'locale': 'nl_NL', 'dir': 'ltr', 'word': 'Taal'},
]

BY_CODE = {l['code']: l for l in LANGS}
CODES = [l['code'] for l in LANGS]
NEW_CODES = ['fr', 'de', 'es', 'it', 'nl']  # languages added on top of en + ar

GLOBE = ('<svg class="lang-globe" viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" '
         'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a15 15 0 0 1 0 18a15 15 0 0 1 0-18z"/></svg>')
CARET = ('<svg class="lang-caret" viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" '
         'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>')


def alt_href(code, canonical):
    """Absolute-on-site href for `canonical` (e.g. '/', '/products/') in `code`."""
    prefix = BY_CODE[code]['prefix']
    if canonical == '/':
        return prefix + '/' if prefix else '/'
    return prefix + canonical


def lang_switch(current, canonical, indent='        '):
    """The <details> language dropdown, current language marked active.

    `canonical` is the language-independent path ('/', '/products/', ...); each
    entry links to the same page in its own language.
    """
    cur = BY_CODE[current]
    lines = [f'{indent}<details class="lang-menu">',
             f'{indent}  <summary aria-label="{cur["word"]}">{GLOBE}<span>{cur["short"]}</span>{CARET}</summary>',
             f'{indent}  <div class="lang-menu-list">']
    for l in LANGS:
        href = alt_href(l['code'], canonical)
        active = ' class="active" aria-current="true"' if l['code'] == current else ''
        lines.append(f'{indent}    <a href="{href}" hreflang="{l["code"]}" lang="{l["code"]}"{active}>{l["native"]}</a>')
    lines.append(f'{indent}  </div>')
    lines.append(f'{indent}</details>')
    return '\n'.join(lines)


def hreflang_block(canonical, indent='  '):
    """<link rel="alternate" hreflang> cluster for all languages + x-default."""
    lines = []
    for l in LANGS:
        lines.append(f'{indent}<link rel="alternate" hreflang="{l["code"]}" href="{BASE}{alt_href(l["code"], canonical)}" />')
    lines.append(f'{indent}<link rel="alternate" hreflang="x-default" href="{BASE}{alt_href("en", canonical)}" />')
    return '\n'.join(lines)


def og_locale_block(current, indent='  '):
    cur = BY_CODE[current]
    lines = [f'{indent}<meta property="og:locale" content="{cur["locale"]}" />']
    for l in LANGS:
        if l['code'] != current:
            lines.append(f'{indent}<meta property="og:locale:alternate" content="{l["locale"]}" />')
    return '\n'.join(lines)


# Internal links that must NOT be language-prefixed.
_SKIP_HREF = re.compile(r'^(#|mailto:|tel:|https?:|//|/assets/|/site\.webmanifest|/sitemap|/robots)')


def prefix_links(html, code):
    """Prefix root-relative internal links with the language prefix.

    Rewrites href="/..." (and the home href="/") to href="/<code>/...".
    Leaves assets, external URLs, anchors, mailto/tel, and manifest/sitemap
    untouched. `src` attributes (images/scripts) are always left untouched.
    """
    prefix = BY_CODE[code]['prefix']
    if not prefix:
        return html

    def repl(m):
        attr, quote, url = m.group(1), m.group(2), m.group(3)
        if _SKIP_HREF.match(url) or not url.startswith('/'):
            return m.group(0)
        seg = url.split('/', 2)
        if len(seg) > 1 and seg[1] in BY_CODE and seg[1] != 'en':
            return m.group(0)  # already language-prefixed
        return f'{attr}={quote}{prefix}{url}{quote}'

    return re.sub(r'(href)=(["\'])([^"\']*)(["\'])', repl, html)
