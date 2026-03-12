// LearnMate AI — script.js

// ── Sidebar Toggle ──────────────────────────────────────
function toggleSidebar() {
  document.getElementById('sidebar').classList.toggle('open');
}

// Close sidebar on outside click (mobile)
document.addEventListener('click', function(e) {
  const sidebar = document.getElementById('sidebar');
  const toggle = document.querySelector('.menu-toggle');
  if (sidebar && toggle && !sidebar.contains(e.target) && !toggle.contains(e.target)) {
    sidebar.classList.remove('open');
  }
});

// ── Animate Progress Bars on Load ──────────────────────
function animateProgressBars() {
  document.querySelectorAll('.pd-bar, .pi-bar').forEach(bar => {
    const target = bar.style.width;
    bar.style.width = '0%';
    setTimeout(() => {
      bar.style.transition = 'width 0.8s cubic-bezier(.4,0,.2,1)';
      bar.style.width = target;
    }, 200);
  });
}

// ── Animate stat counters ──────────────────────────────
function animateCounters() {
  document.querySelectorAll('.stat-value').forEach(el => {
    const raw = el.textContent.trim();
    const end = parseInt(raw);
    if (isNaN(end) || end === 0) return;
    let start = 0;
    const duration = 700;
    const step = Math.ceil(end / (duration / 16));
    const timer = setInterval(() => {
      start += step;
      if (start >= end) {
        el.textContent = end;
        clearInterval(timer);
      } else {
        el.textContent = start;
      }
    }, 16);
  });
}

// ── Card entrance animation ────────────────────────────
function animateCards() {
  const cards = document.querySelectorAll(
    '.feature-card, .stat-card, .quiz-card, .rec-card, .progress-detail-card, .tl-card'
  );
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }, i * 60);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  cards.forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(16px)';
    card.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
    observer.observe(card);
  });
}

// ── Run on DOM ready ───────────────────────────────────
document.addEventListener('DOMContentLoaded', function () {
  animateProgressBars();
  animateCounters();
  animateCards();
});
