"""Accessible, progressively enhanced system architecture for week one."""
from html import escape as e

NODES = {
    "general": [
        ("input", "Girdi", "Input", "Sensör, klavye veya ağdan sisteme veri gelir.", "sensor"),
        ("process", "İşleme", "Processing", "CPU veya MCU komutları yürütür ve karar üretir.", "cpu"),
        ("memory", "Bellek", "Working Memory", "RAM, işlem sırasında gereken geçici veriyi tutar.", "memory"),
        ("storage", "Depolama", "Storage", "SSD veya Flash, kaydedilen veriyi enerji kesilince de korur.", "storage"),
        ("output", "Çıktı", "Output", "Ekran, hoparlör veya aktüatör sonucu dış dünyaya taşır.", "output"),
    ],
    "electronic": [
        ("sensor", "Sensör", "Sensor", "Sıcaklık gibi fiziksel bir büyüklüğü elektriksel veriye dönüştürür.", "sensor"),
        ("adc", "ADC", "Analog-to-Digital Converter", "Analog gerilimi işlemcinin kullanabileceği sayısal değere çevirir.", "adc"),
        ("processor", "CPU / MCU", "Central Processing Unit / Microcontroller Unit", "Ölçümü işler, eşikle karşılaştırır ve sistem davranışını belirler.", "cpu"),
        ("ram", "RAM", "Random Access Memory", "Anlık ölçümü ve ara hesap sonuçlarını geçici olarak tutar.", "memory"),
        ("flash", "Flash / SSD", "Non-volatile Storage", "Kaydedilmesi istenen ölçüm ve programı kalıcı olarak saklar.", "storage"),
        ("actuator", "Ekran / Aktüatör", "Display / Actuator", "Sonucu gösterir veya fan, motor ve LED gibi fiziksel bir çıkışı çalıştırır.", "output"),
    ],
}

def icon(kind):
    paths = {
        "sensor": '<path d="M22 43h20m-10-10v20M55 32c10 6 10 19 0 25m9-34c18 12 18 31 0 43"/><circle cx="32" cy="43" r="8"/>',
        "adc": '<path d="M18 54h14l8-24 10 36 9-24h19"/><path d="M18 20h60M18 70h60"/>',
        "cpu": '<rect x="25" y="25" width="46" height="46" rx="7"/><rect x="36" y="36" width="24" height="24" rx="3"/><path d="M34 15v10m14-10v10m14-10v10M34 71v10m14-10v10m14-10v10M15 34h10m-10 14h10m-10 14h10M71 34h10M71 48h10M71 62h10"/>',
        "memory": '<rect x="15" y="29" width="66" height="38" rx="5"/><rect x="25" y="38" width="13" height="18" rx="2"/><rect x="43" y="38" width="13" height="18" rx="2"/><rect x="61" y="38" width="10" height="18" rx="2"/><path d="M24 67v8m12-8v8m12-8v8m12-8v8m12-8v8"/>',
        "storage": '<rect x="22" y="17" width="52" height="62" rx="7"/><path d="M32 31h32M32 44h32M32 57h20"/><circle cx="62" cy="65" r="3"/>',
        "output": '<rect x="14" y="19" width="68" height="45" rx="5"/><path d="M39 65v11h18V65M30 77h36"/><path d="m35 42 8 8 18-20"/>',
    }
    return f'<svg viewBox="0 0 96 96" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{paths[kind]}</g></svg>'

def node_html(item):
    ident, title, english, description, art = item
    return f'''<button type="button" class="architecture-node node-{e(ident)}" data-architecture-node="{e(ident)}" data-title="{e(title)}" data-english="{e(english)}" data-description="{e(description)}" aria-pressed="false">{icon(art)}<span><strong>{e(title)}</strong><small lang="en">{e(english)}</small></span></button>'''

