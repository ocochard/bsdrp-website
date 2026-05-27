# BSDRP website

Source for the [BSD Router Project](https://bsdrp.net) website, built
with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/).

The BSDRP firmware itself lives in a separate repository:
[github.com/ocochard/BSDRP](https://github.com/ocochard/BSDRP).

## Repo layout

- `docs/` - mkdocs content (Markdown sources, images, assets)
- `mkdocs.yml` - site configuration and navigation
- `.htaccess` - Apache 301 redirects from the previous DokuWiki URLs
- `site/` - build output (gitignored)

## Building

```sh
# Local preview at http://127.0.0.1:8000
mkdocs serve

# Strict build, verifies all internal links
mkdocs build --strict
```

## Contributing

Patches and pull requests are welcome. See
`docs/community/how-to-contribute.md` for guidelines, and `AGENTS.md` for
the copyediting and formatting conventions used across the site.

## License

Content is published under the same terms as the BSD Router Project.
