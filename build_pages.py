#!/usr/bin/env python3
"""Generates FAQ, Pricing, About, and Waitlist pages."""
from build import build_page

# ============================================================
# FAQ PAGE
# ============================================================
faqs = [
    ("medical", "Is Pace a medical or therapeutic product?",
     "No. Pace is a study-focus tool. It does not diagnose, treat, or manage ADHD or any other condition, and it is not a substitute for medical or mental health care. If you're navigating attention challenges, please talk to a qualified professional — Pace is meant to complement good study habits, not replace clinical support."),
    ("privacy-data", "How does the privacy actually work?",
     "Session data — your tasks, check-ins, and reports — lives in your browser's local storage by default. Nothing is sent to a server unless you explicitly choose to export or sync it. There's no login required to try the demo. See the full breakdown on our <a href='features/privacy.html' style=\"text-decoration:underline;color:var(--accent);\">privacy page</a>."),
    ("wearables", "Do I need a wearable or camera for attention signals?",
     "No. Attention signals in Pace are a simple, optional check-in — you tap 'focused,' 'drifting,' or 'fading' yourself. There's no camera access, no microphone access, and no wearable integration. You're always in control of what you share."),
    ("mobile", "Can I use Pace on my phone?",
     "Pace is web-first and works in any modern browser on desktop or mobile. The experience is currently optimized for larger screens, but the core session flow is fully usable on a phone."),
    ("beta", "What's actually included in the beta right now?",
     "The full adaptive session flow: task setup, real-time prompts based on your check-ins, and an end-of-session report. Pro features like cross-device sync and smart scheduling are planned but not built yet — see <a href='pricing.html' style=\"text-decoration:underline;color:var(--accent);\">pricing</a> for details."),
    ("cost", "How much does Pace cost?",
     "Pace is completely free during the beta — no credit card required. We haven't finalized pricing for a future Pro tier; when we do, the current beta feature set will remain free."),
    ("data-export", "Can I export or delete my data?",
     "Yes. Because your data lives locally in your browser, you control it directly — clearing your browser storage removes it. We're building an explicit export/delete option into the app as part of the beta as well."),
    ("who-for", "Who is Pace actually built for?",
     "College students who find that generic timers and productivity apps don't match how their focus actually behaves during a study session — including students who experience ADHD or attention challenges, though Pace is designed to be useful for anyone who wants a more responsive way to study."),
]

faq_items_html = ""
for anchor, q, a in faqs:
    faq_items_html += f"""      <div class="faq-item" id="{anchor}">
        <div class="faq-summary" role="button" tabindex="0" aria-expanded="false">{q}</div>
        <div class="faq-answer"><p>{a}</p></div>
      </div>
"""

build_page(
    slug="faq.html",
    title="FAQ — Pace",
    description="Straight answers about privacy, pricing, the beta, and what Pace is (and isn't) — including our stance on medical claims.",
    depth=0,
    active_nav="faq.html",
    body_content=f"""
<main id="main">
  <section class="wrap" style="padding-top:56px;">
    <div class="section-head" data-reveal="0">
      <span class="eyebrow">FAQ</span>
      <h2>Straight answers, no hedging.</h2>
      <p class="lede">The questions we get asked most — including the ones about what Pace deliberately does <em>not</em> claim to do.</p>
    </div>
    <div class="faq-list" data-reveal="1">
{faq_items_html}    </div>
  </section>

  <section class="wrap">
    <div class="final-cta" data-reveal="0">
      <h2>Still have a question?</h2>
      <p>Reach out directly — a real person (the founder) will answer.</p>
      <a class="btn btn-primary btn-lg" href="mailto:huairui.z@wustl.edu">Email us</a>
    </div>
  </section>
</main>
""",
)

