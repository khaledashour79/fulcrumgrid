# -*- coding: utf-8 -*-
"""Arabic page acceptance checker for the new-design /ar/ re-skin.

For each given Arabic page it verifies the structural markers (new-design CSS,
RTL, Cairo font, lang=ar) and flags any *visible* text node that is still
English prose — i.e. a run of Latin words that is not an allowlisted brand /
product / technology name or acronym. Meant to drive the Arabic re-skin to a
clean state, the way loc_check.py drove the European re-localization.

Usage:
    python3 ar_check.py ar/index.html ar/about/index.html
    python3 ar_check.py            # all ar/**/index.html + ar/404.html
Exit status 0 only when every checked page is structurally correct and has no
leftover English prose.
"""
import os, re, sys, glob, html as _html

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get('FG_ROOT') or os.path.abspath(os.path.join(HERE, '..', '..'))

# Latin terms that legitimately stay in Latin script on an Arabic page.
ALLOW = {
    'fulcrumgrid', 'command center', 'collection', 'hr suite', 'tms', 'voice',
    'crm', 'erp', 'blog', 'faq', 'api', 'rest api v1', 'saas', 'kpi', 'okr',
    'okrs', 'kpis', 'pto', 'hr', 'sop', 'dso', 'dpo', 'gcc', 'uae', 'uk',
    'usa', 'eu', 'sar', 'aed', 'qar', 'kwd', 'bhd', 'omr', 'egp', 'jod', 'ig',
    'ceo', 'cfo', 'sso', 'scim', 'mfa', 'tls', 'gdpr', 'sepa', 'vat', 'na',
    'me', 'sap business one', 'webhooks', 'sandbox', 'paye', 'ni', 'wps',
    'gosi', 'nitaqat', 'starter', 'growth', 'business', 'enterprise', 'pilot',
    'professional', 'agency', 'fulcrum', 'grid', 'fulcrumgrid.com',
    'contact@avenlorconsulting.com', 'avenlor consulting', 'google analytics',
    'fig', 'fg-100', 'assembly', 'english', 'arabic', 'العربية', 'français',
    'deutsch', 'español', 'italiano', 'nederlands', 'sheet', 'net', 'cia',
    'pia', 'sif', 'eosb', 'ksa', 'odoo', 'oracle', 'quickbooks',
    'quickbooks online', 'qbo', 'sap', 'cloud',
}
_STRIP = ' \t\r\n·↗→—–-|/•:.,;!?()[]{}"\'’‘“”%&+#'


def _text_nodes(h):
    h = re.sub(r'<script\b[^>]*>.*?</script>', ' ', h, flags=re.S | re.I)
    h = re.sub(r'<style\b[^>]*>.*?</style>', ' ', h, flags=re.S | re.I)
    for chunk in re.split(r'<[^>]+>', h):
        t = _html.unescape(chunk).strip()
        if t:
            yield re.sub(r'\s+', ' ', t)


def _english_leftover(t):
    """Does this node contain untranslated English prose (not just proper nouns)?"""
    core = t.strip(_STRIP)
    if not core or core.lower() in ALLOW:
        return False
    has_ar = bool(re.search(r'[؀-ۿ]', core))
    # Remove allowlisted terms (case-insensitively), preserving case elsewhere.
    scrub = core
    for a in sorted(ALLOW, key=len, reverse=True):
        scrub = re.sub(r'(?<![A-Za-z])' + re.escape(a) + r'(?![A-Za-z])', ' ', scrub, flags=re.I)
    lat = re.findall(r'[A-Za-z]{3,}', scrub)
    if has_ar:
        # Inside an Arabic node, Capitalized/ALL-CAPS Latin tokens are proper
        # nouns (brands, product names, example companies like Airbnb) and are
        # fine. Only a cluster of lowercase English words signals untranslated
        # English prose.
        lower = [w for w in lat if w[:1].islower()]
        return len(lower) >= 2
    # Pure-Latin node: any two+ English words (of any case) is untranslated.
    return len(lat) >= 2


def check(path):
    full = os.path.join(ROOT, path)
    problems = []
    with open(full, encoding='utf-8') as f:
        h = f.read()
    if 'assets/css/fg2.css' not in h:
        problems.append('MISSING fg2.css (still old design?)')
    if 'assets/css/fg.css' in h.replace('fg2.css', ''):
        problems.append('references old fg.css')
    if 'dir="rtl"' not in h:
        problems.append('missing dir="rtl"')
    if 'cairo' not in h.lower():
        problems.append('missing Cairo font (self-hosted preload / @font-face)')
    if '<html lang="ar"' not in h:
        problems.append('missing <html lang="ar">')
    leftovers = sorted({t for t in _text_nodes(h) if _english_leftover(t)})
    return problems, leftovers


def main():
    args = sys.argv[1:]
    if args:
        pages = args
    else:
        pages = sorted(glob.glob(os.path.join(ROOT, 'ar', '**', 'index.html'), recursive=True))
        p404 = os.path.join(ROOT, 'ar', '404.html')
        if os.path.exists(p404):
            pages.append(p404)
        pages = [os.path.relpath(p, ROOT) for p in pages]
    total_probs = total_left = 0
    for page in pages:
        probs, left = check(page)
        if probs or left:
            print(f'\n### {page}')
            for p in probs:
                print(f'    [struct] {p}')
            for t in left:
                print(f'    [en] {t[:130]!r}')
        total_probs += len(probs)
        total_left += len(left)
    print(f'\nPAGES: {len(pages)}; structural problems: {total_probs}; english leftovers: {total_left}')
    sys.exit(0 if total_probs == 0 and total_left == 0 else 1)


if __name__ == '__main__':
    main()
