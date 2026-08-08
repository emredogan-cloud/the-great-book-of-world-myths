"""
GÖRSEL ŞARTNAMESİ — 68 GÖRSELİN TEK DOĞRULUK KAYNAĞI
================================================================================
İLLÜSTRASYON BU PROJEDE ZORUNLUDUR (karar K4).

Yol haritası bunu bir öneri olarak değil, FİYAT MODELİNİN DAYANAĞI olarak
karara bağlamış:

    İllüstrasyon: "45 bölüm açılış çizimi + 22 kültür vinyeti, SİYAH-BEYAZ"
    Gerekçe: "Renkli baskı bu sayfa sayısında maliyeti 15,95 $'a çıkarır —
              fiyatı 39,99 $'a iter, KATEGORİDEN ÇIKARIR."
    Harita: "1 dünya haritası (22 kültürün konumu) — ön veya arka iç kapak"
    Gerekçe: "Ebeveynin 'eğitici' algısını tek görselde kurar."

45 + 22 + 1 = 68.

--------------------------------------------------------------------------------
ÜSLUP GÖVDESİ TEK YERDE DURUR (Bestiarium D7 / karar K16)
--------------------------------------------------------------------------------
Prompt kütüphanesi ÜRETİLİR, elle yazılmaz. Üslup gövdesi değişirse 68
prompt birlikte değişir. "Tek çizgi dili" şartı ancak böyle tutulabilir.

--------------------------------------------------------------------------------
BESTIARIUM'DAN TAŞINMAYAN ŞEY
--------------------------------------------------------------------------------
Bestiarium'un çizgi dili ANTİKA GRAVÜRDÜR ve 120 plakanın aynı tarama
geometrisinde olması ürünün kendisidir; ölçümü tarama açısı ve darbe/periyot
üzerineydi. Bu kitabın çizgi dili ÇOCUK İLLÜSTRASYONUDUR. Ölçülecek şey
tarama frekansı değil: kadraj, kontrast, mürekkep yoğunluğu ve BASKIDA
OKUNABİLİRLİK.
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb


# =============================================================================
# 1. ÜSLUP GÖVDESİ — 68 PROMPTTA AYNI
# =============================================================================
# Bu dizeler prompt kütüphanesinin imzasıdır. make_prompts.py --check
# hepsinin 68 promptta da geçtiğini kanıtlar; geçmiyorsa "tek çizgi dili"
# şartı ihlal edilmiş demektir ve CI kırmızı yanar.

STYLE_BODY = (
    "black and white pen-and-ink illustration for a children's book, "
    "confident varied line weight, open uncluttered composition, "
    "generous white space, warm and inviting rather than frightening, "
    "no cross-hatching denser than the eye can read at 6x9 inches"
)

STYLE_SIGNATURE = "black and white pen-and-ink illustration for a children's book"

# AGE_POLICY § 2.17 doğrudan buraya iner. "Look Inside"da görünen ilk şey
# bir illüstrasyondur ve ebeveynin ilk izlenimini o kurar (yol haritası R4).
NEGATIVE_PROMPT = (
    "no blood, no gore, no wounds, no corpses, no severed limbs, "
    "no visible entrails, no torture, no nudity, no sexualised figures, "
    "no terrified faces in close-up, no photorealism, no colour, "
    "no grey wash, no digital gradients, no text, no lettering, "
    "no watermark, no signature, no modern objects, no cultural pastiche, "
    "no generic fantasy armour, no stereotyped features"
)

# Her promptta bulunması zorunlu iki teknik işaret
COMPOSITION_MARKER = "upper half of a 6x9 inch page"
VIGNETTE_MARKER = "small spot illustration, no frame"


# =============================================================================
# 2. GÖRSEL TÜRLERİ
# =============================================================================

KINDS = {
    "story": {
        "count": mb.STORY_TARGET,
        "prefix": "story",
        "purpose": "Hikâye açılış çizimi — sayfanın üst yarısı",
        "placement": "Hikâyenin ilk sayfasının üst yarısı",
        "aspect": "3:2 (yatay)",
        "raw_px": (2400, 1600),
        "print_dpi": 600,
        "print_px": (3000, 2000),
        "kindle_px": (1200, 800),
        "web_px": (1400, 933),
        "marker": COMPOSITION_MARKER,
    },
    "culture": {
        "count": mb.CULTURE_TARGET,
        "prefix": "culture",
        "purpose": "Kültür vinyeti — kültür kartında",
        "placement": "Kültür kartı (DECISIONS § A4)",
        "aspect": "1:1 (kare)",
        "raw_px": (1600, 1600),
        "print_dpi": 600,
        "print_px": (1800, 1800),
        "kindle_px": (800, 800),
        "web_px": (900, 900),
        "marker": VIGNETTE_MARKER,
    },
    "map": {
        "count": 1,
        "prefix": "map",
        "purpose": "Dünya haritası — 22 kültürün konumu",
        "placement": "Ön veya arka iç kapak (açık sayfa)",
        "aspect": "2:1 (açık sayfa)",
        "raw_px": (4800, 2400),
        "print_dpi": 600,
        "print_px": (7200, 3600),
        "kindle_px": (1600, 800),
        "web_px": (2000, 1000),
        "marker": "double-page spread map",
    },
}

TOTAL = sum(k["count"] for k in KINDS.values())

# Üretim formatları — RAW ASLA ÜZERİNE YAZILMAZ (karar K5)
FORMATS = {
    "print":  {"dir": "print",  "ext": "tif",  "mode": "L", "dpi": 600,
               "note": "Baskı iç bloğu — gri tonlama TIFF, sıkıştırmasız"},
    "kindle": {"dir": "kindle", "ext": "png",  "mode": "L", "dpi": 300,
               "note": "Kindle — dosya bütçesine optimize (3,0 MB toplam)"},
    "web":    {"dir": "web",    "ext": "webp", "mode": "L", "dpi": 144,
               "note": "A+ içerik ve pazarlama — kayıpsız"},
}

RAW_FORMAT = "png"
RAW_DIR = os.path.join(mb.ASSETS, "raw")
PROCESSED_DIR = os.path.join(mb.ASSETS, "processed")


# =============================================================================
# 3. KALİTE TOLERANSLARI
# =============================================================================
# Bestiarium B1 dersi: 45° taramada √2 yanlış ölçen bir cetvel, doğru
# çizilmiş 112 plakanın TAMAMINI reddedecekti. Ölçüm KALİBRE EDİLMEDEN
# hiçbir görsel ölçülmez → 05_TESTS/image_selftest.py

TOLERANCES = {
    # Mürekkep yoğunluğu: siyah piksel oranı. Çok düşük = boş sayfa hissi,
    # çok yüksek = baskıda blok hâline gelir ve kâğıt ıslanır.
    "ink_coverage": (0.04, 0.22),
    # Kontrast: en koyu ve en açık desilin farkı. Düşükse gri görünür.
    "contrast_min": 0.55,
    # Beyaz kenar payı (kadraj): çizim kenara yapışmamalı.
    "margin_share_min": 0.03,
    # İkili eşiğe uzaklık: çocuk illüstrasyonu YARI TONLU DEĞİL, çizgidir.
    # Piksellerin çoğu uçlarda olmalı.
    "bimodality_min": 0.80,
    # En küçük çizgi kalınlığı (baskı pikselinde). Altındaki çizgiler
    # 600 dpi baskıda KAYBOLUR — Bestiarium'un "baskıda okunabilirlik"
    # riskinin çocuk kitabı karşılığı.
    "min_stroke_px": 3.0,
    # Ölçüm doğruluğu — kalibrasyon testinin geçme eşiği
    "calibration_error_max": 0.05,
}
