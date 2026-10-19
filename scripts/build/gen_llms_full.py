#!/usr/bin/env python3
"""Generate llms-full.txt — a single plain-text dump of the site's core content
for LLMs to ingest in one fetch (English + Arabic).

It is built from the already-generated HTML: the text inside each page's <main>
(nav, header, footer, the concierge widget and all scripts/styles are skipped).
Runs late in build.py, after every page tree exists.

Page selection mirrors llms.txt: the English pages are exactly the ones llms.txt
links to (core pages + the evergreen blog guides), and for each we include the
Arabic equivalent (/ar/...) when that file exists. Templated region pages and the
daily Q&A posts are intentionally left out — llms-full.txt is the curated,
high-value content, not every URL (that is what sitemap.xml is for).
"""
import os, re, html
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = 'https://fulcrumgrid.com'
LLMS = os.path.join(ROOT, 'llms.txt')
OUT = os.path.join(ROOT, 'llms-full.txt')

BLOCK = {'p', 'div', 'section', 'article', 'header', 'footer', 'ul', 'ol', 'li',
         'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'tr', 'thead', 'tbody',
         'br', 'blockquote', 'figure', 'figcaption', 'details', 'summary', 'dl', 'dt', 'dd'}
SKIP = {'script', 'style', 'noscript', 'svg', 'template'}
HEAD = {'h1': '# ', 'h2': '## ', 'h3': '### ', 'h4': '#### ', 'h5': '##### ', 'h6': '###### '}


class MainText(HTMLParser):
    """Collect readable text from inside <main>, with light markdown headings."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_main = 0
        self.skip = 0
        self.out = []
        self.cur = []
        self.head = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'main':
            self.in_main += 1
            return
        if self.in_main <= 0:
            return
        if tag in SKIP:
            self.skip += 1
            return
        if tag in HEAD:
            self._flush(); self.head = HEAD[tag]
        elif tag in BLOCK:
            self._flush()
        if tag in ('td', 'th') and self.cur:
            self.cur.append('·')

    def handle_startendtag(self, tag, attrs):
        if self.in_main > 0 and self.skip == 0 and tag == 'br':
            self._flush()

    def handle_endtag(self, tag):
        if tag == 'main':
            if self.in_main > 0:
                self._flush(); self.in_main -= 1
            return
        if self.in_main <= 0:
            return
        if tag in SKIP:
            if self.skip > 0:
                self.skip -= 1
            return
        if tag in BLOCK:
            self._flush()

    def handle_data(self, data):
        if self.in_main <= 0 or self.skip > 0:
            return
        t = re.sub(r'\s+', ' ', data).strip()
        if t:
            self.cur.append(t)

    def _flush(self):
        line = ' '.join(x for x in self.cur if x).strip()
        self.cur = []
        if self.head:
            line = (self.head + line) if line else ''
            self.head = ''
        line = re.sub(r'\s+·\s+', ' · ', line).strip(' ·')
        if line:
            self.out.append(line)

    def text(self):
        self._flush()
        lines, prev_blank = [], False
        for l in self.out:
            l = re.sub(r'[ \t]+', ' ', l).strip()
            if not l:
                continue
            lines.append(l)
        return '\n\n'.join(lines)


def page_text(path):
    try:
        with open(path, encoding='utf-8') as f:
            src = f.read()
    except OSError:
        return ''
    p = MainText()
    try:
        p.feed(src)
    except Exception:
        pass
    return p.text()


def url_to_file(url):
    path = url.split(SITE, 1)[-1]
    path = path.split('#', 1)[0].split('?', 1)[0]
    if not path.startswith('/'):
        return None
    rel = path.lstrip('/')
    if rel == '' or rel.endswith('/'):
        rel = rel + 'index.html'
    return os.path.join(ROOT, rel)


def parse_llms():
    """Return (summary, [(title, url)]) from llms.txt, in document order."""
    with open(LLMS, encoding='utf-8') as f:
        s = f.read()
    m = re.search(r'^>\s*(.+)$', s, re.M)
    summary = m.group(1).strip() if m else ''
    links = re.findall(r'^- \[([^\]]+)\]\((' + re.escape(SITE) + r'[^)]+)\)', s, re.M)
    return summary, links


def main():
    summary, links = parse_llms()

    seen = set()
    pages = []  # (title, url, file)

    def add(title, url):
        f = url_to_file(url)
        if not f or url in seen or not os.path.isfile(f):
            return
        seen.add(url)
        pages.append((title, url, f))

    # English set: exactly what llms.txt curates (skip its Arabic links for now).
    en_links = [(t, u) for (t, u) in links if '/ar/' not in u]
    ar_links = [(t, u) for (t, u) in links if '/ar/' in u]
    for t, u in en_links:
        add(t, u)

    # Arabic mirror: the /ar/ equivalent of every English page, when it exists,
    # plus any /ar/ links llms.txt lists directly.
    for t, u in en_links:
        tail = u.split(SITE, 1)[-1]
        if tail == '/' or tail == '':
            ar = SITE + '/ar/'
        else:
            ar = SITE + '/ar' + tail
        add(t + ' (العربية)', ar)
    for t, u in ar_links:
        add(t, u)

    parts = []
    parts.append('# FulcrumGrid — full text for LLMs')
    if summary:
        parts.append('> ' + summary)
    parts.append('This file inlines the readable content of FulcrumGrid\'s core pages '
                 '(English and Arabic) in one place. Index with links: ' + SITE + '/llms.txt · '
                 'Full page list: ' + SITE + '/sitemap.xml')

    body = []
    for title, url, f in pages:
        txt = page_text(f)
        if not txt:
            continue
        body.append('\n' + ('=' * 72) + '\n## ' + title + '\nURL: ' + url + '\n' + ('-' * 72) + '\n\n' + txt)

    out = '\n'.join(parts) + '\n' + '\n'.join(body) + '\n'
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(out)
    print('gen_llms_full: wrote llms-full.txt — %d pages, %d KB' % (len(pages), len(out.encode('utf-8')) // 1024))


if __name__ == '__main__':
    main()
