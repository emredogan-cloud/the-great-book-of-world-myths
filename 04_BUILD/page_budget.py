#!/usr/bin/env python3
"""
DETERMİNİSTİK SAYFA BÜTÇESİ MODELİ
================================================================================
SAYFA BÜTÇESİ FİYAT MODELİNİN KENDİSİDİR.

16,99 $ ciltsiz fiyatı 3,76 $ baskı maliyetine dayanır ve o maliyet sayfa
sayısının doğrudan fonksiyonudur (1,00 $ + 0,012 $/sayfa). 230 yerine 280
sayfa maliyeti 0,60 $ artırır ve telifi 6,43 $'dan 5,83 $'a düşürür —
%9 telif kaybı, her satılan kopyada.

Bestiarium bu dersi 380 → 436 düzeltmesiyle öğrendi (D26): prova dizgisi
ölçtü, model yanlıştı, sayfa bütçesi %15 arttı.

--------------------------------------------------------------------------------
⚠ BU MODEL ŞU AN KALİBRE DEĞİLDİR.
--------------------------------------------------------------------------------
`words_per_page` bir TAHMİNDİR (yazı karakteri genişliği oranından
türetilir). Faz 1'in görevlerinden biri onu GERÇEK DİZGİYLE ölçmektir
(karar K3). Bestiarium D36: dolguyla ölçmeye devam etmek "modeli modele
karşı sınamaktır".

Bu yüzden model iki yönde çalışır:
  ①  parametrelerden sayfa sayısını hesaplar
  ②  hedef sayfayı tutturmak için GEREKEN kelime/sayfa değerini çözer
      → yani tipografinin neyi başarması gerektiğini söyler
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb
import editions as ed_mod


# =============================================================================
# MODEL PARAMETRELERİ
# =============================================================================
# Her satır bir editoryal karara denk gelir ve o karar DECISIONS.md'de durur.
# Sayı buradan değiştirilirse belge de değiştirilir.

MODEL = {
    # --- ÖN MADDE ---
    "front_half_title":        1,
    "front_blank_1":           1,
    "front_title_page":        1,
    "front_copyright":         1,   # + AI beyanı burada görünür
    "front_dedication":        1,
    "front_blank_2":           1,
    "front_contents":          3,   # 45 hikâye + 22 kültür kartı
    "front_world_map":         2,   # yol haritasının ZORUNLU kıldığı tek görsel
    "front_introduction":      3,   # "bu kitap nasıl okunur"

    # --- GÖVDE ---
    "part_count":              6,   # A5 → K26 — bölgesel bölümler (KARARA BAĞLANDI)
    "pages_per_part_opener":   2,   # açılış tek sayfa + arkası boş

    # Kültür kartı — A4 → K27 · şık (f): KARTIN AYRI SAYFASI YOKTUR.
    #
    # ⚠ 0 "kart yok" DEMEK DEĞİLDİR. 22 kültür kartının hepsi vardır;
    # hiçbiri EK SAYFA tüketmez. Faz 1'in gerçek dizgi ölçümü şunu buldu:
    # her hikâye 3,219 sayfa içerik taşıyor ama 4 sayfa faturalanıyor
    # (hikâye yeni sayfada başlar → yukarı yuvarlanır). Aradaki 0,781
    # sayfa = 25 satır ZATEN ÖDENİYOR ve 45 hikâyede 35 sayfa ediyor.
    # Kültür kartı (vinyet + 3 cümle + harita işareti ≈ 15 satır) kültürel
    # nottan sonra kalan ~21 satıra sığar.
    #
    # Ölçümden ÖNCE bu proje (a′) şıkkını öneriyordu: kart açık sayfa,
    # 3 sayfa/hikâye, 226 sayfa. Ölçüm o öneriyi ÇÜRÜTTÜ — 357,5 kelime/
    # sayfa ile 3 sayfa/hikâye imkânsız (≥380 gerekiyor) ve (a′) 272
    # sayfaya çıkıyor: en kötü şık. Tahmine dayalı bir öneri, ölçümle
    # düşen bir öneridir; kayıt DECISIONS.md § K27'dedir.
    "culture_card_pages":      0,

    # --- ARKA MADDE ---
    "back_pronunciation":      6,
    "back_whos_who":           8,
    "back_cultural_notes":     4,   # kaynaklar ve varyantlar
    "back_about_author":       1,
    "back_acknowledgements":   1,
    "back_qr_page":            1,   # "22 kültür haritası" indirmesi — e-posta listesi

    # --- HİKÂYE GEOMETRİSİ ---
    # Açılış illüstrasyonu sayfanın ÜST YARISINI kaplar → hikâye sayfa
    # başından başlar ve ilk sayfada yarım sayfa metin sığar.
    "opening_illustration_page_share": 0.5,
    # Her hikâye yeni sayfada başlar (rekto zorunluluğu YOK — rekto kuralı
    # 45 hikâyede ~22 boş sayfa demektir ve 0,26 $ baskı maliyeti ekler).
    "story_starts_new_page":   True,
}


def compute(words_per_page: float,
            stories: int = None,
            cultures: int = None,
            story_words: float = None,
            model: dict = None) -> dict:
    m = dict(MODEL)
    if model:
        m.update(model)

    stories = stories if stories is not None else mb.STORY_TARGET
    cultures = cultures if cultures is not None else mb.CULTURE_TARGET
    story_words = story_words if story_words is not None else mb.WORD_TARGET

    front = sum(v for k, v in m.items() if k.startswith("front_"))
    back = sum(v for k, v in m.items() if k.startswith("back_"))
    parts = m["part_count"] * m["pages_per_part_opener"]
    culture_cards = cultures * m["culture_card_pages"]

    # Hikâye: metin sayfası + açılış illüstrasyonunun yediği pay
    text_pages = story_words / words_per_page
    raw = text_pages + m["opening_illustration_page_share"]
    per_story = math.ceil(raw) if m["story_starts_new_page"] else raw
    body = per_story * stories

    total = front + parts + culture_cards + body + back

    # KDP ciltli 550 sayfa, ciltsiz 828 sayfa sınırı; ayrıca sayfa sayısı
    # baskıda ÇİFT olmak zorundadır (her yaprak iki sayfa).
    billed = int(math.ceil(total / 2) * 2)

    return {
        "wordsPerPage": round(words_per_page, 1),
        "storyWords": story_words,
        "textPagesPerStory": round(text_pages, 3),
        "billedPagesPerStory": per_story,
        "front": front,
        "partOpeners": parts,
        "cultureCards": culture_cards,
        "body": body,
        "back": back,
        "total": total,
        "billed": billed,
    }


def achievable(target_pages: int) -> list[dict]:
    """
    Kelime/sayfa 200–600 arasında değişirken ULAŞILABİLİR sayfa sayıları.

    ⚠ SONUÇ SÜREKLİ DEĞİLDİR. Her hikâye yeni sayfada başlar ve sayfa sayısı
    YUKARI YUVARLANIR; bu yüzden hikâye başına maliyet 3 ↔ 4 arasında ZIPLAR
    ve aradaki bütün sayfa sayıları ULAŞILAMAZ.

    Hedef bu boşluğa düşüyorsa TİPOGRAFİYİ AYARLAMAK İŞE YARAMAZ — yapısal
    bir karar gerekir. Bu, modelin verebileceği en değerli bilgidir ve
    Bestiarium'un D26'da öğrendiği şeyin ta kendisidir: sayfa bütçesini
    kelime hedefi değil, SAYFA KURALLARI belirler.
    """
    buckets: dict[int, list[float]] = {}
    wpp = 200.0
    while wpp <= 600.0:
        got = compute(wpp)["billed"]
        buckets.setdefault(got, []).append(wpp)
        wpp += 1.0
    out = []
    for pages, wpps in sorted(buckets.items()):
        out.append({
            "billed": pages,
            "wppMin": min(wpps),
            "wppMax": max(wpps),
            "delta": pages - target_pages,
            "perStory": compute(min(wpps))["billedPagesPerStory"],
        })
    return out


def structural_levers(target_pages: int) -> list[dict]:
    """Hedefe yaklaştıran YAPISAL seçenekler — her biri bir editoryal karardır."""
    options = []
    for card_pages, part_pages in ((1, 2), (2, 2), (1, 1), (2, 1), (0, 2), (2, 0)):
        for wpp in (280.0, 320.0, 361.0, 420.0, 480.0):
            m = {"culture_card_pages": card_pages, "pages_per_part_opener": part_pages}
            res = compute(wpp, model=m)
            options.append({
                "wpp": wpp,
                "cultureCardPages": card_pages,
                "partOpenerPages": part_pages,
                "perStory": res["billedPagesPerStory"],
                "billed": res["billed"],
                "delta": res["billed"] - target_pages,
            })
    seen, unique = set(), []
    for o in sorted(options, key=lambda x: (abs(x["delta"]), x["billed"])):
        key = (o["billed"], o["cultureCardPages"], o["partOpenerPages"], o["perStory"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(o)
    return unique[:8]


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministik sayfa bütçesi modeli")
    ap.add_argument("--words-per-page", type=float, default=None,
                    help="ölçülmüş kelime/sayfa (varsayılan: tipografiden tahmin)")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    gate = mb.read_gate()
    target = mb.PAGE_TARGET
    tolerance = mb._CFG["scope"]["pageTolerancePct"]

    print("═" * 72)
    print(f"  SAYFA BÜTÇESİ · hedef {target} sayfa · tolerans %{tolerance}")
    print("═" * 72)

    r = mb.Result("page_budget", verbose=args.verbose)

    paperback = ed_mod.get("paperback")
    estimated_wpp = ed_mod.words_per_page(paperback, target)
    wpp = args.words_per_page or estimated_wpp
    calibrated = args.words_per_page is not None or paperback.typography.calibrated

    result = compute(wpp)
    result["calibrated"] = calibrated
    result["gate"] = gate

    print(f"\n  kelime/sayfa           : {wpp:.1f}"
          f"   {'(ÖLÇÜLDÜ)' if calibrated else '(TAHMİN — kalibre değil)'}")
    print(f"  hikâye metni           : {result['textPagesPerStory']:.2f} sayfa")
    print(f"  hikâye başına faturalanan: {result['billedPagesPerStory']} sayfa "
          f"(açılış illüstrasyonu üst yarıyı kaplar)")
    print()
    print(f"  ön madde               : {result['front']:>4}")
    print(f"  bölüm açılışları       : {result['partOpeners']:>4}  "
          f"({MODEL['part_count']} bölüm × {MODEL['pages_per_part_opener']})")
    print(f"  kültür kartları        : {result['cultureCards']:>4}  "
          f"({mb.CULTURE_TARGET} × {MODEL['culture_card_pages']}) ← A4 şık (a)")
    print(f"  hikâyeler              : {result['body']:>4}  "
          f"({mb.STORY_TARGET} × {result['billedPagesPerStory']})")
    print(f"  arka madde             : {result['back']:>4}")
    print(f"  {'─' * 40}")
    print(f"  TOPLAM                 : {result['total']:>4}")
    print(f"  FATURALANAN (çift)     : {result['billed']:>4}")

    deviation = abs(result["billed"] - target) / target * 100
    print(f"\n  hedeften sapma         : %{deviation:.1f}")

    # --- maliyet etkisi ---
    cost = ed_mod.print_cost("paperback", result["billed"])
    roy = ed_mod.print_royalty(16.99, cost)
    target_cost = ed_mod.print_cost("paperback", target)
    target_roy = ed_mod.print_royalty(16.99, target_cost)
    print(f"  ciltsiz maliyet        : {cost:.2f} $   (hedefte {target_cost:.2f} $)")
    print(f"  ciltsiz telif          : {roy:.2f} $   (hedefte {target_roy:.2f} $)")
    print(f"  telif farkı            : {roy - target_roy:+.2f} $ / kopya")

    # --- ULAŞILABİLİRLİK: hedef gerçekten tutturulabilir mi? ---
    grid = achievable(target)
    print("\n  ULAŞILABİLİR SAYFA SAYILARI (kelime/sayfa 200–600 arası taranarak)")
    print("  ┌──────────┬────────────┬───────────────────┬──────────┐")
    print("  │ sayfa    │ hikâye/syf │ kelime/sayfa      │ hedeften │")
    print("  ├──────────┼────────────┼───────────────────┼──────────┤")
    reachable = False
    for row in grid:
        mark = "◀ ŞU AN" if row["wppMin"] <= wpp <= row["wppMax"] else ""
        if abs(row["delta"]) <= target * tolerance / 100:
            reachable = True
            mark = (mark + " ✓ HEDEFTE").strip()
        print(f"  │ {row['billed']:>8} │ {row['perStory']:>10} │ "
              f"{row['wppMin']:>6.0f}–{row['wppMax']:<10.0f} │ {row['delta']:>+8} │ {mark}")
    print("  └──────────┴────────────┴───────────────────┴──────────┘")

    if not reachable:
        print(f"\n  ⚠ {target} SAYFA MEVCUT YAPIYLA ULAŞILAMAZ.")
        print("    Sebep: her hikâye yeni sayfada başlar ve yukarı yuvarlanır;")
        print("    hikâye başına maliyet 3 ↔ 4 arasında ZIPLAR. Tipografiyi")
        print("    ayarlamak aradaki sayfa sayılarını AÇMAZ — yapısal karar gerekir.")
        print("\n    YAPISAL SEÇENEKLER (her biri bir editoryal karar):")
        print("    ┌────────────┬──────────┬──────────┬──────────┬──────────┐")
        print("    │ kelime/syf │ kültür k.│ bölüm aç.│ hikâye/s │ TOPLAM   │")
        print("    ├────────────┼──────────┼──────────┼──────────┼──────────┤")
        for o in structural_levers(target):
            flag = " ✓" if abs(o["delta"]) <= target * tolerance / 100 else ""
            print(f"    │ {o['wpp']:>10.0f} │ {o['cultureCardPages']:>8} │ "
                  f"{o['partOpenerPages']:>8} │ {o['perStory']:>8} │ "
                  f"{o['billed']:>8} │ {o['delta']:>+5}{flag}")
        print("    └────────────┴──────────┴──────────┴──────────┴──────────┘")
        print("    → DECISIONS.md § A4 (kültür vinyeti yeri) ve § A5 (bölüm mimarisi)")
        print("      bu tablodan karara bağlanır. Faz 1'in çıktısıdır.")

    # ------------------------------------------------------------------ kapılar
    r.add(result["billed"] % 2 == 0, "sayfa sayısı çift (baskı yaprağı kuralı)",
          f"{result['billed']} tek sayı")

    try:
        ed_mod.print_cost("hardcover", result["billed"])
        r.ok(f"sayfa sayısı ciltli sınırlarında (75–550): {result['billed']}")
    except ValueError as exc:
        r.fail("sayfa sayısı ciltli sınırlarının dışında",
               f"{exc} — ciltli LANSMAN formatıdır, düşürülemez")

    r.add(roy > 0, f"ciltsiz telif pozitif ({roy:.2f} $)", f"telif NEGATİF: {roy:.2f} $")

    # Model kalibre değilken sapma UYARIDIR; Faz 4'ten itibaren HATADIR.
    if mb.gate_at_least(gate, "phase4"):
        r.add(deviation <= tolerance,
              f"sayfa bütçesi hedefte (%{deviation:.1f} ≤ %{tolerance})",
              f"sapma %{deviation:.1f} > %{tolerance} — FİYAT MODELİ ETKİLENİR. "
              f"Yol haritasının emri: 'kelime hedefini değil SAYFA BÜTÇESİNİ düzelt.'")
    else:
        r.warn(deviation <= tolerance,
               f"sayfa bütçesi hedefte (%{deviation:.1f} ≤ %{tolerance})",
               f"sapma %{deviation:.1f} > %{tolerance} — model KALİBRE DEĞİL. "
               f"Faz 1 gerçek dizgiyle ölçecek (K3). Ulaşılabilirlik tablosu "
               f"yukarıda: hedef tipografiyle DEĞİL, yapısal kararla tutturulur.")

    r.warn(calibrated, "sayfa modeli gerçek dizgiyle kalibre edilmiş",
           "model KALİBRE DEĞİL — kelime/sayfa tipografi tahmininden geliyor. "
           "Bestiarium D36: dolguyla ölçmek 'modeli modele karşı sınamaktır'.")

    if args.json:
        os.makedirs(os.path.dirname(args.json), exist_ok=True)
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"model": MODEL, "result": result,
                       "achievable": grid,
                       "structuralLevers": structural_levers(target),
                       "paperbackCostUsd": round(cost, 2),
                       "paperbackRoyaltyUsd": round(roy, 2)},
                      fh, ensure_ascii=False, indent=2)
            fh.write("\n")

    return r.finish(None)


if __name__ == "__main__":
    sys.exit(main())
