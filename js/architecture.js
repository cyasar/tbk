/* The data journey is an instructional simulation, not connected to hardware. */
(() => {
  const root = document.querySelector('[data-architecture]');
  if (!root) return;
  const tabs = [...root.querySelectorAll('[data-architecture-tab]')];
  const panels = [...root.querySelectorAll('[data-architecture-panel]')];
  const inspector = root.querySelector('[data-architecture-inspector]');
  function selectTab(name, focus = false) {
    tabs.forEach(tab => { const active = tab.dataset.architectureTab === name; tab.setAttribute('aria-selected', String(active)); tab.tabIndex = active ? 0 : -1; if (active && focus) tab.focus(); });
    panels.forEach(panel => { panel.hidden = panel.dataset.architecturePanel !== name; });
  }
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => selectTab(tab.dataset.architectureTab));
    tab.addEventListener('keydown', event => {
      if (!['ArrowLeft','ArrowRight','Home','End'].includes(event.key)) return;
      event.preventDefault(); event.stopPropagation();
      const next = event.key === 'Home' ? 0 : event.key === 'End' ? tabs.length - 1 : (index + (event.key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length;
      selectTab(tabs[next].dataset.architectureTab, true);
    });
  });
  root.querySelectorAll('[data-architecture-node]').forEach(node => node.addEventListener('click', () => {
    root.querySelectorAll('[data-architecture-node]').forEach(item => item.setAttribute('aria-pressed', String(item === node)));
    inspector.querySelector('[data-architecture-title]').textContent = node.dataset.title;
    inspector.querySelector('[data-architecture-english]').textContent = node.dataset.english;
    inspector.querySelector('[data-architecture-description]').textContent = node.dataset.description;
  }));
  selectTab('general');
  const journey = [
    ['Sensör · Sensor', 'Sensör ortam sıcaklığını algılar. Örnekte fiziksel büyüklük 24,0 °C’dir.', 'sensor'],
    ['ADC · Analog-to-Digital Converter', 'Analog sensör gerilimi örneklenir ve sayısal koda çevrilir. Dijital sensörde bu işlem sensörün içinde olabilir.', 'adc'],
    ['CPU / MCU · Processing', 'İşlemci ölçümü kalibrasyon kuralıyla işler ve belirlenen eşikle karşılaştırır.', 'processor'],
    ['RAM · Working Memory', 'Anlık değer ve ara hesaplar çalışma belleğinde tutulur. Bu kopya enerji kesilince korunmaz.', 'ram'],
    ['Flash / SSD · Storage', 'Kayıt istenirse ölçüm zaman bilgisiyle kalıcı depolamaya yazılır. Her örneği kaydetmek zorunlu değildir.', 'flash'],
    ['Ekran / Aktüatör · Output', 'Değer ekranda gösterilir. Eşik aşılırsa uygun sürücü devresi üzerinden fan gibi bir aktüatör çalıştırılabilir.', 'actuator'],
  ];
  const steps = [...root.querySelectorAll('[data-journey-step]')];
  const controls = root.querySelector('.journey-controls');
  const previous = root.querySelector('[data-journey-prev]');
  const next = root.querySelector('[data-journey-next]');
  let current = -1;
  function render() {
    steps.forEach((step, index) => { step.classList.toggle('is-active', index === current); step.classList.toggle('is-complete', index < current); });
    root.querySelectorAll('.architecture-node').forEach(node => node.classList.toggle('flow-active', current >= 0 && node.dataset.architectureNode === journey[current][2]));
    previous.disabled = current <= 0;
    next.disabled = current === journey.length - 1;
    next.textContent = current < 0 ? 'Başlat →' : current === journey.length - 1 ? 'Yolculuk tamamlandı ✓' : 'Sonraki adım →';
    if (current < 0) {
      root.querySelector('.journey-explanation [data-journey-title]').textContent = 'Hazır';
      root.querySelector('[data-journey-text]').textContent = 'Başlat düğmesine basarak verinin sensörden çıktıya yolculuğunu izleyin.';
    } else {
      selectTab('electronic');
      root.querySelector('.journey-explanation [data-journey-title]').textContent = `${current + 1}. ${journey[current][0]}`;
      root.querySelector('[data-journey-text]').textContent = journey[current][1];
    }
  }
  controls.hidden = false;
  next.addEventListener('click', () => { if (current < journey.length - 1) current++; render(); });
  previous.addEventListener('click', () => { if (current > 0) current--; render(); });
  root.querySelector('[data-journey-reset]').addEventListener('click', () => { current = -1; render(); selectTab('general'); });
  render();
})();
