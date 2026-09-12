# Temel Bilgi Teknolojileri · ÇOMÜ

Çanakkale Onsekiz Mart Üniversitesi, Mühendislik Fakültesi, Elektrik-Elektronik Mühendisliği için **2026–2027** ders portalı ve web tabanlı sunum sistemi.

**Durum:** İlk iki haftanın dersleri hazırdır. 3–14. haftalar yalnızca ders planında “Yakında” olarak gösterilir. Ders 2 saat/hafta, toplam 14 hafta / 28 saattir. Bu depo henüz üniversite tarafından onaylanmış resmî yayın olarak tanımlanmamaktadır.

## Amaç

Donanım, işletim sistemleri, ağ, web, bulut, veri analizi, gömülü sistemler ve yapay zekâ arasındaki ilişkileri öğretmek. Öğrenme döngüsü: **Teori → Gerçek Sistem → Küçük Uygulama → GitHub Çalışması**.

İlk hafta bilgisayar tarihi, modern mimari, bileşenler, portlar ve platform karşılaştırmalarını; ikinci hafta kernel, süreç/thread, bellek, dosya sistemleri, boot, işletim sistemi aileleri ve RTOS/bare-metal ayrımını kapsar. Her derste hedefler, kavramlar, uygulama, AI promptu, cevaplı beş soru ve GitHub görevi vardır.

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
css/style.css               Tema ve ortak tasarım
css/responsive.css          Ekran, hareket ve yazdırma kuralları
css/presentation.css        Sunum görünümü
js/theme.js                 Tema tercihi
js/main.js                  Arama, kopyalama ve ilerleme
js/presentation.js          Slayt ve tam ekran denetimi
js/demos.js                 İlerideki dersler için örnek etkileşimler
content/weeks.json          Yayındaki derslerin içerik kaynağı
content/syllabus.json       14 haftalık plan
scripts/build.py            Kaynaktan statik HTML üretimi
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
