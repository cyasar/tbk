/* Progressive enhancement: without JavaScript every event remains readable. */
(() => {
  const root = document.querySelector('[data-history]');
  if (!root) return;
  const links = [...root.querySelectorAll('.history-link')];
  const panels = [...root.querySelectorAll('.history-event')];
  const rail = root.querySelector('.history-rail');
  const previous = root.querySelector('[data-history-prev]');
  const next = root.querySelector('[data-history-next]');
  const status = root.querySelector('[data-history-status]');
  let current = 5; // Begin at the transistor revolution.
  function select(index, { focus = false, scroll = true } = {}) {
    current = Math.max(0, Math.min(panels.length - 1, index));
    panels.forEach((panel, i) => { panel.hidden = i !== current; });
    links.forEach((link, i) => {
      if (i === current) link.setAttribute('aria-current', 'step');
      else link.removeAttribute('aria-current');
    });
    previous.disabled = current === 0;
    next.disabled = current === panels.length - 1;
    status.textContent = `${current + 1} / ${panels.length} · ${links[current].querySelector('.history-year').textContent}`;
    if (scroll) {
      const box = links[current].getBoundingClientRect();
      const viewport = rail.getBoundingClientRect();
      rail.scrollTo({ left: rail.scrollLeft + box.left - viewport.left - (viewport.width - box.width) / 2,
        behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' });
    }
    if (focus) links[current].focus({ preventScroll: true });
  }
  links.forEach((link, i) => link.addEventListener('click', event => { event.preventDefault(); select(i); }));
  root.querySelectorAll('[data-history-jump]').forEach(button => button.addEventListener('click', () => select(Number(button.dataset.historyJump))));
  previous.addEventListener('click', () => select(current - 1));
  next.addEventListener('click', () => select(current + 1));
  // Keep timeline navigation local, including when it is a presentation slide.
  root.addEventListener('keydown', event => {
    if (!event.target.closest('.history-rail, .history-jumps, .history-controls')) return;
    const actions = { ArrowRight: current + 1, ArrowLeft: current - 1, Home: 0, End: panels.length - 1 };
    if (Object.hasOwn(actions, event.key)) { event.preventDefault(); event.stopPropagation(); select(actions[event.key], { focus: true }); }
  });
  function fromHash() {
    const index = panels.findIndex(panel => `#${panel.id}` === location.hash);
    if (index !== -1) select(index);
  }
  root.classList.add('enhanced');
  root.querySelector('.history-jumps').hidden = false;
  root.querySelector('.history-controls').hidden = false;
  select(current, { scroll: false });
  fromHash();
  window.addEventListener('hashchange', fromHash);
  // Scroll only the horizontal rail; never move the document on page load.
  requestAnimationFrame(() => select(current));
})();
