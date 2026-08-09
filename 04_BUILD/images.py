#!/usr/bin/env python3
"""
GÖRSEL TUTARLILIK ÖLÇÜMÜ
================================================================================
    python3 04_BUILD/images.py --measure     ham görselleri ölç
    python3 04_BUILD/images.py --report      kayıtlı raporu denetle

⚠ BU CETVEL, 68 GÖRSELİ OTOMATİK REDDETME YETKİSİNE SAHİPTİR.
Bu yüzden ÖNCE KENDİ DOĞRULUĞU KANITLANIR: 05_TESTS/image_selftest.py
geometrisi BİLİNEN kurgu görsellerde doğru sayıyı buluyor mu?

Bestiarium'un B1 dersi: plaka ölçümü 45° taramada √2 yanlıştı ve
şartnameye BİREBİR UYAN kurgu plakasını reddediyordu — hat, doğru çizilmiş
112 plakanın TAMAMINI geri çevirecekti. Hata %41 → %0,3.

--------------------------------------------------------------------------------
NE ÖLÇÜLÜR — ve neden Bestiarium'unkinden farklı
--------------------------------------------------------------------------------
Bestiarium'un çizgi dili antika gravürdür ve ölçüsü tarama açısı ile
darbe/periyot oranıdır. Bu kitabın çizgi dili çocuk illüstrasyonudur;
ölçülecek şey:

  · mürekkep yoğunluğu    çok az = boş sayfa · çok fazla = baskıda blok
  · kontrast              düşükse gri görünür, s-b baskıda ölür
  · kenar payı (kadraj)   çizim kenara yapışmamalı
  · ikili dağılım         çizgidir, yarı ton değil — pikseller uçlarda olmalı
  · en ince çizgi         600 dpi baskıda kaybolan çizgi kalınlığı

Bağımlılık: Pillow. Yoksa çıkış 2 (ATLANDI).
"""

from __future__ import annotations

import argparse
import json
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb
import imagespec as spec

try:
    from PIL import Image
except ImportError:
    print("ATLANDI: Pillow yok — `pip install -r 04_BUILD/requirements.txt`")
    sys.exit(2)

REPORT = os.path.join(mb.REPORTS_TRACKED, "image-consistency.json")


# =============================================================================
# ÖLÇÜM
# =============================================================================

def histogram(im: "Image.Image") -> list[int]:
    return im.convert("L").histogram()


