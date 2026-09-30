/**
 * Interactive System Architecture and Simulation Lab for Week 3
 * Vanilla JS, no external dependencies, fully accessible.
 */
document.addEventListener('DOMContentLoaded', () => {
  initSysArch();
  initLabTabs();
  initCpuSim();
  initMemSim();
  initPortsSim();
});

/* ========================================================
   1. System Architecture Explorer Inspector
   ======================================================== */
function initSysArch() {
  const container = document.querySelector('[data-sys-arch]');
  if (!container) return;

  const buttons = container.querySelectorAll('.sys-arch-node');
  const titleEl = container.querySelector('[data-inspector-title]');
  const enEl = container.querySelector('[data-inspector-en]');
  const descEl = container.querySelector('[data-inspector-desc]');
  const winEl = container.querySelector('[data-inspector-win]');
  const lnxEl = container.querySelector('[data-inspector-lnx]');
  const macEl = container.querySelector('[data-inspector-mac]');
  const tipEl = container.querySelector('[data-inspector-tip]');

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => b.setAttribute('aria-pressed', 'false'));
      btn.setAttribute('aria-pressed', 'true');

      if (titleEl) titleEl.textContent = btn.dataset.title;
      if (enEl) enEl.textContent = btn.dataset.en;
      if (descEl) descEl.textContent = btn.dataset.desc;
      if (winEl) winEl.textContent = btn.dataset.win;
      if (lnxEl) lnxEl.textContent = btn.dataset.lnx;
      if (macEl) macEl.textContent = btn.dataset.mac;
      if (tipEl) tipEl.textContent = btn.dataset.tip;
    });
  });

  // Activate first node by default if available
  if (buttons.length > 0) {
    buttons[0].click();
  }
}

/* ========================================================
   2. Tab Switcher
   ======================================================== */
function initLabTabs() {
  const lab = document.querySelector('[data-sim-lab]');
  if (!lab) return;

  const tabButtons = lab.querySelectorAll('[data-sim-tab]');
  const panels = lab.querySelectorAll('[data-sim-panel]');

  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.simTab;

      tabButtons.forEach(b => {
        b.setAttribute('aria-selected', b === btn ? 'true' : 'false');
      });

      panels.forEach(p => {
        if (p.dataset.simPanel === target) {
          p.hidden = false;
        } else {
          p.hidden = true;
        }
      });
    });
  });
}

/* ========================================================
   3. CPU & Multitasking Simulator
   ======================================================== */
