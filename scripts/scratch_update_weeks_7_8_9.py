import json
from pathlib import Path

# Load current weeks
weeks_path = Path("content/weeks.json")
weeks = json.load(weeks_path.open("r", encoding="utf-8"))

# Week 07: Google Dokümanlar, Slides, Forms ve Ortak Çalışma
week07 = {
  "title": "Google Dokümanlar, Slides, Forms ve Ortak Çalışma",
  "intro": "Bulut ortamında ortak mühendislik raporu, veri toplama formu ve etkileşimli teknik sunum hazırlayın; gerçek zamanlı iş birliğini ve sürüm yönetimini keşfedin.",
  "group": "Bulut",
  "category": "cloud",
  "concepts": [
    [
      "Eşzamanlı İş Birliği (Real-Time Collaboration)",
      "Birden fazla kullanıcının aynı doküman üzerinde milisaniyeler içinde çakışmasız (Operational Transformation - OT) birlikte çalışabilmesi."
    ],
    [
      "Sürüm Geçmişi & Adlandırılmış Versiyonlar",
      "Belgelerdeki tüm değişikliklerin anlık snapshot'lar halinde saklanması, istenen ana geri dönülebilmesi ve teknik onay adımlarının kaydı."
    ],
    [
      "Biçimlendirme & Semantik Belge Yapısı",
      "Başlık stilleri (H1, H2, H3), otomatik içindekiler tablosu, denklem düzenleyici (LaTeX) ve akademik rapor şablonu standardı."
    ],
    [
      "Google Forms ile Yapılandırılmış Veri Toplama",
      "Fiziksel formlar veya dağınık mesajlar yerine tek merkezden parametrik veri toplama ve doğrudan Google E-Tablolara satır aktarımı."
    ],
    [
      "Google Slides ile Teknik Sunum Mimarisi",
      "Mühendislik projelerini görselleştirme, akış diyagramları, video ve dinamik E-Tablo grafiklerinin sunuma canlı bağlanması (Linked Charts)."
    ],
    [
      "Yorumlar, Eylem Öğeleri & Görev Atama (@mention)",
      "Doküman içi görev yönetimi, hakem denetimi (review), öneri kipi (suggesting mode) ve ekip içi geri bildirim kültürü."
    ]
  ],
  "lessons": [
    [
      "Ders İçeriği · Google Dokümanlar: Mühendislik Raporu Hazırlama",
      "Geleneksel kelime işlemcilerde karşılaşılan 'Rapor_son_v2_final.docx' karmaşası, bulut tabanlı Google Dokümanlar ile tamamen ortadan kalkar.\nBelgeler yerel diskinizde değil, Google Cloud üzerinde tek ve canlı bir ana kopya (Single Source of Truth) olarak tutulur.\nBir mühendislik raporunda metin hiyerarşisi (Başlık 1, Başlık 2) dokümanın otomatik haritasını (Document Outline) ve İçindekiler tablosunu oluşturur. 'Ekle > Denklem' aracıyla LaTeX destekli matematiksel formüller ($V = I \\cdot R$, $\\int f(x)dx$) standart bilimsel gösterimle yazılır.\nSayfa yapısı, üstbilgi/altbilgi, kaynakça dipnotları (Ctrl+Alt+F) ve kurumsal antetli şablon kullanımı profesyonel belgelendirmenin temelidir."
    ],
    [
      "Gerçek Zamanlı Ortak Çalışma Mimarisi ve Sürüm Denetimi",
      "Aynı anda 20 öğrenci bir rapor üzerinde çalışırken metinler nasıl çakışmaz? Google Dokümanlar arka planda Operasyonel Dönüşüm (Operational Transformation - OT) algoritmalarını ve WebSocket bağlantılarını kullanır. Her tuşa basıldığında karakter dizini dönüşümleri sunucuda anında çözülür.\nSürüm Geçmişi (Ctrl+Alt+Shift+H): Belgenin doğumundan bugüne her harfin kim tarafından, ne zaman yazıldığını gösterir. Önemli aşamalarda 'Mevcut sürüme ad ver' (ör. 'Laboratuvar Onayı - 11 Kasım') denilerek projenin kilometre taşları dondurulabilir. İstenildiğinde tek tıkla eski bir sürüme dönülebilir veya kopyası alınabilir."
    ],
    [
      "Geri Bildirim Kültürü: Öneri Kipi, Yorumlar ve Görev Atama",
      "Bir mühendislik ekibinde rapor denetimi (peer-review) hayati önem taşır:\n1. Düzenleme Kipi (Editing): Doğrudan metni değiştirir.\n2. Öneri Kipi (Suggesting): Değişiklikleri yeşil izleme çizgileriyle öneri olarak sunar; belge sahibi 'Kabul Et' (✓) veya 'Reddet' (✗) diyebilir.\n3. Yorum ve @mention Görev Ataması: İlgili metin seçilip Ctrl+Alt+M ile yorum eklenir. '+ogrenci@comu.edu.tr' yazılarak 'Bu görevi şuna ata' kutusu işaretlendiğinde, sistem ilgili kişiye otomatik görev e-postası gönderir."
    ],
    [
      "Google Forms: Yapılandırılmış Ölçüm ve Anket Toplama",
      "Mühendislikte sensör kalibrasyonu, deney katılımı veya kullanıcı geri bildirimi toplamak için Google Forms yapılandırılmış bir arayüz sağlar.\nSoru Türleri: Kısa yanıt, çoktan seçmeli, onay kutuları, Likert ölçeği ve dosya yükleme (ör. laboratuvar devre fotoğrafı).\nKoşullu Dallanma: 'Yanıta göre bölüme git' özelliğiyle akıllı form mantığı kurulur.\nE-Tablo Entegrasyonu: Form yanıtları 'Yanıtlar > E-Tablolarda Görüntüle' butonuyla anında dinamik bir Google E-Tabloya bağlanır. Her form gönderimi bu tabloya yeni bir satır (Record) ve milisaniyelik zaman damgası (Timestamp) ekler."
    ],
    [
      "Google Slides: Teknik ve Etkileşimli Proje Sunumları",
      "Bir mühendisin projesini doğru sunabilmesi en az tasarımı kadar önemlidir. Google Slides şunları sunar:\n1. Dinamik E-Tablo Grafiği Bağlama: Google E-Tablolardaki canlı bir ölçüm grafiği kopyalanıp Slides'a 'Tabloya bağla' seçeneğiyle yapıştırıldığında; tablodaki veri değiştikçe slaytta 'Güncelle' butonu belirir ve sunum her zaman canlı veriyi gösterir.\n2. Birlikte Sunum: Ekip üyeleri farklı konumlardan sunuma eşlik edebilir; 'Slayt Gösterisi' kipinde soru-cevap oturumu (Audience Q&A) açılarak dinleyicilerden canlı soru toplanabilir.\n3. Görsel Şablon ve Akış Diyagramları: Şekiller, bağlayıcı çizgiler ve akıllı kılavuz çizgileriyle temiz devre ve blok diyagramları çizilir."
    ]
  ],
  "diagram": "Google Forms (Kullanıcı / Ölçüm Girdisi)\n             ↓ (Otomatik Zaman Damgası & Satır Ekleme)\nGoogle Sheets (Veri Havuzu & Dinamik Hesaplama)\n      ↓ (Canlı Bağlantılı Grafik)          ↓ (CSV / Tablo)\nGoogle Slides (Yönetici Sunumu)   Google Docs (Resmi Deney Raporu)\n      ↖                              ↗\n       [Ekip Ortak Çalışması: WebSocket + Sürüm Geçmişi]",
  "architecture": "Google Workspace mimarisinde Forms veri giriş kapısı, Sheets veri işleme motoru, Docs detaylı akademik belgelendirme, Slides ise dinamik grafiklerle beslenen görsel sunum katmanıdır. Tüm katmanlar bulut üzerinde anlık senkronize çalışır.",
  "example": "Laboratuvarda 3 kişilik bir mühendislik grubu: Biri Google Forms üzerinden devre ölçüm gerilimlerini girer. Bu veriler anında Google Sheets'e düşer ve grafik otomatik güncellenir. İkinci öğrenci Google Dokümanlar'da raporun 'Bulgular' bölümüne bu canlı grafiği bağlar ve hata payını formüllerle açıklar. Üçüncü öğrenci ise Google Slides'ta proje sunumunu hazırlayıp Docs'tan gelen sonuçları ekibe sunar. Tüm süreçte kimse birbirine dosya göndermez; her şey tek bir Drive klasöründe ortak yürütülür.",
  "practice": [
    "Google Dokümanlar'da 'Laboratuvar Deney Raporu' şablonu oluşturun: Başlık 1-2 stilleri, otomatik içindekiler tablosu ve LaTeX formülü ekleyin.",
    "Bir ekip arkadaşınızı dokümana ekleyip 'Öneri Kipi'nde metin düzeltmesi yapmasını ve size '@' etiketiyle bir görev atamasını sağlayın.",
    "Google Forms ile 5 soruluk 'Cihaz Test & Kalibrasyon Formu' hazırlayın; yanıtları yeni bir Google E-Tabloya bağlayın.",
    "Google Slides'ta 3 slaytlık bir teknik tanıtım hazırlayın; E-Tablodan canlı bağlantılı bir grafiği slayta yerleştirin."
  ],
  "code": "# Google Apps Script (Forms -> Docs / Sheets Otomasyon Örneği)\nfunction onFormSubmit(e) {\n  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();\n  var lastRow = sheet.getLastRow();\n  var timestamp = sheet.getRange(lastRow, 1).getValue();\n  var olcumDegeri = sheet.getRange(lastRow, 2).getValue();\n  Logger.log('Yeni Ölçüm Alındı: ' + timestamp + ' -> ' + olcumDegeri + ' V');\n}",
  "prompt": "Elektrik-Elektronik Mühendisliği öğrencileri için Google Dokümanlar üzerinde akademik ve endüstriyel standartlara uygun bir 'Laboratuvar Proje Raporu' şablonu hazırla. Başlık hiyerarşisi, sürüm geçmişi onay adımları, denklem yazımı ve ekip içi görev atama kurallarını adım adım açıkla.",
  "quiz": [
    [
      "Google Dokümanlar'da 'Öneri Kipi' (Suggesting Mode) ne işe yarar?",
      "Belge üzerinde doğrudan kalıcı değişiklik yapmak yerine, değişiklikleri öneri olarak göstererek belge sahibinin onayına veya reddine sunar."
    ],
    [
      "Google Dokümanlar ve Slides'ta 'Sürüm Geçmişi' neden klasör kopyalamaktan üstündür?",
      "Belgenin her anını tek dosya içinde yazar kimliği ve zaman damgasıyla saklar; diskte gereksiz kopyalar oluşturmadan istenen tarihe dönmeyi sağlar."
    ],
    [
      "Google Forms yanıtları Google E-Tablolara aktarıldığında ne gerçekleşir?",
      "Her yeni form doldurulduğunda tablonun en alt satırına anlık zaman damgasıyla birlikte yapılandırılmış bir veri kaydı (record) eklenir."
    ],
    [
      "Google Slides'a bir grafik 'Tabloya Bağla' (Link to Spreadsheet) seçeneğiyle eklendiğinde ne avantaj sağlar?",
      "E-Tablodaki kaynak veriler veya formüller değiştiğinde, slayttaki grafiğin tek tıkla 'Güncelle' butonuyla canlı olarak yenilenmesini sağlar."
    ],
    [
      "Google Dokümanlar'da otomatik İçindekiler Tablosu oluşturabilmek için ne yapılmalıdır?",
      "Metin başlıklarının standart 'Başlık 1 (H1)', 'Başlık 2 (H2)' ve 'Başlık 3 (H3)' stilleriyle biçimlendirilmesi gerekir."
    ]
  ],
  "task": "3 kişilik bir grup halinde ortak bir Google Drive klasöründe 'Hafta07_Proje' dokümanı ve formu oluşturun. Form üzerinden en az 3 adet ölçüm verisi girin, sonuçları Dokümanlar raporunda ve Slides sunumunda canlı bağlantılı olarak belgeleyin.",
  "goals": [
    "Google Dokümanlar ile semantik başlık yapısına ve LaTeX denklem düzenine sahip akademik rapor oluşturabilmek.",
    "Sürüm geçmişini kullanarak belgenin kritik aşamalarını adlandırabilmek ve geri alabilmek.",
    "Öneri kipi ve '@mention' görev atama mekanizmalarıyla profesyonel ekip çalışması yürütebilmek.",
    "Google Forms ile parametrik veri toplayıp E-Tablolara dinamik satır akışı sağlayabilmek.",
    "Google Slides üzerinde dinamik grafik bağlantılarını ve teknik sunum ilkelerini uygulayabilmek."
  ],
  "verify": [
    "Google Dokümanlar raporundaki içindekiler tablosunun başlıklara tıklandığında ilgili bölüme gittiğini doğrulayın.",
    "Forms üzerinden yeni bir yanıt gönderildiğinde E-Tabloda anında yeni satır oluştuğunu kontrol edin.",
    "Slayta eklenen grafiğin 'Güncelle' butonuyla tablodaki yeni veriyi yansıttığını teyit edin."
  ],
  "sources": [
    [
      "Google Workspace Öğrenim Merkezi · Docs & Slides",
      "https://support.google.com/a/users/answer/9282958"
    ],
    [
      "Google Forms Rehberi ve Veri Toplama İlkeleri",
      "https://support.google.com/docs/answer/6281888"
    ]
  ],
  "table": [
    [
      "Uygulama",
      "Temel Görevi",
      "Mühendislik Kullanım Senaryosu",
      "Çıktı Biçimi"
    ],
    [
      "Google Dokümanlar",
      "Biçimlendirilmiş teknik metin ve rapor",
      "Bitirme projesi, laboratuvar deney föyü, akademik bildiri",
      "Web bağlantısı, PDF, DOCX, EPUB"
    ],
    [
      "Google Slides",
      "Görsel ve dinamik teknik sunum",
      "Proje ara sunumu, poster oturumu, canlı telemetri panosu",
      "Web sunumu, PDF, PPTX"
    ],
    [
      "Google Forms",
      "Yapılandırılmış veri toplama arayüzü",
      "Sensör kalibrasyonu, saha ölçüm anketi, malzeme talep formu",
      "Canlı E-Tablo satırları, özet grafikler"
    ]
  ]
}

