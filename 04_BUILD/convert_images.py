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

def fit_no_distort(base: "Image.Image", target: tuple[int, int]) -> "Image.Image":
    """
    Hedef kutuya SIĞDIR, ASLA ESNETME. Artan yer beyaz kâğıtla doldurulur.

    ⚠ FAZ 5 DÜZELTMESİ. Burada eskiden `base.resize(target)` vardı ve üstünde
    "kesin oranı koru" yazıyordu — ama `resize(target)` oranı KORUMAZ, hedef
    ölçüyü DAYATIR. Şartnameye uyan girdide fark yoktur (2400×1600 → 3000×2000,
    ikisi de 3:2), yani kusur üç faz boyunca GÖRÜNMEZ kaldı. Faz 5 teslimatı
    1024×1536 geldi ve aynı satır onu 3000×2000'e ESNETECEKTİ: her figür yatay
    olarak %120 genişleyecek, 45 hikâye açılışının tamamı bozulacaktı.

    Sığdırma kayıpsızdır ve GERİ DÖNÜLEBİLİRDİR: doğru oranlı görsel geldiğinde
    dolgu kendiliğinden sıfırlanır ve çıktı birebir eskisi olur.
    """
    tw, th = target
    sw, sh = base.size
    if (sw, sh) == (tw, th):
        return base.copy()
    scale = min(tw / sw, th / sh)
    nw, nh = max(1, round(sw * scale)), max(1, round(sh * scale))
    fitted = base.resize((nw, nh), Image.LANCZOS)
    if (nw, nh) == (tw, th):
        return fitted
    canvas_ = Image.new("L", (tw, th), 255)          # beyaz kâğıt
    canvas_.paste(fitted, ((tw - nw) // 2, (th - nh) // 2))
    return canvas_


def clamp_white(g: "Image.Image") -> "Image.Image":
    """
    Kâğıt gürültüsünü beyaza kenetle (imagespec.PREPRESS § 3b).

    Eşiğin ALTINDAKİ hiçbir ton değişmez — bu bilinçlidir: doğrusal
    yeniden ölçekleme çizimin kendi gölgesini de soldururdu.
    """
    wp = spec.PREPRESS["white_point"]
    if wp >= 255:
        return g
    return g.point([255 if v >= wp else v for v in range(256)], mode="L")


def convert_one(raw_path: str, image_id: str, kind: str) -> dict:
    k = spec.KINDS[kind]
    out = {"id": image_id, "kind": kind, "raw": os.path.relpath(raw_path, mb.ROOT),
           "outputs": {}}

    with Image.open(raw_path) as im:
        im.load()
        out["rawSize"] = list(im.size)
        out["rawMode"] = im.mode
        # ⚠ ALFA BEYAZ ÜZERİNE DÜZLEŞTİRİLİR, ATILMAZ.
        # `convert("L")` alfayı sessizce ATAR: saydam bir piksel, altındaki
        # RGB değeri neyse o olur. Faz 5 teslimatının 68 dosyasının hepsi
        # RGBA geldi (alfa tamamen opak, yani zararsız) — ama hat, saydamlık
        # GERÇEKTEN kullanılan bir dosyada siyah lekeler üretirdi. Düzleştirme
        # niyeti açık yazar: baskı zemini BEYAZ kâğıttır.
        if "A" in im.mode or "transparency" in im.info:
            flat = Image.new("RGBA", im.size, (255, 255, 255, 255))
            flat.alpha_composite(im.convert("RGBA"))
            base = flat.convert("L")
            out["alphaFlattened"] = True
        else:
            base = im.convert("L")
            out["alphaFlattened"] = False

        before = sum(base.histogram()[spec.PREPRESS["white_point"]:])
        base = clamp_white(base)
        out["whitePoint"] = spec.PREPRESS["white_point"]
        out["paperNoiseCleanedPx"] = before - base.histogram()[255]

        for fmt, cfg in spec.FORMATS.items():
            target = k[f"{fmt}_px"]
            resized = fit_no_distort(base, target)
            dest_dir = os.path.join(spec.PROCESSED_DIR, cfg["dir"])
            os.makedirs(dest_dir, exist_ok=True)
            dest = os.path.join(dest_dir, f"{image_id}.{cfg['ext']}")

            if cfg["ext"] == "tif":
                resized.save(dest, format="TIFF", compression="tiff_lzw",
                             dpi=(cfg["dpi"], cfg["dpi"]))
            elif cfg["ext"] == "png":
                # ÇİZGİ SANATI 1 BİTTİR (imagespec § FORMATS notu).
                # Eşikleme kullanılır, nicemleme DEĞİL: `quantize(colors=2)`
                # bu içerikte boş görüntü üretiyor.
                if cfg.get("bilevel"):
                    th = cfg["threshold"]
                    bw = resized.point(lambda v, t=th: 0 if v < t else 255,
                                       mode="L").convert("1")
                    bw.save(dest, format="PNG", optimize=True,
                            dpi=(cfg["dpi"], cfg["dpi"]))
                else:
                    resized.quantize(colors=16, method=Image.MEDIANCUT).save(
                        dest, format="PNG", optimize=True,
                        dpi=(cfg["dpi"], cfg["dpi"]))
            elif cfg["ext"] == "webp":
                resized.save(dest, format="WEBP", lossless=True, quality=100)

            out["outputs"][fmt] = {
                "path": os.path.relpath(dest, mb.ROOT),
                "size": list(target),
                "bytes": os.path.getsize(dest),
            }
    return out


def raw_files() -> list[tuple[str, str, str]]:
    """(yol, KANONİK kimlik, tür) — dosya adı sapmaları normalize edilir."""
    found = []
    if not os.path.isdir(spec.RAW_DIR):
        return found
    for name in sorted(os.listdir(spec.RAW_DIR)):
        if not name.lower().endswith(f".{spec.RAW_FORMAT}"):
            continue
        image_id, _renamed = spec.canonical_id(name.rsplit(".", 1)[0])
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

        # yetim ve eksik
        have = {i for _, i, _ in raws}
        want = spec.expected_ids()
        r.warn(not (have - want), "yetim ham görsel yok",
               f"prompt kütüphanesinde olmayan dosya: {sorted(have - want)[:10]}")

        # ⚠ ÖLÜ KURAL DÜZELTMESİ (Faz 5) — burada `r.ok(...)` yazıyordu.
        # `Result.ok()` KOŞULSUZ GEÇER: ikinci argüman yalnızca bir metindir,
        # bir eşik değil. Yani "eksik: 40" yazan bir hat da YEŞİL yanıyordu ve
        # 68 görselin tamlığı hiçbir kapıya bağlı değildi. `illustration.total`
        # fiyat modelinin dayanağıdır (K4) — eksik görsel sessizce geçemez.
        missing_ids = sorted(want - have)
        r.add(not missing_ids,
              f"{len(have)}/{spec.TOTAL} görsel geldi",
              f"{len(missing_ids)} görsel EKSİK: {missing_ids[:10]}"
              f"{' …' if len(missing_ids) > 10 else ''} — 45+22+1=68 illüstrasyon "
              "fiyat modelinin dayanağıdır (K4), eksik görsel sessizce geçemez")

        # ⚠ İKİNCİ ÖLÜ KURAL (Faz 5) — Kindle dosya bütçesi YALNIZCA
        # `calibrate()` içinde denetleniyordu ve `calibrate()` yalnızca HAM
        # GÖRSEL YOKKEN çalışıyordu. Yani bütçe, sınanması gereken tek anda —
        # gerçek görseller geldiğinde — hiç sınanmıyordu. 3,0 MB sayısı
        # 5,14 $ telifin ta kendisidir (project_config § kindle.fileBudgetMb).
        #
        # ⚠ `--check` DE ÖLÇER. İlk düzeltme bütçeyi yalnızca dönüştürme
        # yolunda denetliyordu — ama `qa_all.sh` `--check` çağırır, yani
        # kural CI'da yine ölüydü. Denetim yolunda sayı diskteki türevlerden
        # okunur; yeniden dönüştürmeye gerek yok.
        if args.check:
            kindle_bytes = print_bytes = 0
            for _p, image_id, _k in raws:
                for fmt, cfg in spec.FORMATS.items():
                    f = os.path.join(spec.PROCESSED_DIR, cfg["dir"],
                                     f"{image_id}.{cfg['ext']}")
                    if not os.path.exists(f):
                        continue
                    if fmt == "kindle":
                        kindle_bytes += os.path.getsize(f)
                    elif fmt == "print":
                        print_bytes += os.path.getsize(f)
            results = results or [None]        # aşağıdaki blok koşsun
        elif results:
            kindle_bytes = sum(o["outputs"]["kindle"]["bytes"] for o in results)
            print_bytes = sum(o["outputs"]["print"]["bytes"] for o in results)

        if results:
            if not args.check:
                payload["converted"] = results
            budget_mb = mb._CFG["editions"]["kindle"]["fileBudgetMb"]
            # Metin payı TAHMİN EDİLMEZ, ÖLÇÜLMÜŞSE OKUNUR. `epub.py` gerçek
            # paketi kurar ve metin baytını yazar (ölçüm: 0,13 MB — kalibrasyon
            # tahmini 0,60 MB'dı, yani dört kat muhafazakâr). İki sayıyı ayrı
            # tutmak, aynı bütçe için iki farklı cevap üretirdi.
            overhead_mb = 0.6
            epub_report = os.path.join(mb.REPORTS_TRACKED, "epub-build.json")
            if os.path.exists(epub_report):
                try:
                    with open(epub_report, encoding="utf-8") as fh:
                        overhead_mb = json.load(fh)["textBytes"] / 1e6
                except (OSError, KeyError, ValueError):
                    pass
            projected = kindle_bytes / 1e6 + overhead_mb
            payload["kindleTotals"] = {
                "imageBytes": kindle_bytes,
                "overheadMb": overhead_mb,
                "projectedMb": round(projected, 3),
                "budgetMb": budget_mb,
            }
            print(f"\n  Kindle görsel payı : {kindle_bytes / 1e6:.2f} MB")
            print(f"  + metin/EPUB payı  : {overhead_mb:.2f} MB")
            print(f"  = projeksiyon      : {projected:.2f} MB  (bütçe {budget_mb:.2f} MB)")
            print(f"  baskı TIFF toplamı : {print_bytes / 1e6:.0f} MB")
            r.add(projected <= budget_mb,
                  f"Kindle dosya bütçesi tutuyor ({projected:.2f} ≤ {budget_mb:.2f} MB)",
                  f"Kindle projeksiyonu {projected:.2f} MB > {budget_mb:.2f} MB — "
                  f"0,15 $/MB teslim ücreti telifi "
                  f"{(projected - budget_mb) * 0.15:.2f} $ düşürür")
            r.add(print_bytes / 1e6 < 650,
                  f"baskı varlık toplamı KDP sınırının altında "
                  f"({print_bytes / 1e6:.0f} MB < 650 MB)",
                  f"baskı varlıkları {print_bytes / 1e6:.0f} MB — KDP 650 MB sınırı")

    # `--check` HİÇBİR ŞEY DÖNÜŞTÜRMEZ; raporu boş yükle EZMEZ (Faz 5 düzeltmesi).
    if not args.check:
        os.makedirs(mb.REPORTS_TRACKED, exist_ok=True)
        with open(args.json or REPORT, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=2)
            fh.write("\n")

    return r.finish(None)


if __name__ == "__main__":
    sys.exit(main())
