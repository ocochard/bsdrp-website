# BSDRP website - project notes for AI agent

This is the mkdocs-material site published at `bsdrp.net`. It is the
public documentation for the [BSD Router Project](https://github.com/ocochard/BSDRP).
This repository only holds the website; the BSDRP source distribution
itself lives in a separate repo (see "Companion repo" below).

## Repo layout

```
docs/                - mkdocs content (the source of truth)
  index.md           - homepage
  assets/            - favicon, logo, page images
  documentation/     - user guide, FAQ, technical-docs, examples
  community/         - mailing lists, how to contribute
mkdocs.yml           - site config + full nav (hand-curated)
.htaccess            - Apache 301 redirects from old DokuWiki URLs
site/                - mkdocs build output (gitignored)
```

The site was migrated from a DokuWiki backup in early 2026. The
DokuWiki backup, the conversion scripts, and the migration plan have
all been removed now that `docs/*.md` is the only source of truth.
Anyone curious about the historical migration can read it in git
history (look for the commits prefixed `Phase A`/`Phase B`).

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
- `docs/assets/favicon.ico` - multi-resolution favicon built with ImageMagick.
- `docs/assets/images/bsdrp-logo.png` - theme logo.

If the logo or favicon source files change in `~/BSDRP/logos/`, regenerate
the in-repo assets from there.

## mkdocs conventions in use

- **Relative `.md` links** - internal links use relative paths (e.g.
  `../examples/foo.md`). `mkdocs build --strict` validates them at build
  time; keep it clean.
- **Native mermaid via `pymdownx.superfences`** - *not* the
  `mkdocs-mermaid2` plugin. Mermaid diagrams use fenced ` ```mermaid `
  blocks.
- **Admonitions** - use `!!! note` / `!!! info "Important"` /
  `!!! warning` / `!!! tip`.
- **Kebab-case heading slugs** - mkdocs auto-generates kebab anchors.
  When linking to a heading, use the kebab-case form (e.g.
  `#firewall-impact`).

## Network diagram style

Lab network diagrams are mermaid flowcharts, not PNGs. When converting an
old PNG, rebuild the diagram from the page's router configs (the PNGs are
often out of date) and keep the PNG file. All diagrams share one look:

- **Nodes**: circles, `R2(("<b>R2</b><br/>FRR<br/>..."))`: bold name, then
  the routing suite or role, then at most a couple of short lines. Long
  daemon lists go in a Router/Role table under the diagram, and repetitive
  addressing goes in a sentence (e.g. "10.0.XY.0/24 has an IPv6 twin
  2001:db8:XY::/64").
- **Node colors**, by routing suite, copied verbatim into each diagram:

  ```
  classDef frr fill:#fde2c4,stroke:#d9480f,stroke-width:2px,color:#222
  classDef bird fill:#d0e4f7,stroke:#1c5fa8,stroke-width:2px,color:#222
  classDef router fill:#ffe3e3,stroke:#c92a2a,stroke-width:2px,color:#222
  classDef host fill:#e9ecef,stroke:#6c757d,stroke-width:2px,color:#222
  ```

  `router` is for any other routing/forwarding box (pimd, dnsmasq relay,
  static routes, firewall jails), `host` for end hosts and servers. Keep
  the explicit `color:#222` so the text stays readable in dark mode.
- **Link colors**, by protocol or role, via `linkStyle <index>` (indexes
  follow the order the links are declared): iBGP `#1c7ed6`, eBGP
  `#5f3dc4`, confederation eBGP `#9775fa`, OSPF `#15aabf`, RIP `#f59f00`,
  IS-IS `#2f9e44`, PIM `#d6336c`, DHCP `#f76707`, PPTP/tunnels `#0b7285`,
  plain LAN `#868e96`. Width 4px (3px for plain LANs, 5-6px for an
  emphasised link). Within a single diagram, distinct colors per tunnel
  type or per customer are fine when that is what the reader must tell
  apart.
- **Link labels**: start with the protocol or role in bold, then the
  subnet: `R2 ---|"<b>OSPF</b>, VRRP .254<br/>10.0.12.0/24"| R1`.
- **Containers**: a host holding jails is a subgraph styled
  `fill:#fff5f5,stroke:#e03131,stroke-width:2px,color:#222`; AS boxes
  `fill:#f8f9fa,stroke:#495057`, nested sub-AS
  `fill:#fff9db,stroke:#868e96,stroke-dasharray:5 5`.
- Overlays and tunnels go in a second diagram with dashed links (`-.-`)
  when drawing them on the physical view would clutter it.

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
