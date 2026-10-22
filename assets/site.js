const navToggle = document.querySelector('[data-nav-toggle]');
const siteNav = document.getElementById('site-navigation');
if (navToggle && siteNav) {
  const setMenuOpen = (open) => {
    navToggle.setAttribute('aria-expanded', String(open));
    navToggle.querySelector('[data-menu-label]').textContent = open ? 'Close' : 'Menu';
    siteNav.classList.toggle('is-open', open);
  };
  siteNav.dataset.collapsible = 'true';
  navToggle.hidden = false;
  navToggle.addEventListener('click', () => {
    setMenuOpen(navToggle.getAttribute('aria-expanded') !== 'true');
  });
  siteNav.addEventListener('click', (event) => {
    if (event.target.closest('a')) setMenuOpen(false);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && navToggle.getAttribute('aria-expanded') === 'true') {
      setMenuOpen(false);
      navToggle.focus();
    }
  });
  const mobileMenu = window.matchMedia('(max-width: 760px)');
  mobileMenu.addEventListener('change', () => setMenuOpen(false));
}

document.querySelectorAll('[data-abstract]').forEach(button => {
  const panel = document.getElementById(button.getAttribute('aria-controls'));
  if (!panel) return;
  panel.hidden = true;
  button.hidden = false;
  button.addEventListener('click', () => {
    panel.hidden = !panel.hidden;
    button.setAttribute('aria-expanded', String(!panel.hidden));
    button.querySelector('[data-sign]').textContent = panel.hidden ? '+' : '−';
  });
});
document.querySelectorAll('[data-print]').forEach(button => {
  button.hidden = false;
  button.addEventListener('click', () => window.print());
});
