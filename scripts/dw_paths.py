"""dw_paths.py - canonical DokuWiki-id <-> MkDocs-path mapping.

A DokuWiki "id" looks like `documentation:examples:pf_and_carp_lab` (colon-
separated namespace components, underscores within a component, lowercase).

We map it to:
  - filesystem path inside docs/: `documentation/examples/pf-and-carp-lab.md`
  - public URL:                   `/documentation/examples/pf-and-carp-lab/`

The home page `bsdrp` is special-cased to `index.md` / `/`.
"""

from __future__ import annotations

import posixpath
from pathlib import Path
from typing import Iterator


# Namespaces dropped entirely (they still receive 301 redirects to "/").
DROP_NAMESPACES = ("fr", "wiki", "playground")


def dokuwiki_id_to_new_path(dw_id: str) -> str | None:
    """Return the docs/-relative path for a DokuWiki id, or None if dropped."""
    if any(dw_id == ns or dw_id.startswith(ns + ":") for ns in DROP_NAMESPACES):
        return None
    if dw_id == "bsdrp":
        return "index.md"
    parts = [_kebab(p) for p in dw_id.split(":")]
    return "/".join(parts) + ".md"


def dokuwiki_id_to_url(dw_id: str) -> str | None:
    """Return the absolute MkDocs URL for a DokuWiki id, or None if dropped."""
    if any(dw_id == ns or dw_id.startswith(ns + ":") for ns in DROP_NAMESPACES):
        return None
    if dw_id == "bsdrp":
        return "/"
    parts = [_kebab(p) for p in dw_id.split(":")]
    return "/" + "/".join(parts) + "/"


def dokuwiki_id_to_relative_md(src_dw_id: str, tgt_dw_id: str) -> str | None:
    """Return the relative .md link from src page to tgt page.

    Both ids are canonical DokuWiki ids. Returns None if the target is dropped.
    The result is suitable for use as a mkdocs-native link target, e.g.
    `../examples/foo.md`, which mkdocs validates at build time and renders to
    the correct public URL.
    """
    src_path = dokuwiki_id_to_new_path(src_dw_id)
    tgt_path = dokuwiki_id_to_new_path(tgt_dw_id)
    if src_path is None or tgt_path is None:
        return None
    src_dir = posixpath.dirname(src_path)
    rel = posixpath.relpath(tgt_path, src_dir or ".")
    return rel


def relative_asset_path(src_dw_id: str, asset_rel: str) -> str:
    """Return the relative path from src page to assets/images/<asset_rel>.

    `asset_rel` is the path under assets/images/ (e.g. `documentation/foo.png`).
    """
    src_path = dokuwiki_id_to_new_path(src_dw_id)
    if src_path is None:
        return "/assets/images/" + asset_rel
    src_dir = posixpath.dirname(src_path)
    tgt = "assets/images/" + asset_rel
    return posixpath.relpath(tgt, src_dir or ".")


def dokuwiki_id_to_old_url(dw_id: str) -> str:
    """Return the URL DokuWiki used to serve a page id at."""
    if dw_id == "bsdrp":
        return "/"
    return "/" + "/".join(dw_id.split(":"))


def iter_source_pages(pages_root: Path) -> Iterator[tuple[Path, str]]:
    """Yield (path, dokuwiki_id) for every .txt under pages_root."""
    for p in sorted(pages_root.rglob("*.txt")):
        rel = p.relative_to(pages_root)
        parts = list(rel.with_suffix("").parts)
        # DokuWiki id components are lowercase; underscores are preserved.
        dw_id = ":".join(parts).lower()
        yield p, dw_id


def _kebab(s: str) -> str:
    """component-name -> kebab-case (underscores -> hyphens, lowercase).

    DokuWiki's `cleanID` replaces apostrophes with underscores (e.g.
    `OpenVPN's` -> `openvpn_s`), so we treat `'` like `_`. Dots, commas, and
    parens are dropped entirely so we don't end up with paths like
    "/foo/setting-up-a-vpn-etc...-bench/".
    """
    s = s.lower()
    # Apostrophes act as separators in DokuWiki ids, not as dropped chars.
    s = s.replace("'", "_")
    s = s.replace("_", "-")
    import re as _re
    # Drop characters that aren't safe in URL slugs.
    s = _re.sub(r"[.,()\"!?;:]+", "", s)
    s = _re.sub(r"-+", "-", s).strip("-")
    return s
