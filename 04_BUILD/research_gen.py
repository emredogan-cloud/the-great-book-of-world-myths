#!/usr/bin/env python3
"""
ARAŞTIRMA KAYITLARINI ÜRET
================================================================================
    python3 04_BUILD/research_gen.py            üret
    python3 04_BUILD/research_gen.py --check    bayat mı

story_index.json → 01_RESEARCH/research/<id>.md

Kayıtlar ÜRETİLİR, elle düzenlenmez. Elle yazılan tek şey story_index.json'dır.
Gerekçe Bestiarium D3 ile aynı: aynı bilgiyi iki yerde tutmak bir transkripsiyon
hatası kaynağıdır.

⚠ BESTIARIUM D31 — bu hat YAZIM DURUMUNUN SAHİBİ DEĞİLDİR.
Orada `sync_spec` durumu koşulsuz 'verified' yazıyordu; bir madde 'written'
işaretlendiği an --check bayat yanıyor, --fix ise durumu SESSİZCE GERİ ALIYORDU.
Tamamlanmış yazım işi her tazeleme koşusunda kayboluyordu.
Burada bu betik story_index.json'a HİÇ YAZMAZ.
"""

from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb
import validate_spec as vs

RESEARCH_DIR = os.path.join(mb.RESEARCH, "research")

STAMP = """<!-- OTOMATİK ÜRETİLDİ — 04_BUILD/research_gen.py
     Kaynak: 01_RESEARCH/story_index.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->"""


