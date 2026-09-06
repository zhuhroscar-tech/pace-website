# Pace Website — Build Deliverables (per execution metaprompt v2)

This document fulfills Deliverables 2–4 of `pace-website-build-metaprompt-v2.md`:
a rationale table, an AI-generated-look self-audit, and a functional verification log.

Site repo: `zhuhroscar-tech/pace-website`
Live URL: **https://zhuhroscar-tech.github.io/pace-website/**
Verified commit: `fc29751` (pushed and confirmed live)

---

## 1. Rationale Table

Every major section/CTA/claim, why it's there, and what it's grounded in.

| Element | What it is | Why it's here | Source / justification |
|---|---|---|---|
| Hero headline "Study sessions that adapt to how you actually focus" | H1 | Leads with mechanism + outcome in one sentence, no vague value-prop language | HN "Pain, Claim, Proof" pattern; Baymard/CXL guidance that visitors decide relevance in 3–5s — avoids the "Empowering students..." genericism the brief explicitly bans |
| Hero secondary line "It reads how your session is actually going... not a rigid 25-minute rule" | Subhead | States the actual mechanic (signal-driven pacing) instead of an abstract promise | Brief requirement: "reference an actual mechanic in the working prototype, not an abstract promise" |
| Primary CTA "Join the beta — free" (hero, pricing, final CTA, footer) | Button, repeated verbatim | One dominant CTA repeated at natural points rather than competing offers | Brief Section 2 (single conversion goal); YC/HN thread consensus that inconsistent CTA wording dilutes intent |
| Secondary CTA "Try the live demo" (hero) → anchors to `#demo` | Button | Gives visitors who aren't ready to hand over an email a lower-commitment next step, same page (no dead end) | Matches the ranked goal order in the brief: try demo (1) before waitlist (2) |
| Trust strip ("Session data stays on your device", "No diagnostic or medical claims — ever", etc.) | 4-item row under hero | Concrete, falsifiable claims instead of a vague "we care about privacy" banner | Direct brief constraint: "no vague 'we care about your privacy' filler"; landdding.com research on trust-copy specificity |
| Problem section ("Generic timers weren't built for how attention actually works") | Section | Names the actual failure mode (fixed intervals vs. real attention drift) instead of generic "students struggle to focus" | Competitor teardown: Flocus/Tiimo both lead with a named failure mode before their fix |
| Differentiation 3-card grid (Rigid timers / Pace / Clinical tools) | Section | Positions Pace explicitly between two alternatives, both to show real differentiation AND to preempt the "is this medical?" concern before FAQ | Brief hard constraint: frame as complement not replacement; also addresses Success Bar item (c) directly, before the visitor has to ask |
| Live interactive session simulator (`#demo`) | Functional widget (focused/drifting/fading toggle) | Real, working product proof a judge can click in under 10 seconds — not a static mock or video | Brief Section 5 requirement: "no login required to try the demo"; competitor pattern (Focusmate, Tiimo both let you experience the mechanic before signup) |
| "How it works" 3-step flow | Section | Mirrors the actual prototype flow (task → check-in → report), so it's not a disconnected illustration | Brief: "should visually/functionally connect to the live demo, not be a disconnected illustration" |
| Privacy detail grid (6 specific commitments) | Section | Each item is a specific, checkable claim (local-first storage, no camera, no ad-targeting) rather than a marketing phrase | Direct brief requirement + CXL Institute guidance on trust-copy specificity |
| Founder section (About + homepage teaser) | Section | Legitimate credibility signal for a solo student founder — names the real affiliation (WashU) and real upcoming role (Peer Coach) instead of manufacturing team/scale signals | User-confirmed decision (clarify response): include founder section publicly; explicitly framed as "no manufactured mythology" per brief tone constraint |
| Pricing page: "Free Beta" (current) + "Pro" (TBD, not built) | 2-card pricing | Honest current-state pricing instead of fake tiers/discounts; explicitly states Pro is "planned — not built yet" | Brief: "no fake pricing tiers"; user-confirmed decision: no real usage data yet, so pricing also avoids implying scale it doesn't have |
| Social proof: founder's-note / "We will / we won't" block instead of testimonials | Section (About page) | No real users yet (user-confirmed), so fabricating testimonials would violate the brief's explicit ban — this substitutes an equally credible but honest signal | User clarify response: "No real data yet — use founder's-note block"; brief: "do not fabricate any [testimonials]" |
| FAQ: medical, privacy, wearables, mobile, beta scope, cost, data export, who-for | 8 Q&As | Directly answers the skeptical questions a judge or attention-challenged student would actually ask, incl. the medical framing question first | Brief Section 3 requirement list, verbatim |
| Waitlist page: real mailto CTA ("Signup form is coming very soon") | Interim functional state | User confirmed (clarify): no Google Form URL ready yet, and explicitly chose "leave it visibly marked coming soon" over a broken iframe or a lower-fidelity interim form | User clarify response, this session; brief Section 0.3: "must degrade honestly ... never a silent no-op" |
| Contact email `huairui.z@wustl.edu` (footer, FAQ, waitlist) | Contact channel | Live-verified that the originally-used `hello@paceapp.dev` belongs to an unrelated third-party product (confirmed via `curl`/whois this session) — every mailto: link was dead | Direct functional-audit finding this session; user confirmed the replacement address |
| Feature detail pages (`/features/*.html`) | 4 sub-pages | Lets a visitor go deep on one mechanic (adaptive sessions, attention signals, real-time prompts, privacy) without bloating the homepage | Competitor pattern: Flocus/Tiimo use dedicated feature pages rather than one long homepage; keeps homepage scannable per Baymard length guidance |

