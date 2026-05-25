# BSDRP website: DokuWiki → MkDocs conversion plan

## 0. Goal and scope

Replace the DokuWiki site backed up in `~/bsdrp-dokuwiki/bsdrp.net/` with a
[MkDocs](https://www.mkdocs.org/) site living in this repository. The new site
will be served from the same domain (`bsdrp.net`) on the same Apache host that
currently runs DokuWiki, so DokuWiki URLs must keep working via
`301 Moved Permanently` redirects.

Decisions already taken with the user:

| Topic              | Decision                                                                                                       |
| ------------------ | -------------------------------------------------------------------------------------------------------------- |
| Conversion engine  | `pandoc` (it has a `dokuwiki` reader) + a small Python post-processor for the bits pandoc gets wrong.          |
| French content     | **Dropped.** Only the English tree (`data/pages/` minus `fr/` and minus `wiki/`/`playground/`) is carried over. |
| Deployment         | Same domain, replacing DokuWiki in place. 301s written into the Apache `.htaccess`.                            |
| Diagrams           | Phase 1: copy PNG/GIF as-is. Phase 2 (follow-up): redraw network diagrams as Mermaid.                          |
| Page history       | Discarded (we are starting fresh — git will track future changes).                                             |

Tooling on this machine (already installed):

- `pandoc` 3.9.0.2 (with `dokuwiki` input reader)
- `mkdocs` 1.6.1
- `mkdocs-mermaid2-plugin` 0.6.0
- Python 3.11

We will additionally need (install with `pkg install` or `pip install`):

- **mkdocs-material** — the theme (gives admonitions, code copy, search, dark mode)
- **mkdocs-redirects** — optional, only used if we ever want internal redirects;
  the public-facing 301s live in `.htaccess`

## 1. Inventory of the source

```
data/pages/          79 .txt files     (DokuWiki source)
data/media/          85 image/PDF files (PNG, GIF, SVG, 1 PDF)
```

Top-level English namespaces actually used:

- `bsdrp.txt`                  → site home
- `features.txt`
- `downloads.txt`
- `license.txt`
- `contributors.txt`
- `community/how_to_contribute.txt`, `community/mailing_lists.txt`
- `documentation/end-users_docs.txt`        (+ implicit anchors)
- `documentation/faq.txt`
- `documentation/examples.txt`              (landing page)
- `documentation/examples/*.txt`            (≈ 50 lab/benchmark pages)
- `documentation/technical_docs.txt`
- `documentation/technical_docs/{bench_lab,nanobsd,poudriere,performance}.txt`

To drop entirely (will still receive 301s pointing at the new home page):

- `fr/**` (French — user confirmed not to keep)
- `wiki/**` (DokuWiki's bundled syntax/welcome pages)
- `playground/**` (sandbox)

DokuWiki syntax actually used in the corpus (counts via grep):

| Syntax                                    | Count   | Pandoc handles? | Notes                                                                                   |
| ----------------------------------------- | ------- | --------------- | --------------------------------------------------------------------------------------- |
| `====== H1 ======` … `== H5 ==`           | many    | yes             |                                                                                         |
| `[[ns:page|label]]` interwiki links       | hundreds| partial         | Pandoc emits the link but we must rewrite the URL into the new namespace + drop `.html` |
| `[[http://…|label]]` external links       | many    | yes             |                                                                                         |
| `{{ :path/file.png |alt}}` image embeds   | 86      | yes             | Pandoc rewrites to `![alt](path/file.png)`; we must fix the path                        |
| `{{https://…/img.png}}` remote images     | a few   | yes             | Leave as-is                                                                             |
| `{{description>…}}` SEO macro             | many    | **no**          | Strip; emit as front-matter `description:`                                              |
| `~~NOTOC~~` / `~~NOCACHE~~`               | 5       | **no**          | Strip; map `~~NOTOC~~` to `hide: [toc]` front-matter                                    |
| `<code>` blocks (also `<code lang>`)      | hundreds| yes             | Becomes a fenced code block; pandoc preserves the language                              |
| `<file name>` blocks                      | 29      | yes             | Same as code, with filename annotation                                                  |
| `^ table headers ^` / `| cells |`         | many    | yes             | DokuWiki tables → pipe tables                                                           |
| Bullet `  *` / numbered `  -` lists       | many    | yes             | Indentation-sensitive — pandoc handles it                                               |
| `**bold**`, `//italic//`, `__under__`     | many    | yes             |                                                                                         |
| `<note>` / `<note warning>` boxes         | 0–few   | partial         | Post-processor maps to mkdocs-material `!!! note` admonitions if any are found          |
| Footnotes `((…))`                         | a few   | yes             |                                                                                         |

## 2. Target site layout

```
bsdrp-website/
├── mkdocs.yml
├── docs/
│   ├── index.md                       (← bsdrp.txt)
│   ├── features.md
│   ├── downloads.md
│   ├── license.md
│   ├── contributors.md
│   ├── community/
│   │   ├── how-to-contribute.md
│   │   └── mailing-lists.md
│   ├── documentation/
│   │   ├── end-users-docs.md
│   │   ├── faq.md
│   │   ├── examples.md
│   │   ├── examples/
│   │   │   └── *.md                  (≈ 50 files, kebab-case)
│   │   ├── technical-docs.md
│   │   └── technical-docs/
│   │       ├── bench-lab.md
│   │       ├── nanobsd.md
│   │       ├── performance.md
│   │       └── poudriere.md
│   └── assets/
│       └── images/...                (mirrors DokuWiki media tree)
├── scripts/
│   ├── convert.sh                    (orchestrator)
│   ├── postprocess.py                (fixes pandoc output)
│   └── build_htaccess.py             (emits the 301 map)
├── overrides/                        (optional mkdocs-material theme tweaks)
├── .htaccess                         (generated — committed for review)
├── LICENSE
├── README.md
└── CONVERSION_PLAN.md                (this file)
```

Filename convention: lowercase, words separated by hyphens (`end-users-docs.md`,
not `end-users_docs.md`). This is consistent with mkdocs-material defaults and
makes URLs look modern. The redirect map below takes care of the rename.

## 3. mkdocs.yml (initial sketch)

```yaml
site_name: BSD Router Project
site_url: https://bsdrp.net/
site_description: BSD Router Project — open source router distribution based on FreeBSD
repo_url: https://github.com/ocochard/BSDRP
edit_uri: ""           # site repo is separate from BSDRP source

theme:
  name: material
  features:
    - navigation.sections
    - navigation.indexes
    - navigation.top
    - content.code.copy
    - search.suggest
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      toggle: { icon: material/weather-night, name: Switch to dark mode }
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      toggle: { icon: material/weather-sunny, name: Switch to light mode }

markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - footnotes
  - tables
  - toc:
      permalink: true
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.details
  - pymdownx.highlight
  - pymdownx.inlinehilite
  - pymdownx.snippets

plugins:
  - search

nav:
  - Home: index.md
  - Features: features.md
  - Downloads: downloads.md
  - Documentation:
      - documentation/end-users-docs.md
      - FAQ: documentation/faq.md
      - Examples:
          - documentation/examples.md
          - documentation/examples/*.md       # expanded by hand in final nav
      - Technical:
          - documentation/technical-docs.md
          - documentation/technical-docs/bench-lab.md
          - documentation/technical-docs/nanobsd.md
          - documentation/technical-docs/poudriere.md
          - documentation/technical-docs/performance.md
  - Community:
      - community/how-to-contribute.md
      - community/mailing-lists.md
  - About:
      - License: license.md
      - Contributors: contributors.md
```

## 4. Conversion pipeline

`scripts/convert.sh` is idempotent — running it again wipes `docs/` (except
hand-written extras) and regenerates it from the DokuWiki backup.

Pipeline per source file `data/pages/<ns>/<name>.txt`:

1. **Filter.** Skip if the namespace is `fr/`, `wiki/`, or `playground/`.
2. **Pre-clean** the DokuWiki text:
   - Strip `~~NOTOC~~`, `~~NOCACHE~~` (record `notoc=true` for step 6).
   - Extract `{{description>…}}` content into `description=…` for the
     front-matter, then remove the macro.
   - Normalize `<code lang>` blocks (pandoc handles `<code>` but is picky about
     the language token).
3. **Run pandoc.**
   `pandoc -f dokuwiki -t gfm --wrap=none input.txt -o output.md`
   GFM (GitHub-flavoured markdown) is the closest target to what mkdocs-material
   expects; we'll add admonitions in the post-processor.
4. **Post-process** the markdown (`scripts/postprocess.py`):
   - Rewrite DokuWiki link targets to mkdocs paths:
     - `documentation:examples:pf_and_carp_lab` →
       `documentation/examples/pf-and-carp-lab.md`
     - `documentation:end-users_docs#installation` →
       `documentation/end-users-docs.md#installation`
     - Lowercase the whole path, replace `_` with `-`, replace `:` with `/`.
   - Rewrite image paths: `{{:documentation:examples:foo.png}}` →
     `![](assets/images/documentation/examples/foo.png)`.
   - Convert any `<note>` / `<note warning>` blocks pandoc left behind into
     `!!! note` / `!!! warning` admonitions.
   - Inject YAML front-matter at the top:
     ```yaml
     ---
     title: <H1 from first heading>
     description: <text from {{description>...}} if any>
     ---
     ```
5. **Copy media** from `data/media/` into `docs/assets/images/`, preserving the
   sub-tree. `dont-panic-…png` and the `wiki/` media are dropped.
6. **Emit the redirect map.** `scripts/build_htaccess.py` walks the source tree
   and produces a list of `(old_url, new_url)` pairs (see §5).

The post-processor is conservative: anything it doesn't understand it leaves
alone, and prints a warning. A first dry-run will surface the long tail of
edge cases (3-5 files probably need a hand-tweak — `wiki/syntax.txt` is the
worst offender but we're dropping it anyway).

## 5. 301 redirect map

DokuWiki's `.htaccess` already rewrites unknown paths to `doku.php?id=<path>`.
We replace that block with explicit 301s for every old URL, then fall through
to MkDocs' generated static files.

Mapping rules (all 301):

| Old (DokuWiki, case-insensitive)                          | New (MkDocs)                                          |
| --------------------------------------------------------- | ----------------------------------------------------- |
| `/`                                                       | `/` (served by MkDocs `index.md`)                     |
| `/bsdrp` (DokuWiki home alias)                            | `/`                                                   |
| `/features`                                               | `/features/`                                          |
| `/downloads`                                              | `/downloads/`                                         |
| `/license`                                                | `/license/`                                           |
| `/contributors`                                           | `/contributors/`                                      |
| `/community/how_to_contribute`                            | `/community/how-to-contribute/`                       |
| `/community/mailing_lists`                                | `/community/mailing-lists/`                           |
| `/documentation/end-users_docs`                           | `/documentation/end-users-docs/`                      |
| `/documentation/faq`                                      | `/documentation/faq/`                                 |
| `/documentation/examples`                                 | `/documentation/examples/`                            |
| `/documentation/examples/<dokuwiki_name>`                 | `/documentation/examples/<kebab-case-name>/`          |
| `/documentation/technical_docs`                           | `/documentation/technical-docs/`                      |
| `/documentation/technical_docs/<name>`                    | `/documentation/technical-docs/<name>/`               |
| `/fr/**` (any French page)                                | `/` (or the closest English equivalent if obvious)    |
| `/wiki/**`, `/playground/**`                              | `/` (low value content, send home)                    |
| `/_media/<path>`                                          | `/assets/images/<path>`                               |
| `/_detail/<path>`, `/_export/**`                          | `/` (DokuWiki-only endpoints)                         |

The map is produced as an Apache `.htaccess` snippet, e.g.:

```apache
RewriteEngine on
RewriteBase /

# Always HTTPS + canonical host (kept from the old config)
RewriteCond %{HTTPS} !=on
RewriteRule ^/?(.*) https://%{SERVER_NAME}/$1 [R=301,L]
RewriteCond %{HTTP_HOST} ^www\.bsdrp\.net [NC]
RewriteRule ^(.*)$ https://bsdrp.net/$1 [R=301,L]

# DokuWiki → MkDocs explicit redirects (generated)
RewriteRule ^bsdrp/?$                                  /                                                [R=301,L]
RewriteRule ^community/how_to_contribute/?$            /community/how-to-contribute/                    [R=301,L]
RewriteRule ^community/mailing_lists/?$                /community/mailing-lists/                        [R=301,L]
RewriteRule ^documentation/end-users_docs/?$           /documentation/end-users-docs/                   [R=301,L]
RewriteRule ^documentation/examples/pf_and_carp_lab/?$ /documentation/examples/pf-and-carp-lab/         [R=301,L]
# … one line per DokuWiki page …

# Media URLs DokuWiki served via /_media/
RewriteRule ^_media/(.+)$  /assets/images/$1  [R=301,L]

# Drop French content
RewriteRule ^fr(/.*)?$     /                  [R=301,L]

# Catch DokuWiki endpoints we no longer serve
RewriteRule ^(doku|feed|index|lib/.*)\.php$  /  [R=301,L]
RewriteRule ^_(detail|export)/.*             /  [R=301,L]
```

The script `scripts/build_htaccess.py` produces these `RewriteRule` lines
deterministically from the source filenames so the map cannot drift from the
content.

## 6. Phased execution

### Phase A — scaffolding (small, reviewable commit)

1. Install `py311-mkdocs-material` (or `pip install --user mkdocs-material`).
2. Add `mkdocs.yml` per §3, with a stub `docs/index.md` so `mkdocs serve`
   works.
3. Commit the scaffolding + this plan.

### Phase B — bulk conversion

1. Write `scripts/convert.sh` + `scripts/postprocess.py` + `scripts/build_htaccess.py`.
2. Run the pipeline. Output: `docs/**/*.md`, `docs/assets/images/**`, `.htaccess`.
3. Review the diff. For each warning the post-processor emitted, decide:
   fix in script (preferred) vs. fix in the .md by hand.
4. `mkdocs serve` and click through every page; fix broken internal links
   surfaced by `mkdocs build --strict`.
5. **Refresh dates** in the converted content:
   - `docs/license.md`: bump the copyright span from "2009-2018" to
     "2009-2026" (license itself stays BSD-2-clause / "Simplified BSD" — same
     license as `LICENSE` at the repo root).
   - Scan for any other hardcoded year ranges in the converted pages and
     refresh to 2026 where they refer to "current" / "© up to now" rather
     than a specific historical event.
6. Commit `docs/`, `.htaccess`, and the conversion scripts.

### Phase C — polish (still pre-deploy)

1. Build the final `nav:` in `mkdocs.yml` by hand — wildcards in nav aren't
   real, they're a placeholder above. Group the ~50 example pages sensibly
   (routing / HA / VPN / DHCP / firewall / shaping / IPv6 / benchmarks /
   misc — same buckets the old landing page already uses).
2. Add a `docs/assets/css/extra.css` for any small visual nits (logo size,
   etc.).
3. Set up `mkdocs build --strict` in CI (GitHub Actions) so future content
   changes can't introduce broken links.

### Phase D — deploy cutover

1. Build: `mkdocs build` → `site/`.
2. On the bsdrp.net host:
   - Take a backup of the existing DokuWiki tree (already done — that's the
     `bsdrp.net.2026-05-25.23-07.tgz` archive).
   - Replace the Apache docroot contents with `site/` + the generated
     `.htaccess`.
   - Reload Apache.
3. Smoke-test a representative set of old URLs (one example, one French page,
   one media URL, the home alias `/bsdrp`) — each should land on the right
   new page with a `301`.

### Phase E — diagram modernization (ongoing, separate PRs)

1. Build an inventory of every PNG/GIF used (≈ 85 images).
2. Split into:
   - **Network diagrams** → candidates for Mermaid `graph` / `flowchart`.
   - **Benchmark graphs / screenshots** → keep as bitmap.
3. Convert diagrams one at a time, one PR per file. The MR template should
   show the old PNG next to the new Mermaid render so reviewers can confirm
   equivalence.

## 7. Risks and mitigations

| Risk                                                                                | Mitigation                                                                                                                              |
| ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Pandoc mis-renders a tricky DokuWiki construct in a long page                       | `convert.sh` is idempotent → fix script, re-run, re-diff. For truly hopeless cases, hand-edit and add the path to a `skip-regen` list.  |
| A DokuWiki URL we forgot to map returns 404                                         | Fallback rule at the end of `.htaccess`: `RewriteRule ^.*$ / [R=302,L]` (note: 302 not 301, so we can fix later without cache poisoning) |
| Internal link drift between conversion runs                                         | `mkdocs build --strict` in CI catches broken links before merge.                                                                        |
| Some PNGs live under namespaces we drop (`wiki/`, `playground/`) but are referenced | The post-processor logs unresolved image refs; we either copy the file or replace with text.                                            |
| Search-engine ranking loss across the cutover                                       | Every old URL returns 301 (permanent), which preserves ranking. The fallback rule above is the only place we use 302.                   |

## 7b. Branding (favicon + logo)

All branded artwork lives in `~/BSDRP/logos/` (outside this repo). Authoritative
source is the LibreOffice/OpenOffice Draw file `BSDRP.logo.odg`; the PNGs are
exports of it at fixed sizes.

| Source file                          | Dimensions / kind            | Role                                   |
| ------------------------------------ | ---------------------------- | -------------------------------------- |
| `~/BSDRP/logos/BSDRP.logo.odg`       | OpenDocument Drawing (vector) | Editable master — kept outside `docs/` |
| `~/BSDRP/logos/BSDRP.logo.png`       | 681 × 681 PNG                | High-res rendering                     |
| `~/BSDRP/logos/BSDRP.logo.256.png`   | 256 × 256 PNG                | Retina-ready header logo               |
| `~/BSDRP/logos/BSDRP.logo.128.png`   | 128 × 128 PNG                | Standard header logo                   |
| `~/BSDRP/logos/BSDRP.logo.114.png`   | 114 × 114 PNG                | Apple touch icon                       |
| `~/BSDRP/logos/BSDRP.logo.64.png`    | 64 × 64 PNG                  | Favicon (large)                        |
| `~/BSDRP/logos/BSDRP.logo.48.png`    | 48 × 48 PNG                  | Favicon (standard)                     |

Mapping into the site:

```
docs/assets/
├── favicon.ico                       (multi-resolution: 16+32+48+64, built from the 48/64 PNGs)
├── apple-touch-icon.png              (← BSDRP.logo.114.png, renamed)
└── images/
    ├── bsdrp-logo.png                (← BSDRP.logo.256.png, used by the theme)
    ├── bsdrp-logo@128.png            (← BSDRP.logo.128.png, kept for any in-content use)
    └── bsdrp-logo-source.png         (← BSDRP.logo.png 681×681, full-res download)
```

We keep the `.odg` source **out of `docs/`** so it doesn't end up in the
published site. It stays in `~/BSDRP/logos/` (already in the BSDRP source
repo). The conversion script copies the rendered PNGs into `docs/assets/`
each run, so a future re-export from the .odg only needs the PNGs to be
refreshed.

Wired into `mkdocs.yml` under the `theme:` block:

```yaml
theme:
  name: material
  logo: assets/images/bsdrp-logo.png        # 256×256 — material scales it down
  favicon: assets/favicon.ico
  # mkdocs-material picks up apple-touch-icon.png automatically if present
```

`favicon.ico` is rebuilt from the PNG exports so the .ico contains 16, 32, 48
and 64 px frames (browsers pick the right one). One-liner:

```sh
# requires ImageMagick (pkg install ImageMagick7)
convert ~/BSDRP/logos/BSDRP.logo.48.png ~/BSDRP/logos/BSDRP.logo.64.png \
        -define icon:auto-resize=16,32,48,64 \
        docs/assets/favicon.ico
```

Notes:

- The DokuWiki home page embeds the 128 px logo in the body via
  `{{:bsdrp.logo.128.png}}`. Once mkdocs-material renders the logo in the
  header, we drop that in-body image from `index.md` to avoid showing it
  twice.
- The old `bsdrp.net/favicon.ico` in the DokuWiki backup is ignored — the
  fresh one rebuilt from the .odg-derived PNGs is authoritative.
- The 681 × 681 master PNG is included as `bsdrp-logo-source.png` so anyone
  linking to the logo at full resolution still has a working URL.

## 8. Out of scope (for now)

- Page revision history from `data/attic/` — user explicitly said to discard.
- DokuWiki user accounts / ACLs — the new site is purely static.
- Comments / forum — there were none.
- French translations — dropped per user decision.

---

When you're ready, the next step is **Phase A**: install `mkdocs-material`, lay
down `mkdocs.yml`, and stub `docs/index.md` so `mkdocs serve` runs. Say the
word and I'll do it.
