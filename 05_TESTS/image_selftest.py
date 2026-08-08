#!/usr/bin/env python3
"""
GÖRSEL ÖLÇÜMÜNÜN KALİBRASYONU — cetvel doğru mu ölçüyor
================================================================================
`images.py` 68 görseli OTOMATİK REDDETME yetkisine sahiptir. Bu test o
yetkinin doğru çalıştığını kanıtlar: geometrisi BİLİNEN kurgu görsellerde
ölçüm doğru sayıyı buluyor mu, ve kapı gerçekten ısırıyor mu?

Bestiarium'un B1 dersi bu testin varlık sebebidir: plaka ölçümü 45° taramada
√2 yanlıştı ve şartnameye BİREBİR UYAN kurgu plakasını reddediyordu — hat,
doğru çizilmiş 112 plakanın TAMAMINI geri çevirecekti. İlk kalibrasyon
koşusu iki gerçek kusur buldu; ikisi de düzeltildi. Hata %41 → %0,3.

Bağımlılık: Pillow. Yoksa çıkış 2 (ATLANDI) — CI'ın hafif işi bunu kurmaz,
görsel iş akışı kurar.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "04_BUILD"))

import mythbook as mb

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("ATLANDI: Pillow yok — `pip install -r 04_BUILD/requirements.txt`")
    sys.exit(2)

import images as img_mod
import imagespec as spec


# =============================================================================
# GEOMETRİSİ BİLİNEN KURGULAR
# =============================================================================

def known_ink(w: int, h: int, coverage: float, stroke: int = 6) -> "Image.Image":
    """Mürekkep yoğunluğu TAM OLARAK bilinen görsel: yatay bantlar."""
    im = Image.new("L", (w, h), 255)
    d = ImageDraw.Draw(im)
    target_rows = int(round(h * coverage))
    drawn, y = 0, 0
    period = max(stroke + 1, int(stroke / coverage)) if coverage > 0 else h + 1
    while drawn < target_rows and y < h:
        band = min(stroke, target_rows - drawn, h - y)
        d.rectangle([0, y, w - 1, y + band - 1], fill=0)
        drawn += band
        y += period
    return im


def known_stroke(w: int, h: int, stroke: int) -> "Image.Image":
    """En ince çizgi kalınlığı TAM OLARAK bilinen görsel: dikey çizgiler."""
    im = Image.new("L", (w, h), 255)
    d = ImageDraw.Draw(im)
    for x in range(stroke * 4, w - stroke * 4, stroke * 8):
        d.rectangle([x, int(h * 0.2), x + stroke - 1, int(h * 0.8)], fill=0)
    return im


def edge_bleeding(w: int, h: int) -> "Image.Image":
    """Kadraj kusuru: çizim kenara yapışıyor."""
    im = Image.new("L", (w, h), 255)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, w - 1, int(h * 0.15)], fill=0)
    d.rectangle([int(w * 0.3), int(h * 0.3), int(w * 0.7), int(h * 0.7)], fill=0)
    return im


def grey_wash(w: int, h: int) -> "Image.Image":
    """İkili dağılım kusuru: yarı ton — çizgi değil, gri yıkama."""
    im = Image.new("L", (w, h), 255)
    px = im.load()
    for y in range(h):
        for x in range(0, w, 3):
            px[x, y] = 90 + (x + y) % 60          # hep orta tonlar
    return im


class Report:
    def __init__(self, verbose: bool):
        self.verbose, self.failed, self.passed = verbose, [], 0

    def check(self, ok: bool, label: str, detail: str = ""):
        if ok:
            self.passed += 1
            if self.verbose:
                print(f"  ✓ {label}")
        else:
            self.failed.append(f"{label} — {detail}" if detail else label)
            print(f"  ✗ {label}" + (f"\n      {detail}" if detail else ""))


def main() -> int:
    ap = argparse.ArgumentParser(description="Görsel ölçümünün kalibrasyonu")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  GÖRSEL ÖLÇÜMÜNÜN KALİBRASYONU")
    print("═" * 72)
    print("  68 görseli reddetme yetkisi olan bir cetvel, doğruluğu")
    print("  kanıtlanmadan kullanılamaz.")

    rep = Report(args.verbose)
    W, H = 1200, 800
    errors = []

    # --- ① mürekkep yoğunluğu doğru ölçülüyor mu ---
    mb.banner("① mürekkep yoğunluğu")
    for target in (0.05, 0.10, 0.20):
        im = known_ink(W, H, target)
        got = img_mod.measure(im)["inkCoverage"]
        err = abs(got - target) / target
        errors.append(err)
        rep.check(err <= spec.TOLERANCES["calibration_error_max"],
                  f"hedef {target:.2f} → ölçülen {got:.4f} (hata %{err * 100:.1f})",
                  f"ölçüm %{err * 100:.1f} sapıyor — tolerans "
                  f"%{spec.TOLERANCES['calibration_error_max'] * 100:.0f}")

    # --- ② en ince çizgi doğru ölçülüyor mu ---
    mb.banner("② en ince çizgi kalınlığı")
    for stroke in (3, 6, 12):
        im = known_stroke(W, H, stroke)
        got = img_mod.measure(im)["minStrokePx"]
        err = abs(got - stroke) / stroke
        errors.append(err)
        rep.check(err <= 0.20,
                  f"çizgi {stroke}px → ölçülen {got:.1f}px (hata %{err * 100:.0f})",
                  f"çizgi kalınlığı ölçümü %{err * 100:.0f} sapıyor — "
                  "600 dpi baskıda kaybolan çizgi bu ölçüyle bulunur")

    # --- ③ KAPI ISIRIYOR MU ---
    mb.banner("③ kapı gerçekten ısırıyor mu")

    cases = [
        ("boş sayfa (mürekkep çok az)", known_ink(W, H, 0.005), False),
        ("blok (mürekkep çok fazla)", known_ink(W, H, 0.45), False),
        ("gri yıkama (çizgi değil yarı ton)", grey_wash(W, H), False),
        ("kenara yapışan kadraj", edge_bleeding(W, H), False),
        ("çok ince çizgi (baskıda kaybolur)", known_stroke(W, H, 1), False),
    ]
    for label, im, should_pass in cases:
        m = img_mod.measure(im)
        ok, checks = img_mod.judge(m, "story")
        # story türü 2400×1600 bekler; kurgu 1200×800 → çözünürlük kapısı da
        # devreye girer. Burada YALNIZCA ilgili kuralı sınıyoruz.
        relevant = [c for c in checks if c["rule"] not in
                    ("asgari çözünürlük", "en-boy oranı")]
        passed = all(c["ok"] for c in relevant)
        rep.check(passed == should_pass,
                  f"{label}: {'reddedildi' if not passed else 'KABUL EDİLDİ'}",
                  "KAPI KUSURU GÖRMEDİ — kör bir cetvel, olmayan cetvelden "
                  "tehlikelidir: yeşil yanar.\n      "
                  + ", ".join(f"{c['rule']}={c['value']}" for c in relevant))

    # --- ④ DOĞRU GÖRSEL REDDEDİLMİYOR MU (Bestiarium B1) ---
    mb.banner("④ şartnameye uyan görsel KABUL EDİLİYOR mu")
    good = Image.new("L", (2400, 1600), 255)
    d = ImageDraw.Draw(good)
    for x in range(300, 2100, 60):
        d.rectangle([x, 400, x + 8, 1200], fill=0)
    d.rectangle([250, 350, 2150, 366], fill=0)
    d.rectangle([250, 1200, 2150, 1216], fill=0)
    m = img_mod.measure(good)
    ok, checks = img_mod.judge(m, "story")
    rep.check(ok, "şartnameye uyan kurgu görsel kabul edildi",
              "DOĞRU ÇİZİLMİŞ GÖRSEL REDDEDİLDİ — hat 68 görselin tamamını geri "
              "çevirebilir (Bestiarium B1):\n      "
              + ", ".join(f"{c['rule']}={c['value']}" for c in checks if not c["ok"]))

    mean_err = sum(errors) / len(errors) if errors else 0
    print(f"\n  ortalama ölçüm hatası: %{mean_err * 100:.2f}")

    if args.json:
        os.makedirs(os.path.dirname(args.json), exist_ok=True)
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"meanError": round(mean_err, 5),
                       "passed": rep.passed, "failed": len(rep.failed)},
                      fh, ensure_ascii=False, indent=2)
            fh.write("\n")

    print()
    print("═" * 72)
    if rep.failed:
        print(f"  ⛔ {len(rep.failed)} KALİBRASYON TESTİ BAŞARISIZ · {rep.passed} geçti")
        for f in rep.failed:
            print(f"     · {f}")
        print("═" * 72)
        return 1
    print(f"  ✅ {rep.passed} KALİBRASYON TESTİ GEÇTİ — cetvel doğru ölçüyor")
    print("═" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