---

## 2. AI-Generated-Look Self-Audit Note

Patterns explicitly avoided, and how:

- **No adjective-stacking or hype language.** Ran an automated scan for banned phrases (`empowering students`, `unlock your`, `seamless`, `cutting-edge`, `revolutionize`, `game-changing`, `harness the power`, `synergy`, `leverage`, `world-class`, `best-in-class`, `simple, powerful`) across all 10 served HTML pages. **Result: 0 matches.**
- **No emoji-as-icon feature lists.** All feature/trust/privacy items use real inline SVG icons, not emoji bullets (the one intentional emoji — 🎯/🌊/☕ in the interactive demo — is used as a functional state indicator inside the simulator, not decorative page furniture).
- **No identical repeated card layouts with no hierarchy.** The differentiation grid (3 cards) deliberately visually distinguishes the middle "Pace" card (border-highlighted, `is-pace` class) from the two comparison cards — not three visually identical boxes.
- **No centered-everything layout.** Body copy, problem section, differentiation, privacy grid, and steps are left-aligned in a constrained max-width; only the demo section head and pricing head are intentionally centered as a deliberate visual break, not the default.
- **Concrete over vague claims**, e.g.: "Session data stays on your device" (not "we value your privacy"); "No wearables, no camera, no medical framing" (not "cutting-edge technology"); pricing states literally "$0" / "TBD — Planned, not built yet" rather than a marketing wrapper.
- **No fabricated trust signals.** No fake user counts, no fake school logos, no fake testimonials anywhere — confirmed by grep for common fabrication patterns (percentages, "X students", "trusted by") returning no matches tied to unverified claims.

---

## 3. Functional Verification Log

All checks below were run against either the local build or the **live deployed URL** this session, with tool output as evidence (not narrated).

| Check | Method | Result |
|---|---|---|
| Every link/src across all served pages resolves | Automated Python audit (regex-parsed `href`/`src`, resolved paths + anchors) | **386/386 pass** (initial run found 1 failure — the placeholder iframe — now fixed; re-run confirms 386/386, 0 problems) |
| No leftover placeholder strings (`PASTE_GOOGLE_FORM_EMBED_URL_HERE`, dead email) in any served file | Automated grep across all `.html`/`.py`/`.css`/`.js` | **0 hits**, confirmed both locally and on the live URL |
| Live URL serves all pages | `curl`/`urllib` HTTP status check against `https://zhuhroscar-tech.github.io/pace-website/` for all 10 pages + 3 assets + robots/sitemap | **All 200** |
| Waitlist mailto CTA is live and correctly addressed | Fetched live `waitlist.html`, extracted `mailto:` targets | Both instances point to `huairui.z@wustl.edu`; old `hello@paceapp.dev` count = 0 |
| Interactive demo simulator is functionally live (not just styled) | Headless browser: clicked "Drifting" button via real DOM click, read back resulting DOM state | Ring, label, and response text all updated correctly (`Drifting` / `18:42` / correct nudge copy) — confirms JS event wiring works, not just CSS |
| FAQ accordion is functionally live | Headless browser: clicked first FAQ summary, read back `aria-expanded` + open class | `opened: True`, `aria-expanded: 'true'` — confirmed |
| Responsive at 375px (mobile) | Headless browser, CDP device emulation, screenshot | Renders correctly; hero content visible, no overflow (a real above-the-fold visibility bug was caught by a prior QA pass in this repo's history and fixed with a 1.2s CSS fallback + JS immediate-check — confirmed still working) |
| Responsive at 768px (tablet) | Headless browser, CDP device emulation, screenshot | Renders correctly, nav adapts, no broken layout |
| Responsive at 1280px (desktop) | Headless browser, CDP device emulation, screenshot | Renders correctly; waitlist "coming soon" block displays as intended |
| No banned generic/AI-sounding phrases in copy | Automated regex scan, 15 banned patterns, all served HTML | **0 matches** |
| GitHub Pages build status | `gh api repos/.../pages` + `.../pages/builds/latest` | `status: "built"` for commit `fc29751` (the commit containing both fixes) |
| Git state | `git log`, `git status --short` | Working tree clean after commit; `fc29751` pushed to `origin/main` and confirmed via `git push` output (`3bb61be..fc29751 main -> main`) |

---

## 4. Outstanding / Flagged Items (not blockers, explicitly carried forward)

- `[NEEDS REAL DATA]` — Testimonials/social proof section intentionally omitted per user confirmation (no real users yet). Revisit once real beta users exist.
- Waitlist Google Form embed is intentionally NOT live yet (user confirmed this session: "leave it visibly marked 'form coming soon'"). Swap-in point is documented directly in `build_pages.py` and `waitlist.html` source comments — when the real form exists, replace the `.waitlist-pending` block with the iframe per `~/Downloads/pace-google-form-setup.md`.
- Domain: site currently lives at the GitHub Pages subdomain only (`zhuhroscar-tech.github.io/pace-website`) — no custom domain configured. Not requested as part of this task; flag if a custom domain is wanted for the pitch.