def render_architecture():
    general = ''.join(node_html(item) for item in NODES["general"])
    electronic = ''.join(node_html(item) for item in NODES["electronic"])
    return f'''<link rel="stylesheet" href="../css/architecture.css"><link rel="stylesheet" href="../css/architecture-mobile.css"><div class="architecture-explorer" data-architecture>
      <p class="architecture-lead">Bir bilgisayarı yalnızca parça listesi olarak değil, <strong>verinin dönüştüğü bir sistem</strong> olarak inceleyin. Bir bileşene dokunarak görevini görün veya sıcaklık verisinin yolculuğunu adım adım çalıştırın.</p>
      <div class="architecture-tabs" role="tablist" aria-label="Mimari görünümü"><button type="button" role="tab" id="architecture-tab-general" aria-controls="architecture-general" aria-selected="true" data-architecture-tab="general">Genel bilgi işleme modeli</button><button type="button" role="tab" id="architecture-tab-electronic" aria-controls="architecture-electronic" aria-selected="false" data-architecture-tab="electronic">Elektronik sistem karşılığı</button></div>
      <div class="architecture-panel" id="architecture-general" role="tabpanel" aria-labelledby="architecture-tab-general" data-architecture-panel="general"><div class="architecture-diagram architecture-general" aria-label="Girdi, işleme, bellek, depolama ve çıktı arasındaki ilişki">{general}<span class="architecture-link link-input-process" aria-hidden="true">→</span><span class="architecture-link link-process-memory" aria-hidden="true">↔</span><span class="architecture-link link-process-storage" aria-hidden="true">↕</span><span class="architecture-link link-process-output" aria-hidden="true">→</span></div><p class="architecture-reading"><strong>Okuma:</strong> Veri girdiden gelir; işlemci çalışma belleğiyle sürekli alışveriş yapar. Yalnızca kaydedilmesi gereken bilgi depolamaya yazılır. Sonuç kullanıcıya veya fiziksel dünyaya çıktı olarak iletilir.</p></div>
      <div class="architecture-panel" id="architecture-electronic" role="tabpanel" aria-labelledby="architecture-tab-electronic" data-architecture-panel="electronic" hidden><div class="architecture-diagram architecture-electronic" aria-label="Sensör, ADC, CPU veya MCU, RAM, Flash veya SSD ve ekran veya aktüatör arasındaki ilişki">{electronic}<span class="architecture-link link-sensor-adc" aria-hidden="true">→</span><span class="architecture-link link-adc-processor" aria-hidden="true">→</span><span class="architecture-link link-processor-ram" aria-hidden="true">↔</span><span class="architecture-link link-processor-flash" aria-hidden="true">↕</span><span class="architecture-link link-processor-actuator" aria-hidden="true">→</span></div><p class="architecture-reading"><strong>Okuma:</strong> Analog sensörde ADC dönüşümü ayrı bir adım olabilir; dijital sensör bu işi kendi içinde yapabilir. MCU, RAM ve Flash’ı aynı yongada barındırabilir. Güçlü bir motor veya fan için uygun sürücü devresi gerekir.</p></div>
      <aside class="architecture-inspector" data-architecture-inspector aria-live="polite"><span class="eyebrow">SEÇİLİ BİLEŞEN</span><h3 data-architecture-title>Sistemdeki bir bileşeni seçin</h3><p class="architecture-english" data-architecture-english lang="en">Input → Processing ↔ Memory → Output</p><p data-architecture-description>Şemadaki kartlardan biri seçildiğinde görevini ve İngilizce karşılığını burada göreceksiniz.</p></aside>
      <section class="data-journey" aria-labelledby="data-journey-title"><div class="data-journey-heading"><div><span class="eyebrow">ETKİLEŞİMLİ SENARYO</span><h3 id="data-journey-title">Bir sıcaklık ölçümünün yolculuğu</h3></div><span class="journey-value">24.0 °C</span></div><ol class="journey-steps"><li data-journey-step="0"><span>1</span><strong>Sensör</strong><small>Fiziksel büyüklük</small></li><li data-journey-step="1"><span>2</span><strong>ADC</strong><small>Sayısal ölçüm</small></li><li data-journey-step="2"><span>3</span><strong>CPU / MCU</strong><small>İşleme ve karar</small></li><li data-journey-step="3"><span>4</span><strong>RAM</strong><small>Geçici çalışma</small></li><li data-journey-step="4"><span>5</span><strong>Flash / SSD</strong><small>İsteğe bağlı kayıt</small></li><li data-journey-step="5"><span>6</span><strong>Ekran / Fan</strong><small>Sonuç ve eylem</small></li></ol><div class="journey-controls" hidden><button type="button" data-journey-prev>← Önceki adım</button><button type="button" class="primary" data-journey-next>Başlat →</button><button type="button" data-journey-reset>Sıfırla</button></div><div class="journey-explanation" role="status" aria-live="polite"><strong data-journey-title>Hazır</strong><p data-journey-text>Başlat düğmesine basarak verinin sensörden çıktıya yolculuğunu izleyin.</p></div><noscript><p>Sıra: Sensör → ADC → CPU/MCU ↔ RAM → isteğe bağlı Flash/SSD kaydı → ekran veya aktüatör.</p></noscript></section>
      <div class="architecture-map"><h3>İki modeli eşleştir</h3><div><span>Girdi <small lang="en">Input</small></span><b>→</b><span>Sensör + ADC <small lang="en">Sensor + ADC</small></span></div><div><span>İşleme <small lang="en">Processing</small></span><b>→</b><span>CPU / MCU</span></div><div><span>Bellek <small lang="en">Memory</small></span><b>→</b><span>RAM</span></div><div><span>Depolama <small lang="en">Storage</small></span><b>→</b><span>Flash / SSD</span></div><div><span>Çıktı <small lang="en">Output</small></span><b>→</b><span>Ekran / Aktüatör <small lang="en">Display / Actuator</small></span></div></div>
      <p class="architecture-note"><strong>Mühendislik notu:</strong> Bu şema veri akışını öğrenmek için sadeleştirilmiştir. Gerçek sistemlerde veri yolları çift yönlü olabilir; DMA, önbellek, çevre birimleri ve sürücüler gibi ek katmanlar bulunabilir.</p>
    </div><script src="../js/architecture.js"></script>'''
