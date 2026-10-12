# Source inventory

Source revision: `61676a2ac56710b676f6c142fc4b07b4c4a1fbcd`.

Every tracked source file is accounted for below. No fonts, additional game artwork, download archives, or dedicated Beaver/Farm pages exist in the source. Only Happy Octo has a store link.

| Source file | Destination / replacement | Decision |
|---|---|---|
| `.gitignore` | `—` | Source repository guidance/configuration retained in archive; not copied to public site |
| `AGENTS.md` | `—` | Source repository guidance/configuration retained in archive; not copied to public site |
| `CNAME` | `infra/redirects/wrangler.jsonc` | Do not copy; old custom domain becomes redirect service |
| `README.md` | `—` | Source repository guidance/configuration retained in archive; not copied to public site |
| `apple-touch-icon.png` | `assets/img/apple-touch-icon.png` | Retired source studio mark; use existing Appmonto mark |
| `appmonto.yaml` | `—` | Source repository guidance/configuration retained in archive; not copied to public site |
| `apps/happy-octo-puzzle/banner.png` | `apps/happy-octo-puzzle/banner.png` | Copied unchanged (SHA-256 verified) |
| `apps/happy-octo-puzzle/icon.png` | `apps/happy-octo-puzzle/icon.png` | Copied unchanged (SHA-256 verified) |
| `apps/happy-octo-puzzle/index.html` | `apps/happy-octo-puzzle/index.html` | Migrated; copy and publisher updated |
| `assets/app.css` | `assets/css/site.css` | Retired source styles/script; Appmonto components replace them |
| `assets/home.css` | `assets/css/site.css` | Retired source styles/script; Appmonto components replace them |
| `assets/img/shots/happy-octo-puzzle/01-packs-full.jpg` | `assets/img/shots/happy-octo-puzzle/01-packs-full.jpg` | Copied unchanged (SHA-256 verified) |
| `assets/img/shots/happy-octo-puzzle/01-packs.jpg` | `assets/img/shots/happy-octo-puzzle/01-packs.jpg` | Copied unchanged (SHA-256 verified) |
| `assets/img/shots/happy-octo-puzzle/02-offline-full.jpg` | `assets/img/shots/happy-octo-puzzle/02-offline-full.jpg` | Copied unchanged (SHA-256 verified) |
| `assets/img/shots/happy-octo-puzzle/02-offline.jpg` | `assets/img/shots/happy-octo-puzzle/02-offline.jpg` | Copied unchanged (SHA-256 verified) |
| `assets/img/shots/happy-octo-puzzle/03-gameplay-full.jpg` | `assets/img/shots/happy-octo-puzzle/03-gameplay-full.jpg` | Copied unchanged (SHA-256 verified) |
| `assets/img/shots/happy-octo-puzzle/03-gameplay.jpg` | `assets/img/shots/happy-octo-puzzle/03-gameplay.jpg` | Copied unchanged (SHA-256 verified) |
| `assets/img/shots/happy-octo-puzzle/04-pieces-full.jpg` | `assets/img/shots/happy-octo-puzzle/04-pieces-full.jpg` | Copied unchanged (SHA-256 verified) |
| `assets/img/shots/happy-octo-puzzle/04-pieces.jpg` | `assets/img/shots/happy-octo-puzzle/04-pieces.jpg` | Copied unchanged (SHA-256 verified) |
| `assets/img/shots/happy-octo-puzzle/05-forest-full.jpg` | `assets/img/shots/happy-octo-puzzle/05-forest-full.jpg` | Copied unchanged (SHA-256 verified) |
| `assets/img/shots/happy-octo-puzzle/05-forest.jpg` | `assets/img/shots/happy-octo-puzzle/05-forest.jpg` | Copied unchanged (SHA-256 verified) |
| `assets/privacy.css` | `assets/css/site.css` | Retired source styles/script; Appmonto components replace them |
| `assets/site.css` | `assets/css/site.css` | Retired source styles/script; Appmonto components replace them |
| `assets/site.js` | `assets/js/site.js` | Retired source styles/script; Appmonto components replace them |
| `de/apps/happy-octo-puzzle/index.html` | `de/apps/happy-octo-puzzle/index.html` | Migrated; copy and publisher updated |
| `de/index.html` | `de/games/index.html` | Migrated; copy and publisher updated |
| `de/privacy/index.html` | `de/games/privacy/index.html` | Migrated; copy and publisher updated |
| `docs/roadmap.md` | `—` | Source repository guidance/configuration retained in archive; not copied to public site |
| `es/apps/happy-octo-puzzle/index.html` | `es/apps/happy-octo-puzzle/index.html` | Migrated; copy and publisher updated |
| `es/index.html` | `es/games/index.html` | Migrated; copy and publisher updated |
| `es/privacy/index.html` | `es/games/privacy/index.html` | Migrated; copy and publisher updated |
| `favicon.png` | `favicon.png` | Retired source studio mark; use existing Appmonto mark |
| `index.html` | `games/index.html` | Migrated; copy and publisher updated |
| `privacy/index.html` | `games/privacy/index.html` | Migrated; copy and publisher updated |
| `robots.txt` | `robots.txt` | Replaced by Appmonto configuration covering final routes |
| `sitemap.xml` | `sitemap.xml` | Replaced by Appmonto configuration covering final routes |
| `tools/generate_home.py` | `tools/generate_site.py + content/` | Localized useful copy migrated; source generator retired |

Ignored local `.claude/` settings and Python caches are explicitly excluded from migration and the tracked-source archive.
