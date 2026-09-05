#!/usr/bin/env python3
"""
Static site builder for Pace website.
Injects shared header/footer partials into page bodies, adjusts
relative asset/link paths based on page depth, and writes final
static HTML files (no server-side templating needed — GitHub Pages
just serves the output as-is).

Usage: python3 build.py
Reads:  src/pages/*.html  (page-specific <head> extras + <body> content)
Writes: root-level *.html and features/*.html
"""
import re
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).parent
HEADER = (ROOT / "src/partials/header.html").read_text()
FOOTER = (ROOT / "src/partials/footer.html").read_text()

PAGE_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='22' fill='%231E4A46'/%3E%3Crect x='24' y='60' width='10' height='20' rx='2' fill='%23D98F2B'/%3E%3Crect x='40' y='42' width='10' height='38' rx='2' fill='%23EAE8E0'/%3E%3Crect x='56' y='54' width='10' height='26' rx='2' fill='%23D98F2B'/%3E%3Crect x='72' y='30' width='10' height='50' rx='2' fill='%23EAE8E0'/%3E%3C/svg%3E">
<link rel="stylesheet" href="{prefix}assets/css/base.css">
<link rel="stylesheet" href="{prefix}assets/css/components.css">
{extra_head}
</head>
<body>
"""

PAGE_TAIL = """
</body>
</html>
"""

def adjust_paths(html: str, prefix: str) -> str:
    """Rewrite root-relative-style hrefs to work at any depth.
    Partials are authored assuming ROOT level (no prefix).
    For depth>0 pages, prefix asset/page links with '../' as needed,
    but leave sibling feature links (features/x.html) alone when the
    CURRENT page is itself inside features/ (they become relative siblings)."""
    if prefix == "":
        return html
    # Prefix root-level targets (with or without a #anchor suffix) with the depth prefix.
    # Matches href="assets/..." / href="pricing.html" / href="faq.html#medical" etc.
    root_level_names = ["pricing.html", "faq.html", "about.html", "waitlist.html", "index.html"]
    def repl(m):
        attr, val = m.group(1), m.group(2)
        if val.startswith("assets/"):
            return f'{attr}="{prefix}{val}"'
        head = val.split("#", 1)[0]
        if head in root_level_names:
            return f'{attr}="{prefix}{val}"'
        return m.group(0)
    html = re.sub(r'(href|src)="([^"]+)"', repl, html)
    # features/x.html -> sibling reference stays as-is *inside* features/,
    # but from root-level pages it's already correct. Since prefix != ""
    # only applies to pages inside features/, rewrite features/x.html to x.html
    html = re.sub(r'href="features/([a-zA-Z0-9_\-]+\.html)([^"]*)"', r'href="\1\2"', html)
    return html

def build_page(slug: str, title: str, description: str, body_content: str,
                extra_head: str = "", depth: int = 0, active_nav: Optional[str] = None):
    prefix = "../" * depth
    header = adjust_paths(HEADER, prefix)
    footer = adjust_paths(FOOTER, prefix)

    if active_nav:
        # mark the matching top-level nav link as current
        header = header.replace(f'href="{prefix}{active_nav}"', f'href="{prefix}{active_nav}" aria-current="page"', 1)

    html = PAGE_HEAD.format(title=title, description=description, prefix=prefix, extra_head=extra_head)
    html += header
    html += body_content
    html += footer
    html += PAGE_TAIL

    out_path = ROOT / slug
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html)
    print(f"Built: {slug} ({len(html)} bytes)")

if __name__ == "__main__":
    print("Import this module and call build_page(...) per page — see build_all.py")
