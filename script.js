// Basit, güvenli ve okunaklı script
document.addEventListener('DOMContentLoaded', () => {
  // Mobile menu toggle
  const mobileToggle = document.getElementById('mobile-toggle');
  const mainNav = document.getElementById('main-nav');

  mobileToggle.addEventListener('click', () => {
    mainNav.classList.toggle('active');
    mobileToggle.setAttribute('aria-expanded', mainNav.classList.contains('active'));
  });

  // Site info close / reopen behavior
  const siteInfo = document.getElementById('site-info');
  const closeSiteInfo = document.getElementById('close-site-info');
  const reopenArrow = document.getElementById('reopen-arrow');

  closeSiteInfo.addEventListener('click', () => {
    siteInfo.style.display = 'none';
    reopenArrow.style.display = 'block';
  });

  reopenArrow.addEventListener('click', () => {
    siteInfo.style.display = 'flex';
    reopenArrow.style.display = 'none';
  });

  // Close mobile nav when clicking a link (better UX)
  mainNav.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      if (mainNav.classList.contains('active')) {
        mainNav.classList.remove('active');
      }
    });
  });

  // Accessibility: close mobile nav by pressing Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      if (mainNav.classList.contains('active')) mainNav.classList.remove('active');
      if (siteInfo && siteInfo.style.display === 'flex') { /* no-op */ }
    }
  });
});
