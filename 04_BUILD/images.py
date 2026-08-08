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

    # --- ② kontrast: 5. ve 95. yüzdelik arasındaki fark ---
    cum, p5, p95 = 0, 0, 255
    for v, n in enumerate(hist):
        cum += n
        if p5 == 0 and cum >= total * 0.05:
            p5 = v
        if cum >= total * 0.95:
            p95 = v
            break
    contrast = (p95 - p5) / 255

    # --- ③ ikili dağılım: uçlardaki piksellerin payı ---
    edges = sum(hist[:40]) + sum(hist[216:])
    bimodality = edges / total

    # --- ④ kenar payı: dış %3'lük bantta koyu piksel var mı ---
    band_w = max(1, int(w * spec.TOLERANCES["margin_share_min"]))
    band_h = max(1, int(h * spec.TOLERANCES["margin_share_min"]))
    edge_dark = 0
    step = max(1, min(w, h) // 400)          # örnekleme — büyük görselde hızlı
    for x in range(0, w, step):
        for y in list(range(0, band_h, step)) + list(range(h - band_h, h, step)):
            if px[x, y] < threshold:
                edge_dark += 1
    for y in range(0, h, step):
        for x in list(range(0, band_w, step)) + list(range(w - band_w, w, step)):
            if px[x, y] < threshold:
                edge_dark += 1
    margin_clean = edge_dark == 0

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
        # 10. yüzdelik: en ince çizgiler, gürültüye dayanıklı
        min_stroke = float(runs[max(0, int(len(runs) * 0.10))])

    return {
        "width": w, "height": h,
        "inkCoverage": round(ink, 4),
        "contrast": round(contrast, 4),
        "bimodality": round(bimodality, 4),
        "marginClean": margin_clean,
        "minStrokePx": round(min_stroke, 2),
    }


def judge(m: dict, kind: str) -> tuple[bool, list[dict]]:
    t = spec.TOLERANCES
    checks = []

    lo, hi = t["ink_coverage"]
    checks.append({"rule": "mürekkep yoğunluğu", "value": m["inkCoverage"],
                   "band": [lo, hi], "ok": lo <= m["inkCoverage"] <= hi})
    checks.append({"rule": "kontrast", "value": m["contrast"],
                   "min": t["contrast_min"], "ok": m["contrast"] >= t["contrast_min"]})
    checks.append({"rule": "ikili dağılım", "value": m["bimodality"],
                   "min": t["bimodality_min"], "ok": m["bimodality"] >= t["bimodality_min"]})
    checks.append({"rule": "kenar payı temiz", "value": m["marginClean"],
                   "ok": bool(m["marginClean"])})
    checks.append({"rule": "en ince çizgi", "value": m["minStrokePx"],
                   "min": t["min_stroke_px"], "ok": m["minStrokePx"] >= t["min_stroke_px"]})

    # Beklenen boyut
    k = spec.KINDS[kind]
    want_w, want_h = k["raw_px"]
    ratio_want = want_w / want_h
    ratio_got = m["width"] / m["height"]
    checks.append({"rule": "en-boy oranı", "value": round(ratio_got, 3),
                   "want": round(ratio_want, 3),
                   "ok": abs(ratio_got - ratio_want) < 0.02})
    checks.append({"rule": "asgari çözünürlük", "value": m["width"],
                   "min": want_w, "ok": m["width"] >= want_w})

    return all(c["ok"] for c in checks), checks


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
        image_id = name.rsplit(".", 1)[0]
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

    os.makedirs(mb.REPORTS_TRACKED, exist_ok=True)
    with open(args.json or REPORT, "w", encoding="utf-8") as fh:
        json.dump({"measured": len(results), "accepted": accepted,
                   "tolerances": spec.TOLERANCES, "images": results},
                  fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    return r.finish(None)


if __name__ == "__main__":
    sys.exit(main())