def render(story: dict, index: dict, cultures: dict) -> str:
    cmap = mb.culture_by_id(cultures)
    macro = {m["id"]: m["nameTr"] for m in cultures.get("macroRegions", [])}
    parts = {p["id"]: p["titleTr"] for p in index.get("parts", [])}
    culture = cmap.get(story.get("cultureId"), {})

    L = []
    a = L.append
    a(f"# {story.get('title', story['id'])} — araştırma kaydı")
    a("")
    a(STAMP)
    a("")
    a("| Alan | Değer |")
    a("|---|---|")
    a(f"| **id** | `{story['id']}` |")
    a(f"| **Başlık (EN)** | {story.get('title', '—')} |")
    a(f"| **Çalışma başlığı** | {story.get('titleTr', '—')} |")
    a(f"| **Kültür** | {culture.get('name', story.get('cultureId', '—'))} "
      f"({macro.get(culture.get('macroRegion', ''), '—')}) |")
    a(f"| **Bölge** | {story.get('region', '—')} |")
    a(f"| **Bölüm** | {parts.get(story.get('partId'), '—')} |")
    a(f"| **Sıra** | {story.get('number', '—')} |")
    a(f"| **Durum** | `{story.get('status', '—')}` |")
    a(f"| **Görsel** | `{story.get('imageId') or '—'}` |")
    a(f"| **Kelime hedefi** | {story.get('wordTarget', mb.WORD_TARGET)} |")
    a(f"| **Yaşayan gelenek** | {'evet' if culture.get('livingTradition') else 'hayır'} |")
    a("")

    # --- 1. Kaynaklar ---
    a("## 1. Kaynaklar")
    a("")
    a("> Ölçüt: [`SOURCING_STANDARD.md`](../../SOURCING_STANDARD.md) — ≥2 bağımsız,")
    a("> ≥1 `primary`/`scholarly`, ≥1 güçlü doğrulama. Motif dizini ve **başka bir")
    a("> yeniden anlatım** bağımsız kaynak **sayılmaz**.")
    a("")
    sources = story.get("sources") or []
    for i, src in enumerate(sources, 1):
        a(f"### Kaynak {i} · `{src.get('type')}` · doğrulama `{src.get('verification')}`")
        a("")
        a(f"- **Künye:** {src.get('ref', '—')}")
        if src.get("locus"):
            a(f"- **Yer:** {src['locus']}")
        if src.get("note"):
            a(f"- **Not:** {src['note']}")
        a("")

    independent = [s for s in sources if s.get("type") in vs.INDEPENDENT_TYPES]
    strong = [s for s in independent if s.get("type") in vs.STRONG_TYPES]
    strong_v = [s for s in independent if s.get("verification") in vs.STRONG_VERIFICATIONS]
    a(f"**Kapı durumu:** ≥2 bağımsız {'✅' if len(independent) >= 2 else '❌'} · "
      f"≥1 primary/scholarly {'✅' if strong else '❌'} · "
      f"≥1 güçlü doğrulama {'✅' if strong_v else '❌'}")
    a("")

    # --- 2. Kanonik anlatım ---
    a("## 2. Kanonik anlatım")
    a("")
    a(f"- **Seçilen:** {story.get('canonicalVersion') or '—'}")
    a(f"- **Gerekçe:** {story.get('canonicalRationale') or '—'}")
    variants = story.get("variants") or []
    a(f"- **Bilinen varyantlar:** {'; '.join(variants) if variants else '—'}")
    a(f"- **Okura söylenecek:** {story.get('variantNote') or '—'}")
    a("")

    # --- 3. Kısıtlılık ---
    a("## 3. Kısıtlılık taraması")
    a("")
    a("> **MUAFİYETSİZ** — karar K20. Bestiarium'da tarama muafiyet listeliydi")
    a("> ve liste hatalıydı (D28): en hassas etik notu taşıyan madde kapının")
    a("> **dışında** kaldı ve hiçbir yerde hata görünmedi.")
    a("")
    a(f"- **Tarandı:** {'✅' if story.get('restrictionScreened') else '❌'}")
    a(f"- **Sonuç:** {story.get('restrictionNote') or '—'}")
    a("")

    # --- 4. Yaş uyarlaması ---
    flags = story.get("contentFlags") or []
    a("## 4. Yaş uyarlaması")
    a("")
    a("> Ölçüt: [`AGE_POLICY.md`](../../AGE_POLICY.md)")
    a("")
    if flags:
        a("| İçerik işareti | Politika seviyesi |")
        a("|---|---|")
        for f in flags:
            a(f"| {f} | `{vs.POLICY_LEVEL.get(f, '?')}` |")
    else:
        a("*İçerik işareti yok.*")
    a("")
    a(f"- **Uyarlama notu:** {story.get('ageAdaptationNote') or '—'}")
    a(f"- **İnceleme durumu:** `{story.get('ageReviewStatus', '—')}`")
    a("")

    # --- 5. Kişiler ---
    a("## 5. Kişiler")
    a("")
    chars = story.get("characters") or []
    if chars:
        a("| Ad | Alternatif | Rol | Sözlükte |")
        a("|---|---|---|---|")
        for c in chars:
            alt = ", ".join(c.get("altNames") or []) or "—"
            a(f"| {c.get('name')} | {alt} | {c.get('role')} | "
              f"{'evet' if c.get('glossary', True) else 'hayır'} |")
    else:
        a("*—*")
    a("")

    # --- 6. Telaffuz ---
    a("## 6. Telaffuz")
    a("")
    a("> **Telaffuz uydurulmaz** — SOURCING_STANDARD § 8. Kaynağı yoksa yazılmaz;")
    a("> ad değişir veya hikâye değişir.")
    a("")
    prons = story.get("pronunciationEntries") or []
    if prons:
        a("| Ad | Telaffuz | IPA | Kaynak |")
        a("|---|---|---|---|")
        for p in prons:
            a(f"| {p.get('name')} | {p.get('pronunciation')} | "
              f"{p.get('pronunciationIpa') or '—'} | {p.get('pronunciationSource')} |")
    else:
        a("*—*")
    a("")

    # --- 7. Dört hareket ---
    a("## 7. Olay örgüsü — dört hareket")
    a("")
    plot = story.get("plot") or {}
    for key, label in (("door", "① Kapı"), ("pressure", "② Baskı"),
                       ("turn", "③ Dönüm"), ("outcome", "④ Sonuç")):
        a(f"- **{label}:** {plot.get(key) or '—'}")
    a("")

    # --- 8. Olgusal iddialar ---
    a("## 8. Olgusal iddialar ve kaynakları")
    a("")
    claims = story.get("factualClaims") or []
    if claims:
        a("| İddia | Kaynak |")
        a("|---|---|")
        for c in claims:
            a(f"| {c.get('claim')} | {c.get('sourceRef')} |")
    else:
        a("*—*")
    a("")

    # --- 9. Temalar ---
    a("## 9. Temalar ve motifler")
    a("")
    a(f"- **Temalar:** {', '.join(story.get('themes') or []) or '—'}")
    a(f"- **Motif kodu** (bilgi — **kapı değil**): "
      f"{', '.join(story.get('motifs') or []) or '—'}")
    a("")
    a("---")
    a("")
    a("*Bu dosya `04_BUILD/research_gen.py` tarafından üretilir.*")
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Araştırma kayıtlarını üret")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  ARAŞTIRMA KAYITLARI" + (" · BAYATLIK" if args.check else " · ÜRETİM"))
    print("═" * 72)

    r = mb.Result("research_gen", verbose=args.verbose)
    index = mb.load_stories()
    cultures = mb.load_cultures()
    entries = [s for s in index.get("stories", []) if s.get("status") != "dropped"]

    if not entries:
        r.ok("hikâye dizini boş — üretilecek kayıt yok",
             "envanter Faz 1'in birinci işi (DECISIONS § A3)")
        return r.finish(args.json)

    os.makedirs(RESEARCH_DIR, exist_ok=True)
    stale = []
    for s in entries:
        path = os.path.join(RESEARCH_DIR, f"{s['id']}.md")
        new = render(s, index, cultures)
        old = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
        if args.check:
            if old != new:
                stale.append(s["id"])
        else:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new)

    if args.check:
        r.add(not stale, f"araştırma kayıtları güncel ({len(entries)})",
              f"bayat: {stale[:10]} — `python3 04_BUILD/research_gen.py`")
    else:
        r.ok(f"{len(entries)} araştırma kaydı üretildi")

    return r.finish(args.json)


if __name__ == "__main__":
    sys.exit(main())
