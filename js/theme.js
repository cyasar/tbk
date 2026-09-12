/* Runs before paint. Storage may be unavailable in private browsing. */
(() => {
  let theme;
  try { theme = localStorage.getItem('tbk-theme-v2'); } catch {}
  document.documentElement.dataset.theme = ['dark', 'light'].includes(theme) ? theme : 'light';
  document.addEventListener('DOMContentLoaded', () => {
    const button = document.querySelector('.theme-toggle');
    const update = () => { const dark = document.documentElement.dataset.theme === 'dark'; button.textContent = dark ? '☀' : '☾'; button.setAttribute('aria-label', dark ? 'Açık temaya geç' : 'Koyu temaya geç'); };
    button?.addEventListener('click', () => { const theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark'; document.documentElement.dataset.theme = theme; try { localStorage.setItem('tbk-theme-v2', theme); } catch {} update(); });
    if (button) update();
  });
})();
