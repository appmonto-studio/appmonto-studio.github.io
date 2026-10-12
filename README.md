# appmonto-studio.github.io

The public site of **Appmonto Studio**, an independent app studio and game publisher
in Austria. Live at **https://appmonto.com** via GitHub Pages.

## Products and brand decisions

Appmonto Studio publishes the games directly. KidLogic Loft is retired as a
public-facing brand. “Games” is a descriptive section, not a replacement brand.
The speculative third-brand placeholder is removed because no approved product
was available. Elia remains a distinct family at https://getelia.app.

- Happy Octo Puzzle: released on Google Play, existing app identifier/store URL retained.
- Clever Beaver: in development.
- **Closer Look**: the calm interactive diorama series, with settings that may vary.
  **Closer Look: Farm** replaces Cozy Meadow Farm in current public copy and remains
  in development. No other series releases are announced.
- No ads in any app. In-app purchases are allowed; Farm purchases are planned.
  Never invent prices, included content, launch dates or a studio-wide subscription promise.
- Gameplay, store/billing services and support have separate privacy/offline implications.
  The legal operator has not changed. Keep published app identifiers unchanged.

## Structure and editing

Plain HTML/CSS with local JavaScript for the theme switch. No framework, package
manager, external fonts, runtime dependencies or required npm install.

| Source | Purpose |
|---|---|
| `content/games.json` | EN/DE/ES game, studio, support and privacy copy |
| `content/home/en.html` | Existing English studio homepage content |
| `content/octo/{en,de,es}.html` | Migrated detailed Happy Octo body content |
| `tools/generate_site.py` | Shared Appmonto shell, localized pages, metadata and sitemap |
| `index.html`, `de/`, `es/`, `games/`, `apps/`, `support/` | Committed generated pages served by Pages |
| `legal/index.html`, `privacy/index.html`, `404.html` | Existing hand-written legal, website privacy and error pages |
| `assets/css/site.css`, `assets/js/site.js` | Shared studio visual language and theme switch |
| `apps/happy-octo-puzzle/*.png`, `assets/img/shots/` | Preserved game images |
| `docs/kidlogic-migration.md` | Migration decisions, exact external cutover/rollback and deletion gates |
| `docs/migration-inventory.md` | Every source page/asset and its destination or retirement |

English routes use the root; German and Spanish use `/de/` and `/es/`. Each has
`games/`, `apps/happy-octo-puzzle/`, `apps/clever-beaver/`, `apps/closer-look-farm/`,
`games/privacy/`, and `support/`. `/privacy/` remains the website notice, distinct
from app privacy. Legal documents remain English with their language indicated.

Edit sources, then regenerate the committed files:

```bash
python3 tools/generate_site.py
python3 tools/build_site.py
node --check assets/js/site.js
git diff --check
```

`build_site.py` checks deterministic output, validates all internal links/assets,
locale reciprocity, canonical URLs, structured data and sitemap, and exports a
clean `dist/` production artifact. GitHub Pages still serves the committed root;
this export does not change its publishing configuration. No pre-existing lint or
type suite exists. Node is used only for the JavaScript syntax check; Python uses
its standard library. `dist/` and local caches are ignored.

## Production boundaries

Production cutover evidence is recorded in `docs/kidlogic-migration.md`. The old repository must remain
until the [cutover and deletion gates](docs/kidlogic-migration.md) are satisfied.
The owner chose a direct URL replacement: update store/app/contact references,
then retire the old website. Do not add old-domain redirects, legacy URL bridges,
or extra hosting infrastructure. Old website URLs are intentionally retired.
The owner confirmed `support@appmonto.com` works on 12 October 2026. `hello@appmonto.com` remains general studio/legal contact.

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
2. Keep `hello@appmonto.com` and `support@appmonto.com` working as described in the migration document.
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
