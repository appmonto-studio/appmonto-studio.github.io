# appmonto-studio.github.io

The public site of **Appmonto Studio** — an independent app studio in Austria,
and the umbrella for the studio's app brands.

Live at **https://appmonto.com** (custom domain; also served at
https://appmonto-studio.github.io) via GitHub Pages.

## What this is

A one-page brand site: who the studio is, which brands it publishes under, and
how to reach it. Plus the legally required imprint and a privacy notice. It sells
nothing, tracks nothing, and has no backend.

Individual apps are documented on their own brand sites:

| Brand | Audience | Site |
|---|---|---|
| KidLogic Loft | Children, ages 3–8 | https://kidlogicloft.com |
| Elia | Birth and family life | https://getelia.app |
| _(third brand)_ | In development | — |

## Structure

```
.
├── index.html            # The site
├── 404.html
├── legal/index.html      # Imprint (Impressum) — noindex
├── privacy/index.html    # Website privacy notice
├── assets/
│   ├── css/site.css      # Hand-written, light + dark
│   └── img/              # logo.svg, favicon.svg, apple-touch-icon.png, og.png,
│                         # icon-512.png, play-icon-512.png (square, unrounded)
├── CNAME                 # appmonto.com
├── robots.txt            # Sitemap + AI-crawler opt-out
├── sitemap.xml
└── .nojekyll             # Serve files as-is
```

Plain HTML and CSS. No build step, no dependencies, no external fonts or scripts
— every asset is served from this repository.

## The mark

`assets/img/logo.svg` is the source of truth: a letter **A** whose silhouette is
also a peak, snow above the ridge line, rock below. The PNGs are rasterised from
the same geometry — regenerate them if the SVG changes, don't edit them by hand.
`play-icon-512.png` is the unrounded square version for store listings, which
apply their own corner mask.

## Before publishing

1. Register the domain and point it at GitHub Pages (below), then enable HTTPS.
2. Set up the `hello@appmonto.com` mailbox — the address appears on every page.
3. Add the VAT ID (UID-Nummer) to `legal/index.html` if the business leaves the
   small-business exemption (Kleinunternehmerregelung).

## Personal data on the site

The owner's name, postal address, and phone number appear **nowhere in plain
text** — not in the imprint, not in the privacy notice, not in the homepage
JSON-LD. They live as an XOR+base64 payload in the `data-x` attribute of the
`.reveal` block in `legal/index.html`, written into the page only when a reader
opens that `<details>` section. Crawlers render pages but do not open
`<details>`, so the values stay out of indexes and out of naive scrapes.

To change those details, regenerate the payload rather than typing them in:

```bash
python3 - <<'PY'
import base64, itertools
KEY = b"appmonto-studio"
frag = '<dl><dt>Owner</dt><dd>…</dd></dl>'   # the HTML fragment to hide
raw = frag.encode("utf-8")
print(base64.b64encode(bytes(b ^ k for b, k in zip(raw, itertools.cycle(KEY)))).decode())
PY
```

This is obfuscation, not secrecy: anyone determined can decode it. It stops
address harvesters and accidental indexing, nothing stronger. Keep plain-text
copies out of new pages, and re-run the grep below before publishing:

```bash
grep -rn "Sydorenko\|Liechtensteinklamm\|2712871" --include="*.html" .
```

The imprint carries `noindex` on purpose: it must be reachable under §5 ECG, but
it does not have to be searchable. It is deliberately **not** disallowed in
`robots.txt` — a crawler has to fetch the page to see the `noindex` tag.

## GitHub Pages setup

Settings → Pages → Source: **Deploy from a branch**, branch `main`, folder
`/ (root)`. Custom domain `appmonto.com`, **Enforce HTTPS** on.

DNS at the registrar:

```
A     @   185.199.108.153
A     @   185.199.109.153
A     @   185.199.110.153
A     @   185.199.111.153
CNAME www appmonto-studio.github.io.
```

The repository name matches the account name, so this is the account's **user
site** and is served from the domain root on both addresses. Every link in the
site is root-relative (`/legal/`, `/assets/…`) and resolves correctly either way
— keep it that way. A rename to anything else would turn this into a project
repo served under `/<repo>/`, and every one of those links would 404 on the
github.io address.

## Local preview

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000
