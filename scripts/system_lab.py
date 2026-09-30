"""Interactive simulation and visual architecture components for Week 3."""
from html import escape as esc

SUBSYSTEMS = [
    ("user-space", "Kullanıcı Alanı", "User Space", "Uygulamalar, web sunucuları ve terminal kabukları (CLI/GUI) burada kısıtlı yetkiyle (Ring 3) çalışır.", "apps",
     "Windows: Win32/UWP Apps, PowerShell", "Linux: Kullanıcı Süreçleri, Bash, Zsh", "macOS: Cocoa Apps, Zsh Terminali", "Doğrudan donanıma erişemez; sistem çağrısı (syscall) yapmak zorundadır."),
    ("syscalls", "Sistem Çağrıları", "System Calls (Syscall)", "Kullanıcı programlarının işletim sistemi çekirdeğinden kaynak istemesini sağlayan güvenli geçiş kapısı.", "syscall",
     "Windows: Win32 API, NTDLL.dll (NtReadFile vb.)", "Linux: POSIX API (read, write, fork, exec)", "macOS: BSD/Mach Syscalls (open, mmap, fork)", "Kullanıcı modundan çekirdek moduna (Ring 0) bağlam geçişi (context switch) tetikler."),
    ("scheduler", "İşlemci & Zamanlayıcı", "CPU Scheduler & Processes", "Çalışmaya hazır süreçleri ve iş parçacıklarını CPU çekirdeklerine paylaştırır.", "cpu",
     "Windows: Preemptive Priority Scheduler (0-31)", "Linux: Completely Fair Scheduler (CFS)", "macOS: Mach Preemptive Scheduler", "Round-Robin ve öncelik algoritmalarıyla hiçbir sürecin sistemi kilitlemesine izin vermez."),
    ("vmm", "Sanal Bellek & MMU", "Virtual Memory Manager (VMM)", "Her sürece izole 64-bit sanal adres alanı sunar; fiziksel RAM ve disk takas (swap) alanını yönetir.", "memory",
     "Windows: VirtualAlloc, pagefile.sys", "Linux: mmap, /dev/swap veya swapfile", "macOS: VM Subsystem, dinamik takas (/var/vm)", "Sayfalama (paging) ve MMU ile süreçlerin birbirinin belleğine müdahalesini engeller."),
    ("vfs", "Sanal Dosya Sistemi (VFS)", "Virtual File System & Storage", "Farklı disk formatlarını tek tip dosya ağacı altında uygulamalara sunar.", "storage",
     "Windows: NTFS, ReFS, FAT32 / Sürücü Harfleri (C:, D:)", "Linux: VFS (ext4, btrfs) / Tek Ağaç Hiyerarşisi (/)", "macOS: APFS, HFS+ / Kök Dizin (/)", "Günlükleme (journaling) ile ani güç kesintilerinde dosya bozulmalarını önler."),
    ("drivers", "Aygıt Sürücüleri & IRQ", "Device Drivers & Interrupts", "Donanıma özgü sinyalleri çekirdeğin anlayabileceği standart API'lere çevirir.", "driver",
     "Windows: Windows Driver Framework (WDF, KMDF)", "Linux: Kernel Modules (.ko), udev kuralları", "macOS: DriverKit / I/O Kit", "Donanım veri ürettiğinde kesme (IRQ) göndererek CPU'nun hemen işlem yapmasını sağlar."),
    ("net-stack", "Ağ Yığını & Portlar", "Network Stack & Socket Ports", "TCP/IP protokollerini ve 1-65535 arası mantıksal servis portlarını yönetir.", "network",
     "Windows: Winsock2, Get-NetTCPConnection", "Linux: Netfilter/Socket API, ss, ip, netstat", "macOS: BSD Sockets, lsof -i", "Hangi ağ paketinin hangi yerel sürece teslim edileceğini port numaraları belirler."),
    ("hardware", "Fiziksel Donanım Katmanı", "Physical Hardware", "İşlemci, RAM, SSD/Flash, USB-UART dönüştürücüler, Ethernet ve çevre birimleri.", "board",
     "Windows: ACPI, PCI Express, USB PnP", "Linux: /sys, /dev, lspci, lsusb", "macOS: Apple Silicon / Thunderbolt Fabric", "Elektriksel sinyaller, veri yolları ve saat frekansı seviyesinde çalışan fiziksel dünya.")
]

