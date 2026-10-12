# Games consolidation and direct URL cutover

## Decisions

Appmonto Studio is the public publisher for Happy Octo Puzzle, Clever Beaver and
Closer Look: Farm. KidLogic Loft is retired as a public-facing brand. “Games” is
a descriptive section, not a new brand. Closer Look is the calm interactive diorama
series; Closer Look: Farm replaces Cozy Meadow Farm. Settings may vary between
releases; no other releases are announced. Elia retains https://getelia.app and
its distinct identity; its repository is outside this migration.

The owner explicitly chose **direct URL replacement without redirects** because
there are no known external links worth maintaining. Update known website,
privacy and support references, then retire the old site. Old custom-domain and
GitHub project URLs are intentionally allowed to stop working. Do not add HTTP
redirects, HTML refresh bridges, Cloudflare Workers or other compatibility hosting.
No continuity checks for old URLs are deletion prerequisites.

No advertising is allowed in any app. Optional in-app purchases are allowed;
Closer Look: Farm purchases are planned, with no approved prices or included-content
offer. Happy Octo's current free/no-subscription statement remains app-specific.
Separate offline gameplay from downloads, store billing/restoration and support.
Published package ID `com.kidlogicloft.happyocto`, store URLs and legal operator
remain unchanged. The imprint's encoded operator payload is preserved.

## Audit and content inventory

Audit date: 12 October 2026. Destination base: `4f506c1`; source revision:
`61676a2ac56710b676f6c142fc4b07b4c4a1fbcd`. Both checkouts were initially clean.
Both websites use static HTML/CSS/JS on GitHub Pages, with no package manager or
framework. The source has three generated homepages and hand-written Happy Octo
and privacy pages. All nine source routes were reachable during the audit.

The source repository is `appmonto-studio/kidlogicloft.github.io`, with the custom
domain `kidlogicloft.com`. Appmonto keeps its existing GitHub Pages publishing
configuration, `CNAME=appmonto.com`, `.nojekyll`, studio assets and theme script.
No new hosting provider or destination DNS migration is required.

[migration-inventory.md](migration-inventory.md) accounts for all 37 tracked source
files. All 12 game image files (icon, banner and five screenshot/full-image pairs)
were copied unchanged and verified by SHA-256. Source studio marks, styles and
scripts were replaced by existing Appmonto components. The source has no additional
game artwork, downloads or dedicated Beaver/Farm pages. No secrets, local settings,
caches or build output were copied.

Here `L` means empty, `de/` or `es/`. This is a content mapping, not a redirect map:

| Source content | Destination on appmonto.com |
|---|---|
| `/L` game catalog | `/Lgames/` |
| `/Lapps/happy-octo-puzzle/` | Same path |
| `/Lprivacy/` game policy | `/Lgames/privacy/` |
| Clever Beaver homepage card | `/Lapps/clever-beaver/` |
| Cozy Meadow Farm homepage card | `/Lapps/closer-look-farm/` |
| Support contacts | `/Lsupport/` with app-specific mailto subjects |
| Happy Octo icon/banner and screenshots | Same asset paths |

New studio homepages are `/`, `/de/` and `/es/`. Existing English documents remain
at `/legal/` and `/privacy/`; the latter is the **website** notice, not app privacy.
Game routes have translated navigation, reciprocal hreflang, final canonical URLs,
Open Graph and structured data. The sitemap contains 22 final indexable URLs.
There are no legacy-slug aliases or project-path compatibility pages.

## Known references to replace

