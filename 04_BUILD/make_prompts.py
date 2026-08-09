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
import coverspec as cover_spec
import editions as ed_mod

MD_OUT = os.path.join(mb.ASSETS, "IMAGE_PROMPT_LIBRARY.md")
HTML_OUT = os.path.join(mb.ASSETS, "IMAGE_PROMPT_LIBRARY.html")


def commercial_records() -> list[dict]:
    """
    Faz 5 ticari varlıkları: kapaklar + Amazon A+ modülleri.

    ⚠ SIRT GENİŞLİĞİ SAYFA SAYISINDAN TÜRETİLİR ve sayfa sayısı ÜRETİLMİŞ
    İÇ BLOKTAN okunur — modelden değil. Model 232 diyor, gerçek dizgi 236
    çıktı; sırt 0,01 inç farkla basılırsa kapak kayar. Ölçülmüş sayı yoksa
    modele düşülür ve rapor bunu söyler.
    """
    pages = mb.PAGE_TARGET
    report = os.path.join(mb.REPORTS_TRACKED, "interior-build.json")
    if os.path.exists(report):
        try:
            with open(report, encoding="utf-8") as fh:
                pages = json.load(fh)["editions"]["paperback"]["totalPages"]
        except (OSError, KeyError, ValueError):
            pass
    ed = ed_mod.get("paperback")
    return cover_spec.all_records(pages, ed.trim_w_in, ed.trim_h_in)


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
            # Olay örgüsünün dönüm cümlesi noktayla biter; şablon kendi
            # noktalamasını eklediği için sondaki nokta düşürülür.
            f"the turning moment of “{story['title']}”: {turn.rstrip('.')}"
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
        # ⚠ KISITLILIK TARAMASI VİNYETE DE İNER (Faz 5).
        #
        # Genel konu ("o geleneğin okurunun hemen tanıyacağı bir nesne")
        # üreticiyi serbest bırakır ve üretici KISITLI malzemeyi seçebilir:
        # Faz 5'te Hawai'i vinyeti bir **ki'i** (heiau tapınak figürü) olarak
        # geldi, oysa `culture_index.hawaiian.restrictionNote` "heiau ritüel
        # ayrıntısı KULLANILMAZ" diyor ve kültürün kısıtlılık riski YÜKSEK.
        #
        # Çözüm konuyu ELLE YAZMAK değil, DİZİNE bağlamaktır: kısıtlılık
        # değerlendirmesi zaten orada duruyor, vinyet konusu da orada durmalı.
        # `vignetteSubject` yoksa genel konu kullanılır — 21 kültür için
        # hiçbir şey değişmez.
        subject = (
            (culture or {}).get("vignetteSubject")
            or (f"a small emblem for {culture['name']} tradition — one object or "
                f"creature that a reader of that tradition would recognise at once"
                if culture else "PENDING — culture inventory is Phase 1's first task")
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
    # ⚠ FAZ 5 KÖK SEBEP DÜZELTMESİ — HARİTA İŞARETLERİNİ ÜRETİCİ KOYAMAZ.
    #
    # Eski konu üreticiden "22 kültürün anayurdunu İŞARETLEMESİNİ" istiyordu.
    # Üretici bunu yapabilmek için 22 kültürün kim olduğunu BİLMEK zorundadır
    # ve bilmiyordu: teslim edilen harita Haudenosaunee, Inca, Guaraní, Celtic
    # ve **Aboriginal** etiketleri taşıyordu — beşi de kitabın kilitli 22
    # kültüründe YOK, ve Aboriginal yol haritası § 5'in KASITLI DIŞARIDA
    # BIRAKMA kararıyla doğrudan çelişiyor (o karar okura arka maddede
    # söyleniyor). Ayrıca üretilen etiketler 1536 px'te okunmuyordu.
    #
    # Doğru mimari § 44–45'in haritaya uygulanmış hâlidir: ÜRETİCİ ZEMİNİ
    # verir, İŞARETLER VE ETİKETLER `culture_index.json → mapPoint`ten
    # DETERMİNİSTİK olarak basılır. 22 kültürün de lat/lon'u dizinde kayıtlı;
    # yani doğru cevap zaten depoda duruyor ve modele sorulması gereksizdi.
    subject = ("a clean hand-drawn world map with no labels of any kind, in "
               "the manner of an old chart but honest about coastlines: "
               "continents, major islands and a simple compass rose only. "
               "Leave the oceans open and uncluttered — location markers and "
               "place names are typeset afterwards and must not be drawn")
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

    # =========================================================================
    # FAZ 5 — TİCARİ GÖRSEL AİLESİ (kitabın 68'inden AYRI)
    # =========================================================================
    for title, family in (("FAZ 5 — KAPAK PROMPTLARI", "cover"),
                          ("FAZ 5 — AMAZON A+ İÇERİK PROMPTLARI", "aplus")):
        items = [x for x in commercial_records() if x["family"] == family]
        a("")
        a("---")
        a("")
        a(f"# {title}")
        a("")
        a(f"**{len(items)} prompt.** Bunlar **68 iç görsele DÂHİL DEĞİLDİR** "
          "(talimat § 29): ayrı bir ticari varlık ailesidir.")
        a("")
        if family == "cover":
            a("> **Kapak, markanın bilinçli esnetildiği tek yerdir.** Yol "
              "haritası § 18: iç bloğun *koyu kodeks* dili kapakta İŞLEMEZ. "
              "Kapak renkli, sıcak ve karakterlidir.")
        a("")
        a("> **Tipografi üretilmez.** Kesin başlık, alt başlık, yaş aralığı ve "
          "sırt yazısı CLI ile SONRADAN basılır (§ 44–45). Prompt yalnızca "
          "**yer ayırır**.")
        a("")
        for rec in items:
            a(f"## `{rec['id']}`")
            a("")
            a(f"| Alan | Değer |")
            a("|---|---|")
            a(f"| HEDEF | {rec['target']} |")
            if rec.get("module"):
                a(f"| AMAZON MODÜLÜ | {rec['module']} |")
            a(f"| ORAN | {rec['aspect']} |")
            if rec.get("sizeIn"):
                a(f"| ÖLÇÜ (inç) | {rec['sizeIn'][0]} × {rec['sizeIn'][1]} |")
            a(f"| ÜRETİM (px) | {rec['renderPx'][0]} × {rec['renderPx'][1]} |")
            a(f"| TİPOGRAFİ | {'SONRADAN BASILIR' if rec['typography'] == 'post' else 'ÜRETİLİR'} |")
            a(f"| TESTLER | {', '.join(rec['checks'])} |")
            a("")
            a(f"**Amaç.** {rec['purpose']}")
            a("")
            a("**Metin-güvenli alanlar.**")
            for z in rec["textZones"]:
                a(f"- {z}")
            a("")
            a("```")
            a(cover_spec.compose(rec))
            a("```")
            a("")
            a("NEGATIVE_PROMPT")
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

def commercial_rows(family: str) -> list[str]:
    """
    Ticari kayıtları iç promptlarla AYNI kart yapısında basar.

    Aynı `.card` / `.block` / `button.copy[data-target]` iskeleti kullanılır;
    böylece sayfanın altındaki tek `querySelectorAll('.copy')` bağlaması yeni
    kartları da kendiliğinden kapsar — kopyalama düğmeleri için ikinci bir
    betik yazmak gerekmez ve mevcut davranış bozulmaz.
    """
    e = html.escape
    out = []
    for rec in commercial_records():
        if rec["family"] != family:
            continue
        zones = "".join(f"<li>{e(z)}</li>" for z in rec["textZones"])
        meta = [
            ("HEDEF", rec["target"]),
            ("ORAN", rec["aspect"]),
            ("ÜRETİM (px)", f"{rec['renderPx'][0]} × {rec['renderPx'][1]}"),
            ("TİPOGRAFİ", "SONRADAN BASILIR (CLI)"
             if rec["typography"] == "post" else "ÜRETİLİR"),
        ]
        if rec.get("module"):
            meta.insert(1, ("AMAZON MODÜLÜ", rec["module"]))
        if rec.get("sizeIn"):
            meta.insert(2, ("ÖLÇÜ (inç)",
                            f"{rec['sizeIn'][0]} × {rec['sizeIn'][1]}"))
        meta.append(("TESTLER", ", ".join(rec["checks"])))
        kvs = "".join(
            f"<div class='kv'><span>{e(k)}</span><code>{e(str(v))}</code></div>"
            for k, v in meta)
        out.append(f"""
<article class="card" data-kind="{e(rec['family'])}"
         data-search="{e((rec['id'] + ' ' + rec['target'] + ' ' + rec['purpose']).lower())}">
  <header>
    <h2>{e(rec['id'])}</h2>
    <span class="badge badge-{e(rec['family'])}">{e(rec['family'])}</span>
    <span class="badge">tipografi: {'post' if rec['typography'] == 'post' else 'üretilir'}</span>
  </header>
  <p class="purpose">{e(rec['purpose'])}</p>
  <div class="meta">{kvs}</div>
  <p class="note">Metin-güvenli alanlar:</p>
  <ul class="zones">{zones}</ul>
  <div class="block">
    <div class="block-head"><h3>PROMPT</h3>
      <button class="copy" data-target="p-{e(rec['id'])}">Kopyala</button></div>
    <pre id="p-{e(rec['id'])}">{e(cover_spec.compose(rec))}</pre>
  </div>
  <div class="block">
    <div class="block-head"><h3>NEGATIVE_PROMPT</h3>
      <button class="copy" data-target="n-{e(rec['id'])}">Kopyala</button></div>
    <pre id="n-{e(rec['id'])}">{e(rec['negative'])}</pre>
  </div>
</article>""")
    return out


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
    comm = commercial_records()
    n_cover = sum(1 for x in comm if x["family"] == "cover")
    n_aplus = sum(1 for x in comm if x["family"] == "aplus")

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
.badge-cover {{ border-color:#2f7d5b; color:#2f7d5b; }}
.badge-aplus {{ border-color:#3a5f96; color:#3a5f96; }}
h2.section {{ margin:2.5rem 0 1rem; padding-top:1.5rem; font-size:1rem;
  letter-spacing:.08em; text-transform:uppercase; color:var(--accent);
  border-top:2px solid var(--accent); }}
ul.zones {{ margin:.2rem 0 .9rem 1.1rem; padding:0; font-size:.82rem;
  color:var(--muted); }}
ul.zones li {{ margin:.15rem 0; }}
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
  <p class="sub">{len(records)} iç görsel · {counts['story']} hikâye açılışı ·
     {counts['culture']} kültür vinyeti · {counts['map']} harita ·
     <strong>siyah-beyaz</strong>
     &nbsp;+&nbsp; <a href="#phase5-cover">{n_cover} kapak</a> ·
     <a href="#phase5-aplus">{n_aplus} A+</a> (Faz 5 · ayrı aile, renkli) ·
     ÜRETİLDİ, elle yazılmadı</p>
  <div class="controls">
    <input type="search" id="q" placeholder="ara: id, hikâye, kültür…">
    <button class="filter on" data-kind="all">tümü</button>
    <button class="filter" data-kind="story">hikâye</button>
    <button class="filter" data-kind="culture">kültür</button>
    <button class="filter" data-kind="map">harita</button>
    <button class="filter" data-kind="cover">kapak</button>
    <button class="filter" data-kind="aplus">A+</button>
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

  <!-- ===================================================================
       FAZ 5 — TİCARİ VARLIK AİLESİ
       Bu bölüm kitabın 68 iç görselinden AYRIDIR (talimat § 29) ve
       kütüphanenin SONUNA eklenir (§ 28). Yukarıdaki 68 kayıt
       DEĞİŞTİRİLMEDİ, YENİDEN SIRALANMADI, SİLİNMEDİ.
       ================================================================ -->
  <h2 class="section" id="phase5-cover">FAZ 5 — KAPAK PROMPTLARI</h2>
  <div class="notice">
    <strong>Kapak, markanın bilinçli esnetildiği tek yerdir.</strong>
    Yol haritası § 18: iç bloğun <em>koyu kodeks</em> dili kapakta
    <strong>işlemez</strong>. Kapak renkli, sıcak ve karakterlidir; yaş
    aralığı köşede okunur; küçük resimde <code>World</code> ve
    <code>22 Cultures</code> seçilebilmelidir.
    <br><br>
    <strong>Tipografi üretilmez.</strong> Kesin başlık, alt başlık, yaş
    aralığı, sırt ve arka kapak metni <strong>CLI ile sonradan basılır</strong>
    (§ 44–45). Prompt yalnızca <em>yer ayırır</em> — üretilmiş bir başlıkta
    tek harf hatası küçük resimde bile görünür.
  </div>
  {''.join(commercial_rows('cover'))}

  <h2 class="section" id="phase5-aplus">FAZ 5 — AMAZON A+ İÇERİK PROMPTLARI</h2>
  <div class="notice">
    Modüller <strong>uydurulmadı</strong>: her kayıt gerçek bir Amazon
    standart A+ modülüne ve onun gerçek piksel ölçüsüne bağlıdır.
    A+ görselleri kitapla tutarlıdır ama <strong>iç sayfanın kopyası
    değildir</strong>. Ticari metin yine <strong>sonradan</strong> basılır.
  </div>
  {''.join(commercial_rows('aplus'))}
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

    # --- FAZ 5: TİCARİ AİLE AYRI SAYILIR VE 68'İ EZEMEZ (talimat § 29) ---
    comm = commercial_records()
    n_cover = sum(1 for x in comm if x["family"] == "cover")
    n_aplus = sum(1 for x in comm if x["family"] == "aplus")
    r.add(len(records) == spec.TOTAL,
          f"iç görsel envanteri bozulmadı ({len(records)}/{spec.TOTAL})",
          f"İÇ GÖRSEL SAYISI DEĞİŞTİ: {len(records)} — 45+22+1=68 fiyat "
          "modelinin dayanağıdır (K4)")
    r.add(n_cover > 0 and n_aplus > 0,
          f"ticari aile üretildi ({n_cover} kapak · {n_aplus} A+)",
          "kapak/A+ promptları üretilmedi")
    comm_ids = [x["id"] for x in comm]
    r.add(len(set(comm_ids)) == len(comm_ids),
          "ticari prompt kimlikleri benzersiz", "yinelenen ticari kimlik")
    r.add(not (set(comm_ids) & set(ids)),
          "ticari kimlikler iç görsel kimlikleriyle ÇAKIŞMIYOR",
          f"ÇAKIŞAN KİMLİK: {sorted(set(comm_ids) & set(ids))} — iki envanter "
          "karışırsa 68 sayımı bozulur")

    # Kapak, iç bloğun üslup gövdesini KULLANMAMALI (yol haritası § 18).
    leaked = [x["id"] for x in comm
              if spec.STYLE_SIGNATURE in cover_spec.compose(x)]
    r.add(not leaked,
          "kapak/A+ promptları iç blok üslup gövdesini taşımıyor",
          f"KOYU KODEKS DİLİ KAPAĞA SIZDI: {leaked} — yol haritası § 18 "
          "kapağın çocuk kitabı konvansiyonuna uymasını şart koşar")

    # Tipografi üretilmemeli (§ 44–45).
    gen_type = [x["id"] for x in comm if x["typography"] != "post"]
    r.add(not gen_type,
          f"bütün ticari promptlarda tipografi SONRADAN basılıyor ({len(comm)})",
          f"ÜRETİLEN TİPOGRAFİ: {gen_type} — kesin ticari metin için görsel "
          "üreticisine güvenilmez (§ 44)")
    no_text = [x["id"] for x in comm if "no text" not in x["negative"]]
    r.add(not no_text, "her ticari promptta 'no text' kısıtı var",
          f"'no text' eksik: {no_text}")

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
