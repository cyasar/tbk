# Temel Bilgi Teknolojileri · ÇOMÜ

Çanakkale Onsekiz Mart Üniversitesi, Mühendislik Fakültesi, Elektrik-Elektronik Mühendisliği için **2026–2027** ders portalı ve web tabanlı sunum sistemi.

**Durum:** İlk dört haftanın dersleri hazırdır. 5–14. haftalar yalnızca ders planında “Yakında” olarak gösterilir. Ders 2 saat/hafta, toplam 14 hafta / 28 saattir. Bu depo henüz üniversite tarafından onaylanmış resmî yayın olarak tanımlanmamaktadır.

## Amaç

Donanım, işletim sistemleri, ağ, web, bulut, veri analizi, gömülü sistemler ve yapay zekâ arasındaki ilişkileri öğretmek. Öğrenme döngüsü: **Teori → Gerçek Sistem → Küçük Uygulama → GitHub Çalışması**.

Her derste hedefler, kavramlar, uygulama, AI promptu, cevaplı beş soru ve GitHub görevi bulunur.

## Hazır Haftalık İçerikler ve Laboratuvar Modülleri

- **01 / HAFTA: Bilgisayar Sistemleri ve Donanım Temelleri**
  - Bilgisayarların tarihsel gelişimi ve etkileşimli zaman çizgisi.
  - Modern von Neumann mimarisi, CPU, RAM, depolama ve veri yolları.
  - Fiziksel ve mantıksal portlar (USB, PCIe, UART, I2C, SPI) ve platform karşılaştırmaları.
- **02 / HAFTA: İşletim Sistemleri, Çekirdek (Kernel) ve Mimariler**
  - Çekirdek (Monolitik vs. Mikroçekirdek) ve kullanıcı/ayrıcalıklı mod (User/Kernel space).
  - Süreç (process), iş parçacığı (thread), bellek hiyerarşisi ve dosya sistemleri.
  - Masaüstü/sunucu işletim sistemleri ile RTOS ve bare-metal mikrodenetleyici farkları.
- **03 / HAFTA: İşlemci, Bellek, Dosya ve Sistem Yönetimi**
  - Windows, Linux ve macOS ortamlarında sistem yönetimi ve CLI komutları (`Get-Process`, `top`, `ss -tuln`, `lsof`).
  - Disk bakımı, dosya sistemleri (NTFS, ext4, APFS), takas alanı (swap/pagefile) ve Görev Yöneticisi optimizasyonları.
  - **İşletim Sistemleri Simülasyon Laboratuvarı:** CPU Zamanlayıcı (Round Robin, FCFS, Priority), Bellek & Sayfalama (Paging, Swap, OOM), Port Yönetimi ve Canlı Görev Yöneticisi.