The public [Happy Octo listing](https://play.google.com/store/apps/details?id=com.kidlogicloft.happyocto)
was inspected during the audit. It identifies Appmonto Studio and exposes the old
privacy URL and a Gmail support address. Its Data safety section describes no
collection/sharing; this does not establish future billing behaviour.

| Reference | Final value / owner action |
|---|---|
| Play privacy: `https://kidlogicloft.com/privacy/` | `https://appmonto.com/games/privacy/` |
| Game website field, if configured | `https://appmonto.com/apps/happy-octo-puzzle/` |
| Play support email: `vr.sommerfeld@gmail.com` | `support@appmonto.com` |
| Website contact: `hello@kidlogicloft.com` | `support@appmonto.com` |
| General studio/legal contact | Keep `hello@appmonto.com` |

Use `/de/` or `/es/` equivalents for localized website/privacy fields where supported.
A website field was not visible on the public listing; inspect Console rather
than assuming one exists. Check any app settings, draft listings, profiles or
other owner-controlled places that contain the old URLs and replace them directly.
Do not rename package IDs or app namespaces. Installed-app link changes, if needed,
belong in a separate app release; this task does not edit app code or store records.

The destination had no dedicated support mailbox. `support@appmonto.com` is the
proposed new address and must be configured and tested by the owner. Legacy email
forwarding is optional and independent of website retirement, not a required web
redirect mechanism. If desired, `hello@kidlogicloft.com` can forward to the new
mailbox; do not forward unrelated personal Gmail messages. No email administration
has been performed here.

## Deployment order (owner-run)

1. Review the content and current Happy Octo free/no-subscription statement. Set up
   `support@appmonto.com` and verify receipt and replies. Keep the legal operator
   unchanged. Farm-specific billing disclosures must be finalized before app launch.
2. Retain the source archive described below and save relevant Pages/DNS/mail
   configuration separately for recovery. Record the current production revision.
3. From the Appmonto checkout run:
   ```sh
   python3 tools/generate_site.py --check
   python3 tools/build_site.py
   node --check assets/js/site.js
   git diff --check
   ```
   Push the approved commits to Appmonto `main` when ready. Existing GitHub Pages
   branch publishing remains unchanged; no extra infrastructure is needed.
4. Verify all sitemap URLs and `/legal/` on production, image loading, EN/DE/ES
   navigation, desktop/mobile and dark mode. Verify the app privacy page at
   `/games/privacy/`, website policy at `/privacy/`, and support mailto subjects.
5. Replace the Play Console privacy, support email and website fields using the
   table above. Update any other known app/profile references. Check the public
   listing after publication; new targets must work before the old website stops.
6. Disable the old website's GitHub Pages publishing and retire its web DNS records
   as appropriate. Do not create redirects or migrate the old domain to another
   provider. Preserve mail DNS if email on that domain is still in use.
7. After the deletion conditions below are met, the owner may separately delete
   the old repository. No repository deletion or production action is performed
   by this local implementation task.

## Rollback

Keep the source repository/archive and prior provider configuration until cutover
is accepted. If the new site needs repair, fix or restore its pages while keeping
new store references usable. To revert the whole cutover, restore old Pages/DNS
settings and verify the old site before changing store references back. Revert
Appmonto changes with new commits and publish normally; do not rewrite history.
Retain a working support mailbox throughout. There is no redirect service to undo.

## Archive and repository deletion

A local archive exists outside the website repositories in
`KidLogicLoft/migration-archives/2026-10-12/`: `kidlogicloft.bundle` (all locally
available refs and full history), `kidlogicloft-head.tar.gz` (tracked HEAD),
`SHA256SUMS`, and restoration notes. Bundle verification, a clean restore and
`git fsck --full` passed; restored HEAD matches the audited source revision.
Ignored local settings and live provider configuration are not included.
Copy the archive to independent durable storage and update it if the source changes.

The old repository is ready for deletion only after:

1. Needed content/assets are in Appmonto (locally verified).
2. Appmonto is deployed and new pages, privacy and support links are verified.
3. Known store/app/contact references have been replaced and checked.
4. The new support mailbox works.
5. A recoverable archive and relevant provider configuration are retained.

Old URL continuity and website redirects are explicitly **not** required by the
owner's revised decision. Local implementation alone does not establish the other
production conditions.

## Validation and remaining limits

The simplified production build validates 24 HTML documents (21 localized pages
and three existing documents), internal links/assets/anchors, canonical URLs,
reciprocal languages, JSON-LD and sitemap, including the clean `dist/` export.
JavaScript syntax and whitespace checks pass. No pre-existing lint/type suite
exists. Removing redirect infrastructure does not change the visible product pages.

Earlier browser checks covered the live source sites, updated homepage/catalog,
all game page types, privacy and support, desktop/mobile, light/dark themes, actual
DE-to-ES switching and visible keyboard focus. All 21 localized pages at 320px
had one h1, no document overflow and no broken loaded images. All 12 migrated image
hashes match; the legal operator payload is unchanged. The source checkout was not
modified. Redirect tests and provider dry runs are no longer relevant to this design.

No authenticated Play Console, DNS, hosting or email administration was performed.
Unreleased-app billing facts remain release-time work. Original legal wording is
preserved in source history/archive; current policy scopes gameplay claims to Happy
Octo, acknowledges support/store processing and avoids zero-security-risk promises.
Future work is tracked only in `docs/roadmap.md`; this document is the decision and
operating procedure, not a second task inventory.
