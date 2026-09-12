/* All teaching state is temporary; no access to actual RAM, files or hardware. */
(() => {
 const root = document.querySelector('.concept-explorer');
 if (!root) return;
 const cards = [...root.querySelectorAll('.explore-card')];
 const count = root.querySelector('[data-concept-count]');
 root.querySelector('.concept-filters').hidden = false;
 function filter(group) {
  let visible = 0;
  cards.forEach(card => { card.hidden = group !== 'all' && card.dataset.conceptGroup !== group; if (!card.hidden) visible++; });
  root.querySelectorAll('[data-concept-filter]').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.conceptFilter === group)));
  count.textContent = `${visible} kavram · Açmak veya kapatmak için karta dokunun.`;
 }
 root.querySelectorAll('[data-concept-filter]').forEach(button => button.addEventListener('click', () => filter(button.dataset.conceptFilter)));
 filter('all');
 function revealHash() {
  const card = cards.find(item => `#${item.id}` === location.hash);
  if (card) { filter('all'); card.open = true; }
 }
 revealHash(); window.addEventListener('hashchange', revealHash);
 const cpu = root.querySelector('[data-cpu-pixels]');
 const gpu = root.querySelector('[data-gpu-pixels]');
 for (let i = 0; i < 12; i++) { cpu.append(document.createElement('span')); gpu.append(document.createElement('span')); }
 let step = 0;
 const stepButton = root.querySelector('[data-parallel-step]');
 function draw() {
  const a = Math.min(step, 12), b = Math.min(step * 4, 12);
  [...cpu.children].forEach((cell, i) => cell.classList.toggle('done', i < a));
  [...gpu.children].forEach((cell, i) => cell.classList.toggle('done', i < b));
  root.querySelector('[data-cpu-result]').textContent = `${a} / 12 piksel`;
  root.querySelector('[data-gpu-result]').textContent = `${b} / 12 piksel`;
  root.querySelector('[data-parallel-status]').textContent = `Adım ${step}: tek akış ${a}, paralel yaklaşım ${b} piksel işledi.`;
  stepButton.disabled = step === 12;
 }
 root.querySelector('.lab-controls').hidden = false;
 stepButton.addEventListener('click', () => { step = Math.min(12, step + 1); draw(); });
 root.querySelector('[data-parallel-reset]').addEventListener('click', () => { step = 0; draw(); });
 draw();
 let ram = 24, disk = 24, power = true;
 const edit = root.querySelector('[data-memory-edit]');
 const save = root.querySelector('[data-memory-save]');
 const toggle = root.querySelector('[data-memory-power]');
 function memory(message) {
  root.querySelector('[data-memory-ram]').textContent = power ? `${ram} °C` : 'Boş · Güç yok';
  root.querySelector('[data-memory-disk]').textContent = `${disk} °C`;
  root.querySelector('[data-memory-status]').textContent = message;
  edit.disabled = save.disabled = !power;
  toggle.textContent = power ? 'Gücü kes' : 'Yeniden aç ve dosyayı yükle';
 }
 root.querySelector('.memory-controls').hidden = false;
 edit.addEventListener('click', () => { ram++; memory('Çalışma kopyası değişti; SSD’deki dosya henüz güncellenmedi.'); });
 save.addEventListener('click', () => { disk = ram; memory('RAM’deki değer SSD’ye kaydedildi.'); });
 toggle.addEventListener('click', () => {
  power = !power;
  if (!power) { ram = null; memory('Güç kesildi. RAM içeriği kayboldu; SSD’deki kayıt korundu.'); }
  else { ram = disk; memory('Sistem açıldı; SSD’deki son kayıt RAM’e yüklendi.'); }
 });
 root.querySelector('[data-memory-reset]').addEventListener('click', () => { ram = disk = 24; power = true; memory('Deney sıfırlandı: RAM ve SSD 24 °C.'); });
 // In print, reveal native details; restore the student's reading state afterwards.
 let printState;
 window.addEventListener('beforeprint', () => { printState = cards.map(card => ({open:card.open,hidden:card.hidden})); cards.forEach(card => { card.open = true; card.hidden = false; }); });
 window.addEventListener('afterprint', () => { if (printState) cards.forEach((card, i) => { card.open = printState[i].open; card.hidden = printState[i].hidden; }); });
})();
