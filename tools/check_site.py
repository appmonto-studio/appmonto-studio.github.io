#!/usr/bin/env python3
"""Validate final static routes, reciprocal locales, links, assets and metadata."""
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
HOST='https://appmonto.com'

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links=[]; self.ids=set(); self.canonical=[]; self.alternates={}; self.h1=0; self.lang=None; self.json=[]; self.in_json=False; self.buffer=''; self.noindex=False
        self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html': self.lang=a.get('lang')
        if tag=='h1': self.h1+=1
        if 'id' in a:
            assert a['id'] not in self.ids, f'duplicate id {a["id"]}'
            self.ids.add(a['id'])
        if tag=='img': assert 'alt' in a, 'image lacks alt'
        if tag=='meta' and a.get('name')=='robots': self.noindex='noindex' in a.get('content','')
        if tag=='link' and a.get('rel')=='canonical': self.canonical.append(a['href'])
        if tag=='link' and a.get('hreflang'): self.alternates[a['hreflang']]=a['href']
        for k in ['href','src']:
            if k in a: self.links.append(a[k])
        if tag=='meta' and a.get('property') in ['og:image','og:url']: self.links.append(a['content'])
        if tag=='script' and a.get('type')=='application/ld+json': self.in_json=True; self.buffer=''
    def handle_data(self,data):
        if self.in_json: self.buffer+=data
    def handle_endtag(self,tag):
        if tag=='script' and self.in_json:
            self.json.append(json.loads(self.buffer)); self.in_json=False

paths=[p for p in ROOT.rglob('*.html') if not any(x in p.relative_to(ROOT).parts for x in ['content','docs','dist','.git'])]
pages={}
for p in paths:
    s=p.read_text(); rel=p.relative_to(ROOT).as_posix(); url=HOST+'/'+rel.removesuffix('index.html')
    page=Page(s); pages[url]=page
    assert page.h1==1, f'{rel}: expected one h1'
    assert page.lang in ['en','de','es'],rel
    if rel.startswith('kidlogicloft.github.io/'):
        assert page.noindex and len(page.canonical)==1 and page.canonical[0].startswith(HOST+'/'),rel
    elif rel!='404.html': assert page.canonical==[url],f'{rel}: canonical {page.canonical}'
    assert not re.search(r'KidLogic Loft|Cozy Meadow Farm|hello@kidlogicloft|no in.app purchases|keine in.app.käufe|sin compras dentro de la app',s,re.I),rel
    for data in page.json: assert isinstance(data,dict),rel

for url,page in pages.items():
    for link in page.links:
        dest=urlsplit(urljoin(url,link))
        assert dest.hostname!='kidlogicloft.com',f'{url}: stale link {link}'
        if dest.scheme not in ['http','https'] or dest.hostname!='appmonto.com': continue
        target=ROOT/unquote(dest.path).lstrip('/')
        if dest.path.endswith('/'): target=target/'index.html'
        assert target.is_file(),f'{url}: missing {link}'
        if dest.fragment and HOST+dest.path in pages:
            assert unquote(dest.fragment) in pages[HOST+dest.path].ids,f'{url}: missing anchor {link}'
    if page.alternates:
        assert set(page.alternates)=={'en','de','es','x-default'},url
        for lang,target in page.alternates.items():
            other=pages[target]
            assert other.lang==('en' if lang=='x-default' else lang),target
            assert other.alternates==page.alternates,f'nonreciprocal: {target}'

sitemap=ET.parse(ROOT/'sitemap.xml')
listed={n.text for n in sitemap.findall('.//{*}loc')}
expected={u for u,p in pages.items() if not p.noindex and not u.endswith('/404.html')}
assert listed==expected,f'sitemap mismatch: {listed ^ expected}'
for p in (ROOT/'assets').rglob('*.css'):
    for asset in re.findall(r'url\([\'"]?(/[^)\'" ]+)',p.read_text()):
        assert (ROOT/asset.lstrip('/')).is_file(),asset
print(f'Validated {len(pages)} pages; internal links, assets, anchors, locales, JSON-LD and sitemap pass.')
