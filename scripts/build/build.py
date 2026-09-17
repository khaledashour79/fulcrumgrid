#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FulcrumGrid site build.

Regenerates the generator-owned pages (pricing + blog) from the structured
content under /content/. Idempotent: with content unchanged it reproduces the
committed HTML byte-for-byte, so it is safe to run on every deploy.

Content is the source of truth:
  content/blog/*.json      one file per post (full for CMS-authored posts,
                           catalogue-only for legacy posts kept as static HTML)
  content/blog/_order.json display order (newest first)
  content/pricing/*.json   per-app pricing (tiers, prices, module matrix)

OG card images are NOT regenerated here (they need a headless browser). Run
scripts/build/gen_og.py + gen_og2.py by hand when an app's name/price/plans
change; the committed PNGs under assets/og/ are used at deploy time.
"""
import os, sys, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

# gen_pricing runs its work at import/module scope; gen_blog under __main__.
STEPS = ['gen_pricing.py', 'gen_blog.py']

def main():
    env = dict(os.environ, FG_ROOT=ROOT)
    for script in STEPS:
        print('\n=== build: %s ===' % script)
        subprocess.check_call([sys.executable, os.path.join(HERE, script)], env=env)
    print('\nbuild complete')

if __name__ == '__main__':
    main()