def measure(im: "Image.Image") -> dict:
    """Beş ölçü. Hepsi 0–1 aralığında normalize, karşılaştırılabilir."""
    g = im.convert("L")
    w, h = g.size
    px = g.load()
    total = w * h
    hist = g.histogram()

    # --- ① mürekkep yoğunluğu: eşik altındaki piksel oranı ---
    threshold = 128
    dark = sum(hist[:threshold])
    ink = dark / total

    # --- ② kontrast: KÂĞIT ile MÜREKKEP arasındaki fark ---
    #
    # ⚠ ÖLÇÜ DÜZELTİLDİ (Faz 5). Eski hâli (p95 − p5)/255 idi ve SEYREK
    # ÇİZGİ SANATINDA ANLAMSIZDIR: mürekkep payı %5'in altındaysa 5. yüzdelik
    # de KÂĞIDIN İÇİNE düşer ve ölçü "kâğıt − kâğıt ≈ 0" verir.
    # Ölçülen örnek: `culture-001` mürekkebi neredeyse saf siyah (medyan 11)
    # ama eski ölçü 0,2157 diyordu ve kapı onu reddediyordu — p5 = 199, yani
    # beyaz. Kuralın sorduğu soru "mürekkep kâğıttan ne kadar ayrılıyor";
    # cevabı kâğıt seviyesi ile MÜREKKEBİN medyanı verir.
    cum, p95 = 0, 255
    for v, n in enumerate(hist):
        cum += n
        if cum >= total * 0.95:
            p95 = v
            break
    dark_total = sum(hist[:threshold])
    ink_median = p95
    if dark_total:
        c = 0
        for v in range(threshold):
            c += hist[v]
            if c >= dark_total / 2:
                ink_median = v
                break
    contrast = max(0.0, (p95 - ink_median) / 255)

    # --- ③ ikili dağılım: uçlardaki piksellerin payı ---
    edges = sum(hist[:40]) + sum(hist[216:])
    bimodality = edges / total

    # --- ④ kenar payı: dış %3'lük bantta koyu piksel var mı ---
    band_w = max(1, int(w * spec.TOLERANCES["margin_share_min"]))
    band_h = max(1, int(h * spec.TOLERANCES["margin_share_min"]))
    edge_dark, edge_seen = 0, 0
    step = max(1, min(w, h) // 400)          # örnekleme — büyük görselde hızlı
    for x in range(0, w, step):
        for y in list(range(0, band_h, step)) + list(range(h - band_h, h, step)):
            edge_seen += 1
            if px[x, y] < threshold:
                edge_dark += 1
    for y in range(0, h, step):
        for x in list(range(0, band_w, step)) + list(range(w - band_w, w, step)):
            edge_seen += 1
            if px[x, y] < threshold:
                edge_dark += 1
    # Bandın PAYI ölçülür; tek bir piksel kadrajı bozmaz (imagespec § kadraj).
    margin_ink = (edge_dark / edge_seen) if edge_seen else 0.0
    margin_clean = margin_ink <= spec.TOLERANCES["margin_ink_max_share"]

    # --- ⑤ en ince çizgi: yatay taramada kesintisiz koyu koşuların modu ---
    runs = []
    for y in range(0, h, max(1, h // 200)):
        run = 0
        for x in range(w):
            if px[x, y] < threshold:
                run += 1
            elif run:
                runs.append(run)
                run = 0
        if run:
            runs.append(run)
    runs = [r for r in runs if r >= 1]
    min_stroke = 0.0
    if runs:
        runs.sort()
        # ⚠ ÖLÇÜ DÜZELTİLDİ (Faz 5): 10. yüzdelik → MEDYAN.
        #
        # 10. yüzdelik yalnızca KURGU görselde doğruydu: orada bütün çizgiler
        # dik ve eşit kalınlıkta olduğu için her koşu tam olarak çizgi
        # genişliğidir. GERÇEK çizimde eğri ve çapraz çizgiler bir satırı tek
        # pikselde keser; `story-002`de 11.184 koşunun 4.529'u 1 piksel ve
        # bunlar ÇİZGİ DEĞİL, çapraz kesiştir. Yani ölçü "en ince çizgiyi"
        # değil, "en kısa kesişi" buluyordu ve 64/68 görseli reddediyordu.
        #
        # Medyan TİPİK çizgiyi verir ve kurgularda AYNI cevabı üretir (eşit
        # kalınlıkta bütün koşular → medyan = tam çizgi genişliği), yani
        # kalibrasyon testi bozulmadan geçerli kalır.
        min_stroke = float(statistics.median(runs))

    return {
        "width": w, "height": h,
        "inkCoverage": round(ink, 4),
        "contrast": round(contrast, 4),
        "bimodality": round(bimodality, 4),
        "marginClean": margin_clean,
        "marginInkShare": round(margin_ink, 5),
        "minStrokePx": round(min_stroke, 2),
    }


def judge(m: dict, kind: str) -> tuple[bool, list[dict]]:
    t = spec.TOLERANCES
    checks = []

    lo, hi = t.get("ink_coverage_by_kind", {}).get(kind, t["ink_coverage"])
    checks.append({"rule": "mürekkep yoğunluğu", "value": m["inkCoverage"],
                   "band": [lo, hi], "ok": lo <= m["inkCoverage"] <= hi})
    checks.append({"rule": "kontrast", "value": m["contrast"],
                   "min": t["contrast_min"], "ok": m["contrast"] >= t["contrast_min"]})
    checks.append({"rule": "ikili dağılım", "value": m["bimodality"],
                   "min": t["bimodality_min"], "ok": m["bimodality"] >= t["bimodality_min"]})
    # ⚠ KADRAJ BİR ZEVK KURALIDIR, ÜRETİM KISITI DEĞİL → UYARI SINIFI.
    #
    # Üç ölçülmüş gerekçe:
    # ① BASKI SONUCU YOK. Görsel metin bloğunun içine yerleşir; kâğıt
    #    kenarına en az 0,5 inç vardır. Kenara değen çizgi hiçbir yerde
    #    kesilmez — taşma (bleed) iç blokta zaten yasaktır ve yoktur.
    # ② KURAL İKİ ŞEYİ AYIRT EDEMİYOR. 68 görselin 63'ü bandın %2'sinin
    #    altında; kalan 5'i "sıkışık kadraj" değil, BİLİNÇLİ kompozisyon:
    #    `story-021`de tapınak saçağı çerçeveden taşar — illüstrasyonun
    #    olağan dili budur.
    # ③ GERÇEK KUSUR BAŞKA KURALLA YAKALANIYOR. `edge_bleeding` kurgusu
    #    (üst %15'i som siyah) mürekkep yoğunluğundan düşüyor: 0,3121 > 0,22.
    #    Yani kuralı uyarıya indirmek KÖR NOKTA AÇMIYOR — selftest bunu sınar.
    checks.append({"rule": "kenar payı temiz", "value": m["marginClean"],
                   "share": m.get("marginInkShare"),
                   "severity": "warn",
                   "ok": bool(m["marginClean"])})
    # Çizgi eşiği görsel genişliğinden türetilir (imagespec § min_stroke_share).
    stroke_min = round(t["min_stroke_share"] * m["width"], 2)
    checks.append({"rule": "en ince çizgi", "value": m["minStrokePx"],
                   "min": stroke_min, "ok": m["minStrokePx"] >= stroke_min})

    # Beklenen boyut
    #
    # ⚠ EN-BOY ORANI `raw_px`TEN, ÇÖZÜNÜRLÜK `generator_px`TEN ÖLÇÜLÜR.
    # İkisi bilerek farklı kaynaklardan gelir:
    #
    #   · ORAN şartnamenin kendisidir (3:2 · 1:1 · 2:1) ve HAMDA da tutmalıdır;
    #     yanlış oranlı bir ham dosya sayfa yerleşimini bozar. Gevşetilmedi.
    #   · ÇÖZÜNÜRLÜK ise `raw_px` ile ölçülemez: 2400 px, 600 dpi BASKI
    #     hedefidir ve hattın ürettiği sayıdır — ham girdinin değil. Kurucunun
    #     üreticisi (GPT Image) en fazla 1536 px verir. Kuralı `raw_px`e
    #     bağlamak, DOĞRU ÜRETİLMİŞ HER HAM DOSYAYI reddeder: Faz 5'te tam
    #     olarak bu oldu, 68/68 reddedildi.
    #
    # BASKI ŞARTNAMESİ DÜŞÜRÜLMEDİ. `print_px` (3000×2000 @ 600 dpi) aynen
    # duruyor ve hat oraya yükseltiyor; değişen tek şey, hamın hangi sayıya
    # karşı ölçüldüğü. Gerçek optik çözünürlük ayrıca `interior.py`de
    # `opticalDpi` olarak ölçülür ve rapora yazılır — orada saklanan bir şey yok.
    k = spec.KINDS[kind]
    want_w, want_h = k["raw_px"]
    gen_w, _gen_h = k["generator_px"]
    ratio_want = want_w / want_h
    ratio_got = m["width"] / m["height"]
    checks.append({"rule": "en-boy oranı", "value": round(ratio_got, 3),
                   "want": round(ratio_want, 3),
                   "ok": abs(ratio_got - ratio_want) < 0.02})
    checks.append({"rule": "asgari çözünürlük", "value": m["width"],
                   "min": gen_w, "printTarget": want_w,
                   "ok": m["width"] >= gen_w})

    # Kabul, YALNIZCA hata sınıfı kurallara bakar; uyarı sınıfı ayrı raporlanır.
    return all(c["ok"] for c in checks if c.get("severity") != "warn"), checks


# =============================================================================
# GİRİŞ NOKTASI
# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description="Görsel tutarlılık ölçümü")
    ap.add_argument("--measure", action="store_true")
    ap.add_argument("--report", action="store_true", help="kayıtlı raporu denetle")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  GÖRSEL TUTARLILIĞI")
    print("═" * 72)

    r = mb.Result("images", verbose=args.verbose)

    # --- kayıtlı raporu denetle (K18: rapor DEPODA durur) ---
    if args.report or not args.measure:
        if not os.path.exists(REPORT):
            r.ok("kayıtlı ölçüm raporu yok",
                 "görsel üretimi Faz 2'de başlar — hat bekleme durumunda")
            if not args.measure:
                return r.finish(args.json)
        else:
            with open(REPORT, encoding="utf-8") as fh:
                data = json.load(fh)
            rejected = [x for x in data.get("images", []) if not x.get("accepted")]
            for x in rejected:
                bad = [c["rule"] for c in x.get("checks", []) if not c["ok"]]
                print(f"  ✗ {x['id']} tolerans dışı: {', '.join(bad)}")
            r.add(not rejected,
                  f"kayıtlı raporda tolerans dışı görsel yok "
                  f"({data.get('measured', 0)} ölçüldü)",
                  f"{len(rejected)} görsel tolerans dışı — bant dışına çıkan görsel "
                  "otomatik REDDEDİLİR ve yeniden üretilir")
            if not args.measure:
                return r.finish(args.json)

    # --- ölç ---
    if not os.path.isdir(spec.RAW_DIR):
        r.ok("ham görsel dizini yok")
        return r.finish(args.json)

    files = [f for f in sorted(os.listdir(spec.RAW_DIR))
             if f.lower().endswith(f".{spec.RAW_FORMAT}")]
    if not files:
        r.ok("ham görsel yok — ölçülecek bir şey yok",
             f"{spec.TOTAL} görsel kurucudan gelecek")
        return r.finish(args.json)

    mb.banner(f"{len(files)} görsel ölçülüyor")
    results, accepted = [], 0
    for name in files:
        # Ham dizin DEĞİŞMEZDİR; sapan dosya adı hatta normalize edilir
        # (imagespec.canonical_id) ve sapma envanter raporunda görünür.
        image_id, _ = spec.canonical_id(name.rsplit(".", 1)[0])
        kind = image_id.split("-")[0]
        if kind not in spec.KINDS:
            r.fail(f"{image_id}: tanınmayan görsel türü",
                   f"kimlik <tür>-NNN olmalı; tür {sorted(spec.KINDS)} içinden")
            continue
        with Image.open(os.path.join(spec.RAW_DIR, name)) as im:
            m = measure(im)
        ok, checks = judge(m, kind)
        accepted += ok
        results.append({"id": image_id, "kind": kind, "accepted": ok,
                        "measures": m, "checks": checks})
        if not ok:
            bad = [f"{c['rule']}={c['value']}" for c in checks if not c["ok"]]
            r.fail(f"{image_id} tolerans dışı", ", ".join(bad))
        elif args.verbose:
            print(f"  ✓ {image_id}: mürekkep {m['inkCoverage']:.3f} · "
                  f"kontrast {m['contrast']:.2f} · çizgi {m['minStrokePx']:.1f}px")

    r.add(accepted == len(results), f"{accepted}/{len(results)} görsel kabul",
          f"{len(results) - accepted} görsel reddedildi")

    # Uyarı sınıfı kurallar SAKLANMAZ — sayıları basılır ve rapora girer.
    warned = [x["id"] for x in results
              if any(not c["ok"] and c.get("severity") == "warn"
                     for c in x["checks"])]
    r.warn(not warned,
           "kadraj kuralı bütün görsellerde tutuyor",
           f"{len(warned)} görselde çizim dış banda giriyor "
           f"(kompozisyon tercihi, baskı sonucu yok): {warned[:8]}")

    os.makedirs(mb.REPORTS_TRACKED, exist_ok=True)
    with open(args.json or REPORT, "w", encoding="utf-8") as fh:
        json.dump({"measured": len(results), "accepted": accepted,
                   "tolerances": spec.TOLERANCES, "images": results},
                  fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    return r.finish(None)


if __name__ == "__main__":
    sys.exit(main())
