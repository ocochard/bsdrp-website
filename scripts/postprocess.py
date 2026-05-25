#!/usr/bin/env python3.11
"""postprocess.py - convert DokuWiki pages to MkDocs markdown.

Strategy:
  1. Walk the DokuWiki pages tree, filtering namespaces we drop.
  2. For each .txt:
       a. Pre-clean DokuWiki text (strip {{description>}}, ~~NOTOC~~, etc.).
       b. Run pandoc -f dokuwiki -t gfm.
       c. Post-process the resulting markdown:
          - rewrite internal links to mkdocs paths
          - rewrite image refs to assets/images/...
          - turn 4-space indented code blocks into fenced ```
          - prepend YAML front-matter (title, description, hide_toc)
  3. Write to docs/<new path>.md.

The mapping from DokuWiki id to MkDocs URL/path is the single source of truth
for both the link rewriter and build_htaccess.py - it lives in dw_paths.py.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from dw_paths import (
    DROP_NAMESPACES,
    dokuwiki_id_to_new_path,
    dokuwiki_id_to_relative_md,
    dokuwiki_id_to_url,
    iter_source_pages,
    relative_asset_path,
)


# ---------------------------------------------------------------------------
# Pre-clean: strip / extract DokuWiki-specific syntax before handing to pandoc
# ---------------------------------------------------------------------------

DESC_RE = re.compile(r"\{\{description>([^}]*)\}\}")
NOTOC_RE = re.compile(r"~~NOTOC~~")
NOCACHE_RE = re.compile(r"~~NOCACHE~~")

# DokuWiki `[[target|label]]` link target containing parens confuses pandoc -
# it treats them as a markdown link title. Squash parens inside the target
# before pandoc sees the page.
DW_LINK_RE = re.compile(r"\[\[([^\]\|]+)(\|[^\]]+)?\]\]")


def pre_clean(text: str) -> tuple[str, dict]:
    """Return (cleaned text, metadata dict).

    Metadata keys: description (str|None), hide_toc (bool).
    """
    meta: dict = {"description": None, "hide_toc": False}

    m = DESC_RE.search(text)
    if m:
        meta["description"] = m.group(1).strip()
        text = DESC_RE.sub("", text)

    if NOTOC_RE.search(text):
        meta["hide_toc"] = True
        text = NOTOC_RE.sub("", text)

    text = NOCACHE_RE.sub("", text)

    # Replace parens inside DokuWiki link *targets* (pandoc otherwise parses
    # them as a markdown link "title"). Keep the contained text - DokuWiki
    # normalizes parens to underscores when computing the page id, so e.g.
    # `Setting up a VPN (IPSec, GRE, etc...) performance benchmark lab` and
    # `Setting up a VPN IPSec GRE etc performance benchmark lab` both resolve
    # to the same id once kebabified.
    def _scrub_target(m: re.Match[str]) -> str:
        target = m.group(1)
        rest = m.group(2) or ""
        target = target.replace("(", " ").replace(")", " ")
        # DokuWiki query-string-style separators - strip them, keeping any
        # trailing `#anchor`.
        target = re.sub(r"\?&?", "", target)
        target = re.sub(r"\s+", " ", target).strip()
        return f"[[{target}{rest}]]"
    text = DW_LINK_RE.sub(_scrub_target, text)

    return text, meta


# ---------------------------------------------------------------------------
# pandoc invocation
# ---------------------------------------------------------------------------


def run_pandoc(text: str) -> str:
    result = subprocess.run(
        ["pandoc", "-f", "dokuwiki", "-t", "gfm", "--wrap=none"],
        input=text,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


# ---------------------------------------------------------------------------
# Post-process: rewrite links, images, code fences
# ---------------------------------------------------------------------------

# Match markdown links: [label](target) - careful about escaped parens.
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
# Match markdown images: ![alt](target)
IMG_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
# Match an indented code block (lines starting with 4 spaces or a tab).
# We collapse runs of indented lines into a fenced block.
INDENT_CODE_LINE = re.compile(r"^(    |\t)(.*)$")


def is_external(url: str) -> bool:
    return url.startswith(("http://", "https://", "mailto:", "ftp://", "//"))


# Set of known top-level namespace segments - populated from the source tree
# at startup. Used to detect "relative" links that are actually absolute
# (e.g. `[[documentation/examples/foo]]` when DokuWiki has `useslash=1`).
_KNOWN_TOP_NS: set[str] = set()


def _is_namespaced_absolute(target: str) -> bool:
    """Heuristic: target starts with a known top-level namespace segment."""
    t = target.lstrip("/").lstrip(":")
    # split on either / or :
    seg = re.split(r"[/:]", t, maxsplit=1)[0].lower()
    return seg in _KNOWN_TOP_NS


def normalize_dw_link(target: str, current_ns: str = "") -> str:
    """Turn a pandoc-emitted DokuWiki link target into a clean DokuWiki id.

    Pandoc converts `[[ns:page]]` into a link to "/Ns/Page" (with original
    case, spaces preserved, leading slash sometimes there). DokuWiki has two
    flavors of internal link:
      - absolute (`[[:documentation:examples:foo]]`, with namespace) -> pandoc
        emits a leading "/"
      - relative (`[[foo]]` or `[[setting_up_..._lab]]` from a page already in
        ns documentation:examples) -> pandoc emits just "foo" with no slash.

    We canonicalize to a DokuWiki id (colon-separated, lowercase, underscores
    inside components):
      - if the target had a leading "/" -> absolute id (strip the slash)
      - otherwise -> resolve against current_ns
    """
    t = target
    frag = ""
    if "#" in t:
        t, frag = t.split("#", 1)
        frag = "#" + frag

    if t.startswith("/") or t.startswith(":"):
        t = t.lstrip("/").lstrip(":")
        absolute = True
    elif _is_namespaced_absolute(t):
        # `documentation/examples/foo` or `documentation:examples:foo` with no
        # leading separator - DokuWiki with useslash treats these as absolute.
        absolute = True
    else:
        absolute = False

    t = t.replace("/", ":")
    t = t.replace(" ", "_")
    t = t.lower()

    if not absolute and current_ns:
        t = current_ns + ":" + t

    return t + frag


def _kebab_anchor(anchor: str) -> str:
    """Convert a DokuWiki-style snake_case anchor to mkdocs kebab-case.

    DokuWiki auto-generates heading anchors as snake_case (`firewall_impact`),
    mkdocs-material's toc extension uses kebab-case (`firewall-impact`).
    This is a best-effort transform; some legacy anchors won't resolve because
    the underlying heading was renamed or contains characters (like `(4)`)
    that the two slugifiers handle differently. Those orphan anchors degrade
    gracefully to "land at page top".
    """
    return anchor.replace("_", "-")


def rewrite_link(label: str, target: str, current_ns: str, src_dw_id: str) -> str:
    """Rewrite a single link. Returns the replacement markdown."""
    if is_external(target):
        return f"[{label}]({target})"

    # Anchor-only link (#section) - rewrite snake_case -> kebab-case so it
    # matches mkdocs' auto-generated heading slug.
    if target.startswith("#"):
        return f"[{label}](#{_kebab_anchor(target[1:])})"

    # Already-resolved relative .md link (e.g. produced by normalize_self_links
    # in an earlier pass) - leave it alone.
    base = target.split("#", 1)[0]
    if base.endswith(".md") or base.startswith("../") or base.startswith("./"):
        return f"[{label}]({target})"

    dw_id = normalize_dw_link(target, current_ns=current_ns)
    base, _, frag = dw_id.partition("#")
    new = dokuwiki_id_to_relative_md(src_dw_id, base)
    if new is None:
        # Unknown target - leave the original text but warn.
        print(f"  WARN: unresolved link [{label}]({target}) (ns={current_ns!r})", file=sys.stderr)
        return f"[{label}]({target})"
    if frag:
        new += "#" + _kebab_anchor(frag)
    return f"[{label}]({new})"


def rewrite_image(alt: str, target: str, current_ns: str, src_dw_id: str) -> str:
    """Rewrite an image. Returns the replacement markdown."""
    if is_external(target):
        return f"![{alt}]({target})"

    # Pandoc emits absolute paths ("/documentation/examples/foo.png") for
    # `{{ :ns:foo.png }}` and relative paths ("foo.png") for `{{ foo.png }}`.
    t = target
    if t.startswith("/"):
        t = t.lstrip("/")
    elif current_ns:
        # bare filename: lives in the source page's namespace.
        t = current_ns.replace(":", "/") + "/" + t
    new = relative_asset_path(src_dw_id, t)
    return f"![{alt}]({new})"


def rewrite_links_and_images(md: str, current_ns: str, src_dw_id: str) -> str:
    # Images first (they share syntax with links but are prefixed with `!`).
    md = IMG_RE.sub(
        lambda m: rewrite_image(m.group(1), m.group(2), current_ns, src_dw_id),
        md,
    )

    # Then plain links. We have to be careful not to re-match image syntax
    # (which we just rewrote and may now contain `]`). LINK_RE doesn't match
    # the `!` prefix because it doesn't include it in the pattern, but our
    # already-rewritten image strings start with `!` so a fresh LINK_RE
    # scan would re-match them. Guard with a negative lookbehind via a
    # custom function.
    out = []
    last = 0
    for m in LINK_RE.finditer(md):
        if m.start() > 0 and md[m.start() - 1] == "!":
            continue
        out.append(md[last:m.start()])
        out.append(rewrite_link(m.group(1), m.group(2), current_ns, src_dw_id))
        last = m.end()
    out.append(md[last:])
    return "".join(out)


_LIST_LINE = re.compile(r"^\s*([-*]|\d+\.)\s")


def fix_indented_code(md: str) -> str:
    """Convert runs of 4-space-indented lines into ``` fenced blocks.

    Skips runs whose first indented line looks like a list item (e.g. a `*`
    bullet that GFM would render as continuation, not as code).
    """
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        prev_blank = (i == 0) or (lines[i - 1].strip() == "")
        m = INDENT_CODE_LINE.match(line)
        if prev_blank and m and not _LIST_LINE.match(m.group(2)):
            block = []
            while i < n and (
                INDENT_CODE_LINE.match(lines[i]) or lines[i].strip() == ""
            ):
                mm = INDENT_CODE_LINE.match(lines[i])
                if mm:
                    block.append(mm.group(2))
                else:
                    j = i + 1
                    while j < n and lines[j].strip() == "":
                        j += 1
                    if j < n and INDENT_CODE_LINE.match(lines[j]):
                        block.append("")
                        i = j
                        continue
                    else:
                        break
                i += 1
            while block and block[-1] == "":
                block.pop()
            if block:
                out.append("```")
                out.extend(block)
                out.append("```")
            continue
        out.append(line)
        i += 1
    return "\n".join(out) + ("\n" if md.endswith("\n") else "")