# Week 08: Hesap Tablolama Teknolojileri
week08 = {
  "title": "Hesap Tablolama Teknolojileri",
  "intro": "Hücrelerden dinamik formüllere: gerilim, akım, güç ve enerji hesabını matematiksel modellerle güvenilir bir Google E-Tabloya dönüştürün.",
  "group": "Veri",
  "category": "cloud",
  "concepts": [
    [
      "Hücre Adresleme & Matris Yapısı",
      "Verilerin sütun harfleri ve satır numaralarıyla (A1, B5) 2 boyutlu koordinat sistemi üzerinde modellenmesi."
    ],
    [
      "Mutlak ($A$1) ve Göreceli (A1) Başvuru",
      "Formüller kopyalandığında hücre indisinin korunması ($ işareti) veya formülün konumuna göre dinamik ötelenmesi."
    ],
    [
      "Temel Matematiksel & İstatistiki Fonksiyonlar",
      "SUM, AVERAGE, MIN, MAX, COUNT, STDEV fonksiyonlarıyla mühendislik verilerini anında hesaplama."
    ],
    [
      "Veri Tipleri & Hücre Biçimlendirme",
      "Sayı, Para Birimi, Yüzde, Tarih ve Özel Sayı Biçimleri (Ohm Ω, Volt V, Amper A ekleri)."
    ],
    [
      "Mantıksal Fonksiyonlar (IF / EĞER)",
      "Belirlenen elektriksel eşik değerlerine göre otomatik karar üretme (Örn: Gerilim > 240V ise 'YÜKSEK GERİLİM' uyarısı)."
    ],
    [
      "CSV Veri Alma ve Ayrıştırma (Import & Split)",
      "Sensörlerden gelen virgülle ayrılmış ham metin verilerini tablolara düzgün sütunlar halinde yerleştirme."
    ]
  ],
  "lessons": [
    [
      "Ders İçeriği · Elektronik Tablo Mantığı: Koordinatlar ve Veri Tipleri",
      "Google E-Tablolar (Sheets), arka planda 2 boyutlu bir matris veri yapısı gibi çalışır. Her hücre bir veri türüne sahiptir: Metin, Sayı, Tarih veya Boolean (DOĞRU/YANLIŞ).\nBir hücreye '=' işareti yazıldığında program hesaplama motorunu devreye sokar.\nTip Hatası: Bir metin ile bir sayıyı çarpmaya çalışırsanız '#DEĞER!' (#VALUE!) hatası alırsınız. Bu nedenle sensörlerden gelen sayıların ondalık ayırıcısına (nokta veya virgül) dikkat edilmelidir."
    ],
    [
      "Göreceli (Relative) ve Mutlak (Absolute) Hücre Başvuruları",
      "Bir mühendisin en sık yaptığı ve en çok hata üreten konu hücre sabitlemesidir:\n1. Göreceli Başvuru (A1): '=A1*B1' formülünü alt satıra kopyaladığınızda otomatik olarak '=A2*B2' olur.\n2. Mutlak Başvuru ($A$1): Eğer tüm ölçüm gerilimlerini sabit bir referans direnç değerine ($B$1) bölecekseniz formül '=A2/$B$1' olmalıdır. Formülü aşağı çekseniz bile $B$1 hücresi sabit kalır (F4 tuşu sabitlemeyi otomatik yapar).\n3. Karma Başvuru ($A1 veya A$1): Yalnızca satırı veya yalnızca sütunu sabitler."
    ],
    [
      "Mühendislik Hesaplamaları: Ohm Kanunu ve Güç Tablosu",
      "Bir devrede farklı akım (I) ve direnç (R) değerleri için gerilim ($V = I \\cdot R$) ve güç ($P = I^2 \\cdot R$ veya $P = V \\cdot I$) hesabı:\nÖrneğin A sütununda Akım (A), B sütununda Direnç (Ω) varsa; C sütununa '=A2*B2' (Gerilim), D sütununa '=POWER(A2;2)*B2' veya '=A2^2*B2' (Güç) yazılarak binlerce veri noktası saniyeler içinde hesaplanır."
    ],
    [
      "Mantıksal Karar Yapıları: IF, AND, OR (EĞER, VE, YADA)",
      "Mühendislik sistemlerinde sınır durumlarını denetlemek için şartlı mantık kullanılır:\nFormül: '=IF(C2>240; \"KRİTİK GERİLİM\"; \"NORMAL\")'\nİç İçe IF veya IFS (ÇOKUEĞER): Birden fazla çalışma aralığı tanımlamak için (ör. Düşük, Normal, Aşırı Yük).\nBu fonksiyonlar manuel denetim yerine tablonun anomalileri otomatik işaretlemesini sağlar."
    ],
    [
      "Sensör CSV Verisi İçe Aktarma ve Veri Temizleme",
      "ESP32 veya laboratuvar osiloskobundan alınan veriler çoğunlukla 'zaman,gerilim,akim' biçiminde CSV olarak kaydedilir.\n'Dosya > İçe Aktar' seçeneğiyle bu dosya yüklendiğinde ayırıcı türü (virgül, noktalı virgül) seçilir.\n'Verileri Sütunlara Böl' (Split text to columns) aracı tek bir hücreye sıkışmış ham verileri anında bağımsız sütunlara dönüştürür."
    ]
  ],
  "diagram": "Ham Sensör CSV Verisi\n       ↓\n[Dosya > İçe Aktar / Metni Sütunlara Böl]\n       ↓\n[Matris Hücre Düzeni: A (Zaman) | B (Akım) | C (Direnç)]\n       ↓ Formüller: V = B2*C2 | P = (B2^2)*C2 | $R$1 Sabit\n[Dinamik Hesaplama Motoru (Reactive DAG)]\n       ↓ Mantık: =IF(P2>50; \"AŞIRI ISINMA\"; \"GÜVENLİ\")\n[Koşullu Biçimlendirme & Alarm Tablosu]",
  "architecture": "Google Sheets hesaplama motoru, hücreler arasındaki matematiksel bağımlılıkları Yönlü Döngüsüz Çizge (DAG) üzerinde modeller. Bir sensör hücresi güncellendiğinde sadece ona bağlı formüller yeniden hesaplanır, sistem yüksek performans sunar.",
  "example": "Bir fotovoltaik güneş paneli testinde: 100 farklı ışık şiddetinde panelin açık devre gerilimi ve kısa devre akımı ölçülür. A sütununda Işık Şiddeti, B'de Akım, C'de Gerilim bulunur. D sütununda güç '=B2*C2' formülüyle hesaplanır. Alt kısımda '=MAX(D2:D101)' ile maksimum güç noktası (MPP), '=AVERAGE(D2:D101)' ile ortalama üretim anında bulunur.",
  "practice": [
    "50 satırlık örnek gerilim ve direnç tablosu oluşturun; Ohm kanununu mutlak başvuru ($) kullanarak hesaplayın.",
    "Formüllerle '=SUM()', '=AVERAGE()', '=STDEV()' istatistiklerini tablonun altına ekleyin.",
    "IF fonksiyonu ile gücü 10 Watt'ın üzerinde olan satırlara 'SOĞUTUCU GEREKLİ' yazdırın.",
    "CSV formatındaki ham bir sensör dosyasını E-Tabloya aktarıp sütunlara ayırın."
  ],
  "code": "# Google E-Tablo Formül Sözdizimi\n# 1. Ohm Kanunu Gerilim Hesabı:\n=A2 * $B$1\n# 2. Güç Hesabı (P = I^2 * R):\n=POWER(A2; 2) * $B$1\n# 3. Koşullu Durum Kontrolü:\n=IF(D2 > 10; \"AŞIRI YÜK\"; \"NORMAL\")\n# 4. Genel İstatistikler:\n=AVERAGE(D2:D50)\n=STDEV(D2:D50)",
  "prompt": "Elektrik-Elektronik Mühendisliği öğrencisi için Google E-Tablolar üzerinde bir DC Motor Güç ve Verim Hesaplama Tablosu tasarla. Giriş gerilimi, çekilen akım, mekanik tork ve devir sayısı sütunlarını içersin. Göreceli ve mutlak hücre başvurusu kurallarını, verim formülünü ve aşırı ısınma IF koşulunu detaylandır.",
  "quiz": [
    [
      "Hücre başvurusunda '$' işareti (Örn: $C$3) ne anlama gelir?",
      "Formül başka hücrelere kopyalandığında veya sürüklendiğinde ilgili satır ve sütunun sabit kalmasını (mutlak başvuru) sağlar."
    ],
    [
      "Google E-Tablolarda '#DEĞER!' (#VALUE!) hatası neden kaynaklanır?",
      "Matematiksel bir formülde sayı yerine metin karakteri kullanılması gibi uyumsuz veri türü işlemlerinde ortaya çıkar."
    ],
    [
      "'=IF(A1>5; B1*2; B1/2)' formülünün mantığı nedir?",
      "Eğer A1 hücresi 5'ten büyükse B1'i 2 ile çarpar, değilse B1'i 2'ye böler."
    ],
    [
      "CSV (Comma-Separated Values) dosyası ile XLSX/Google Sheets farkı nedir?",
      "CSV yalnızca düz metin ve virgülle ayrılmış ham verileri tutar, formül veya biçimlendirme barındırmaz; Sheets ise formülleri ve görsel düzeni işler."
    ],
    [
      "Bir ölçüm serisindeki en büyük değeri ve aritmetik ortalamayı hangi fonksiyonlar verir?",
      "En büyük değer için MAX(), aritmetik ortalama için AVERAGE() fonksiyonu kullanılır."
    ]
  ],
  "task": "Kendi laboratuvar devreniz veya verilen 30 satırlık test verisi için: Akım, Gerilim, Güç ve Verim değerlerini formüller ve sabit referans hücresi kullanarak hesaplayan, eşik değerleri IF ile denetleyen bir Google E-Tablosu hazırlayın.",
  "goals": [
    "Google E-Tablolarda 2 boyutlu hücre koordinat sistemini ve veri tiplerini hatasız kullanabilmek.",
    "Göreceli ve mutlak ($) hücre başvurularını doğru senaryolarda uygulayabilmek.",
    "Ohm kanunu, güç ve istatistik hesaplamalarını fonksiyonlarla otomatize edebilmek.",
    "IF mantıksal karar fonksiyonu ile otomatik eşik kontrolleri tanımlayabilmek.",
    "Harici cihazlardan gelen CSV verilerini içe aktarıp düzenleyebilmek."
  ],
  "verify": [
    "Formül kopyalandığında sabit kalması gereken hücrelerin kaymadığını ($ doğrulaması) kontrol edin.",
    "Tablodaki bir giriş değeri değiştiğinde ona bağlı güç ve verim sonuçlarının anında güncellendiğini teyit edin.",
    "Hatalı veri girişinde tablonun mantıksal uyarı ürettiğini test edin."
  ],
  "sources": [
    [
      "Google E-Tablolar Fonksiyon Listesi & Dokümantasyonu",
      "https://support.google.com/docs/table/25273"
    ],
    [
      "Mühendislik Hesaplamalarında Tablolama Teknikleri",
      "https://support.google.com/a/users/answer/9300022"
    ]
  ],
  "table": [
    [
      "Fonksiyon",
      "Kullanım Örneği",
      "Mühendislik Amacı",
      "Beklenen Sonuç"
    ],
    [
      "SUM",
      "=SUM(C2:C20)",
      "Toplam enerji tüketimini hesaplama",
      "Hücrelerin sayısal toplamı"
    ],
    [
      "AVERAGE",
      "=AVERAGE(B2:B50)",
      "Ortalama çalışma gerilimini bulma",
      "Aritmetik ortalama değeri"
    ],
    [
      "STDEV",
      "=STDEV(D2:D100)",
      "Sensör gürültüsünü ve ölçüm kararlılığını ölçme",
      "Standart sapma miktarı"
    ],
    [
      "IF",
      "=IF(P2>100; \"ALARM\"; \"OK\")",
      "Kritik limit aşımlarında güvenlik uyarısı",
      "Koşula bağlı metin veya sayı"
    ]
  ]
}

