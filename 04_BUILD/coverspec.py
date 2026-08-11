"""
KAPAK VE A+ İÇERİK ŞARTNAMESİ — TİCARİ GÖRSEL AİLESİ
================================================================================
Bu dosya, kitabın İÇİNDEKİ 68 görselden AYRI bir varlık ailesini tanımlar:
kapaklar ve Amazon A+ içerik modülleri. İkisini karıştırmak sayımı bozar
(talimat § 29) — 68 iç görsel bir envanterdir, bunlar başka bir envanterdir.

--------------------------------------------------------------------------------
KAPAK, MARKANIN BİLİNÇLİ OLARAK ESNETİLDİĞİ TEK YERDİR
--------------------------------------------------------------------------------
Master yol haritası § 18 bunu adıyla yazar:

    "Çocuk kitabı kapağı tür konvansiyonuna uymak zorundadır ve bizim
     'koyu kodeks' dilimiz burada İŞLEMEZ; daha aydınlık, daha karakterli,
     yaş aralığı köşede net bir kapak gerekir."

Bu yüzden `imagespec.STYLE_BODY` buraya UYGULANMAZ. İç blok siyah-beyaz
kalem-mürekkeptir; kapak renkli, sıcak ve karakterlidir. İkisi aynı kitabın
iki farklı işidir ve tek bir üslup gövdesine zorlanamazlar.

--------------------------------------------------------------------------------
TİPOGRAFİ ÜRETİLMEZ, SONRADAN BASILIR
--------------------------------------------------------------------------------
Talimat § 44 ve § 45 kesin: kesin ticari tipografi için görsel üreticisine
GÜVENİLMEZ. Üretici kompozisyonu, karakterleri ve atmosferi verir; başlık,
alt başlık, yaş aralığı ve sırt yazısı CLI ile sonradan basılır. Gerekçe
teknik değil ticaridir: yanlış yazılmış bir başlık, küçük resimde bile
görünür ve iade sebebidir.

Her promptun `typography` alanı bunu makine okunur tutar:
    "post"      → metin sonradan basılır, prompt YER AYIRIR
    "generated" → metnin üretilmesi kasıtlıdır (yalnızca dekoratif olduğunda)
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb


# =============================================================================
# 1. KAPAK ÜSLUP GÖVDESİ — 68 İÇ GÖRSELDEN AYRI
# =============================================================================

COVER_STYLE = (
    "full-colour children's book cover illustration, ages 8 to 12, "
    "warm and inviting, bright saturated palette with a clear focal point, "
    "characterful stylised figures with friendly readable faces, "
    "storybook poster composition rather than a busy collage, "
    "strong silhouette that still reads when the image is one inch wide"
)

COVER_SIGNATURE = "full-colour children's book cover illustration, ages 8 to 12"

COVER_NEGATIVE = (
    "no blood, no gore, no wounds, no corpses, no weapons pointed at the viewer, "
    "no nudity, no sexualised figures, no terrified faces, no horror imagery, "
    "no dark gothic codex styling, no muted desaturated palette, "
    "no photorealism, no 3D render, no anime pastiche, "
    "no text, no lettering, no title, no logo, no watermark, no signature, "
    "no cultural pastiche, no stereotyped features, no sacred or restricted "
    "ceremonial imagery, no religious iconography presented as decoration, "
    "no busy edge-to-edge detail that collapses at thumbnail size"
)

# A+ görselleri kitabın İÇ dilini taklit etmemeli ama ondan kopuk da olmamalı.
APLUS_STYLE = (
    "clean marketing illustration for a children's book product page, "
    "generous flat background, one clear subject, "
    "colour palette drawn from the book cover, "
    "calm uncluttered composition with deliberate empty space for text"
)

APLUS_NEGATIVE = (
    "no text, no lettering, no logos, no watermark, no signature, "
    "no user interface elements, no fake screenshots, no star ratings, "
    "no price tags, no Amazon branding, no busy collage, no photorealism, "
    "no stereotyped features, no cultural pastiche"
)


# =============================================================================
# 2. SIRT VE TAŞMA — SAYFA SAYISINDAN TÜRETİLİR
# =============================================================================
# ⚠ BU SAYILAR TÜRETİLMİŞTİR, SEÇİLMEMİŞTİR ve SAYFA SAYISINA BAĞLIDIR.
# Sayfa sayısı değişirse sırt genişliği değişir ve kapak dosyası geçersizleşir.
# Faz 6 nihai sayıyı KDP'nin KENDİ ŞABLON ÜRETİCİSİNDEN alacaktır; buradaki
# hesap prompt şartnamesini üretmek ve oranı doğru vermek içindir.

BLEED_IN = 0.125
SPINE_PER_PAGE_CREAM_IN = 0.0025      # KDP: siyah-beyaz · krem kâğıt

# =============================================================================
# CİLTLİ GEOMETRİ — KDP COVER CALCULATOR'DAN OKUNDU, TÜRETİLMEDİ
# =============================================================================
# ⚠ CİLTLİ GEOMETRİ ARTIK HİÇ TÜRETİLMİYOR. Aşağıdaki tablo KDP'nin kendi
# hesaplayıcısının ekran görüntüsünden birebir alınmıştır:
#
#     kdp.amazon.com/en_US/cover-calculator
#     Hardcover · Black & white · Cream paper · Left to Right · Inches
#     6 × 9 in · 234 sayfa   (11 Ağustos 2026, kurucu)
#
# İKİ TÜRETME DENENDİ VE İKİSİ DE YANLIŞTI:
#
#   Faz 6 : 2×(6,0 + 0,510) + 0,645 = 13,665 × 10,020
#   Faz 7d: 2×(6,0 + 0,591) + 0,774 = 13,956 × 10,182
#   KDP   :                           14,349 × 10,417
#
# İkinci türetme sırtı ve sarımı DOĞRU aldı ve hâlâ yanlıştı. Kaçırılan şey
# şuydu: **CİLTLİ KAPAKTA PANEL, TRIM DEĞİL KARTONDUR.** Karton kitap
# bloğundan taşar ("square"): 6,197 × 9,236, yani trim'den 0,197" geniş ve
# 0,236" uzun. Panel olarak 6×9 kullanan her formül dar kapak üretir.
#
# Ders: yayımlanmamış bir formülü türetmek, iki kez üst üste yanlış
# yapılabilir. Sayı yayımlanmıyorsa TABLO OKUNUR.
#
# Tablonun kendi içinde tutarlılığı doğrulandı:
#     2×(front 6,197 + wrap 0,591) + spine 0,774 = 14,350 ≈ 14,349 ✓
#     front_h 9,236 + 2×wrap 0,591               = 10,418 ≈ 10,417 ✓
#     menteşe genişliğe EKLENMEZ (sarımın içindedir) ✓

HARDCOVER_KDP = {
    "source": "KDP Print Cover Calculator (kdp.amazon.com/en_US/cover-calculator)",
    "inputs": "Hardcover · Black & white · Cream paper · 6×9 in · 234 pages",
    "readOn": "2026-08-11",
    "pages": 234,
    # 1 · Full Cover
    "fullCoverIn": [14.349, 10.417],
    # 2 · Front Cover — KARTON ölçüsü (trim DEĞİL)
    "frontCoverIn": [6.197, 9.236],
    # 3 · Margin — karton kenarından güvenli alana
    "marginIn": 0.125,
    # 4 · Wrap — kartonun etrafına dolanan pay
    "wrapIn": 0.591,
    # 5 · Hinge — sırtın iki yanı; GENİŞLİĞE EKLENMEZ, güvenli alanı daraltır
    "hingeIn": 0.394,
    # 6 · Spine
    "spineIn": 0.774,
    # 7 · Spine Safe Area
    "spineSafeIn": [0.649, 8.986],
    # 8 · Spine Margin
    "spineMarginIn": 0.062,
    # 9 · Barcode Margin
    "barcodeMarginIn": [0.25, 0.375],
}

# Geriye dönük adlar — tek kaynak yukarıdaki tablodur.
HARDCOVER_WRAP_IN = HARDCOVER_KDP["wrapIn"]
HARDCOVER_HINGE_IN = HARDCOVER_KDP["hingeIn"]
HARDCOVER_MARGIN_IN = HARDCOVER_KDP["marginIn"]

# Barkod alanı — KDP belgesinden. KDP kendi barkodunu basar; bizim işimiz
# o dikdörtgeni TEMİZ bırakmaktır.
BARCODE_W_IN = 2.0                    # "2" (50.8 mm) wide"
BARCODE_H_IN = 1.2                    # "1.2" (30.5 mm) high"
BARCODE_FROM_BOTTOM_IN = 0.76         # "at least 0.76" (19 mm) from the bottom"
BARCODE_FROM_HINGE_IN = 0.25          # "0.25" (6 mm) from the spine hinge"

# Ciltli geometri TÜRETİLMİYOR — tablodan okunuyor.
HARDCOVER_SPINE_IS_DERIVED = False

# ⚠ TABLO TEK BİR SAYFA SAYISI İÇİNDİR.
# 234 sayfa için okundu. BAŞKA bir sayfa sayısında bu tablonun HİÇBİR
# satırı geçerli değildir — sırt da, karton da, tam kapak da değişir.
# `covers.py` bunu kapıya bağlar: sayfa sayısı değişirse kırmızı yanar ve
# kurucudan hesaplayıcıyı yeniden çalıştırmasını ister.
HARDCOVER_SPINE_ANCHOR = {
    "pages": HARDCOVER_KDP["pages"],
    "spineIn": HARDCOVER_KDP["spineIn"],
    "source": HARDCOVER_KDP["source"],
    "verifiedOn": HARDCOVER_KDP["readOn"],
}


def hardcover_board_in() -> tuple[float, float]:
    """Ciltli PANEL ölçüsü — karton, trim değil (KDP 'Front Cover')."""
    w, h = HARDCOVER_KDP["frontCoverIn"]
    return w, h


def spine_width_in(pages: int, binding: str = "paperback") -> float:
    """
    Sırt genişliği.

    CİLTSİZ: KDP formülü YAYIMLANMIŞTIR → sayfa × 0,0025 (krem · s-b).
    CİLTLİ : KDP formül yayımlamıyor → TABLODAN okunur, türetilmez.
             Tablo tek sayfa sayısı içindir; `hardcover_geometry_is_anchored`
             başka sayfa sayısında kapıyı kırmızı yakar.
    """
    if binding == "hardcover":
        return HARDCOVER_KDP["spineIn"]
    return round(pages * SPINE_PER_PAGE_CREAM_IN, 4)


def hardcover_geometry_is_anchored(pages: int) -> tuple[bool, str]:
    """
    Ciltli geometri, KDP tablosunun okunduğu sayfa sayısında mı?

    Tablo 234 sayfa için okundu. Başka bir sayfa sayısında tablonun
    HİÇBİR satırı geçerli değildir: sırt da, karton da, tam kapak da
    değişir. Türetmek iki kez denendi ve iki kez yanlış çıktı — üçüncüsü
    denenmeyecek. Sayfa sayısı değişirse hesaplayıcı yeniden çalışır.
    """
    want = HARDCOVER_KDP["pages"]
    if pages != want:
        return False, (
            f"ciltli geometri KDP hesaplayıcısından {want} sayfa için "
            f"okundu, şimdi {pages} sayfa var — tablonun hiçbir satırı "
            "artık geçerli değil. KDP Cover Calculator'ı yeniden "
            "çalıştırın ve HARDCOVER_KDP tablosunu güncelleyin. "
            "TÜRETMEYİN: iki türetme denendi, ikisi de yanlıştı.")
    return True, ""


# Geriye dönük ad — eski çağrı yerleri için.
hardcover_spine_is_anchored = hardcover_geometry_is_anchored


def panel_size_in(binding: str, trim_w: float, trim_h: float) -> tuple[float, float]:
    """
    Bir kapak PANELİNİN (ön/arka) ölçüsü.

    ⚠ CİLTLİDE PANEL TRIM DEĞİL KARTONDUR. Karton kitap bloğundan taşar
    ("square") ve 6×9 bir kitapta 6,197 × 9,236'dır. Faz 7d bunu kaçırdı:
    sırtı ve sarımı doğru aldı ama paneli 6×9 varsaydı ve kapak 0,393 inç
    dar, 0,235 inç kısa çıktı. KDP reddetti.
    """
    if binding == "hardcover":
        return hardcover_board_in()
    return trim_w, trim_h


def full_cover_in(pages: int, trim_w: float, trim_h: float,
                  binding: str = "paperback") -> tuple[float, float]:
    """
    Taşma/sarım dâhil tam kapak ölçüsü (genişlik, yükseklik).

    CİLTSİZ — TÜRETİLİR (KDP formülü yayımlar):
        2×trim + sırt + iki yanda 0,125" taşma

    CİLTLİ — TÜRETİLMEZ, TABLODAN OKUNUR:
        KDP hesaplayıcısının verdiği "Full Cover" satırı doğrudan kullanılır.
        Türetme iki kez denendi ve iki kez yanlış çıktı (bkz. modül başlığı).
        Tutarlılık için tablonun kendi iç formülü de doğrulanır:
            2×(front + wrap) + spine  ve  front_h + 2×wrap
    """
    if binding == "hardcover":
        w, h = HARDCOVER_KDP["fullCoverIn"]
        return float(w), float(h)
    spine = spine_width_in(pages, binding)
    w = 2 * trim_w + spine + 2 * BLEED_IN
    h = trim_h + 2 * BLEED_IN
    return round(w, 4), round(h, 4)


def hardcover_table_is_consistent() -> tuple[bool, str]:
    """
    KDP tablosu kendi içinde tutuyor mu?

    Tabloyu elle kopyalarken bir hane yanlış yazılırsa kapak sessizce
    yanlış üretilir. Bu denetim, tablonun kendi satırlarını birbirine
    karşı sınar — kopyalama hatası burada patlar.
    """
    k = HARDCOVER_KDP
    fw, fh = k["fullCoverIn"]
    bw, bh = k["frontCoverIn"]
    w = 2 * (bw + k["wrapIn"]) + k["spineIn"]
    h = bh + 2 * k["wrapIn"]
    if abs(w - fw) > 0.002:
        return False, (f"tablo tutmuyor: 2×({bw}+{k['wrapIn']})+{k['spineIn']}"
                       f" = {w:.3f} ≠ Full Cover {fw}")
    if abs(h - fh) > 0.002:
        return False, (f"tablo tutmuyor: {bh}+2×{k['wrapIn']} = {h:.3f} "
                       f"≠ Full Cover {fh}")
    return True, ""


# =============================================================================
# 3. KAPAK PROMPTLARI
# =============================================================================
# Her kayıt bir ÜRETİM ŞARTNAMESİDİR, bir fikir değil: hangi oran, hangi
# kompozisyon, metin nereye gelecek, hangi test geçilecek.

def cover_records(pages: int, trim_w: float, trim_h: float) -> list[dict]:
    pb_w, pb_h = full_cover_in(pages, trim_w, trim_h, "paperback")
    hc_w, hc_h = full_cover_in(pages, trim_w, trim_h, "hardcover")
    pb_spine = spine_width_in(pages, "paperback")
    hc_spine = spine_width_in(pages, "hardcover")

    front_only = (
        f"front cover only, portrait {trim_w}×{trim_h} inches. "
        "Composition: one hero scene that says 'stories from the whole world' "
        "without naming a single culture — a child-scaled figure looking out "
        "over a horizon where several distinct landscapes meet (northern ice, "
        "desert river, forest, island sea), with a few unmistakable mythic "
        "silhouettes at readable scale in the middle distance: a feathered "
        "serpent, a thunder-hammer, a great fish, a firebird. "
        "Keep the upper third visually calm — that band carries the title. "
        "Keep the lower right corner calm — that corner carries the age range."
    )

    return [
        {
            "id": "cover-paperback-front",
            "family": "cover",
            "target": "KDP paperback · front cover",
            "aspect": f"{trim_w}:{trim_h} (portrait)",
            "sizeIn": [trim_w, trim_h],
            "renderPx": [1800, 2700],
            "typography": "post",
            "textZones": [
                "top third — title (post-processed)",
                "under title — subtitle (post-processed)",
                "lower right corner — 'Ages 8–12' badge (post-processed)",
            ],
            "purpose": "Ana satış görseli. 160 piksel testini bu geçmek zorunda.",
            "subject": front_only,
            "checks": ["160px", "thumbnail-silhouette", "age-badge-corner"],
        },
        {
            "id": "cover-paperback-wrap",
            "family": "cover",
            "target": f"KDP paperback · full wrap (bleed dahil {pb_w}×{pb_h} in)",
            "aspect": f"{pb_w}:{pb_h} (landscape wrap)",
            "sizeIn": [pb_w, pb_h],
            "renderPx": [3852, 2775],
            "typography": "post",
            "textZones": [
                f"spine ({pb_spine}\" wide) — title + author, post-processed",
                "back cover left two thirds — blurb, post-processed",
                "back cover lower right — ISBN/barcode clear zone, 2×1.2 in, "
                "must stay empty of detail",
            ],
            "purpose": "Arka kapak + sırt + ön kapak tek dosyada.",
            "subject": (
                f"a single continuous wrap-around cover illustration, "
                f"landscape {pb_w}×{pb_h} inches. The same world-horizon scene "
                "continues across the back: on the back cover the landscape "
                "opens into calm sky and empty ground so a paragraph of text "
                "can sit on it. Keep a vertical band "
                f"{pb_spine} inches wide dead centre almost empty — that is the "
                "spine and any detail there will be lost in the fold. "
                "Keep the bottom right of the back cover flat and light for the "
                "barcode. Do not mirror the front composition on the back."
            ),
            "checks": ["spine-safe", "barcode-clear-zone", "no-detail-in-fold"],
        },
        {
            "id": "cover-hardcover-wrap",
            "family": "cover",
            "target": f"KDP hardcover · case laminate wrap ({hc_w}×{hc_h} in)",
            "aspect": f"{hc_w}:{hc_h} (landscape wrap)",
            "sizeIn": [hc_w, hc_h],
            "renderPx": [4116, 3075],
            "typography": "post",
            "textZones": [
                f"spine ({hc_spine}\" wide) — title + author, post-processed",
                "back cover — blurb, post-processed",
                f"outer {HARDCOVER_WRAP_IN}\" on every edge — WRAP, folds around "
                "the board and is not seen; no subject may sit there",
                f"{HARDCOVER_HINGE_IN}\" either side of the spine — HINGE, "
                "creases in binding",
            ],
            "purpose": "Ciltli sarım. Ciltsizden AYRI dosyadır — sarım ve "
                       "menteşe payları ciltsizde yoktur.",
            "subject": (
                f"the same wrap-around world-horizon scene, landscape "
                f"{hc_w}×{hc_h} inches, but composed with a wider safety "
                f"margin: every important element must sit at least "
                f"{HARDCOVER_WRAP_IN + HARDCOVER_HINGE_IN} inches inside the "
                "outer edge, because the outer band folds around the board and "
                "the band beside the spine creases into the hinge. "
                "Extend background colour and sky all the way to the edge so "
                "the fold shows no white."
            ),
            "checks": ["wrap-safe", "hinge-safe", "spine-safe"],
        },
        {
            "id": "cover-front-variant-figures",
            "family": "cover",
            "target": "KDP paperback · front cover — variant A",
            "aspect": f"{trim_w}:{trim_h} (portrait)",
            "sizeIn": [trim_w, trim_h],
            "renderPx": [1800, 2700],
            "typography": "post",
            "textZones": ["top third — title", "lower right — age badge"],
            "purpose": "Karakter ağırlıklı alternatif. Rakip rafta figürlü "
                       "kapaklar daha iyi çalışıyor; ölçülecek.",
            "subject": (
                "front cover only, portrait. Composition: a loose ring of six "
                "to eight mythic figures from clearly different traditions, "
                "drawn at the same scale and with the same warmth so no "
                "tradition outranks another — a trickster spider, a sun-catcher "
                "with a rope, a thunder god with a hammer, a feathered serpent, "
                "a woman rising from dark water, a boy with wax wings. "
                "They face outward around a calm centre. "
                "Leave the top third quiet for the title."
            ),
            "checks": ["160px", "no-culture-outranks-another", "age-badge-corner"],
        },
        {
            "id": "cover-front-variant-object",
            "family": "cover",
            "target": "KDP paperback · front cover — variant B",
            "aspect": f"{trim_w}:{trim_h} (portrait)",
            "sizeIn": [trim_w, trim_h],
            "renderPx": [1800, 2700],
            "typography": "post",
            "textZones": ["upper third — title", "lower right — age badge"],
            "purpose": "Tek-nesne alternatifi: küçük resimde en güçlü siluet.",
            "subject": (
                "front cover only, portrait. Composition: one enormous open "
                "book lying open, and out of its pages a whole world rises — "
                "mountains, an ocean with a great fish, a stepped pyramid, a "
                "longship, a torii gate, a baobab — small enough to read as "
                "one shape at thumbnail size. A child sits on the lower edge "
                "of the book looking up into it. "
                "The silhouette of book-plus-rising-world must be legible as a "
                "single mark at one inch tall."
            ),
            "checks": ["160px", "single-silhouette", "age-badge-corner"],
        },
        {
            "id": "cover-back-panel",
            "family": "cover",
            "target": "KDP · back cover panel (wrap içinde)",
            "aspect": f"{trim_w}:{trim_h} (portrait)",
            "sizeIn": [trim_w, trim_h],
            "renderPx": [1800, 2700],
            "typography": "post",
            "textZones": [
                "upper two thirds — blurb + '45 stories · 22 cultures' line",
                "lower right 2×1.2 in — barcode clear zone, keep flat",
            ],
            "purpose": "Sarım kullanılmazsa ayrı arka kapak paneli.",
            "subject": (
                "back cover panel, portrait. Composition: mostly calm sky and "
                "open ground in the cover's palette, with a thin band of small "
                "mythic silhouettes along the very bottom like a horizon "
                "frieze. The upper two thirds must be quiet enough that a "
                "paragraph of text sits on it and stays readable. "
                "Bottom right must be flat and pale for the barcode."
            ),
            "checks": ["blurb-legibility", "barcode-clear-zone"],
        },
        {
            "id": "cover-thumbnail-test",
            "family": "cover",
            "target": "İç test — 160 piksel okunabilirlik",
            "aspect": f"{trim_w}:{trim_h} (portrait)",
            "sizeIn": [trim_w, trim_h],
            "renderPx": [160, 240],
            "typography": "post",
            "textZones": ["title band", "age badge"],
            "purpose": (
                "ÜRETİM VARLIĞI DEĞİL, TESTTİR. Yol haritası § 18 kapağın "
                "160 pikselde okunmasını şart koşar: 'World' ve '22 Cultures' "
                "küçük resimde okunabilmeli. Bu kayıt, seçilen kapağın "
                "küçültülüp sınanacağı adımı görünür tutar."
            ),
            "subject": (
                "NOT A GENERATION PROMPT. Take the chosen front cover with "
                "post-processed typography applied, downscale it to 160 pixels "
                "wide, and check by eye: is the word 'World' readable? is "
                "'22 Cultures' readable? is the age badge readable? does the "
                "hero shape still read as one thing? "
                "If any answer is no, the cover fails and is reworked."
            ),
            "checks": ["160px", "world-readable", "22-cultures-readable"],
        },
    ]


# =============================================================================
# 4. A+ İÇERİK PROMPTLARI
# =============================================================================
# Modül ölçüleri Amazon'un STANDART A+ modüllerinindir. Modülü uydurmak
# (talimat § 27) yerine gerçek modül adı ve gerçek piksel ölçüsü verilir.

def aplus_records() -> list[dict]:
    def rec(i, mid, module, px, purpose, subject, zones, checks):
        return {
            "id": f"aplus-{i:03d}-{mid}",
            "family": "aplus",
            "target": f"Amazon A+ · {module}",
            "module": module,
            "renderPx": list(px),
            "aspect": f"{px[0]}:{px[1]}",
            "typography": "post",
            "textZones": zones,
            "purpose": purpose,
            "subject": subject,
            "checks": checks,
        }

    return [
        rec(1, "hero", "Standard Image Header with Text", (970, 600),
            "Ürün tanıtımı — modülün ilk ekranı.",
            "a wide banner illustration: the same world-horizon idea as the "
            "cover, stretched into a panorama — northern ice on the far left "
            "running through desert river, forest and island sea to the far "
            "right, with small mythic silhouettes spaced along it. "
            "The left 40 percent must stay very calm and light: a headline "
            "sits there. Nothing important in the outer 30 pixels.",
            ["left 40% — headline and subhead, post-processed"],
            ["text-safe-left", "no-generated-text"]),

        rec(2, "cultures", "Standard Image & Light Text Overlay", (970, 300),
            "22 kültüre genel bakış — 'kapsam' vaadini tek görselde kurar.",
            "a long horizontal frieze of twenty-two small emblems in one "
            "consistent flat-colour style, evenly spaced on a plain warm "
            "background: sankofa bird, eye of horus, sun disc, feathered "
            "serpent, dragon, kantele, greek helmet, outrigger canoe, conch, "
            "kayak, triquetra, torii, hourglass drum, maya glyph, lamassu, "
            "fish hook, hammer, winged lion, wolf head, long dragon, bell, "
            "shield and spear. Equal visual weight for every emblem — none "
            "larger or more central than another. Plenty of clear space above "
            "and below the row for a text overlay.",
            ["full width — light text overlay, post-processed"],
            ["equal-weight-cultures", "text-safe-overlay"]),

        rec(3, "map", "Standard Single Image & Sidebar", (300, 400),
            "Dünya haritası kavramı — ebeveynin 'eğitici' algısı.",
            "a simplified, friendly world map in the cover palette with "
            "twenty-two small glowing dots marking homelands, no country "
            "borders, no place names. Portrait crop centred on the Atlantic so "
            "the Americas, Africa and Europe all read. Warm paper background.",
            ["none in image — caption sits in the module's sidebar"],
            ["no-generated-text", "no-labels", "matches-locked-culture-list"]),

        rec(4, "value", "Standard Four Image & Text", (220, 220),
            "'45 hikâye / 22 kültür' eğitsel değeri — dört kareden biri.",
            "a small square icon-illustration: a stack of open books with a "
            "large friendly numeral shape suggested by the composition (not "
            "drawn as a character), on a flat warm background with wide "
            "margins. Simple enough to read at 220 pixels.",
            ["caption below image, post-processed — the numbers 45 and 22 "
             "are TEXT, never generated"],
            ["220px-legible", "no-generated-numerals"]),

        rec(5, "linework", "Standard Four Image & Text", (220, 220),
            "Siyah-beyaz illüstrasyon sistemi — iç bloğun dürüst tanıtımı.",
            "a small square showing a single black-and-white pen-and-ink "
            "vignette in the book's actual interior style, floating on a flat "
            "warm background with wide margins — this one square deliberately "
            "uses the interior line language so the buyer sees what is really "
            "inside the book.",
            ["caption below image, post-processed"],
            ["matches-interior-style", "220px-legible"]),

        rec(6, "reader", "Standard Four Image & Text", (220, 220),
            "Genç okur konumlandırması — 8–12 yaş.",
            "a small square: a child of about ten reading, absorbed, sitting "
            "with knees up, one small mythic silhouette drifting out of the "
            "book above their head. Warm flat background, wide margins. "
            "Ambiguous enough in dress and features that any reader can be the "
            "child in it.",
            ["caption below image, post-processed"],
            ["age-positioning", "inclusive-figure"]),

        rec(7, "backmatter", "Standard Four Image & Text", (220, 220),
            "Telaffuz · sözlük · kültürel not — öğretmen/ebeveyn gerekçesi.",
            "a small square: an open book showing two facing pages laid out as "
            "a reference spread — a column of short entries on the left and a "
            "small emblem on the right — rendered as shape and rhythm only, "
            "with NO readable words. Flat warm background, wide margins.",
            ["caption below image, post-processed"],
            ["no-generated-text", "reads-as-reference-page"]),

        rec(8, "interior", "Standard Three Images & Text", (300, 300),
            "Kitap içi önizleme — 'Look Inside' beklentisini dürüst kurar.",
            "a three-quarter view of the physical paperback lying open, showing "
            "a story opening: illustration across the upper half of the page "
            "and text below it. The page content is suggested, not readable. "
            "Soft shadow, plain warm background, generous margin.",
            ["caption below image, post-processed"],
            ["honest-interior-representation", "no-generated-text"]),

        rec(9, "parent", "Standard Single Left Image", (300, 300),
            "Ebeveyn/öğretmen değer önerisi — güven tarafı.",
            "a warm domestic scene reduced to essentials: an adult and a child "
            "sharing the open book, seen from the side, both looking at the "
            "same page. No faces in detail. Flat background in the cover "
            "palette, wide clear margin on the right for text.",
            ["right side — value proposition text, post-processed"],
            ["buyer-trust", "text-safe-right"]),

        rec(10, "series", "Standard Company Logo", (600, 180),
            "Seri kimliği — 'The Great Book of…' rafı.",
            "a horizontal series lockup ILLUSTRATION ONLY: a simple emblem — "
            "an open book with a small globe rising from it — centred on a "
            "flat background, with a wide empty band to its right. "
            "The series name is TEXT and is added afterwards; do not draw any "
            "letterforms.",
            ["right band — series wordmark, post-processed"],
            ["no-generated-text", "logo-safe"]),
    ]


def all_records(pages: int, trim_w: float, trim_h: float) -> list[dict]:
    out = []
    for r in cover_records(pages, trim_w, trim_h):
        r["style"] = COVER_STYLE
        r["negative"] = COVER_NEGATIVE
        out.append(r)
    for r in aplus_records():
        r["style"] = APLUS_STYLE
        r["negative"] = APLUS_NEGATIVE
        out.append(r)
    return out


def compose(rec: dict) -> str:
    """Konu + üslup gövdesi + yaş kısıtı — iç promptlarla aynı disiplin."""
    return (f"{rec['subject']} {rec['style']}. "
            "Suitable for readers aged 8 to 12: the image may be dramatic, "
            "it may not be frightening.")