_DW_LEFTOVER_RE = re.compile(r"\[\[([^\]\|]+)(?:\|([^\]]+))?\]\]")


def fix_leftover_dw_links(md: str, current_ns: str, src_dw_id: str) -> str:
    """Convert any surviving `[[target|label]]` or `[[target]]` to markdown."""
    def sub(m: re.Match[str]) -> str:
        target = m.group(1).strip()
        label = (m.group(2) or target).strip()
        if is_external(target):
            return f"[{label}]({target})"
        dw_id = normalize_dw_link(target, current_ns=current_ns)
        base, _, frag = dw_id.partition("#")
        new = dokuwiki_id_to_relative_md(src_dw_id, base)
        if new is None:
            print(f"  WARN: unresolved [[{target}|{label}]] (ns={current_ns!r})",
                  file=sys.stderr)
            return f"[{label}]({target})"
        if frag:
            new += "#" + _kebab_anchor(frag)
        return f"[{label}]({new})"
    return _DW_LEFTOVER_RE.sub(sub, md)


_SELF_URL_RE = re.compile(r"(https?://bsdrp\.net)(/[^\s)\"]*?)(?=[\s)\"'<]|$)")


def normalize_self_links(md: str, src_dw_id: str) -> str:
    """Rewrite `https?://bsdrp.net/foo` -> relative `.md` link via the canonical
    DokuWiki id mapping so slug rules stay consistent and mkdocs can validate."""
    def sub(m: re.Match[str]) -> str:
        path = m.group(2)
        frag = ""
        if "#" in path:
            path, frag = path.split("#", 1)
            frag = "#" + frag
        dw_id = path.lstrip("/").rstrip("/").replace("/", ":").lower()
        new = dokuwiki_id_to_relative_md(src_dw_id, dw_id)
        if new is None:
            return m.group(0)  # leave it alone
        if frag:
            new += "#" + _kebab_anchor(frag)
        return new
    return _SELF_URL_RE.sub(sub, md)


