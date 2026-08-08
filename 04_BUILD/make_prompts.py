#!/usr/bin/env python3
"""
GÖRSEL PROMPT KÜTÜPHANESİNİ ÜRET
================================================================================
    python3 04_BUILD/make_prompts.py            üret (MD + HTML)
    python3 04_BUILD/make_prompts.py --check    bayat mı / senkron mu

Çıktı:
    07_ASSETS/IMAGE_PROMPT_LIBRARY.md     — okunabilir kayıt
    07_ASSETS/IMAGE_PROMPT_LIBRARY.html   — kurucunun çalışma arayüzü,
                                            kopyalama düğmeleriyle

PROMPT ÜRETİLİR, ELLE YAZILMAZ (Bestiarium D7 / karar K16). Üslup gövdesi
`imagespec.py`'de TEK YERDE durur; değişirse 68 prompt birlikte değişir.
"Tek çizgi dili" şartı ancak böyle tutulabilir.

AKIŞ:
    IMAGE_PROMPT_LIBRARY.html  →  kurucu · GPT Image  →  07_ASSETS/raw/*.png
                               →  convert_images.py   →  07_ASSETS/processed/
                               →  images.py --measure →  06_REPORTS/tracked/

Kurucudan KDP'ye hazır dosya İSTENMEZ. Ham çıktı PNG'dir; üretim formatını
hat türetir (karar K5). Ham dosyanın üzerine ASLA yazılmaz.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb
import imagespec as spec

MD_OUT = os.path.join(mb.ASSETS, "IMAGE_PROMPT_LIBRARY.md")
HTML_OUT = os.path.join(mb.ASSETS, "IMAGE_PROMPT_LIBRARY.html")


# =============================================================================
# KAYIT ÜRETİMİ
# =============================================================================

def build_records() -> list[dict]:
    index = mb.load_stories()
    cultures = mb.load_cultures()
    stories = [s for s in index.get("stories", []) if s.get("status") != "dropped"]
    stories.sort(key=lambda s: s.get("number") or 999)
    locked = [c for c in cultures.get("cultures", []) if c.get("status") == "locked"]
    locked.sort(key=lambda c: c["name"])

    records = []

    # --- 45 hikâye açılışı ---
    k = spec.KINDS["story"]
    for i in range(1, k["count"] + 1):
        story = stories[i - 1] if i <= len(stories) else None
        sid = f"story-{i:03d}"
        # ⚠ ÖLÜ REFERANS DÜZELTMESİ (Faz 1). Burada eskiden `story.imagePrompt`
        # okunuyordu; oysa story_index.schema.json `additionalProperties: false`
        # taşır ve `imagePrompt` diye bir alan TANIMLI DEĞİLDİR — yani o dal
        # hiçbir koşulda çalışamazdı. Sessizce başlığa düşüyordu ve kimse
        # farkı göremiyordu. Konu, kilitli olay örgüsünün DÖNÜM anından
        # türetilir: açılış illüstrasyonunun işi tam olarak odur.
        turn = ((story or {}).get("plot") or {}).get("turn")
        subject = (
            f"the turning moment of “{story['title']}”: {turn}"
            if story and turn else
            f"a single defining moment from the story “{story['title']}”"
            if story else
            "PENDING — story inventory is Phase 1's first task"
        )
        records.append({
            "id": sid,
            "kind": "story",
            "storyId": (story or {}).get("id"),
            "cultureId": (story or {}).get("cultureId"),
            "purpose": k["purpose"],
            "subject": subject,
            "prompt": compose(k, subject, (story or {}).get("cultureId")),
            "negative": spec.NEGATIVE_PROMPT,
            "filename": f"{sid}.{spec.RAW_FORMAT}",
            "rawPath": f"07_ASSETS/raw/{sid}.{spec.RAW_FORMAT}",
            "processedPaths": {
                f: f"07_ASSETS/processed/{v['dir']}/{sid}.{v['ext']}"
                for f, v in spec.FORMATS.items()
            },
            "format": spec.RAW_FORMAT.upper(),
            "width": k["raw_px"][0],
            "height": k["raw_px"][1],
            "aspect": k["aspect"],
            "dpi": k["print_dpi"],
            "colorMode": "grayscale (1-bit line art on white)",
            "placement": k["placement"],
            "status": "pending" if story else "blocked-on-inventory",
            "notes": "" if story else
                     "Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3).",
        })

    # --- 22 kültür vinyeti ---
    k = spec.KINDS["culture"]
    for i in range(1, k["count"] + 1):
        culture = locked[i - 1] if i <= len(locked) else None
        # ⚠ Vinyet kimliğinin TEK SAHİBİ culture_index.json'dır.
        # Burada konumdan yeniden türetmek ikinci bir doğruluk kaynağı
        # yaratırdı: dizindeki bir ad değişince sıralama kayar, kimlikler
        # sessizce kayar ve 07_ASSETS/raw/culture-0NN.png dosyaları YANLIŞ
        # kültüre bağlanır. Dizinde kimlik varsa o kullanılır.
        cid = (culture or {}).get("vignetteId") or f"culture-{i:03d}"
        subject = (
            f"a small emblem for {culture['name']} tradition — one object or "
            f"creature that a reader of that tradition would recognise at once"
            if culture else "PENDING — culture inventory is Phase 1's first task"
        )
        records.append({
            "id": cid,
            "kind": "culture",
            "storyId": None,
            "cultureId": (culture or {}).get("id"),
            "purpose": k["purpose"],
            "subject": subject,
            "prompt": compose(k, subject, (culture or {}).get("id")),
            "negative": spec.NEGATIVE_PROMPT,
            "filename": f"{cid}.{spec.RAW_FORMAT}",
            "rawPath": f"07_ASSETS/raw/{cid}.{spec.RAW_FORMAT}",
            "processedPaths": {
                f: f"07_ASSETS/processed/{v['dir']}/{cid}.{v['ext']}"
                for f, v in spec.FORMATS.items()
            },
            "format": spec.RAW_FORMAT.upper(),
            "width": k["raw_px"][0],
            "height": k["raw_px"][1],
            "aspect": k["aspect"],
            "dpi": k["print_dpi"],
            "colorMode": "grayscale (1-bit line art on white)",
            "placement": k["placement"],
            "status": "pending" if culture else "blocked-on-inventory",
            "notes": "" if culture else
                     "22 kültür kilitlenmeden vinyet konusu yazılamaz (DECISIONS § A2).",
        })

    # --- 1 dünya haritası ---
    k = spec.KINDS["map"]
    mid = "map-001"
    subject = ("a hand-drawn world map marking the homelands of the "
               f"{mb.CULTURE_TARGET} cultures in this book, in the manner of an "
               "old chart but honest about coastlines")
    records.append({
        "id": mid,
        "kind": "map",
        "storyId": None,
        "cultureId": None,
        "purpose": k["purpose"],
        "subject": subject,
        "prompt": compose(k, subject, None),
        "negative": spec.NEGATIVE_PROMPT + ", no place labels (typeset separately)",
        "filename": f"{mid}.{spec.RAW_FORMAT}",
        "rawPath": f"07_ASSETS/raw/{mid}.{spec.RAW_FORMAT}",
        "processedPaths": {
            f: f"07_ASSETS/processed/{v['dir']}/{mid}.{v['ext']}"
            for f, v in spec.FORMATS.items()
        },
        "format": spec.RAW_FORMAT.upper(),
        "width": k["raw_px"][0],
        "height": k["raw_px"][1],
        "aspect": k["aspect"],
        "dpi": k["print_dpi"],
        "colorMode": "grayscale (1-bit line art on white)",
        "placement": k["placement"],
        "status": "pending",
        "notes": ("Yer adları DİZGİDE eklenir, çizimde değil — böylece 5 dil "
                  "sürümünde harita yeniden üretilmez."),
    })

    return records


def compose(kind: dict, subject: str, culture_id: str | None) -> str:
    """Prompt gövdesi. ÜSLUP TEK YERDEN gelir — imagespec.STYLE_BODY."""
    bits = [subject + ".", spec.STYLE_BODY + ".", kind["marker"] + "."]
    if culture_id:
        bits.append(
            f"visual detail drawn from {culture_id} material culture, "
            "researched not invented; no pastiche and no borrowed motifs "
            "from other traditions."
        )
    bits.append(
        "Suitable for readers aged 8 to 12: the image may be dramatic, "
        "it may not be frightening."
    )
    return " ".join(bits)


# =============================================================================
# MARKDOWN
# =============================================================================

def render_md(records: list[dict]) -> str:
    L = []
    a = L.append
    a("# IMAGE PROMPT LIBRARY — The Great Book of World Myths")
    a("")
    a("<!-- OTOMATİK ÜRETİLDİ — 04_BUILD/make_prompts.py · ELLE DÜZENLEMEYİN -->")
    a("")
    a(f"**{len(records)} görsel** · {spec.KINDS['story']['count']} hikâye açılışı · "
      f"{spec.KINDS['culture']['count']} kültür vinyeti · {spec.KINDS['map']['count']} harita")
    a("")
    a("> Çalışma arayüzü: [`IMAGE_PROMPT_LIBRARY.html`](IMAGE_PROMPT_LIBRARY.html)")
    a("> — kopyalama düğmeleriyle. Bu dosya kayıt nüshasıdır.")
    a("")
    a("## Akış")
    a("")
    a("```")
    a("IMAGE_PROMPT_LIBRARY.html")
    a("      ↓  kurucu · GPT Image")
    a("07_ASSETS/raw/<id>.png                    ← HAM · ÜZERİNE ASLA YAZILMAZ")
    a("      ↓  04_BUILD/convert_images.py")
    a("07_ASSETS/processed/print/<id>.tif        ← 600 dpi gri TIFF")
    a("07_ASSETS/processed/kindle/<id>.png       ← dosya bütçesine optimize")
    a("07_ASSETS/processed/web/<id>.webp         ← A+ ve pazarlama")
    a("      ↓  04_BUILD/images.py --measure")
    a("06_REPORTS/tracked/image-consistency.json ← ölçüm depoda durur (K18)")
    a("```")
    a("")
    a("**Kurucudan KDP'ye hazır dosya istenmez.** Ham çıktı PNG'dir; üretim")
    a("formatlarını hat türetir (karar K5).")
    a("")
    a("## Üslup gövdesi — 68 promptta AYNI")
    a("")
    a("```")
    a(spec.STYLE_BODY)
    a("```")
    a("")
    a("## Olumsuz kısıtlar — AGE_POLICY § 2.17")
    a("")
    a("```")
    a(spec.NEGATIVE_PROMPT)
    a("```")
    a("")
    a("> Yol haritası R4 (iade oranı): *\"'Look Inside' örneğinde **gerçek** bir")
    a("> bölüm açılışı ve **gerçek** bir illüstrasyon.\"* Yani ilk illüstrasyonlar")
    a("> ebeveynin gördüğü ilk şeydir.")
    a("")
    a("---")
    a("")

    for rec in records:
        a(f"## `{rec['id']}` — {rec['purpose']}")
        a("")
        a("| Alan | Değer |")
        a("|---|---|")
        a(f"| ID | `{rec['id']}` |")
        a(f"| STORY_ID | `{rec['storyId'] or '—'}` |")
        a(f"| CULTURE_ID | `{rec['cultureId'] or '—'}` |")
        a(f"| PURPOSE | {rec['purpose']} |")
        a(f"| OUTPUT_FILENAME | `{rec['filename']}` |")
        a(f"| RAW_OUTPUT_PATH | `{rec['rawPath']}` |")
        for f, p in rec["processedPaths"].items():
            a(f"| PROCESSED_{f.upper()} | `{p}` |")
        a(f"| FORMAT | {rec['format']} |")
        a(f"| EXPECTED_WIDTH | {rec['width']} px |")
        a(f"| EXPECTED_HEIGHT | {rec['height']} px |")
        a(f"| ASPECT | {rec['aspect']} |")
        a(f"| DPI | {rec['dpi']} |")
        a(f"| COLOR_MODE | {rec['colorMode']} |")
        a(f"| PLACEMENT | {rec['placement']} |")
        a(f"| STATUS | `{rec['status']}` |")
        if rec["notes"]:
            a(f"| NOTES | {rec['notes']} |")
        a("")
        a("**PROMPT**")
        a("")
        a("```")
        a(rec["prompt"])
        a("```")
        a("")
        a("**NEGATIVE_PROMPT**")
        a("")
        a("```")
        a(rec["negative"])
        a("```")
        a("")

    a("---")
    a("")
    a("*Bu dosya `04_BUILD/make_prompts.py` tarafından üretilir.*")
    return "\n".join(L) + "\n"


# =============================================================================
# HTML — kurucunun çalışma arayüzü
# =============================================================================

def render_html(records: list[dict]) -> str:
    e = html.escape
    rows = []
    for rec in records:
        proc = "".join(
            f"<div class='kv'><span>PROCESSED_{e(f.upper())}</span><code>{e(p)}</code></div>"
            for f, p in rec["processedPaths"].items())
        rows.append(f"""
