# Pace Website

Marketing site for **Pace** — a privacy-first, adaptive study companion for college students, in beta.

Live: https://zhuhroscar-tech.github.io/pace-website/ (once GitHub Pages is enabled — see below)

## Structure

```
index.html                     Homepage (hero, demo, differentiation, trust, founder, pricing, CTA)
about.html                     Founder story + product approach
pricing.html                   Beta pricing + planned Pro tier
faq.html                       FAQ, including the medical-claims disclaimer
waitlist.html                  Waitlist signup (Google Form embed)
404.html                       Custom not-found page
features/
  adaptive-sessions.html
  attention-signals.html
  real-time-prompts.html
  privacy.html
assets/
  css/base.css                 Design system: tokens, layout, nav, buttons, footer
  css/components.css           Section-specific components (hero, simulator, FAQ, pricing, etc.)
  js/site.js                   Shared JS: mobile nav, dropdown, FAQ accordion, scroll-reveal
src/
  partials/header.html         Shared header (edit once, rebuild to propagate)
  partials/footer.html         Shared footer
build.py                       Templating engine — injects partials, fixes relative paths per page depth
build_features.py              Generates the 4 feature pages
build_pages.py                 Generates FAQ / Pricing / About / Waitlist
robots.txt / sitemap.xml       Basic SEO
```

## Editing content

1. Edit `src/partials/header.html` or `footer.html` for site-wide nav/footer changes.
2. Edit `build_features.py` / `build_pages.py` for page copy.
3. Run:
   ```bash
   python3 build_features.py
   python3 build_pages.py
   ```
4. `index.html` is currently hand-authored (not templated) — edit it directly.

## Before shipping: finish the waitlist form

`waitlist.html` has a placeholder `PASTE_GOOGLE_FORM_EMBED_URL_HERE` iframe src.
See `~/Downloads/pace-google-form-setup.md` for exact Google Form field setup,
then replace that placeholder with your form's real embed URL and rebuild
(`python3 build_pages.py`).

## Deploying to GitHub Pages

1. Push this repo to GitHub (already done if you're reading this from the repo).
2. In GitHub: **Settings → Pages → Source: Deploy from a branch → main / (root)**.
3. Site will be live at `https://<username>.github.io/pace-website/`.

## Design system

- Colors: deep forest green `#1E4A46` (primary), amber `#D98F2B` (accent)
- Fonts: Fraunces (headings), Inter (body)
- All copy avoids medical/diagnostic claims per product positioning constraints.