# Week 09: İleri Hesap Tablolama ve Veri Analizi
week09 = {
  "title": "İleri Hesap Tablolama ve Veri Analizi",
  "intro": "Sensör ve deney verilerini ileri analitik araçlarla işleyin: VLOOKUP/XLOOKUP, Pivot Tablolar, Koşullu Biçimlendirme ve dinamik mühendislik grafikleriyle görselleştirin.",
  "group": "Veri",
  "category": "cloud",
  "concepts": [
    [
      "Koşullu Biçimlendirme (Conditional Formatting)",
      "Hücre renginin verinin büyüklüğüne göre otomatik değişmesi (Isı haritası, limit dışı değerlerin kırmızı yanması)."
    ],
    [
      "Arama ve Eşleme Fonksiyonları (VLOOKUP / XLOOKUP)",
      "Bir sensör kodundan veya bileşen numarasından parça kütüphanesindeki teknik özellikleri anında çekme."
    ],
    [
      "Pivot Tablolar (Özet Tablolar)",
      "Binlerce satırlık ham veriyi tek satır kod yazmadan gruplama, ortalamalarını alma ve özet matrisler üretme."
    ],
    [
      "Mühendislik Grafikleri & Trend Çizgileri",
      "Serpilme (Scatter X-Y) grafikleri, doğrusal/polinom regresyon denklemleri ve $R^2$ korelasyon katsayısı."
    ],
    [
      "Veri Doğrulama & Açılır Listeler (Data Validation)",
      "Kullanıcının yanlış veri girmesini engelleyen dinamik açılır menüler ve sayı aralığı kısıtlamaları."
    ],
    [
      "Filtreleme & FILTER / QUERY Fonksiyonları",
      "Tabloyu bozmadan sadece belirli kriterleri (ör. Sıcaklık > 40°C olan testler) dinamik olarak listeleme."
    ]
  ],
  "lessons": [
    [
      "Ders İçeriği · Koşullu Biçimlendirme ile Görsel Telemetri",
      "Bir mühendis yüzlerce satır veriyi tek tek okumaz; gözün anomalileri yakalaması için görsel ipuçları kullanır.\nKoşullu Biçimlendirme (Format > Conditional formatting): Belirli bir kurala göre hücrenin arka planını ve yazı rengini otomatik değiştirir.\nÖrnek: Sıcaklık > 60°C ise kırmızı dolgu, 20°C - 60°C arası yeşil, < 20°C ise mavi dolgu.\nRenk Ölçeği (Color Scale): Hücreleri sıcaklık büyüklüğüne göre kademeli renklendirerek bir Isı Haritası (Heatmap) oluşturur."
    ],
    [
      "Veri Tabanı Mantığı: VLOOKUP ve Modern XLOOKUP",
      "Mühendislik projelerinde veriler tek bir sayfada bulunmaz. Bir sayfada 'Ölçüm Sonuçları', diğer sayfada 'Sensör Özellikleri' yer alır.\nVLOOKUP (DÜŞEYARA): Belirtilen anahtar değeri tablonun ilk sütununda arar ve karşılık gelen sütundaki bilgiyi getirir.\nXLOOKUP (ÇAPRAZARA): Yeni nesil ve çok daha güçlü arama fonksiyonudur. Arama sütunu solda olmak zorunda değildir; bulunamadığında döndürülecek özel mesajı tek seferde yönetir.\nÖrnek: Devreye bağlanan transistör koduna (ör. 'BC547') göre maksimum akım sınırını parametre tablosundan otomatik çekme."
    ],
    [
      "Pivot Tablo (Özet Tablo) ile Büyük Veri Analizi",
      "Bir gün boyunca her saniye kaydedilen 86.400 satırlık sıcaklık verisini nasıl analiz edersiniz?\nPivot Tablo (Ekle > Pivot tablo): Ham verileri sütun, satır ve değer alanlarına sürükleyerek anında gruplar.\nÖrnek: Her bir sensörün saatlik ortalama, maksimum ve minimum değerlerini tek bir özet tabloda saniyeler içinde çıkarır."
    ],
    [
      "Mühendislikte Grafik Çizimi: Scatter (X-Y) ve Regresyon",
      "Mühendislikte çizgi (line) grafiği yerine çoğunlukla Serpilme (Scatter X-Y) grafiği kullanılır. Çünkü hem X hem Y ekseni sayısal birer büyüklüktür (Örn: Gerilim vs. Akım).\nTrend Çizgisi (Trendline): Ölçüm noktalarının arasından geçen en uygun matematiksel doğruyu ($y = mx + b$) çizer.\n$R^2$ Belirlilik Katsayısı: Ölçüm noktalarının doğruya ne kadar uyduğunu gösterir ($R^2 = 1.0$ mükemmel uyumdur). Doğrunun eğimi ($m$) devrenin direncini ($R = V/I$) verir."
    ],
    [
      "Veri Doğrulama ve Dinamik FILTER Fonksiyonu",
      "Veri Doğrulama (Veri > Veri doğrulama): Bir hücreye sadece önceden tanımlanmış bileşen adlarının (Örn: 'Direnç', 'Kapasitör', 'Bobin') girilmesini sağlayan açılır liste (dropdown) oluşturur.\nFILTER Fonksiyonu: '=FILTER(A2:D100; C2:C100 > 50)' formülü, orijinal veriyi bozmadan kriteri sağlayan tüm satırları yan tarafa dinamik yeni bir tablo olarak döker."
    ]
  ],
  "diagram": "[Büyük Ham Sensör Veri Havuzu (Binlerce Satır)]\n         ↙                      ↓                      ↘\n[Koşullu Biçimlendirme]   [XLOOKUP Eşleme]       [Pivot Tablo Özetleme]\n    Isı Haritası &         Bileşen Özellikleri      Sensör / Zaman Bazlı\n    Kritik Limit Kırmızı     ve Parametreler          Gruplanmış Ortalamalar\n         ↘                      ↓                      ↙\n           [Mühendislik Grafiği: Scatter X-Y]\n           [Trend Çizgisi: y = m*x + b & R² Değeri]\n           [Dinamik Gösterge Paneli (Dashboard)]",
  "architecture": "İleri veri analitiğinde ham veri dokunulmaz tutulur; XLOOKUP ile ilişkisel zenginleştirme yapılır, Pivot Tablo ile boyut indirgenir ve Scatter grafikleriyle sistemin transfer fonksiyonu ve doğrusallığı modellenir.",
  "example": "Laboratuvarda bir NTC termistörün sıcaklık-direnç karakteristiği ölçülür. 50 farklı sıcaklıkta direnç kaydedilir. XLOOKUP ile kalibrasyon katsayıları getirilir. Scatter grafiği çizilip üstel trend çizgisi eklenir. Grafiğin matematiksel formülü ve $R^2$ değeri panoya yazdırılır. Koşullu biçimlendirme ile direncin 1 kΩ altına düştüğü aşırı sıcak anlar kırmızı renkle vurgulanır.",
  "practice": [
    "100 satırlık sıcaklık verisine 3 renkli ısı haritası (Koşullu Biçimlendirme) uygulayın.",
    "Bileşen koduna göre tolerans ve maksimum gerilimi çeken bir XLOOKUP formülü yazın.",
    "Büyük bir deney veri setinden Pivot Tablo oluşturarak cihaz bazlı ortalama ve tepe değerleri çıkarın.",
    "X ekseni Akım, Y ekseni Gerilim olan bir Serpilme (Scatter) grafiği çizip lineer trend çizgisi ve formülünü ekleyin."
  ],
  "code": "# İleri Analiz Formülleri\n# 1. Modern Arama ve Eşleme (XLOOKUP):\n=XLOOKUP(A2; 'Katalog'!A:A; 'Katalog'!B:B; \"Bileşen Bulunamadı\")\n# 2. Dinamik Filtreleme:\n=FILTER(A2:E100; (C2:C100 > 40) * (D2:D100 < 12))\n# 3. İki Kriterli Sayım:\n=COUNTIFS(B2:B100; \">220\"; C2:C100; \"<5\")",
  "prompt": "Elektrik-Elektronik Mühendisliği öğrencileri için Google E-Tablolar'da V-I (Gerilim-Akım) Karakteristik Eğrisi Analiz Şablonu oluştur. X-Y Serpilme grafiği ayarları, trend çizgisi üzerinden direnç ($R$) hesabı, $R^2$ hata payı yorumu ve anormal ölçümleri kırmızıya boyayan koşullu biçimlendirme kurallarını detaylandır.",
  "quiz": [
    [
      "Mühendislik ölçümlerinde Çizgi (Line) grafiği yerine neden Serpilme (Scatter X-Y) grafiği tercih edilir?",
      "Çünkü mühendislikte her iki eksen de oransal sayısal büyüklükleri temsil eder; çizgi grafiği ise X eksenini metin/kategori olarak ele alır."
    ],
    [
      "Bir trend çizgisinde $R^2 = 0.998$ değeri ne anlama gelir?",
      "Matematiksel modelin ölçüm noktalarına mükemmel seviyede uyduğunu ve deneysel hatanın çok düşük olduğunu gösterir."
    ],
    [
      "XLOOKUP fonksiyonunun VLOOKUP'a göre en büyük üstünlüğü nedir?",
      "Aranan sütunun en solda olma zorunluluğunun bulunmaması, sağdan sola arama yapabilmesi ve hata durumunda doğrudan varsayılan değer dönebilmesidir."
    ],
    [
      "Koşullu Biçimlendirmede 'Renk Ölçeği' (Color Scale) ne işe yarar?",
      "Hücre değerlerinin minimum ve maksimumuna göre otomatik degrade renk atayarak tablodan canlı bir Isı Haritası (Heatmap) üretir."
    ],
    [
      "Pivot Tablo hangi durumda kullanılmalıdır?",
      "Çok sayıda satırdan oluşan ham verileri belirli kategorilere göre (ör. sensör türü, gün, cihaz) hızlıca gruplayıp özetlemek için."
    ]
  ],
  "task": "Verilen laboratuvar ölçüm seti üzerinden: XLOOKUP ile bileşen kütüphanesini bağlayan, Pivot tablo ile saatlik tüketim özetini çıkaran ve X-Y grafiği üzerinden trend çizgisi denklemini hesaplayan profesyonel bir 'Analiz Panosu' (Dashboard) hazırlayın.",
  "goals": [
    "Koşullu biçimlendirme ve renk ölçekleri ile telemetri ısı haritaları oluşturabilmek.",
    "XLOOKUP ile ilişkisel tablolar arasında dinamik veri eşleştirmesi yapabilmek.",
    "Pivot Tablo kullanarak binlerce satırlık mühendislik verisini özetleyebilmek.",
    "Serpilme (Scatter X-Y) grafikleriyle devre parametrelerinin transfer fonksiyonunu ve $R^2$ değerini saptayabilmek.",
    "Veri doğrulama ile kullanıcı hatalarını kaynağında engelleyebilmek."
  ],
  "verify": [
    "Scatter grafiğinde trend çizgisinin denklem ve R² değerinin görünür olduğunu kontrol edin.",
    "Açılır menüden farklı bir sensör seçildiğinde XLOOKUP ile tüm teknik özelliklerin dinamik değiştiğini doğrulayın.",
    "Pivot Tablonun kaynak veri güncellendiğinde doğru özet değerler ürettiğini test edin."
  ],
  "sources": [
    [
      "Google Workspace Veri Analizi ve Pivot Tablo Kılavuzu",
      "https://support.google.com/docs/answer/1272900"
    ],
    [
      "Mühendislikte Regresyon ve Grafiksel Analiz",
      "https://support.google.com/docs/answer/63824"
    ]
  ],
  "table": [
    [
      "Analiz Aracı",
      "Kullanım Yeri",
      "Mühendislik Kararı",
      "Temel Avantajı"
    ],
    [
      "Koşullu Biçimlendirme",
      "Sıcaklık ve Gerilim tabloları",
      "Sistemin güvenli çalışma bölgesinde olup olmadığını saptama",
      "Gözle anında fark edilen renkli uyarılar"
    ],
    [
      "XLOOKUP",
      "Katalog ve envanter eşleme",
      "Ölçülen parçanın fabrika sınır değerlerini bulma",
      "Hızlı, esnek ve hatasız veri birleştirme"
    ],
    [
      "Pivot Tablo",
      "Aylık/Günlük telemetri kayıtları",
      "Hangi cihazın daha çok enerji tükettiğini belirleme",
      "Formülsüz dinamik gruplama ve özetleme"
    ],
    [
      "Scatter & Trendline",
      "Diyot, transistör, sensör testleri",
      "Direnç ($R$), iletkenlik veya duyarlılık katsayısı çıkarma",
      "Matematiksel modelleme ve formül çıkarma"
    ]
  ]
}

# Replace or append weeks 7, 8, 9
new_weeks = weeks[:6] + [week07, week08, week09]

with open(weeks_path, "w", encoding="utf-8") as f:
  json.dump(new_weeks, f, ensure_ascii=False, indent=2)

print("weeks.json successfully updated with 9 weeks!")
