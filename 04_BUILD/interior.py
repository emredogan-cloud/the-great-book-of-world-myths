#!/usr/bin/env python3
"""
ÜRETİM İÇ BLOĞU — CİLTSİZ + CİLTLİ PDF
================================================================================
    python3 04_BUILD/interior.py                    her iki sürümü diz
    python3 04_BUILD/interior.py --edition paperback
    python3 04_BUILD/interior.py --check            kayıtlı rapor bayat mı

Bu, `proof_interior.py`'nin YERİNE GEÇMEZ. O bir MÜHENDİSLİK PROVASIDIR ve
görsel yerine çerçeve çizer; sayfa modelinin regresyon avcısıdır. Bu betik
ÜRETİM İÇ BLOĞUDUR: gerçek gömülü font, gerçek görsel, gerçek ön/arka madde,
gerçek sayfa numarası, aynalı marj.

    02_MANUSCRIPT/book.json          proza (DEPO DIŞINDA)
    01_RESEARCH/*.json               yapı · telaffuz · sözlük · kültür kartı
    07_ASSETS/processed/print/*.tif  600 dpi gri görseller
              ↓
    08_OUTPUT/<edition>/interior.pdf         ← PROZA İÇERİR, DEPODA DURMAZ
    06_REPORTS/tracked/interior-build.json   ← YALNIZCA SAYI, depoda durur

--------------------------------------------------------------------------------
GÖMÜLÜ FONT BİR KDP ŞARTIDIR — VE MODELİN KENDİSİDİR
--------------------------------------------------------------------------------
reportlab'ın "Times-Roman"u base-14'tür ve PDF'e GÖMÜLMEZ; KDP gömülü font
ister. Ayrıca K27 sayfa modelini ölçerken yazı karakterinin kelime/sayfa'yı
%21 oynattığını bulmuştu (DejaVu 282,8 · Times/Liberation 357,5). Yani font
seçimi bir tipografi zevki değil, FİYAT MODELİNİN PARAMETRESİDİR.

Liberation Serif seçildi: Times New Roman ile metrik uyumludur (modelin
kalibre edildiği metrik), SIL OFL lisanslıdır (gömme ve dağıtım serbest) ve
kitabın ihtiyaç duyduğu bütün diakritikleri taşır — ā · ō · ī · ʻokina ·
U+2019 · em dash dâhil (K28 · D35).
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb
import editions as ed_mod
import imagespec as spec
import page_budget as pb

OUT_JSON = os.path.join(mb.REPORTS_TRACKED, "interior-build.json")
PRINT_DIR = os.path.join(spec.PROCESSED_DIR, "print")

# Aranacak font yolları — ilki bulunan kazanır. Depoya ikili dosya koymamak
# için sistem fontu kullanılır; `07_ASSETS/fonts/` kurucunun kendi lisanslı
# fontunu koyabilmesi için ÖNCE aranır.
FONT_CANDIDATES = {
    "body": ["Liberation Serif", "LiberationSerif-Regular.ttf"],
    "bold": ["Liberation Serif Bold", "LiberationSerif-Bold.ttf"],
    "italic": ["Liberation Serif Italic", "LiberationSerif-Italic.ttf"],
}
FONT_DIRS = [
    os.path.join(mb.ASSETS, "fonts"),
    "/usr/share/fonts/truetype/liberation",
    "/usr/local/share/fonts",
    os.path.expanduser("~/.fonts"),
]

FONT_BODY, FONT_BOLD, FONT_ITALIC = "BookBody", "BookBold", "BookItalic"


_RAW_DIMS: dict[str, tuple[int, int]] = {}


def _raw_dims(image_id: str) -> tuple[int, int] | None:
    """Ham dosyanın gerçek ölçüsü — dosya adı sapmaları dâhil."""
    if not _RAW_DIMS:
        from PIL import Image as PILImage
        if os.path.isdir(spec.RAW_DIR):
            for name in os.listdir(spec.RAW_DIR):
                if not name.lower().endswith(f".{spec.RAW_FORMAT}"):
                    continue
                cid, _ = spec.canonical_id(name.rsplit(".", 1)[0])
                try:
                    with PILImage.open(os.path.join(spec.RAW_DIR, name)) as im:
                        _RAW_DIMS[cid] = im.size
                except OSError:
                    continue
    return _RAW_DIMS.get(image_id)


def _raw_pixel_width(image_id: str) -> int | None:
    d = _raw_dims(image_id)
    return d[0] if d else None


def _art_share(image_id: str, derivative_w: int) -> float | None:
    """
    Türev tuvalinin ne kadarını GERÇEK çizim kaplıyor.

    `convert_images.fit_no_distort` oranı korumak için beyaz dolgu ekler;
    dolgu bilgi taşımaz ve çözünürlük hesabına girmemelidir. Oran, hamın
    türeve sığdırılmasından türetilir — dosyayı tekrar açmaya gerek yok.
    """
    d = _raw_dims(image_id)
    if not d:
        return None
    kind = image_id.split("-")[0]
    if kind not in spec.KINDS:
        return None
    tw, th = spec.KINDS[kind]["print_px"]
    scale = min(tw / d[0], th / d[1])
    return (d[0] * scale) / derivative_w


def calibrated_wpp() -> float:
    """
    Kelime/sayfa'nın TEK kaynağı `editions.words_per_page`'tir (K27 kalibrasyonu).
    `proof_interior.py` bu sayıyı 354,2 diye ELLE yazıyor; iki yerde tutulan
    bir sayı ayrışır. Burada kaynaktan okunur.
    """
    return ed_mod.words_per_page(ed_mod.get("paperback"), mb.PAGE_TARGET)


def billed_pages_per_story() -> int:
    return pb.compute(calibrated_wpp())["billedPagesPerStory"]


# =============================================================================
# FONT
# =============================================================================

def register_fonts() -> dict:
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    resolved = {}
    for key, names in FONT_CANDIDATES.items():
        path = None
        for d in FONT_DIRS:
            for n in names:
                if not n.lower().endswith(".ttf"):
                    continue
                cand = os.path.join(d, n)
                if os.path.exists(cand):
                    path = cand
                    break
            if path:
                break
        if not path:
            raise FileNotFoundError(
                f"'{key}' için font bulunamadı. Aranan: {names} · {FONT_DIRS}\n"
                "Debian/Ubuntu: sudo apt-get install fonts-liberation")
        resolved[key] = path

    pdfmetrics.registerFont(TTFont(FONT_BODY, resolved["body"]))
    pdfmetrics.registerFont(TTFont(FONT_BOLD, resolved["bold"]))
    pdfmetrics.registerFont(TTFont(FONT_ITALIC, resolved["italic"]))
    return resolved


# =============================================================================
# DİZGİ MOTORU
# =============================================================================

class Interior:
    """
    Tek sürümün iç bloğunu dizer.

    Sayfa geometrisi AYNALIDIR: iç marj tek sayfada solda, çift sayfada
    sağdadır. KDP'nin 0,500" iç marj şartı sayfa sayısına bağlıdır ve
    `editions.required_gutter()` onu tek yerde tutar.
    """

    def __init__(self, edition_key: str, pages_estimate: int):
        from reportlab.lib.pagesizes import inch
        from reportlab.pdfgen import canvas

        self.key = edition_key
        self.ed = ed_mod.get(edition_key)
        self.t = self.ed.typography
        self.gutter = ed_mod.required_gutter(pages_estimate)
        self.w_in, self.h_in = ed_mod.text_block(self.ed, pages_estimate)
        self.width = self.w_in * 72
        self.lead = self.t.leading_pt
        self.lines_per_page = ed_mod.lines_per_page(self.ed, pages_estimate)

        self.out_pdf = os.path.join(mb.ROOT, "08_OUTPUT", edition_key, "interior.pdf")
        os.makedirs(os.path.dirname(self.out_pdf), exist_ok=True)
        # ⚠ `initialFontName` GÖMÜLÜ FONT OLMAK ZORUNDA.
        # reportlab her sayfanın içerik akışına bir açılış durumu yazar ve o
        # durumun fontu varsayılan olarak Helvetica'dır — base-14, yani
        # GÖMÜLMEZ. Tek satır Helvetica çizilmese bile `pdffonts` onu
        # "emb: no" listeler ve KDP'nin "gömülü olmayan font: 0" şartı düşer.
        # Sayfa başında `setFont` çağırmak YETMEZ: açılış durumu ondan önce
        # yazılıyor. Kaynağı burasıdır.
        self.c = canvas.Canvas(
            self.out_pdf,
            pagesize=(self.ed.trim_w_in * inch, self.ed.trim_h_in * inch),
            initialFontName=FONT_BODY,
            initialFontSize=self.t.body_pt,
            initialLeading=self.t.leading_pt)
        self.c.setTitle(mb._CFG["project"]["title"])
        # ⚠ project.author DİYE BİR ANAHTAR YOK — bu satır her koşuda
        # sessizce BOŞ dize yazıyordu ve iki üretim PDF'i yazarsız
        # çıkıyordu. Ad tek kaynaktan gelir.
        self.c.setAuthor(mb.AUTHOR)
        self.c.setSubject(mb._CFG["project"]["subtitle"])

        self.page = 0                 # basılmış sayfa sayısı
        self.issues: list[str] = []
        self.sections: list[dict] = []
        self.placed_images: list[dict] = []
        self.blanks: list[dict] = []
        self.folio_pages = 0

    # --- geometri ---------------------------------------------------------

    @property
    def is_recto(self) -> bool:
        """Bir sonraki basılacak sayfa tek mi (sağ sayfa)."""
        return (self.page + 1) % 2 == 1

    def left_margin(self) -> float:
        """Aynalı: tek sayfada iç marj SOLDA, çift sayfada dışta."""
        return (self.gutter if self.is_recto else self.t.margin_outer_in) * 72

    def top_y(self) -> float:
        return (self.ed.trim_h_in - self.t.margin_top_in) * 72

    def bottom_y(self) -> float:
        return self.t.margin_bottom_in * 72

    # --- sayfa akışı ------------------------------------------------------

    def new_page(self, folio: bool = True, section: str | None = None) -> None:
        if self.page:
            self.c.showPage()
        self.page += 1
        # ⚠ HER SAYFA GÖMÜLÜ FONTLA AÇILIR.
        # reportlab yeni sayfayı Helvetica ile başlatır ve o font base-14'tür:
        # PDF'e GÖMÜLMEZ. Hiçbir şey çizilmese bile sayfa kaynaklarına yazılır
        # ve `pdffonts` onu "emb: no" olarak listeler — KDP'nin "gömülü olmayan
        # font: 0" şartını tek satır çizmeden ihlal eder. İlk gerçek bulgu
        # buydu: 235 sayfalık PDF'te Helvetica duruyordu.
        self.c.setFont(FONT_BODY, self.t.body_pt)
        self.x = self.left_margin()
        self.y = self.top_y()
        self.avail = self.lines_per_page
        self._folio = folio
        if folio:
            self.folio_pages += 1
        if section:
            self.sections.append({"section": section, "page": self.page})

    def _draw_folio(self) -> None:
        if not getattr(self, "_folio", False):
            return
        self.c.setFont(FONT_BODY, 9)
        label = str(self.page)
        w = self.c.stringWidth(label, FONT_BODY, 9)
        cx = self.left_margin() + (self.width - w) / 2
        self.c.drawString(cx, self.t.margin_bottom_in * 72 - 22, label)

    def finish_page(self) -> None:
        self._draw_folio()

    def blank(self, count: int = 1, reason: str = "spacer") -> None:
        for _ in range(count):
            self.new_page(folio=False)
            self.blanks.append({"page": self.page, "reason": reason})
            self.finish_page()

    def to_recto(self, reason: str = "recto-start") -> None:
        """
        Kitap konvansiyonu: bölüm ve önemli açılışlar TEK sayfada başlar.

        ⚠ BU SAYFALAR MODELDE YOKTUR. `page_budget` bileşenleri sayar
        (ön madde · bölüm · kart · gövde · arka madde) ama "sağ sayfada
        başla" kuralının ürettiği boş sayfaları saymaz. Gerçek dizgide
        varlar ve SAYFA SAYISINA GİRERLER — yani fiyat modeline de. Sayıları
        rapora ayrı satır olarak yazılır ki model ile gerçek arasındaki fark
        tahmin değil ÖLÇÜ olsun.
        """
        if not self.is_recto:
            self.blank(reason=reason)

    # --- metin ------------------------------------------------------------

    def wrap(self, text: str, font: str, size: float,
             width: float | None = None, indent: float = 12.0) -> list[tuple[str, bool]]:
        from reportlab.pdfbase.pdfmetrics import stringWidth
        maxw = width if width is not None else self.width
        out: list[tuple[str, bool]] = []
        for para in mb.paragraphs(text):
            cur, first = "", True
            avail = maxw - indent
            for word in para.split():
                trial = word if not cur else cur + " " + word
                if stringWidth(trial, font, size) <= avail:
                    cur = trial
                else:
                    out.append((cur, first))
                    first = False
                    avail = maxw
                    cur = word
            if cur:
                out.append((cur, first))
        return out

    def line(self, text: str, font: str, size: float,
             indent: float = 0.0, align: str = "left") -> None:
        if self.avail <= 0:
            self.finish_page()
            self.new_page()
        if text:
            self.c.setFont(font, size)
            if align == "center":
                w = self.c.stringWidth(text, font, size)
                self.c.drawString(self.x + (self.width - w) / 2, self.y, text)
            else:
                self.c.drawString(self.x + indent, self.y, text)
        self.y -= self.lead
        self.avail -= 1

    def flow(self, lines: list[tuple[str, bool]], font: str, size: float,
             indent: float = 12.0, widow_control: bool = True) -> None:
        """
        Satırları dök. DUL/YETİM DENETİMİ (§ 20):
          · yetim = paragrafın İLK satırı sayfanın SON satırı olamaz
          · dul   = paragrafın SON satırı sayfanın TEK satırı olamaz
        İkisi de satırı bir sonraki sayfaya İTEREK çözülür; metne dokunulmaz.
        """
        i = 0
        while i < len(lines):
            text, first = lines[i]
            if widow_control and self.avail == 1 and first and i + 1 < len(lines):
                # yetim: tek başına kalacak ilk satırı it
                self.line("", font, size)
                continue
            if widow_control and self.avail == 1 and i + 1 < len(lines) \
                    and lines[i + 1][1] is False and i + 2 == len(lines):
                # bir sonraki sayfada tek başına kalacak son satır — bunu da it
                self.line("", font, size)
                continue
            self.line(text, font, size, indent=indent if first else 0.0)
            i += 1

    # --- görsel -----------------------------------------------------------

    def image(self, image_id: str, box_w_pt: float, box_h_pt: float,
              y_top: float, kind: str, valign: str = "center") -> dict:
        """
        Görseli kutuya SIĞDIRARAK yerleştirir — asla esnetmez, asla kırpmaz.

        Kutuda İKİ EKSENDE DE ORTALANIR. Üste yaslamak, oranı şartnameden
        dar gelen bir görselde kutunun altında ölü bir bant bırakıyordu:
        ilk prova sayfasında çizim ile başlık arasında 1,5 inçlik boşluk
        vardı ve sayfa "bozuk" görünüyordu. Ortalama, kutuyu şartnameye uyan
        görselde AYNI bırakır (dolduran görselde ortalama = yaslama) ve
        uymayanda kabul edilebilir kılar.
        """
        from reportlab.lib.utils import ImageReader
        path = os.path.join(PRINT_DIR, f"{image_id}.tif")
        rec = {"id": image_id, "kind": kind, "page": self.page + 1,
               "present": os.path.exists(path)}
        if not rec["present"]:
            self.issues.append(f"{image_id}: baskı türevi yok ({path})")
            return rec

        from PIL import Image as PILImage
        with PILImage.open(path) as im:
            iw, ih = im.size
        scale = min(box_w_pt / iw, box_h_pt / ih)
        dw, dh = iw * scale, ih * scale
        dx = self.x + (box_w_pt - dw) / 2
        dy = y_top - dh if valign == "top" else y_top - dh - (box_h_pt - dh) / 2
        self.c.drawImage(ImageReader(path), dx, dy, width=dw, height=dh,
                         preserveAspectRatio=True, anchor="n", mask=None)

        # ⚠ GERÇEK ÇÖZÜNÜRLÜK TÜREVİN DEĞİL, HAMIN PİKSELİYLE ÖLÇÜLÜR.
        #
        # Baskı TIFF'i 3000×2000'dir ve 4,875 inçe basılınca 615 dpi çıkar —
        # ama o piksellerin bir kısmı HAT TARAFINDAN ÜRETİLDİ: ham dosya
        # 1024 px genişliğindeydi ve büyütüldü. Büyütme bilgi eklemez.
        # 615 dpi yazmak "600 dpi şartı tutuyor" demek olurdu ve bu YANLIŞ
        # OLURDU. Aşağıdaki sayı hamın kendi pikselini basılan inçe böler:
        # kâğıda gerçekten düşen bilgi budur.
        raw_px = _raw_pixel_width(image_id)
        art_w_in = (dw / 72) * (_art_share(image_id, iw) or 1.0)
        rec.update({
            "pxWidth": iw, "pxHeight": ih,
            "rawPxWidth": raw_px,
            "drawnWidthIn": round(dw / 72, 4), "drawnHeightIn": round(dh / 72, 4),
            "artWidthIn": round(art_w_in, 4),
            "derivativeDpi": round(iw / (dw / 72), 1) if dw else 0,
            "opticalDpi": round(raw_px / art_w_in, 1) if (raw_px and art_w_in) else None,
            "boxWidthIn": round(box_w_pt / 72, 4),
            "boxHeightIn": round(box_h_pt / 72, 4),
            "boxFillPct": round(100 * (dw * dh) / (box_w_pt * box_h_pt), 1),
            # Kutuya sığdı mı: taşma yoksa kırpılma da yoktur.
            "clipped": bool(dw > box_w_pt + 0.5 or dh > box_h_pt + 0.5),
        })
        self.placed_images.append(rec)
        if rec["clipped"]:
            self.issues.append(f"{image_id}: görsel kutusundan taştı")
        return rec

    def save(self) -> None:
        """
        Son sayfayı AÇIKÇA kapat. reportlab tamamen boş bir sayfayı `save()`
        sırasında yutuyor: iç sayaç 236 derken PDF 235 sayfa çıkıyordu ve
        tek/çift denetimi yanlış sayı üzerinde çalışıyordu. Sayfa sayısı
        fiyat modelidir; bir sayfalık sapma ölçülmeden geçemez.
        """
        self.finish_page()
        self.c.showPage()
        self.c.save()


# =============================================================================
# BÖLÜMLER
# =============================================================================

def front_matter(b: Interior, cfg: dict) -> None:
    p = cfg["project"]

    # ① yarım başlık
    b.new_page(folio=False, section="half-title")
    b.y = b.top_y() - 2.2 * 72
    b.line(p["title"].upper(), FONT_BOLD, 20, align="center")
    b.finish_page()

    # ② boş
    b.blank()

    # ③ başlık sayfası
    b.new_page(folio=False, section="title-page")
    b.y = b.top_y() - 1.6 * 72
    b.line(p["title"].upper(), FONT_BOLD, 26, align="center")
    b.line("", FONT_BODY, 12)
    for ln in b.wrap(p["subtitle"], FONT_ITALIC, 12, indent=0):
        b.line(ln[0], FONT_ITALIC, 12, align="center")
    b.finish_page()

    # ④ künye
    b.new_page(folio=False, section="copyright")
    b.y = b.top_y() + 0.0
    lines = [
        p["title"],
        p["subtitle"],
        "",
        f"Series: {p['series']}",
        "",
        "All rights reserved. No part of this book may be reproduced in any "
        "form without written permission from the publisher.",
        "",
        "The retellings in this book are original prose. Sources for every "
        "story are listed in the back matter.",
        "",
        "Australian Aboriginal traditions are deliberately not included in "
        "this book. Those stories are held by their communities, and who may "
        "tell them is decided by rule, not by preference.",
        "",
        "ISBN: [PENDING — publisher decision]",
        "",
        "AI disclosure: see the note in the back matter.",
    ]
    for text in lines:
        if not text:
            b.line("", FONT_BODY, 9)
            continue
        for ln, first in b.wrap(text, FONT_BODY, 9, indent=0):
            b.line(ln, FONT_BODY, 9)
    b.finish_page()

    # ⑤ ithaf
    b.new_page(folio=False, section="dedication")
    b.y = b.top_y() - 2.6 * 72
    b.line("For every reader who finished the Greek book", FONT_ITALIC, 12,
           align="center")
    b.line("and asked what else there was.", FONT_ITALIC, 12, align="center")
    b.finish_page()

    # ⑥ boş
    b.blank()

    # ⑦ içindekiler (3 sayfa)
    b.to_recto()
    contents_pages(b)

    # ⑧ dünya haritası — açık sayfa (2)
    world_map(b)

    # ⑨ giriş (3)
    b.to_recto()
    introduction(b)


def contents_pages(b: Interior) -> None:
    idx = mb.load_stories()
    parts = sorted(idx.get("parts", []), key=lambda x: x.get("order") or 99)
    by_part: dict[str, list] = {}
    for s in idx.get("stories", []):
        if s.get("status") == "candidate" or not s.get("number"):
            continue
        by_part.setdefault(s.get("partId"), []).append(s)

    b.new_page(section="contents")
    b.line("CONTENTS", FONT_BOLD, 16, align="center")
    b.line("", FONT_BODY, 12)
    for part in parts:
        if b.avail < 4:
            b.finish_page()
            b.new_page()
        b.line(part["title"].upper(), FONT_BOLD, 11)
        for s in sorted(by_part.get(part["id"], []), key=lambda x: x["number"]):
            if b.avail < 2:
                b.finish_page()
                b.new_page()
            b.line(f"{s['number']}.  {s['title']}", FONT_BODY, 10, indent=14)
        b.line("", FONT_BODY, 10)
    for label in ("Say These Names", "Who's Who", "Where the Stories Come From",
                  "About the Author"):
        if b.avail < 2:
            b.finish_page()
            b.new_page()
        b.line(label, FONT_BOLD, 11)
    b.finish_page()


# Haritanın çizili kapsamı. Üretici tam bir eş-dikdörtgen izdüşüm vermez;
# bu iki bant, çizilen haritanın gerçekten kapladığı enlem/boylam aralığıdır
# ve işaretler ona göre yerleşir. Değerler basılı sayfaya bakılarak
# doğrulanmıştır — tahmin değil, ayar.
MAP_LON = (-180.0, 180.0)
MAP_LAT = (83.0, -58.0)          # üst kenar · alt kenar


def map_markers(b: Interior, placed: dict) -> None:
    """
    22 kültürün konumunu haritaya CLI ile işaretler.

    ⚠ İŞARETLERİ ÜRETİCİ KOYAMAZ (imagespec/make_prompts § harita notu).
    İlk teslimatta koymuştu ve beşi kitapta olmayan kültürlerdi — biri de
    yol haritasının KASITLI DIŞARIDA BIRAKTIĞI Aborjin geleneğiydi. Doğru
    cevap zaten depoda: `culture_index.json → mapPoint` her kilitli kültür
    için enlem/boylam taşıyor. Numaralar karşı sayfadaki anahtarla birebir
    aynı sırayı kullanır (ada göre alfabetik), yani iki liste ayrışamaz.
    """
    if not placed.get("present"):
        return
    dw = placed["drawnWidthIn"] * 72
    dh = placed["drawnHeightIn"] * 72
    x0 = b.x + (b.width - dw) / 2
    y_top = b.y

    # ⚠ İZDÜŞÜM, ÇERÇEVEYE DEĞİL, ÇİZİMİN KENDİSİNE OTURTULUR.
    # Harita dosyası kenarlarında beyaz pay taşıyor; kıtalar çerçevenin
    # tamamını doldurmuyor. Boylamı çerçeveye göre hesaplamak işaretleri
    # kaydırıyordu (Mısır Levant'a, Zulu okyanusa düşüyordu). Mürekkebin
    # sınırlayıcı kutusu ölçülür ve izdüşüm ONUN üstüne kurulur — böylece
    # harita yeniden üretilse ve payı değişse bile işaretler kendiliğinden
    # doğru yere gider.
    from PIL import Image as PILImage, ImageChops
    src = os.path.join(PRINT_DIR, "map-001.tif")
    try:
        with PILImage.open(src) as mim:
            g = mim.convert("L")
            ink = ImageChops.invert(g.point(lambda v: 0 if v < 240 else 255,
                                            mode="L"))
            bb = ink.getbbox()
            iw, ih = g.size
    except OSError:
        bb, iw, ih = None, 1, 1
    if bb:
        x0 += dw * (bb[0] / iw)
        y_top -= dh * (bb[1] / ih)
        dw *= (bb[2] - bb[0]) / iw
        dh *= (bb[3] - bb[1]) / ih

    cultures = [c for c in mb.load_cultures().get("cultures", [])
                if c.get("status") == "locked"]
    cultures.sort(key=lambda c: c["name"])
    lon0, lon1 = MAP_LON
    lat0, lat1 = MAP_LAT
    for i, c in enumerate(cultures, 1):
        mp = c.get("mapPoint") or {}
        if "lat" not in mp or "lon" not in mp:
            b.issues.append(f"{c['id']}: mapPoint yok — harita işareti konamadı")
            continue
        fx = (mp["lon"] - lon0) / (lon1 - lon0)
        fy = (lat0 - mp["lat"]) / (lat0 - lat1)
        fx = min(max(fx, 0.0), 1.0)
        fy = min(max(fy, 0.0), 1.0)
        px = x0 + fx * dw
        py = y_top - fy * dh
        r = 5.0
        b.c.setLineWidth(0.6)
        b.c.circle(px, py, r, stroke=1, fill=1)
        b.c.setFillGray(1.0)
        b.c.setFont(FONT_BOLD, 6)
        label = str(i)
        w = b.c.stringWidth(label, FONT_BOLD, 6)
        b.c.drawString(px - w / 2, py - 2.1, label)
        b.c.setFillGray(0.0)


def world_map(b: Interior) -> None:
    """
    Dünya haritası AÇIK SAYFADIR (page_budget: front_world_map = 2).
    Taşma YOKTUR: her yarı kendi metin bloğuna yerleşir, iç kenarlar cilt
    payında buluşur. Görsel ikiye BÖLÜNMEZ — tek görsel iki sayfaya yayılırsa
    ciltte ortası kaybolur; onun yerine harita SOL sayfaya tam yerleşir ve
    SAĞ sayfa efsane/anahtar taşır.
    """
    # sol (çift) sayfada başlasın ki açık sayfa gerçekten açık olsun
    if b.is_recto:
        b.blank()
    b.new_page(section="world-map")
    b.line("WHERE THE STORIES COME FROM", FONT_BOLD, 13)
    b.line("", FONT_BODY, 10)
    box_h = (b.ed.trim_h_in - b.t.margin_top_in - b.t.margin_bottom_in) * 72 - 3 * b.lead
    placed = b.image("map-001", b.width, box_h, b.y, "map", valign="top")
    map_markers(b, placed)
    b.avail = 0
    b.finish_page()

    b.new_page()
    b.line("THE TWENTY-TWO CULTURES", FONT_BOLD, 13)
    b.line("", FONT_BODY, 10)
    cultures = [c for c in mb.load_cultures().get("cultures", [])
                if c.get("status") == "locked"]
    cultures.sort(key=lambda c: c["name"])
    half = -(-len(cultures) // 2)
    col_w = b.width / 2 - 10
    from reportlab.pdfbase.pdfmetrics import stringWidth
    y0 = b.y
    for col in range(2):
        b.y = y0
        chunk = cultures[col * half:(col + 1) * half]
        cx = b.x + col * (b.width / 2)
        for j, c in enumerate(chunk):
            n = col * half + j + 1          # haritadaki numarayla AYNI sıra
            b.c.setFont(FONT_BOLD, 9)
            b.c.drawString(cx, b.y, f"{n}.")
            b.c.setFont(FONT_BODY, 10)
            b.c.drawString(cx + 15, b.y, c["name"])
            b.c.setFont(FONT_ITALIC, 9)
            reg = (c.get("macroRegion") or c.get("region") or "").replace("-", " ")
            w = stringWidth(reg, FONT_ITALIC, 9)
            if w < col_w - 15:
                b.c.drawString(cx + col_w - w, b.y, reg)
            b.y -= b.lead
    b.avail = 0
    b.finish_page()


def introduction(b: Interior) -> None:
    b.new_page(section="introduction")
    b.line("BEFORE YOU START", FONT_BOLD, 16)
    b.line("", FONT_BODY, 12)
    text = (
        "Most books of myths for young readers are Greek books. This one is "
        "not. Greek stories are here — three of them — but so are stories "
        "from twenty-one other places, and none of them is a footnote to the "
        "Greek ones.\n\n"
        "Every story in this book is a retelling. That means somebody, a long "
        "time ago, told it out loud, and somebody else wrote it down, and now "
        "it has been written again for you. Along the way people changed "
        "things. Where the tellers disagree about what happened, this book "
        "picks one version and says so rather than pretending there was only "
        "ever one.\n\n"
        "Some of these stories are still told today by people who hold them "
        "as their own. Where that is true, the culture card at the start of "
        "the section says who tells them and where. A few things those "
        "communities keep private are not in this book, and that is on "
        "purpose.\n\n"
        "Names that look hard are not hard. At the back there is a guide that "
        "tells you how to say every one of them, and a Who's Who if you lose "
        "track of a god. The map at the front shows where each tradition "
        "lives.\n\n"
        "Nothing here has been made gentler than it is. Some of these stories "
        "end badly for people who did not deserve it. That is what the "
        "stories say, and changing it would be a different kind of lie."
    )
    b.flow(b.wrap(text, FONT_BODY, 11), FONT_BODY, 11)
    b.finish_page()


def part_opener(b: Interior, part: dict) -> None:
    """Bölüm açılışı: 2 sayfa (page_budget: pages_per_part_opener)."""
    b.to_recto()
    b.new_page(folio=False, section=f"part:{part['id']}")
    b.y = b.top_y() - 2.0 * 72
    for ln, _ in b.wrap(part["title"].upper(), FONT_BOLD, 18, indent=0):
        b.line(ln, FONT_BOLD, 18, align="center")
    if part.get("epigraph"):
        b.line("", FONT_BODY, 11)
        for ln, _ in b.wrap(part["epigraph"], FONT_ITALIC, 11,
                            width=b.width * 0.8, indent=0):
            b.line(ln, FONT_ITALIC, 11, align="center")
    b.finish_page()
    b.blank()


def culture_card(b: Interior, culture: dict, own_page: bool,
                 story_start: int | None = None) -> dict:
    """
    Kültür kartı: vinyet + üç cümle. K30 beş kültüre KENDİ SAYFASINI verir;
    kalan on yedisi hikâye kuyruğundaki ÖDENMİŞ boşlukta durur (K27).
    """
    ct = culture.get("cardText") or {}
    vignette = culture.get("vignetteId")
    rec = {"cultureId": culture["id"], "ownPage": own_page, "page": None,
           "vignette": vignette, "fits": None}

    sentences = " ".join(ct.get(k, "") for k in ("whoTells", "where", "today")).strip()
    heading = f"{culture['name']} — {ct.get('language', '')}".strip(" —")

    vign_lines = pb.MODEL["culture_card_vignette_lines"]
    need = (vign_lines + pb.MODEL["culture_card_gap_lines"]
            + len(b.wrap(heading, FONT_BOLD, 11, indent=0))
            + len(b.wrap(sentences, FONT_BODY, 10, indent=0)))

    if own_page:
        b.new_page(section=f"card:{culture['id']}")
        rec["fits"] = True
    else:
        # ⚠ DOĞRU PAYDA "KULLANILAN SAYFADA KALAN SATIR" DEĞİL, "FATURALANAN
        # KAPASİTE"DİR — Faz 4'ün kendi düzeltmesi (proof_interior.py § 223).
        # K27'nin bütün argümanı "boşluk ZATEN ÖDENİYOR" üzerine kuruludur:
        # hikâye 3 sayfada bitse de model 4 sayfa faturalar, yani dördüncü
        # sayfa kartın hakkıdır. Kartın oraya AKMASI kusur DEĞİLDİR; kusur,
        # kartın hikâyeyi FATURALANAN sayfa sayısının ÖTESİNE taşımasıdır.
        billed = billed_pages_per_story()
        rec["flowedToNextPage"] = b.avail < need
        if b.avail < need:
            b.new_page()
        else:
            b.line("", FONT_BODY, 10)
        used = (b.page - story_start + 1) if story_start else 1
        rec["storyPagesWithCard"] = used
        rec["billedPages"] = billed
        rec["fits"] = used <= billed
        if not rec["fits"]:
            b.issues.append(
                f"{culture['id']}: kültür kartı hikâyeyi faturalanan "
                f"{billed} sayfanın ötesine taşıdı ({used} sayfa) — K27/K30")

    rec["page"] = b.page
    # KENDİ SAYFASINDAKİ KART DAHA BÜYÜK VİNYET TAŞIR.
    # K30 o beş kültüre TAM SAYFA verdi; vinyeti kuyruk ölçüsünde (10 satır)
    # bırakmak sayfanın üçte ikisini boş bırakıyordu — ödenmiş bir sayfayı
    # boş basmak, K30'un bedelini ikinci kez ödemektir. Kuyruktaki kartlar
    # 10 satırda KALIR: orada boşluk gerçekten kıt.
    lines_for_vignette = 18 if own_page else vign_lines
    if own_page:
        # blok sayfada dikey ortalansın
        block = (lines_for_vignette + 2
                 + len(b.wrap(heading, FONT_BOLD, 13, indent=0))
                 + len(b.wrap(sentences, FONT_BODY, 11, indent=0)))
        pad = max(0, (b.lines_per_page - block) // 2)
        for _ in range(pad):
            b.line("", FONT_BODY, 11)

    box_h = lines_for_vignette * b.lead
    if vignette:
        b.image(vignette, b.width, box_h, b.y, "culture")
    b.y -= box_h
    b.avail -= lines_for_vignette
    b.line("", FONT_BODY, 10)
    if own_page:
        b.line(heading, FONT_BOLD, 13, align="center")
        b.line("", FONT_BODY, 11)
        b.flow(b.wrap(sentences, FONT_BODY, 11), FONT_BODY, 11, indent=0)
    else:
        b.line(heading, FONT_BOLD, 11)
        b.flow(b.wrap(sentences, FONT_BODY, 10), FONT_BODY, 10, indent=0)
    return rec


def story_page(b: Interior, s: dict, rec: dict) -> dict:
    """Her hikâye YENİ SAYFADA başlar; açılış çizimi sayfanın ÜST YARISINDA."""
    b.new_page(section=f"story:{rec['id']}")
    start = b.page

    illo_lines = int(b.lines_per_page * pb.MODEL["opening_illustration_page_share"])
    box_h = illo_lines * b.lead
    img = b.image(rec.get("imageId"), b.width, box_h, b.y, "story") \
        if rec.get("imageId") else None
    if not rec.get("imageId"):
        b.issues.append(f"{rec['id']}: imageId yok")
    b.y -= box_h
    b.avail -= illo_lines

    b.line("", FONT_BODY, 12)
    title_lines = b.wrap(s["title"], FONT_BOLD, 16, indent=0)
    if len(title_lines) > 2:
        b.issues.append(f"{rec['id']}: başlık {len(title_lines)} satır")
    for ln, _ in title_lines:
        b.line(ln, FONT_BOLD, 16)
    b.line("", FONT_BODY, 12)

    b.flow(b.wrap(s.get("text", ""), FONT_BODY, b.t.body_pt),
           FONT_BODY, b.t.body_pt)

    note = (s.get("culturalNote") or "").strip()
    if note:
        if b.avail < 4:
            b.finish_page()
            b.new_page()
        b.line("", FONT_BODY, 10)
        b.flow(b.wrap(note, FONT_ITALIC, 10, width=b.width * 0.9),
               FONT_ITALIC, 10, indent=0)

    return {"id": rec["id"], "number": rec.get("number"),
            "startPage": start, "endPage": b.page,
            "pages": b.page - start + 1,
            "words": mb.word_count(s.get("text", "")),
            "image": img, "tailLinesFree": max(0, b.avail)}


def back_matter(b: Interior) -> None:
    idx = mb.load_stories()
    entries = [s for s in idx.get("stories", [])
               if s.get("status") not in ("dropped", "candidate") and s.get("number")]

    def key(n: str) -> str:
        return mb.strip_diacritics(n).lower()

    # --- telaffuz ---
    b.to_recto()
    b.new_page(section="pronunciation")
    b.line("SAY THESE NAMES", FONT_BOLD, 16)
    b.line("", FONT_BODY, 11)
    b.flow(b.wrap("Nobody will mind if you say a name your own way. "
                  "But if you would like to say it the way the story's own "
                  "people say it, here is how.", FONT_ITALIC, 10),
           FONT_ITALIC, 10, indent=0)
    b.line("", FONT_BODY, 11)
    seen, pron = set(), []
    for s in entries:
        for e in s.get("pronunciationEntries") or []:
            if e["name"] in seen:
                continue
            seen.add(e["name"])
            pron.append(e)
    for e in sorted(pron, key=lambda x: key(x["name"])):
        if b.avail < 2:
            b.finish_page()
            b.new_page()
        b.c.setFont(FONT_BOLD, 10)
        b.c.drawString(b.x, b.y, e["name"])
        w = b.c.stringWidth(e["name"] + "   ", FONT_BOLD, 10)
        b.c.setFont(FONT_BODY, 10)
        b.c.drawString(b.x + w, b.y, e.get("pronunciation", ""))
        b.y -= b.lead
        b.avail -= 1
    b.finish_page()

    # --- kim kimdir ---
    b.to_recto()
    b.new_page(section="whos-who")
    b.line("WHO'S WHO", FONT_BOLD, 16)
    b.line("", FONT_BODY, 11)
    seen, who = set(), []
    for s in entries:
        for ch in s.get("characters") or []:
            if not ch.get("glossary") or ch["name"] in seen:
                continue
            seen.add(ch["name"])
            who.append(ch)
    for ch in sorted(who, key=lambda x: key(x["name"])):
        need = 1 + len(b.wrap(ch.get("role", ""), FONT_BODY, 10, indent=0))
        if b.avail < need + 1:
            b.finish_page()
            b.new_page()
        b.line(ch["name"], FONT_BOLD, 10)
        b.flow(b.wrap(ch.get("role", ""), FONT_BODY, 10), FONT_BODY, 10, indent=14)
    b.finish_page()

    # --- kültürel notlar / kaynaklar ---
    b.to_recto()
    b.new_page(section="cultural-notes")
    b.line("WHERE THE STORIES COME FROM", FONT_BOLD, 16)
    b.line("", FONT_BODY, 11)
    cmap = mb.culture_by_id(mb.load_cultures())
    for s in sorted(entries, key=lambda x: x["number"]):
        srcs = [src for src in s.get("sources", [])
                if src.get("kind") not in ("index", "retelling")]
        line = f"{s['number']}. {s['title']} — {cmap.get(s['cultureId'], {}).get('name', '')}"
        body = "; ".join(src.get("citation", "")[:120] for src in srcs[:2])
        need = 1 + len(b.wrap(body, FONT_BODY, 9, indent=0))
        if b.avail < need + 1:
            b.finish_page()
            b.new_page()
        b.line(line, FONT_BOLD, 9)
        b.flow(b.wrap(body, FONT_BODY, 9), FONT_BODY, 9, indent=12)
    b.finish_page()

    # --- yazar · teşekkür · AI beyanı · QR ---
    b.to_recto()
    b.new_page(section="about-author")
    b.line("ABOUT THE AUTHOR", FONT_BOLD, 16)
    b.line("", FONT_BODY, 11)
    b.flow(b.wrap("[AUTHOR BIO — founder copy pending]", FONT_BODY, 11),
           FONT_BODY, 11)
    b.finish_page()

    b.new_page(section="acknowledgements")
    b.line("A NOTE ON HOW THIS BOOK WAS MADE", FONT_BOLD, 14)
    b.line("", FONT_BODY, 11)
    b.flow(b.wrap(
        "Every story here was researched from published scholarship and "
        "primary collections; the two most important sources for each story "
        "are listed a few pages back. Retellings by other authors were not "
        "used as sources.\n\n"
        "Artificial intelligence tools were used in producing this book. "
        "The specific disclosure required by the retailer is filed with the "
        "publication record.", FONT_BODY, 10), FONT_BODY, 10)
    b.finish_page()

    b.new_page(section="qr")
    b.line("THE MAP, FULL SIZE", FONT_BOLD, 14)
    b.line("", FONT_BODY, 11)
    b.flow(b.wrap("A printable copy of the twenty-two-culture map is "
                  "available online. [QR CODE — Phase 6]", FONT_BODY, 11),
           FONT_BODY, 11)
    b.finish_page()


# =============================================================================
# TAM İÇ BLOK
# =============================================================================

def build(edition_key: str) -> dict:
    cfg = mb._CFG
    book = mb.load_book()
    if not book:
        return {}
    prose = mb.book_stories(book)
    idx = mb.load_stories()
    by_id = {s["id"]: s for s in idx.get("stories", [])}
    parts = sorted(idx.get("parts", []), key=lambda x: x.get("order") or 99)
    cultures = {c["id"]: c for c in mb.load_cultures().get("cultures", [])
                if c.get("status") == "locked"}

    b = Interior(edition_key, mb.PAGE_TARGET)
    front_matter(b, cfg)

    written = sorted(prose.items(),
                     key=lambda kv: by_id.get(kv[0], {}).get("number") or 999)
    # Kültür kartı, o kültürün İLK hikâyesinde durur.
    first_of_culture: dict[str, str] = {}
    for sid, _ in written:
        cid = by_id.get(sid, {}).get("cultureId")
        if cid and cid not in first_of_culture:
            first_of_culture[cid] = sid
    card_host = {v: k for k, v in first_of_culture.items()}

    per_story, cards = [], []
    for part in parts:
        part_opener(b, part)
        for sid, s in written:
            rec = by_id.get(sid, {})
            if rec.get("partId") != part["id"]:
                continue
            cid = card_host.get(sid)
            # K30: kendi sayfası olan kart hikâyeden ÖNCE gelir — kültürü tanıtır.
            if cid and cultures.get(cid, {}).get("cardOwnPage"):
                cards.append(culture_card(b, cultures[cid], own_page=True))
            info = story_page(b, s, rec)
            if cid and not cultures.get(cid, {}).get("cardOwnPage"):
                cards.append(culture_card(b, cultures[cid], own_page=False,
                                          story_start=info["startPage"]))
            info["pages"] = b.page - info["startPage"] + 1
            per_story.append(info)

    body_end = b.page
    back_matter(b)

    # Matbaa imzası ÇİFT sayfada çalışır: tek sayfa sayısı gönderilirse
    # KDP arkaya kendi boş sayfasını ekler ve son sayfa kontrolü bizde olmaz.
    if b.page % 2 == 1:
        b.blank(reason="even-page-parity")
    b.save()

    # --- MODEL ↔ GERÇEK UZLAŞTIRMASI ---
    # Fark tahmin edilmez, KALEM KALEM ÇIKARILIR. `page_budget` beş bileşen
    # sayar; gerçek dizgide ayrıca "sağ sayfada başla" boşlukları ve tek/çift
    # tamamlaması vardır ve modelin onlar için satırı YOKTUR.
    model = pb.compute(calibrated_wpp())
    story_pages = sum(p["pages"] for p in per_story)
    card_own = sum(1 for c in cards if c["ownPage"])
    front_pages = next((s["page"] for s in b.sections
                        if s["section"].startswith("part:")), 1) - 1
    back_pages = b.page - body_end
    reconciliation = {
        "modelTotal": model["total"],
        "actualTotal": b.page,
        "delta": b.page - model["total"],
        "components": {
            "front": {"model": model["front"], "actual": front_pages},
            "partOpeners": {"model": model["partOpeners"],
                            "actual": 6 * pb.MODEL["pages_per_part_opener"]},
            "cultureCardsOwnPage": {"model": model["cultureCards"], "actual": card_own},
            "storyBody": {"model": model["body"], "actual": story_pages},
            "back": {"model": model["back"], "actual": back_pages},
        },
        "blankPagesNotInModel": len(b.blanks),
        "blanksByReason": {
            reason: sum(1 for x in b.blanks if x["reason"] == reason)
            for reason in sorted({x["reason"] for x in b.blanks})
        },
    }

    return {
        "edition": edition_key,
        "pdf": os.path.relpath(b.out_pdf, mb.ROOT),
        "totalPages": b.page,
        "bodyEndPage": body_end,
        "reconciliation": reconciliation,
        "blanks": b.blanks,
        "geometry": {
            "trimIn": [b.ed.trim_w_in, b.ed.trim_h_in],
            "textBlockIn": [round(b.w_in, 4), round(b.h_in, 4)],
            "gutterIn": b.gutter,
            "marginOuterIn": b.t.margin_outer_in,
            "marginTopIn": b.t.margin_top_in,
            "marginBottomIn": b.t.margin_bottom_in,
            "bodyPt": b.t.body_pt, "leadingPt": b.lead,
            "linesPerPage": b.lines_per_page,
        },
        "stories": len(per_story),
        "perStory": per_story,
        "cultureCards": cards,
        "cardsOwnPage": sum(1 for c in cards if c["ownPage"]),
        "cardsInTail": sum(1 for c in cards if not c["ownPage"]),
        "cardsThatDidNotFit": [c["cultureId"] for c in cards if c["fits"] is False],
        "imagesPlaced": len(b.placed_images),
        "imagesMissing": [i["id"] for i in b.placed_images if not i["present"]],
        "sections": b.sections,
        "issues": b.issues,
    }


# =============================================================================
# ÜRETİLMİŞ PDF'İN DENETİMİ — belge ayarına değil, ÇIKTIYA bakar
# =============================================================================
# Talimat § 21: "Yalnızca CSS/belge ayarlarına güvenmeyin. İŞLENMİŞ SAYFALARI
# ÖLÇÜN." Aşağısı tam olarak bunu yapar: PDF'i dışarıdan okur (poppler) ve
# sayfaları gerçekten RASTERİZE EDİP (ghostscript) mürekkebin nerede
# durduğunu ölçer. Belge ayarı doğru olduğu hâlde çıktının yanlış olduğu
# durumları yalnızca bu yakalar.

def _run(cmd: list[str]) -> str | None:
    import subprocess
    try:
        return subprocess.run(cmd, capture_output=True, text=True,
                              timeout=600, check=True).stdout
    except (FileNotFoundError, subprocess.CalledProcessError,
            subprocess.TimeoutExpired):
        return None


def pdf_facts(path: str) -> dict:
    """pdfinfo + pdffonts — dışarıdan bakan bir göz."""
    facts: dict = {"tool": None}
    info = _run(["pdfinfo", path])
    if info is None:
        return facts
    facts["tool"] = "poppler"
    for line in info.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        k, v = k.strip(), v.strip()
        if k == "Pages":
            facts["pages"] = int(v)
        elif k == "Page size":
            facts["pageSize"] = v
            try:
                w, h = v.split("x")[0].strip(), v.split("x")[1].split("pts")[0].strip()
                facts["widthPt"], facts["heightPt"] = float(w), float(h)
            except (ValueError, IndexError):
                pass
        elif k == "File size":
            facts["fileBytes"] = int(v.split()[0])
        elif k == "PDF version":
            facts["pdfVersion"] = v

    fonts = _run(["pdffonts", path])
    facts["fonts"] = []
    if fonts:
        for line in fonts.splitlines()[2:]:
            if not line.strip():
                continue
            parts = line.split()
            if len(parts) < 6:
                continue
            facts["fonts"].append({"name": parts[0], "embedded": parts[-4] == "yes"})
    facts["notEmbedded"] = [f["name"] for f in facts["fonts"] if not f["embedded"]]
    return facts


def measure_rendered_margins(path: str, pages: list[int], trim_w: float,
                             trim_h: float, dpi: int = 72) -> list[dict]:
    """
    Sayfaları GERÇEKTEN rasterize eder ve mürekkebin trim kenarına uzaklığını
    inç olarak ölçer. Ghostscript yoksa boş liste döner (kapı ATLANMAZ,
    yalnızca bu ölçü yapılamaz ve rapora öyle yazılır).
    """
    import tempfile
    from PIL import Image, ImageChops

    out = []
    with tempfile.TemporaryDirectory() as tmp:
        for p in pages:
            png = os.path.join(tmp, f"p{p}.png")
            ok = _run(["gs", "-q", "-dNOPAUSE", "-dBATCH", "-sDEVICE=pnggray",
                       f"-r{dpi}", f"-dFirstPage={p}", f"-dLastPage={p}",
                       f"-sOutputFile={png}", path])
            if ok is None or not os.path.exists(png):
                return []
            with Image.open(png) as im:
                g = im.convert("L")
                w, h = g.size
                ink = ImageChops.invert(g.point(lambda v: 0 if v < 240 else 255,
                                                mode="L"))
                bb = ink.getbbox()
            if bb is None:
                out.append({"page": p, "blank": True})
                continue
            l, t, rgt, bot = bb
            out.append({
                "page": p, "blank": False,
                "leftIn": round(l / w * trim_w, 4),
                "rightIn": round((w - rgt) / w * trim_w, 4),
                "topIn": round(t / h * trim_h, 4),
                "bottomIn": round((h - bot) / h * trim_h, 4),
            })
    return out


# =============================================================================
# GİRİŞ NOKTASI
# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description="Üretim iç bloğu")
    ap.add_argument("--edition", default="all",
                    choices=["all", "paperback", "hardcover"])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    print("═" * 72)
    print("  ÜRETİM İÇ BLOĞU")
    print("═" * 72)

    r = mb.Result("interior", verbose=args.verbose)

    try:
        resolved = register_fonts()
    except (ImportError, FileNotFoundError) as exc:
        r.fail("font kaydedilemedi", str(exc))
        return r.finish(None)
    print("\n  gömülecek fontlar:")
    for k, v in resolved.items():
        print(f"    {k:>7}: {v}")

    keys = ["paperback", "hardcover"] if args.edition == "all" else [args.edition]
    payload = {"$comment": [
        "ÜRETİM İÇ BLOĞU RAPORU — yalnızca ÖLÇÜ içerir; tek bir hikâye",
        "cümlesi bile yoktur (K21 · Bestiarium D38). PDF depo dışındadır.",
        "Üretici: 04_BUILD/interior.py",
    ], "gate": mb.read_gate(), "fonts": resolved, "editions": {}}

    for key in keys:
        data = build(key)
        if not data:
            print("\n  manuscript yerelde yok — iç blok UYGULANAMAZ (K21).")
            r.add(os.path.exists(OUT_JSON),
                  "kayıtlı iç blok raporu depoda",
                  "interior-build.json yok — denetlenecek rapor depoda "
                  "durmuyorsa o denetim ÖLÜ KURALDIR (K18)")
            return r.finish(None)
        payload["editions"][key] = data

        lo, hi = ed_mod.PAGE_LIMITS[key]
        print(f"\n  ── {key} ──")
        print(f"     sayfa           : {data['totalPages']}")
        print(f"     gövde biter     : {data['bodyEndPage']}")
        print(f"     görsel yerleşti : {data['imagesPlaced']}")
        print(f"     kart (ayrı/kuyruk): {data['cardsOwnPage']} / {data['cardsInTail']}")

        r.add(not data["issues"], f"{key}: yapısal kusur yok",
              f"{key} KUSURLARI:\n         "
              + "\n         ".join(data["issues"][:12]))
        r.add(lo <= data["totalPages"] <= hi,
              f"{key}: sayfa sayısı KDP sınırlarında "
              f"({data['totalPages']} ∈ [{lo}, {hi}])",
              f"{key}: {data['totalPages']} sayfa KDP sınırı [{lo}, {hi}] dışında")
        r.add(data["totalPages"] % 2 == 0,
              f"{key}: sayfa sayısı çift",
              f"{key}: {data['totalPages']} TEK — matbaa çifte tamamlar")
        r.add(not data["imagesMissing"],
              f"{key}: bütün görseller yerleşti ({data['imagesPlaced']})",
              f"{key}: eksik görsel {data['imagesMissing'][:8]}")
        r.add(not data["cardsThatDidNotFit"],
              f"{key}: bütün kültür kartları yerleşti",
              f"{key}: kuyruğa sığmayan kart {data['cardsThatDidNotFit']}")
        r.add(data["cardsOwnPage"] == 5,
              f"{key}: K30 — 5 kart kendi sayfasında",
              f"{key}: K30 bozuldu — {data['cardsOwnPage']} kart ayrı sayfada, 5 olmalı")

        # --- ÜRETİLMİŞ PDF'İN KENDİSİ ---
        ed = ed_mod.get(key)
        facts = pdf_facts(os.path.join(mb.ROOT, data["pdf"]))
        data["pdf_facts"] = facts
        if facts.get("tool") is None:
            r.warn(False, f"{key}: PDF dışarıdan denetlendi",
                   "poppler yok (pdfinfo/pdffonts) — üretilmiş PDF ÖLÇÜLEMEDİ")
        else:
            r.add(facts.get("pages") == data["totalPages"],
                  f"{key}: PDF sayfa sayısı iç sayaçla aynı ({facts.get('pages')})",
                  f"{key}: PDF {facts.get('pages')} sayfa, dizgi {data['totalPages']} "
                  "diyor — sayfa sayısı fiyat modelidir, sapma geçemez")
            want_w, want_h = ed.trim_w_in * 72, ed.trim_h_in * 72
            r.add(abs(facts.get("widthPt", 0) - want_w) < 1
                  and abs(facts.get("heightPt", 0) - want_h) < 1,
                  f"{key}: sayfa ölçüsü {ed.trim_w_in}×{ed.trim_h_in} inç",
                  f"{key}: sayfa ölçüsü {facts.get('pageSize')} — "
                  f"{want_w}×{want_h} pt olmalı")
            r.add(not facts["notEmbedded"],
                  f"{key}: bütün fontlar gömülü ({len(facts['fonts'])} font)",
                  f"{key}: GÖMÜLÜ OLMAYAN FONT: {facts['notEmbedded']} — "
                  "KDP şartı 'gömülü olmayan font: 0'")
            r.add(facts.get("fileBytes", 0) < 650_000_000,
                  f"{key}: dosya boyutu KDP sınırında "
                  f"({facts.get('fileBytes', 0) / 1e6:.0f} MB < 650 MB)",
                  f"{key}: {facts.get('fileBytes', 0) / 1e6:.0f} MB > 650 MB")

        # --- MARJ: İŞLENMİŞ SAYFADAN ÖLÇÜLÜR ---
        sample = sorted({s["page"] for s in data["sections"]
                         if s["section"].startswith(("story:", "card:"))})[:8]
        sample += [data["totalPages"] - 1]
        marg = measure_rendered_margins(os.path.join(mb.ROOT, data["pdf"]),
                                        sample, ed.trim_w_in, ed.trim_h_in)
        data["renderedMargins"] = marg
        if not marg:
            r.warn(False, f"{key}: marjlar işlenmiş sayfadan ölçüldü",
                   "ghostscript yok — marj yalnızca belge ayarından biliniyor")
        else:
            inner = ed_mod.required_gutter(mb.PAGE_TARGET)
            outer_min = 0.25
            bad = []
            for m in marg:
                if m.get("blank"):
                    continue
                # tek sayfa → iç marj SOLDA, çift sayfa → SAĞDA
                in_edge = m["leftIn"] if m["page"] % 2 == 1 else m["rightIn"]
                out_edge = m["rightIn"] if m["page"] % 2 == 1 else m["leftIn"]
                if in_edge < inner - 0.01:
                    bad.append(f"s.{m['page']} iç marj {in_edge:.3f}\" < {inner}\"")
                if min(out_edge, m["topIn"], m["bottomIn"]) < outer_min:
                    bad.append(f"s.{m['page']} dış/üst/alt "
                               f"{min(out_edge, m['topIn'], m['bottomIn']):.3f}\" "
                               f"< {outer_min}\"")
            r.add(not bad,
                  f"{key}: işlenmiş sayfalarda marjlar tutuyor "
                  f"({len(marg)} sayfa ölçüldü · iç ≥{inner}\" · dış ≥{outer_min}\")",
                  f"{key}: MARJ İHLALİ:\n         " + "\n         ".join(bad[:8]))

    if args.check:
        if not os.path.exists(OUT_JSON):
            r.fail("interior-build.json yok", "`interior.py` çalıştırın")
            return r.finish(None)
        with open(OUT_JSON, encoding="utf-8") as fh:
            old = json.load(fh)
        same = all(old.get("editions", {}).get(k, {}).get("perStory")
                   == payload["editions"][k]["perStory"] for k in keys)
        r.add(same, "iç blok raporu güncel",
              "BAYAT — proza, görsel veya tipografi değişmiş")
        return r.finish(None)

    os.makedirs(mb.REPORTS_TRACKED, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"\n  ✎ {os.path.relpath(OUT_JSON, mb.ROOT)}")
    for key in keys:
        print(f"  ✎ {payload['editions'][key]['pdf']}  (DEPO DIŞINDA — proza içerir)")

    return r.finish(None)


if __name__ == "__main__":
    sys.exit(main())