- **04 / HAFTA: İnternet ve Ağ Teknolojilerinin Temelleri**
  - **Temel Ağ Yönetim Protokolleri (DHCP, NAT, DNS):**
    - **DHCP (UDP 67/68):** DORA süreci (**D**iscover $\rightarrow$ **O**ffer $\rightarrow$ **R**equest $\rightarrow$ **A**CK) ile otomatik IP kiralama, alt ağ maskesi, gateway ve DNS yapılandırması.
    - **NAT / PAT (RFC 1631):** IPv4 yetersizliğine çözüm; yerel özel IP'lerin (`192.168.x.x`) yönlendirici çıkışında tek bir Genel IP (`Public IP`) ve dinamik portlarla dış dünyaya bağlanması, iç ağın güvenliği.
    - **DNS (UDP 53):** Hiyerarşik alan adı çözümleme (Önbellek $\rightarrow$ ISS Resolver $\rightarrow$ Kök `.` $\rightarrow$ TLD `.tr` $\rightarrow$ Yetkili Sunucu) ve TCP/IP Traceroute yönlendirici atlamaları (hop).
  - **Web (WWW) ve İnternet Arasındaki Fark:**
    - İnternet küresel fiber optik, uydu ve yönlendirici otoyoludur; Web (HTTP/HTTPS) bu otoyoldaki araçlardan yalnızca biridir. Web servisi kapansa bile e-posta (SMTP), SSH ve IoT telemetrisi (MQTT) çalışmayı sürdürür.
  - **Web Sunucu Türleri:**
    - **Nginx:** Olay güdümlü, asenkron, yüksek eşzamanlılık, ters vekil (Reverse Proxy) ve statik dosya sunumu.
    - **Apache HTTP Server:** Modüler mimari, `.htaccess` desteği.
    - **Microsoft IIS:** Windows Server derin entegrasyonu, ASP.NET Core optimizasyonu.
    - **Caddy:** Otomatik Let's Encrypt SSL/TLS sertifika yönetimi.
  - **Web Yazılım Teknolojileri Yığını:**
    - **Frontend:** HTML5 (yapı), CSS3 (görsel/responsive), JavaScript (dinamik etkileşim/Fetch API), React (bileşen tabanlı UI/Virtual DOM).
    - **Backend:** PHP (dinamik derleme/WordPress/Laravel), Python (Flask/FastAPI/Django/AI/IoT REST API), Node.js (asenkron I/O/WebSocket), Java (Spring Boot kurumsal mimari), ASP.NET Core (C# derlenen yüksek performans).
  - **Ağ ve Web Simülasyon Laboratuvarı:**
    - Sekme 1: DNS Çözümleme & Traceroute + DHCP DORA IP Kiralama + Canlı NAT/PAT Çeviri Tablosu.
    - Sekme 2: Web vs. İnternet Otoyolu Trafik Kontrolü.
    - Sekme 3: Nginx Web Sunucusu Statik (1.4 ms) vs. Dinamik (38.6 ms PHP/MySQL) İstek Akışı.
    - Sekme 4: Web Yazılım Teknolojileri Kılavuzu ve Canlı Kod Kartları.

## Yerel çalıştırma

`index.html` dosyasını tarayıcıda açabilirsiniz. Pano erişimi gibi tarayıcı yeteneklerini güvenilir biçimde kullanmak için yerel HTTP sunucusu önerilir:

```sh
python -m http.server 8000
```

Ardından `http://localhost:8000` adresini açın. XAMPP kullanıyorsanız proje klasörü üzerinden `http://localhost/tbk/` adresi de kullanılabilir. Site PHP veya veritabanı gerektirmez.

## GitHub Pages üzerinde yayınlama

1. Dosyaları `cyasar/tbk` deposunun `main` dalına gönderin.
2. GitHub → **Settings → Pages** bölümünü açın.
3. **Build and deployment → Source → Deploy from a branch** seçin.
4. Dal olarak **main**, klasör olarak **/(root)** seçip kaydedin.
5. Dağıtım tamamlandığında Pages ekranındaki adresi doğrulayın. Beklenen proje adresi: [cyasar.github.io/tbk](https://cyasar.github.io/tbk/).

Yayın adresi ancak Pages etkinleştirilip dağıtım tamamlandığında çalışır. Tüm yerel bağlantılar göreli olduğu için depo alt yoluyla uyumludur. `.nojekyll` statik dosyaların Jekyll işleme gerektirmeden sunulmasını sağlar. Ayrıntılar: [GitHub Pages resmî rehberi](https://docs.github.com/en/pages/quickstart).

## Kullanım

- Tema düğmesi açık/koyu görünümü değiştirir; tercih `localStorage` içinde saklanır.
- Ana sayfada hafta araması ve kategori filtreleri bulunur.
- “Bu haftayı tamamladım” yerel ilerlemeyi kaydeder. Hesap veya notlandırma sistemi değildir.
- “Sunum modunu başlat” dersin her bölümünü slayt olarak gösterir. Uzun slaytlar kaydırılabilir.
- **← / →**, **Space**: gezinme; **Home / End**: ilk/son; **Esc**: çıkış; **F**: tam ekran.
- Düğme veya soru üzerindeyken Space ilgili kontrolü çalıştırır. Metin girişinde slayt kısayolları devre dışıdır.
- Kod blokları kopyalanabilir. Pano izni yoksa metni seçip elle kopyalayın.
- Sorular klavyeyle açılıp kapatılabilir. Sistem hareket azaltma tercihini destekler.

## Proje yapısı

```text
index.html                  Ana sayfa ve 14 haftalık plan
weeks/week01.html           Ayrıntılı ilk hafta
weeks/week02.html           Ayrıntılı ikinci hafta
weeks/week03.html           Ayrıntılı üçüncü hafta
weeks/week04.html           Ayrıntılı dördüncü hafta (İnternet & Ağ Teknolojileri)
css/style.css               Tema ve ortak tasarım
css/system-lab.css          3. hafta simülasyon ve mimari stilleri
css/network-lab.css         4. hafta ağ ve web simülasyon stilleri
css/responsive.css          Ekran, hareket ve yazdırma kuralları
css/presentation.css        Sunum görünümü
js/theme.js                 Tema tercihi
js/main.js                  Arama, kopyalama ve ilerleme
js/presentation.js          Slayt ve tam ekran denetimi
js/system-lab.js            3. hafta etkileşimli CPU, bellek ve port simülatörleri
js/network-lab.js           4. hafta etkileşimli DNS, DHCP, NAT, Web Server ve Tech Stack simülatörleri
js/demos.js                 İlerideki dersler için örnek etkileşimler
content/weeks.json          Yayındaki derslerin içerik kaynağı
content/syllabus.json       14 haftalık plan
scripts/build.py            Kaynaktan statik HTML üretimi
scripts/system_lab.py       3. hafta etkileşimli bileşen üretimi
scripts/network_lab.py      4. hafta etkileşimli ağ ve web bileşeni üretimi
scripts/check.py            Bağlantı ve içerik denetimi
assets/icons/               Yerel SVG favicon
assets/images/              İleride eklenecek görseller
assets/data/olcumler.csv     Dönem projesi örnek verisi
```

Tarayıcı yalnızca HTML5, CSS3 ve JavaScript ES6+ kullanır. Framework, harici font, CDN, npm bağımlılığı, izleme aracı veya sunucu tarafı bileşen yoktur. Git, GitHub ve GitHub Pages sürümleme ve yayınlama için kullanılır. Python yalnızca isteğe bağlı geliştirme aracıdır, çalıştırma bağımlılığı değildir.

## İçerik geliştirme ve katkı

`content/weeks.json` içeriğini veya `scripts/build.py` şablonunu değiştirin, ardından çalıştırın:

```sh
python scripts/build.py
python scripts/check.py
node --check js/main.js
node --check js/presentation.js
```

Üretilen HTML dosyalarını kaynakla birlikte commit edin. Yeni hafta eklerken öğrenme hedefleri, açıklamalı kavramlar, ders metni, sistem mimarisi, gerçek örnek, uygulama, doğrulama maddeleriyle AI promptu, beş cevaplı soru ve haftalık görevi tamamlayın. Plan kartının etkinliğini de üretim şablonunda güncelleyin.

Bir özellik dalında çalışın; küçük ve anlamlı commit’ler oluşturun. Pull request açıklamasına amaç, değişiklik ve doğrulama sonucu ekleyin. Teknik bilgileri kaynaklandırın; kişisel verileri ve anahtarları depoya koymayın. Öğrenci AI kullanabilir ancak teslim ettiği kodu ve kararları açıklayıp doğrulamalıdır.

## Kontrol listesi

Ana sayfa ve iki ders sayfasını mobil/masaüstünde, açık/koyu temada inceleyin. Filtreler, soru cevapları, kopyalama, ilerleme, önceki/sonraki hafta ve sunum kısayollarını deneyin. GitHub Pages üzerinde büyük/küçük harf duyarlılığını ve alt yol bağlantılarını ayrıca kontrol edin.

Dönem projesi gerçek bir bulut veya sensör servisine bağlı değildir; örnek CSV ile çalışma öngörülür. Canlı veri entegrasyonu sonraki aşamada ayrıca tasarlanacaktır.


## İlk hafta: etkileşimli bilgisayar tarihi

İlk haftadaki **Bilgisayarların Tarihi** bölümü, abaküsten günümüze 14 dönüm noktasını yatay bir tarih çizgisinde gösterir. Başlangıç durağı 1947 transistör devrimidir. Transistör öncesi ve sonrası farklı renklerle ayrılır; önceki/sonraki düğmeleri ve dönem kısayolları ile gezinilir. Çizgi odaktayken ok tuşları ve Home/End tarihleri değiştirir; sunumun slaytını değiştirmez.

İçerik `content/history.json`, üretim `scripts/history.py`, davranış `js/history.js`, görünüm `css/history.css` dosyalarındadır. `assets/images/history/` altındaki özgün SVG çizimler temsili eğitim görselleridir; arşiv fotoğrafı veya ölçekli teknik çizim değildir. Kaynaklar her durağın içinde bağlantılıdır. JavaScript kapalıyken ve yazdırmada tüm duraklar okunur. Tarihler sıralıdır; çizgideki aralıklar gerçek zaman uzunluğunu temsil etmez.


## Açık ve sade görünüm

Arayüz açık tema ile başlar; koyu tema isteğe bağlıdır. Yeni görünüm tercihi `tbk-theme-v2` anahtarında tutulur; önceki tema tercihi bu tasarım yenilemesinde bir kez sıfırlanır. Ders ilerlemesi korunur. Mobilde ana menü ve ders içindekiler açılıp kapanır. Hazır iki hafta öne çıkarılır, planlanan haftalar kısa kartlarda gösterilir.

CSS bu proje için özgün yazılmıştır; Edunex paketinin CSS dosyaları veya bağımlılıkları kullanılmamıştır. Tasarım framework gerektirmez. Responsive kurallar `css/responsive.css` içinde, ortak değişken ve bileşenler `css/style.css` içindedir.
