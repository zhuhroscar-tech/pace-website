#!/usr/bin/env python3
"""Generates all Pace website pages using build.py's build_page()."""
from build import build_page

# ============================================================
# FEATURE PAGE: Adaptive Sessions
# ============================================================
build_page(
    slug="features/adaptive-sessions.html",
    title="Adaptive Sessions — Pace",
    description="Pace adjusts your study session in real time based on how it's actually going, instead of forcing a fixed timer on every task.",
    depth=1,
    body_content="""
<main id="main">
  <section class="feature-hero wrap">
    <span class="eyebrow">Feature</span>
    <h1>Sessions that flex to how you're actually doing.</h1>
    <p class="lede">Most timers assume every study session behaves the same way. Pace assumes the opposite: your focus moves, so your session should too.</p>
    <div class="feature-nav-pills">
      <a class="feature-nav-pill" aria-current="page" href="adaptive-sessions.html">Adaptive sessions</a>
      <a class="feature-nav-pill" href="attention-signals.html">Attention signals</a>
      <a class="feature-nav-pill" href="real-time-prompts.html">Real-time prompts</a>
      <a class="feature-nav-pill" href="privacy.html">Privacy-first design</a>
    </div>
  </section>

  <section class="wrap section-border">
    <div class="detail-block" data-reveal="0">
      <div class="detail-visual"><span style="font-size:64px;">⏱️</span></div>
      <div class="detail-text">
        <h3>Start with an estimate, not a rule</h3>
        <p>Add a task and roughly how long you think it'll take. Pace uses that as a starting point — not a countdown you have to obey. If you're deep in flow at the 25-minute mark, Pace doesn't interrupt just because a timer says so.</p>
        <ul>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Flexible session length based on real progress</li>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>No forced breaks mid-flow</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="wrap section-border">
    <div class="detail-block reverse" data-reveal="0">
      <div class="detail-visual"><span style="font-size:64px;">🔄</span></div>
      <div class="detail-text">
        <h3>Adjusts as the session unfolds</h3>
        <p>Rather than a single static plan, Pace treats a session as something that evolves. Your check-ins (see Attention Signals) feed back into pacing decisions — when to nudge, when to suggest a break, when to just stay quiet.</p>
        <ul>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Responsive pacing, not a fixed interval</li>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Built for real study sessions, not generic productivity blocks</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="wrap section-border">
    <div class="section-head center" data-reveal="0">
      <span class="eyebrow">See it in action</span>
      <h2>Try the live session simulator</h2>
      <p class="lede">The full interactive demo lives on the homepage.</p>
      <div style="margin-top:20px;"><a class="btn btn-primary" href="../index.html#demo">Try the demo</a></div>
    </div>
  </section>

  <section class="wrap">
    <div class="final-cta" data-reveal="0">
      <h2>Ready to try a session that adapts to you?</h2>
      <p>Free during beta. No credit card. Your data stays on your device.</p>
      <a class="btn btn-primary btn-lg" href="../waitlist.html">Join the beta</a>
    </div>
  </section>
</main>
""",
)

