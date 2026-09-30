"""Interactive simulation and visual architecture components for Week 4 (Internet & Network Technologies)."""
from html import escape as esc

NETWORK_NODES = [
    ("client", "İstemci (Tarayıcı / App)", "Client Tier", "Kullanıcının web sitelerine girdiği tarayıcı (Chrome, Firefox) veya mobil uygulama; HTML, CSS, JavaScript çalıştırır.", "browser",
     "Protokol: HTTP/HTTPS, WebSockets", "Diller: HTML5, CSS3, JavaScript, React", "Görevi: Kullanıcı etkileşimi, DOM render ve API istekleri."),
    ("dhcp", "DHCP Sunucusu", "Dynamic Host Config", "Ağa katılan cihaza otomatik olarak IP adresi, alt ağ maskesi, varsayılan ağ geçidi ve DNS adresini DORA süreciyle kiralar.", "dhcp",
     "Protokol: DHCP (UDP Port 67/68)", "Aşamalar: Discover → Offer → Request → ACK", "Görevi: Manuel IP girmeyi ortadan kaldırmak, IP çakışmalarını önlemek."),
    ("nat", "NAT & Ağ Geçidi", "Network Address Translation", "Yerel özel IP'leri (192.168.x.x) dış dünyada tek bir genel IP'ye ve portlara (PAT) eşleyerek IPv4 yetersizliğini çözer.", "router",
     "Standart: RFC 1631 / PAT (Port Address Translation)", "Donanım: Modem / Yönlendirici (Router)", "Görevi: İç ağı gizlemek ve binlerce yerel cihazı tek genel IP ile internete çıkarmak."),
    ("dns", "DNS Çözümleyici", "Domain Name System", "İnsan dostu alan adlarını ('www.comu.edu.tr') bilgisayarların anladığı sayısal IP adreslerine ('193.255.140.18') çevirir.", "dns",
     "Protokol: DNS (UDP/TCP Port 53)", "Hiyerarşi: Önbellek → Root (.) → TLD (.tr) → Yetkili DNS", "Görevi: IP adresi tespiti ve yönlendirme."),
    ("firewall", "Güvenlik Duvarı & SSL/TLS", "Firewall & Security", "Yetkisiz port erişimlerini engeller (WAF) ve veri paketlerini TLS/HTTPS ile uçtan uca şifreler.", "security",
     "Protokol: TLS 1.3, HTTPS (Port 443)", "Standartlar: X.509 Sertifikaları, Let's Encrypt", "Görevi: Şifreleme, kimlik doğrulama, DDoS engelleme."),
    ("web-server", "Web Sunucusu (Nginx/Apache)", "Web Server Tier", "İstemcilerden gelen HTTP isteklerini karşılar, statik dosyaları sunar ve dinamik istekleri backend motoruna iletir.", "server",
     "Yazılımlar: Nginx, Apache HTTP Server, Microsoft IIS, Caddy", "Rol: Reverse Proxy, Yük Dengeleme, Statik Önbellek", "Görevi: Port 80/443 dinleme ve istek yönlendirme."),
    ("app-server", "Backend Uygulama Motoru", "Application / Backend", "İş mantığını çalıştıran, kullanıcı yetkilerini denetleyen ve dinamik HTML/JSON çıktısı üreten sunucu yazılımı.", "backend",
     "Diller: PHP (Laravel), Python (Django/Flask), Node.js, Java, C# (ASP.NET)", "Protokol: FastCGI, WSGI, ASGI, HTTP API", "Görevi: Dinamik kod çalıştırma ve API yönetimi."),
    ("database", "Veritabanı Katmanı", "Database Tier", "Kullanıcı hesaplarını, ölçüm verilerini ve site içeriklerini güvenli ve sorgulanabilir şekilde saklayan depolama katmanı.", "database",
     "Yazılımlar: MySQL, PostgreSQL, SQLite, MongoDB", "Protokol: SQL (Port 3306, 5432 vb.)", "Görevi: Kalıcı veri saklama, indeksleme ve sorgulama.")
]