function initCpuSim() {
  const panel = document.querySelector('[data-sim-panel="cpu"]');
  if (!panel) return;

  const DEFAULT_PROCESSES = [
    { id: 'P1', name: 'Nginx Web Sunucu', burst: 6, prio: 1 },
    { id: 'P2', name: 'ESP32 Sensör Servisi', burst: 5, prio: 2 },
    { id: 'P3', name: 'MySQL Veritabanı', burst: 7, prio: 1 },
    { id: 'P4', name: 'Python Derleyici', burst: 4, prio: 3 },
    { id: 'P5', name: 'Sistem Günlükleyici (Log)', burst: 3, prio: 4 }
  ];

  let readyQueue = JSON.parse(JSON.stringify(DEFAULT_PROCESSES));
  let cores = [
    { task: null, remainingTick: 0, pct: 0 },
    { task: null, remainingTick: 0, pct: 0 },
    { task: null, remainingTick: 0, pct: 0 },
    { task: null, remainingTick: 0, pct: 0 }
  ];
  let contextSwitches = 0;
  let autoTimer = null;
  let processCounter = 6;

  const queueList = panel.querySelector('[data-process-queue]');
  const queueCount = panel.querySelector('[data-queue-count]');
  const contextCountEl = panel.querySelector('[data-context-count]');
  const cpuTotalEl = panel.querySelector('[data-cpu-total]');
  const playBtn = panel.querySelector('[data-cpu-action="play"]');
  const stepBtn = panel.querySelector('[data-cpu-action="step"]');
  const addBtn = panel.querySelector('[data-cpu-action="add"]');
  const resetBtn = panel.querySelector('[data-cpu-action="reset"]');

  function renderQueue() {
    if (!queueList) return;
    queueList.innerHTML = '';
    if (readyQueue.length === 0) {
      queueList.innerHTML = '<span class="muted" style="font-size:12px">Kuyruk boş. Bütün süreçler çekirdeklerde veya tamamlandı.</span>';
    } else {
      readyQueue.forEach(p => {
        const pill = document.createElement('div');
        pill.className = 'proc-pill';
        pill.innerHTML = `<strong>${p.id}</strong> <span>${p.name}</span> <small>Kalan: ${p.burst}s</small>`;
        queueList.appendChild(pill);
      });
    }
    if (queueCount) queueCount.textContent = `${readyQueue.length} Süreç Bekliyor`;
  }

  function updateCoresUI() {
    let busyCount = 0;
    cores.forEach((c, idx) => {
      const box = panel.querySelector(`[data-core="${idx}"]`);
      const pctEl = panel.querySelector(`[data-core-pct="${idx}"]`);
      const barEl = panel.querySelector(`[data-core-bar="${idx}"]`);
      const taskEl = panel.querySelector(`[data-core-task="${idx}"]`);

      if (c.task) {
        busyCount++;
        c.pct = Math.min(100, Math.floor(60 + Math.random() * 38));
        if (box) box.classList.add('busy');
        if (taskEl) taskEl.textContent = `${c.task.id}: ${c.task.name} (${c.remainingTick}t)`;
      } else {
        c.pct = 0;
        if (box) box.classList.remove('busy');
        if (taskEl) taskEl.textContent = 'Boşta (Idle)';
      }

      if (pctEl) pctEl.textContent = `${c.pct}%`;
      if (barEl) barEl.style.width = `${c.pct}%`;
    });

    if (cpuTotalEl) {
      const avg = Math.round(cores.reduce((sum, c) => sum + c.pct, 0) / cores.length);
      cpuTotalEl.textContent = `${avg}%`;
    }
    if (contextCountEl) contextCountEl.textContent = contextSwitches;
  }

  function step() {
    // 1. Progress current tasks on cores
    cores.forEach((c) => {
      if (c.task) {
        c.remainingTick--;
        c.task.burst--;

        // Quantum expired or process finished
        if (c.task.burst <= 0) {
          // Completed
          c.task = null;
          c.remainingTick = 0;
        } else if (c.remainingTick <= 0) {
          // Time slice expired -> Context Switch back to queue!
          contextSwitches++;
          readyQueue.push(c.task);
          c.task = null;
        }
      }
    });

    // 2. Schedule waiting tasks to idle cores
    cores.forEach((c) => {
      if (!c.task && readyQueue.length > 0) {
        const nextTask = readyQueue.shift();
        c.task = nextTask;
        c.remainingTick = 2; // Quantum = 2 ticks
        contextSwitches++;
      }
    });

    renderQueue();
    updateCoresUI();
  }

  if (stepBtn) {
    stepBtn.addEventListener('click', () => {
      if (autoTimer) stopPlay();
      step();
    });
  }

  function stopPlay() {
    clearInterval(autoTimer);
    autoTimer = null;
    if (playBtn) playBtn.textContent = '▶️ Otomatik Yürüt';
  }

  if (playBtn) {
    playBtn.addEventListener('click', () => {
      if (autoTimer) {
        stopPlay();
      } else {
        playBtn.textContent = '⏸️ Duraklat';
        autoTimer = setInterval(step, 800);
      }
    });
  }

  if (addBtn) {
    addBtn.addEventListener('click', () => {
      const names = ['Grafik Render', 'TCP Veri Ayrıştırıcı', 'Kamera Akışı', 'Yapay Zekâ Çıkarımı', 'Sıcaklık Grafiği'];
      const pickName = names[Math.floor(Math.random() * names.length)];
      readyQueue.push({
        id: `P${processCounter++}`,
        name: pickName,
        burst: Math.floor(4 + Math.random() * 5),
        prio: 2
      });
      renderQueue();
    });
  }

  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      stopPlay();
      readyQueue = JSON.parse(JSON.stringify(DEFAULT_PROCESSES));
      cores = [
        { task: null, remainingTick: 0, pct: 0 },
        { task: null, remainingTick: 0, pct: 0 },
        { task: null, remainingTick: 0, pct: 0 },
        { task: null, remainingTick: 0, pct: 0 }
      ];
      contextSwitches = 0;
      processCounter = 6;
      renderQueue();
      updateCoresUI();
    });
  }

  // Initial render
  renderQueue();
  updateCoresUI();
}

/* ========================================================
   4. Memory, Paging & Swap Simulator
   ======================================================== */