def sub_icon(kind):
    icons = {
        "apps": '<rect x="18" y="24" width="28" height="24" rx="4"/><rect x="50" y="24" width="28" height="24" rx="4"/><rect x="18" y="52" width="60" height="20" rx="4"/><circle cx="28" cy="62" r="3"/><circle cx="38" cy="62" r="3"/>',
        "syscall": '<path d="M20 48h56m-14-14 14 14-14 14M76 48H20"/><rect x="14" y="22" width="68" height="52" rx="8" stroke-dasharray="4 4"/>',
        "cpu": '<rect x="26" y="26" width="44" height="44" rx="8"/><rect x="38" y="38" width="20" height="20" rx="4"/><path d="M36 16v10m12-10v10m12-10v10M36 70v10m12-10v10m12-10v10M16 36h10m-10 12h10m-10 12h10M70 36h10m-10 12h10m-10 12h10"/>',
        "memory": '<rect x="16" y="30" width="64" height="36" rx="6"/><path d="M26 40h12v16H26zM42 40h12v16H42zM58 40h12v16H58zM24 66v8m12-8v8m12-8v8m12-8v8m12-8v8"/>',
        "storage": '<rect x="22" y="20" width="52" height="56" rx="8"/><circle cx="48" cy="48" r="16"/><circle cx="48" cy="48" r="4"/><path d="M30 68h36"/>',
        "driver": '<path d="M48 20v14m0 28v14M20 48h14m28 0h14"/><circle cx="48" cy="48" r="14"/><circle cx="48" cy="48" r="5"/>',
        "network": '<circle cx="48" cy="30" r="10"/><circle cx="28" cy="66" r="10"/><circle cx="68" cy="66" r="10"/><path d="M42 38l-9 20m15-20l9 20M38 66h20"/>',
        "board": '<rect x="20" y="20" width="56" height="56" rx="8"/><circle cx="32" cy="32" r="3"/><circle cx="64" cy="32" r="3"/><circle cx="32" cy="64" r="3"/><circle cx="64" cy="64" r="3"/><path d="M40 38h16v20H40z"/>'
    }
    return f'<svg viewBox="0 0 96 96" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{icons[kind]}</g></svg>'

def render_system_architecture():
    cards = []
    for item in SUBSYSTEMS:
        ident, title, english, desc, art, win, lnx, mac, tip = item
        cards.append(f'''<button type="button" class="sys-arch-node" data-arch-id="{esc(ident)}" data-title="{esc(title)}" data-en="{esc(english)}" data-desc="{esc(desc)}" data-win="{esc(win)}" data-lnx="{esc(lnx)}" data-mac="{esc(mac)}" data-tip="{esc(tip)}" aria-pressed="false">
          <div class="node-icon">{sub_icon(art)}</div>
          <div class="node-text"><strong>{esc(title)}</strong><small lang="en">{esc(english)}</small></div>
        </button>''')
    
    return f'''<div class="sys-architecture-explorer" data-sys-arch>
      <p class="sys-arch-lead">İşletim sistemi; donanım ile kullanıcı yazılımları arasında köprü kuran <strong>katmanlı bir denetim merkezidir</strong>. Bir katmana tıklayarak görevini, Windows/Linux/macOS karşılıklarını ve kilit mühendislik detaylarını inceleyin.</p>
      
      <div class="sys-arch-grid" role="region" aria-label="Sistem Mimarisi Katmanları">
        {''.join(cards)}
      </div>

      <aside class="sys-arch-inspector" data-arch-inspector aria-live="polite">
        <div class="inspector-header">
          <span class="eyebrow">SEÇİLİ SİSTEM KATMANI</span>
          <h3 data-inspector-title>İncelemek için yukarıdan bir katman seçin</h3>
          <p class="inspector-en" data-inspector-en lang="en">User Space ↔ Kernel Subsystems ↔ Hardware Layer</p>
        </div>
        <p class="inspector-desc" data-inspector-desc>Herhangi bir katman kartına dokunduğunuzda görevini, çekirdek modunu ve üç ana işletim sistemindeki somut karşılıklarını burada göreceksiniz.</p>
        <div class="os-comparison-pills">
          <div class="os-pill win"><strong>Windows:</strong> <span data-inspector-win>Win32 / NT Kernel</span></div>
          <div class="os-pill lnx"><strong>Linux:</strong> <span data-inspector-lnx>POSIX / Monolithic Kernel</span></div>
          <div class="os-pill mac"><strong>macOS:</strong> <span data-inspector-mac>XNU / Darwin Subsystems</span></div>
        </div>
        <div class="inspector-tip">
          <strong>Mühendislik Notu:</strong> <span data-inspector-tip>İşletim sistemi olmadan bir program çalıştırmak (bare-metal) bu soyutlamaların tamamından vazgeçmek anlamına gelir.</span>
        </div>
      </aside>
    </div>'''