# Pandoc emits DokuWiki `<note ...>...</note>` as escaped literals:
#   `\<note warning\> body \</note\>`
# Match both escaped and bare forms and convert to mkdocs-material admonitions.
_NOTE_RE = re.compile(
    r"\\?<note(?:\s+(important|warning|tip))?\s*\\?>"  # opening
    r"(.*?)"                                            # body (non-greedy)
    r"\\?</note\\?>",                                   # closing
    re.DOTALL | re.IGNORECASE,
)
_NOTE_KIND = {
    None: ("note", None),
    "important": ("info", "Important"),
    "warning": ("warning", None),
    "tip": ("tip", None),
}


def convert_notes(md: str) -> str:
    """Convert DokuWiki <note> blocks to mkdocs-material admonitions."""
    def sub(m: re.Match[str]) -> str:
        kind = (m.group(1) or "").lower() or None
        body = m.group(2).strip()
        admon, title = _NOTE_KIND.get(kind, ("note", None))
        header = f"!!! {admon}"
        if title:
            header += f' "{title}"'
        # Indent each body line by 4 spaces; preserve blank lines.
        indented = "\n".join(
            ("    " + line) if line.strip() else ""
            for line in body.splitlines()
        )
        # Ensure a blank line before and after the admonition so it parses.
        return f"\n{header}\n{indented}\n"
    return _NOTE_RE.sub(sub, md)


