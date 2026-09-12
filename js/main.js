/* Shared navigation, code copying and device-local learning progress. */
document.querySelectorAll('.code-wrap').forEach(wrapper => {
  const button = document.createElement('button'); button.className = 'copy'; button.textContent = 'Kopyala'; button.type = 'button'; wrapper.prepend(button);
  button.addEventListener('click', async () => { try { await navigator.clipboard.writeText(wrapper.querySelector('code').textContent); button.textContent = 'Kopyalandı ✓'; } catch { button.textContent = 'Metni seçip kopyalayın'; } setTimeout(() => button.textContent = 'Kopyala', 2200); });
});
const readProgress = () => { try { const value = JSON.parse(localStorage.getItem('tbk-progress') || '[]'); return Array.isArray(value) ? value.filter(n => Number.isInteger(n) && n >= 1 && n <= 14) : []; } catch { return []; } };
let completed = [...new Set(readProgress())];
function renderProgress() {
  document.querySelectorAll('[data-week]').forEach(card => { const label = card.querySelector('.card-status'); if (label) { label.textContent = completed.includes(Number(card.dataset.week)) ? 'Tamamlandı ✓' : '2 saat · Ders notları'; label.classList.toggle('completed-label', completed.includes(Number(card.dataset.week))); } });
  const count = document.querySelector('#completed-count'); if (count) count.textContent = `${completed.length} / 14 hafta`;
  const progress = document.querySelector('#course-progress'); if (progress) progress.value = completed.length;
  const button = document.querySelector('#mark-complete'); if (button) { const done = completed.includes(Number(document.body.dataset.week)); button.textContent = done ? 'Tamamlandı ✓ · Geri al' : 'Bu haftayı tamamladım'; button.setAttribute('aria-pressed', String(done)); }
}
document.querySelector('#mark-complete')?.addEventListener('click', () => { const week = Number(document.body.dataset.week); completed = completed.includes(week) ? completed.filter(n => n !== week) : [...completed, week]; try { localStorage.setItem('tbk-progress', JSON.stringify(completed)); } catch {} renderProgress(); });
renderProgress();
document.querySelectorAll('.week-card[aria-disabled="true"]').forEach(card => { card.querySelector('.card-status').textContent = 'Yakında · Ders planı'; card.querySelector('.card-bottom b').textContent = '◷'; });
let category = 'all';
function filterWeeks() { const query = (document.querySelector('#week-search')?.value || '').toLocaleLowerCase('tr'); let count = 0; document.querySelectorAll('.week-card').forEach(card => { const show = (category === 'all' || card.dataset.category === category) && card.textContent.toLocaleLowerCase('tr').includes(query); card.hidden = !show; if (show) count++; }); const empty = document.querySelector('#empty-results'); if (empty) empty.hidden = count !== 0; const status = document.querySelector('#filter-status'); if (status) status.textContent = `${count} hafta gösteriliyor`; }
document.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click', () => { category = button.dataset.filter; document.querySelectorAll('[data-filter]').forEach(b => b.setAttribute('aria-pressed', String(b === button))); filterWeeks(); }));
document.querySelector('#week-search')?.addEventListener('input', filterWeeks);

// Navigation remains visible without JavaScript; enhancement collapses it on mobile.
const menuButton = document.querySelector('.menu-toggle');
const menuLinks = document.querySelector('#primary-links');
if (menuButton && menuLinks) {
  document.documentElement.classList.add('nav-ready');
  menuButton.hidden = false;
  const closeMenu = () => { menuButton.setAttribute('aria-expanded', 'false'); menuLinks.classList.remove('is-open'); };
  menuButton.addEventListener('click', () => {
    const open = menuButton.getAttribute('aria-expanded') !== 'true';
    menuButton.setAttribute('aria-expanded', String(open));
    menuLinks.classList.toggle('is-open', open);
  });
  menuLinks.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') { closeMenu(); menuButton.focus(); }
  });
  document.addEventListener('click', event => { if (!event.target.closest('.nav-inner')) closeMenu(); });
}
const contents = document.querySelector('.toc-disclosure');
if (contents) {
  const mobile = matchMedia('(max-width: 760px)');
  const updateContents = () => { contents.open = !mobile.matches; };
  updateContents();
  mobile.addEventListener('change', updateContents);
}
