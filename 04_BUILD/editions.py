#!/usr/bin/env python3
"""
SÜRÜM KAYIT DEFTERİ — KDP ÜRETİM MODELİ
================================================================================
Bir "sürüm" = bir ürün SKU'su. Her sürüm kendi iç blok tipografisini, kendi
kapak geometrisini ve kendi doğrulama eşiklerini taşır. Hiçbir betikte
sürüme özgü sabit yoktur; hepsi buradan okunur.

    from editions import EDITIONS, get, print_cost, royalty
    ed = get("hardcover")

Yeni bir sürüm eklemek = buraya bir Edition satırı eklemek.

--------------------------------------------------------------------------------
KAYNAKLAR — Amazon KDP resmî yardım sayfaları, Ağustos 2026 itibarıyla
okunmuş hâli. Master yol haritası § BÖLÜM 01.1 "Doğrulanmış" etiketiyle
kayıt altına almıştır. Amazon bu değerleri önceden haber vermeden
değiştirebilir; yayına gitmeden panelden TEYİT EDİLİR.
--------------------------------------------------------------------------------
  · İç marj (gutter) — "Set Trim Size, Bleed, and Margins"
        24–150 s : 0.375"   151–300 s : 0.500"   301–500 s : 0.625"
       501–700 s : 0.750"   701–828 s : 0.875"
    Dış/üst/alt asgari: taşmasız 0.25", taşmalı 0.375".

  · Ciltsiz baskı maliyeti (ABD, normal trim, s-b):
        24–110 s = 2,30 $ sabit · 110–828 s = 1,00 $ + 0,012 $/sayfa

  · Ciltli baskı maliyeti (ABD, s-b):
        75–108 s = 6,80 $ sabit · 110–550 s = 5,65 $ + 0,012 $/sayfa
    Minimum 75, maksimum 550 sayfa. Ciltlide STANDART RENKLİ YOKTUR.

  · Baskı telifi: %60 (≥9,99 $) · %50 (≤9,98 $) · genişletilmiş dağıtım %40

  · E-kitap telifi: %70 bandı 2,99–12,99 $ (7 Tem 2026'da 9,99 $'dan
    yükseldi), teslim ücreti 0,15 $/MB. %35 bandı 0,99–200 $, teslim ücreti yok.
"""

from __future__ import annotations

import argparse
import math
import os
import sys
from dataclasses import dataclass, field

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb


# =============================================================================
# 1. KDP TABLOLARI (DOĞRULANMIŞ)
# =============================================================================

GUTTER_TABLE = [
    (24, 150, 0.375),
    (151, 300, 0.500),
    (301, 500, 0.625),
    (501, 700, 0.750),
    (701, 828, 0.875),
]

OUTER_MIN_NO_BLEED = 0.25
OUTER_MIN_BLEED = 0.375

# Baskı telifi eşiği
ROYALTY_HIGH = 0.60
ROYALTY_LOW = 0.50
ROYALTY_THRESHOLD_USD = 9.99

# KDP sayfa sınırları — 6×9 siyah-beyaz. Bu sayılar üç yerde ayrı ayrı
# yazılıydı (dosya başlığı · print_cost dalları · yol haritası § 18) ve
# üçünü ayrı tutmak tam olarak "ayrışan kapı" riskidir. Tek yer burasıdır.
PAGE_LIMITS = {
    "paperback": (24, 828),
    "hardcover": (75, 550),
}

# E-kitap
EBOOK_70_BAND = (2.99, 12.99)
EBOOK_DELIVERY_PER_MB = 0.15


def required_gutter(pages: int) -> float:
    for lo, hi, g in GUTTER_TABLE:
        if lo <= pages <= hi:
            return g
    if pages < 24:
        raise ValueError(f"{pages} sayfa — KDP asgarisi 24")
    raise ValueError(f"{pages} sayfa — KDP azamisi 828")


