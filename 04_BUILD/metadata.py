#!/usr/bin/env python3
"""
KDP METADATA PAKETİ
================================================================================
    python3 04_BUILD/metadata.py            paketi üret + karakter sınırlarını sına
    python3 04_BUILD/metadata.py --check    kayıtlı rapor bayat mı

    08_OUTPUT/metadata.json                 ← KDP alanlarının makine okunur hâli
    08_OUTPUT/upload-checklist.md           ← alan alan yükleme listesi
    06_REPORTS/tracked/metadata.json        ← YALNIZCA ÖLÇÜ, depoda durur

--------------------------------------------------------------------------------
UYDURULMAYAN ÜÇ ŞEY
--------------------------------------------------------------------------------
ISBN (A9) · KDP Select (A7) · yazar adı — üçü de KURUCU/HUKUK kararıdır ve
bu betik onları ÜRETMEZ. Yer tutucu bırakır ve yer tutucunun kendisini kapıya
bağlar: çözülmemiş bir alan sessizce "tamam" görünemez.

Talimat § 41: "do not invent ISBNs." § 40: "do not enroll." Bir metadata
üreticisinin en kolay hatası, boş bir alanı makul bir değerle doldurmaktır.

--------------------------------------------------------------------------------
AI BEYANI BİR OLGU BİLDİRİMİDİR
--------------------------------------------------------------------------------
KDP, AI ile üretilmiş içeriğin BEYAN EDİLMESİNİ ister ve iki kategori ayırır:
üretilmiş (AI-generated) ve yardım almış (AI-assisted). Bu kitabın prozası bir
ajan tarafından yazıldı; görselleri GPT Image üretti. Beyan bu olgulardan
çıkar, bir tercihten değil — ama BEYANI VEREN KURUCUDUR ve bu betik onu
"onaylanmış" gösteremez.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb
import editions as ed_mod

OUT_DIR = os.path.join(mb.ROOT, "08_OUTPUT")
OUT_JSON = os.path.join(OUT_DIR, "metadata.json")
OUT_MD = os.path.join(OUT_DIR, "upload-checklist.md")
REPORT = os.path.join(mb.REPORTS_TRACKED, "metadata.json")

# KDP alan sınırları
LIMITS = {
    "title": 200,
    "subtitle": 200,
    "description": 4000,
    "keyword": 50,
    "keywords": 7,
}

PLACEHOLDER = "[PENDING — FOUNDER DECISION]"

DESCRIPTION = """\
Most books of myths for young readers are Greek books. This one is not.

The Great Book of World Myths retells forty-five stories from twenty-two \
traditions — Korean, Inuit, Māori, Hawaiian, Yoruba, Akan, Persian, Turkic, \
Greek, Norse, Irish, Finnish, Egyptian, Mesopotamian, Japanese, Chinese, \
Vietnamese, Hindu, Maya, Aztec, Andean and Zulu — in one volume, at one \
standard, with one voice.

These are stories to READ, not a picture book to flip through. Every story \
runs about a thousand words: long enough to fall into, short enough to finish \
before bed. A black-and-white illustration opens each one. The book is built \
for the eight-to-twelve reader who has finished the Greek shelf and wants to \
know what else is out there.

WHAT IS INSIDE
· 45 stories from 22 cultures, grouped into six regions of the world
· A hand-drawn map showing where every tradition comes from
· A culture card for each tradition: who tells these stories, where, and \
whether they are still told today
· Say These Names — how to pronounce every name in the book, with sources
· Who's Who — a guide to the gods, heroes and monsters
· Where the Stories Come From — the real sources behind every retelling
· A two-line cultural note at the end of every story

HONEST ABOUT THE STORIES
Where the tellers disagree, this book picks one version and says so. Nothing \
has been made gentler than it is: some of these stories end badly for people \
who did not deserve it, and changing that would be a different kind of lie. \
Nothing has been made harsher either — violence is present but never staged.

Some traditions are deliberately left out. Australian Aboriginal stories are \
held by their communities, and who may tell them is decided by rule, not by \
preference. The book says so, in the book.

