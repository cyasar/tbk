"""Interactive Web Technologies History component and vector illustrations for Week 4."""
import json
from html import escape as e
from pathlib import Path

WEB_ERAS = {
    'origin': 'WWW\'NİN DOĞUŞU',
    'web1': 'WEB 1.0 (SALT OKUNUR)',
    'web2': 'WEB 2.0 (SOSYAL & AJAX)',
    'modern': 'MODERN WEB & SPA',
    'future': 'WEB 3.0 & YAPAY ZEKÂ'
}

def web_illustration(kind):
    drawings = {
        'nextcube': (
            '<rect x="80" y="45" width="160" height="135" rx="8" fill="#182c44"/>'
            '<rect x="95" y="60" width="130" height="85" rx="4" fill="#0d1b2a"/>'
            '<path d="M110 85h60M110 100h85M110 115h40" stroke="#f4c38b"/>'
            '<rect x="140" y="180" width="40" height="15" fill="#182c44"/>'
            '<rect x="110" y="195" width="100" height="8" rx="4" fill="#9cbfe8"/>'
            '<circle cx="215" cy="72" r="3" fill="#24705b"/>'
        ),
        'firstweb': (
            '<rect x="40" y="30" width="240" height="165" rx="10" fill="#182c44"/>'
            '<rect x="55" y="55" width="210" height="125" rx="4" fill="#0d1b2a"/>'
            '<path d="M55 45h210M70 40h4M80 40h4M90 40h4"/>'
            '<text x="65" y="75" fill="#9cbfe8" font-family="monospace" font-size="10">http://info.cern.ch</text>'
            '<path d="M65 95h120M65 110h180M65 125h140M65 140h160M65 155h90" stroke="#f4c38b" stroke-width="2"/>'
        ),
        'browser_mosaic': (
            '<rect x="45" y="30" width="230" height="165" rx="8" fill="#182c44"/>'
            '<rect x="58" y="68" width="204" height="112" rx="4" fill="#0d1b2a"/>'
            '<path d="M45 52h230M60 42h12M78 42h12M96 42h12"/>'
            '<rect x="70" y="80" width="60" height="45" rx="4" fill="#213954"/>'
            '<circle cx="85" cy="95" r="5" fill="#f4c38b"/>'
            '<path d="M75 118l15-15 12 12 12-8 12 11" stroke="#9cbfe8"/>'
            '<path d="M145 85h100M145 100h85M145 115h95M70 140h175M70 155h130" stroke="#f4c38b"/>'
        ),
        'w3c': (
            '<circle cx="160" cy="112" r="65" fill="#182c44"/>'
            '<ellipse cx="160" cy="112" rx="28" ry="65"/>'
            '<path d="M98 112h124M107 80h106M107 144h106"/>'
            '<rect x="110" y="90" width="100" height="44" rx="6" fill="#0d1b2a" stroke="#f4c38b" stroke-width="2"/>'
            '<text x="160" y="118" fill="#f4c38b" font-weight="bold" font-family="sans-serif" font-size="18" text-anchor="middle">W3C</text>'
        ),
        'web1': (
            '<rect x="50" y="30" width="220" height="165" rx="8" fill="#182c44"/>'
            '<rect x="65" y="60" width="190" height="120" rx="4" fill="#0d1b2a"/>'
            '<path d="M80 80h90M80 95h140M80 110h110M80 125h150" stroke="#9cbfe8"/>'
            '<rect x="175" y="75" width="65" height="35" rx="4" fill="#213954"/>'
            '<text x="207" y="96" fill="#f4c38b" font-family="monospace" font-size="9" text-anchor="middle">.GIF</text>'
            '<text x="160" y="160" fill="#9cbfe8" font-family="monospace" font-size="11" text-anchor="middle">&lt;HTML 1.0&gt; Read-Only</text>'
        ),
        'web2': (
            '<circle cx="110" cy="100" r="40" fill="#182c44"/>'
            '<circle cx="210" cy="100" r="40" fill="#213954"/>'
            '<path d="M110 70c20 0 35 15 35 30s-15 30-35 30M210 70c-20 0-35 15-35 30s15 30 35 30" stroke="#f4c38b" stroke-width="3"/>'
            '<text x="110" y="105" fill="#9cbfe8" font-size="12" font-weight="bold" text-anchor="middle">AJAX</text>'
            '<text x="210" y="105" fill="#f4c38b" font-size="12" font-weight="bold" text-anchor="middle">Sosyal</text>'
            '<path d="M125 155h70M160 145l15 10-15 10" stroke="#f4c38b" stroke-width="2"/>'
            '<text x="160" y="185" fill="#9cbfe8" font-family="sans-serif" font-size="11" text-anchor="middle">Read + Write (Katılımcı)</text>'
        ),
        'html5_node': (
            '<rect x="60" y="45" width="90" height="120" rx="8" fill="#182c44"/>'
            '<rect x="170" y="45" width="90" height="120" rx="8" fill="#182c44"/>'
            '<text x="105" y="95" fill="#e95420" font-size="20" font-weight="bold" text-anchor="middle">HTML5</text>'
            '<text x="105" y="125" fill="#9cbfe8" font-size="10" text-anchor="middle">İstemci (Client)</text>'
            '<text x="215" y="95" fill="#24705b" font-size="20" font-weight="bold" text-anchor="middle">Node</text>'
            '<text x="215" y="125" fill="#9cbfe8" font-size="10" text-anchor="middle">Sunucu (Server)</text>'
            '<path d="M150 105h20M160 95l10 10-10 10" stroke="#f4c38b"/>'
        ),
        'react_spa': (
            '<ellipse cx="160" cy="112" rx="65" ry="24" fill="none" stroke="#0078d4" stroke-width="3" transform="rotate(30 160 112)"/>'
            '<ellipse cx="160" cy="112" rx="65" ry="24" fill="none" stroke="#0078d4" stroke-width="3" transform="rotate(-30 160 112)"/>'
            '<ellipse cx="160" cy="112" rx="65" ry="24" fill="none" stroke="#0078d4" stroke-width="3" transform="rotate(90 160 112)"/>'
            '<circle cx="160" cy="112" r="10" fill="#0078d4"/>'
            '<text x="160" y="195" fill="#9cbfe8" font-family="sans-serif" font-size="11" text-anchor="middle">Tek Sayfa Uygulamaları (SPA)</text>'
        ),
        'web3_ai': (
            '<circle cx="100" cy="100" r="28" fill="#182c44"/>'
            '<circle cx="220" cy="100" r="28" fill="#182c44"/>'
            '<circle cx="160" cy="60" r="24" fill="#213954"/>'
            '<circle cx="160" cy="140" r="24" fill="#213954"/>'
            '<path d="M100 100l60-40 60 40-60 40zM160 60v80" stroke="#f4c38b" stroke-width="2"/>'
            '<text x="160" y="105" fill="#ffffff" font-weight="bold" font-size="12" text-anchor="middle">AI &amp; Wasm</text>'
            '<text x="160" y="190" fill="#9cbfe8" font-family="sans-serif" font-size="11" text-anchor="middle">Semantik Ağ &amp; Akıllı Ajanlar</text>'
        )
    }
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 225"><rect width="320" height="225" rx="16" fill="#102440"/><g fill="none" stroke="#9cbfe8" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{drawings[kind]}</g></svg>'