function initMemSim() {
  const panel = document.querySelector('[data-sim-panel="mem"]');
  if (!panel) return;

  const RAM_SIZE = 4;
  const SWAP_SIZE = 4;

  let ram = [null, null, null, null]; // Frame 0..3
  let swap = [null, null, null, null]; // Swap 0..3
  let pageHistory = []; // for LRU / FIFO tracking

  let hits = 0;
  let faults = 0;
  let swaps = 0;

  const hitsEl = panel.querySelector('[data-mem-hits]');
  const faultsEl = panel.querySelector('[data-mem-faults]');
  const swapsEl = panel.querySelector('[data-mem-swaps]');
  const eventTitle = panel.querySelector('[data-mmu-event-title]');
  const eventDesc = panel.querySelector('[data-mmu-event-desc]');
  const statusBadge = panel.querySelector('[data-mem-status-badge]');
  const statusText = panel.querySelector('[data-mem-status-text]');

  const pageButtons = panel.querySelectorAll('[data-vpage]');
  const randomBtn = panel.querySelector('[data-mem-action="random"]');
  const fillBtn = panel.querySelector('[data-mem-action="fill"]');
  const thrashBtn = panel.querySelector('[data-mem-action="thrash"]');
  const resetBtn = panel.querySelector('[data-mem-action="reset"]');

  function renderFrames() {
    for (let i = 0; i < RAM_SIZE; i++) {
      const slot = panel.querySelector(`[data-frame="${i}"]`);
      if (slot) {
        if (ram[i] !== null) {
          slot.className = 'frame-slot occupied';
          slot.innerHTML = `<span>Çerçeve ${i}</span><strong>Sayfa ${ram[i]}</strong>`;
        } else {
          slot.className = 'frame-slot empty';
          slot.innerHTML = `<span>Çerçeve ${i}</span><strong>Boş</strong>`;
        }
      }
    }

    for (let j = 0; j < SWAP_SIZE; j++) {
      const slot = panel.querySelector(`[data-swap="${j}"]`);
      if (slot) {
        if (swap[j] !== null) {
          slot.className = 'frame-slot swap-slot occupied';
          slot.innerHTML = `<span>Swap ${j}</span><strong>Sayfa ${swap[j]}</strong>`;
        } else {
          slot.className = 'frame-slot swap-slot empty';
          slot.innerHTML = `<span>Swap ${j}</span><strong>Boş</strong>`;
        }
      }
    }

    if (hitsEl) hitsEl.textContent = hits;
    if (faultsEl) faultsEl.textContent = faults;
    if (swapsEl) swapsEl.textContent = swaps;
  }

  function requestPage(vPage) {
    vPage = parseInt(vPage, 10);

    // 1. Is page already in RAM?
    const ramIndex = ram.indexOf(vPage);
    if (ramIndex !== -1) {
      hits++;
      const slot = panel.querySelector(`[data-frame="${ramIndex}"]`);
      if (slot) {
        slot.classList.remove('highlight-hit');
        void slot.offsetWidth; // retrigger anim
        slot.classList.add('highlight-hit');
      }
      if (eventTitle) eventTitle.textContent = `🟢 RAM HIT: Sayfa ${vPage}`;
      if (eventDesc) eventDesc.textContent = `Sanal Sayfa ${vPage}, fiziksel Çerçeve ${ramIndex} içinde bulundu! Çok hızlı erişim (~10 ns).`;
      setNormalStatus('Sistem Kararlı · RAM Erişimi');
      renderFrames();
      return;
    }

    // 2. PAGE FAULT! Page is NOT in RAM.
    faults++;

    // Check if it's currently stored in Swap
    const swapIndex = swap.indexOf(vPage);
    if (swapIndex !== -1) {
      swap[swapIndex] = null; // will be brought back
    }

    // Find an empty RAM frame
    const emptyRamIndex = ram.indexOf(null);
    if (emptyRamIndex !== -1) {
      ram[emptyRamIndex] = vPage;
      pageHistory.push(vPage);
      if (eventTitle) eventTitle.textContent = `🟡 PAGE FAULT: Sayfa ${vPage}`;
      if (eventDesc) eventDesc.textContent = `Sayfa ${vPage} RAM'de yoktu! Diskten Çerçeve ${emptyRamIndex}'e yüklendi.`;
      setNormalStatus('Sayfa Hatası Çözüldü');
    } else {
      // RAM IS FULL! Need page eviction (Page Replacement)
      swaps++;
      const evictedPage = pageHistory.shift();
      const victimIndex = ram.indexOf(evictedPage);

      // Save victim to Swap disk
      const emptySwapIndex = swap.indexOf(null);
      if (emptySwapIndex !== -1) {
        swap[emptySwapIndex] = evictedPage;
      } else {
        swap[0] = evictedPage; // overwrite oldest swap
      }

      ram[victimIndex] = vPage;
      pageHistory.push(vPage);

      if (eventTitle) eventTitle.textContent = `🟠 SWAP TAKASI: Sayfa ${evictedPage} Diske Atıldı`;
      if (eventDesc) eventDesc.textContent = `RAM doluydu! Sayfa ${evictedPage} diske yazıldı (Page Out) ve yeni Sayfa ${vPage} RAM'e alındı.`;
      setWarningStatus('Disk Takası (Swap) Devrede');
    }

    renderFrames();
  }

  function setNormalStatus(msg) {
    if (statusBadge) statusBadge.className = 'sim-status-indicator';
    if (statusText) statusText.textContent = msg;
  }
  function setWarningStatus(msg) {
    if (statusBadge) statusBadge.className = 'sim-status-indicator warning';
    if (statusText) statusText.textContent = msg;
  }
  function setDangerStatus(msg) {
    if (statusBadge) statusBadge.className = 'sim-status-indicator danger';
    if (statusText) statusText.textContent = msg;
  }

  pageButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      requestPage(btn.dataset.vpage);
    });
  });

  if (randomBtn) {
    randomBtn.addEventListener('click', () => {
      const rand = Math.floor(Math.random() * 8);
      requestPage(rand);
    });
  }

  if (fillBtn) {
    fillBtn.addEventListener('click', () => {
      [0, 1, 2, 3, 4, 5].forEach(p => requestPage(p));
    });
  }

  if (thrashBtn) {
    thrashBtn.addEventListener('click', () => {
      // simulate rapid alternating page requests
      setDangerStatus('⚠️ THRASHING! Aşırı Sayfalama Tespit Edildi!');
      if (eventTitle) eventTitle.textContent = '🚨 SİSTEM YAVAŞLADI: Thrashing';
      if (eventDesc) eventDesc.textContent = 'Bellek yetersiz! İşlemci komut yürütmek yerine zamanının %90\'ını RAM-Disk arasında sayfa takasına harcıyor.';
      
      let stepCount = 0;
      const thrashSeq = [0, 4, 1, 5, 2, 6, 3, 7];
      const thrashTimer = setInterval(() => {
        if (stepCount >= thrashSeq.length) {
          clearInterval(thrashTimer);
        } else {
          requestPage(thrashSeq[stepCount++]);
        }
      }, 350);
    });
  }

  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      ram = [null, null, null, null];
      swap = [null, null, null, null];
      pageHistory = [];
      hits = 0;
      faults = 0;
      swaps = 0;
      setNormalStatus('Sistem Normal · Bellek Temizlendi');
      if (eventTitle) eventTitle.textContent = 'Olay Bekleniyor';
      if (eventDesc) eventDesc.textContent = 'Sayfa talep düğmelerine basarak adres çözümlemesini tetikleyin.';
      renderFrames();
    });
  }

  renderFrames();
}