<article class="card" data-kind="{e(rec['kind'])}" data-status="{e(rec['status'])}"
         data-search="{e((rec['id'] + ' ' + (rec['storyId'] or '') + ' ' + (rec['cultureId'] or '') + ' ' + rec['purpose']).lower())}">
  <header>
    <h2>{e(rec['id'])}</h2>
    <span class="badge badge-{e(rec['kind'])}">{e(rec['kind'])}</span>
    <span class="badge status-{e(rec['status'])}">{e(rec['status'])}</span>
  </header>
  <p class="purpose">{e(rec['purpose'])}</p>
  <div class="meta">
    <div class="kv"><span>STORY_ID</span><code>{e(rec['storyId'] or '—')}</code></div>
    <div class="kv"><span>CULTURE_ID</span><code>{e(rec['cultureId'] or '—')}</code></div>
    <div class="kv"><span>OUTPUT_FILENAME</span><code>{e(rec['filename'])}</code></div>
    <div class="kv"><span>RAW_OUTPUT_PATH</span><code>{e(rec['rawPath'])}</code></div>
    {proc}
    <div class="kv"><span>FORMAT</span><code>{e(rec['format'])}</code></div>
    <div class="kv"><span>EXPECTED SIZE</span><code>{rec['width']}×{rec['height']} px · {e(rec['aspect'])}</code></div>
    <div class="kv"><span>DPI</span><code>{rec['dpi']}</code></div>
    <div class="kv"><span>COLOR_MODE</span><code>{e(rec['colorMode'])}</code></div>
    <div class="kv"><span>PLACEMENT</span><code>{e(rec['placement'])}</code></div>
  </div>
  {f'<p class="note">{e(rec["notes"])}</p>' if rec['notes'] else ''}
  <div class="block">
    <div class="block-head"><h3>PROMPT</h3>
      <button class="copy" data-target="p-{e(rec['id'])}">Kopyala</button></div>
    <pre id="p-{e(rec['id'])}">{e(rec['prompt'])}</pre>
  </div>
  <div class="block">
    <div class="block-head"><h3>NEGATIVE_PROMPT</h3>
      <button class="copy" data-target="n-{e(rec['id'])}">Kopyala</button></div>
    <pre id="n-{e(rec['id'])}">{e(rec['negative'])}</pre>
  </div>