def print_cost(binding: str, pages: int, trim: str = "regular", ink: str = "bw") -> float:
    """ABD baskı maliyeti."""
    if ink != "bw":
        raise NotImplementedError(
            "Bu kitap SİYAH-BEYAZ basılır. Yol haritası: renkli baskı bu sayfa "
            "sayısında maliyeti 15,95 $'a çıkarır, fiyatı 39,99 $'a iter ve "
            "KİTABI KATEGORİDEN ÇIKARIR."
        )
    if trim != "regular":
        raise NotImplementedError("6×9 normal trimdir; geniş trim bu kitapta kullanılmaz")

    lo, hi = PAGE_LIMITS[binding]
    if binding == "paperback":
        if pages < lo:
            raise ValueError(f"ciltsiz asgari {lo} sayfa ({pages})")
        if pages <= 110:
            return 2.30
        if pages > hi:
            raise ValueError(f"ciltsiz azami {hi} sayfa ({pages})")
        return 1.00 + 0.012 * pages

    if binding == "hardcover":
        if pages < lo:
            raise ValueError(f"ciltli asgari {lo} sayfa ({pages}) — KDP kuralı")
        if pages <= 108:
            return 6.80
        if pages > hi:
            raise ValueError(f"ciltli azami {hi} sayfa ({pages}) — KDP kuralı")
        return 5.65 + 0.012 * pages

    raise ValueError(f"bilinmeyen ciltleme: {binding}")


def print_royalty(price: float, cost: float) -> float:
    rate = ROYALTY_HIGH if price >= ROYALTY_THRESHOLD_USD else ROYALTY_LOW
    return price * rate - cost


def ebook_royalty(price: float, file_mb: float, rate: float = 0.70) -> float:
    if rate == 0.70:
        lo, hi = EBOOK_70_BAND
        if not (lo <= price <= hi):
            raise ValueError(f"%70 telif bandı {lo}–{hi} $; fiyat {price} $")
        return price * 0.70 - file_mb * EBOOK_DELIVERY_PER_MB
    return price * 0.35


def max_ebook_mb(price: float, target_royalty: float) -> float:
    """Hedef telifi korumak için azami dosya boyutu."""
    return (price * 0.70 - target_royalty) / EBOOK_DELIVERY_PER_MB


def breakeven_acos(royalty: float, price: float) -> float:
    return royalty / price * 100 if price else 0.0


# =============================================================================
# 2. TİPOGRAFİ PROFİLLERİ
# =============================================================================

@dataclass(frozen=True)
class Typography:
    """İç blok tipografisi. Ölçüler punto (pt) ve inç."""
    body_pt: float
    leading_pt: float
    margin_top_in: float
    margin_bottom_in: float
    margin_outer_in: float
    # Ortalama karakter genişliği / punto oranı — gövde yazı karakterine bağlı.
    # DİKKAT: bu bir TAHMİNDİR ve Faz 1'de GERÇEK DİZGİYLE kalibre edilir.
    # Bestiarium D36: dolguyla ölçmek "modeli modele karşı sınamaktır".
    avg_char_width_ratio: float = 0.48
    avg_chars_per_word: float = 5.4          # boşluk dâhil, çocuk İngilizcesi
    calibrated: bool = False
    calibration_source: str = ""


@dataclass(frozen=True)
class Edition:
    key: str
    label: str
    binding: str                    # paperback · hardcover · kindle
    enabled: bool
    launch: bool
    price_usd: float
    typography: Typography | None
    trim_w_in: float = 6.0
    trim_h_in: float = 9.0
    notes: str = ""
    roadmap_cost_usd: float | None = None      # yol haritasının verdiği sayı
    roadmap_royalty_usd: float | None = None
    file_budget_mb: float | None = None
    tags: list = field(default_factory=list)


# 8–12 yaş için gövde puntosu yetişkin cildinden BÜYÜKTÜR. Bu bir konfor
# kararı değil, bir yaş kararıdır: 12 pt / 16,5 pt bölüm-kitabı normudur.
CHILD_BODY = Typography(
    body_pt=12.0,
    leading_pt=16.5,
    margin_top_in=0.75,
    margin_bottom_in=0.75,
    margin_outer_in=0.625,
    # ✅ FAZ 1'DE GERÇEK DİZGİYLE KALİBRE EDİLDİ (karar K3 · K27).
    # Aşağıdaki iki sayı artık TAHMİN DEĞİL ÖLÇÜMDÜR: pilot hikâyenin
    # gerçek prozası, gerçek 4,875"×7,5" metin bloğuna, gerçek yazı
    # karakteri genişlik tablolarıyla dizildi ve satırlar sayıldı.
    # Ölçüm: 04_BUILD/calibrate_pages.py → 06_REPORTS/tracked/page-calibration.json
    #
    # Tahmin ne kadar yanlıştı: kelime/sayfa 361,1 (tahmin) → 357,5 (ölçüm),
    # yani %1,0. Tipografi tahmini İYİYDİ. Asıl sürpriz başka yerdeydi:
    # yazı karakteri seçimi kelime/sayfa'yı %21 oynatıyor (DejaVu Serif
    # 282,8 · Times/Liberation 357,5). Model hatası değil YAZI KARAKTERİ
    # KARARI baskındır ve o karar Faz 5'e aittir.
    avg_char_width_ratio=0.4895,     # ölçüldü (tahmin 0,48 idi)
    avg_chars_per_word=5.349,        # pilot prozasından ölçüldü (tahmin 5,4 idi)
    calibrated=True,
    calibration_source=(
        "Faz 1 · korean-dangun (972 kelime) · Times-Roman & Liberation Serif "
        "12/16,5 pt · 06_REPORTS/tracked/page-calibration.json"
    ),
)