def fix_bold_escapes(md: str) -> str:
    """pandoc emits `\*\*` for `**bold**` that appears at line start when the
    bold spans words containing punctuation. Unescape the simple case."""
    # Replace `\*` -> `*` everywhere - safe because real escape would already
    # be `\\*` after gfm escaping.
    return md.replace(r"\*", "*").replace(r"\_", "_")


def extract_title(md: str) -> tuple[str, str]:
    """Pull the first `# H1` out of the body, return (title, body_without_h1)."""
    lines = md.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            del lines[i]
            # also drop one blank line after the title if present
            if i < len(lines) and lines[i].strip() == "":
                del lines[i]
            return title, "\n".join(lines)
    return "", md


def drop_home_logo(md: str) -> str:
    """Drop the in-body BSDRP logo from the home page; the theme renders it."""
    # markdown image form
    md = re.sub(
        r"!?\[[^\]]*\]\([^)]*bsdrp\.logo\.128\.png\)\s*",
        "",
        md,
        flags=re.IGNORECASE,
    )
    # raw <img ... bsdrp.logo.128.png ... /> form (pandoc emits this for
    # `{{ :bsdrp.logo.128.png | alt }}` because of the alignment hint)
    md = re.sub(
        r"<img[^>]*bsdrp\.logo\.128\.png[^>]*/?>\s*",
        "",
        md,
        flags=re.IGNORECASE,
    )
    # leftover freebsd-foundation donor badge - drop the image-in-link wrapper,
    # keeping the link with a text label
    md = re.sub(
        r"\[\{\{freebsd-fundation-donor\.gif\\?\|([^}]+)\}\}\]\(([^)]+)\)",
        r"[\1](\2)",
        md,
        flags=re.IGNORECASE,
    )
    return md


def build_frontmatter(title: str, meta: dict) -> str:
    lines = ["---"]
    if title:
        lines.append(f"title: {yaml_quote(title)}")
    if meta.get("description"):
        lines.append(f"description: {yaml_quote(meta['description'])}")
    if meta.get("hide_toc"):
        lines.append("hide:")
        lines.append("  - toc")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def yaml_quote(s: str) -> str:
    """Minimal YAML scalar quoting - wrap in double quotes if needed."""
    if any(c in s for c in ":#\"'\n") or s.startswith(("- ", "[", "{", "&", "*", "!")):
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def convert_one(src: Path, dw_id: str, docs_dir: Path) -> None:
    rel_new = dokuwiki_id_to_new_path(dw_id)
    if rel_new is None:
        return
    dst = docs_dir / rel_new
    dst.parent.mkdir(parents=True, exist_ok=True)

    text = src.read_text(encoding="utf-8")
    text, meta = pre_clean(text)
    md = run_pandoc(text)
    md = fix_indented_code(md)
    md = convert_notes(md)
    md = fix_bold_escapes(md)
    md = normalize_self_links(md, src_dw_id=dw_id)

    # current_ns = the source page's namespace, e.g. "documentation:examples"
    current_ns = ":".join(dw_id.split(":")[:-1])
    md = fix_leftover_dw_links(md, current_ns, src_dw_id=dw_id)

    # Home page gets the redundant body logo dropped.
    if dw_id == "bsdrp":
        md = drop_home_logo(md)

    md = rewrite_links_and_images(md, current_ns=current_ns, src_dw_id=dw_id)

    title, body = extract_title(md)
    front = build_frontmatter(title, meta)
    out = front + body.lstrip("\n")
    if not out.endswith("\n"):
        out += "\n"
    dst.write_text(out, encoding="utf-8")


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--pages", required=True, type=Path)
    p.add_argument("--docs", required=True, type=Path)
    args = p.parse_args(argv)

    # Discover top-level namespaces from the source tree so we can detect
    # `[[documentation/examples/foo]]`-style absolute links that look relative.
    for entry in args.pages.iterdir():
        if entry.is_dir():
            _KNOWN_TOP_NS.add(entry.name.lower())

    n_kept = 0
    n_skipped = 0
    for src, dw_id in iter_source_pages(args.pages):
        if any(dw_id == ns or dw_id.startswith(ns + ":") for ns in DROP_NAMESPACES):
            n_skipped += 1
            continue
        convert_one(src, dw_id, args.docs)
        n_kept += 1
    print(f"  converted {n_kept} pages, skipped {n_skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