# ============================================================
# PRICING PAGE
# ============================================================
build_page(
    slug="pricing.html",
    title="Pricing — Pace",
    description="Pace is free during the beta. No credit card, no trial countdown. See what's included now and what's planned for a future Pro tier.",
    depth=0,
    active_nav="pricing.html",
    body_content="""
<main id="main">
  <section class="wrap" style="padding-top:56px;">
    <div class="section-head center" data-reveal="0">
      <span class="eyebrow">Pricing</span>
      <h2>Free in beta. Simple after that.</h2>
      <p class="lede">No credit card to start. No trial countdown creating artificial urgency. When a paid tier exists, everything in the current beta stays free.</p>
    </div>
    <div class="pricing-grid" data-reveal="1">
      <div class="price-card active">
        <div class="badge">Current</div>
        <h3>Free Beta</h3>
        <div class="price">$0</div>
        <div class="period">Free during beta</div>
        <ul>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Full adaptive session flow</li>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Real-time attention-based prompts</li>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>End-of-session reports</li>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Local-first data, no login required</li>
        </ul>
        <a class="btn btn-primary" href="waitlist.html">Join the beta</a>
      </div>
      <div class="price-card">
        <h3>Pro</h3>
        <div class="price">TBD</div>
        <div class="period">Planned — not built yet</div>
        <ul>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Smart scheduling across courses</li>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Cross-device sync (opt-in)</li>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Trend insights across sessions</li>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Everything in Free</li>
        </ul>
        <a class="btn btn-secondary" href="waitlist.html">Get notified</a>
      </div>
    </div>
  </section>

  <section class="wrap section-border">
    <div class="section-head" data-reveal="0">
      <span class="eyebrow">Why free right now</span>
      <h2>We're still learning what's actually useful.</h2>
      <p class="lede">Pace is a solo-founder project in active development. Charging before the product has proven its value to real students would put the cart before the horse. The beta is free so we can focus on getting the core experience right — not on billing infrastructure.</p>
    </div>
  </section>

  <section class="wrap">
    <div class="final-cta" data-reveal="0">
      <h2>Try it now — no payment info needed.</h2>
      <p>Join the beta and help shape what Pro should include.</p>
      <a class="btn btn-primary btn-lg" href="waitlist.html">Join the beta</a>
    </div>
  </section>
</main>
""",
)

# ============================================================
# ABOUT PAGE
# ============================================================
build_page(
    slug="about.html",
    title="About — Pace",
    description="Pace is built by a solo student founder at Washington University in St. Louis, in preparation for the Skandalaris Venture Competition.",
    depth=0,
    active_nav="about.html",
    body_content="""
<main id="main">
  <section class="wrap" style="padding-top:56px;">
    <div class="section-head" data-reveal="0">
      <span class="eyebrow">About</span>
      <h2>Why Pace exists.</h2>
      <p class="lede">A short, honest version of the story — no manufactured mythology, just what actually happened.</p>
    </div>
  </section>

  <section class="wrap section-border">
    <div class="founder-card" data-reveal="0">
      <div class="founder-avatar">O</div>
      <div>
        <div class="founder-name">Oscar Zhu</div>
        <div class="founder-role">Founder — Math &amp; Financial Engineering, Washington University in St. Louis</div>
        <p class="founder-bio">Pace started from a simple, recurring frustration: generic study timers never matched how focus actually feels session to session. Some days a fixed 25-minute Pomodoro works fine. Other days it interrupts real flow, or fails to catch a slow drift into distraction. That mismatch was the seed for Pace.</p>
        <p class="founder-bio">The product is being designed and built at WashU, with an eye toward the Skandalaris Venture Competition. Right now it's a solo effort — one person doing product, design, code, and support — which is also why the beta is intentionally simple: a small set of things done honestly, rather than a long feature list done half-way.</p>
        <span class="founder-fact">🦅 Fun fact: ex-Eagleland</span>
      </div>
    </div>
  </section>

  <section class="wrap section-border">
    <div class="section-head" data-reveal="0">
      <span class="eyebrow">Our approach</span>
      <h2>What we will and won't do.</h2>
    </div>
    <div class="diff-grid">
      <div class="diff-card is-pace" data-reveal="1">
        <div class="diff-label">We will</div>
        <h4>Build honestly, in public</h4>
        <ul>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Keep session data local by default</li>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Be upfront about what's built vs. planned</li>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Listen to real student feedback before adding features</li>
        </ul>
      </div>
      <div class="diff-card" data-reveal="2">
        <div class="diff-label">We won't</div>
        <h4>Overclaim or misrepresent</h4>
        <ul>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Claim to diagnose or treat any condition</li>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Fabricate testimonials or user numbers</li>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Sell or advertise against your study data</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="wrap">
    <div class="final-cta" data-reveal="0">
      <h2>Want to help shape Pace?</h2>
      <p>Join the beta, or just say hi — early feedback directly shapes what gets built next.</p>
      <a class="btn btn-primary btn-lg" href="waitlist.html">Join the beta</a>
    </div>
  </section>
</main>
""",
)

