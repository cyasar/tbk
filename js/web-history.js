/* Progressive enhancement for Web History Timeline (Week 4) */
(() => {
  'use strict';

  function initWebHistory() {
    const root = document.querySelector('[data-web-history]');
    if (!root) return;

    const links = [...root.querySelectorAll('.history-link')];
    const panels = [...root.querySelectorAll('.history-event')];
    const rail = root.querySelector('.history-rail');
    const previous = root.querySelector('[data-web-prev]');
    const next = root.querySelector('[data-web-next]');
    const status = root.querySelector('[data-web-status]');
    let current = 0; // Begin at Tim Berners-Lee (1989)

    function select(index, { focus = false, scroll = true } = {}) {
      current = Math.max(0, Math.min(panels.length - 1, index));
      panels.forEach((panel, i) => { panel.hidden = i !== current; });
      links.forEach((link, i) => {
        if (i === current) link.setAttribute('aria-current', 'step');
        else link.removeAttribute('aria-current');
      });
      if (previous) previous.disabled = current === 0;
      if (next) next.disabled = current === panels.length - 1;
      if (status) {
        status.textContent = `${current + 1} / ${panels.length} · ${links[current].querySelector('.history-year').textContent}`;
      }
      if (scroll && rail) {
        const box = links[current].getBoundingClientRect();
        const viewport = rail.getBoundingClientRect();
        rail.scrollTo({
          left: rail.scrollLeft + box.left - viewport.left - (viewport.width - box.width) / 2,
          behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth'
        });
      }
      if (focus) links[current].focus({ preventScroll: true });
    }

    links.forEach((link, i) => link.addEventListener('click', event => {
      event.preventDefault();
      select(i);
    }));

    root.querySelectorAll('[data-web-jump]').forEach(button => {
      button.addEventListener('click', () => select(Number(button.dataset.webJump)));
    });

    if (previous) previous.addEventListener('click', () => select(current - 1));
    if (next) next.addEventListener('click', () => select(current + 1));

    root.addEventListener('keydown', event => {
      if (!event.target.closest('.history-rail, .history-jumps, .history-controls')) return;
      const actions = { ArrowRight: current + 1, ArrowLeft: current - 1, Home: 0, End: panels.length - 1 };
      if (Object.hasOwn(actions, event.key)) {
        event.preventDefault();
        event.stopPropagation();
        select(actions[event.key], { focus: true });
      }
    });

    function fromHash() {
      const index = panels.findIndex(panel => `#${panel.id}` === location.hash);
      if (index !== -1) select(index);
    }

    root.classList.add('enhanced');
    const jumps = root.querySelector('.history-jumps');
    const controls = root.querySelector('.history-controls');
    if (jumps) jumps.hidden = false;
    if (controls) controls.hidden = false;

    select(current, { scroll: false });
    fromHash();
    window.addEventListener('hashchange', fromHash);
    requestAnimationFrame(() => select(current));
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initWebHistory);
  } else {
    initWebHistory();
  }
})();