/* ========================================================
   5. Hardware & Network Ports Station
   ======================================================== */
function initPortsSim() {
  const panel = document.querySelector('[data-sim-panel="ports"]');
  if (!panel) return;

  // Sublab 1: USB / Hardware
  let usbConnected = false;
  let serialOpen = false;
  let serialTimer = null;

  const devCard = panel.querySelector('.device-card');
  const devTitle = panel.querySelector('[data-device-title]');
  const devSub = panel.querySelector('[data-device-sub]');
  const usbBtn = panel.querySelector('[data-port-action="toggle-usb"]');
  const pnpLog = panel.querySelector('[data-pnp-log]');
  const activeComEl = panel.querySelector('[data-active-com]');
  const serialBtn = panel.querySelector('[data-port-action="toggle-serial"]');
  const serialOutput = panel.querySelector('[data-serial-output]');
  const baudSelect = panel.querySelector('[data-baud-select]');

  function logPnp(text) {
    if (!pnpLog) return;
    const line = document.createElement('div');
    line.className = 'log-line';
    line.textContent = `[${new Date().toLocaleTimeString()}] ${text}`;
    pnpLog.appendChild(line);
    pnpLog.scrollTop = pnpLog.scrollHeight;
  }

  if (usbBtn) {
    usbBtn.addEventListener('click', () => {
      usbConnected = !usbConnected;
      if (usbConnected) {
        devCard.setAttribute('data-device-state', 'connected');
        usbBtn.textContent = 'USB Kablosunu Çıkar';
        devTitle.textContent = 'ESP32 DevKit V1 (CH340 Sürücüsü)';
        devSub.textContent = 'Bağlandı · Windows: COM4 | Linux: /dev/ttyUSB0';
        logPnp('PnP Olayı: Yeni USB aygıtı takıldı (VID: 0x1A86, PID: 0x7523).');
        logPnp('Sürücü eşlendi: ch341.sys / ch341.ko -> Sanal Seri Port COM4 atandı.');
        if (activeComEl) activeComEl.textContent = 'COM4 Hazır';
        if (serialBtn) serialBtn.disabled = false;
      } else {
        if (serialOpen) toggleSerial();
        devCard.setAttribute('data-device-state', 'disconnected');
        usbBtn.textContent = 'USB Kablosunu Tak';
        devTitle.textContent = 'ESP32 DevKit V1';
        devSub.textContent = 'USB Bağlantısı Yok';
        logPnp('PnP Olayı: Aygıt çıkarıldı. Port COM4 serbest bırakıldı.');
        if (activeComEl) activeComEl.textContent = 'COM Kapalı';
        if (serialBtn) serialBtn.disabled = true;
      }
    });
  }

  function toggleSerial() {
    serialOpen = !serialOpen;
    if (serialOpen) {
      serialBtn.textContent = 'Portu Kapat';
      serialOutput.innerHTML = '';
      const baud = baudSelect ? baudSelect.value : '115200';
      serialOutput.innerHTML += `<div>--- COM4 Seri Port Açıldı (${baud} bps) ---</div>`;
      
      let temp = 23.5;
      serialTimer = setInterval(() => {
        temp += (Math.random() - 0.48) * 0.3;
        const line = document.createElement('div');
        line.textContent = `[SENSOR_DATA] {"temp_c": ${temp.toFixed(2)}, "humidity": 47.8, "heap_free": 178240}`;
        serialOutput.appendChild(line);
        serialOutput.scrollTop = serialOutput.scrollHeight;
      }, 1000);
    } else {
      serialBtn.textContent = 'Portu Aç';
      clearInterval(serialTimer);
      serialTimer = null;
      serialOutput.innerHTML += '<div>--- COM4 Portu Kapatıldı ---</div>';
    }
  }

  if (serialBtn) {
    serialBtn.addEventListener('click', toggleSerial);
  }

  // Sublab 2: Network Ports (Sockets)
  const portStates = {
    80: false,
    443: false,
    22: false,
    8080: false
  };

  const packetLog = panel.querySelector('[data-packet-log]');

  function logPacket(msg) {
    if (!packetLog) return;
    packetLog.innerHTML = `<span style="color:var(--accent)">[${new Date().toLocaleTimeString()}]</span> ${msg}`;
  }

  [80, 443, 22, 8080].forEach(port => {
    const btn = panel.querySelector(`[data-toggle-net="${port}"]`);
    const pill = panel.querySelector(`[data-port-state="${port}"]`);

    if (btn && pill) {
      btn.addEventListener('click', () => {
        portStates[port] = !portStates[port];
        if (portStates[port]) {
          pill.className = 'status-pill listening';
          pill.textContent = 'LISTENING';
          btn.textContent = 'Servisi Durdur';
          logPacket(`Port ${port} dinlemeye başladı (0.0.0.0:${port}). İşletim sistemi gelen TCP paketlerini bu sürece yönlendirecek.`);
        } else {
          pill.className = 'status-pill closed';
          pill.textContent = 'CLOSED';
          btn.textContent = 'Servisi Başlat';
          logPacket(`Port ${port} kapatıldı. Soket serbest bırakıldı.`);
        }
      });
    }
  });

  const sendButtons = panel.querySelectorAll('[data-send-packet]');
  sendButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const port = parseInt(btn.dataset.sendPacket, 10);
      if (portStates[port]) {
        const pill = panel.querySelector(`[data-port-state="${port}"]`);
        if (pill) {
          pill.className = 'status-pill established';
          pill.textContent = 'ESTABLISHED';
          setTimeout(() => {
            if (portStates[port]) {
              pill.className = 'status-pill listening';
              pill.textContent = 'LISTENING';
            }
          }, 1500);
        }
        logPacket(`✅ [TCP 3-Way Handshake Başarılı] Port ${port} üzerinde soket kuruldu! Veri paketi teslim edildi ve HTTP 200 yanıtı döndü.`);
      } else {
        logPacket(`❌ [Connection Refused / Bağlantı Reddedildi] 127.0.0.1:${port} üzerinde dinleyen bir süreç bulunamadı! İşletim sistemi TCP RST paketi döndürdü.`);
      }
    });
  });
}