# ============================================================
# WAITLIST PAGE
# ============================================================
build_page(
    slug="waitlist.html",
    title="Join the Beta — Pace",
    description="Join the Pace beta waitlist by email — free, no credit card, takes about 30 seconds.",
    depth=0,
    active_nav="waitlist.html",
    body_content="""
<main id="main">
  <section class="wrap" style="padding-top:56px;">
    <div class="section-head center" data-reveal="0">
      <span class="eyebrow">Join the beta</span>
      <h2>Free during beta. Takes about 30 seconds.</h2>
      <p class="lede">Email us from this page and we'll reach out with access details and updates. No spam, no credit card, unsubscribe anytime.</p>
    </div>

    <div class="waitlist-block" data-reveal="1">
      <div class="waitlist-form-wrap">
        <!--
          WAITLIST FORM STATUS: intentionally not embedded yet.
          Rationale: an iframe pointed at a placeholder URL is a
          broken/dead element, which the build standard here treats as
          worse than an honest "not live yet" state. Swap this block
          for a real signup form the moment one exists, and keep the
          fallback email path visible for users who do not want to use
          an embedded third-party form.
        -->
        <div class="waitlist-pending" role="status">
          <div class="waitlist-pending-icon" aria-hidden="true">
            <svg viewBox="0 0 20 20" fill="none" width="22" height="22"><path d="M10 2L3 5v5c0 4.5 3 7.5 7 8.5 4-1 7-4 7-8.5V5l-7-3z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
          </div>
          <h3>Signup form is coming very soon</h3>
          <p>We're finalizing the beta signup form right now. In the meantime, email us directly and we'll add you to the list by hand &mdash; same result, one extra step.</p>
          <a class="btn btn-primary" href="mailto:huairui.z@wustl.edu?subject=Pace%20beta%20waitlist">Email to join the waitlist</a>
        </div>
        <p style="font-size:12.5px;color:var(--text-faint);margin-top:16px;">
          Prefer not to email? Check back soon &mdash; a live signup form will replace this notice as soon as it's ready.
        </p>
      </div>
    </div>
  </section>

  <section class="wrap section-border">
    <div class="section-head" data-reveal="0">
      <span class="eyebrow">What happens next</span>
      <h2>No surprises.</h2>
    </div>
    <div class="steps">
      <div class="step" data-reveal="1">
        <div class="step-num">1</div>
        <h4>You send the waitlist email</h4>
        <p>A short email is enough; include your school if you want student-specific updates.</p>
      </div>
      <div class="step" data-reveal="2">
        <div class="step-num">2</div>
        <h4>We follow up by email</h4>
        <p>You'll hear back directly from the founder with access details and next steps.</p>
      </div>
      <div class="step" data-reveal="3">
        <div class="step-num">3</div>
        <h4>You start a free beta session</h4>
        <p>No credit card, no trial countdown — just the current beta feature set.</p>
      </div>
    </div>
  </section>
</main>
""",
)

print("\nAll pages (FAQ, Pricing, About, Waitlist) built successfully.")
