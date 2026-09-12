/* Teaching simulations: no sensor, cloud account or hardware connection. */
const ledButton = document.querySelector('#led-toggle');
ledButton?.addEventListener('click', () => { const on = ledButton.getAttribute('aria-pressed') !== 'true'; ledButton.setAttribute('aria-pressed', String(on)); document.querySelector('#led').classList.toggle('on', on); document.querySelector('#led-state').textContent = on ? 'LED açık' : 'LED kapalı'; });
document.querySelector('#sensor-read')?.addEventListener('click', () => { document.querySelector('#sensor-value').textContent = `${(20 + Math.random() * 10).toFixed(1)} °C (simülasyon)`; });
const powerForm = document.querySelector('#power-demo');
function updatePower() { const v = Number(powerForm.elements.voltage.value), i = Number(powerForm.elements.current.value), t = Number(powerForm.elements.hours.value); document.querySelector('#power-result').textContent = `P = ${(v*i).toFixed(2)} W · E = ${(v*i*t).toFixed(2)} Wh`; }
if (powerForm) { powerForm.addEventListener('input', updatePower); powerForm.addEventListener('submit', e => e.preventDefault()); updatePower(); }
