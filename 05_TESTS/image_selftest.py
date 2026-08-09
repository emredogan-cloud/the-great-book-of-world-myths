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
    # ⚠ KADRAJ UYARI SINIFINA İNDİ — KÖR NOKTA AÇMADIĞI BURADA KANITLANIR.
    # `edge_bleeding` (üst %15'i som siyah) kadraj kuralı OLMADAN da
    # reddedilmeli; reddedilmiyorsa indirme bir kusur gizlemiş demektir.
    _m = img_mod.measure(edge_bleeding(W, H))
    _ok, _checks = img_mod.judge(_m, "story")
    _hard = [c for c in _checks
             if c["rule"] not in ("asgari çözünürlük", "en-boy oranı",
                                  "kenar payı temiz")]
    rep.check(not all(c["ok"] for c in _hard),
              "kenara taşan kurgu, KADRAJ KURALI OLMADAN da reddediliyor",
              "KADRAJ UYARIYA İNDİRİLDİ VE KUSUR KAÇTI — indirme ancak "
              "başka bir kural aynı kusuru yakalıyorsa meşrudur")
    rep.check(any(c["rule"] == "kenar payı temiz" and c.get("severity") == "warn"
                  for c in _checks),
              "kadraj kuralı uyarı sınıfında ve hâlâ ÖLÇÜLÜYOR",
              "kadraj kuralı büsbütün kaldırılmış — uyarı bile kalmamış")

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

    # --- ⑤ HAT KUSURLARININ REGRESYON TESTİ (Faz 5) ---
    #
    # Aşağıdaki üç kusur da üç faz boyunca YEŞİL yandı. Hiçbiri ölçüm hatası
    # değildi — üçü de HATTIN KENDİ kusuruydu ve yalnızca gerçek teslimat
    # geldiğinde görünür oldular. Kapılar artık ısırıyor; bu testler
    # ısırmayı sabitler.
    mb.banner("⑤ hat kusurları — Faz 5 regresyonu")

    import convert_images as conv

    # ⑤a — ESNETME. `resize(target)` oranı dayatıyordu; sığdırma esnetmemeli.
    portrait = Image.new("L", (1024, 1536), 255)
    ImageDraw.Draw(portrait).ellipse([312, 668, 712, 868], fill=0)   # daire
    fitted = conv.fit_no_distort(portrait, (3000, 2000))
    rep.check(fitted.size == (3000, 2000),
              "sığdırma hedef ölçüyü veriyor",
              f"beklenen (3000, 2000), gelen {fitted.size}")
    # Daire daire kalmalı: esnetilseydi yatay çap dikeyin ~1,8 katı olurdu.
    bb = fitted.point(lambda v: 255 if v < 128 else 0, mode="L").getbbox()
    ratio = (bb[2] - bb[0]) / (bb[3] - bb[1])
    rep.check(abs(ratio - 2.0) < 0.15,
              f"sığdırma ESNETMİYOR (daire oranı {ratio:.2f}, beklenen 2.00)",
              "GÖRSEL ESNETİLDİ — 45 hikâye açılışının tamamı bozulur")

    # Şartnameye uyan girdi DEĞİŞMEDEN geçmeli (geri dönülebilirlik).
    conforming = Image.new("L", (2400, 1600), 255)
    ImageDraw.Draw(conforming).ellipse([1000, 700, 1400, 900], fill=0)
    ref = conforming.resize((3000, 2000), Image.LANCZOS)
    rep.check(list(conv.fit_no_distort(conforming, (3000, 2000)).getdata())
              == list(ref.getdata()),
              "şartnameye uyan görselde sığdırma çıktıyı DEĞİŞTİRMİYOR",
              "doğru oranlı görselde dolgu oluştu — dönüşüm geri dönülebilir değil")

    # ⑤b — KİMLİK NORMALİZASYONU. `story-43.png` sessizce yetim kalıyordu.
    rep.check(spec.canonical_id("story-43") == ("story-043", True),
              "sıfır dolgusu kaçmış dosya adı normalize ediliyor (sapma bildirilerek)",
              f"gelen {spec.canonical_id('story-43')}")
    rep.check(spec.canonical_id("story-043") == ("story-043", False),
              "kanonik ad sapma olarak İŞARETLENMİYOR",
              "doğru ad yanlışlıkla sapma sayıldı")
    rep.check(spec.canonical_id("kapak-001") == ("kapak-001", False),
              "tanınmayan tür uydurulmuyor",
              "tanınmayan kimlik sessizce şartname kimliğine dönüştürüldü")
    rep.check(len(spec.expected_ids()) == spec.TOTAL,
              f"şartname {spec.TOTAL} kimlik bekliyor",
              f"beklenen kimlik sayısı {len(spec.expected_ids())}")

    # ⑤c — ÖLÜ KURALLAR. Result.ok() KOŞULSUZ geçer; eksik görsel ve Kindle
    # bütçesi ona bağlanmıştı. Kaynakta artık `r.ok(` ile bağlanmamalı.
    src = open(os.path.join(ROOT, "04_BUILD", "convert_images.py"),
               encoding="utf-8").read()
    rep.check("r.ok(f\"{len(have)}/{spec.TOTAL} görsel geldi\"" not in src,
              "eksik ham görsel KOŞULSUZ GEÇEN kurala bağlı değil",
              "ÖLÜ KURAL GERİ GELDİ: Result.ok() her zaman geçer, eksik görsel "
              "sessizce yeşil yanar")
    rep.check("kindleTotals" in src,
              "Kindle dosya bütçesi GERÇEK görsellerde de denetleniyor",
              "ÖLÜ KURAL GERİ GELDİ: bütçe yalnızca --calibrate yolunda "
              "denetleniyor, yani yalnızca görsel YOKKEN")

    # ⑤d — B1'İN BU PROJEDEKİ HÂLİ: ÜRETİCİNİN VEREBİLDİĞİ EN İYİ DOSYA
    # REDDEDİLMEMELİ. Çözünürlük kapısı `raw_px`e (2400 px, BASKI hedefi)
    # bağlıyken, üreticinin azamisi 1536 px olduğu için 68/68 görsel
    # reddedilmişti — şartnameye BİREBİR UYAN bir teslimat bile geçemezdi.
    for kind in ("story", "culture", "map"):
        gw, gh = spec.KINDS[kind]["generator_px"]
        art = Image.new("L", (gw, gh), 255)
        d2 = ImageDraw.Draw(art)
        step = max(12, gw // 60)
        for x in range(int(gw * 0.15), int(gw * 0.85), step):
            d2.rectangle([x, int(gh * 0.30), x + max(3, step // 6),
                          int(gh * 0.72)], fill=0)
        d2.rectangle([int(gw * 0.12), int(gh * 0.26),
                      int(gw * 0.88), int(gh * 0.26) + max(3, gh // 200)], fill=0)
        d2.rectangle([int(gw * 0.12), int(gh * 0.74),
                      int(gw * 0.88), int(gh * 0.74) + max(3, gh // 200)], fill=0)
        ok_kind, checks_kind = img_mod.judge(img_mod.measure(art), kind)
        res_check = next(c for c in checks_kind if c["rule"] == "asgari çözünürlük")
        rep.check(res_check["ok"],
                  f"{kind}: üreticinin azami boyutundaki görsel çözünürlük "
                  f"kapısını geçiyor ({gw} px)",
                  f"ÜRETİLEBİLİR EN İYİ DOSYA REDDEDİLDİ — kapı {gw} px'i "
                  f"{res_check.get('min')} px'e karşı ölçüyor; hiçbir teslimat "
                  "geçemez (Bestiarium B1)")

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
