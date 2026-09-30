/**
 * Network Architecture & Interactive Simulation Lab (Week 4)
 * Vanilla JavaScript - Zero External Dependencies
 */
(function() {
  'use strict';

  document.addEventListener('DOMContentLoaded', function() {
    initNetArch();
    initNetLabTabs();
    initProtoSubnav();
    initDnsSim();
    initDhcpSim();
    initNatSim();
    initWebVsNetSim();
    initWebServerSim();
    initTechStackSim();
    initInteractiveQuiz();
  });

  /* ----------------------------------------------------
   * 1. Architecture Explorer
   * ---------------------------------------------------- */
  function initNetArch() {
    const explorer = document.querySelector('[data-net-arch]');
    if (!explorer) return;

    const nodes = explorer.querySelectorAll('.net-arch-node');
    const titleEl = explorer.querySelector('[data-net-title]');
    const enEl = explorer.querySelector('[data-net-en]');
    const descEl = explorer.querySelector('[data-net-desc]');
    const protoEl = explorer.querySelector('[data-net-proto]');
    const stackEl = explorer.querySelector('[data-net-stack]');
    const roleEl = explorer.querySelector('[data-net-role]');

    nodes.forEach(function(node) {
      node.addEventListener('click', function() {
        nodes.forEach(function(n) { n.setAttribute('aria-pressed', 'false'); });
        node.setAttribute('aria-pressed', 'true');

        if (titleEl) titleEl.textContent = node.dataset.title;
        if (enEl) enEl.textContent = node.dataset.en;
        if (descEl) descEl.textContent = node.dataset.desc;
        if (protoEl) protoEl.textContent = node.dataset.proto;
        if (stackEl) stackEl.textContent = node.dataset.stack;
        if (roleEl) roleEl.textContent = node.dataset.role;
      });
    });
  }

  /* ----------------------------------------------------
   * 2. Tabs Management
   * ---------------------------------------------------- */
  function initNetLabTabs() {
    const lab = document.querySelector('[data-net-lab]');
    if (!lab) return;

    const tabs = lab.querySelectorAll('[data-net-tab]');
    const panels = lab.querySelectorAll('[data-net-panel]');

    tabs.forEach(function(tab) {
      tab.addEventListener('click', function() {
        const target = tab.dataset.netTab;

        tabs.forEach(function(t) {
          t.setAttribute('aria-selected', t === tab ? 'true' : 'false');
        });

        panels.forEach(function(panel) {
          if (panel.dataset.netPanel === target) {
            panel.removeAttribute('hidden');
          } else {
            panel.setAttribute('hidden', '');
          }
        });
      });
    });
  }

  /* ----------------------------------------------------
   * 2b. Protocol Sub-navigation (DNS / DHCP / NAT)
   * ---------------------------------------------------- */
  function initProtoSubnav() {
    const nav = document.querySelector('.proto-subnav');
    if (!nav) return;
    const btns = nav.querySelectorAll('.subnav-btn');
    const views = document.querySelectorAll('.subproto-view');

    btns.forEach(function(btn) {
      btn.addEventListener('click', function() {
        const target = btn.dataset.subproto;
        btns.forEach(function(b) { b.classList.remove('active'); });
        btn.classList.add('active');

        views.forEach(function(view) {
          if (view.dataset.subprotoView === target) {
            view.removeAttribute('hidden');
          } else {
            view.setAttribute('hidden', '');
          }
        });
      });
    });
  }

  /* ----------------------------------------------------
   * 2c. DHCP (DORA) Simulation
   * ---------------------------------------------------- */
  function initDhcpSim() {
    const startBtn = document.querySelector('[data-net-action="start-dhcp"]');
    const releaseBtn = document.querySelector('[data-net-action="release-dhcp"]');
    if (!startBtn) return;

    const cards = document.querySelectorAll('.dora-card');
    const logEl = document.querySelector('[data-dhcp-log]');
    let isRunning = false;

    startBtn.addEventListener('click', function() {
      if (isRunning) return;
      isRunning = true;
      startBtn.disabled = true;

      cards.forEach(function(c) {
        c.classList.remove('active-step', 'done-step');
        const st = c.querySelector('.dora-status');
        if (st) st.textContent = 'Bekliyor...';
      });

      // 1. Discover
      cards[0].classList.add('active-step');
      cards[0].querySelector('.dora-status').textContent = 'Broadcast Gönderiliyor...';
      logEl.innerHTML = '📢 <strong>1. Discover:</strong> İstemci henüz bir IP adresine sahip olmadığı için (0.0.0.0), yerel ağdaki herkese <code>255.255.255.255:67 UDP</code> adresine <em>"Ağda IP dağıtacak DHCP sunucusu var mı?"</em> paketi yayınladı.';

      setTimeout(function() {
        cards[0].classList.remove('active-step');
        cards[0].classList.add('done-step');
        cards[0].querySelector('.dora-status').textContent = 'Tamamlandı';

        // 2. Offer
        cards[1].classList.add('active-step');
        cards[1].querySelector('.dora-status').textContent = 'Teklif Geldi';
        logEl.innerHTML = '🎁 <strong>2. Offer:</strong> Yönlendirici DHCP servisi (192.168.1.1:67), cihazın MAC adresine özel boş bir IP önerdi: <code>192.168.1.105</code> (Alt Ağ Maskesi: <code>255.255.255.0</code>).';
      }, 900);

      setTimeout(function() {
        cards[1].classList.remove('active-step');
        cards[1].classList.add('done-step');
        cards[1].querySelector('.dora-status').textContent = 'Tamamlandı';

        // 3. Request
        cards[2].classList.add('active-step');
        cards[2].querySelector('.dora-status').textContent = 'İstek İletildi';
        logEl.innerHTML = '✍️ <strong>3. Request:</strong> İstemci teklifi kabul etti: <em>"192.168.1.105 nolu IP adresini üzerime tahsis etmeni talep ediyorum."</em>';
      }, 1800);

      setTimeout(function() {
        cards[2].classList.remove('active-step');
        cards[2].classList.add('done-step');
        cards[2].querySelector('.dora-status').textContent = 'Tamamlandı';

        // 4. ACK
        cards[3].classList.add('active-step');
        cards[3].classList.add('done-step');
        cards[3].querySelector('.dora-status').textContent = 'Kiralandı (24 Saat)';
        logEl.innerHTML = '✅ <strong>4. Acknowledge (Kira Onayı):</strong> DHCP sunucusu işlemi onayladı! Parametreler cihaza yüklendi:<br>' +
                          '• Atanan Yerel IP: <code>192.168.1.105</code><br>' +
                          '• Varsayılan Ağ Geçidi (Router): <code>192.168.1.1</code><br>' +
                          '• DNS Sunucusu: <code>195.175.39.39</code><br>' +
                          '• Kira Süresi (Lease Time): <strong>86400 saniye (24 saat)</strong>';
        isRunning = false;
        startBtn.disabled = false;
      }, 2700);
    });

    if (releaseBtn) {
      releaseBtn.addEventListener('click', function() {
        cards.forEach(function(c) {
          c.classList.remove('active-step', 'done-step');
          const st = c.querySelector('.dora-status');
          if (st) st.textContent = 'IP Bırakıldı';
        });
        logEl.innerHTML = '🔌 <strong>ipconfig /release simülasyonu:</strong> İstemci yönlendiriciye kiraladığı IP adresini iade etti. Cihazın IP adresi <code>0.0.0.0</code> oldu ve ağ bağlantısı durduruldu. Yeniden bağlanmak için <code>ipconfig /renew</code> yapılmalıdır.';
      });
    }
  }

  /* ----------------------------------------------------
   * 2d. NAT / PAT Simulation
   * ---------------------------------------------------- */
  function initNatSim() {
    const sendBtn = document.querySelector('[data-net-action="send-nat-packet"]');
    const clearBtn = document.querySelector('[data-net-action="clear-nat"]');
    const tbody = document.querySelector('[data-nat-tbody]');
    const logEl = document.querySelector('[data-nat-log]');
    if (!sendBtn || !tbody) return;

    const SAMPLES = [
      { name: 'ESP32 Sıcaklık Sensörü', priv: '192.168.1.88:4102', nat: '212.58.244.70:52112', dest: '193.255.140.18:80 (ÇOMÜ API)', proto: 'HTTP/TCP' },
      { name: 'Akıllı TV (Oturma Odası)', priv: '192.168.1.45:38291', nat: '212.58.244.70:52113', dest: '142.250.187.174:443 (YouTube)', proto: 'HTTPS/TCP' },
      { name: 'Mobil Tablet', priv: '192.168.1.33:49811', nat: '212.58.244.70:52114', dest: '185.15.59.224:443 (Wikipedia)', proto: 'HTTPS/TCP' }
    ];

    let sampleIdx = 0;

    sendBtn.addEventListener('click', function() {
      const item = SAMPLES[sampleIdx % SAMPLES.length];
      sampleIdx++;

      const tr = document.createElement('tr');
      tr.innerHTML = '<td>' + item.name + '</td>' +
                     '<td><code>' + item.priv + '</code></td>' +
                     '<td><code>' + item.nat + '</code></td>' +
                     '<td><code>' + item.dest + '</code></td>' +
                     '<td><span class="proto-tag">' + item.proto + '</span></td>';
      tbody.appendChild(tr);

      logEl.innerHTML = '🔄 <strong>NAT & PAT Çevirisi Gerçekleşti:</strong><br>' +
                        '1. <strong>' + item.name + '</strong> yerel IP\'sinden (<code>' + item.priv + '</code>) dış hedef sunucuya (<code>' + item.dest + '</code>) paket yolladı.<br>' +
                        '2. Yönlendirici paketteki yerel özel IP\'yi internete doğrudan çıkaramaz.<br>' +
                        '3. Paketin kaynak adresini kendi Genel IP\'si ve benzersiz bir dış portla (<code>' + item.nat + '</code>) değiştirdi ve NAT tablosuna kaydetti.<br>' +
                        '4. Dış sunucudan bu genel porta gelen paketler doğrudan ' + item.name + '\'ne iletilecektir!';
    });

    if (clearBtn) {
      clearBtn.addEventListener('click', function() {
        tbody.innerHTML = '<tr><td>Öğrenci Laptop</td><td><code>192.168.1.15:49152</code></td><td><code>212.58.244.70:52110</code></td><td><code>193.255.140.18:443 (ÇOMÜ Web)</code></td><td><span class="proto-tag">HTTPS/TCP</span></td></tr>';
        logEl.innerHTML = '🧹 <strong>NAT Tablosu Sıfırlandı:</strong> Eski aktif oturum kayıtları temizlendi.';
      });
    }
  }

  /* ----------------------------------------------------
   * 3. DNS & Packet Traceroute Simulation
   * ---------------------------------------------------- */
  function initDnsSim() {
    const startBtn = document.querySelector('[data-net-action="start-dns"]');
    if (!startBtn) return;

    const selectEl = document.querySelector('[data-dns-select]');
    const stages = document.querySelectorAll('.dns-stage');
    const resolvedIpEl = document.querySelector('[data-resolved-ip]');
    const hopsListEl = document.querySelector('[data-hops-list]');
    const logEl = document.querySelector('[data-dns-log]');

    const DOMAIN_DATA = {
      'comu.edu.tr': {
        ip: '193.255.140.18',
        tld: '.tr TLD Name Server (nic.tr / BTK)',
        auth: 'ns1.comu.edu.tr (Çanakkale Onsekiz Mart Üniv.)',
        hops: [
          { ip: '192.168.1.1', name: 'Yerel Ağ Ağ Geçidi (Modem / Router)', latency: '1 ms' },
          { ip: '195.175.39.39', name: 'Türk Telekom Omurga Ağ Geçidi (ISP BGP)', latency: '8 ms' },
          { ip: '193.140.83.1', name: 'ULAKBİM Ulusal Akademik Ağ Omurgası', latency: '14 ms' },
          { ip: '193.255.140.18', name: 'ÇOMÜ Veri Merkezi Nginx Web Sunucusu', latency: '19 ms' }
        ]
      },
      'github.com': {
        ip: '140.82.121.4',
        tld: '.com VeriSign Global TLD Server',
        auth: 'ns-1707.awsdns-21.co.uk (GitHub DNS)',
        hops: [
          { ip: '192.168.1.1', name: 'Yerel Ağ Ağ Geçidi (Router)', latency: '1 ms' },
          { ip: '212.156.120.1', name: 'ISP Uluslararası Çıkış Yönlendiricisi', latency: '12 ms' },
          { ip: '62.115.114.89', name: 'Telia Carrier Frankfurt Sualtı Fiber Hattı', latency: '42 ms' },
          { ip: '140.82.121.4', name: 'GitHub Anycast Edge Server (Frankfurt)', latency: '46 ms' }
        ]
      },
      'wikipedia.org': {
        ip: '185.15.59.224',
        tld: '.org PIR TLD Name Server',
        auth: 'ns0.wikimedia.org (Wikimedia Foundation)',
        hops: [
          { ip: '192.168.1.1', name: 'Yerel Gateway', latency: '1 ms' },
          { ip: '195.175.51.10', name: 'ISP Şehir İçi Fiber Dağıtım Noktası', latency: '9 ms' },
          { ip: '80.249.208.34', name: 'AMS-IX Amsterdam İnternet Değişim Noktası', latency: '38 ms' },
          { ip: '185.15.59.224', name: 'Wikimedia CDN Caching Server', latency: '41 ms' }
        ]
      }
    };

    let isRunning = false;

    startBtn.addEventListener('click', function() {
      if (isRunning) return;
      isRunning = true;
      startBtn.disabled = true;

      const domain = selectEl.value;
      const data = DOMAIN_DATA[domain] || DOMAIN_DATA['comu.edu.tr'];

      stages.forEach(function(s) {
        s.classList.remove('active-stage', 'resolved-stage');
      });
      resolvedIpEl.textContent = 'Çözümleniyor...';
      hopsListEl.innerHTML = '';
      logEl.innerHTML = '<strong>DNS Aşaması 1/5:</strong> Tarayıcı ve işletim sistemi DNS önbelleği kontrol ediliyor (Cache Miss)...';

      // Step 1: Cache
      stages[0].classList.add('active-stage');

      setTimeout(function() {
        stages[0].classList.remove('active-stage');
        stages[0].classList.add('resolved-stage');
        stages[1].classList.add('active-stage');
        logEl.innerHTML = '<strong>DNS Aşaması 2/5:</strong> ISS Resolver sunucusuna (Port 53 UDP) istek yapıldı. Önbellekte yok, Kök DNS aranıyor...';
      }, 700);

      // Step 2: Resolver to Root
      setTimeout(function() {
        stages[1].classList.remove('active-stage');
        stages[1].classList.add('resolved-stage');
        stages[2].classList.add('active-stage');
        logEl.innerHTML = '<strong>DNS Aşaması 3/5:</strong> Dünyadaki 13 Kök DNS kümesinden birine soruldu. Kök sunucu: <em>"Ben IP bilmiyorum ama ' + domain.split('.').pop() + ' TLD sunucusuna git!"</em> dedi.';
      }, 1500);

      // Step 3: TLD
      setTimeout(function() {
        stages[2].classList.remove('active-stage');
        stages[2].classList.add('resolved-stage');
        stages[3].classList.add('active-stage');
        logEl.innerHTML = '<strong>DNS Aşaması 4/5:</strong> ' + data.tld + ' sorgulandı. TLD sunucu: <em>"Bu alan adının yetkili sunucusu ' + data.auth + '"</em> yanıtını döndü.';
      }, 2300);

      // Step 4: Auth
      setTimeout(function() {
        stages[3].classList.remove('active-stage');
        stages[3].classList.add('resolved-stage');
        stages[4].classList.add('active-stage');
        logEl.innerHTML = '<strong>DNS Aşaması 5/5:</strong> Yetkili DNS sunucusu <strong>A Kaydını</strong> doğruladı: <code>' + domain + ' → ' + data.ip + '</code>. IP adresi tarayıcıya teslim edildi!';
        resolvedIpEl.textContent = data.ip;
      }, 3100);

      // Step 5: Start Traceroute Packet Journey
      setTimeout(function() {
        stages[4].classList.remove('active-stage');
        stages[4].classList.add('resolved-stage');
        logEl.innerHTML = '<strong>TCP/IP Paket İletimi:</strong> IP adresi elde edildi. Şimdi TCP 3-Way Handshake için yönlendirici atlamaları (Routing Hops) başlatılıyor:';

        data.hops.forEach(function(hop, idx) {
          setTimeout(function() {
            const hopDiv = document.createElement('div');
            hopDiv.className = 'hop-item';
            hopDiv.innerHTML = '<span class="hop-num">Hop ' + (idx + 1) + '</span>' +
                               '<code>' + hop.ip + '</code>' +
                               '<span>' + hop.name + '</span>' +
                               '<span class="hop-latency">' + hop.latency + '</span>';
            hopsListEl.appendChild(hopDiv);

            if (idx === data.hops.length - 1) {
              logEl.innerHTML += '<br>✅ <strong>Bağlantı Kuruldu:</strong> HTTP/HTTPS (Port 443) üzerinden Nginx/Apache sunucusuyla TLS el sıkışması tamamlandı!';
              isRunning = false;
              startBtn.disabled = false;
            }
          }, (idx + 1) * 600);
        });
      }, 3800);
    });
  }

  /* ----------------------------------------------------
   * 4. Web vs Internet Simulation
   * ---------------------------------------------------- */
  function initWebVsNetSim() {
    const container = document.querySelector('[data-net-panel="web-vs-net"]');
    if (!container) return;

    const vehicles = container.querySelectorAll('.service-vehicle');
    const logEl = container.querySelector('[data-web-vs-net-log]');

    vehicles.forEach(function(veh) {
      const btn = veh.querySelector('button');
      const service = veh.dataset.service;

      btn.addEventListener('click', function() {
        const isActive = veh.classList.contains('active');
        if (isActive) {
          veh.classList.remove('active');
          veh.classList.add('disabled');
          btn.textContent = 'Servisi Yeniden Başlat';
        } else {
          veh.classList.remove('disabled');
          veh.classList.add('active');
          const names = { web: 'Web Servisi', mail: 'E-Posta', ssh: 'SSH Terminal', iot: 'IoT Telemetri' };
          btn.textContent = (names[service] || 'Servisi') + ' Kapat';
        }

        updateHighwayLog();
      });
    });

    function updateHighwayLog() {
      const webActive = container.querySelector('[data-service="web"]').classList.contains('active');
      const mailActive = container.querySelector('[data-service="mail"]').classList.contains('active');
      const sshActive = container.querySelector('[data-service="ssh"]').classList.contains('active');
      const iotActive = container.querySelector('[data-service="iot"]').classList.contains('active');

      if (!webActive && (mailActive || sshActive || iotActive)) {
        logEl.innerHTML = '🎯 <strong>Önemli Ayrım Gözlendi:</strong> Web servisi (HTTP/Port 80-443) tamamen kapalı! Tarayıcıda hiçbir web sitesi açılmaz. <strong>Ancak İnternet altyapısı çalışıyor:</strong> E-postalarınız (SMTP), sunucu yönetiminiz (SSH) ve ESP32 sensör verileriniz (MQTT) kesintisiz akmaya devam ediyor. Bu durum, <em>Web ile İnternetin aynı şey olmadığını</em> kanıtlar!';
      } else if (!webActive && !mailActive && !sshActive && !iotActive) {
        logEl.innerHTML = '⚠️ <strong>Tüm Uygulama Servisleri Kapalı:</strong> Ancak kablolar, uydular ve yönlendiriciler (IP Altyapısı) hala ayakta! Sadece üzerinde çalışan aplikasyon protokolleri durduruldu.';
      } else if (webActive && !mailActive) {
        logEl.innerHTML = 'ℹ️ Web çalışıyor (siteler açık), ancak e-posta altyapısı durduruldu. Servisler birbirinden bağımsız çalışır.';
      } else {
        logEl.innerHTML = '<strong>Mühendislik Çıkarımı:</strong> Web (HTTP/HTTPS) kapalı olsa bile internet altyapısı çalışmaya devam eder; e-postalar gitmeye, SSH terminalleri bağlanmaya ve ESP32 sensörleri MQTT ile veri basmaya devam edebilir!';
      }
    }
  }

  /* ----------------------------------------------------
   * 5. Web Server Simulation (Static vs Dynamic)
   * ---------------------------------------------------- */
  function initWebServerSim() {
    const panel = document.querySelector('[data-net-panel="web-server"]');
    if (!panel) return;

    const btns = panel.querySelectorAll('[data-server-test]');
    const logEl = panel.querySelector('[data-server-log]');
    const clientBox = panel.querySelector('.client-box');
    const serverBox = panel.querySelector('.server-box');
    const backendBox = panel.querySelector('.backend-box');
    const reqArrow = panel.querySelector('[data-flow-arrow-req]');
    const backendArrow = panel.querySelector('[data-flow-arrow-backend]');

    btns.forEach(function(btn) {
      btn.addEventListener('click', function() {
        const type = btn.dataset.serverTest;
        runServerRequest(type);
      });
    });

    function resetVisuals() {
      clientBox.classList.remove('active-pulse');
      serverBox.classList.remove('active-pulse');
      backendBox.classList.remove('active-pulse');
      reqArrow.classList.remove('active-stream');
      backendArrow.classList.remove('active-stream');
    }

    function runServerRequest(type) {
      resetVisuals();
      clientBox.classList.add('active-pulse');
      reqArrow.classList.add('active-stream');

      if (type === 'static') {
        logEl.innerHTML = '📤 <strong>1. İstemci İsteği:</strong> <code>GET /index.html HTTP/1.1</code> → Nginx (Port 80/443)';
        setTimeout(function() {
          serverBox.classList.add('active-pulse');
          logEl.innerHTML = '⚡ <strong>2. Web Sunucusu (Nginx):</strong> Dosya uzantısını kontrol etti (.html / .css). Doğrudan Linux/Windows diskinden (DocumentRoot) okudu.<br>' +
                            '📥 <strong>HTTP Yanıtı:</strong> <code>200 OK</code> · Content-Type: <code>text/html</code> · Süre: <strong>1.4 ms</strong> (Ultra Hızlı - Backend/PHP çalıştırılmadı!)';
        }, 500);
      } else if (type === 'dynamic') {
        logEl.innerHTML = '📤 <strong>1. İstemci İsteği:</strong> <code>POST /api/kaydet.php</code> (Sensör JSON Verisi: <code>{"sicaklik": 23.4}</code>)';
        setTimeout(function() {
          serverBox.classList.add('active-pulse');
          backendArrow.classList.add('active-stream');
          logEl.innerHTML = '⚙️ <strong>2. Nginx Yönlendirmesi:</strong> İstek <code>.php</code> uzantılı olduğu için Nginx bunu doğrudan sunamaz. FastCGI soketi üzerinden <strong>PHP-FPM motoruna</strong> aktardı...';
        }, 600);

        setTimeout(function() {
          backendBox.classList.add('active-pulse');
          logEl.innerHTML = '💾 <strong>3. Backend & SQL:</strong> PHP betiği çalıştı, JSON verisini doğruladı, MySQL veritabanına <code>INSERT INTO sensor_logs</code> yaptı.<br>' +
                            '📥 <strong>HTTP Yanıtı:</strong> <code>201 Created</code> · JSON: <code>{"durum": "kaydedildi", "id": 1042}</code> · Süre: <strong>38.6 ms</strong> (Dinamik derleme ve DB sorgusu yapıldı)';
        }, 1300);
      } else if (type === '404') {
        logEl.innerHTML = '📤 <strong>1. İstemci İsteği:</strong> <code>GET /olmayan_sayfa.html</code>';
        setTimeout(function() {
          serverBox.classList.add('active-pulse');
          logEl.innerHTML = '❌ <strong>2. Web Sunucusu:</strong> Diskte belirtilen dosya bulunamadı.<br>' +
                            '📥 <strong>HTTP Yanıtı:</strong> <code>404 Not Found</code> · Web sunucusu istemciye hata sayfasını iletti. Süre: <strong>1.1 ms</strong>';
        }, 500);
      }
    }
  }

  /* ----------------------------------------------------
   * 6. Web Technology Stack Explorer
   * ---------------------------------------------------- */
  function initTechStackSim() {
    const panel = document.querySelector('[data-net-panel="tech-stack"]');
    if (!panel) return;

    const buttons = panel.querySelectorAll('.tech-btn');
    const roleEl = panel.querySelector('[data-tech-role]');
    const titleEl = panel.querySelector('[data-tech-title]');
    const envEl = panel.querySelector('[data-tech-env]');
    const descEl = panel.querySelector('[data-tech-desc]');
    const codeEl = panel.querySelector('[data-tech-code]');

    const TECH_DATA = {
      html: {
        role: 'FRONTEND YAPITAŞI',
        title: 'HTML5 (HyperText Markup Language)',
        env: 'Tarayıcıda Çalışır (İstemci)',
        desc: 'Web sayfalarının iskeletini ve anlamsal yapısını oluşturur. Tüm başlıklar, formlar, paragraflar ve butonlar HTML ile tanımlanır.',
        code: '<!DOCTYPE html>\n<html>\n  <head><title>IoT Paneli</title></head>\n  <body>\n    <h1>Sensör İzleme</h1>\n    <button id="okuBtn">Veri Oku</button>\n  </body>\n</html>'
      },
      css: {
        role: 'GÖRSEL STİL & DÜZEN',
        title: 'CSS3 (Cascading Style Sheets)',
        env: 'Tarayıcıda Çalışır (İstemci)',
        desc: 'HTML elemanlarının renk, tipografi, grid/flexbox yerleşimi, karanlık mod ve responsive (mobil uyumlu) tasarımını sağlar.',
        code: '.sensor-card {\n  background: #ffffff;\n  border-radius: 12px;\n  padding: 16px;\n  box-shadow: 0 4px 12px rgba(0,0,0,0.08);\n  display: flex;\n  justify-content: space-between;\n}'
      },
      js: {
        role: 'DİNAMİK ETKİLEŞİM & MANTIK',
        title: 'JavaScript (ECMAScript 6+)',
        env: 'Tarayıcı & Sunucuda Çalışır',
        desc: 'Sayfa yenilenmeden arka planda API çağrıları (Fetch / AJAX), DOM manipülasyonu ve kullanıcı etkileşimlerini yönetir.',
        code: 'async function veriGetir() {\n  const res = await fetch(\'/api/sensor-data\');\n  const data = await res.json();\n  document.getElementById(\'temp\').textContent = `${data.sicaklik} °C`;\n}'
      },
      react: {
        role: 'MODERN BİLEŞEN KÜTÜPHANESİ',
        title: 'React (Meta / Facebook)',
        env: 'Frontend UI Kütüphanesi',
        desc: 'Bileşen tabanlı (Component-based) mimari ve Virtual DOM ile ultra hızlı, tek sayfalı (SPA) modern web arayüzleri geliştirilmesini sağlar.',
        code: 'function SensorWidget({ degeri }) {\n  return (\n    <div className="badge">\n      <h3>Sıcaklık</h3>\n      <span>{degeri} °C</span>\n    </div>\n  );\n}'
      },
      php: {
        role: 'SUNUCU TARAFLI BETİK DİLİ',
        title: 'PHP (Hypertext Preprocessor)',
        env: 'Sunucuda Çalışır (XAMPP / Linux FPM)',
        desc: 'Web dünyasının %75\'ini (WordPress, Laravel vb.) çalıştıran, MySQL ile en kolay entegre olan sunucu taraflı dildir.',
        code: '<?php\n$sicaklik = $_POST[\'sicaklik\'] ?? 0;\n$db = new PDO(\'mysql:host=localhost;dbname=iot\', \'root\', \'\');\n$stmt = $db->prepare(\'INSERT INTO olcum (deger) VALUES (?)\');\n$stmt->execute([$sicaklik]);\necho json_encode([\'durum\' => \'kaydedildi\']);\n?>'
      },
      python: {
        role: 'GÜÇLÜ & TEMİZ SUNUCU BACKEND',
        title: 'Python (Flask / FastAPI / Django)',
        env: 'Sunucuda Çalışır (WSGI / ASGI)',
        desc: 'Veri bilimi, yapay zeka ve IoT API sunucuları için dünyada en çok tercih edilen, son derece okunabilir backend dilidir.',
        code: 'from flask import Flask, request, jsonify\napp = Flask(__name__)\n\n@app.route(\'/api/olcum\', methods=[\'POST\'])\ndef kaydet():\n    veri = request.get_json()\n    return jsonify({"mesaj": "Kaydedildi", "deger": veri["sicaklik"]}), 201'
      },
      node: {
        role: 'ASENKRON JAVASCRIPT SUNUCUSU',
        title: 'Node.js (V8 Motoru)',
        env: 'Sunucuda Çalışır (Event-Driven)',
        desc: 'JavaScript\'i tarayıcı dışına çıkarıp sunucuda çalıştırır. Asenkron I/O mimarisi sayesinde anlık mesajlaşma ve IoT socket bağlantılarında çok hızlıdır.',
        code: 'const http = require(\'http\');\n\nconst server = http.createServer((req, res) => {\n  res.writeHead(200, { \'Content-Type\': \'application/json\' });\n  res.end(JSON.stringify({ status: \'online\', uptime: process.uptime() }));\n});\nserver.listen(3000);'
      },
      java: {
        role: 'KURUMSAL & YÜKSEK GÜVENLİKLİ',
        title: 'Java (Spring Boot)',
        env: 'Sunucuda JVM Üzerinde Çalışır',
        desc: 'Bankacılık, büyük ölçekli kurumsal sistemler ve mikroservis mimarilerinde sıkı tip güvenliği ve yüksek performansıyla tercih edilir.',
        code: '@RestController\n@RequestMapping("/api")\npublic class SensorController {\n    @GetMapping("/durum")\n    public SensorData getStatus() {\n        return new SensorData("Aktif", 24.5);\n    }\n}'
      },
      asp: {
        role: 'YÜKSEK PERFORMANSLI MICROSOFT STACK',
        title: 'ASP.NET Core (C#)',
        env: 'Kestrel / IIS / Linux Üzerinde Çalışır',
        desc: 'Microsoft tarafından açık kaynak ve platformlar arası hale getirilen, dünyanın en hızlı web backend çerçevelerinden biridir.',
        code: '[ApiController]\n[Route("api/[controller]")]\npublic class OlcumController : ControllerBase {\n    [HttpPost]\n    public IActionResult Kaydet([FromBody] OlcumModel model) {\n        return Ok(new { sonuc = "Basarili", id = 1 });\n    }\n}'
      }
    };

    buttons.forEach(function(btn) {
      btn.addEventListener('click', function() {
        buttons.forEach(function(b) { b.classList.remove('active'); });
        btn.classList.add('active');

        const key = btn.dataset.tech;
        const data = TECH_DATA[key];
        if (!data) return;

        if (roleEl) roleEl.textContent = data.role;
        if (titleEl) titleEl.textContent = data.title;
        if (envEl) envEl.textContent = data.env;
        if (descEl) descEl.textContent = data.desc;
        if (codeEl) codeEl.textContent = data.code;
      });
    });
  }

  /* ----------------------------------------------------
   * 7. Interactive Engineering Assessment (10 Questions)
   * ---------------------------------------------------- */
  function initInteractiveQuiz() {
    const container = document.querySelector('[data-quiz-lab]');
    if (!container) return;

    const cards = container.querySelectorAll('.quiz-q-card');
    const scoreDisplay = container.querySelector('[data-score-display]');
    const checkAllBtn = container.querySelector('[data-action="check-all-quiz"]');
    const resetBtn = container.querySelector('[data-action="reset-quiz"]');

    const EXPLANATIONS = {
      1: {
        correct: 'Tebrikler! DHCP kiralama süreci tam olarak DORA (Discover → Offer → Request → Acknowledge) sırasıyla işler: İstemci önce arama yayını yapar, sunucu boş IP teklif eder, istemci onay ister, sunucu kira parametrelerini onaylar.',
        wrong: 'Hatalı sıralama! DHCP süreci D-O-R-A akrostişi ile hatırlanır: 1. Discover (Keşif), 2. Offer (Teklif), 3. Request (İstek), 4. ACK (Onay).'
      },
      2: {
        correct: 'Doğru! NAT (PAT - Port Address Translation), yerel cihazın Özel IP (Private IP) adresini siler; yerine yönlendiricinin tek Genel IP (Public IP) adresini ve benzersiz dinamik bir dış portu eşleyerek paket başlığını değiştirir.',
        wrong: 'Hatalı! NAT hedef adresi değiştirmez, kaynak Özel IP adresini yönlendiricinin Genel IP\'si ve dinamik bir port ile değiştirerek iç ağı dış dünyadan izole eder.'
      },
      3: {
        correct: 'Harika analiz! DNS hiyerarşisi ters ağaç yapısındadır: Yerel önbellekte yoksa ISS Resolver önce dünyadaki 13 Kök Ad Sunucusuna (.), ardından üst düzey alan (.tr) TLD sunucusuna, en son alan adından sorumlu Yetkili Sunucuya (ns1.comu.edu.tr) gider.',
        wrong: 'Hatalı! DNS çözümlemesi hiyerarşik aşağıdan yukarı değil, Kök (.) → TLD (.tr) → Yetkili Sunucu (Authoritative) sırasıyla yürütülür.'
      },
      4: {
        correct: 'Tebrikler! Web (Port 80/443 HTTP/HTTPS) kapalı olsa bile İnternet altyapısı çalışır; Port 22 SSH uzak yönetimi ve Port 1883 MQTT telemetrisi bağımsız IP protokolleri olarak çalışmaya devam eder.',
        wrong: 'Hatalı! Port 80 ve 443 Web (HTTP/HTTPS) servisleridir. REST API ve web siteleri bu portları kullandığı için durur; ancak SSH (Port 22) ve MQTT (Port 1883) internet üzerinde kesintisiz çalışır.'
      },
      5: {
        correct: 'Doğru! Nginx, her bağlantı için yeni bir süreç/thread açmak yerine tek bir işlemde asenkron (non-blocking event-driven) epoll mimarisi kullandığından çok düşük bellekle on binlerce eşzamanlı bağlantıyı yönetir.',
        wrong: 'Hatalı! Apache prefork her bağlantı için yeni süreç açarak yüksek belleğe yol açar. Olay güdümlü asenkron yapı Nginx\'in temel gücüdür.'
      },
      6: {
        correct: 'Eksiksiz eşleştirme! Web 1.0 salt okunur statik HTML çağıdır; Web 2.0 AJAX ve sosyal ağlarla okur-yazar katılımcı webdir; Web 3.0 ise semantik veri, Wasm ve yapay zekâ entegrasyonudur.',
        wrong: 'Eşleştirme eksik veya hatalı! Web 1.0 (Salt Okunur), Web 2.0 (AJAX & Sosyal), Web 3.0 (Semantik Ağ & Yapay Zekâ) olmalıdır.'
      },
      7: {
        correct: 'Mükemmel teşhis! PHP/Python motoru çöktüğünde Nginx 502 Bad Gateway döner; bulunamayan kaynak 404 Not Found\'dur; yeni bir kaynak başarıyla oluşturulduğunda REST API standardı 201 Created döndürür.',
        wrong: 'Durum kodları hatalı! Backend motoru ile iletişim kopuksa 502 Bad Gateway, dosya yoksa 404 Not Found, yeni veri eklenmişse 201 Created döner.'
      },
      8: {
        correct: 'Doğru! PHP ve Python backend dilleri olup sunucuda çalışır ve dinamik çıktı üretir; HTML, CSS ve JavaScript/React ise kullanıcının tarayıcısında (Client DOM) yorumlanır.',
        wrong: 'Hatalı! PHP veya Python asla doğrudan tarayıcıya indirilip Chrome\'da çalıştırılmaz; sunucu üzerinde derlenip istemciye salt HTML/JSON gönderilir.'
      },
      9: {
        correct: 'Kesinlikle doğru! Tim Berners-Lee 1994\'te W3C\'yi kurarak web standartlarının açık, patentsiz ve herkes için ücretsiz bir küresel kamu malı olarak kalmasını sağlamıştır.',
        wrong: 'Hatalı! Tim Berners-Lee web standartlarını satmamış; tam aksine patentsiz ve kamu malı kalması için W3C\'yi kurmuştur.'
      },
      10: {
        correct: 'Harika bir mühendislik kararı! Sensör veritabanı kaydında hiçbir ölçüm kaybolmamalıdır (TCP garanti eder); canlı video yayınında ise anlık akış hızı öncelikli olup küçük paket kayıpları tolere edilebilir (UDP kullanılır).',
        wrong: 'Hatalı seçim! Eksiksiz veri aktarımı için TCP 3-way handshake gereklidir; canlı düşük gecikmeli görüntü/ses akışları için ise doğrulamasız UDP tercih edilir.'
      }
    };

    function evaluateQuestion(card) {
      const qNum = Number(card.dataset.q);
      const feedbackEl = card.querySelector('[data-feedback="' + qNum + '"]');
      let isCorrect = false;

      if (qNum === 1) {
        const s1 = card.querySelector('[data-user-step="1"]').value;
        const s2 = card.querySelector('[data-user-step="2"]').value;
        const s3 = card.querySelector('[data-user-step="3"]').value;
        const s4 = card.querySelector('[data-user-step="4"]').value;
        isCorrect = (s1 === 'D' && s2 === 'O' && s3 === 'R' && s4 === 'A');
      } else if (qNum === 6) {
        const e1 = card.querySelector('[data-era-match="1"]').value;
        const e2 = card.querySelector('[data-era-match="2"]').value;
        const e3 = card.querySelector('[data-era-match="3"]').value;
        isCorrect = (e1 === 'web1' && e2 === 'web2' && e3 === 'web3');
      } else if (qNum === 7) {
        const h1 = card.querySelector('[data-http-match="1"]').value;
        const h2 = card.querySelector('[data-http-match="2"]').value;
        const h3 = card.querySelector('[data-http-match="3"]').value;
        isCorrect = (h1 === '502' && h2 === '404' && h3 === '201');
      } else {
        const selected = card.querySelector('input[type="radio"]:checked');
        const correctVal = card.dataset.correct;
        isCorrect = (selected && selected.value === correctVal);
      }

      card.classList.remove('answered-correct', 'answered-wrong');
      card.classList.add(isCorrect ? 'answered-correct' : 'answered-wrong');

      if (feedbackEl) {
        feedbackEl.removeAttribute('hidden');
        feedbackEl.className = 'q-feedback ' + (isCorrect ? 'success' : 'error');
        feedbackEl.innerHTML = (isCorrect ? '✅ ' : '❌ ') + (isCorrect ? EXPLANATIONS[qNum].correct : EXPLANATIONS[qNum].wrong);
      }

      return isCorrect;
    }

    function updateScore() {
      let correctCount = 0;
      cards.forEach(function(card) {
        if (card.classList.contains('answered-correct')) {
          correctCount++;
        }
      });
      if (scoreDisplay) {
        scoreDisplay.textContent = correctCount + ' / ' + cards.length;
      }
    }

    cards.forEach(function(card) {
      const qNum = card.dataset.q;
      const checkBtn = card.querySelector('[data-check-q="' + qNum + '"]');
      if (checkBtn) {
        checkBtn.addEventListener('click', function() {
          evaluateQuestion(card);
          updateScore();
        });
      }
    });

    if (checkAllBtn) {
      checkAllBtn.addEventListener('click', function() {
        cards.forEach(function(card) {
          evaluateQuestion(card);
        });
        updateScore();
      });
    }

    if (resetBtn) {
      resetBtn.addEventListener('click', function() {
        cards.forEach(function(card) {
          card.classList.remove('answered-correct', 'answered-wrong');
          const fb = card.querySelector('.q-feedback');
          if (fb) fb.setAttribute('hidden', '');
          const selects = card.querySelectorAll('select');
          selects.forEach(function(s) { s.value = ''; });
          const radios = card.querySelectorAll('input[type="radio"]');
          radios.forEach(function(r) { r.checked = false; });
        });
        if (scoreDisplay) scoreDisplay.textContent = '0 / ' + cards.length;
      });
    }
  }
})();
