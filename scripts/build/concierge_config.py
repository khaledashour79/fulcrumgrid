# -*- coding: utf-8 -*-
"""Concierge (AI voice character) build configuration.

The concierge is a lower-left animated character that greets visitors, listens
by voice (Web Speech API) and answers through a Cloudflare Worker that proxies
Claude + a neural TTS. The front-end lives in assets/js/concierge.js +
assets/css/concierge.css; the Worker lives in workers/concierge/.

Nothing is injected into the public site until ENABLED is True AND a WORKER_ORIGIN
is set. Keep ENABLED False until:
  1. the Worker is deployed (workers/concierge/README.md) and reachable, and
  2. the Rive artwork (.riv) is in place at assets/brand/concierge.riv
     (the widget falls back to a built-in SVG placeholder if it is missing).
"""

# Master switch. False = the injector strips any previously-injected widget
# markup from every page, so flipping off fully removes it.
ENABLED = True

# Deployed Worker origin, no trailing slash, e.g.
#   'https://fg-concierge.<your-subdomain>.workers.dev'
# or a custom route like 'https://concierge.fulcrumgrid.com'.
# Added to each page's CSP connect-src when ENABLED.
WORKER_ORIGIN = 'https://fg-concierge.khaled-ashour.workers.dev'

# Languages that get the voice/chat experience now. Others still render the
# character but route interaction to the contact page until added here.
LANGS = ['en', 'ar']

# Path (site-absolute) to the Rive artwork once supplied. If the file is absent
# at runtime the widget shows the built-in SVG placeholder instead.
RIVE_SRC = '/assets/brand/concierge.riv'