LARGE_PRINT_BODY = Typography(
    body_pt=16.0,
    leading_pt=24.0,
    margin_top_in=0.85,
    margin_bottom_in=0.85,
    margin_outer_in=0.75,
    calibrated=False,
    calibration_source="devre dışı sürüm — A6/K6",
)


EDITIONS: dict[str, Edition] = {
    "paperback": Edition(
        key="paperback",
        label="Ciltsiz (perfect bound)",
        binding="paperback",
        enabled=True,
        launch=True,
        price_usd=16.99,
        typography=CHILD_BODY,
        roadmap_cost_usd=3.76,
        roadmap_royalty_usd=6.43,
        notes="Başabaş ACOS %37,8 — reklam rahat çalışır.",
        tags=["launch", "primary"],
    ),
    "hardcover": Edition(
        key="hardcover",
        label="Ciltli (case laminate)",
        binding="hardcover",
        enabled=True,
        launch=True,
        price_usd=26.99,
        typography=CHILD_BODY,
        roadmap_cost_usd=8.41,
        roadmap_royalty_usd=7.78,
        notes=("Yol haritası: 'Bu kitapta ciltli LANSMANLA BİRLİKTE açılmalı — "
               "okul/kütüphane ve hediye alımı ciltliye gider.' KDP ciltli "
               "sayfa sınırı 75–550."),
        tags=["launch", "library", "gift"],
    ),
    "kindle": Edition(
        key="kindle",
        label="Kindle e-kitap",
        binding="kindle",
        enabled=True,
        launch=True,
        price_usd=7.99,
        typography=None,
        roadmap_royalty_usd=5.14,
        file_budget_mb=3.0,
        notes=("Dosya bütçesi TÜRETİLMİŞTİR, seçilmemiştir: 7,99 $ × %70 = 5,593 $; "
               "yol haritasının verdiği 5,14 $ telif, 0,453 $ teslim ücreti demektir; "
               "0,15 $/MB'de bu 3,02 MB eder. Bütçe 3,0 MB."),
        tags=["launch"],
    ),
    "largeprint": Edition(
        key="largeprint",
        label="Büyük punto",
        binding="paperback",
        enabled=False,
        launch=False,
        price_usd=19.99,
        typography=LARGE_PRINT_BODY,
        notes=("DEVRE DIŞI — karar K6/A6. Yol haritası büyük puntoyu 'uzun vadeli "
               "genişleme' listesine koyuyor, lansman formatlarına değil. Tanımlı "
               "tutulur ki hat bozulmadan beklesin; kurucu isterse enabled=True yeter."),
        tags=["derivative"],
    ),
}


def get(key: str) -> Edition:
    return EDITIONS[key]


def launch_editions() -> list[Edition]:
    return [e for e in EDITIONS.values() if e.enabled and e.launch]


# =============================================================================
# 3. SAYFA GEOMETRİSİ
# =============================================================================

def text_block(ed: Edition, pages: int) -> tuple[float, float]:
    """(genişlik, yükseklik) inç."""
    t = ed.typography
    if t is None:
        raise ValueError(f"{ed.key} bir e-kitaptır; sabit sayfa geometrisi yoktur")
    gutter = required_gutter(pages)
    w = ed.trim_w_in - gutter - t.margin_outer_in
    h = ed.trim_h_in - t.margin_top_in - t.margin_bottom_in
    return w, h