# ============================================================
# FEATURE PAGE: Attention Signals
# ============================================================
build_page(
    slug="features/attention-signals.html",
    title="Attention Signals — Pace",
    description="A simple, optional check-in you control — no wearables, no cameras, no passive tracking. You tell Pace how you're doing.",
    depth=1,
    body_content="""
<main id="main">
  <section class="feature-hero wrap">
    <span class="eyebrow">Feature</span>
    <h1>A signal you control. Never one that watches you.</h1>
    <p class="lede">Attention signals in Pace are a deliberate check-in, not passive surveillance. You decide when and how to share how a session is going.</p>
    <div class="feature-nav-pills">
      <a class="feature-nav-pill" href="adaptive-sessions.html">Adaptive sessions</a>
      <a class="feature-nav-pill" aria-current="page" href="attention-signals.html">Attention signals</a>
      <a class="feature-nav-pill" href="real-time-prompts.html">Real-time prompts</a>
      <a class="feature-nav-pill" href="privacy.html">Privacy-first design</a>
    </div>
  </section>

  <section class="wrap section-border">
    <div class="detail-block" data-reveal="0">
      <div class="detail-visual"><span style="font-size:64px;">👁️</span></div>
      <div class="detail-text">
        <h3>Three simple states, entirely optional</h3>
        <p>Focused, drifting, or fading — that's the entire vocabulary. No biometric scores, no hidden inference, no always-on tracking. You tap a button when you feel like it; Pace responds to what you tell it.</p>
        <ul>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>No wearables required</li>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>No camera or microphone access</li>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8l3 3 7-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Completely optional — skip check-ins entirely if you prefer</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="wrap section-border">
    <div class="detail-block reverse" data-reveal="0">
      <div class="detail-visual"><span style="font-size:64px;">🎚️</span></div>
      <div class="detail-text">
        <h3>Why self-reported, not sensor-driven</h3>
        <p>Fatigue and attention tools that rely on cameras or biometric sensors raise real privacy concerns and can feel invasive during something as personal as studying. Pace deliberately keeps the signal in your hands: honest, low-friction, and something you can trust because you're the one providing it.</p>
      </div>
    </div>
  </section>

  <section class="wrap">
    <div class="final-cta" data-reveal="0">
      <h2>Try checking in during a simulated session.</h2>
      <p>See exactly how Pace responds to each signal — no account needed.</p>
      <a class="btn btn-primary btn-lg" href="../index.html#demo">Try the demo</a>
    </div>
  </section>
</main>
""",
)

# ============================================================
# FEATURE PAGE: Real-Time Prompts
# ============================================================
build_page(
    slug="features/real-time-prompts.html",
    title="Real-Time Prompts — Pace",
    description="Gentle, context-aware nudges based on your signal — never nagging, never a wall of notifications.",
    depth=1,
    body_content="""
<main id="main">
  <section class="feature-hero wrap">
    <span class="eyebrow">Feature</span>
    <h1>Prompts that read the room, not a script.</h1>
    <p class="lede">Every prompt Pace shows is tied to your current signal. Focused sessions get silence. Drifting sessions get one gentle nudge. Fading sessions get a real break suggestion.</p>
    <div class="feature-nav-pills">
      <a class="feature-nav-pill" href="adaptive-sessions.html">Adaptive sessions</a>
      <a class="feature-nav-pill" href="attention-signals.html">Attention signals</a>
      <a class="feature-nav-pill" aria-current="page" href="real-time-prompts.html">Real-time prompts</a>
      <a class="feature-nav-pill" href="privacy.html">Privacy-first design</a>
    </div>
  </section>

  <section class="wrap section-border">
    <div class="detail-block" data-reveal="0">
      <div class="detail-visual"><span style="font-size:64px;">🎯</span></div>
      <div class="detail-text">
        <h3>In flow? Pace stays quiet.</h3>
        <p>The single most common failure mode of focus apps is interrupting someone who's actually doing fine. When your signal is "focused," Pace's default behavior is to do nothing — maybe a soft ambient track, nothing more.</p>
      </div>
    </div>
  </section>

  <section class="wrap section-border">
    <div class="detail-block reverse" data-reveal="0">
      <div class="detail-visual"><span style="font-size:64px;">🌊</span></div>
      <div class="detail-text">
        <h3>Drifting? One gentle nudge.</h3>
        <p>A single, specific prompt — like "what's one thing to focus on right now?" — designed to re-anchor attention without shame or urgency. Not a stream of notifications.</p>
      </div>
    </div>
  </section>

  <section class="wrap section-border">
    <div class="detail-block" data-reveal="0">
      <div class="detail-visual"><span style="font-size:64px;">☕</span></div>
      <div class="detail-text">
        <h3>Fading? A real break, not guilt.</h3>
        <p>Pushing through fatigue usually just produces worse work. When your signal is "fading," Pace suggests an actual break and reminds you when to come back — treating rest as part of the plan, not a failure of it.</p>
      </div>
    </div>
  </section>

  <section class="wrap">
    <div class="final-cta" data-reveal="0">
      <h2>Hear the difference for yourself.</h2>
      <p>Switch between focused, drifting, and fading in the live demo.</p>
      <a class="btn btn-primary btn-lg" href="../index.html#demo">Try the demo</a>
    </div>
  </section>
</main>
""",
)

