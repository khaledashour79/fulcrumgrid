# -*- coding: utf-8 -*-
"""Inject (or remove) the concierge AI-character widget on every built page.

Runs LAST in build.py, after every page (EN + AR + fr/de/es/it/nl + generated
pricing/regions/blog/daily) exists on disk, so one pass reaches them all.

Idempotent in both directions:
  * concierge_config.ENABLED True  -> ensure the stylesheet link, the mount +
    bootstrap script (between markers), and the CSP additions are present.
  * ENABLED False -> strip any previously injected markup and CSP additions.

The markup lives between <!-- fg-concierge:start --> and <!-- fg-concierge:end -->
so it is replaced, never duplicated.
"""
import os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import concierge_config as cfg

ROOT = os.environ.get('FG_ROOT') or os.path.abspath(os.path.join(HERE, '..', '..'))

CSS_LINK = '<link rel="stylesheet" href="/assets/css/concierge.css">'
M_A, M_B = '<!-- fg-concierge:start -->', '<!-- fg-concierge:end -->'
# Directories never scanned (no HTML pages we own, or third-party).
SKIP_DIRS = {'.git', 'node_modules', 'assets', 'workers', 'scripts', 'content', 'docs'}


def _block():
    """The mount + bootstrap, rebuilt each run from current config."""
    langs = ','.join("'%s'" % l for l in cfg.LANGS)
    boot = (
        'window.FG_CONCIERGE={'
        "endpoint:'%s'," % cfg.WORKER_ORIGIN +
        "riveSrc:'%s'," % cfg.RIVE_SRC +
        'langs:[%s]};' % langs
    )
    return (
        '%s\n'
        '<div id="fg-concierge" data-fg-concierge hidden></div>\n'
        '<script>%s</script>\n'
        '<script src="/assets/js/concierge.js" defer></script>\n'
        '%s' % (M_A, boot, M_B)
    )


def _strip(html):
    html = re.sub(re.escape(M_A) + r'.*?' + re.escape(M_B) + r'\n?', '', html, flags=re.S)
    html = html.replace('  ' + CSS_LINK + '\n', '').replace(CSS_LINK + '\n', '').replace(CSS_LINK, '')
    return html


def _patch_csp(html, enable):
    """Add/remove the Worker origin in connect-src and media-src blob: for audio."""
    m = re.search(r'(<meta http-equiv="Content-Security-Policy" content=")([^"]*)(")', html)
    if not m:
        return html
    csp = m.group(2)
    origin = cfg.WORKER_ORIGIN.strip()
    # always start from a clean slate for our additions
    if origin:
        csp = csp.replace(' ' + origin, '')
    csp = re.sub(r"\s*media-src 'self' blob:;", '', csp)
    if enable:
        if origin and 'connect-src' in csp:
            csp = re.sub(r'(connect-src )([^;]*)(;)', lambda mm: mm.group(1) + mm.group(2) + ' ' + origin + mm.group(3), csp, count=1)
        # audio returned by the Worker is played from a blob: URL
        if 'media-src' not in csp:
            csp = csp.rstrip()
            if not csp.endswith(';'):
                csp += ';'
            csp += " media-src 'self' blob:;"
    return html[:m.start(2)] + csp + html[m.end(2):]


def process(path, enable):
    with open(path, encoding='utf-8') as f:
        html = f.read()
    if '</body>' not in html:
        return False
    before = html
    html = _strip(html)                       # remove any prior injection first
    html = _patch_csp(html, enable)
    if enable:
        if '</head>' in html and CSS_LINK not in html:
            html = html.replace('</head>', '  ' + CSS_LINK + '\n</head>', 1)
        html = html.replace('</body>', _block() + '\n</body>', 1)
    if html != before:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        return True
    return False


def main():
    enable = bool(getattr(cfg, 'ENABLED', False)) and bool(cfg.WORKER_ORIGIN.strip())
    if getattr(cfg, 'ENABLED', False) and not cfg.WORKER_ORIGIN.strip():
        print('gen_concierge: ENABLED but WORKER_ORIGIN is empty — skipping injection.')
    changed = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith('.')]
        for fn in filenames:
            if fn.endswith('.html'):
                if process(os.path.join(dirpath, fn), enable):
                    changed += 1
    print('gen_concierge: %s on %d page(s) [enabled=%s]' % (
        'injected' if enable else 'stripped', changed, enable))


if __name__ == '__main__':
    main()
