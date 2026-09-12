"""Static, progressively enhanced history section and original SVG diagrams."""
import json
from html import escape as e
from pathlib import Path

ERAS={'before':'TRANSİSTÖR ÖNCESİ','turn':'DÖNÜM NOKTASI','after':'TRANSİSTÖR SONRASI'}

def illustration(kind):
    # Conceptual drawings, not archival photographs or scale representations.
    drawings={
      'abacus':'<rect x="55" y="35" width="210" height="150" rx="8"/>'+''.join(f'<path d="M65 {y}h190"/>'+''.join(f'<rect x="{x}" y="{y-9}" width="17" height="18" rx="7" fill="#e9ad65"/>' for x in (85,110,160,185)) for y in (65,100,135,165)),
      'gears':''.join(f'<g transform="translate({x} {y})"><circle r="{r}"/>'+''.join(f'<path d="M0 -{r-5}v-17" transform="rotate({a})"/>' for a in range(0,360,45))+f'<circle r="{r//3}"/></g>' for x,y,r in [(120,110,48),(211,125,31)]),
      'program':'<rect x="75" y="30" width="170" height="160" rx="8"/><path d="M100 60h85M100 86h120M100 112h55M100 138h105M100 164h70"/><path d="m40 85-20 25 20 25m240-50 20 25-20 25"/>',
      'tubes':''.join(f'<g transform="translate({x} 0)"><rect x="0" y="45" width="54" height="115" rx="26"/><path d="M10 163h34M17 167v24m20-24v24M27 145V85m-12 40 24-15-24-15 24-15" stroke="#e9ad65"/></g>' for x in (55,133,211)),
      'transistor':'<path d="M65 162h190M130 162v30m60-30v30"/><rect x="110" y="130" width="100" height="30" rx="5" fill="#24483e"/><path d="m160 42-28 84m28-84 30 84" stroke="#e9ad65"/><path d="M160 42V22M67 125l45 18m140-18-42 18"/><circle cx="160" cy="42" r="6" fill="#e9ad65"/>',
      'chip':'<rect x="100" y="52" width="120" height="120" rx="12" fill="#213954"/><rect x="126" y="78" width="68" height="68" rx="4"/>'+''.join(f'<path d="M{x} 32v20m0 120v20M80 {x-50}h20m120 0h20"/>' for x in (120,145,170,195)),
      'desktop':'<rect x="58" y="30" width="205" height="132" rx="10"/><rect x="74" y="45" width="173" height="91" rx="3" fill="#213954"/><path d="M139 163v20h43v-20M95 185h130M68 204h187M92 72h65m-65 18h105m-105 18h42"/>',
      'network':'<circle cx="160" cy="107" r="43"/><ellipse cx="160" cy="107" rx="19" ry="43"/><path d="M118 107h84M126 83h68m-68 48h68M115 75 63 48m141 31 53-31M117 142l-54 34m142-34 52 34"/>'+''.join(f'<rect x="{x}" y="{y}" width="40" height="28" rx="4"/>' for x,y in [(28,26),(252,26),(28,168),(252,168)]),
      'phone':'<rect x="108" y="20" width="104" height="186" rx="18"/><path d="M142 36h36M119 169h82"/><circle cx="160" cy="187" r="6"/>'+''.join(f'<rect x="{x}" y="{y}" width="21" height="21" rx="4" fill="#213954"/>' for x in (125,173) for y in (61,98,135)),
      'board':'<rect x="47" y="42" width="226" height="145" rx="12" fill="#183e37"/><rect x="125" y="85" width="67" height="64" rx="4"/><path d="M67 64h183M77 87v75h29m95-55h49m-49 18h49"/>'+''.join(f'<circle cx="{x}" cy="64" r="3" fill="#e9ad65"/>' for x in range(73,250,16))+'<rect x="44" y="99" width="40" height="31"/><rect x="218" y="154" width="41" height="35"/>',
      'ai':''.join(f'<path d="M{x1} {y1} {x2} {y2}" opacity=".65"/>' for x1,y1 in [(60,65),(60,155)] for x2,y2 in [(155,40),(155,110),(155,180)])+''.join(f'<path d="M155 {y1} 260 {y2}" opacity=".65"/>' for y1 in (40,110,180) for y2 in (75,150))+''.join(f'<circle cx="{x}" cy="{y}" r="15" fill="#213954"/>' for x,y in [(60,65),(60,155),(155,40),(155,110),(155,180),(260,75),(260,150)])
    }
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 225"><rect width="320" height="225" rx="16" fill="#102440"/><g fill="none" stroke="#9cbfe8" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">'+drawings[kind]+'</g></svg>'

