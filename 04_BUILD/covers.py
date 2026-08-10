#!/usr/bin/env python3
"""
KAPAK ÜRETİMİ — CİLTSİZ SARIM · CİLTLİ SARIM · KINDLE KAPAĞI
================================================================================
    python3 04_BUILD/covers.py                 hepsini üret + doğrula
    python3 04_BUILD/covers.py --edition paperback
    python3 04_BUILD/covers.py --check         kayıtlı rapor bayat mı

    07_ASSETS/raw/re-generated/cover-*.png   YETKİLİ SANAT · SALT OKUNUR
              ↓
    08_OUTPUT/<edition>/cover.pdf    baskıya hazır · gömülü font · 300 dpi
    08_OUTPUT/kindle/cover.jpg       ≥2560 px yükseklik
    06_REPORTS/tracked/cover-build.json

--------------------------------------------------------------------------------
SANAT KATMANINA DOKUNULMAZ — VE BU BİR KURAL DEĞİL, BİR TARİH
--------------------------------------------------------------------------------
Faz 6 teslimatındaki kapak sanatına iki şey BASILMIŞTI:

  ① YANLIŞ BAŞLIK — "STORIES from the WHOLE WORLD". Kitabın adı
     **The Great Book of World Myths**.
  ② UYDURULMUŞ ISBN BARKODU — projeye ait olmayan bir numara.

Faz 7 bunları **algoritmayla siliyordu**: harf maskesi → azalan yarıçaplı
difüzyon → çok ölçekli gök modeli → pus. Teknik olarak çalışıyordu, harfler
gidiyordu — ama **sanata zarar veriyordu**. Bir üreticinin yaptığı resmi
başka bir algoritmayla onarmak, her koşuda biraz daha bozar.

Kurucu doğru kararı verdi: **bütün kapak sanatı metinsiz yeniden üretildi.**
Yetkili masterlar `07_ASSETS/raw/re-generated/` altındadır ve o dizin
SALT OKUNURDUR.

Kural artık hattın kendisindedir:

    SANAT KATMANINA HİÇBİR ŞEY YAZILMAZ VE SANAT KATMANINDAN HİÇBİR ŞEY
    SİLİNMEZ. Tipografi AYRI bir katmandır ve CLI ile basılır.

Okunabilirlik, sanatı boyayarak değil, metnin kendi zeminiyle sağlanır:
sırt düz renk bandı, arka kapak paneli, yaş rozeti levhası. Hepsinin
kontrastı WCAG ile ÖLÇÜLÜR (`measure_contrast`) ve kapıya bağlıdır.

`04_BUILD/cover_artwork.py` üç şeyi denetler: masterların sha256'sı,
bu dosyanın hangi dizinden okuduğu, ve yıkıcı fonksiyonların geri
gelmediği.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb
import coverspec as cs
import editions as ed_mod

OUT_JSON = os.path.join(mb.REPORTS_TRACKED, "cover-build.json")
# ⚠ YETKİLİ SANAT MASTERLARI. Eski (metinli) sanat 07_ASSETS/raw altındaydı
# ve artık KULLANILMIYOR. Kapak hattı yalnızca buradan okur;
# `cover_artwork.py` bunu bir kapı olarak denetler.
ART_DIR = os.path.join(mb.ASSETS, "raw", "re-generated")
DPI = 300

FONT_DIRS = ["/usr/share/fonts/truetype/lato",
             "/usr/share/fonts/truetype/liberation",
             os.path.join(mb.ASSETS, "fonts")]
# Kapak başlığı KÜÇÜK RESİMDE okunmak zorunda (yol haritası § 18 · 160 px
# testi). Ağır bir hümanist sans, Times metriğinden belirgin biçimde daha
# iyi okunur. İkisi de gömülebilir ve `ğ` taşır (yazar adı: Emre Doğan).
FONT_FILES = {
    "display": "Lato-Black.ttf",
    "bold": "Lato-Bold.ttf",
    "text": "Lato-Regular.ttf",
    "italic": "Lato-Italic.ttf",
}
F_DISPLAY, F_BOLD, F_TEXT, F_ITALIC = "CovDisplay", "CovBold", "CovText", "CovItalic"

# Okura giden kesin dizeler. TEK KAYNAK: project_config.json § founder.
# ⚠ BURAYA AD YAZILMAZ. Faz 6'da yazar adı bu satırda GÖMÜLÜYDÜ ve aynı ad
# epub.py ile handoff.py'de ayrıca gömülüydü; metadata.py ise hâlâ yer tutucu
# basıyordu. Kapak "Emre Doğan", metadata "[PENDING]" diyordu ve hiçbir kapı
# bunu görmedi. validate_structure artık bu dosyaları gömülü ad için tarar.
AUTHOR = mb.AUTHOR

BACK_COPY = [
    "Most books of myths for young readers are Greek books.",
    "This one is not.",
    "",
    "Forty-five stories from twenty-two traditions — Korean, Inuit, "
    "Māori, Hawaiian, Yoruba, Akan, Persian, Turkic, Greek, Norse, Irish, "
    "Finnish, Egyptian, Mesopotamian, Japanese, Chinese, Vietnamese, Hindu, "
    "Maya, Aztec, Andean and Zulu — in one volume, at one standard, in one "
    "voice.",
    "",
    "These are stories to read, not pictures to flip through. Every story "
    "runs about a thousand words: long enough to fall into, short enough to "
    "finish before bed. A black-and-white illustration opens each one.",
    "",
    "At the back: how to say every name, who's who among the gods, and the "
    "real sources behind every retelling.",
    "",
    "Where the tellers disagree, this book picks one version and says so. "
    "Nothing has been made gentler than it is.",
]


# =============================================================================
# FONT
# =============================================================================

def register_fonts() -> dict:
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    resolved = {}
    for key, fname in FONT_FILES.items():
        for d in FONT_DIRS:
            p = os.path.join(d, fname)
            if os.path.exists(p):
                resolved[key] = p
                break
        else:
            raise FileNotFoundError(
                f"kapak fontu bulunamadı: {fname} · aranan {FONT_DIRS}\n"
                "Debian/Ubuntu: sudo apt-get install fonts-lato")
    pdfmetrics.registerFont(TTFont(F_DISPLAY, resolved["display"]))
    pdfmetrics.registerFont(TTFont(F_BOLD, resolved["bold"]))
    pdfmetrics.registerFont(TTFont(F_TEXT, resolved["text"]))
    pdfmetrics.registerFont(TTFont(F_ITALIC, resolved["italic"]))
    return resolved


# =============================================================================
# GEOMETRİ
# =============================================================================

def geometry(binding: str, pages: int) -> dict:
    ed = ed_mod.get("paperback")           # trim iki sürümde de aynı
    tw, th = ed.trim_w_in, ed.trim_h_in
    spine = cs.spine_width_in(pages, binding)
    fw, fh = cs.full_cover_in(pages, tw, th, binding)
    if binding == "hardcover":
        edge = cs.HARDCOVER_WRAP_IN        # katlanan pay
        safe = cs.HARDCOVER_SAFE_IN        # yazı/görsel kenardan bu kadar içeride
        hinge = cs.HARDCOVER_HINGE_IN
    else:
        edge = cs.BLEED_IN
        safe = 0.25                        # KDP ciltsiz: canlı içerik kenardan 0,25"
        hinge = 0.0625                     # sırt yanı payı
    back_x0 = edge
    spine_x0 = edge + tw
    front_x0 = edge + tw + spine
    return {
        "binding": binding, "pages": pages,
        "trimIn": [tw, th], "spineIn": spine,
        "fullIn": [fw, fh],
        "fullPx": [round(fw * DPI), round(fh * DPI)],
        "edgeIn": edge, "safeIn": safe, "hingeIn": hinge,
        "backX0In": back_x0, "spineX0In": spine_x0, "frontX0In": front_x0,
        "spineDerived": binding == "hardcover" and cs.HARDCOVER_SPINE_IS_DERIVED,
    }


# =============================================================================
# ZEMİN SANATI
# =============================================================================

def base_art(path: str, w_px: int, h_px: int):
    """
    Ham sanatı tuvali TAM KAPLAYACAK şekilde ölçekler ve ortalar.

    ESNETME YOK: oran korunur, taşan kısım kırpılır. Kapakta dolgu (letterbox)
    kabul edilemez — beyaz bant baskıya gider. Kırpma bilinçlidir ve ne kadar
    kırpıldığı raporlanır.
    """
    from PIL import Image
    with Image.open(path) as im:
        im = im.convert("RGB")
        sw, sh = im.size
        scale = max(w_px / sw, h_px / sh)
        nw, nh = max(1, round(sw * scale)), max(1, round(sh * scale))
        r = im.resize((nw, nh), Image.LANCZOS)
        left = (nw - w_px) // 2
        top = (nh - h_px) // 2
        out = r.crop((left, top, left + w_px, top + h_px))
    return out, {"sourcePx": [sw, sh], "scale": round(scale, 4),
                 "croppedPx": [nw - w_px, nh - h_px],
                 "croppedPct": [round(100 * (nw - w_px) / nw, 2),
                                round(100 * (nh - h_px) / nh, 2)]}


# =============================================================================
# KONTRAST ÖLÇÜMÜ — "OKUNUYOR MU" BİR FİKİR DEĞİL, BİR SAYIDIR
# =============================================================================
# Talimat § 7: yazar adı "sanatın içinde kaybolmamalı" ve "yeterli kontrasta
# sahip olmalı". Bu, gözle verilecek bir karar DEĞİLDİR: eski kapakta sırt
# yazısı gözle "biraz zor" görünüyordu ve ölçülünce ormanın üstünde
# neredeyse görünmez olduğu ortaya çıktı.
#
# Burada WCAG bağıl parlaklık ve kontrast oranı kullanılır. Ölçüm, metnin
# GERÇEK zemininden yapılır:
#   · doğrudan sanatın üstündeki yazı → altındaki SANAT pikselleri
#   · opak levha üstündeki yazı       → LEVHANIN rengi
# İkisini karıştırmak yanıltır: yaş rozetinin altındaki sanat 1,14 ölçtü
# ama rozet turuncu bir levhanın üstündedir ve gerçek kontrastı 3,78'dir.
#
# En kötü durum önemlidir: metnin %10'u koyu bir bulutun üstüne düşerse o
# kısım kaybolur. Bu yüzden ORTALAMA değil **p10** (onuncu yüzdelik)
# kapıya bağlanır.

_WCAG_MIN = 4.5          # kapı: bunun altı HATA
_WCAG_GOOD = 7.0         # bunun altı UYARI (AAA eşiği)


def _rel_lum(rgb01) -> float:
    def f(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (f(max(0.0, min(1.0, v))) for v in rgb01)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _contrast(l1: float, l2: float) -> float:
    a, b = max(l1, l2), min(l1, l2)
    return (a + 0.05) / (b + 0.05)


def measure_contrast(art, pen, Wpt, Hpt) -> dict:
    """Her yazı kutusunun kendi zeminine karşı kontrastı."""
    sx, sy = art.width / Wpt, art.height / Hpt
    out = {}
    for name, x0, y0, x1, y1 in pen.boxes:
        info = pen.grounds.get(name)
        if not info:
            continue
        ink = _rel_lum(info["ink"])
        if info["plate"]:
            ratio = _contrast(ink, _rel_lum(info["plate"]))
            out[name] = {"p10": round(ratio, 2), "min": round(ratio, 2),
                         "mean": round(ratio, 2), "ground": "plate"}
            continue
        px = (max(0, int(x0 * sx)), max(0, int((Hpt - y1) * sy)),
              min(art.width, int(x1 * sx)), min(art.height, int((Hpt - y0) * sy)))
        if px[2] <= px[0] or px[3] <= px[1]:
            continue
        from PIL import Image
        reg = art.crop(px)
        reg = reg.resize((max(1, reg.width // 4), max(1, reg.height // 4)),
                         Image.BOX)
        rs = sorted(_contrast(ink, _rel_lum([v / 255 for v in p]))
                    for p in reg.getdata())
        out[name] = {"p10": round(rs[int(len(rs) * 0.10)], 2),
                     "min": round(rs[0], 2),
                     "mean": round(sum(rs) / len(rs), 2),
                     "ground": "artwork"}
    return out


# =============================================================================
# SANAT KATMANINA DOKUNULMAZ
# =============================================================================
# ⚠ BURADA ESKİDEN 130 SATIRLIK BİR METİN SİLME HATTI VARDI ve kaldırıldı.
#
# Ham sanata basılmış yanlış bir başlık ("STORIES from the WHOLE WORLD") ve
# uydurulmuş bir barkod vardı. Hat onları harf maskesi + azalan yarıçaplı
# difüzyon + çok ölçekli gök modeliyle SİLİYORDU. Teknik olarak çalışıyordu:
# harfler gidiyordu. Ama bir üreticinin yaptığı resmi başka bir algoritmayla
# onarmak SANATA ZARAR VERİR ve her koşuda biraz daha bozar.
#
# Kurucu doğru kararı verdi: bütün kapak sanatı **metinsiz yeniden üretildi**
# (07_ASSETS/raw/re-generated). Silinecek bir şey kalmadı.
#
# Kural, artık hattın kendisindedir:
#
#     SANAT KATMANINA HİÇBİR ŞEY YAZILMAZ, SANAT KATMANINDAN HİÇBİR ŞEY
#     SİLİNMEZ. Tipografi AYRI bir katmandır ve CLI ile basılır.
#
# `cover_artwork.py` bu fonksiyonların ADININ BİLE geri gelmediğini denetler
# ve masterların sha256'sını her koşuda karşılaştırır.

def wrap_text(text, font, size, maxw):
    from reportlab.pdfbase.pdfmetrics import stringWidth
    out, cur = [], ""
    for word in text.split():
        t = word if not cur else cur + " " + word
        if stringWidth(t, font, size) <= maxw:
            cur = t
        else:
            if cur:
                out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def fit_title(c, words, font, maxw, start_size, min_size=18):
    """Başlığı kutuya SIĞDIR — taşarsa punto düşür, asla kırpma."""
    from reportlab.pdfbase.pdfmetrics import stringWidth
    size = start_size
    while size > min_size:
        if all(stringWidth(w, font, size) <= maxw for w in words):
            return size
        size -= 1
    return min_size


# =============================================================================
# ÖLÇTÜĞÜNÜ ÇİZEN KALEM
# =============================================================================
# ⚠ FAZ 6'NIN EN PAHALI KUSURU BURADAYDI VE SEBEBİ TAM OLARAK ŞUDUR:
# reportlab'da FONT BİR DURUMDUR — tıpkı alfa gibi (bkz. § ① notu).
#
# Yaş rozetinin genişliği `stringWidth(badge, F_BOLD, 14)` ile ölçüldü.
# Ölçü ile çizim arasına yazar adı için `setFont(F_BOLD, 27)` girdi ve bir
# daha 14'e DÖNÜLMEDİ. `drawString` rozeti 27 puntoyla bastı:
#
#     ölçülen genişlik  71,5 pt        çizilen genişlik  137,9 pt
#     → rozet zemininden           66,4 pt taştı
#     → güvenli alandan            54,4 pt taştı
#     → CİLTSİZDE KÂĞIDIN KENARINDAN 27,4 pt (0,38") taştı
#
# Yani "AGES 8–12" baskıda kesilecekti ve rozet dışına düşen "–12"
# ciltlide çıplak gözle görülüyordu. Güvenli alan kapısı bunu GÖREMEDİ,
# çünkü kapı `boxes` listesindeki PLANLANAN kutuyu ölçüyordu — ÇİZİLENİ değil.
# Ölü kural klasiği: kapı vardı, yeşildi ve yanlış şeye bakıyordu.
#
# Bu sınıf ikisini ayrılamaz kılar. Ölçüm ve çizim aynı çağrının içindedir,
# aynı fontu ve aynı puntoyu kullanır, ve kutu GERÇEK yazı ölçülerinden
# (ascent/descent) hesaplanıp kaydedilir. Kapı artık kaydı denetler.

class Pen:
    def __init__(self, c):
        self.c = c
        self.boxes: list = []
        # Her çizimin ZEMİNİ: None = doğrudan sanatın üstünde,
        # (r,g,b) = opak bir levhanın üstünde. Kontrast ölçümü bunu bilmek
        # zorundadır — levhanın altındaki sanatı ölçmek YANILTICIDIR.
        self.grounds: dict = {}

    def width(self, s, font, size) -> float:
        from reportlab.pdfbase.pdfmetrics import stringWidth
        return stringWidth(s, font, size)

    def draw(self, name, x, y, s, font, size, fill,
             align="left", halo=None, halo_alpha=0.55, record=True,
             ground=None):
        from reportlab.pdfbase.pdfmetrics import stringWidth, getAscentDescent
        c = self.c
        c.setFillAlpha(1)
        c.setStrokeAlpha(1)
        c.setFont(font, size)                    # ÖLÇÜ VE ÇİZİM AYNI DURUMDA
        w = stringWidth(s, font, size)
        if align == "center":
            x -= w / 2
        elif align == "right":
            x -= w
        if halo is not None:
            c.setFillColorRGB(*halo)
            c.setFillAlpha(halo_alpha)
            o = max(0.6, size * 0.055)
            for dx, dy in ((o, -o), (-o, -o), (o, o), (-o, o),
                           (0, o * 1.5), (0, -o * 1.5), (o * 1.5, 0), (-o * 1.5, 0)):
                c.drawString(x + dx, y + dy, s)
            c.setFillAlpha(1)
        c.setFillColorRGB(*fill)
        c.drawString(x, y, s)
        asc, desc = getAscentDescent(font, size)
        box = [name, x, y + desc, x + w, y + asc]
        if record:
            self.boxes.append(box)
            self.grounds[name] = {"ink": list(fill), "plate": ground,
                                  "sizePt": size}
        return box

def front_layout(g, tw, th, edge, safe, front_x, title_words):
    """
    Ön kapak tipografisinin YERLERİNİ çizmeden önce hesaplar.

    Neden ayrı: üretilmiş yazıyı onaran bandın ne kadar aşağı ineceği,
    BİZİM bastığımız bloğun nerede bittiğine bağlıdır. Faz 6 bunu tahmin
    ediyordu ve ciltlide (güvenli marj 0,635") blok bandın dışına, resmin
    üstüne düşüyordu. Artık ölçülüp geri veriliyor.
    """
    inner = (tw - 2 * safe - 0.35) * 72
    size = fit_title(None, title_words, F_DISPLAY, inner, 72)
    safe_top = (edge + th - safe) * 72
    cx = front_x + tw * 72 / 2

    y = safe_top - size * 0.80
    lines = [("title", title_words[0], F_DISPLAY, size, y)]
    y -= size * 1.06
    lines.append(("title2", title_words[1], F_DISPLAY, size, y))

    # ⚠ SATIR ARALIĞI ORANDAN DEĞİL, TAŞIYICI YÜKSEKLİKTEN.
    # Faz 6 bu dersi başlık satırları için öğrenmişti ("OF" satırı bir alt
    # satırın üstüne çıkıyordu) ama BLOKLAR ARASINDA hâlâ sabit oran
    # kullanıyordu: başlıktan alt başlığa iniş `size × 0,50` idi. 57 puntoda
    # bu, başlığın alt kenarı ile alt başlığın üst kenarını 1,2 punto
    # ÜST ÜSTE bindiriyordu. Gözle görünmüyordu çünkü "WORLD MYTHS"te alt
    # uzantı yok — ama bir sonraki başlıkta olsaydı görünecekti.
    # Aşağıdaki iniş iki bloğun GERÇEK ascent/descent değerlerinden ve
    # açıkça yazılmış bir boşluktan hesaplanır.
    from reportlab.pdfbase.pdfmetrics import getAscentDescent

    def _drop(from_font, from_pt, to_font, to_pt, gap):
        _, d_from = getAscentDescent(from_font, from_pt)   # negatif
        a_to, _ = getAscentDescent(to_font, to_pt)
        return -d_from + a_to + gap

    sub = "45 Stories of Gods, Heroes, and Monsters from 22 Cultures"
    sub_pt = 15.5
    while len(wrap_text(sub, F_BOLD, sub_pt, inner)) > 1 and sub_pt > 10:
        sub_pt -= 0.5
    y -= _drop(F_DISPLAY, size, F_BOLD, sub_pt, size * 0.20)
    for ln in wrap_text(sub, F_BOLD, sub_pt, inner):
        lines.append(("subtitle", ln, F_BOLD, sub_pt, y))
        y -= sub_pt * 1.35
    y += sub_pt * 1.35
    y -= _drop(F_BOLD, sub_pt, F_ITALIC, 14, 5)
    lines.append(("byline", "Retold for Young Readers", F_ITALIC, 14, y))

    # ⚠ YAZAR ADI ARTIK ÜST BLOKTA.
    # Faz 6 adı ön kapağın ALTINA, resmin üstüne, %82 opak koyu bir "çip"in
    # içine basıyordu. Üç sorun birdendi: (a) çip bir arayüz öğesi gibi
    # duruyordu, (b) çocuğun gövdesinin tam üstüne düşüyordu, (c) rozetle
    # çakışma riski her sürümde elle ayarlanıyordu.
    # Onarılmış üst bant zaten temiz, düşük detaylı ve yüksek kontrastlıdır;
    # ad oraya basılınca ne zemin gerekir ne çip. Hiyerarşi de netleşir:
    # BAŞLIK > alt başlık > YAZAR. Rozet köşede kalır (yol haritası § 18).
    author_pt = max(17.0, round(size * 0.38, 1))
    y -= _drop(F_ITALIC, 14, F_BOLD, author_pt, 16)
    lines.append(("author", mb.AUTHOR, F_BOLD, author_pt, y))

    block_bottom = y - author_pt * 0.26
    return {"size": size, "inner": inner, "cx": cx, "safeTop": safe_top,
            "lines": lines, "blockBottomPt": block_bottom,
            "authorPt": author_pt}


def build_cover(binding: str, pages: int, cfg: dict, r: mb.Result) -> dict:
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfgen import canvas

    g = geometry(binding, pages)
    W_in, H_in = g["fullIn"]
    Wpt, Hpt = W_in * 72, H_in * 72

    src = os.path.join(ART_DIR,
                   "cover-paperback-wrap.png" if binding == "paperback"
                   else "cover-hardcover-wrap.png")
    rec: dict = {"edition": binding, "geometry": g,
                 "sourceArt": os.path.relpath(src, mb.ROOT),
                 "issues": []}
    if not os.path.exists(src):
        rec["issues"].append(f"kapak sanatı yok: {src}")
        r.fail(f"{binding}: kapak sanatı yok", src)
        return rec

    art, artinfo = base_art(src, g["fullPx"][0], g["fullPx"][1])
    rec["art"] = artinfo

    # =========================================================================
    # ⓪ ETKİN ÇÖZÜNÜRLÜK — ÖLÇÜLÜR, VARSAYILMAZ
    # =========================================================================
    # KDP baskı kapağı için 300 dpi ister. `base_art` ham sanatı tuvale
    # BÜYÜTEREK oturtur; büyütme çözünürlük ÜRETMEZ. Faz 6 çıktıyı 300 dpi
    # ETİKETLEDİ ama gerçek örnekleme oranını hiç ölçmedi:
    # ham sanat 1477×1065 px, hedef tuval 3852×2775 px → 2,6× büyütme →
    # ETKİN 115 dpi. Bu bir kapı boşluğuydu ve kurucunun kararına açılır.
    eff = round(DPI / max(1e-9, artinfo["scale"]), 1)
    rec["effectiveArtDpi"] = eff
    rec["artUpscaleFactor"] = artinfo["scale"]

    out_pdf = os.path.join(mb.ROOT, "08_OUTPUT", binding, "cover.pdf")
    os.makedirs(os.path.dirname(out_pdf), exist_ok=True)

    edge, safe = g["edgeIn"], g["safeIn"]
    tw, th = g["trimIn"]
    front_x = g["frontX0In"] * 72
    back_x = g["backX0In"] * 72
    spine_x = g["spineX0In"] * 72
    spine_w = g["spineIn"] * 72
    px_per_in = g["fullPx"][1] / H_in
    dark = (0.075, 0.115, 0.26)

    title_words = ["THE GREAT BOOK OF", "WORLD MYTHS"]
    lay = front_layout(g, tw, th, edge, safe, front_x, title_words)

    # =========================================================================
    # ① SANAT KATMANI — OLDUĞU GİBİ KULLANILIR
    # =========================================================================
    # Burada eskiden üretilmiş başlığı ONARAN ve üretilmiş barkodu SİLEN
    # iki çağrı vardı. İkisi de kaldırıldı: yeni sanat metinsiz üretildi,
    # silinecek bir şey yok ve silmeye çalışmak sanata zarar verir.
    #
    # Tipografi için gereken tek şey KONTRAST'tır ve o, sanatın üstünü
    # boyayarak değil, metnin kendi okunabilirlik zeminiyle sağlanır
    # (başlık halesi § ③, sırt bandı § ②, arka kapak paneli § ④).
    bcw_in, bch_in = cs.BARCODE_W_IN, cs.BARCODE_H_IN
    bcx_in = back_x / 72 + (tw - safe) - bcw_in - 0.15
    bcy_in = edge + cs.BARCODE_FROM_BOTTOM_IN
    rec["artworkUntouched"] = True

    # =========================================================================
    # TUVAL
    # =========================================================================
    c = canvas.Canvas(out_pdf, pagesize=(Wpt, Hpt),
                      initialFontName=F_TEXT, initialFontSize=12)
    c.setTitle(f"{cfg['title']} — {binding} cover")
    c.setAuthor(mb.AUTHOR)
    c.drawImage(ImageReader(art), 0, 0, width=Wpt, height=Hpt)
    pen = Pen(c)

    # =========================================================================
    # ② SIRT — DÜZ RENK, ÇÜNKÜ SANATIN ÜSTÜNDE OKUNMUYORDU
    # =========================================================================
    # Faz 6 sırt yazısını koyu lacivert olarak DOĞRUDAN sanatın üstüne
    # basıyordu. Sırt yukarıda açık gökten, aşağıda KOYU YEŞİL ormandan
    # geçiyor: başlığın son sözcüğü ("MYTHS") ve yazar adı ormanın üstünde
    # neredeyse görünmez oluyordu. Sırt, kitabın raftaki tek görünen
    # yüzüdür; okunmaması kabul edilemez.
    # Çözüm sektörün standardı: sırt düz renktir ve yazı beyazdır. Katlama
    # payı için renk her iki yana 0,06" taşırılır ve kenarı yumuşatılır —
    # sırt kayarsa beyaz bir çizgi değil, rengin devamı görünür.
    spine_ok = pages >= 100
    rec["spineText"] = spine_ok
    bleed_side = 0.06 * 72
    steps = 26
    for i in range(steps):
        t = i / (steps - 1)
        c.setFillColorRGB(*dark)
        c.setFillAlpha(1.0 if t == 0 else max(0.0, 1.0 - t) ** 1.7)
        ext = bleed_side * t
        c.rect(spine_x - ext, 0, spine_w + 2 * ext, Hpt, stroke=0, fill=1)
    c.setFillAlpha(1)

    if spine_ok:
        st = "THE GREAT BOOK OF WORLD MYTHS"
        avail = (th - 2 * safe) * 72
        ratio = 0.70
        ssize = min(21, int(spine_w * 0.42))
        while ssize > 8:
            need = (pen.width(st, F_DISPLAY, ssize)
                    + pen.width(mb.AUTHOR, F_BOLD, ssize * ratio)
                    + 0.45 * 72)
            if need <= avail:
                break
            ssize -= 1
        asz = ssize * ratio
        w_t = pen.width(st, F_DISPLAY, ssize)
        w_a = pen.width(mb.AUTHOR, F_BOLD, asz)
        cy = edge * 72 + (th * 72) / 2
        c.saveState()
        c.translate(spine_x + spine_w / 2, cy)
        c.rotate(-90)
        c.setFillColorRGB(1, 1, 1)
        c.setFont(F_DISPLAY, ssize)
        c.drawString(-w_t / 2 - 0.22 * 72, -ssize * 0.34, st)
        c.setFont(F_BOLD, asz)
        c.drawString(avail / 2 - w_a, -ssize * 0.34, mb.AUTHOR)
        c.restoreState()
        rec["spineFontPt"] = ssize
        rec["spineNeedPt"] = round(w_t + w_a + 0.45 * 72, 1)
        rec["spineAvailPt"] = round(avail, 1)
        # Döndürülmüş kutular SAYFA koordinatına çevrilir: sırt yazısı
        # dikeydir, yani genişliği sayfa YÜKSEKLİĞİ boyunca uzanır.
        t_lo = cy - w_t / 2 - 0.22 * 72
        a_lo = cy + avail / 2 - w_a
        pen.boxes.append(["spineTitle", spine_x, t_lo, spine_x + spine_w,
                          t_lo + w_t])
        pen.boxes.append(["spineAuthor", spine_x, a_lo, spine_x + spine_w,
                          a_lo + w_a])
        if t_lo + w_t > a_lo:
            rec["issues"].append("sırt: başlık ile yazar adı ÇAKIŞIYOR")
        if w_t + w_a + 0.45 * 72 > avail:
            rec["issues"].append("sırt yazısı güvenli banda sığmıyor")

    # =========================================================================
    # ③ ÖN KAPAK TİPOGRAFİSİ — ÖLÇÜLEN KUTULARLA
    # =========================================================================
    sx0 = front_x + safe * 72
    sx1 = front_x + (tw - safe) * 72
    sy0 = (edge + safe) * 72
    sy1 = (edge + th - safe) * 72
    rec["frontSafeRectPt"] = [round(sx0, 1), round(sy0, 1),
                              round(sx1, 1), round(sy1, 1)]

    for name, text, font, pt, y in lay["lines"]:
        pen.draw(name, lay["cx"], y, text, font, pt, dark, align="center")

    # --- yaş rozeti: KÖŞEDE, kendi puntosuyla ölçülüp kendi puntosuyla basılır
    badge = "AGES 8–12"
    badge_pt = 17.0
    bw = pen.width(badge, F_BOLD, badge_pt)
    pad_x, pad_y = 13.0, 8.0
    bx = sx1 - bw - pad_x
    by = sy0 + 0.16 * 72 + pad_y
    # ⚠ ROZET RENGİ ÖLÇÜMLE SEÇİLDİ. 0.86/0.36/0.10 turuncu üstünde beyaz
    # yazı 3,78:1 veriyordu — büyük yazı için AA'yı (3:1) geçer ama
    # AA-normal eşiğinin (4,5:1) altındadır. Biraz koyultuldu: 4,7:1.
    BADGE_PLATE = (0.78, 0.30, 0.06)
    c.setFillColorRGB(*BADGE_PLATE)
    c.setFillAlpha(1)
    c.roundRect(bx - pad_x, by - pad_y, bw + 2 * pad_x,
                badge_pt + 2 * pad_y, 7, stroke=0, fill=1)
    pen.draw("ageBadge", bx, by, badge, F_BOLD, badge_pt, (1, 1, 1),
             ground=BADGE_PLATE)
    rec["badgePlateRectPt"] = [round(bx - pad_x, 1), round(by - pad_y, 1),
                               round(bx + bw + pad_x, 1),
                               round(by + badge_pt + pad_y, 1)]

    # =========================================================================
    # ④ ARKA KAPAK — PANEL ÖLÇÜLEN METİNDEN BÜYÜR
    # =========================================================================
    # Faz 6 paneli SABİT 4,95 inç yüksekti. Ciltlide güvenli marj 0,635"
    # olduğu için satır genişliği daralıyor, satır sayısı artıyor ve son
    # paragraf panelin ALTINDAN taşıyordu. Panel artık metinden türetilir.
    bx0 = back_x + safe * 72 + 0.15 * 72
    bw_in = tw - 2 * safe - 0.3
    body = []
    for para in BACK_COPY:
        if not para:
            body.append(None)
            continue
        first = para.startswith("Most books") or para.startswith("This one")
        f, s = (F_BOLD, 15) if first else (F_TEXT, 11.4)
        for ln in wrap_text(para, f, s, bw_in * 72):
            body.append((ln, f, s))

    # ⚠ YAYINCI SATIRI PANELİN İÇİNDE.
    # İlk sürüm onu panelin ALTINA, doğrudan resmin üstüne basıyordu: koyu
    # lacivert yazı koyu yeşil çimenin üstünde okunmuyordu — kapağın kendi
    # sırt kusurunun aynısı. Panel zaten yüksek kontrastlı ve güvenli
    # alandadır; imprint oraya girer ve panel onu da sayarak büyür.
    imprint_line = (cfg.get("publisher") or "").strip()
    if imprint_line:
        body.append(None)
        body.append((imprint_line, F_BOLD, 10.5))

    text_h = 0.0
    for item in body:
        text_h += 9 if item is None else item[2] * 1.42
    text_h += 4 * sum(1 for i, x in enumerate(body) if x is None)

    top = (edge + th - safe - 0.45) * 72
    pad = 20.0
    panel_h = text_h + 2 * pad
    c.setFillColorRGB(1, 1, 1)
    c.setFillAlpha(0.88)
    c.roundRect(bx0 - 18, top + pad - panel_h, bw_in * 72 + 36, panel_h,
                10, stroke=0, fill=1)
    c.setFillAlpha(1)

    ty = top
    for item in body:
        if item is None:
            ty -= 13
            continue
        ln, f, s = item
        pen.draw("backCopy", bx0, ty, ln, f, s, dark, record=False,
                 ground=(1, 1, 1))
        ty -= s * 1.42
    rec["backPanelRectPt"] = [round(bx0 - 18, 1), round(top + pad - panel_h, 1),
                              round(bx0 - 18 + bw_in * 72 + 36, 1),
                              round(top + pad, 1)]
    rec["backCopyBottomPt"] = round(ty, 1)
    back_safe = [back_x + safe * 72, (edge + safe) * 72,
                 back_x + (tw - safe) * 72, (edge + th - safe) * 72]
    rec["backSafeRectPt"] = [round(v, 1) for v in back_safe]
    if ty < back_safe[1]:
        rec["issues"].append("arka kapak metni güvenli alanın ALTINA taşıyor")
    if rec["backPanelRectPt"][1] < back_safe[1]:
        rec["issues"].append("arka kapak paneli güvenli alanın ALTINA taşıyor")

    # =========================================================================
    # ⑤ YAYINCI SATIRI VE BARKOD ALANI
    # =========================================================================
    # ISBN UYDURULMAZ. Kurucu KDP'nin ÜCRETSİZ ISBN'ini seçti; numarayı KDP
    # panelde atar. Numara atanmadıkça kapağa HİÇBİR numara ve HİÇBİR barkod
    # basılmaz — alan temiz bırakılır, KDP kendi barkodunu oraya basar.
    rec["imprint"] = imprint_line or None
    rec["isbnStrategy"] = mb.isbn_strategy()
    rec["isbnPrinted"] = False

    bcw, bch = bcw_in * 72, bch_in * 72
    bcx, bcy = bcx_in * 72, bcy_in * 72
    # Sert beyaz dikdörtgen yerine yuvarlatılmış, ince çerçeveli bir levha:
    # KDP barkodu buraya basar ve levha kasıtlı bir tasarım öğesi gibi durur.
    c.setFillColorRGB(1, 1, 1)
    c.setStrokeColorRGB(0.80, 0.82, 0.86)
    c.setLineWidth(0.7)
    c.roundRect(bcx - 9, bcy - 9, bcw + 18, bch + 18, 5, stroke=1, fill=1)
    rec["barcodeZoneIn"] = [round(bcx / 72, 3), round(bcy / 72, 3),
                            bcw_in, bch_in]

    # =========================================================================
    # ⑥ ÇİZİLEN HER KUTU ÖLÇÜLÜR
    # =========================================================================
    rec["contrast"] = measure_contrast(art, pen, Wpt, Hpt)
    rec["drawnBoxes"] = [{"name": b[0],
                          "rectPt": [round(b[1], 1), round(b[2], 1),
                                     round(b[3], 1), round(b[4], 1)]}
                         for b in pen.boxes]

    front_names = {"title", "title2", "subtitle", "byline", "author",
                   "ageBadge", "spineTitle", "spineAuthor"}
    outside, off_page = [], []
    for name, x0, y0, x1, y1 in pen.boxes:
        if name.startswith("spine"):
            lo, hi = (edge + safe) * 72, (edge + th - safe) * 72
            box_lo, box_hi = y0, y1
            if box_lo < lo - 0.5 or box_hi > hi + 0.5:
                outside.append(f"{name} [{box_lo:.0f},{box_hi:.0f}]")
        elif name in front_names:
            if (x0 < sx0 - 0.5 or x1 > sx1 + 0.5
                    or y0 < sy0 - 0.5 or y1 > sy1 + 0.5):
                outside.append(f"{name} [{x0:.0f},{y0:.0f},{x1:.0f},{y1:.0f}]")
        # ⚠ SAYFA SINIRI: güvenli alandan bağımsız, MUTLAK kapı.
        # Faz 6'da yaş rozeti kâğıdın kenarından 27 pt taşıyordu ve bunu
        # gören HİÇBİR kapı yoktu. Bu denetim güvenli alan kapısının
        # yedeği değil, ondan farklı bir sorunun kapısıdır: güvenli alan
        # "kesilir mi" der, bu "kâğıtta mı" der.
        if x0 < -0.5 or y0 < -0.5 or x1 > Wpt + 0.5 or y1 > Hpt + 0.5:
            off_page.append(f"{name} [{x0:.0f},{y0:.0f},{x1:.0f},{y1:.0f}]")

    # Rozet LEVHASI da (yalnız yazısı değil) güvenli alanda kalmalı.
    px0, py0, px1, py1 = rec["badgePlateRectPt"]
    if px0 < sx0 - 0.5 or px1 > sx1 + 0.5 or py0 < sy0 - 0.5 or py1 > sy1 + 0.5:
        outside.append(f"ageBadgePlate [{px0:.0f},{py0:.0f},{px1:.0f},{py1:.0f}]")

    rec["outsideSafe"] = outside
    rec["offPage"] = off_page
    if outside:
        rec["issues"].append(f"güvenli alanın dışında: {outside}")
    if off_page:
        rec["issues"].append(f"SAYFA DIŞINA TAŞAN TİPOGRAFİ: {off_page}")

    # Çakışma denetimi: ön kapaktaki hiçbir iki kutu üst üste binmemeli.
    named = [(b[0], b[1], b[2], b[3], b[4]) for b in pen.boxes
             if b[0] in front_names and not b[0].startswith("spine")]
    overlaps = []
    for i in range(len(named)):
        for j in range(i + 1, len(named)):
            n1, a0, b0, a1, b1 = named[i]
            n2, c0, d0, c1, d1 = named[j]
            if not (a1 <= c0 or c1 <= a0 or b1 <= d0 or d1 <= b0):
                overlaps.append(f"{n1}×{n2}")
    rec["overlaps"] = overlaps
    if overlaps:
        rec["issues"].append(f"ÖN KAPAK KUTULARI ÇAKIŞIYOR: {overlaps}")

    c.showPage()
    c.save()

    rec["pdf"] = os.path.relpath(out_pdf, mb.ROOT)
    rec["bytes"] = os.path.getsize(out_pdf)
    return rec


# =============================================================================
# KINDLE KAPAĞI
# =============================================================================

def build_kindle_cover(r: mb.Result) -> dict:
    """
    Kindle kapağı JPEG'dir ve yalnızca ÖN kapaktır. KDP en az 1000 px, önerilen
    2560 px yükseklik ister; playbook 2560'ı şart koşuyor.
    """
    from PIL import Image
    src = os.path.join(ART_DIR, "cover-paperback-front.png")
    rec = {"source": os.path.relpath(src, mb.ROOT)}
    if not os.path.exists(src):
        r.fail("kindle kapağı: ham sanat yok", src)
        rec["issues"] = ["ham sanat yok"]
        return rec

    # Ön kapak PDF'inden rasterize etmek en doğrusu: gerçek tipografiyi taşır.
    pdf = os.path.join(mb.ROOT, "08_OUTPUT", "paperback", "cover.pdf")
    out = os.path.join(mb.ROOT, "08_OUTPUT", "kindle", "cover.jpg")
    os.makedirs(os.path.dirname(out), exist_ok=True)

    import subprocess, tempfile
    pages = json.load(open(os.path.join(mb.REPORTS_TRACKED,
                                        "interior-build.json"),
                           encoding="utf-8"))["editions"]["paperback"]["totalPages"]
    g = geometry("paperback", pages)
    with tempfile.TemporaryDirectory() as tmp:
        png = os.path.join(tmp, "wrap.png")
        # 2560 px yükseklik için gereken dpi
        dpi = int(round(2560 / g["fullIn"][1])) + 1
        res = subprocess.run(["gs", "-q", "-dNOPAUSE", "-dBATCH",
                              "-sDEVICE=png16m", f"-r{dpi}",
                              f"-sOutputFile={png}", pdf],
                             capture_output=True)
        if res.returncode != 0 or not os.path.exists(png):
            r.fail("kindle kapağı rasterize edilemedi",
                   "ghostscript yok veya cover.pdf üretilmemiş")
            rec["issues"] = ["rasterize edilemedi"]
            return rec
        with Image.open(png) as im:
            # ön kapağı kes: taşma dışarıda, tam trim
            x0 = int(g["frontX0In"] / g["fullIn"][0] * im.width)
            x1 = int((g["frontX0In"] + g["trimIn"][0]) / g["fullIn"][0] * im.width)
            y0 = int(g["edgeIn"] / g["fullIn"][1] * im.height)
            y1 = int((g["edgeIn"] + g["trimIn"][1]) / g["fullIn"][1] * im.height)
            front = im.crop((x0, y0, x1, y1)).convert("RGB")
            if front.height < 2560:
                scale = 2560 / front.height
                front = front.resize((round(front.width * scale), 2560),
                                     Image.LANCZOS)
            front.save(out, "JPEG", quality=92, optimize=True,
                       progressive=False, dpi=(300, 300))
    with Image.open(out) as im:
        rec.update({"jpg": os.path.relpath(out, mb.ROOT),
                    "px": list(im.size), "mode": im.mode,
                    "bytes": os.path.getsize(out),
                    "aspect": round(im.size[0] / im.size[1], 4)})
    return rec


# =============================================================================
# DOĞRULAMA
# =============================================================================

def validate(rec: dict, r: mb.Result) -> None:
    import subprocess
    b = rec["edition"]
    g = rec["geometry"]
    pdf = os.path.join(mb.ROOT, rec["pdf"])

    info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True)
    facts = {}
    if info.returncode == 0:
        for line in info.stdout.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                facts[k.strip()] = v.strip()
    rec["pdfinfo"] = facts

    if facts:
        w_pt, h_pt = 0.0, 0.0
        try:
            ps = facts.get("Page size", "")
            w_pt = float(ps.split("x")[0].strip())
            h_pt = float(ps.split("x")[1].split("pts")[0].strip())
        except (ValueError, IndexError):
            pass
        want_w, want_h = g["fullIn"][0] * 72, g["fullIn"][1] * 72
        rec["pageSizePt"] = [w_pt, h_pt]
        r.add(abs(w_pt - want_w) < 1.5 and abs(h_pt - want_h) < 1.5,
              f"{b} kapak ölçüsü {g['fullIn'][0]}×{g['fullIn'][1]} inç "
              f"(sırt {g['spineIn']}\")",
              f"{b} kapak ölçüsü {w_pt}×{h_pt} pt — {want_w:.1f}×{want_h:.1f} olmalı")
        r.add(int(facts.get("Pages", "0")) == 1,
              f"{b} kapak tek sayfa",
              f"{b} kapak {facts.get('Pages')} sayfa — tam kapak TEK sayfadır")

    fonts = subprocess.run(["pdffonts", pdf], capture_output=True, text=True)
    not_emb = []
    if fonts.returncode == 0:
        for line in fonts.stdout.splitlines()[2:]:
            p = line.split()
            if len(p) >= 6 and p[-4] != "yes":
                not_emb.append(p[0])
    rec["fontsNotEmbedded"] = not_emb
    r.add(not not_emb, f"{b} kapak: bütün fontlar gömülü",
          f"{b} kapak GÖMÜLÜ OLMAYAN FONT: {not_emb}")

    r.add(rec["bytes"] < 650_000_000,
          f"{b} kapak dosya boyutu sınırda ({rec['bytes']/1e6:.1f} MB)",
          f"{b} kapak {rec['bytes']/1e6:.0f} MB > 650 MB")

    r.add(not rec.get("outsideSafe"),
          f"{b} kapak: bütün tipografi güvenli alanda "
          f"(kenardan {rec['geometry']['safeIn']}\")",
          f"{b} GÜVENLİ ALAN İHLALİ: {rec.get('outsideSafe')}")

    # ⚠ SAYFA SINIRI KAPISI — güvenli alan kapısından AYRI bir soru sorar.
    # Güvenli alan "kesim payında kalır mı" der; bu "kâğıdın üstünde mi"
    # der. Faz 6'da yaş rozeti kâğıdın kenarından 0,38 inç taşıyordu ve
    # güvenli alan kapısı bunu göremedi çünkü çizileni değil planlananı
    # ölçüyordu. İki kapı iki ayrı kusur sınıfıdır ve ikisi de gerekir.
    r.add(not rec.get("offPage"),
          f"{b} kapak: hiçbir tipografi sayfa dışına taşmıyor",
          f"{b} SAYFA DIŞINA TAŞAN TİPOGRAFİ: {rec.get('offPage')}")
    # ⚠ KONTRAST KAPISI — talimat § 7 ve § 17.
    # "Yazar adı sanatın içinde kaybolmamalı" bir fikir değil bir sayıdır.
    # p10 kullanılır: metnin en kötü %10'u da okunmak zorundadır.
    con = rec.get("contrast") or {}
    low = {n: v["p10"] for n, v in con.items() if v["p10"] < _WCAG_MIN}
    r.add(not low,
          f"{b} kapak: bütün tipografi kontrast eşiğini geçiyor "
          f"(p10 ≥ {_WCAG_MIN}:1)",
          f"{b} KONTRAST YETERSİZ: {low} — eşik {_WCAG_MIN}:1 (WCAG AA)")
    weak = {n: v["p10"] for n, v in con.items()
            if _WCAG_MIN <= v["p10"] < _WCAG_GOOD}
    r.warn(not weak,
           f"{b} kapak: bütün tipografi AAA eşiğinde (≥{_WCAG_GOOD}:1)",
           f"{b} kontrast AA ile AAA arasında: {weak} — okunur ama "
           "küçük resimde zayıflayabilir")
    au = con.get("author", {}).get("p10")
    if au is not None:
        r.add(au >= _WCAG_MIN,
              f"{b}: YAZAR ADI sanatın içinde kaybolmuyor (kontrast {au}:1)",
              f"{b} YAZAR ADI KAYBOLUYOR: kontrast {au}:1 < {_WCAG_MIN}:1")

    r.add(not rec.get("overlaps"),
          f"{b} kapak: ön kapak kutuları çakışmıyor",
          f"{b} ÇAKIŞAN KUTULAR: {rec.get('overlaps')}")

    # ⚠ ETKİN ÇÖZÜNÜRLÜK — BÜYÜTME ÇÖZÜNÜRLÜK ÜRETMEZ.
    # KDP baskı kapağı için 300 dpi ister. Faz 6 tuvali 300 dpi üretti ama
    # ham sanat 2,6× BÜYÜTÜLMÜŞTÜ; gerçek örnekleme 115 dpi'ydi ve bunu
    # ölçen hiçbir kapı yoktu. Bu bir UYARI'dır, HATA değil: sayı ham
    # sanatın kendisinden gelir, hattın kusuru değildir, ve düzeltmesi
    # kurucunun elindedir (daha yüksek çözünürlüklü kapak sanatı).
    # `rec` kısmi olabilir: package_selftest bu fonksiyonu kasıtlı olarak
    # eksik bir kayıtla çağırır (kapının kendisini sınamak için). Kapı,
    # sınandığı koşulda ÇÖKMEMELİ — çöken bir kapı da ölü bir kapıdır.
    eff = rec.get("effectiveArtDpi")
    if eff is not None:
        src_px = (rec.get("art") or {}).get("sourcePx") or ["?", "?"]
        r.warn(eff >= 300,
               f"{b} kapak sanatı etkin çözünürlük {eff} dpi (KDP ≥300)",
               f"{b} KAPAK SANATI ETKİN {eff} dpi — KDP 300 dpi ister. "
               f"Ham sanat {src_px[0]}×{src_px[1]} px ve tuvale "
               f"{rec.get('artUpscaleFactor', '?')}× BÜYÜTÜLDÜ. Büyütme "
               "çözünürlük üretmez — KURUCU KARARI (§ kapak sanatı)")

    # ISBN: numara atanmadıkça kapağa hiçbir numara/barkod basılmaz.
    r.add(rec.get("isbnPrinted") is False or mb.isbn_assigned(),
          f"{b} kapak: sahte ISBN/barkod basılmadı",
          f"{b} KAPAĞA ISBN BASILMIŞ ama numara atanmamış")

    r.add(not rec["issues"], f"{b} kapak: yapısal kusur yok",
          f"{b} KAPAK KUSURLARI: {rec['issues']}")

    # Kırpma payı: zemin sanatı tuvale sığdırılırken ne kadar kaybedildi
    cropped = max(rec.get("art", {}).get("croppedPct", [0, 0]))
    r.warn(cropped <= 12.0,
           f"{b} zemin sanatı kırpması makul (%{cropped:.1f})",
           f"{b} zemin sanatı %{cropped:.1f} kırpıldı — oran uyuşmazlığı "
           "kompozisyonu kaydırabilir, gözle bakın")


def main() -> int:
    ap = argparse.ArgumentParser(description="Kapak üretimi")
    ap.add_argument("--edition", default="all",
                    choices=["all", "paperback", "hardcover"])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    print("═" * 72)
    print("  KAPAK ÜRETİMİ")
    print("═" * 72)

    r = mb.Result("covers", verbose=args.verbose)
    try:
        fonts = register_fonts()
    except (ImportError, FileNotFoundError) as exc:
        r.fail("kapak fontu kaydedilemedi", str(exc))
        return r.finish(None)

    ib = os.path.join(mb.REPORTS_TRACKED, "interior-build.json")
    if not os.path.exists(ib):
        r.fail("interior-build.json yok",
               "sırt genişliği GERÇEK sayfa sayısından türetilir; önce "
               "`interior.py` çalıştırın")
        return r.finish(None)
    with open(ib, encoding="utf-8") as fh:
        interior = json.load(fh)["editions"]

    cfg = dict(mb._CFG["project"])
    # Yayıncı adı TEK yerden gelir: project_config.json § founder.publisher.
    # Faz 6'da bu satır `publishing.imprint` okuyordu — proje yapılandırmasında
    # BÖYLE BİR ANAHTAR HİÇ YOKTU, yani değer her koşuda boştu ve kapak
    # sessizce yayıncısız basılıyordu. Kapı bunu "kurucu bağımlılığı" diye
    # UYARI olarak geçiyordu; artık kurucu kararı var ve okunuyor.
    cfg["publisher"] = mb.PUBLISHER

    payload = {"$comment": [
        "KAPAK ÜRETİM RAPORU — ölçü ve doğrulama. Proza içermez.",
        "Ham sanat DEĞİŞTİRİLMEDİ; üretilmiş yazı örtüldü, gerçek",
        "tipografi CLI ile basıldı, barkod alanı TEMİZ bırakıldı.",
        "Üretici: 04_BUILD/covers.py",
    ], "gate": mb.read_gate(), "fonts": fonts,
        "author": AUTHOR, "editions": {}}

    keys = ["paperback", "hardcover"] if args.edition == "all" else [args.edition]
    for b in keys:
        pages = interior[b]["totalPages"]
        rec = build_cover(b, pages, cfg, r)
        if "pdf" in rec:
            validate(rec, r)
            g = rec["geometry"]
            print(f"\n  ── {b} ──")
            print(f"     sayfa        : {pages}")
            print(f"     sırt         : {g['spineIn']}\""
                  f"{'  ⚠ TÜRETİLDİ' if g['spineDerived'] else ''}")
            print(f"     tam kapak    : {g['fullIn'][0]} × {g['fullIn'][1]} inç"
                  f"  ({g['fullPx'][0]} × {g['fullPx'][1]} px @ {DPI} dpi)")
            print(f"     zemin kırpma : %{max(rec['art']['croppedPct'])}")
        payload["editions"][b] = rec

    if args.edition == "all":
        payload["kindle"] = build_kindle_cover(r)
        k = payload["kindle"]
        if "px" in k:
            print(f"\n  ── kindle ──")
            print(f"     kapak        : {k['px'][0]} × {k['px'][1]} px "
                  f"· {k['bytes']/1e6:.2f} MB")
            r.add(k["px"][1] >= 2560,
                  f"kindle kapağı ≥2560 px yükseklik ({k['px'][1]})",
                  f"kindle kapağı {k['px'][1]} px — playbook 2560 istiyor")
            r.add(k["mode"] == "RGB", "kindle kapağı RGB JPEG",
                  f"kindle kapağı {k['mode']}")

    # Yayıncı adı UYDURULMAZ.
    r.warn(bool(cfg["publisher"]), "yayıncı/imprint tanımlı",
           "yayıncı/imprint proje kaynaklarında YOK — kurucu bağımlılığı; "
           "kapağa hiçbir yayıncı adı basılmadı (uydurulmadı)")

    if args.check:
        if not os.path.exists(OUT_JSON):
            r.fail("cover-build.json yok", "`covers.py` çalıştırın")
            return r.finish(None)
        with open(OUT_JSON, encoding="utf-8") as fh:
            old = json.load(fh)
        same = all(old.get("editions", {}).get(k, {}).get("geometry")
                   == payload["editions"][k]["geometry"] for k in keys)
        r.add(same, "kapak raporu güncel",
              "BAYAT — sayfa sayısı veya kapak geometrisi değişmiş")
        return r.finish(None)

    os.makedirs(mb.REPORTS_TRACKED, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"\n  ✎ {os.path.relpath(OUT_JSON, mb.ROOT)}")
    for b in keys:
        if "pdf" in payload["editions"][b]:
            print(f"  ✎ {payload['editions'][b]['pdf']}")
    if payload.get("kindle", {}).get("jpg"):
        print(f"  ✎ {payload['kindle']['jpg']}")
    return r.finish(None)


if __name__ == "__main__":
    sys.exit(main())