def render_system_lab():
    return '''<div class="system-sim-lab" data-sim-lab>
      <div class="sim-tabs" role="tablist" aria-label="Simülasyon Modülleri">
        <button type="button" role="tab" id="tab-cpu" aria-controls="panel-cpu" aria-selected="true" data-sim-tab="cpu">
          ⚡ 1. İşlemci (CPU) & Çoklu Görev
        </button>
        <button type="button" role="tab" id="tab-mem" aria-controls="panel-mem" aria-selected="false" data-sim-tab="mem">
          🧠 2. Sanal Bellek & Sayfa Takası (Swap)
        </button>
        <button type="button" role="tab" id="tab-ports" aria-controls="panel-ports" aria-selected="false" data-sim-tab="ports">
          🔌 3. Donanım & Ağ Portları İstasyonu
        </button>
        <button type="button" role="tab" id="tab-tasks-disk" aria-controls="panel-tasks-disk" aria-selected="false" data-sim-tab="tasks-disk">
          🛠️ 4. Görev Yöneticisi & Disk Bakımı
        </button>
      </div>

      <!-- PANEL 1: CPU SCHEDULING SIMULATOR -->
      <div class="sim-panel" id="panel-cpu" role="tabpanel" aria-labelledby="tab-cpu" data-sim-panel="cpu">
        <div class="sim-header">
          <div>
            <span class="eyebrow">İNTERAKTİF SİMÜLATÖR</span>
            <h3>4 Çekirdekli CPU Zamanlayıcı & Multitasking</h3>
            <p>Modern işletim sistemlerinde CPU Zamanlayıcı (Scheduler), süreçleri çekirdeklere dağıtır ve zaman dilimleri (time slices) bitince bağlam değişimi (context switch) yapar.</p>
          </div>
          <div class="sim-stats-badge">
            <span class="badge-label">Aktif Algoritma:</span>
            <strong>Round Robin (Kuantum: 2 Tick)</strong>
          </div>
        </div>

        <div class="cpu-cores-grid" aria-label="CPU Çekirdekleri">
          <div class="cpu-core-box" data-core="0">
            <div class="core-top"><span>Çekirdek 0</span><strong data-core-pct="0">0%</strong></div>
            <div class="core-meter"><div class="meter-bar" data-core-bar="0" style="width:0%"></div></div>
            <div class="core-active-task" data-core-task="0">Boşta (Idle)</div>
          </div>
          <div class="cpu-core-box" data-core="1">
            <div class="core-top"><span>Çekirdek 1</span><strong data-core-pct="1">0%</strong></div>
            <div class="core-meter"><div class="meter-bar" data-core-bar="1" style="width:0%"></div></div>
            <div class="core-active-task" data-core-task="1">Boşta (Idle)</div>
          </div>
          <div class="cpu-core-box" data-core="2">
            <div class="core-top"><span>Çekirdek 2</span><strong data-core-pct="2">0%</strong></div>
            <div class="core-meter"><div class="meter-bar" data-core-bar="2" style="width:0%"></div></div>
            <div class="core-active-task" data-core-task="2">Boşta (Idle)</div>
          </div>
          <div class="cpu-core-box" data-core="3">
            <div class="core-top"><span>Çekirdek 3</span><strong data-core-pct="3">0%</strong></div>
            <div class="core-meter"><div class="meter-bar" data-core-bar="3" style="width:0%"></div></div>
            <div class="core-active-task" data-core-task="3">Boşta (Idle)</div>
          </div>
        </div>

        <div class="process-queue-section">
          <div class="queue-heading">
            <strong>Hazır Süreç Kuyruğu (Ready Queue):</strong>
            <span data-queue-count>4 Süreç Bekliyor</span>
          </div>
          <div class="process-pills-list" data-process-queue>
            <!-- Dynamically populated via JS -->
          </div>
        </div>

        <div class="sim-controls-bar">
          <button type="button" class="primary" data-cpu-action="play">▶️ Otomatik Yürüt</button>
          <button type="button" data-cpu-action="step">⏭️ 1 Tick İlerle</button>
          <button type="button" data-cpu-action="add">➕ Yeni Süreç Ekle</button>
          <button type="button" data-cpu-action="reset">🔄 Sıfırla</button>
          <div class="sim-live-metrics">
            <span>Bağlam Değişimi (Context Switch): <strong data-context-count>0</strong></span>
            <span>Toplam CPU: <strong data-cpu-total>0%</strong></span>
          </div>
        </div>
        <p class="sim-explainer"><strong>Gözlem:</strong> Bir sürecin işlemciyi kesintisiz tekeline alamadığını; kuantum süresi bitince sıradaki sürece yer verdiğini ve çekirdekler arası yük dengelendiğini izleyin.</p>
      </div>

      <!-- PANEL 2: MEMORY & PAGING SIMULATOR -->
      <div class="sim-panel" id="panel-mem" role="tabpanel" aria-labelledby="tab-mem" data-sim-panel="mem" hidden>
        <div class="sim-header">
          <div>
            <span class="eyebrow">İNTERAKTİF SİMÜLATÖR</span>
            <h3>Sanal Bellek, Sayfalama (Paging) ve Swap Deneyi</h3>
            <p>Süreçler sanal sayfa (Virtual Page) ister. Sayfa fiziksel RAM'deyse <strong>HIT</strong> olur. RAM'de yoksa <strong>PAGE FAULT</strong> tetiklenir ve diskten takas yapılır.</p>
          </div>
          <div class="sim-status-indicator" data-mem-status-badge>
            <span class="dot"></span> <strong data-mem-status-text>Sistem Normal · Bellek Hazır</strong>
          </div>
        </div>

        <div class="memory-blocks-layout">
          <div class="mem-column">
            <h4>Fiziksel RAM (4 Çerçeve / Frame)</h4>
            <div class="frames-grid" data-ram-frames>
              <div class="frame-slot empty" data-frame="0"><span>Çerçeve 0</span><strong>Boş</strong></div>
              <div class="frame-slot empty" data-frame="1"><span>Çerçeve 1</span><strong>Boş</strong></div>
              <div class="frame-slot empty" data-frame="2"><span>Çerçeve 2</span><strong>Boş</strong></div>
              <div class="frame-slot empty" data-frame="3"><span>Çerçeve 3</span><strong>Boş</strong></div>
            </div>
            <small>Hızlı Erişim: ~10 ns gecikme</small>
          </div>

          <div class="mem-mmu-column">
            <div class="mmu-chip">
              <strong>MMU</strong>
              <small>Adres Çevirici</small>
            </div>
            <div class="mmu-event-card" data-mmu-event>
              <strong data-mmu-event-title>Olay Bekleniyor</strong>
              <p data-mmu-event-desc>Sayfa talep düğmelerine basarak adres çözümlemesini tetikleyin.</p>
            </div>
          </div>

          <div class="mem-column">
            <h4>Disk Takas Alanı (Swap / Pagefile)</h4>
            <div class="frames-grid swap-grid" data-swap-frames>
              <div class="frame-slot swap-slot empty" data-swap="0"><span>Swap Yuva 0</span><strong>Boş</strong></div>
              <div class="frame-slot swap-slot empty" data-swap="1"><span>Swap Yuva 1</span><strong>Boş</strong></div>
              <div class="frame-slot swap-slot empty" data-swap="2"><span>Swap Yuva 2</span><strong>Boş</strong></div>
              <div class="frame-slot swap-slot empty" data-swap="3"><span>Swap Yuva 3</span><strong>Boş</strong></div>
            </div>
            <small>Yavaş Depolama: ~5 ms gecikme (500.000x daha yavaş!)</small>
          </div>
        </div>

        <div class="virtual-pages-palette">
          <strong>Erişilmek İstenen Sanal Sayfa (Virtual Page):</strong>
          <div class="page-buttons" data-page-triggers>
            <button type="button" data-vpage="0">Sayfa 0 (Kod)</button>
            <button type="button" data-vpage="1">Sayfa 1 (Yığın)</button>
            <button type="button" data-vpage="2">Sayfa 2 (Veri)</button>
            <button type="button" data-vpage="3">Sayfa 3 (Öbek)</button>
            <button type="button" data-vpage="4">Sayfa 4 (Sensör Buffer)</button>
            <button type="button" data-vpage="5">Sayfa 5 (Grafik)</button>
            <button type="button" data-vpage="6">Sayfa 6 (Ağ Paketi)</button>
            <button type="button" data-vpage="7">Sayfa 7 (Dosya Önbellek)</button>
          </div>
        </div>

        <div class="sim-controls-bar">
          <button type="button" class="primary" data-mem-action="random">🎲 Rastgele Sayfa İste</button>
          <button type="button" data-mem-action="fill">⚡ RAM'i Doldur ve Swap Zorla</button>
          <button type="button" data-mem-action="thrash">⚠️ Thrashing (Aşırı Sayfalama) Testi</button>
          <button type="button" data-mem-action="reset">🔄 Belleği Sıfırla</button>
          <div class="sim-live-metrics">
            <span>RAM Hit: <strong data-mem-hits>0</strong></span>
            <span>Page Fault: <strong data-mem-faults>0</strong></span>
            <span>Swap Sayısı: <strong data-mem-swaps>0</strong></span>
          </div>
        </div>
        <p class="sim-explainer"><strong>Mühendislik Çıkarımı:</strong> RAM dolduğunda işletim sistemi en az kullanılan sayfayı diske atar (Page Out). Eğer sürekli diske gidip gelinirse <em>Thrashing</em> oluşur ve bilgisayar kilitlenir.</p>
      </div>

      <!-- PANEL 3: HARDWARE & NETWORK PORTS LAB -->
      <div class="sim-panel" id="panel-ports" role="tabpanel" aria-labelledby="tab-ports" data-sim-panel="ports" hidden>
        <div class="sim-header">
          <div>
            <span class="eyebrow">İNTERAKTİF DENEY İSTASYONU</span>
            <h3>Donanım Portları (USB/COM) ve Mantıksal Ağ Soketleri</h3>
            <p>Fiziksel aygıt bağlantısı (USB-UART dönüştürücüler) ile TCP/IP ağ soket portları (HTTP, SSH, API) arasındaki farkı canlı deneyle öğrenin.</p>
          </div>
        </div>

        <div class="ports-dual-grid">
          <!-- SUB-COL 1: HARDWARE PORT (ESP32 / SERIAL) -->
          <div class="port-sublab">
            <div class="sublab-head">
              <h4>1. Donanım & Seri COM Port Deneyi</h4>
              <span class="sublab-tag">Fiziksel Katman</span>
            </div>
            <p class="sublab-desc">Bir ESP32 mikrodenetleyicisini USB ile bilgisayara bağlayın. PnP tespiti, sürücü eşleşmesi ve sanal COM portu oluşumunu izleyin.</p>
            
            <div class="hardware-connection-visual">
              <div class="device-card" data-device-state="disconnected">
                <div class="dev-icon">🔌</div>
                <div class="dev-info">
                  <strong data-device-title>ESP32 DevKit V1</strong>
                  <span data-device-sub>USB Bağlantısı Yok</span>
                </div>
                <button type="button" class="primary" data-port-action="toggle-usb">USB Kablosunu Tak</button>
              </div>

              <div class="os-pnp-log" data-pnp-log>
                <div class="log-line info">[Sistem] USB Denetleyici hazır, aygıt bekleniyor...</div>
              </div>

              <div class="serial-terminal" data-serial-term>
                <div class="term-header">
                  <span>Seri Monitör (<strong data-active-com>COM Kapalı</strong>)</span>
                  <div class="term-controls">
                    <select data-baud-select aria-label="Baud Hızı">
                      <option value="115200">115200 Baud</option>
                      <option value="9600">9600 Baud</option>
                    </select>
                    <button type="button" data-port-action="toggle-serial" disabled>Portu Aç</button>
                  </div>
                </div>
                <div class="term-body" data-serial-output>
                  <span class="muted">Seri port kapalı. Aygıt takıp portu açınız.</span>
                </div>
              </div>
            </div>
          </div>

          <!-- SUB-COL 2: NETWORK PORTS (TCP SOCKETS) -->
          <div class="port-sublab">
            <div class="sublab-head">
              <h4>2. Mantıksal Ağ Portları (TCP Dinleyici)</h4>
              <span class="sublab-tag">Ağ Katmanı</span>
            </div>
            <p class="sublab-desc">1-65535 arası ağ portları; gelen veri paketlerinin hangi sürece (process) ait olduğunu belirler. Soketleri açıp test istekleri gönderin.</p>

            <div class="network-ports-table-wrap">
              <table class="sim-table" aria-label="Ağ Portları Durumu">
                <thead>
                  <tr>
                    <th>Port</th>
                    <th>Servis / Protokol</th>
                    <th>Durum</th>
                    <th>İşlem</th>
                  </tr>
                </thead>
                <tbody>
                  <tr data-net-row="80">
                    <td><strong>80</strong></td>
                    <td>HTTP Web Sunucusu (Nginx/Apache)</td>
                    <td><span class="status-pill closed" data-port-state="80">CLOSED</span></td>
                    <td><button type="button" data-toggle-net="80">Servisi Başlat</button></td>
                  </tr>
                  <tr data-net-row="443">
                    <td><strong>443</strong></td>
                    <td>HTTPS Güvenli Web</td>
                    <td><span class="status-pill closed" data-port-state="443">CLOSED</span></td>
                    <td><button type="button" data-toggle-net="443">Servisi Başlat</button></td>
                  </tr>
                  <tr data-net-row="22">
                    <td><strong>22</strong></td>
                    <td>SSH Uzak Terminal Bağlantısı</td>
                    <td><span class="status-pill closed" data-port-state="22">CLOSED</span></td>
                    <td><button type="button" data-toggle-net="22">Servisi Başlat</button></td>
                  </tr>
                  <tr data-net-row="8080">
                    <td><strong>8080</strong></td>
                    <td>IoT Sıcaklık Ölçüm API Servisi</td>
                    <td><span class="status-pill closed" data-port-state="8080">CLOSED</span></td>
                    <td><button type="button" data-toggle-net="8080">Servisi Başlat</button></td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div class="client-packet-tester">
              <strong>İstemci Paketi Gönder (Soket Testi):</strong>
              <div class="packet-actions">
                <button type="button" class="primary" data-send-packet="80">HTTP GET / (Port 80)</button>
                <button type="button" data-send-packet="8080">POST /api/olcum (Port 8080)</button>
                <button type="button" data-send-packet="22">SSH Bağlantı İsteği (Port 22)</button>
              </div>
              <div class="packet-result-log" data-packet-log>
                <span class="muted">Bir servisi başlatın ve paket göndererek TCP soket el sıkışmasını (SYN-ACK) test edin.</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- PANEL 4: TASK MANAGER & DISK MAINTENANCE LAB -->
      <div class="sim-panel" id="panel-tasks-disk" role="tabpanel" aria-labelledby="tab-tasks-disk" data-sim-panel="tasks-disk" hidden>
        <div class="sim-header">
          <div>
            <span class="eyebrow">İNTERAKTİF SİSTEM BAKIM MERKEZİ</span>
            <h3>Görev Yöneticisi & Disk Bakım İstasyonu</h3>
            <p><strong>Ne işe yarar? Neden çok önemlidir?</strong> Görev Yöneticisi kilitlenen süreçleri sonlandırıp sistemin çökmesini engeller; Disk Bakımı ise bozuk sektörleri onarır, SSD TRIM ile yazma hızını ve veri bütünlüğünü korur.</p>
          </div>
        </div>

        <div class="ports-dual-grid">
          <!-- SUB-COL 1: TASK MANAGER / PROCESS CONTROL -->
          <div class="port-sublab">
            <div class="sublab-head">
              <h4>1. Canlı Görev Yöneticisi (Task Manager)</h4>
              <span class="sublab-tag">Sistem Kararlılığı</span>
            </div>
            <p class="sublab-desc">Aşağıda çalışan süreçler listelenmektedir. Kilitlenen ve aşırı bellek tüketen süreci tespit edip <strong>Görevi Sonlandır (End Task)</strong> ile sistemi kurtarın.</p>

            <div class="network-ports-table-wrap">
              <table class="sim-table" aria-label="Görev Yöneticisi Süreç Tablosu">
                <thead>
                  <tr>
                    <th>Süreç Adı</th>
                    <th>CPU</th>
                    <th>Bellek</th>
                    <th>Durum / İşlem</th>
                  </tr>
                </thead>
                <tbody data-taskmgr-body>
                  <tr data-task-row="nginx">
                    <td><strong>nginx.exe</strong><br><small>Web Sunucu</small></td>
                    <td>%2</td>
                    <td>140 MB</td>
                    <td><span class="status-pill listening">Çalışıyor</span></td>
                  </tr>
                  <tr data-task-row="esp32-service">
                    <td><strong>esp32_collector.py</strong><br><small>Sensör Servisi</small></td>
                    <td>%8</td>
                    <td>95 MB</td>
                    <td><span class="status-pill listening">Çalışıyor</span></td>
                  </tr>
                  <tr data-task-row="chrome">
                    <td><strong>chrome.exe</strong><br><small>Tarayıcı (14 Sekme)</small></td>
                    <td>%16</td>
                    <td>1.4 GB</td>
                    <td><span class="status-pill listening">Çalışıyor</span></td>
                  </tr>
                  <tr data-task-row="rogue" class="danger-row" style="background:rgba(220,38,38,0.08)">
                    <td><strong style="color:#dc2626">data_leak_script.py</strong><br><small style="color:#dc2626">⚠️ Bellek Sızıntısı & Kilitlenme!</small></td>
                    <td><strong style="color:#dc2626">%94</strong></td>
                    <td><strong style="color:#dc2626">3.8 GB</strong></td>
                    <td><button type="button" class="primary" style="background:#dc2626;border-color:#dc2626;color:#fff" data-task-action="kill-rogue">Görevi Sonlandır (kill -9)</button></td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div class="packet-result-log" data-taskmgr-log>
              <span class="muted">Görev yöneticisindeki 'data_leak_script.py' süreci CPU'nun %94'ünü sömürüyor. 'Görevi Sonlandır' butonuna basarak RAM'i kurtarın.</span>
            </div>
          </div>

          <!-- SUB-COL 2: DISK MAINTENANCE & SSD TRIM -->
          <div class="port-sublab">
            <div class="sublab-head">
              <h4>2. Disk Bakımı, TRIM & Sağlık İstasyonu</h4>
              <span class="sublab-tag">Depolama Güvenliği</span>
            </div>
            <p class="sublab-desc">Disk bakımı; dosya sistemi çökmelerini önler (chkdsk), SSD ömrünü ve yazma hızını uzatır (TRIM), disk doluluğunu temizler (cleanmgr).</p>

            <div class="disk-health-card">
              <div class="disk-meta" style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:8px">
                <strong>Yerel Disk (C:) · NVMe SSD 512 GB</strong>
                <span data-disk-space-text>440 GB / 512 GB (%86 Dolu)</span>
              </div>
              <div class="core-meter" style="height:14px;margin-bottom:12px">
                <div class="meter-bar" data-disk-bar style="width:86%;background:#d97706"></div>
              </div>

              <div class="disk-smart-badges" style="display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap">
                <span class="sim-stats-badge">Sağlık Durumu (SMART): <strong style="color:#24705b" data-smart-health>%98 Mükemmel</strong></span>
                <span class="sim-stats-badge">Sıcaklık: <strong data-smart-temp>36 °C</strong></span>
                <span class="sim-stats-badge">Gereksiz Geçici Dosya: <strong data-temp-files>18.4 GB</strong></span>
              </div>

              <div class="packet-actions" style="margin-bottom:12px">
                <button type="button" data-disk-action="chkdsk">🔍 Dosya Bütünlüğü (chkdsk / fsck)</button>
                <button type="button" class="primary" data-disk-action="trim">⚡ SSD TRIM Optimizasyonu</button>
                <button type="button" data-disk-action="clean">🧹 Gereksiz Dosyaları Temizle</button>
              </div>

              <div class="packet-result-log" data-disk-log>
                <span class="muted">Bir bakım aracı seçerek disk sağlığını koruyun ve performansını artırın.</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>'''