def lines_per_page(ed: Edition, pages: int) -> int:
    _, h = text_block(ed, pages)
    return int(h * 72 // ed.typography.leading_pt)


def words_per_page(ed: Edition, pages: int) -> float:
    t = ed.typography
    w, _ = text_block(ed, pages)
    chars_per_line = (w * 72) / (t.body_pt * t.avg_char_width_ratio)
    words_per_line = chars_per_line / t.avg_chars_per_word
    return lines_per_page(ed, pages) * words_per_line


# =============================================================================
# 4. DOĞRULAMA
# =============================================================================

def verify(pages: int, r: mb.Result) -> None:
    """Yol haritasının verdiği maliyet ve telif sayıları KDP tablosundan
    türetilebiliyor mu? Türetilemiyorsa ya sayfa modeli ya yol haritası
    yanlıştır — ve ikisini de bilmek gerekir."""

    mb.banner(f"sürüm doğrulaması · {pages} sayfa")

    for ed in EDITIONS.values():
        if not ed.enabled:
            r.ok(f"{ed.key}: devre dışı", ed.notes.split(".")[0])
            continue

        if ed.binding == "kindle":
            mbs = ed.file_budget_mb or 0
            roy = ebook_royalty(ed.price_usd, mbs)
            r.add(abs(roy - (ed.roadmap_royalty_usd or roy)) < 0.02,
                  f"{ed.key}: {ed.price_usd:.2f} $ · {mbs:.1f} MB → telif {roy:.2f} $",
                  f"{ed.key} telifi {roy:.2f} $, yol haritası {ed.roadmap_royalty_usd} $ diyor")
            cap = max_ebook_mb(ed.price_usd, ed.roadmap_royalty_usd or roy)
            print(f"        azami dosya boyutu (telifi korumak için): {cap:.2f} MB")
            continue

        # --- baskı ---
        try:
            cost = print_cost(ed.binding, pages)
        except ValueError as exc:
            r.fail(f"{ed.key}: sayfa sayısı KDP sınırları dışında", str(exc))
            continue

        roy = print_royalty(ed.price_usd, cost)
        acos = breakeven_acos(roy, ed.price_usd)

        if ed.roadmap_cost_usd is not None:
            ok = abs(cost - ed.roadmap_cost_usd) < 0.02
            r.add(ok,
                  f"{ed.key}: {pages} sayfa → maliyet {cost:.2f} $ "
                  f"(yol haritası {ed.roadmap_cost_usd:.2f} $)",
                  f"{ed.key} maliyeti {cost:.2f} $, yol haritası {ed.roadmap_cost_usd:.2f} $ "
                  f"diyor — SAYFA MODELİ ile YOL HARİTASI AYRIŞMIŞ")
        if ed.roadmap_royalty_usd is not None:
            ok = abs(roy - ed.roadmap_royalty_usd) < 0.02
            r.add(ok,
                  f"{ed.key}: telif {roy:.2f} $ · başabaş ACOS %{acos:.1f}",
                  f"{ed.key} telifi {roy:.2f} $, yol haritası {ed.roadmap_royalty_usd:.2f} $ diyor")

        r.add(roy > 0, f"{ed.key}: telif pozitif", f"{ed.key} telifi NEGATİF ({roy:.2f} $)")

        gutter = required_gutter(pages)
        w, h = text_block(ed, pages)
        print(f"        iç marj {gutter}\" · metin bloğu {w:.3f}×{h:.3f}\" · "
              f"{lines_per_page(ed, pages)} satır · ~{words_per_page(ed, pages):.0f} kelime/sayfa")


def main() -> int:
    ap = argparse.ArgumentParser(description="Sürüm kayıt defteri ve doğrulaması")
    ap.add_argument("--pages", type=int, default=None, help="sayfa sayısı (varsayılan: hedef)")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    pages = args.pages or mb.PAGE_TARGET

    print("═" * 72)
    print(f"  SÜRÜM KAYIT DEFTERİ · {pages} sayfa · 6×9 · siyah-beyaz")
    print("═" * 72)

    r = mb.Result("editions", verbose=args.verbose)
    verify(pages, r)

    launch = launch_editions()
    r.add(any(e.key == "hardcover" for e in launch),
          "ciltli lansman formatları arasında",
          "ciltli lansmanda yok — yol haritasının açık kararına aykırı")

    return r.finish(args.json)


if __name__ == "__main__":
    sys.exit(main())
