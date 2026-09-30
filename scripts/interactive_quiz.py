"""Interactive Engineering Assessment (10 Questions: Comboboxes, Ordering, Matching) for Week 4."""

def render_interactive_quiz():
    return '''<div class="interactive-quiz-container" data-quiz-lab>
      <div class="quiz-header-card">
        <div>
          <span class="eyebrow">UYGULAMALI DEĞERLENDİRME</span>
          <h3>Ağ, İnternet ve Web Teknolojileri Mühendislik Testi (10 Soru)</h3>
          <p>4. haftanın tüm konularını (Web Tarihi, DNS, DHCP, NAT, Web Sunucuları, HTTP ve Web Yazılım Yığını) kapsayan zorlayıcı, analitik düşünmeyi ölçen etkileşimli sorular. Cevaplarınızı seçin ve anında geri bildirim alın.</p>
        </div>
        <div class="quiz-score-badge" data-quiz-score-box>
          <span class="score-num" data-score-display>0 / 10</span>
          <span class="score-label">Doğru Sayısı</span>
        </div>
      </div>

      <div class="quiz-questions-grid">
        <!-- SORU 1: DHCP DORA Sıralaması -->
        <div class="quiz-q-card" data-q="1" data-correct="1,2,3,4">
          <div class="q-top">
            <span class="q-badge">Soru 1 · Protokol Sıralaması</span>
            <span class="q-points">1 Puan</span>
          </div>
          <h4>Bir IoT cihazı (ESP32) Wi-Fi ağına ilk katıldığında DHCP sunucusundan IP alırken gerçekleşen DORA adımlarının doğru sırası nedir?</h4>
          <div class="combobox-stack">
            <div class="combo-row">
              <label>1. Adım:</label>
              <select data-user-step="1" aria-label="1. DHCP Adımı">
                <option value="">Seçiniz...</option>
                <option value="O">Offer (Yönlendiricinin boş IP adresi teklif etmesi)</option>
                <option value="D">Discover (İstemcinin 255.255.255.255 yayınıyla DHCP sunucusu araması)</option>
                <option value="A">ACK (Sunucunun kira onayını ve parametreleri göndermesi)</option>
                <option value="R">Request (İstemcinin teklif edilen IP'yi onaylama isteği)</option>
              </select>
            </div>
            <div class="combo-row">
              <label>2. Adım:</label>
              <select data-user-step="2" aria-label="2. DHCP Adımı">
                <option value="">Seçiniz...</option>
                <option value="R">Request (İstemcinin teklif edilen IP'yi onaylama isteği)</option>
                <option value="A">ACK (Sunucunun kira onayını ve parametreleri göndermesi)</option>
                <option value="O">Offer (Yönlendiricinin boş IP adresi teklif etmesi)</option>
                <option value="D">Discover (İstemcinin 255.255.255.255 yayınıyla DHCP sunucusu araması)</option>
              </select>
            </div>
            <div class="combo-row">
              <label>3. Adım:</label>
              <select data-user-step="3" aria-label="3. DHCP Adımı">
                <option value="">Seçiniz...</option>
                <option value="A">ACK (Sunucunun kira onayını ve parametreleri göndermesi)</option>
                <option value="O">Offer (Yönlendiricinin boş IP adresi teklif etmesi)</option>
                <option value="D">Discover (İstemcinin 255.255.255.255 yayınıyla DHCP sunucusu araması)</option>
                <option value="R">Request (İstemcinin teklif edilen IP'yi onaylama isteği)</option>
              </select>
            </div>
            <div class="combo-row">
              <label>4. Adım:</label>
              <select data-user-step="4" aria-label="4. DHCP Adımı">
                <option value="">Seçiniz...</option>
                <option value="D">Discover (İstemcinin 255.255.255.255 yayınıyla DHCP sunucusu araması)</option>
                <option value="R">Request (İstemcinin teklif edilen IP'yi onaylama isteği)</option>
                <option value="A">ACK (Sunucunun kira onayını ve parametreleri göndermesi)</option>
                <option value="O">Offer (Yönlendiricinin boş IP adresi teklif etmesi)</option>
              </select>
            </div>
          </div>
          <div class="q-actions-bar">
            <button type="button" class="check-btn" data-check-q="1">Cevabı Kontrol Et</button>
            <button type="button" class="retry-btn" data-retry-q="1" title="Bu soruyu temizle ve tekrar dene">🔄 Tekrar Dene</button>
            <button type="button" class="solution-btn" data-solution-q="1" title="Doğru çözümü soru üzerinde göster">💡 Çözümü Göster</button>
          </div>
          <div class="q-feedback" data-feedback="1" hidden></div>
        </div>

        <!-- SORU 2: NAT/PAT Port Mantığı -->
        <div class="quiz-q-card" data-q="2" data-correct="B">
          <div class="q-top">
            <span class="q-badge">Soru 2 · NAT/PAT Ağ Mimarisi</span>
            <span class="q-points">1 Puan</span>
          </div>
          <h4>Yerel ağdaki bir laptop (192.168.1.15), uzaktaki bir web sunucusuna (193.255.140.18:443) HTTPS isteği gönderdiğinde modem/yönlendirici NAT (PAT) tablosunda hangi işlemi gerçekleştirir?</h4>
          <div class="options-group">
            <label class="opt-label"><input type="radio" name="q2" value="A"> <span>A) Paketin hedef IP adresini siler ve kendi IP'sini hedef olarak atar.</span></label>
            <label class="opt-label"><input type="radio" name="q2" value="B"> <span>B) Kaynak Özel IP'yi (192.168.1.15) siler; yerine kendi Genel IP'sini ve rastgele dinamik bir dış portu eşleyerek kaydeder.</span></label>
            <label class="opt-label"><input type="radio" name="q2" value="C"> <span>C) Yalnızca DNS sorgulaması yapar; IP adreslerinde hiçbir değişiklik yapmadan paketi geçirir.</span></label>
            <label class="opt-label"><input type="radio" name="q2" value="D"> <span>D) Paketi doğrudan yerel ağda yayın (broadcast) yaparak diğer tüm bilgisayarlara çoğaltır.</span></label>
          </div>
          <div class="q-actions-bar">
            <button type="button" class="check-btn" data-check-q="2">Cevabı Kontrol Et</button>
            <button type="button" class="retry-btn" data-retry-q="2" title="Bu soruyu temizle ve tekrar dene">🔄 Tekrar Dene</button>
            <button type="button" class="solution-btn" data-solution-q="2" title="Doğru çözümü soru üzerinde göster">💡 Çözümü Göster</button>
          </div>
          <div class="q-feedback" data-feedback="2" hidden></div>
        </div>

        <!-- SORU 3: DNS Hiyerarşisi -->
        <div class="quiz-q-card" data-q="3" data-correct="C">
          <div class="q-top">
            <span class="q-badge">Soru 3 · DNS Çözümleme Yolu</span>
            <span class="q-points">1 Puan</span>
          </div>
          <h4>Tarayıcıya <code>www.comu.edu.tr</code> yazıldığında yerel önbellekte (Cache) eşleşme yoksa, ISS DNS Resolver sunucusu hiyerarşik olarak sırasıyla hangi sunucuları sorgulamalıdır?</h4>
          <div class="options-group">
            <label class="opt-label"><input type="radio" name="q3" value="A"> <span>A) Önce Yetkili DNS (ns1.comu.edu.tr) → Sonra Kök Sunucu (.) → En son TLD (.tr)</span></label>
            <label class="opt-label"><input type="radio" name="q3" value="B"> <span>B) Doğrudan Google 8.8.8.8 sunucusu → DHCP sunucusu → Bilgisayar BIOS belleği</span></label>
            <label class="opt-label"><input type="radio" name="q3" value="C"> <span>C) Kök DNS Sunucuları (.) → Üst Düzey Alan Adı TLD Sunucusu (.tr) → ÇOMÜ Yetkili DNS Sunucusu (Authoritative)</span></label>
            <label class="opt-label"><input type="radio" name="q3" value="D"> <span>D) Nginx Web Sunucusu → MySQL Veritabanı → Linux Kernel Socket Katmanı</span></label>
          </div>
          <div class="q-actions-bar">
            <button type="button" class="check-btn" data-check-q="3">Cevabı Kontrol Et</button>
            <button type="button" class="retry-btn" data-retry-q="3" title="Bu soruyu temizle ve tekrar dene">🔄 Tekrar Dene</button>
            <button type="button" class="solution-btn" data-solution-q="3" title="Doğru çözümü soru üzerinde göster">💡 Çözümü Göster</button>
          </div>
          <div class="q-feedback" data-feedback="3" hidden></div>
        </div>

        <!-- SORU 4: Web vs İnternet Bağımsızlığı -->
        <div class="quiz-q-card" data-q="4" data-correct="D">
          <div class="q-top">
            <span class="q-badge">Soru 4 · Web ve İnternet Ayrımı</span>
            <span class="q-points">1 Puan</span>
          </div>
          <h4>Bir siber güvenlik olayı sebebiyle bir kurumun Port 80 (HTTP) ve Port 443 (HTTPS) erişimleri tamamen kapatılmıştır. Bu durumda aşağıdakilerden hangisi çalışmaya DEVAM EDEBİLİR?</h4>
          <div class="options-group">
            <label class="opt-label"><input type="radio" name="q4" value="A"> <span>A) Tarayıcıda açılan üniversite öğrenci bilgi sistemi web portalı</span></label>
            <label class="opt-label"><input type="radio" name="q4" value="B"> <span>B) React ile geliştirilmiş tek sayfalı arayüzün REST API sorguları</span></label>
            <label class="opt-label"><input type="radio" name="q4" value="C"> <span>C) Wikipedia web sayfalarındaki görsellerin yüklenmesi</span></label>
            <label class="opt-label"><input type="radio" name="q4" value="D"> <span>D) Port 22 üzerinden sunucuya bağlanan SSH uzak terminali ve Port 1883 ile veri ileten MQTT IoT sensörü</span></label>
          </div>
          <div class="q-actions-bar">
            <button type="button" class="check-btn" data-check-q="4">Cevabı Kontrol Et</button>
            <button type="button" class="retry-btn" data-retry-q="4" title="Bu soruyu temizle ve tekrar dene">🔄 Tekrar Dene</button>
            <button type="button" class="solution-btn" data-solution-q="4" title="Doğru çözümü soru üzerinde göster">💡 Çözümü Göster</button>
          </div>
          <div class="q-feedback" data-feedback="4" hidden></div>
        </div>

        <!-- SORU 5: Web Sunucusu Mimarisi -->
        <div class="quiz-q-card" data-q="5" data-correct="B">
          <div class="q-top">
            <span class="q-badge">Soru 5 · Sunucu Mimarisi & Concurrency</span>
            <span class="q-points">1 Puan</span>
          </div>
          <h4>Yüksek trafikli bir web uygulamasında on binlerce eşzamanlı bağlantıyı her istek için yeni bir süreç/thread açmadan, tek bir işlem döngüsünde asenkron olay güdümlü (event-driven) karşılayan web sunucusu hangisidir?</h4>
          <div class="options-group">
            <label class="opt-label"><input type="radio" name="q5" value="A"> <span>A) Klasik Process-per-connection mimarili Apache prefork modülü</span></label>
            <label class="opt-label"><input type="radio" name="q5" value="B"> <span>B) Asenkron non-blocking epoll/kqueue olay döngüsü kullanan Nginx</span></label>
            <label class="opt-label"><input type="radio" name="q5" value="C"> <span>C) Yalnızca statik HTML dosyası okuyabilen Python simple HTTP modülü</span></label>
            <label class="opt-label"><input type="radio" name="q5" value="D"> <span>D) Salt Windows COM+ nesneleri çalıştıran eski IIS 5.0 sunucusu</span></label>
          </div>
          <div class="q-actions-bar">
            <button type="button" class="check-btn" data-check-q="5">Cevabı Kontrol Et</button>
            <button type="button" class="retry-btn" data-retry-q="5" title="Bu soruyu temizle ve tekrar dene">🔄 Tekrar Dene</button>
            <button type="button" class="solution-btn" data-solution-q="5" title="Doğru çözümü soru üzerinde göster">💡 Çözümü Göster</button>
          </div>
          <div class="q-feedback" data-feedback="5" hidden></div>
        </div>

        <!-- SORU 6: Web Evrimi Eşleştirme (Combobox) -->
        <div class="quiz-q-card" data-q="6" data-correct="1:web1,2:web2,3:web3">
          <div class="q-top">
            <span class="q-badge">Soru 6 · Web 1.0 / 2.0 / 3.0 Eşleştirme</span>
            <span class="q-points">1 Puan</span>
          </div>
          <h4>Aşağıdaki mimari özellikleri ait oldukları Web evrim dönemi ile combobox üzerinden eşleştiriniz:</h4>
          <div class="combobox-stack">
            <div class="combo-row">
              <label>Statik HTML, salt okunur içerik (Read-Only), tek yönlü yayın:</label>
              <select data-era-match="1" aria-label="1. Dönem Seçimi">
                <option value="">Seçiniz...</option>
                <option value="web2">Web 2.0</option>
                <option value="web1">Web 1.0</option>
                <option value="web3">Web 3.0</option>
              </select>
            </div>
            <div class="combo-row">
              <label>AJAX, sayfa yenilenmeden asenkron veri, sosyal ağlar, kullanıcı üretimli içerik (Read-Write):</label>
              <select data-era-match="2" aria-label="2. Dönem Seçimi">
                <option value="">Seçiniz...</option>
                <option value="web3">Web 3.0</option>
                <option value="web2">Web 2.0</option>
                <option value="web1">Web 1.0</option>
              </select>
            </div>
            <div class="combo-row">
              <label>Semantik Ağ (Linked Data), WebAssembly (Wasm yüksek hız) ve Yapay Zekâ ajanları:</label>
              <select data-era-match="3" aria-label="3. Dönem Seçimi">
                <option value="">Seçiniz...</option>
                <option value="web1">Web 1.0</option>
                <option value="web3">Web 3.0</option>
                <option value="web2">Web 2.0</option>
              </select>
            </div>
          </div>
          <div class="q-actions-bar">
            <button type="button" class="check-btn" data-check-q="6">Cevabı Kontrol Et</button>
            <button type="button" class="retry-btn" data-retry-q="6" title="Bu soruyu temizle ve tekrar dene">🔄 Tekrar Dene</button>
            <button type="button" class="solution-btn" data-solution-q="6" title="Doğru çözümü soru üzerinde göster">💡 Çözümü Göster</button>
          </div>
          <div class="q-feedback" data-feedback="6" hidden></div>
        </div>

        <!-- SORU 7: HTTP Durum Kodları Teşhisi -->
        <div class="quiz-q-card" data-q="7" data-correct="1:502,2:404,3:201">
          <div class="q-top">
            <span class="q-badge">Soru 7 · HTTP Durum Kodları (Teşhis)</span>
            <span class="q-points">1 Puan</span>
          </div>
          <h4>Aşağıdaki sistem mühendisliği senaryolarında istemciye dönecek en doğru HTTP durum kodlarını seçiniz:</h4>
          <div class="combobox-stack">
            <div class="combo-row">
              <label>Nginx web sunucusu ayakta ancak arkasındaki PHP-FPM / Python backend servisi çökmüşse:</label>
              <select data-http-match="1" aria-label="1. Durum Kodu">
                <option value="">Seçiniz...</option>
                <option value="404">404 Not Found</option>
                <option value="502">502 Bad Gateway</option>
                <option value="200">200 OK</option>
                <option value="500">500 Internal Server Error</option>
              </select>
            </div>
            <div class="combo-row">
              <label>İstemci diskte ve routing tablosunda tanımlı olmayan bir URL talep ettiğinde:</label>
              <select data-http-match="2" aria-label="2. Durum Kodu">
                <option value="">Seçiniz...</option>
                <option value="502">502 Bad Gateway</option>
                <option value="404">404 Not Found</option>
                <option value="400">400 Bad Request</option>
                <option value="403">403 Forbidden</option>
              </select>
            </div>
            <div class="combo-row">
              <label>ESP32 sensör verisi POST isteğiyle veritabanına başarıyla YENİ bir kayıt olarak eklendiğinde:</label>
              <select data-http-match="3" aria-label="3. Durum Kodu">
                <option value="">Seçiniz...</option>
                <option value="200">200 OK</option>
                <option value="301">301 Moved Permanently</option>
                <option value="201">201 Created</option>
                <option value="204">204 No Content</option>
              </select>
            </div>
          </div>
          <div class="q-actions-bar">
            <button type="button" class="check-btn" data-check-q="7">Cevabı Kontrol Et</button>
            <button type="button" class="retry-btn" data-retry-q="7" title="Bu soruyu temizle ve tekrar dene">🔄 Tekrar Dene</button>
            <button type="button" class="solution-btn" data-solution-q="7" title="Doğru çözümü soru üzerinde göster">💡 Çözümü Göster</button>
          </div>
          <div class="q-feedback" data-feedback="7" hidden></div>
        </div>

        <!-- SORU 8: Web Yazılım Teknolojileri Çalışma Yeri -->
        <div class="quiz-q-card" data-q="8" data-correct="C">
          <div class="q-top">
            <span class="q-badge">Soru 8 · Frontend vs. Backend Yürütme Ortamı</span>
            <span class="q-points">1 Puan</span>
          </div>
          <h4>Web mimarisinde yazılan kodların çalıştığı yer (Execution Environment) ile ilgili aşağıdaki ifadelerden hangisi DOĞRUDUR?</h4>
          <div class="options-group">
            <label class="opt-label"><input type="radio" name="q8" value="A"> <span>A) PHP ve Python kodları kullanıcının tarayıcısına indirilip Chrome V8 motoru tarafından çalıştırılır.</span></label>
            <label class="opt-label"><input type="radio" name="q8" value="B"> <span>B) React bileşenleri veritabanına doğrudan SQL bağlantısı (Port 3306) açarak veriyi doğrudan çeker.</span></label>
            <label class="opt-label"><input type="radio" name="q8" value="C"> <span>C) PHP/Python sunucu tarafında çalışarak dinamik HTML/JSON üretir; HTML, CSS ve React/JS ise kullanıcının tarayıcısında (Client) yorumlanıp ekrana çizilir.</span></label>
            <label class="opt-label"><input type="radio" name="q8" value="D"> <span>D) CSS dosyaları işletim sistemi kernel'ında derlenir ve doğrudan ekran kartı sürücüsüne gönderilir.</span></label>
          </div>
          <div class="q-actions-bar">
            <button type="button" class="check-btn" data-check-q="8">Cevabı Kontrol Et</button>
            <button type="button" class="retry-btn" data-retry-q="8" title="Bu soruyu temizle ve tekrar dene">🔄 Tekrar Dene</button>
            <button type="button" class="solution-btn" data-solution-q="8" title="Doğru çözümü soru üzerinde göster">💡 Çözümü Göster</button>
          </div>
          <div class="q-feedback" data-feedback="8" hidden></div>
        </div>

        <!-- SORU 9: Tarihî Öncüler ve Standartlar -->
        <div class="quiz-q-card" data-q="9" data-correct="A">
          <div class="q-top">
            <span class="q-badge">Soru 9 · Web Tarihi ve Öncüleri</span>
            <span class="q-points">1 Puan</span>
          </div>
          <h4>1989'da CERN'de World Wide Web'i tasarlayan Tim Berners-Lee, web teknolojilerinin (HTML, HTTP) geleceğini güvenceye almak için 1994'te hangi kritik adımı atmıştır?</h4>
          <div class="options-group">
            <label class="opt-label"><input type="radio" name="q9" value="A"> <span>A) W3C'yi kurmuş; web teknolojilerinin patentsiz, telifsiz ve küresel açık bir kamu malı olarak kalmasını sağlamıştır.</span></label>
            <label class="opt-label"><input type="radio" name="q9" value="B"> <span>B) HTML patentini Microsoft'a satmış ve Internet Explorer'ın tek resmi tarayıcı olmasını şart koşmuştur.</span></label>
            <label class="opt-label"><input type="radio" name="q9" value="C"> <span>C) Web sitelerinde CSS kullanımını yasaklayarak yalnızca siyah-beyaz metin yayınlanmasını zorunlu kılmıştır.</span></label>
            <label class="opt-label"><input type="radio" name="q9" value="D"> <span>D) HTTP protokolünü kapatıp yerine doğrudan FTP protokolünü koymuştur.</span></label>
          </div>
          <div class="q-actions-bar">
            <button type="button" class="check-btn" data-check-q="9">Cevabı Kontrol Et</button>
            <button type="button" class="retry-btn" data-retry-q="9" title="Bu soruyu temizle ve tekrar dene">🔄 Tekrar Dene</button>
            <button type="button" class="solution-btn" data-solution-q="9" title="Doğru çözümü soru üzerinde göster">💡 Çözümü Göster</button>
          </div>
          <div class="q-feedback" data-feedback="9" hidden></div>
        </div>

        <!-- SORU 10: TCP 3-Way Handshake vs UDP Akışı -->
        <div class="quiz-q-card" data-q="10" data-correct="B">
          <div class="q-top">
            <span class="q-badge">Soru 10 · İletim Katmanı Seçimi (TCP vs UDP)</span>
            <span class="q-points">1 Puan</span>
          </div>
          <h4>Bir akıllı sera projesinde iki farklı iletişim görevi vardır: (1) Güvenli sensör veritabanı kaydı (eksik paket olmamalı), (2) Canlı düşük gecikmeli kamera video akışı (ufak tefek paket kaybı tolere edilebilir). En uygun protokol eşleşmesi nedir?</h4>
          <div class="options-group">
            <label class="opt-label"><input type="radio" name="q10" value="A"> <span>A) Görev 1 için UDP, Görev 2 için TCP</span></label>
            <label class="opt-label"><input type="radio" name="q10" value="B"> <span>B) Görev 1 için TCP (Sıralı, doğrulamalı ve güvenilir) · Görev 2 için UDP (Bağlantısız, hızlı ve düşük gecikmeli)</span></label>
            <label class="opt-label"><input type="radio" name="q10" value="C"> <span>C) Her iki görev için de sadece DNS (Port 53)</span></label>
            <label class="opt-label"><input type="radio" name="q10" value="D"> <span>D) Her iki görev için de yalnızca ARP protokolü</span></label>
          </div>
          <div class="q-actions-bar">
            <button type="button" class="check-btn" data-check-q="10">Cevabı Kontrol Et</button>
            <button type="button" class="retry-btn" data-retry-q="10" title="Bu soruyu temizle ve tekrar dene">🔄 Tekrar Dene</button>
            <button type="button" class="solution-btn" data-solution-q="10" title="Doğru çözümü soru üzerinde göster">💡 Çözümü Göster</button>
          </div>
          <div class="q-feedback" data-feedback="10" hidden></div>
        </div>
      </div>

      <div class="quiz-actions-footer">
        <button type="button" class="primary" data-action="check-all-quiz">Tüm Soruları Kontrol Et</button>
        <button type="button" data-action="reset-quiz">Cevapları Sıfırla</button>
      </div>
    </div>'''
