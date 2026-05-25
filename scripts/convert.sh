#!/bin/sh
# convert.sh - orchestrate the DokuWiki -> MkDocs conversion.
#
# Reads:   ~/bsdrp-dokuwiki/bsdrp.net/data/{pages,media}
# Writes:  docs/**/*.md, docs/assets/images/**, .htaccess
#
# Idempotent: re-running wipes the generated content under docs/ and rebuilds
# it. Hand-written files outside the converted tree (index.md, assets/) are
# preserved.

set -eu

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DW_ROOT="${DW_ROOT:-$HOME/bsdrp-dokuwiki/bsdrp.net/data}"
DW_PAGES="$DW_ROOT/pages"
DW_MEDIA="$DW_ROOT/media"

DOCS="$REPO_ROOT/docs"
ASSETS_IMG="$DOCS/assets/images"

if [ ! -d "$DW_PAGES" ]; then
    echo "ERROR: DokuWiki source not found at $DW_PAGES" >&2
    exit 1
fi

echo "==> Cleaning previously converted content"
# Remove only the converted tree; preserve hand-written index.md and assets/.
for d in community documentation; do
    rm -rf "$DOCS/$d"
done
for f in features.md downloads.md license.md contributors.md; do
    rm -f "$DOCS/$f"
done
# Wipe the converted images mirror (keeps the branding assets in
# assets/images/*.png and assets/favicon.ico).
rm -rf "$ASSETS_IMG/documentation" "$ASSETS_IMG/wiki"
rm -f "$ASSETS_IMG/freebsd-fundation-donor.gif" \
      "$ASSETS_IMG/lab_virtuel_v6only.png" \
      "$ASSETS_IMG/bsdrp-example-lab.png" \
      "$ASSETS_IMG/bsdrp.logo.128.png"

echo "==> Converting pages (pandoc + post-processor)"
python3.11 "$REPO_ROOT/scripts/postprocess.py" \
    --pages "$DW_PAGES" \
    --docs  "$DOCS"

echo "==> Copying media"
# Copy media tree except namespaces we drop (wiki/) and the
# "dont-panic" PNG, which is DokuWiki internal.
mkdir -p "$ASSETS_IMG"
( cd "$DW_MEDIA" && find . -type f \
    ! -path './wiki/*' \
    ! -name 'dont-panic*' \
    -print ) | while IFS= read -r rel; do
    src="$DW_MEDIA/${rel#./}"
    dst="$ASSETS_IMG/${rel#./}"
    mkdir -p "$(dirname "$dst")"
    cp "$src" "$dst"
done

echo "==> Generating .htaccess"
python3.11 "$REPO_ROOT/scripts/build_htaccess.py" \
    --pages "$DW_PAGES" \
    --out   "$REPO_ROOT/.htaccess"

echo "==> Done"
echo "    pages : $(find "$DOCS" -name '*.md' | wc -l | tr -d ' ')"
echo "    images: $(find "$ASSETS_IMG" -type f | wc -l | tr -d ' ')"
echo "    htaccess: $(wc -l < "$REPO_ROOT/.htaccess" | tr -d ' ') lines"
