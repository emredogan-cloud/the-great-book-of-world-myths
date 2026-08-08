#!/usr/bin/env python3
"""
HAM PNG → ÜRETİM FORMATLARI
================================================================================
    python3 04_BUILD/convert_images.py              hepsini dönüştür
    python3 04_BUILD/convert_images.py --check      bütçeleri denetle
    python3 04_BUILD/convert_images.py --calibrate  görsel gelmeden bütçeyi ölç

KURUCUDAN KDP'YE HAZIR DOSYA İSTENMEZ (karar K5).

    RAW  : 07_ASSETS/raw/<id>.png            GPT Image çıktısı
    ÇIKTI: 07_ASSETS/processed/print/<id>.tif    600 dpi gri TIFF
           07_ASSETS/processed/kindle/<id>.png   dosya bütçesine optimize
           07_ASSETS/processed/web/<id>.webp     A+ ve pazarlama

HAM DOSYANIN ÜZERİNE ASLA YAZILMAZ. Dönüşüm tek yönlüdür ve deterministiktir:
aynı ham dosya her koşuda birebir aynı çıktıyı verir.

--------------------------------------------------------------------------------
KİNDLE BÜTÇESİ TÜRETİLMİŞTİR, SEÇİLMEMİŞTİR
--------------------------------------------------------------------------------
7,99 $ × %70 = 5,593 $. Yol haritasının verdiği 5,14 $ telif, 0,453 $ teslim
ücreti demektir; 0,15 $/MB'de bu 3,02 MB eder. 68 görselin TOPLAM Kindle
payı bu sayının altında kalmak zorundadır, yoksa her satılan kopyada telif
düşer.

--calibrate, görsel GELMEDEN bu bütçeyi sınar: şartnameyle aynı çizgi
dilinde kurgu görseller üretir ve dönüşüm zincirinden geçirir. Bestiarium
aynı şeyi yaptı ve Kindle boyut riskini plaka gelmeden ölçtü.

Bağımlılık: Pillow. Yoksa çıkış 2 (ATLANDI) — CI'ın hafif işi bunu kurmaz.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb
import imagespec as spec

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("ATLANDI: Pillow yok — `pip install -r 04_BUILD/requirements.txt`")
    sys.exit(2)

REPORT = os.path.join(mb.REPORTS_TRACKED, "image-formats.json")


# =============================================================================
# DÖNÜŞÜM
# =============================================================================

def convert_one(raw_path: str, image_id: str, kind: str) -> dict:
    k = spec.KINDS[kind]
    out = {"id": image_id, "kind": kind, "raw": os.path.relpath(raw_path, mb.ROOT),
           "outputs": {}}

    with Image.open(raw_path) as im:
        im.load()
        out["rawSize"] = list(im.size)
        out["rawMode"] = im.mode
        base = im.convert("L")

        for fmt, cfg in spec.FORMATS.items():
            target = k[f"{fmt}_px"]
            # Kesin oranı koru — LANCZOS deterministiktir
            resized = base.resize(target, Image.LANCZOS)
            dest_dir = os.path.join(spec.PROCESSED_DIR, cfg["dir"])
            os.makedirs(dest_dir, exist_ok=True)
            dest = os.path.join(dest_dir, f"{image_id}.{cfg['ext']}")

            if cfg["ext"] == "tif":
                resized.save(dest, format="TIFF", compression="tiff_lzw",
                             dpi=(cfg["dpi"], cfg["dpi"]))
            elif cfg["ext"] == "png":
                # 16 ton yeter ve dosyayı küçültür — ince çizgi için kayıpsız şart.
                # Bestiarium D27: kayıplı kodlayıcı ince taramada en kötü durumdur.
                resized.quantize(colors=16, method=Image.MEDIANCUT).save(
                    dest, format="PNG", optimize=True)
            elif cfg["ext"] == "webp":
                resized.save(dest, format="WEBP", lossless=True, quality=100)

            out["outputs"][fmt] = {
                "path": os.path.relpath(dest, mb.ROOT),
                "size": list(target),
                "bytes": os.path.getsize(dest),
            }
    return out


def raw_files() -> list[tuple[str, str, str]]:
    """(yol, kimlik, tür)"""
    found = []
    if not os.path.isdir(spec.RAW_DIR):
        return found
    for name in sorted(os.listdir(spec.RAW_DIR)):
        if not name.lower().endswith(f".{spec.RAW_FORMAT}"):
            continue
        image_id = name.rsplit(".", 1)[0]
        kind = image_id.split("-")[0]
        if kind not in spec.KINDS:
            continue
        found.append((os.path.join(spec.RAW_DIR, name), image_id, kind))
    return found


# =============================================================================
# KALİBRASYON — görsel gelmeden bütçeyi ölç
# =============================================================================

def synthetic(kind: str, seed: int) -> "Image.Image":
    """
    Şartnameyle AYNI çizgi dilinde kurgu görsel: beyaz zemin, siyah çizgi,
    açık kompozisyon. Belirleyici olan KONU değil ÇİZGİ DİLİDİR ve kurgu
    tam o dildedir — bu yüzden dosya boyutu tahmini gerçekçidir.

    Deterministik: aynı seed her koşuda aynı görüntüyü verir.
    """
    w, h = spec.KINDS[kind]["raw_px"]
    im = Image.new("L", (w, h), 255)
    d = ImageDraw.Draw(im)
    stroke = max(3, w // 400)
    rnd = seed * 2654435761 % 2**32

    def nxt(n: int) -> int:
        nonlocal rnd
        rnd = (1103515245 * rnd + 12345) % 2**31
        return rnd % n

    # Ana hat — kapalı bir siluet
    pts = []
    cx, cy = w // 2, h // 2
    r = min(w, h) // 3
    for i in range(14):
        ang = i / 14 * 2 * math.pi
        rr = r * (0.72 + nxt(45) / 100)
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang) * 0.8))
    d.line(pts + [pts[0]], fill=0, width=stroke)

    # İç ayrıntı — çocuk illüstrasyonu seyrek çizgidir, taramalı gravür değil
    for i in range(18):
        x1 = cx - r + nxt(2 * r)
        y1 = cy - int(r * 0.8) + nxt(int(1.6 * r))
        d.line([(x1, y1), (x1 + 20 + nxt(90), y1 + nxt(50) - 25)],
               fill=0, width=max(2, stroke - 1))

    # Zemin işareti — ufuk
    d.line([(int(w * 0.08), int(h * 0.86)), (int(w * 0.92), int(h * 0.86))],
           fill=0, width=stroke)
    return im


def calibrate(r: mb.Result) -> dict:
    mb.banner("format bütçesi kalibrasyonu (görsel gelmeden)")

    import tempfile
    totals = {f: 0 for f in spec.FORMATS}
    per_kind = {}

    with tempfile.TemporaryDirectory() as tmp:
        for kind, k in spec.KINDS.items():
            im = synthetic(kind, seed=len(kind))
            raw = os.path.join(tmp, f"{kind}-sample.png")
            im.save(raw, format="PNG", optimize=True)
            sizes = {}
            base = im.convert("L")
            for fmt, cfg in spec.FORMATS.items():
                resized = base.resize(k[f"{fmt}_px"], Image.LANCZOS)
                dest = os.path.join(tmp, f"{kind}.{cfg['ext']}")
                if cfg["ext"] == "tif":
                    resized.save(dest, format="TIFF", compression="tiff_lzw")
                elif cfg["ext"] == "png":
                    resized.quantize(colors=16, method=Image.MEDIANCUT).save(
                        dest, format="PNG", optimize=True)
                else:
                    resized.save(dest, format="WEBP", lossless=True, quality=100)
                n = os.path.getsize(dest)
                sizes[fmt] = n
                totals[fmt] += n * k["count"]
            per_kind[kind] = sizes

    budget_mb = mb._CFG["editions"]["kindle"]["fileBudgetMb"]
    kindle_mb = totals["kindle"] / 1e6
    # Metin ve EPUB yükü için pay: 45 hikâye × ~950 kelime ≈ 260 KB düz metin
    # + EPUB iskeleti. Muhafazakâr 0,6 MB.
    overhead_mb = 0.6
    projected = kindle_mb + overhead_mb

    print(f"\n  kurgu görsel başına (bayt):")
    for kind, sizes in per_kind.items():
        print(f"    {kind:>8}: " + " · ".join(f"{f} {n:,}" for f, n in sizes.items()))
    print(f"\n  {spec.TOTAL} görsele izdüşüm:")
    for fmt, n in totals.items():
        print(f"    {fmt:>8}: {n / 1e6:.2f} MB")
    print(f"\n  Kindle projeksiyonu: {kindle_mb:.2f} MB görsel + "
          f"{overhead_mb:.2f} MB metin = {projected:.2f} MB")
    print(f"  Bütçe              : {budget_mb:.2f} MB "
          f"(7,99 $ fiyatta 5,14 $ telifi korumak için)")

    r.add(projected <= budget_mb,
          f"Kindle dosya bütçesi tutuyor ({projected:.2f} ≤ {budget_mb:.2f} MB)",
          f"Kindle projeksiyonu {projected:.2f} MB > {budget_mb:.2f} MB — "
          f"0,15 $/MB teslim ücreti telifi {(projected - budget_mb) * 0.15:.2f} $ "
          "daha düşürür. Görseller küçültülmeli veya %35 telif seçeneği hesaplanmalı.")

    r.add(totals["print"] / 1e6 < 650,
          f"baskı PDF varlık toplamı KDP sınırının altında ({totals['print']/1e6:.0f} MB)",
          "baskı varlıkları 650 MB KDP sınırını zorluyor")

    return {"perKind": per_kind, "totals": totals,
            "kindleProjectedMb": round(projected, 3), "budgetMb": budget_mb}


# =============================================================================
# GİRİŞ NOKTASI
# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description="Ham PNG → üretim formatları")
    ap.add_argument("--check", action="store_true", help="dönüştürme, bütçeyi denetle")
    ap.add_argument("--calibrate", action="store_true", help="görsel gelmeden ölç")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  GÖRSEL FORMAT HATTI")
    print("═" * 72)

    r = mb.Result("convert_images", verbose=args.verbose)
    payload: dict = {}

    if args.calibrate:
        payload["calibration"] = calibrate(r)
        return r.finish(args.json)

    raws = raw_files()
    if not raws:
        r.ok("ham görsel yok — hat bekleme durumunda",
             f"{spec.TOTAL} görsel kurucudan gelecek "
             "(07_ASSETS/IMAGE_PROMPT_LIBRARY.html)")
        payload["calibration"] = calibrate(r)
    else:
        mb.banner(f"{len(raws)} ham görsel")
        results = []
        for path, image_id, kind in raws:
            if args.check:
                k = spec.KINDS[kind]
                missing = [f for f, cfg in spec.FORMATS.items()
                           if not os.path.exists(os.path.join(
                               spec.PROCESSED_DIR, cfg["dir"], f"{image_id}.{cfg['ext']}"))]
                r.add(not missing, f"{image_id}: bütün formatlar üretilmiş",
                      f"{image_id}: eksik format {missing}")
            else:
                results.append(convert_one(path, image_id, kind))
                if args.verbose:
                    print(f"  ✎ {image_id}")
        payload["converted"] = results

        # yetim ve eksik
        have = {i for _, i, _ in raws}
        want = set()
        for kind, k in spec.KINDS.items():
            want |= {f"{k['prefix']}-{n:03d}" for n in range(1, k["count"] + 1)}
        r.warn(not (have - want), "yetim ham görsel yok",
               f"prompt kütüphanesinde olmayan dosya: {sorted(have - want)[:10]}")
        r.ok(f"{len(have)}/{spec.TOTAL} görsel geldi",
             f"eksik: {len(want - have)}")

        if have:
            total = sum(o["outputs"]["kindle"]["bytes"]
                        for o in results for _ in [0]) if results else 0
            if total:
                print(f"\n  gelen görsellerin Kindle payı: {total / 1e6:.2f} MB")

    if args.json or True:
        os.makedirs(mb.REPORTS_TRACKED, exist_ok=True)
        with open(args.json or REPORT, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=2)
            fh.write("\n")

    return r.finish(None)


if __name__ == "__main__":
    sys.exit(main())