def net_icon(kind):
    icons = {
        "browser": '<rect x="16" y="20" width="64" height="52" rx="8"/><path d="M16 34h64M26 27h3M34 27h3M42 27h3"/><path d="m36 50 8 8 16-16"/>',
        "dhcp": '<rect x="20" y="24" width="56" height="48" rx="8"/><path d="M32 48h32M48 32v32M20 36h56"/><circle cx="36" cy="30" r="2"/><circle cx="44" cy="30" r="2"/>',
        "dns": '<ellipse cx="48" cy="24" rx="32" ry="10"/><path d="M16 24v24c0 5.5 14.3 10 32 10s32-4.5 32-10V24M16 48v24c0 5.5 14.3 10 32 10s32-4.5 32-10V48"/><path d="M48 34v14m-10-7h20"/>',
        "router": '<rect x="18" y="38" width="60" height="28" rx="6"/><circle cx="32" cy="52" r="3"/><circle cx="44" cy="52" r="3"/><circle cx="56" cy="52" r="3"/><path d="M30 38V22m18 16V18m18 20V22"/>',
        "security": '<path d="M48 18 24 28v22c0 16 10.3 30.8 24 34 13.7-3.2 24-18 24-34V28L48 18z"/><path d="m40 48 6 6 12-12"/>',
        "server": '<rect x="18" y="20" width="60" height="20" rx="4"/><rect x="18" y="46" width="60" height="20" rx="4"/><circle cx="68" cy="30" r="3"/><circle cx="68" cy="56" r="3"/><path d="M26 30h20M26 56h20"/>',
        "backend": '<path d="m30 36-12 12 12 12m36-24 12 12-12 12M52 28l-8 40"/>',
        "database": '<ellipse cx="48" cy="26" rx="28" ry="9"/><path d="M20 26v40c0 5 12.5 9 28 9s28-4 28-9V26M20 46c0 5 12.5 9 28 9s28-4 28-9"/>'
    }
    return f'<svg viewBox="0 0 96 96" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{icons.get(kind, icons["browser"])}</g></svg>'

def render_network_architecture():
    cards = []
    for item in NETWORK_NODES:
        ident, title, english, desc, art, proto, stack, role = item
        cards.append(f'''<button type="button" class="net-arch-node" data-net-id="{esc(ident)}" data-title="{esc(title)}" data-en="{esc(english)}" data-desc="{esc(desc)}" data-proto="{esc(proto)}" data-stack="{esc(stack)}" data-role="{esc(role)}" aria-pressed="false">
          <div class="node-icon">{net_icon(art)}</div>
          <div class="node-text"><strong>{esc(title)}</strong><small lang="en">{esc(english)}</small></div>
        </button>''')

    return f'''<div class="net-architecture-explorer" data-net-arch>
      <p class="net-arch-lead">Bir web sitesini açtığınızda arka planda tek bir bilgisayar değil; <strong>DHCP, NAT, DNS, yönlendiriciler, web sunucuları ve backend motorlarından oluşan küresel bir orkestra</strong> çalışır. Bileşenlere dokunarak veri akışındaki rolünü keşfedin.</p>
      
      <div class="net-arch-grid" role="region" aria-label="Ağ ve Web Mimarisi Katmanları">
        {''.join(cards)}
      </div>

      <aside class="net-arch-inspector" data-net-inspector aria-live="polite">
        <div class="inspector-header">
          <span class="eyebrow">SEÇİLİ BİLEŞEN DETAYI</span>
          <h3 data-net-title>İncelemek için yukarıdaki mimari kartlardan birine tıklayın</h3>
          <p class="inspector-en" data-net-en lang="en">Client Tier ↔ DHCP ↔ NAT Router ↔ DNS ↔ Web Server ↔ Backend Engine ↔ Database</p>
        </div>
        <p class="inspector-desc" data-net-desc>İstemci tarayıcısından DHCP ile IP almaya, NAT çevirisine, DNS çözümlemesine ve veritabanı işlemlerine kadar tüm katmanların rollerini burada görebilirsiniz.</p>
        <div class="net-spec-pills">
          <div class="spec-pill proto"><strong>Kullanılan Protokoller:</strong> <span data-net-proto>DHCP (UDP 67/68), NAT/PAT, DNS (UDP 53), HTTP/HTTPS (443)</span></div>
          <div class="spec-pill stack"><strong>Teknoloji / Standart:</strong> <span data-net-stack>RFC 2131, RFC 1631, Nginx, PHP, Python, MySQL</span></div>
          <div class="spec-pill role"><strong>Mimari Görevi:</strong> <span data-net-role>Ağ yapılandırma, yönlendirme, çeviri ve web sunumu</span></div>
        </div>
      </aside>
    </div>'''

