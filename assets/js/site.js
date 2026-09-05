// ============== Pace — Shared Site JS ==============

document.addEventListener('DOMContentLoaded', () => {

  // Mobile nav toggle
  const menuToggle = document.querySelector('.menu-toggle');
  const mobileNav = document.querySelector('.mobile-nav');
  const mobileNavClose = document.querySelector('.mobile-nav-close');

  if (menuToggle && mobileNav) {
    menuToggle.addEventListener('click', () => {
      mobileNav.classList.add('open');
      menuToggle.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
    });
  }
  if (mobileNavClose && mobileNav) {
    mobileNavClose.addEventListener('click', () => {
      mobileNav.classList.remove('open');
      menuToggle?.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    });
  }
  // Close mobile nav on link click
  mobileNav?.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      mobileNav.classList.remove('open');
      document.body.style.overflow = '';
    });
  });

  // Desktop dropdown (keyboard accessible)
  const dropdown = document.querySelector('.nav-dropdown');
  const trigger = document.querySelector('.nav-dropdown-trigger');
  const menu = document.querySelector('.nav-dropdown-menu');
  if (dropdown && trigger && menu) {
    trigger.addEventListener('click', () => {
      const isOpen = menu.classList.toggle('open');
      trigger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
    document.addEventListener('click', (e) => {
      if (!dropdown.contains(e.target)) {
        menu.classList.remove('open');
        trigger.setAttribute('aria-expanded', 'false');
      }
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        menu.classList.remove('open');
        trigger.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // FAQ accordions (works across pages if .faq-list present)
  document.querySelectorAll('.faq-item').forEach(item => {
    const summary = item.querySelector('.faq-summary');
    summary?.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');
      // allow multiple open; if you want accordion-exclusive behavior, close siblings here
      item.classList.toggle('open', !isOpen);
      summary.setAttribute('aria-expanded', String(!isOpen));
    });
    summary?.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        summary.click();
      }
    });
  });

  // Scroll-reveal (restrained, respects reduced motion)
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!prefersReducedMotion && 'IntersectionObserver' in window) {
    const revealEls = document.querySelectorAll('[data-reveal]');
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(el => io.observe(el));
  } else {
    document.querySelectorAll('[data-reveal]').forEach(el => el.classList.add('is-visible'));
  }

  // Active nav link highlighting based on current path
  const currentPath = window.location.pathname.replace(/\/index\.html$/, '/');
  document.querySelectorAll('nav.header-nav a, .mobile-nav a').forEach(a => {
    try {
      const linkPath = new URL(a.href).pathname.replace(/\/index\.html$/, '/');
      if (linkPath === currentPath) a.setAttribute('aria-current', 'page');
    } catch (e) {}
  });
});
