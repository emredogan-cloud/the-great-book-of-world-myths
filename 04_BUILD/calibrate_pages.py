#!/usr/bin/env python3
"""
SAYFA MODELİ KALİBRASYONU — GERÇEK DİZGİYLE
================================================================================
    python3 04_BUILD/calibrate_pages.py            ölç ve raporu yaz
    python3 04_BUILD/calibrate_pages.py --check    rapor bayat mı

⚠ BU BETİK MODELİ MODELE KARŞI SINAMAZ.

Bestiarium D36'nın emri: dolguyla ölçmek "modeli modele karşı sınamaktır".
Bu yüzden burada **gerçek pilot hikâyenin gerçek prozası**, gerçek 6×9
metin bloğuna, gerçek 12/16,5 pt tipografiyle, gerçek yazı karakteri
genişlik tablolarıyla satır satır dizilir ve satırlar SAYILIR.

Ölçülen iki sayı, `editions.Typography`'nin iki TAHMİNİNİ değiştirir:

    avg_chars_per_word    5,4  ← tahmin   →  pilot prozasından ÖLÇÜLDÜ
    avg_char_width_ratio  0,48 ← tahmin   →  yazı karakteri metriğinden ÖLÇÜLDÜ

Çıktı: 06_REPORTS/tracked/page-calibration.json (karar K18 — denetlenen
rapor depoda durur).
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb
import editions as ed_mod
import page_budget as pb

OUT = os.path.join(mb.REPORTS_TRACKED, "page-calibration.json")

# Ölçüm yazı karakterleri. Times-Roman reportlab'ın gömülü Type1'idir ve
# metrikleri standarttır (kurulumdan bağımsız, her koşuda aynı). DejaVu Serif
# ve Liberation Serif gerçek OFL/GPL+FE dosyalarıdır ve KDP'nin gömme şartını
# karşılar. Üçünü birlikte ölçmek DUYARLILIĞI gösterir: tek bir yazı
# karakterine göre kalibre edip "ölçtük" demek yanıltıcı olurdu.
FONT_CANDIDATES = [
    ("Times-Roman", None),
    ("DejaVuSerif", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"),
    ("LiberationSerif", "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"),
]


def _load_fonts():
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    available = []
    for name, path in FONT_CANDIDATES:
        if path is None:
            available.append(name)
            continue
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont(name, path))
                available.append(name)
            except Exception:
                pass
    return available


def break_lines(text: str, font: str, size: float, width_pt: float) -> int:
    """Gerçek satır kırma: greedy, yazı karakterinin GERÇEK genişlik tablosuyla.

    Bu, dizgi motorlarının kullandığı temel algoritmadır. Knuth–Plass
    (InDesign/TeX) biraz daha sıkı paketler; fark tipik olarak %1–2'dir ve
    rapora `algorithm` alanında yazılır — gizlenmez.
    """
    from reportlab.pdfbase.pdfmetrics import stringWidth
    lines = 0
    for para in mb.paragraphs(text):
        cur = ""
        for word in para.split():
            trial = word if not cur else cur + " " + word
            if stringWidth(trial, font, size) <= width_pt:
                cur = trial
            else:
                lines += 1
                cur = word
        if cur:
            lines += 1
    return lines


def measure() -> dict | None:
    """Ölçüm. Manuscript yerelde yoksa None döner — bu bir HATA DEĞİLDİR."""
    book = mb.load_book()
    stories = mb.book_stories(book)
    if not stories:
        return None

    ed = ed_mod.get("paperback")
    t = ed.typography
    target = mb.PAGE_TARGET

    w_in, h_in = ed_mod.text_block(ed, target)
    width_pt = w_in * 72
    lpp = ed_mod.lines_per_page(ed, target)

    fonts = _load_fonts()
    if not fonts:
        raise SystemExit("Ölçüm yazı karakteri bulunamadı.")

    per_story, per_font = [], {}
    for sid, s in sorted(stories.items()):
        text = s.get("text", "")
        words = mb.word_count(text)
        chars = sum(len(x) for x in mb.words(text))
        entry = {
            "id": sid,
            "words": words,
            # Boşluk dâhil ortalama kelime uzunluğu — modelin
            # avg_chars_per_word TAHMİNİNİN yerine geçen ÖLÇÜM.
            "avgCharsPerWord": round(chars / words + 1, 3),
            "fonts": {},
        }
        for f in fonts:
            lines = break_lines(text, f, t.body_pt, width_pt)
            entry["fonts"][f] = {
                "lines": lines,
                "wordsPerLine": round(words / lines, 3),
                "wordsPerPage": round(words / lines * lpp, 1),
                "textPages": round(lines / lpp, 3),
            }
            per_font.setdefault(f, []).append(words / lines * lpp)
        per_story.append(entry)

    measured = {f: round(sum(v) / len(v), 1) for f, v in per_font.items()}
    primary = fonts[0]
    wpp_measured = measured[primary]
    wpp_estimated = round(ed_mod.words_per_page(ed, target), 1)

    # Ölçülen kelime/sayfa'dan geriye doğru: modelin genişlik oranı ne
    # olmalıydı? Bu, tahminin NE KADAR yanlış olduğunu tek sayıda verir.
    acpw = round(sum(e["avgCharsPerWord"] for e in per_story) / len(per_story), 3)
    implied_ratio = round((width_pt / (wpp_measured / lpp * acpw)) / t.body_pt, 4)

    before = pb.compute(wpp_estimated)
    after = pb.compute(wpp_measured)

    cost_b = ed_mod.print_cost("paperback", before["billed"])
    cost_a = ed_mod.print_cost("paperback", after["billed"])
    roy_b = ed_mod.print_royalty(ed.price_usd, cost_b)
    roy_a = ed_mod.print_royalty(ed.price_usd, cost_a)

    return {
        "$comment": [
            "GERÇEK DİZGİ ÖLÇÜMÜ — karar K3 · Bestiarium D36.",
            "Bu dosya bir tahmin değil bir ÖLÇÜMDÜR: pilot hikâyenin gerçek",
            "prozası, gerçek metin bloğuna, gerçek yazı karakteri genişlik",
            "tablolarıyla dizilmiş ve satırlar sayılmıştır.",
            "Üretici: 04_BUILD/calibrate_pages.py",
        ],
        "calibrated": True,
        "gate": mb.read_gate(),
        "source": {
            "stories": [e["id"] for e in per_story],
            "totalWords": sum(e["words"] for e in per_story),
            "note": "Faz 1 tam olarak BİR hikâye yazar (K3); ölçüm o hikâyeye dayanır ve Faz 3'te yeniden yapılır.",
        },
        "geometry": {
            "trimIn": [ed.trim_w_in, ed.trim_h_in],
            "pagesAssumed": target,
            "gutterIn": ed_mod.required_gutter(target),
            "textBlockIn": [round(w_in, 4), round(h_in, 4)],
            "bodyPt": t.body_pt,
            "leadingPt": t.leading_pt,
            "linesPerPage": lpp,
        },
        "algorithm": "greedy first-fit line breaking with real font width tables; Knuth–Plass typically packs 1–2% tighter",
        "fontsMeasured": measured,
        "primaryFont": primary,
        "perStory": per_story,
        "measured": {
            "wordsPerPage": wpp_measured,
            "avgCharsPerWord": acpw,
            "impliedCharWidthRatio": implied_ratio,
        },
        "estimated": {
            "wordsPerPage": wpp_estimated,
            "avgCharsPerWord": t.avg_chars_per_word,
            "charWidthRatio": t.avg_char_width_ratio,
        },
        "delta": {
            "wordsPerPagePct": round((wpp_measured - wpp_estimated) / wpp_estimated * 100, 2),
            "billedPagesBefore": before["billed"],
            "billedPagesAfter": after["billed"],
            "billedPagesDelta": after["billed"] - before["billed"],
            "perStoryPagesBefore": before["billedPagesPerStory"],
            "perStoryPagesAfter": after["billedPagesPerStory"],
            "paperbackRoyaltyBefore": round(roy_b, 2),
            "paperbackRoyaltyAfter": round(roy_a, 2),
            "royaltyDeltaPerCopy": round(roy_a - roy_b, 2),
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Sayfa modeli kalibrasyonu")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    print("═" * 72)
    print("  SAYFA MODELİ KALİBRASYONU · GERÇEK DİZGİ")
    print("═" * 72)

    r = mb.Result("calibrate_pages", verbose=args.verbose)
    data = measure()

    # ⚠ MANUSCRIPT YOKSA BU BİR HATA DEĞİL, "UYGULANAMAZ"DIR.
    #
    # Depo public, manuscript değil (karar K21): CI'da proza HİÇBİR ZAMAN
    # bulunmaz. Bu betik eskiden orada SystemExit(1) ile ölüyordu ve
    # v0.1.0 sürüm koşusunu kırmızı yaktı — kusur veri veya prozada değil,
    # bu betiğin ortam varsayımındaydı.
    #
    # Ama "uygulanamaz" ile "devre dışı" AYNI ŞEY DEĞİLDİR (talimat § M):
    # kayıtlı rapor DEPODA DURUR ve varlığı burada da denetlenir. Yani
    # proza olmadan da söylenebilecek her şey söylenir; yalnızca yeniden
    # ölçüm ertelenir.
    if data is None:
        print("\n  manuscript yerelde yok — yeniden ölçüm UYGULANAMAZ (K21).")
        print("  Depo public, manuscript değil; CI proza görmez ve görmemelidir.")
        r.add(os.path.exists(OUT),
              "kayıtlı kalibrasyon raporu depoda (06_REPORTS/tracked/)",
              "page-calibration.json YOK — denetlenecek rapor depoda "
              "durmuyorsa o denetim ÖLÜ KURALDIR (karar K18)")
        if os.path.exists(OUT):
            with open(OUT, encoding="utf-8") as fh:
                old = json.load(fh)
            r.add(old.get("calibrated") is True
                  and float(old.get("measured", {}).get("wordsPerPage", 0)) > 0,
                  f"rapor ölçülmüş bir model taşıyor "
                  f"({old.get('measured', {}).get('wordsPerPage')} kelime/sayfa)",
                  "rapor 'calibrated' değil — sayfa modeli hâlâ tahmin")
        return r.finish(None)

    m, e, d = data["measured"], data["estimated"], data["delta"]
    print(f"\n  metin bloğu        : {data['geometry']['textBlockIn'][0]}\" × "
          f"{data['geometry']['textBlockIn'][1]}\"  ·  {data['geometry']['linesPerPage']} satır/sayfa")
    print(f"  ölçülen yazı krk.  : {', '.join(f'{k} {v}' for k, v in data['fontsMeasured'].items())}")
    print()
    print(f"  kelime/sayfa TAHMİN: {e['wordsPerPage']:>7.1f}")
    print(f"  kelime/sayfa ÖLÇÜM : {m['wordsPerPage']:>7.1f}   ({d['wordsPerPagePct']:+.1f}%)")
    print(f"  karakter/kelime    : {e['avgCharsPerWord']} → {m['avgCharsPerWord']}")
    print(f"  genişlik oranı     : {e['charWidthRatio']} → {m['impliedCharWidthRatio']}")
    print()
    print(f"  hikâye/sayfa       : {d['perStoryPagesBefore']} → {d['perStoryPagesAfter']}")
    print(f"  kitap sayfası      : {d['billedPagesBefore']} → {d['billedPagesAfter']} "
          f"({d['billedPagesDelta']:+d})")
    print(f"  ciltsiz telif      : {d['paperbackRoyaltyBefore']:.2f} $ → "
          f"{d['paperbackRoyaltyAfter']:.2f} $ ({d['royaltyDeltaPerCopy']:+.2f} $/kopya)")

    if args.check:
        if not os.path.exists(OUT):
            r.fail("page-calibration.json yok", "`calibrate_pages.py` çalıştırın")
            return r.finish(None)
        with open(OUT, encoding="utf-8") as fh:
            old = json.load(fh)
        same = (old.get("measured") == data["measured"]
                and old.get("geometry") == data["geometry"]
                and old.get("fontsMeasured") == data["fontsMeasured"])
        r.add(same, "page-calibration.json güncel",
              "BAYAT — proza veya tipografi değişmiş; `calibrate_pages.py` çalıştırın")
        return r.finish(None)

    os.makedirs(mb.REPORTS_TRACKED, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"\n  ✎ {os.path.relpath(OUT, mb.ROOT)}")
    r.ok("kalibrasyon yazıldı", "sayfa modeli artık ÖLÇÜLMÜŞ değerle çalışıyor")
    return r.finish(None)


if __name__ == "__main__":
    sys.exit(main())