def render_network_lab():
    return '''<div class="network-sim-lab" data-net-lab>
      <div class="sim-tabs" role="tablist" aria-label="Ağ Simülasyon Modülleri">
        <button type="button" role="tab" id="tab-net-proto" aria-controls="panel-net-proto" aria-selected="true" data-net-tab="net-proto">
          🌐 1. Ağ Protokolleri (DNS, DHCP & NAT)
        </button>
        <button type="button" role="tab" id="tab-web-vs-net" aria-controls="panel-web-vs-net" aria-selected="false" data-net-tab="web-vs-net">
          🛣️ 2. Web vs. İnternet Katmanı
        </button>
        <button type="button" role="tab" id="tab-web-server" aria-controls="panel-web-server" aria-selected="false" data-net-tab="web-server">
          ⚙️ 3. Web Sunucusu (Statik vs Dinamik)
        </button>
        <button type="button" role="tab" id="tab-tech-stack" aria-controls="panel-tech-stack" aria-selected="false" data-net-tab="tech-stack">
          💻 4. Web Yazılım Teknolojileri Yığını
        </button>
      </div>

      <!-- PANEL 1: NETWORK PROTOCOLS (DNS, DHCP, NAT) -->
      <div class="sim-panel" id="panel-net-proto" role="tabpanel" aria-labelledby="tab-net-proto" data-net-panel="net-proto">
        <div class="sim-header">
          <div>
            <span class="eyebrow">İNTERAKTİF PROTOKOL SİMÜLATÖRÜ</span>
            <h3>Ağ Protokolleri Deney Alanı: DNS, DHCP ve NAT</h3>
            <p>Bir cihazın ağa ilk bağlandığı andan (DHCP IP kiralama), genel internete çıkışına (NAT adres çevirisi) ve web sitesinin IP adresini bulmasına (DNS) kadar olan 3 temel aşamayı test edin.</p>
          </div>
        </div>

        <!-- Protocol Sub-Navigation -->
        <div class="proto-subnav" role="tablist" aria-label="Protokol Seçenekleri">
          <button type="button" class="subnav-btn active" data-subproto="dns">🔍 1. DNS Çözümleme & Rotalama</button>
          <button type="button" class="subnav-btn" data-subproto="dhcp">⚡ 2. DHCP (DORA) IP Kiralama</button>
          <button type="button" class="subnav-btn" data-subproto="nat">🔄 3. NAT / PAT Adres Çevirisi</button>
        </div>

        <!-- SUBVIEW A: DNS SIMULATOR -->
        <div class="subproto-view" data-subproto-view="dns">
          <div class="dns-input-bar">
            <label for="dns-query-input">Sorgulanacak Web Adresi:</label>
            <div class="input-action-group">
              <select id="dns-query-input" data-dns-select aria-label="Web Adresi Seç">
                <option value="comu.edu.tr">www.comu.edu.tr (Üniversite Portalı)</option>
                <option value="github.com">github.com (Kod Deposu)</option>
                <option value="wikipedia.org">www.wikipedia.org (Açık Ansiklopedi)</option>
              </select>
              <button type="button" class="primary" data-net-action="start-dns">🔍 DNS Çözümlemesini Başlat</button>
            </div>
          </div>

          <div class="dns-pipeline-visual" data-dns-pipeline>
            <div class="dns-stage" data-stage="cache">
              <span class="stage-num">1</span>
              <strong>Tarayıcı Önbelleği</strong>
              <small>Yerel Bellek (0 ms)</small>
            </div>
            <div class="dns-arrow">→</div>
            <div class="dns-stage" data-stage="resolver">
              <span class="stage-num">2</span>
              <strong>ISS DNS Resolver</strong>
              <small>195.175.39.39</small>
            </div>
            <div class="dns-arrow">→</div>
            <div class="dns-stage" data-stage="root">
              <span class="stage-num">3</span>
              <strong>Kök DNS (.)</strong>
              <small>Root Name Server</small>
            </div>
            <div class="dns-arrow">→</div>
            <div class="dns-stage" data-stage="tld">
              <span class="stage-num">4</span>
              <strong>TLD (.tr) DNS</strong>
              <small>Top-Level Domain</small>
            </div>
            <div class="dns-arrow">→</div>
            <div class="dns-stage" data-stage="auth">
              <span class="stage-num">5</span>
              <strong>Yetkili DNS (Authoritative)</strong>
              <small>ns1.comu.edu.tr</small>
            </div>
          </div>

          <div class="packet-routing-box">
            <div class="routing-head">
              <strong>TCP/IP Paket Rotalama (Traceroute):</strong>
              <span data-resolved-ip>IP Bekleniyor...</span>
            </div>
            <div class="hops-list" data-hops-list>
              <div class="hop-item placeholder">DNS çözümlemesi başlatıldığında yönlendirici atlamaları burada listelenecektir.</div>
            </div>
          </div>

          <div class="packet-result-log" data-dns-log>
            <span class="muted">'DNS Çözümlemesini Başlat' düğmesine basarak sorgulama basamaklarını adım adım gözleyin.</span>
          </div>
        </div>

        <!-- SUBVIEW B: DHCP DORA SIMULATOR -->
        <div class="subproto-view" data-subproto-view="dhcp" hidden>
          <div class="dhcp-explain-banner">
            <strong>DHCP (Dynamic Host Configuration Protocol - Port 67/68 UDP):</strong>
            <p>Bir bilgisayar veya telefon ağa bağlandığında manuel IP girmek yerine yönlendiriciden 4 adımda (<strong>DORA</strong>) otomatik yapılandırma alır.</p>
          </div>

          <div class="dhcp-dora-grid">
            <div class="dora-card" data-dora="discover">
              <span class="dora-letter">D</span>
              <strong>1. Discover (Keşif)</strong>
              <p>İstemci ağa broadcast (255.255.255.255) haykırır: <em>"Ağda boşta IP dağıtacak bir DHCP sunucusu var mı?"</em></p>
              <span class="dora-status">Bekliyor...</span>
            </div>
            <div class="dora-card" data-dora="offer">
              <span class="dora-letter">O</span>
              <strong>2. Offer (Teklif)</strong>
              <p>Yönlendirici DHCP servisi yanıt döner: <em>"Sana 192.168.1.105 IP'sini ve 192.168.1.1 Gateway'ini öneriyorum."</em></p>
              <span class="dora-status">Bekliyor...</span>
            </div>
            <div class="dora-card" data-dora="request">
              <span class="dora-letter">R</span>
              <strong>3. Request (İstek)</strong>
              <p>İstemci bildirir: <em>"192.168.1.105 nolu IP teklifini kabul ediyorum, lütfen bana tahsis et."</em></p>
              <span class="dora-status">Bekliyor...</span>
            </div>
            <div class="dora-card" data-dora="ack">
              <span class="dora-letter">A</span>
              <strong>4. ACK (Onay & Kira)</strong>
              <p>DHCP sunucusu onaylar: <em>"IP kiralandı! Alt ağ: 255.255.255.0, DNS: 195.175.39.39, Kira Süresi: 24 saat."</em></p>
              <span class="dora-status">Bekliyor...</span>
            </div>
          </div>

          <div class="sim-controls-bar">
            <button type="button" class="primary" data-net-action="start-dhcp">⚡ DHCP DORA Sürecini Başlat (Yeni Cihaz Bağla)</button>
            <button type="button" data-net-action="release-dhcp">🔌 IP Kirasını Bırak (ipconfig /release)</button>
          </div>

          <div class="packet-result-log" data-dhcp-log>
            <span class="muted">'DHCP DORA Sürecini Başlat' butonuna basarak cihazın ağdan dinamik IP alışını gözleyin.</span>
          </div>
        </div>

        <!-- SUBVIEW C: NAT / PAT SIMULATOR -->
        <div class="subproto-view" data-subproto-view="nat" hidden>
          <div class="dhcp-explain-banner">
            <strong>NAT / PAT (Network Address & Port Translation - RFC 1631):</strong>
            <p>Evinizdeki 10 farklı telefon ve bilgisayar yerel özel IP (192.168.1.x) kullanır. İnternete çıkarken yönlendirici NAT tablosu üzerinden tüm trafiği tek bir <strong>Genel (Public) IP</strong> ve farklı portlarla dışarı iletir.</p>
          </div>

          <div class="nat-translation-table-box">
            <div class="nat-table-header">
              <strong>Yönlendirici Canlı NAT Çeviri Tablosu (NAT Translation Table)</strong>
              <span class="badge" data-nat-public-ip>Yönlendirici Genel IP: 212.58.244.70</span>
            </div>
            <table class="nat-data-table">
              <thead>
                <tr>
                  <th>Cihaz Adı</th>
                  <th>İç Ağ (Özel IP : Port)</th>
                  <th>Çevrilen Dış (Genel IP : Port)</th>
                  <th>Hedef Sunucu (IP : Port)</th>
                  <th>Protokol</th>
                </tr>
              </thead>
              <tbody data-nat-tbody>
                <tr>
                  <td>Öğrenci Laptop</td>
                  <td><code>192.168.1.15:49152</code></td>
                  <td><code>212.58.244.70:52110</code></td>
                  <td><code>193.255.140.18:443 (ÇOMÜ Web)</code></td>
                  <td><span class="proto-tag">HTTPS/TCP</span></td>
                </tr>
                <tr>
                  <td>Akıllı Telefon</td>
                  <td><code>192.168.1.22:51204</code></td>
                  <td><code>212.58.244.70:52111</code></td>
                  <td><code>140.82.121.4:443 (GitHub)</code></td>
                  <td><span class="proto-tag">HTTPS/TCP</span></td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="sim-controls-bar">
            <button type="button" class="primary" data-net-action="send-nat-packet">📦 Yeni İç Ağ Paketi Gönder (NAT Çevirisi Yap)</button>
            <button type="button" data-net-action="clear-nat">🧹 NAT Tablosunu Temizle</button>
          </div>

          <div class="packet-result-log" data-nat-log>
            <span class="muted">Yeni bir iç ağ cihazından dış sunucuya paket gönderildiğinde yönlendiricinin port eşleme mantığını izleyin.</span>
          </div>
        </div>
      </div>

      <!-- PANEL 2: WEB VS INTERNET -->
      <div class="sim-panel" id="panel-web-vs-net" role="tabpanel" aria-labelledby="tab-web-vs-net" data-net-panel="web-vs-net" hidden>
        <div class="sim-header">
          <div>
            <span class="eyebrow">KAVRAMSAL DENEY</span>
            <h3>Web ve İnternet Aynı Şey Midir?</h3>
            <p><strong>Cevap: Hayır!</strong> İnternet küresel fiber optik, uydu ve yönlendirici otoyoludur. Web (HTTP) bu otoyoldaki araçlardan yalnızca biridir. Aşağıdaki servisleri açıp kapatarak test edin.</p>
          </div>
        </div>

        <div class="highway-container">
          <div class="highway-roadbed">
            <div class="road-label">KÜRESEL İNTERNET ALTYAPISI (IP Protokolü, Yönlendiriciler, Fiber & Bakır Kablolar)</div>
            <div class="road-status">Durum: <strong style="color:#24705b">AKTİF & BAĞLI</strong></div>
          </div>

          <div class="services-traffic-grid">
            <div class="service-vehicle active" data-service="web">
              <div class="veh-icon">🌐</div>
              <div class="veh-info">
                <strong>World Wide Web (Web)</strong>
                <small>HTTP / HTTPS · Port 80, 443</small>
              </div>
              <button type="button" data-toggle-service="web">Web Servisini Kapat</button>
            </div>

            <div class="service-vehicle active" data-service="mail">
              <div class="veh-icon">📧</div>
              <div class="veh-info">
                <strong>E-Posta Servisi</strong>
                <small>SMTP / IMAP · Port 25, 993</small>
              </div>
              <button type="button" data-toggle-service="mail">E-Postayı Kapat</button>
            </div>

            <div class="service-vehicle active" data-service="ssh">
              <div class="veh-icon">🔒</div>
              <div class="veh-info">
                <strong>Uzak Güvenli Terminal (SSH)</strong>
                <small>SSH Protokolü · Port 22</small>
              </div>
              <button type="button" data-toggle-service="ssh">SSH'ı Kapat</button>
            </div>

            <div class="service-vehicle active" data-service="iot">
              <div class="veh-icon">📡</div>
              <div class="veh-info">
                <strong>IoT Telemetri Ağı</strong>
                <small>MQTT / CoAP · Port 1883</small>
              </div>
              <button type="button" data-toggle-service="iot">IoT Ağını Kapat</button>
            </div>
          </div>
        </div>

        <div class="packet-result-log" data-web-vs-net-log>
          <strong>Mühendislik Çıkarımı:</strong> Web (HTTP/HTTPS) kapalı olsa bile internet altyapısı çalışmaya devam eder; e-postalar gitmeye, SSH terminalleri bağlanmaya ve ESP32 sensörleri MQTT ile veri basmaya devam edebilir!
        </div>
      </div>

      <!-- PANEL 3: WEB SERVER (STATIC VS DYNAMIC) -->
      <div class="sim-panel" id="panel-web-server" role="tabpanel" aria-labelledby="tab-web-server" data-net-panel="web-server" hidden>
        <div class="sim-header">
          <div>
            <span class="eyebrow">MİMARİ KARŞILAŞTIRMA</span>
            <h3>Web Sunucusu Nasıl Çalışır? Statik vs. Dinamik İstek</h3>
            <p>Nginx veya Apache istemciden istek aldığında iki farklı yol izler: Statik dosyaları (HTML/CSS) doğrudan diskten sunar; dinamik istekleri backend motoruna (PHP/Python) derletir.</p>
          </div>
        </div>

        <div class="client-server-flow">
          <div class="flow-box client-box">
            <div class="box-tag">İstemci</div>
            <strong>Tarayıcı / ESP32</strong>
            <p>HTTP İstek Üretici</p>
          </div>

          <div class="flow-arrow" data-flow-arrow-req>
            <span data-req-label>HTTP İsteği</span>
            <strong>→</strong>
          </div>

          <div class="flow-box server-box">
            <div class="box-tag">Web Sunucusu</div>
            <strong>Nginx / Apache</strong>
            <p>Port 80/443 Dinleyici</p>
          </div>

          <div class="flow-arrow" data-flow-arrow-backend>
            <span data-backend-label>FastCGI / WSGI</span>
            <strong>→</strong>
          </div>

          <div class="flow-box backend-box">
            <div class="box-tag">Backend & SQL</div>
            <strong>PHP / Python + MySQL</strong>
            <p>Dinamik Derleyici</p>
          </div>
        </div>

        <div class="sim-controls-bar">
          <button type="button" class="primary" data-server-test="static">📄 Statik İstek Gönder (index.html · CSS)</button>
          <button type="button" data-server-test="dynamic">⚡ Dinamik İstek Gönder (olcum.php / API)</button>
          <button type="button" data-server-test="404">❌ Hatalı İstek Gönder (olmayan_sayfa.html)</button>
        </div>

        <div class="packet-result-log" data-server-log>
          <span class="muted">Statik veya dinamik istek butonlarına basarak web sunucusunun yanıt süresini ve çalışma farkını izleyin.</span>
        </div>
      </div>

      <!-- PANEL 4: WEB TECHNOLOGY STACK EXPLORER -->
      <div class="sim-panel" id="panel-tech-stack" role="tabpanel" aria-labelledby="tab-tech-stack" data-net-panel="tech-stack" hidden>
        <div class="sim-header">
          <div>
            <span class="eyebrow">TEKNOLOJİ REHBERİ</span>
            <h3>Web Yazılım Teknolojileri: Frontend & Backend</h3>
            <p>Bir web projesinde kullanılan temel teknolojilere tıklayarak görevini, kod örneğini ve avantajını inceleyin.</p>
          </div>
        </div>

        <div class="tech-stack-split">
          <div class="tech-col">
            <h4>Frontend (İstemci Tarafı - Tarayıcıda Çalışır)</h4>
            <div class="tech-pills-grid">
              <button type="button" class="tech-btn active" data-tech="html">HTML5</button>
              <button type="button" class="tech-btn" data-tech="css">CSS3</button>
              <button type="button" class="tech-btn" data-tech="js">JavaScript</button>
              <button type="button" class="tech-btn" data-tech="react">React</button>
            </div>
          </div>

          <div class="tech-col">
            <h4>Backend (Sunucu Tarafı - Server'da Çalışır)</h4>
            <div class="tech-pills-grid">
              <button type="button" class="tech-btn" data-tech="php">PHP</button>
              <button type="button" class="tech-btn" data-tech="python">Python (Flask/Django)</button>
              <button type="button" class="tech-btn" data-tech="node">Node.js</button>
              <button type="button" class="tech-btn" data-tech="java">Java (Spring)</button>
              <button type="button" class="tech-btn" data-tech="asp">ASP.NET (C#)</button>
            </div>
          </div>
        </div>

        <div class="tech-preview-card" data-tech-preview>
          <div class="preview-head">
            <div>
              <span class="eyebrow" data-tech-role>FRONTEND YAPITAŞI</span>
              <h3 data-tech-title>HTML5 (HyperText Markup Language)</h3>
            </div>
            <span class="tech-badge" data-tech-env>Tarayıcıda Çalışır</span>
          </div>
          <p data-tech-desc>Web sayfalarının iskeletini ve anlamsal içeriğini oluşturur. Başlıklar, paragraflar, formlar ve butonlar HTML ile tanımlanır.</p>
          <div class="code-wrap">
            <pre><code data-tech-code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
  &lt;body&gt;
    &lt;h1&gt;Akıllı Sensör Ölçümü&lt;/h1&gt;
    &lt;p&gt;Sıcaklık: 24.5 °C&lt;/p&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>
          </div>
        </div>
      </div>
    </div>'''
