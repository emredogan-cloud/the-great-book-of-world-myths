#!/usr/bin/env python3
"""
KAPAK ÜRETİMİ — CİLTSİZ SARIM · CİLTLİ SARIM · KINDLE KAPAĞI
================================================================================
    python3 04_BUILD/covers.py                 hepsini üret + doğrula
    python3 04_BUILD/covers.py --edition paperback
    python3 04_BUILD/covers.py --check         kayıtlı rapor bayat mı

    07_ASSETS/raw/cover-*.png        ham sanat (DEĞİŞTİRİLMEZ)
              ↓
    08_OUTPUT/<edition>/cover.pdf    baskıya hazır · gömülü font · 300 dpi
    08_OUTPUT/kindle/cover.jpg       ≥2560 px yükseklik
    06_REPORTS/tracked/cover-build.json

--------------------------------------------------------------------------------
ÜRETİLMİŞ YAZI KULLANILMAZ — VE BU SEFER SEBEBİ SOYUT DEĞİL
--------------------------------------------------------------------------------
Faz 5 şartnamesi bütün kapak promptlarını `typography: post` işaretlemişti:
kesin ticari metin için görsel üreticisine güvenilmez. Faz 6 teslimatı bunu
doğruladı ve bedeli ölçülebilir:

  ① KAPAKTA YANLIŞ BAŞLIK VAR. Üretilen sanat "STORIES from the WHOLE
     WORLD" yazıyor. Kitabın adı **The Great Book of World Myths**.
     Üç kapak dosyasının üçünde de aynı yanlış başlık basılı.
  ② ARKA KAPAKTA UYDURULMUŞ ISBN VE BARKOD VAR:
     "978-1-963000-22-5". Bu numara projeye ait DEĞİLDİR; A9 kararı hâlâ
     açıktır ve talimat § 41 ISBN uydurmayı açıkça yasaklar. Gerçek bir
     ISBN'e çakışabilecek sahte bir barkod basmak ticari bir tehlikedir.

Bu yüzden ham sanat burada YALNIZCA ZEMİNDİR. Üretilmiş yazının bulunduğu
bölge kapatılır, gerçek tipografi CLI ile basılır, barkod alanı TEMİZ
bırakılır (KDP kendi barkodunu oraya basar).
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
RAW = os.path.join(mb.ASSETS, "raw")
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

# Okura giden kesin dizeler. TEK KAYNAK: project_config + kurucu kararı.
AUTHOR = "Emre Doğan"

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


def sky_band(img, x0, y0, x1, y1):
    """Bir bölgenin ortalama rengi — üretilmiş yazıyı örtecek bandın rengi."""
    from PIL import Image
    box = img.crop((max(0, int(x0)), max(0, int(y0)),
                    min(img.width, int(x1)), min(img.height, int(y1))))
    box = box.resize((1, 1), Image.LANCZOS)
    return box.getpixel((0, 0))


# =============================================================================
# ÇİZİM
# =============================================================================

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


def build_cover(binding: str, pages: int, cfg: dict, r: mb.Result) -> dict:
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase.pdfmetrics import stringWidth

    g = geometry(binding, pages)
    W_in, H_in = g["fullIn"]
    Wpt, Hpt = W_in * 72, H_in * 72

    src = os.path.join(RAW, "cover-paperback-wrap.png" if binding == "paperback"
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

    out_pdf = os.path.join(mb.ROOT, "08_OUTPUT", binding, "cover.pdf")
    os.makedirs(os.path.dirname(out_pdf), exist_ok=True)
    c = canvas.Canvas(out_pdf, pagesize=(Wpt, Hpt),
                      initialFontName=F_TEXT, initialFontSize=12)
    c.setTitle(f"{cfg['title']} — {binding} cover")
    c.setAuthor(AUTHOR)

    # --- zemin ---
    c.drawImage(ImageReader(art), 0, 0, width=Wpt, height=Hpt)

    edge, safe = g["edgeIn"], g["safeIn"]
    tw, th = g["trimIn"]
    front_x = g["frontX0In"] * 72
    back_x = g["backX0In"] * 72
    spine_x = g["spineX0In"] * 72
    spine_w = g["spineIn"] * 72

    # =========================================================================
    # ① ÜRETİLMİŞ BAŞLIĞI ÖRT
    # =========================================================================
    # Sanatın ön kapak üst bölgesinde YANLIŞ bir başlık basılı
    # ("STORIES from the WHOLE WORLD"). Ölçüldü: yazı, tam kapak
    # yüksekliğinin ÜSTTEN %0,067–%0,28 bandında duruyor.
    #
    # ⚠ İLK DENEME YETMEDİ ve sebebi öğreticidir: bant bir GRADYAN'dı ve
    # yazının bulunduğu yükseklikte örtme gücü %82'ydi — "WHOLE WORLD"
    # başlığın altından hayalet gibi görünüyordu. Örtü, yazının olduğu yerde
    # TAM OPAK olmak zorundadır; yumuşama ancak yazının BİTTİĞİ yerden
    # sonra başlayabilir.
    px_per_in = g["fullPx"][1] / H_in
    # Temiz gök örneği: yazının SOL ÜSTÜNDE kalan boş alan.
    sample = sky_band(art,
                      (front_x / 72 + 0.10 * tw) * px_per_in,
                      0.020 * g["fullPx"][1],
                      (front_x / 72 + 0.30 * tw) * px_per_in,
                      0.055 * g["fullPx"][1])
    rgb = tuple(v / 255 for v in sample)

    # Bandın nereye kadar OPAK olacağı iki kısıtın büyüğüdür:
    #   · üretilmiş yazının ölçülen alt sınırı (%0,30)
    #   · BİZİM basacağımız başlık bloğunun alt sınırı
    # İkincisi ciltlide daha aşağıdadır (güvenli marj 0,635" başlığı aşağı
    # iter) ve ilk sürümde alt satırlar bandın dışına, resmin üstüne düşüyordu.
    safe_top_pt = (edge + th - safe) * 72
    title_pt = fit_title(c, ["THE GREAT BOOK OF", "WORLD MYTHS"], F_DISPLAY,
                         (tw - 2 * safe - 0.35) * 72, 72)
    block_bottom = safe_top_pt - title_pt * 0.80 - title_pt * 1.06 \
        - title_pt * 0.50 - 3 * 16 * 1.35 - 20
    TEXT_BOTTOM_FRAC = 0.30                 # ölçülen %0,28 + emniyet payı
    FADE_FRAC = 0.09
    opaque_top = Hpt                        # tuvalin en üstü (taşma dâhil)
    opaque_bot = min(Hpt * (1 - TEXT_BOTTOM_FRAC), block_bottom)
    c.setFillColorRGB(*rgb)
    c.setFillAlpha(1)
    c.rect(front_x, opaque_bot, tw * 72, opaque_top - opaque_bot,
           stroke=0, fill=1)
    steps = 80
    fade_h = Hpt * FADE_FRAC
    for i in range(steps):
        t = i / (steps - 1)                 # 0 = bandın üstü, 1 = altı
        y = opaque_bot - fade_h * (i + 1) / steps
        c.setFillAlpha(max(0.0, 1.0 - t))
        c.rect(front_x, y, tw * 72, fade_h / steps + 1.4, stroke=0, fill=1)
    # ⚠ ALFA SIZINTISI: reportlab'da alfa DURUM'dur ve sonraki her çizime
    # taşınır. İlk sürümde başlık bu yüzden soluk basıldı.
    c.setFillAlpha(1)
    c.setStrokeAlpha(1)

    # =========================================================================
    # ② ÖN KAPAK TİPOGRAFİSİ
    # =========================================================================
    # ⚠ BAŞLIK İKİ SATIRDIR, ÜÇ DEĞİL.
    # "OF"u kendi satırına almak, ortalanmış küçük bir sözcüğü tam olarak
    # alt satırın sözcük arasına düşürüyor ve "WORLD^OF MYTHS" gibi
    # okunuyordu. İki satır hem çakışmayı ortadan kaldırır hem daha iyi kırar.
    title_words = ["THE GREAT BOOK OF", "WORLD MYTHS"]
    inner = (tw - 2 * safe - 0.35) * 72
    size = fit_title(c, title_words, F_DISPLAY, inner, 72)
    cx = front_x + tw * 72 / 2
    dark = (0.075, 0.115, 0.26)

    def centred(text, font, pt, y, fill=dark, halo=0.0):
        c.setFont(font, pt)
        w = stringWidth(text, font, pt)
        if halo:
            c.setFillColorRGB(1, 1, 1)
            c.setFillAlpha(halo)
            for dx, dy in ((1.7, -1.7), (-1.7, -1.7), (1.7, 1.7), (-1.7, 1.7)):
                c.drawString(cx - w / 2 + dx, y + dy, text)
            c.setFillAlpha(1)
        c.setFillColorRGB(*fill)
        c.drawString(cx - w / 2, y, text)
        return w

    # ⚠ SATIR ARALIĞI TAŞIYICI YÜKSEKLİKTEN HESAPLANIR, ORANDAN DEĞİL.
    # İlk sürümde "OF" satırından sonraki iniş 0,68×punto idi; "WORLD MYTHS"
    # taşıyıcı yüksekliği 0,72×punto olduğu için üst satırın ÜSTÜNE çıkıyor
    # ve "WORLD^OF MYTHS" gibi görünüyordu. Aşağıdaki üç iniş açıkça yazılır.
    # Başlık ÜST GÜVENLİ KENARDAN konumlanır, taşma kenarından değil.
    title_y0 = safe_top_pt - size * 0.80
    y = title_y0
    centred(title_words[0], F_DISPLAY, size, y)
    y -= size * 1.06
    centred(title_words[1], F_DISPLAY, size, y)

    y -= size * 0.50
    sub = "45 Stories of Gods, Heroes, and Monsters from 22 Cultures"
    sub_pt = 15.5
    while len(wrap_text(sub, F_BOLD, sub_pt, inner)) > 1 and sub_pt > 10:
        sub_pt -= 0.5
    for ln in wrap_text(sub, F_BOLD, sub_pt, inner):
        centred(ln, F_BOLD, sub_pt, y)
        y -= sub_pt * 1.35
    centred("Retold for Young Readers", F_ITALIC, 14, y - 2)

    # --- yazar adı: ÖN KAPAK ALTINDA, kendi şeridinde ---
    # İlk sürümde ad doğrudan resmin üstüne basılıyordu ve açık zeminde
    # kayboluyordu. Ad, kapağın ticari kimliğidir; okunması pazarlık konusu
    # değildir — arkasına ince bir koyu şerit konur.
    # ⚠ ROZET VE YAZAR ADI ÇAKIŞMAMALI. Ciltlide güvenli marj daha geniş
    # (0,635" vs 0,25") ve ilk sürümde rozet, ortalanmış yazar şeridinin
    # üstüne biniyordu. Yazar şeridi rozetin ÜSTÜNE alınır ve rozet köşede
    # kendi satırında kalır.
    # GÜVENLİ DİKDÖRTGEN — bütün ön kapak tipografisi bunun içinde kalmalı
    # ve kalıp kalmadığı ÖLÇÜLÜR (aşağıda `safeBoxes`). Ciltlide bu kutu
    # ciltsizden dar: 0,635" vs 0,25".
    sx0 = front_x + safe * 72
    sx1 = front_x + (tw - safe) * 72
    sy0 = (edge + safe) * 72
    sy1 = (edge + th - safe) * 72
    rec["frontSafeRectPt"] = [round(sx0, 1), round(sy0, 1),
                              round(sx1, 1), round(sy1, 1)]
    boxes = []

    badge = "AGES 8–12"
    badge_pt = 14
    c.setFont(F_BOLD, badge_pt)
    bw = stringWidth(badge, F_BOLD, badge_pt)
    by = sy0 + 0.17 * 72
    badge_top = by + 21

    c.setFont(F_BOLD, 27)
    aw = stringWidth(AUTHOR, F_BOLD, 27)
    ay = badge_top + 0.34 * 72
    c.setFillColorRGB(0.075, 0.115, 0.26)
    c.setFillAlpha(0.82)
    c.roundRect(cx - aw / 2 - 22, ay - 13, aw + 44, 46, 9, stroke=0, fill=1)
    c.setFillAlpha(1)
    c.setFillColorRGB(1, 1, 1)
    c.drawString(cx - aw / 2, ay, AUTHOR)

    bx = sx1 - bw - 12
    c.setFillColorRGB(0.86, 0.36, 0.10)
    c.setFillAlpha(1)
    c.roundRect(bx - 12, by - 9, bw + 24, 30, 7, stroke=0, fill=1)
    c.setFillColorRGB(1, 1, 1)
    c.drawString(bx, by, badge)

    boxes.append(("ageBadge", bx - 12, by - 9, bx + bw + 12, by + 21))
    boxes.append(("author", cx - aw / 2 - 22, ay - 13, cx + aw / 2 + 22, ay + 33))
    boxes.append(("title", cx - inner / 2, title_y0 - size * 1.06,
                  cx + inner / 2, title_y0 + size * 0.78))

    outside = []
    for name, x0, y0, x1, y1 in boxes:
        if x0 < sx0 - 0.5 or x1 > sx1 + 0.5 or y0 < sy0 - 0.5 or y1 > sy1 + 0.5:
            outside.append(f"{name} [{x0:.0f},{y0:.0f},{x1:.0f},{y1:.0f}]")
    rec["safeBoxes"] = [{"name": n, "rectPt": [round(a, 1), round(b_, 1),
                                               round(c_, 1), round(d, 1)]}
                        for n, a, b_, c_, d in boxes]
    rec["outsideSafe"] = outside
    if outside:
        rec["issues"].append(f"güvenli alanın dışında: {outside}")

    # Çakışma denetimi: rozet ile yazar şeridi üst üste binmemeli.
    _, abx0, aby0, abx1, aby1 = boxes[0]
    _, aux0, auy0, aux1, auy1 = boxes[1]
    if not (abx1 < aux0 or aux1 < abx0 or aby1 < auy0 or auy1 < aby0):
        rec["issues"].append("yaş rozeti ile yazar şeridi ÇAKIŞIYOR")

    rec["authorPanelBottomIn"] = round((ay - 13) / 72, 3)
    rec["badgeTopIn"] = round(badge_top / 72, 3)

    # =========================================================================
    # ③ SIRT
    # =========================================================================
    # KDP: 100 sayfanın altında sırt yazısı basılmaz. 236 sayfada basılır.
    spine_ok = pages >= 100
    rec["spineText"] = spine_ok
    if spine_ok:
        c.saveState()
        c.translate(spine_x + spine_w / 2, edge * 72 + (th * 72) / 2)
        c.rotate(-90)
        st = "THE GREAT BOOK OF WORLD MYTHS"
        # Sırtta kullanılabilir uzunluk, kitabın YÜKSEKLİĞİ eksi iki güvenli
        # marjdır — ciltlide bu 0,635"×2'dir. İlk sürüm sabit 1,6" düşüyordu
        # ve ciltli sırtta yazı taşıyordu.
        avail = (th - 2 * safe) * 72
        asize_ratio = 0.70
        ssize = 21
        while ssize > 8:
            need = (stringWidth(st, F_DISPLAY, ssize)
                    + stringWidth(AUTHOR, F_BOLD, ssize * asize_ratio)
                    + 0.45 * 72)
            if need <= avail:
                break
            ssize -= 1
        c.setFont(F_DISPLAY, ssize)
        w = stringWidth(st, F_DISPLAY, ssize)
        asz = ssize * asize_ratio
        aw = stringWidth(AUTHOR, F_BOLD, asz)
        # Başlık merkezden sola, yazar adı sağ uçta — ikisi de güvenli bantta.
        c.setFillColorRGB(*dark)
        c.drawString(-w / 2 - 0.22 * 72, -ssize * 0.34, st)
        c.setFont(F_BOLD, asz)
        c.drawString(avail / 2 - aw, -ssize * 0.34, AUTHOR)
        c.restoreState()
        rec["spineFontPt"] = ssize
        rec["spineNeedPt"] = round(w + aw + 0.45 * 72, 1)
        rec["spineAvailPt"] = round(avail, 1)
        if w + aw + 0.45 * 72 > avail:
            rec["issues"].append("sırt yazısı güvenli banda sığmıyor")

    # =========================================================================
    # ④ ARKA KAPAK
    # =========================================================================
    bx0 = back_x + safe * 72 + 0.15 * 72
    bw_in = tw - 2 * safe - 0.3
    ty = (edge + th - safe - 0.55) * 72

    # okunabilirlik paneli — gökyüzü üstünde metin
    c.setFillColorRGB(1, 1, 1)
    c.setFillAlpha(0.86)
    c.roundRect(bx0 - 18, ty - 4.35 * 72, bw_in * 72 + 36, 4.95 * 72,
                10, stroke=0, fill=1)
    c.setFillAlpha(1)
    c.setFillColorRGB(*dark)
    for para in BACK_COPY:
        if not para:
            ty -= 9
            continue
        first = para.startswith("Most books") or para.startswith("This one")
        f, s = (F_BOLD, 15) if first else (F_TEXT, 11.4)
        for ln in wrap_text(para, f, s, bw_in * 72):
            c.setFont(f, s)
            c.drawString(bx0, ty, ln)
            ty -= s * 1.42
        ty -= 4

    # =========================================================================
    # ⑤ BARKOD ALANI — TEMİZ BIRAKILIR
    # =========================================================================
    # Ham sanatta UYDURULMUŞ bir ISBN barkodu vardı. KDP kendi barkodunu
    # basar ve bizden yalnızca TEMİZ bir dikdörtgen ister. Beyaz doldurulur;
    # hiçbir numara yazılmaz (A9 açık · talimat § 41).
    bcw, bch = cs.BARCODE_W_IN * 72, cs.BARCODE_H_IN * 72
    bcx = back_x + (tw - safe) * 72 - bcw - 0.15 * 72
    bcy = (edge + cs.BARCODE_FROM_BOTTOM_IN) * 72
    c.setFillColorRGB(1, 1, 1)
    c.rect(bcx - 8, bcy - 8, bcw + 16, bch + 16, stroke=0, fill=1)
    rec["barcodeZoneIn"] = [round(bcx / 72, 3), round(bcy / 72, 3),
                            cs.BARCODE_W_IN, cs.BARCODE_H_IN]

    # yayıncı satırı — DEĞER YOKSA YAZILMAZ
    imprint = (cfg.get("publisher") or "").strip()
    rec["imprint"] = imprint or None
    if imprint:
        c.setFont(F_TEXT, 10)
        c.setFillColorRGB(*dark)
        c.drawString(bx0, (edge + safe + 0.1) * 72, imprint)

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
    src = os.path.join(RAW, "cover-paperback-front.png")
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
    cfg["publisher"] = (mb._CFG.get("publishing") or {}).get("imprint") or ""

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