def render_history(root: Path):
    events=json.loads((root/'content/history.json').read_text(encoding='utf-8'))
    folder=root/'assets/images/history';folder.mkdir(parents=True,exist_ok=True)
    for kind in {event['art'] for event in events}:
        (folder/f'{kind}.svg').write_text(illustration(kind),encoding='utf-8')
    rail=[];panels=[]
    for i,event in enumerate(events):
        rail.append(f'<li class="history-stop {event["era"]}"><a id="history-link-{i}" href="#history-event-{i}" class="history-link"><span class="history-year">{e(event["year"])}</span><span class="history-dot" aria-hidden="true"></span><span class="history-name">{e(event["title"].split(":")[0])}</span></a></li>')
        panels.append(f'''<article class="history-event {event['era']}" id="history-event-{i}" aria-labelledby="history-heading-{i}"><figure><img src="../assets/images/history/{event['art']}.svg" width="320" height="225" alt="{e(event['title'])} için temsili çizim"><figcaption>Temsili çizim · tarihî fotoğraf değildir.</figcaption></figure><div><span class="history-era">{ERAS[event['era']]} · {e(event['year'])}</span><h3 id="history-heading-{i}">{e(event['title'])}</h3><p>{e(event['text'])}</p><p class="history-impact"><strong>Ne değişti?</strong> {e(event['impact'])}</p><a class="history-source" href="{e(event['source'])}">{e(event['sourceName'])} ↗</a></div></article>''')
    return f'''<div class="history" data-history><p class="history-intro">Dişlilerden yarı iletkenlere, oda büyüklüğündeki makinelerden cebimizdeki bilgisayara. Çizgi üzerindeki bir tarihi seçerek keşfedin.</p><div class="history-jumps" hidden><button type="button" data-history-jump="0">← Transistör öncesi</button><button type="button" data-history-jump="5" class="history-revolution">1947 · Devrim</button><button type="button" data-history-jump="6">Transistör sonrası →</button><button type="button" data-history-jump="13">Günümüze git ↗</button></div><p class="history-hint">Yatay çizgiyi kaydırın · Tarihler kronolojiktir; aralıklar zaman ölçeğinde değildir.</p><nav class="history-rail" aria-label="Bilgisayar tarihi dönüm noktaları"><ol>{''.join(rail)}</ol></nav><div class="history-panels">{''.join(panels)}</div><div class="history-controls" hidden><button type="button" data-history-prev>← Önceki</button><output data-history-status aria-live="polite" aria-atomic="true"></output><button type="button" data-history-next>Sonraki →</button></div><div class="history-comparison"><h3>1947 neden bir kırılma noktası?</h3><div class="history-compare-grid"><div><span class="history-era">ÖNCESİ · VAKUM TÜPÜ</span><p>Elektron akışını vakum içinde kontrol eder. Isıtılan katot, yüksek ısı ve büyük fiziksel yapılar sistem tasarımını sınırlar.</p></div><div><span class="history-era">SONRASI · TRANSİSTÖR</span><p>Akımı yarı iletkende kontrol eder. Küçülme ve düşük güçlü devreler için yol açar; entegrasyonla aynı yongada çok sayıda eleman üretilebilir.</p></div></div><p class="history-hint">Geçiş bir gecede olmadı: 1947 icat → 1950’ler transistörlü bilgisayarlar → 1958–1959 entegre devre → 1971 mikroişlemci. Tüpler özel uygulamalarda kullanılmaya devam eder.</p></div></div>'''