def render_web_history(root: Path):
    events = json.loads((root / 'content/web_history.json').read_text(encoding='utf-8'))
    folder = root / 'assets/images/web_history'
    folder.mkdir(parents=True, exist_ok=True)
    for event in events:
        kind = event['art']
        (folder / f'{kind}.svg').write_text(web_illustration(kind), encoding='utf-8')

    rail = []
    panels = []
    for i, event in enumerate(events):
        rail.append(f'''<li class="history-stop {event["era"]}">
          <a id="web-history-link-{i}" href="#web-history-event-{i}" class="history-link">
            <span class="history-year">{e(event["year"])}</span>
            <span class="history-dot" aria-hidden="true"></span>
            <span class="history-name">{e(event["title"].split(":")[0])}</span>
          </a>
        </li>''')

        panels.append(f'''<article class="history-event {event['era']}" id="web-history-event-{i}" aria-labelledby="web-history-heading-{i}">
          <figure>
            <img src="../assets/images/web_history/{event['art']}.svg" width="320" height="225" alt="{e(event['title'])} için temsili çizim">
            <figcaption>Temsili çizim · tarihî fotoğraf değildir.</figcaption>
          </figure>
          <div>
            <span class="history-era">{WEB_ERAS.get(event['era'], 'WEB TARİHİ')} · {e(event['year'])}</span>
            <h3 id="web-history-heading-{i}">{e(event['title'])}</h3>
            <p>{e(event['text'])}</p>
            <p class="history-impact"><strong>Ne değişti?</strong> {e(event['impact'])}</p>
            <a class="history-source" href="{e(event['source'])}">{e(event['sourceName'])} ↗</a>
          </div>
        </article>''')

    return f'''<div class="history web-history" data-web-history>
      <p class="history-intro">CERN laboratuvarındaki ilk NeXT Cube sunucusundan modern yapay zekâ entegreli Web 3.0 platformlarına. Zaman çizgisi üzerindeki duraklara tıklayarak webin evrimini keşfedin.</p>
      
      <div class="history-jumps" hidden>
        <button type="button" data-web-jump="0">← 1989 · Tim Berners-Lee & WWW</button>
        <button type="button" data-web-jump="4" class="history-revolution">1995 · Web 1.0 (Salt Okunur)</button>
        <button type="button" data-web-jump="5">2004 · Web 2.0 (AJAX & Sosyal)</button>
        <button type="button" data-web-jump="8">2020+ · Web 3.0 & Yapay Zekâ →</button>
      </div>

      <p class="history-hint">Yatay çizgiyi kaydırın · Tarihler kronolojiktir; aralıklar zaman ölçeğinde değildir.</p>
      <nav class="history-rail" aria-label="Web teknolojileri tarihi dönüm noktaları">
        <ol>{''.join(rail)}</ol>
      </nav>

      <div class="history-panels">
        {''.join(panels)}
      </div>

      <div class="history-controls" hidden>
        <button type="button" data-web-prev>← Önceki Dönem</button>
        <output data-web-status aria-live="polite" aria-atomic="true"></output>
        <button type="button" data-web-next>Sonraki Dönem →</button>
      </div>

      <div class="history-comparison">
        <h3>Web 1.0, Web 2.0 ve Web 3.0 Karşılaştırması</h3>
        <div class="history-compare-grid" style="grid-template-columns: repeat(3, 1fr);">
          <div>
            <span class="history-era" style="color:var(--history-warm)">WEB 1.0 (1989–2004)</span>
            <strong>Salt Okunur Web (Read-Only)</strong>
            <p>Statik HTML sayfaları, GIF'ler, misafir defterleri. Kullanıcı yalnızca bilgi tüketicisidir; sunucuya içerik besleyemez.</p>
          </div>
          <div>
            <span class="history-era" style="color:var(--accent)">WEB 2.0 (2004–2020)</span>
            <strong>Okur-Yazar Web (Read-Write)</strong>
            <p>AJAX, REST API'ler, Wikipedia, sosyal ağlar, YouTube. Sayfa yenilenmeden arka planda asenkron veri alışverişi ve kullanıcı üretimli içerik çağı.</p>
          </div>
          <div>
            <span class="history-era" style="color:#24705b">WEB 3.0 (2020+)</span>
            <strong>Semantik & Akıllı Web (Read-Write-Execute)</strong>
            <p>Makinelerin anladığı bağlantılı veriler (Linked Data), WebAssembly (Wasm yüksek performans), merkeziyetsiz protokoller ve Yapay Zekâ ajanları.</p>
          </div>
        </div>
      </div>
    </div>'''