# ============================================================
# FEATURE PAGE: Privacy
# ============================================================
build_page(
    slug="features/privacy.html",
    title="Privacy-First Design — Pace",
    description="Exactly what Pace collects, what stays local, and what we will never do with your study data.",
    depth=1,
    body_content="""
<main id="main">
  <section class="feature-hero wrap">
    <span class="eyebrow">Feature</span>
    <h1>Not a vibe. A specific set of commitments.</h1>
    <p class="lede">"Privacy-first" is an overused phrase. Here's exactly what it means for Pace, with no hand-waving.</p>
    <div class="feature-nav-pills">
      <a class="feature-nav-pill" href="adaptive-sessions.html">Adaptive sessions</a>
      <a class="feature-nav-pill" href="attention-signals.html">Attention signals</a>
      <a class="feature-nav-pill" href="real-time-prompts.html">Real-time prompts</a>
      <a class="feature-nav-pill" aria-current="page" href="privacy.html">Privacy-first design</a>
    </div>
  </section>

  <section class="wrap section-border">
    <div class="privacy-grid" data-reveal="0">
      <div class="privacy-item">
        <div class="privacy-icon"><svg viewBox="0 0 20 20" fill="none" width="20" height="20"><path d="M10 2L3 5v5c0 4.5 3 7.5 7 8.5 4-1 7-4 7-8.5V5l-7-3z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg></div>
        <div><h4>Local-first storage</h4><p>Session history, tasks, and reports are stored in your browser's local storage by default. Nothing is uploaded unless you explicitly choose to export or sync.</p></div>
      </div>
      <div class="privacy-item">
        <div class="privacy-icon"><svg viewBox="0 0 20 20" fill="none" width="20" height="20"><path d="M6 9V6a4 4 0 118 0v3M5 9h10v8H5V9z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg></div>
        <div><h4>No login for the demo</h4><p>The interactive demo runs entirely client-side. No account, no email, no data collection required to try it.</p></div>
      </div>
      <div class="privacy-item">
        <div class="privacy-icon"><svg viewBox="0 0 20 20" fill="none" width="20" height="20"><path d="M4 10h4l2-6 2 12 2-6h2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        <div><h4>No passive sensors</h4><p>Attention signals are self-reported check-ins. Pace does not use your camera, microphone, or any wearable device to infer focus.</p></div>
      </div>
      <div class="privacy-item">
        <div class="privacy-icon"><svg viewBox="0 0 20 20" fill="none" width="20" height="20"><path d="M4 6h12M4 10h12M4 14h8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></div>
        <div><h4>Never sold, never ad-targeted</h4><p>We do not sell study data, and we are not building an ad-supported product. Your study habits are not the business model.</p></div>
      </div>
      <div class="privacy-item">
        <div class="privacy-icon"><svg viewBox="0 0 20 20" fill="none" width="20" height="20"><path d="M10 3v14M4 10h12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></div>
        <div><h4>Not a medical device</h4><p>Pace does not diagnose, treat, or claim to manage ADHD or any other condition. It's a study-focus tool, not a substitute for clinical care.</p></div>
      </div>
      <div class="privacy-item">
        <div class="privacy-icon"><svg viewBox="0 0 20 20" fill="none" width="20" height="20"><path d="M10 2l7 3v5c0 4.5-3 7.5-7 8.5-4-1-7-4-7-8.5V5l7-3z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg></div>
        <div><h4>Transparent as we grow</h4><p>If a future paid tier introduces optional cloud sync, it will be opt-in, clearly explained, and never required to use Pace's core features.</p></div>
      </div>
    </div>
  </section>

  <section class="wrap">
    <div class="final-cta" data-reveal="0">
      <h2>Questions about how this works?</h2>
      <p>Check the FAQ, or reach out directly — we'll give you a straight answer.</p>
      <a class="btn btn-primary btn-lg" href="../faq.html">Read the FAQ</a>
    </div>
  </section>
</main>
""",
)

print("\nAll feature pages built successfully.")