</article>""")

    counts = {k: sum(1 for r in records if r["kind"] == k) for k in spec.KINDS}

    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Image Prompt Library — The Great Book of World Myths</title>
<style>
:root {{
  --bg:#faf8f4; --fg:#1d1b18; --muted:#6b655c; --line:#ddd6ca;
  --card:#fff; --accent:#8a5a2b; --code:#f3efe7;
}}
@media (prefers-color-scheme: dark) {{
  :root {{ --bg:#16150f; --fg:#ece7dd; --muted:#a09889; --line:#332f26;
           --card:#1e1c15; --accent:#d3a15f; --code:#252219; }}
}}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--bg); color:var(--fg);
  font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,sans-serif; }}
header.top {{ position:sticky; top:0; z-index:10; background:var(--bg);
  border-bottom:1px solid var(--line); padding:1rem 1.25rem; }}
h1 {{ margin:0 0 .35rem; font-size:1.2rem; letter-spacing:.01em; }}
.sub {{ color:var(--muted); font-size:.85rem; margin:0 0 .75rem; }}
.controls {{ display:flex; gap:.5rem; flex-wrap:wrap; align-items:center; }}
input[type=search] {{ flex:1; min-width:200px; padding:.5rem .7rem;
  border:1px solid var(--line); border-radius:7px; background:var(--card); color:var(--fg); }}
button {{ font:inherit; cursor:pointer; border:1px solid var(--line);
  background:var(--card); color:var(--fg); border-radius:7px; padding:.45rem .8rem; }}
button.on {{ background:var(--accent); color:#fff; border-color:var(--accent); }}
main {{ padding:1.25rem; max-width:960px; margin:0 auto; }}
.notice {{ border-left:3px solid var(--accent); padding:.75rem 1rem; margin-bottom:1.5rem;
  background:var(--card); border-radius:0 7px 7px 0; font-size:.9rem; }}
.notice code {{ background:var(--code); padding:.1rem .3rem; border-radius:4px; }}
.card {{ background:var(--card); border:1px solid var(--line); border-radius:11px;
  padding:1.1rem; margin-bottom:1.1rem; }}
.card header {{ display:flex; align-items:center; gap:.6rem; flex-wrap:wrap; margin-bottom:.3rem; }}
.card h2 {{ margin:0; font-size:1rem; font-family:ui-monospace,SFMono-Regular,Menlo,monospace; }}
.badge {{ font-size:.7rem; text-transform:uppercase; letter-spacing:.06em;
  padding:.15rem .45rem; border-radius:5px; border:1px solid var(--line); color:var(--muted); }}
.badge-story {{ border-color:var(--accent); color:var(--accent); }}
.status-blocked-on-inventory {{ border-color:#b4532f; color:#b4532f; }}
.purpose {{ margin:.2rem 0 .8rem; color:var(--muted); font-size:.9rem; }}
.meta {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
  gap:.25rem .9rem; margin-bottom:.9rem; }}
.kv {{ display:flex; justify-content:space-between; gap:.5rem; font-size:.78rem;
  border-bottom:1px dotted var(--line); padding:.2rem 0; }}
.kv span {{ color:var(--muted); letter-spacing:.03em; }}
.kv code, code {{ font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:.76rem; }}
.note {{ font-size:.82rem; color:#b4532f; margin:.2rem 0 .9rem; }}
.block {{ margin-top:.7rem; }}
.block-head {{ display:flex; justify-content:space-between; align-items:center; }}
.block-head h3 {{ margin:0; font-size:.72rem; letter-spacing:.08em;
  text-transform:uppercase; color:var(--muted); }}
pre {{ background:var(--code); border-radius:7px; padding:.75rem .85rem; margin:.35rem 0 0;
  white-space:pre-wrap; word-break:break-word; font-size:.8rem; overflow-x:auto; }}
.copy.done {{ background:var(--accent); color:#fff; border-color:var(--accent); }}
footer {{ padding:2rem 1.25rem; color:var(--muted); font-size:.8rem; text-align:center; }}
</style>
</head>
<body>
<header class="top">
  <h1>Image Prompt Library — The Great Book of World Myths</h1>
  <p class="sub">{len(records)} görsel · {counts['story']} hikâye açılışı ·
     {counts['culture']} kültür vinyeti · {counts['map']} harita ·
     <strong>siyah-beyaz</strong> · ÜRETİLDİ, elle yazılmadı</p>
  <div class="controls">
    <input type="search" id="q" placeholder="ara: id, hikâye, kültür…">
    <button class="filter on" data-kind="all">tümü</button>
    <button class="filter" data-kind="story">hikâye</button>
    <button class="filter" data-kind="culture">kültür</button>
    <button class="filter" data-kind="map">harita</button>
    <button id="copyAll">Görünenlerin promptlarını kopyala</button>
  </div>
</header>
<main>
  <div class="notice">
    <strong>Akış.</strong> Promptu kopyalayın → GPT Image ile üretin →
    çıktıyı <code>07_ASSETS/raw/&lt;id&gt;.png</code> olarak <em>tam bu adla</em>
    kaydedin → <code>python3 04_BUILD/convert_images.py</code> çalıştırın.
    Üretim formatlarını (baskı TIFF, Kindle PNG, web WebP) hat türetir;
    <strong>sizden KDP'ye hazır dosya istenmiyor</strong>.
    <br><br>
    <strong>Ham dosyanın üzerine asla yazılmaz.</strong> Yeniden üretirseniz
    eskisini <code>07_ASSETS/raw/superseded/</code> altına taşıyın.
  </div>
  {''.join(rows)}
</main>
<footer>04_BUILD/make_prompts.py tarafından üretildi · üslup gövdesi
  <code>04_BUILD/imagespec.py</code> içinde tek yerde durur</footer>
<script>
const q = document.getElementById('q');
const cards = [...document.querySelectorAll('.card')];
let kind = 'all';

function apply() {{
  const term = q.value.trim().toLowerCase();
  cards.forEach(c => {{
    const okKind = kind === 'all' || c.dataset.kind === kind;
    const okTerm = !term || c.dataset.search.includes(term);
    c.style.display = (okKind && okTerm) ? '' : 'none';
  }});
}}
q.addEventListener('input', apply);
document.querySelectorAll('.filter').forEach(b => b.addEventListener('click', () => {{
  document.querySelectorAll('.filter').forEach(x => x.classList.remove('on'));
  b.classList.add('on'); kind = b.dataset.kind; apply();
}}));

async function copy(text, btn) {{
  try {{ await navigator.clipboard.writeText(text); }}
  catch (e) {{
    const ta = document.createElement('textarea');
    ta.value = text; document.body.appendChild(ta); ta.select();
    document.execCommand('copy'); ta.remove();
  }}
  const old = btn.textContent;
  btn.textContent = 'Kopyalandı'; btn.classList.add('done');
  setTimeout(() => {{ btn.textContent = old; btn.classList.remove('done'); }}, 1400);
}}

document.querySelectorAll('.copy').forEach(b => b.addEventListener('click', () =>
  copy(document.getElementById(b.dataset.target).textContent, b)));

document.getElementById('copyAll').addEventListener('click', e => {{
  const visible = cards.filter(c => c.style.display !== 'none');
  const text = visible.map(c => {{
    const id = c.querySelector('h2').textContent;
    const p = c.querySelector('pre').textContent;
    return `### ${{id}}\\n${{p}}`;
  }}).join('\\n\\n');
  copy(text, e.target);
}});
</script>
</body>
</html>
"""


