# -*- coding: utf-8 -*-
"""Localization acceptance oracle.

For one or more canonical paths, (re)builds the fr/de/es/it/nl pages via
loc_static, then reports any *visible* text node that is byte-identical between
the English source and a localized page — i.e. text that should have been
translated but was not, because no catalog entry covers it.

An allowlist of terms that legitimately stay English (brand + product names,
acronyms, a few universal words) is excluded, as are nodes that are pure
punctuation, numbers, or code-like tokens.

Usage:
    python3 loc_check.py /faq/ /about/         # check specific canons
    python3 loc_check.py                        # check every registered page

Exit status is 0 only when nothing untranslated remains. Meant to be run with
FG_ROOT set (build.py sets it); falls back to the repo root otherwise.
"""
import os, re, sys, html as _html

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import i18n
from loc_catalog import COMMON, PAGES
import loc_static

ROOT = os.environ.get('FG_ROOT') or os.path.abspath(os.path.join(HERE, '..', '..'))

# Terms that are supposed to remain English on every localized page.
ALLOW = {
    'fulcrumgrid', 'command center', 'collection', 'hr suite', 'tms', 'voice',
    'crm', 'erp', 'blog', 'faq', 'api', 'saas', 'kpi', 'okr', 'okrs', 'kpis',
    'pto', 'hr', 'sop', 'dso', 'gcc', 'uae', 'uk', 'usa', 'eu', 'sar', 'aed',
    'qar', 'kwd', 'bhd', 'omr', 'egp', 'jod', 'sar', 'ig', 'ceo', 'cfo',
    'fulcrumgrid.com', 'hello@fulcrumgrid.com', 'english', 'arabic', 'français',
    'deutsch', 'español', 'italiano', 'nederlands', 'العربية',
    'avenlor consulting', 'avenlor consulting ↗', 'contact@avenlorconsulting.com',
    'fulcrum', 'grid', 'fulcrum grid',
}
# Strip the trailing "↗" glyph, bullets, and surrounding punctuation for compare.
_STRIP = ' \t\r\n·↗→—–-|/•:.,;!?()[]{}"\'’‘“”'


def _strip_tags(s):
    return re.sub(r'\s+', ' ', _html.unescape(re.sub(r'<[^>]+>', '', s))).strip()


# Text of every catalog key (COMMON + all page catalogs), tags stripped. A
# visible node whose text matches one of these is considered "handled": either
# it is translated, or the key is stale and already reported via MISSING.
HANDLED = {_strip_tags(k) for k in COMMON}
for _m in PAGES.values():
    HANDLED |= {_strip_tags(k) for k in _m.get('t', {})}


def _text_nodes(html_str):
    """Yield normalized visible text nodes (contents of <script>/<style> removed)."""
    html_str = re.sub(r'<script\b[^>]*>.*?</script>', ' ', html_str, flags=re.S | re.I)
    html_str = re.sub(r'<style\b[^>]*>.*?</style>', ' ', html_str, flags=re.S | re.I)
    # text between tags
    for chunk in re.split(r'<[^>]+>', html_str):
        t = _html.unescape(chunk).strip()
        if t:
            t = re.sub(r'\s+', ' ', t)
            yield t


def _is_meaningful_english(t):
    """Heuristic: does this node contain a lowercase English word worth translating?"""
    core = t.strip(_STRIP)
    if not core:
        return False
    low = core.lower()
    if low in ALLOW:
        return False
    if t in HANDLED or core in HANDLED:
        return False
    # Remove allowlisted terms, then see if letters remain.
    scrub = low
    for a in sorted(ALLOW, key=len, reverse=True):
        scrub = scrub.replace(a, ' ')
    # Need at least one run of >=3 ascii letters to be "a word".
    words = re.findall(r'[a-z]{3,}', scrub)
    return len(words) >= 1


def check(canon):
    src = os.path.join(ROOT, PAGES[canon]['src'])
    with open(src, encoding='utf-8') as f:
        en_nodes = set(_text_nodes(f.read()))
    leftovers = {}
    for lang in i18n.NEW_CODES:
        out = os.path.join(ROOT, lang, PAGES[canon]['src'])
        if not os.path.exists(out):
            continue
        with open(out, encoding='utf-8') as f:
            loc_nodes = list(_text_nodes(f.read()))
        bad = [t for t in loc_nodes
               if t in en_nodes and _is_meaningful_english(t)]
        if bad:
            leftovers[lang] = sorted(set(bad))
    return leftovers


def main():
    only = sys.argv[1:]
    canons = [c for c in only if c in PAGES] if only else sorted(PAGES)
    if only:
        # (re)build just these
        loc_static.MISSING.clear()
        for canon in canons:
            for lang in i18n.NEW_CODES:
                loc_static.localize(canon, PAGES[canon]['src'], lang)
    total = 0
    for canon in canons:
        lo = check(canon)
        if lo:
            n = sum(len(v) for v in lo.values())
            total += n
            print(f'\n### {canon}: {n} untranslated node(s)')
            # print the union across langs (fr representative)
            union = sorted({t for v in lo.values() for t in v})
            for t in union:
                print(f'    {t[:140]!r}')
    if loc_static.MISSING:
        print(f'\n!! {len(loc_static.MISSING)} stale catalog key(s) (declared but not in source):')
        for canon, en in loc_static.MISSING:
            print(f'    [{canon}] {en[:120]!r}')
    print(f'\nTOTAL untranslated nodes: {total}; stale keys: {len(loc_static.MISSING)}')
    sys.exit(0 if total == 0 and not loc_static.MISSING else 1)


if __name__ == '__main__':
    main()
