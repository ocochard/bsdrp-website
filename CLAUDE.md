# BSDRP website — project notes for Claude

This is the mkdocs-material site published at `bsdrp.net`. It is the
public documentation for the [BSD Router Project](https://github.com/ocochard/BSDRP).
This repository only holds the website; the BSDRP source distribution
itself lives in a separate repo (see "Companion repo" below).

## Repo layout

```
docs/                — mkdocs content (the source of truth)
  index.md           — homepage
  assets/            — favicon, logo, page images
  documentation/     — user guide, FAQ, technical-docs, examples
  community/         — mailing lists, how to contribute
mkdocs.yml           — site config + full nav (hand-curated)
.htaccess            — Apache 301 redirects from old DokuWiki URLs
site/                — mkdocs build output (gitignored)
```

The site was migrated from a DokuWiki backup in early 2026 (see
`CONVERSION_PLAN.md` for the historical migration plan). The DokuWiki
backup and conversion scripts have been removed — `docs/*.md` is now
the only source of truth.

## Companion repo: `~/BSDRP`

The main project repository is at `~/BSDRP` (github.com/ocochard/BSDRP).
That repo builds the BSDRP firmware image and is the source of truth for
software versions, the kernel config, lab scripts, and so on.

**A Claude session running in either repo should be aware of the other**:

- Changes in `~/BSDRP` (a software bump, a new lab script, a feature)
  often warrant matching updates here (release notes, version mentions
  on the homepage, new pages under `docs/documentation/examples/`).
- Changes here (corrections to example labs, FAQ updates) sometimes
  reflect behavior changes that were made in `~/BSDRP` first.

**Workflow when working across both repos**: edit each repo on its own,
run `mkdocs build --strict` here after changes to verify links, and
commit and push each repo independently. Do not couple them with a
submodule; they have separate lifecycles.

The BSDRP repo's `AGENTS.md` (symlinked as `CLAUDE.md` there) has a
matching pointer back to this repo.

## Branding

Logo and favicon source files live in `~/BSDRP/logos/`. In this repo:
- `docs/assets/favicon.ico` — multi-resolution favicon built with ImageMagick.
- `docs/assets/images/bsdrp-logo.png` — theme logo.

If the logo or favicon source files change in `~/BSDRP/logos/`, regenerate
the in-repo assets from there.

## mkdocs conventions in use

- **Relative `.md` links** — internal links use relative paths (e.g.
  `../examples/foo.md`). `mkdocs build --strict` validates them at build
  time; keep it clean.
- **Native mermaid via `pymdownx.superfences`** — *not* the
  `mkdocs-mermaid2` plugin. Mermaid diagrams use fenced ` ```mermaid `
  blocks.
- **Admonitions** — use `!!! note` / `!!! info "Important"` /
  `!!! warning` / `!!! tip`.
- **Kebab-case heading slugs** — mkdocs auto-generates kebab anchors.
  When linking to a heading, use the kebab-case form (e.g.
  `#firewall-impact`).

## Copyediting rules

ASCII-clean prose, with these rules:

- **No em-dashes (—) or en-dashes (–)** in prose. Use `,` or `-`.
- **No non-breaking spaces** (U+00A0, U+202F, etc).
- **No unicode ellipsis** (…). Use ASCII `...`.
- **No unicode arrows** (→, ⇒). Use ASCII `->` if needed.
- **Curly double quotes** (`"` `"`) are normalised to ASCII `"`. This
  matters for license text and verbatim quotations.
- **Curly apostrophes** (`'` U+2019) are *preserved* as-is.
- **Hardware spec conventions**: `2.13 GHz` (space before unit),
  `8 GB`, `1.488 Mpps`. Adjective forms hyphenated: `quad-core`,
  `dual-port`. Project terms: `IPsec` (not `IPSec`), `AES-NI`,
  `GitHub`, `BSDRP`, `Gigabit Ethernet`.
- **FreeBSD identifiers** kept verbatim: `igb(4)`, `pf`, `ipfw`, `bhyve`,
  `netmap`, `pkt-gen`, `cxgbe`, `t5nex`, etc.

## Common operations

```sh
# Strict build (verifies all internal links and front-matter)
mkdocs build --strict

# Local preview
mkdocs serve
```

## Known stale content (tracked separately)

- A handful of hardware-reference pages contain dated dmesg dumps from
  FreeBSD 9-11.
- External links to `sourceforge.net`, `freecode.com`, and old DokuWiki
  manual pages may be dead. Not fixed during migration.