# =============================================================================
# GİRİŞ NOKTASI
# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description="Görsel prompt kütüphanesi")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  GÖRSEL PROMPT KÜTÜPHANESİ" + (" · BAYATLIK" if args.check else " · ÜRETİM"))
    print("═" * 72)

    r = mb.Result("make_prompts", verbose=args.verbose)

    if not mb._CFG["illustration"]["required"]:
        r.ok("illüstrasyon hattı GEREKLİ DEĞİL", "project_config.illustration.required = false")
        return r.finish(args.json)

    records = build_records()

    # --- sayım ve tek üslup gövdesi ---
    r.add(len(records) == spec.TOTAL, f"{spec.TOTAL} prompt üretildi ({len(records)})",
          f"{len(records)} prompt, beklenen {spec.TOTAL}")
    r.add(len(records) == mb._CFG["illustration"]["total"],
          "prompt sayısı project_config ile aynı",
          f"{len(records)} ≠ {mb._CFG['illustration']['total']}")

    sig = sum(1 for x in records if spec.STYLE_SIGNATURE in x["prompt"])
    r.add(sig == len(records),
          f"tek üslup gövdesi — imza {len(records)} promptun hepsinde",
          f"üslup imzası yalnızca {sig}/{len(records)} promptta — "
          "TEK ÇİZGİ DİLİ ŞARTI İHLAL EDİLDİ (karar K16)")

    neg = sum(1 for x in records if "no blood" in x["negative"])
    r.add(neg == len(records), "olumsuz kısıtlar her promptta",
          f"yalnızca {neg}/{len(records)} promptta — AGE_POLICY § 2.17")

    markers = sum(1 for x in records if spec.KINDS[x["kind"]]["marker"] in x["prompt"])
    r.add(markers == len(records), "kompozisyon işareti her promptta",
          f"yalnızca {markers}/{len(records)} promptta")

    ids = [x["id"] for x in records]
    r.add(len(set(ids)) == len(ids), "prompt kimlikleri benzersiz", "yinelenen kimlik var")

    # --- yaz / denetle ---
    for path, render in ((MD_OUT, render_md), (HTML_OUT, render_html)):
        new = render(records)
        old = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
        name = os.path.relpath(path, mb.ROOT)
        if args.check:
            r.add(old == new, f"{name} güncel",
                  f"{name} BAYAT — `python3 04_BUILD/make_prompts.py` çalıştırın")
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new)
            print(f"  ✎ {name}")
            r.ok(f"{name} üretildi")

    blocked = [x["id"] for x in records if x["status"] == "blocked-on-inventory"]
    if blocked:
        r.ok(f"{len(blocked)} prompt envantere bağlı",
             "hikâye ve kültür envanteri Faz 1'de kilitlenince konular yazılır")

    if args.json:
        os.makedirs(os.path.dirname(args.json), exist_ok=True)
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"total": len(records), "records": records},
                      fh, ensure_ascii=False, indent=2)
            fh.write("\n")

    return r.finish(None)


if __name__ == "__main__":
    sys.exit(main())