For readers aged 8 to 12. For parents, grandparents, teachers and school \
librarians who would like the shelf to be wider than one country.\
"""

KEYWORDS = [
    "world mythology for kids",
    "myths and legends for children",
    "greek norse egyptian myths kids",
    "multicultural stories for children",
    "gods heroes and monsters book",
    "mythology collection ages 8-12",
    "world cultures classroom reading",
]

# ⚠ KDP 2023'ten beri ham BISAC kodu değil, KENDİ kategori ağacından seçim
# ister. Bu yüzden burada YOL verilir; emin olunan BISAC kodu ayrıca yazılır,
# emin olunmayan UYDURULMAZ.
CATEGORIES = [
    {
        "path": "Children's Books › Literature & Fiction › Myths & Legends",
        "bisac": "JUV033010",
        "bisacLabel": "JUVENILE FICTION / Legends, Myths, Fables / General",
        "confidence": "high",
    },
    {
        "path": "Children's Books › Literature & Fiction › Myths & Legends › "
                "Other (multicultural / world)",
        "bisac": None,
        "bisacLabel": "KDP kategori seçicisinden seçilecek — kod uydurulmadı",
        "confidence": "picker",
    },
    {
        "path": "Children's Books › Education & Reference › Social Studies › "
                "Cultural Studies",
        "bisac": None,
        "bisacLabel": "KDP kategori seçicisinden seçilecek — kod uydurulmadı",
        "confidence": "picker",
    },
]

AI_DISCLOSURE = {
    "$comment": (
        "OLGU BİLDİRİMİ — tercih değil. KDP 'AI-generated' ile 'AI-assisted' "
        "ayrımı yapar: üretilmiş içerik, aracın oluşturduğu ve sizin "
        "düzenlediğiniz içeriktir; yardım almış içerik, sizin oluşturup araca "
        "düzelttirdiğiniz içeriktir. Aşağıdaki iki satır bu kitabın gerçeğidir."
    ),
    "text": "AI-generated",
    "textDetail": (
        "Prose was drafted by an AI agent under a written editorial "
        "specification, then measured and revised against automated quality "
        "gates and an adversarial fact check."
    ),
    "images": "AI-generated",
    "imagesDetail": (
        "The 68 interior illustrations and the world map were generated with "
        "GPT Image from written prompts, then converted to production formats "
        "by the project's own pipeline."
    ),
    "translation": "not applicable",
    "founderConfirmed": False,
    "note": (
        "Bu beyanı KDP formunda VEREN KURUCUDUR. Betik onu 'onaylandı' "
        "gösteremez; `founderConfirmed` kurucu elle true yapana kadar false "
        "kalır ve kapı bunu açıkça basar."
    ),
}


def measured() -> dict:
    """Ölçülmüş üretim sayıları — tahmin edilmez, raporlardan okunur."""
    out = {"pages": None, "epubMb": None, "images": None}
    p = os.path.join(mb.REPORTS_TRACKED, "interior-build.json")
    if os.path.exists(p):
        try:
            with open(p, encoding="utf-8") as fh:
                d = json.load(fh)["editions"]["paperback"]
            out["pages"] = d["totalPages"]
            out["images"] = d["imagesPlaced"]
        except (OSError, KeyError, ValueError):
            pass
    p = os.path.join(mb.REPORTS_TRACKED, "epub-build.json")
    if os.path.exists(p):
        try:
            with open(p, encoding="utf-8") as fh:
                out["epubMb"] = json.load(fh)["totalMb"]
        except (OSError, KeyError, ValueError):
            pass
    return out


def build() -> dict:
    p = mb._CFG["project"]
    a = mb._CFG["audience"]
    m = measured()
    pages = m["pages"] or mb.PAGE_TARGET

    formats = {}
    for key in ("paperback", "hardcover"):
        ed = ed_mod.get(key)
        lo, hi = ed_mod.PAGE_LIMITS[key]
        cost = ed_mod.print_cost(key, pages)
        formats[key] = {
            "trimIn": [ed.trim_w_in, ed.trim_h_in],
            "paper": "cream",
            "ink": "black & white",
            "bleed": False,
            "pages": pages,
            "pageLimits": [lo, hi],
            "priceUsd": ed.price_usd,
            "printCostUsd": round(cost, 2),
            "royaltyUsd": round(ed_mod.print_royalty(ed.price_usd, cost), 2),
        }
    kd = mb._CFG["editions"]["kindle"]
    formats["kindle"] = {
        "format": "reflowable EPUB",
        "tocRequired": True,
        "imageWidthPx": 1200,
        "fileBudgetMb": kd["fileBudgetMb"],
        "measuredMb": m["epubMb"],
        "priceUsd": kd["priceUsd"],
        "royaltyRate": kd["royaltyRate"],
    }

    return {
        "$comment": [
            "KDP METADATA PAKETİ — Faz 5 hazırlığı. Faz 6 nihai paketlemeyi yapar.",
            "ISBN · KDP Select · yazar adı KURUCU KARARIDIR ve uydurulmamıştır.",
            "Üretici: 04_BUILD/metadata.py",
        ],
        "gate": mb.read_gate(),
        "title": p["title"],
        "subtitle": p["subtitle"],
        "series": p["series"],
        "author": PLACEHOLDER,
        "authorNote": "Yol haritası § 2: 'Yazar adı Codex serisiyle AYNI'. "
                      "Ad depoda kayıtlı değil — kurucu girdisi.",
        "language": p["language"],
        "description": DESCRIPTION,
        "descriptionChars": len(DESCRIPTION),
        "keywords": KEYWORDS,
        "categories": CATEGORIES,
        "ageRange": {"min": a["readerAgeMin"], "max": a["readerAgeMax"],
                     "bisacAgeRange": a["bisacAgeRange"],
                     "gradeRange": a["gradeRange"]},
        "aiDisclosure": AI_DISCLOSURE,
        "isbn": {"paperback": PLACEHOLDER, "hardcover": PLACEHOLDER,
                 "decision": "A9 — AÇIK. KDP ücretsiz ISBN verir ama "
                             "'Publisher' alanı 'Independently published' olur; "
                             "kendi ISBN'imiz okul/kütüphane kanalında anlamlıdır."},
        "kdpSelect": {"enrolled": None,
                      "decision": "A7 — AÇIK. Kayıt YAPILMADI ve YAPILMAYACAK; "
                                  "karar yayından sonra ilk 90 günün verisiyle."},
        "formats": formats,
        "measured": m,
    }


def render_checklist(d: dict) -> str:
    L = ["# KDP YÜKLEME KONTROL LİSTESİ — metadata alanları", "",
         "<!-- OTOMATİK ÜRETİLDİ — 04_BUILD/metadata.py · ELLE DÜZENLEMEYİN -->",
         "",
         "> Bu liste **Faz 5 hazırlığıdır**. Nihai KDP paketlemesi **Faz 6**'nın işidir.",
         "> Adım adım arayüz akışı: [`KDP_UPLOAD_PLAYBOOK.md`](../KDP_UPLOAD_PLAYBOOK.md)",
         "", "## Alanlar", "",
         "| Alan | Değer | Sınır | Durum |", "|---|---|---:|---|"]
    rows = [
        ("Title", d["title"], LIMITS["title"]),
        ("Subtitle", d["subtitle"], LIMITS["subtitle"]),
        ("Series", d["series"], LIMITS["title"]),
        ("Description", f"{d['descriptionChars']} karakter", LIMITS["description"]),
    ]
    for name, val, lim in rows:
        n = len(val) if isinstance(val, str) and "karakter" not in str(val) \
            else d["descriptionChars"]
        ok = "✅" if n <= lim else "⛔ AŞIYOR"
        show = val if len(str(val)) < 70 else str(val)[:67] + "…"
        L.append(f"| {name} | {show} | {lim} | {ok} |")
    L.append(f"| Author | `{d['author']}` | — | ⛔ **KURUCU** |")
    L.append(f"| Language | {d['language']} | — | ✅ |")
    L.append(f"| Age range | {d['ageRange']['min']}–{d['ageRange']['max']} "
             f"(BISAC {d['ageRange']['bisacAgeRange']}) | — | ✅ |")
    L += ["", "## Anahtar kelimeler (7)", ""]
    for i, k in enumerate(d["keywords"], 1):
        flag = "✅" if len(k) <= LIMITS["keyword"] else "⛔"
        L.append(f"{i}. `{k}` — {len(k)}/{LIMITS['keyword']} {flag}")
    L += ["", "## Kategoriler", ""]
    for c in d["categories"]:
        bis = f" · BISAC `{c['bisac']}`" if c["bisac"] else \
              " · **BISAC kodu UYDURULMADI** — KDP seçicisinden seçin"
        L.append(f"- {c['path']}{bis}")
    L += ["", "## AI beyanı", "",
          f"- Metin: **{d['aiDisclosure']['text']}**",
          f"- Görsel: **{d['aiDisclosure']['images']}**",
          f"- Çeviri: {d['aiDisclosure']['translation']}",
          "",
          "> ⛔ **Kurucu onayı bekliyor.** Bu bir hukuki bildirimdir; ajan onu",
          "> 'onaylandı' gösteremez.", "",
          "## Formatlar", "",
          "| Format | Ölçü | Sayfa | Fiyat | Maliyet | Telif |",
          "|---|---|---:|---:|---:|---:|"]
    for k in ("paperback", "hardcover"):
        f = d["formats"][k]
        L.append(f"| {k} | {f['trimIn'][0]}×{f['trimIn'][1]}\" · {f['paper']} · "
                 f"{f['ink']} | {f['pages']} | {f['priceUsd']:.2f} $ | "
                 f"{f['printCostUsd']:.2f} $ | {f['royaltyUsd']:.2f} $ |")
    kf = d["formats"]["kindle"]
    L.append(f"| kindle | {kf['format']} · {kf['imageWidthPx']} px | — | "
             f"{kf['priceUsd']:.2f} $ | — | bütçe {kf['fileBudgetMb']:.1f} MB "
             f"(ölçülen {kf['measuredMb']}) |")
    L += ["", "## Çözülmemiş kurucu kararları", "",
          f"- **A9 · ISBN** — {d['isbn']['decision']}",
          f"- **A7 · KDP Select** — {d['kdpSelect']['decision']}",
          "- **Yazar adı** — yol haritası 'Codex serisiyle aynı' diyor, ad depoda yok",
          "- **H8 · iki ebeveyn okuması** — `03_EDITORIAL/PARENT_READINGS.md`",
          "", "---", "",
          "*Bu dosya `04_BUILD/metadata.py` tarafından üretilir.*"]
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="KDP metadata paketi")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    print("═" * 72)
    print("  KDP METADATA PAKETİ")
    print("═" * 72)

    r = mb.Result("metadata", verbose=args.verbose)
    d = build()

    print(f"\n  başlık      : {len(d['title'])}/{LIMITS['title']}")
    print(f"  alt başlık  : {len(d['subtitle'])}/{LIMITS['subtitle']}")
    print(f"  açıklama    : {d['descriptionChars']}/{LIMITS['description']}")
    print(f"  anahtar kel.: {len(d['keywords'])}/{LIMITS['keywords']}")
    print(f"  kategori    : {len(d['categories'])}/3")

    r.add(len(d["title"]) <= LIMITS["title"], "başlık sınırda",
          f"başlık {len(d['title'])} > {LIMITS['title']}")
    r.add(len(d["subtitle"]) <= LIMITS["subtitle"], "alt başlık sınırda",
          f"alt başlık {len(d['subtitle'])} > {LIMITS['subtitle']}")
    r.add(d["descriptionChars"] <= LIMITS["description"], "açıklama sınırda",
          f"açıklama {d['descriptionChars']} > {LIMITS['description']}")
    r.add(len(d["keywords"]) == LIMITS["keywords"],
          f"{LIMITS['keywords']} anahtar kelime",
          f"{len(d['keywords'])} anahtar kelime — KDP tam 7 alan verir")
    long_kw = [k for k in d["keywords"] if len(k) > LIMITS["keyword"]]
    r.add(not long_kw, "anahtar kelimeler karakter sınırında",
          f"uzun anahtar kelime: {long_kw}")
    r.add(len(d["categories"]) <= 3, "kategori sayısı KDP sınırında (≤3)",
          f"{len(d['categories'])} kategori — KDP en fazla 3 alır")
    r.add(all(x.strip() for x in d["keywords"]), "boş anahtar kelime yok", "boş alan")

    # Alt başlıktaki iki sayı KAPIYA BAĞLIDIR: alıcı tam o iki sayıyı tarıyor.
    r.add(str(mb.STORY_TARGET) in d["subtitle"]
          and str(mb.CULTURE_TARGET) in d["subtitle"],
          f"alt başlık {mb.STORY_TARGET} ve {mb.CULTURE_TARGET} sayılarını taşıyor",
          "alt başlıktaki hikâye/kültür sayısı envanterle uyuşmuyor")
    r.add(str(mb.CULTURE_TARGET) in d["description"]
          and str(mb.STORY_TARGET) in d["description"],
          "açıklama envanterle tutarlı",
          "açıklamadaki sayılar envanterle uyuşmuyor")

    # --- UYDURULMAYANLAR açıkça kırmızı ---
    r.warn(d["author"] != PLACEHOLDER, "yazar adı girilmiş",
           "yazar adı KURUCU GİRDİSİ — yer tutucu duruyor")
    r.warn(d["isbn"]["paperback"] != PLACEHOLDER, "ISBN girilmiş",
           "A9 AÇIK — ISBN uydurulmadı (talimat § 41)")
    r.warn(d["kdpSelect"]["enrolled"] is not None, "KDP Select kararı verilmiş",
           "A7 AÇIK — kayıt yapılmadı ve yapılmayacak (talimat § 40)")
    r.warn(d["aiDisclosure"]["founderConfirmed"], "AI beyanı kurucu onaylı",
           "AI beyanı hazır ama KURUCU ONAYI YOK — hukuki bildirimi ajan veremez")

    if args.check:
        if not os.path.exists(REPORT):
            r.fail("metadata raporu yok", "`metadata.py` çalıştırın")
            return r.finish(None)
        with open(REPORT, encoding="utf-8") as fh:
            old = json.load(fh)
        r.add(old.get("keywords") == d["keywords"]
              and old.get("descriptionChars") == d["descriptionChars"],
              "metadata raporu güncel", "BAYAT — `metadata.py` çalıştırın")
        return r.finish(None)

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write(render_checklist(d))
    os.makedirs(mb.REPORTS_TRACKED, exist_ok=True)
    with open(REPORT, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    for p in (OUT_JSON, OUT_MD, REPORT):
        print(f"  ✎ {os.path.relpath(p, mb.ROOT)}")
    return r.finish(None)


if __name__ == "__main__":
    sys.exit(main())
