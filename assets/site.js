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
