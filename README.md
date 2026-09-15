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

## The marks

Two pieces, drawn to the same geometry:

- **`assets/img/logo.svg`** — the app mark: a letter **A** whose silhouette is
  also a peak, snow above the ridge line, rock below. The PNGs are rasterised
  from the same geometry — regenerate them if the SVG changes, don't edit them by
  hand. `play-icon-512.png` is the unrounded square version for store listings,
  which apply their own corner mask.
- **`assets/img/wordmark.svg`** — APPMONTO, drawn as original geometric
  letterforms on a 100-unit cap-height grid. No typeface is involved, so nothing
  here is licensed from a foundry, and the wordmark's A repeats the app mark's
  peak at the same crossbar height.

The wordmark is painted through a CSS mask (`.brand__word`) rather than an
`<img>`, so it inherits `currentColor` and follows the light/dark theme. Its
width and height in CSS must keep the source aspect ratio of 768 × 116.

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

## Project descriptor

`appmonto.yaml` at the repository root identifies this project and points at sources that already
exist here, for studio-level tooling. It carries data and references only — never commands,
credentials, checkout paths, status, version numbers, or copies of release evidence — and makes no
claim about release readiness or store availability.

Keep its `sources` paths correct when a referenced document moves. Do not add derived state to it:
if a fact already lives in a document, the descriptor points at that document instead.

## Where future work is recorded

- `docs/roadmap.md` is the only task source in this repository. Record intended work there, not
  in a new file, a handoff, or a comment — a second inventory drifts from the first and
  studio tooling will report it as an undeclared task source.
- One heading is one task. Bullets under it are its specification. If a bullet is
  something you would close and report on its own, give it its own heading.
- Each entry carries `**<ID>** · `<status>`` directly under its heading, where status is
  `todo`, `blocked` or `idea`. A `blocked` entry names its blocker on the same line. A
  `todo` entry carries a `**Done when:**` paragraph stating a checkable condition.
- Identifiers use the `AWEB-NNN` form and are never reused, including after deletion.
  Take the next number from the file's header and raise the header in the same change.
- Delete an entry once delivered, but only after the decision behind it is recorded
  outside the task file. Record the choice, its reason, and the constraint it places on
  future work — including decisions to stop or revert, which are the easiest to lose and
  save the most. "We did it" is not worth keeping; version control already has that.
- The exact grammar, including the markers for sections that are not tasks, is in the
  header of the task file itself.

## Keeping the recorded state true

This is what the standing obligation to keep documentation current means for the task file and
the descriptor. Each item belongs in the change that causes it, not in a separate pass at the
end, and none of it waits to be asked for. If you suspect the record has drifted anyway, "wrap
up" asks for a sweep of the list below — but a sweep is a safety net, not the mechanism.

- **Work you finished:** delete its entry from `docs/roadmap.md` and record the decision behind
  it in `README.md` — the choice, its reason, and the constraint it now places on future work.
  "We did it" is not worth keeping; Git history already has that.
- **Work you decided to do:** add an entry, taking the next identifier from the file's header
  and raising that counter in the same change.
- **Work that became stuck:** set the entry to `blocked` and name what blocks it on the same
  line. A blocked entry that does not say why reads as neglect.
- **Work that turned out to need a decision rather than effort:** set it to `idea` and say what
  the decision is.
- **A `todo` entry you touched:** check its `**Done when:**` still describes what finishing
  means. If the work changed shape, the condition is stale.
- **A source that moved:** update the matching path in `appmonto.yaml`, or the board will report
  it missing.

Nothing here requires the studio console to be present. If it is, running its validator against
this checkout confirms the descriptor and its declared paths in one step.
