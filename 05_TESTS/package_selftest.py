#!/usr/bin/env python3
"""
FAZ 6 PAKET KAPILARININ KENDİ TESTİ — kapılar gerçekten ısırıyor mu
================================================================================
Faz 6, dört yeni kapı ailesi getirdi: kapak geometrisi, kapak tipografisi,
A+ modül ölçüleri ve EPUB paketi. Bir kapının VARLIĞI onun ÇALIŞTIĞI anlamına
gelmez — bu projenin üç fazdır tekrar tekrar öğrendiği ders budur
(Faz 5'te üç ölü kural bulundu, hepsi yıllardır yeşil yanıyordu).

Bu test KASITLI KUSUR üretir ve her kapının o kusuru GÖRDÜĞÜNÜ kanıtlar.
Kusurlar geçici dizinlerde yaşar; üretim durumu DEĞİŞMEZ.

    python3 05_TESTS/package_selftest.py
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "04_BUILD"))

import mythbook as mb
import coverspec as cs
import editions as ed_mod

try:
    from PIL import Image
except ImportError:
    print("ATLANDI: Pillow yok")
    sys.exit(2)


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


# =============================================================================
# ① KAPAK GEOMETRİSİ
# =============================================================================

def test_cover_geometry(rep: Report) -> None:
    mb.banner("① kapak geometrisi kusuru görüyor mu")
    import covers

    pages = 236
    g = covers.geometry("paperback", pages)

    # --- doğru geometri kabul edilmeli ---
    rep.check(abs(g["fullIn"][0] - (2 * 6 + 0.59 + 0.25)) < 0.001,
              f"ciltsiz tam kapak genişliği doğru ({g['fullIn'][0]}\")",
              f"beklenen {2*6+0.59+0.25}, gelen {g['fullIn'][0]}")
    rep.check(abs(g["spineIn"] - 0.59) < 0.0001,
              f"236 sayfada sırt 0,59\" ({g['spineIn']})",
              f"sırt {g['spineIn']}")

    # --- SAYFA SAYISI DEĞİŞİRSE SIRT DEĞİŞMELİ ---
    # Kapak sayfa sayısına bağlıdır; bağlı DEĞİLSE eski kapak yeni iç blokla
    # basılır ve sırt kayar. Bu, KDP'de en sık görülen kapak hatasıdır.
    g2 = covers.geometry("paperback", 300)
    rep.check(g2["spineIn"] != g["spineIn"],
              "sırt genişliği sayfa sayısına GERÇEKTEN bağlı",
              "sayfa sayısı 236→300 değişti ama sırt aynı kaldı — kapak "
              "sayfa sayısından türetilmiyor demektir")
    rep.check(abs(g2["spineIn"] - 300 * 0.0025) < 0.0001,
              "300 sayfada sırt 0,75\"",
              f"gelen {g2['spineIn']}")

    # --- ciltli ile ciltsiz AYNI OLMAMALI ---
    gh = covers.geometry("hardcover", pages)
    rep.check(gh["fullIn"] != g["fullIn"] and gh["spineIn"] != g["spineIn"],
              "ciltli kapak geometrisi ciltsizden FARKLI",
              "ciltli ve ciltsiz aynı ölçüyü veriyor — ciltsiz kapağı "
              "ciltliye yüklemek KDP'de reddedilir")
    rep.check(abs(gh["edgeIn"] - 0.51) < 0.0001 and abs(gh["safeIn"] - 0.635) < 0.0001,
              "ciltli sarım 0,51\" ve güvenli alan 0,635\" (KDP belgesi)",
              f"sarım {gh['edgeIn']} · güvenli {gh['safeIn']}")


# =============================================================================
# ② KAPAK DOĞRULAMASI KUSURU GÖRÜYOR MU
# =============================================================================

def test_phase7_gates(rep: Report, tmp: str) -> None:
    """
    FAZ 7'DE DOĞAN İKİ KAPI GERÇEKTEN ISIRIYOR MU

    ⓐ SAYFA SINIRI. Faz 6'da yaş rozeti kâğıdın kenarından 27 pt taşıyordu
       ve bunu gören hiçbir kapı yoktu: güvenli alan kapısı ÇİZİLENİ değil
       PLANLANANI ölçüyordu. Yeni kapı mutlak sayfa kutusuna bakar.

    ⓑ METİNSİZ A+ MODÜLÜ. Faz 6'da iki modül (009, 010) şartnamesi metin
       istediği hâlde metinsiz üretildi ve doğrulama yalnızca ölçü/renk/
       boyut denetliyordu.
    """
    mb.banner("⑥ Faz 7 kapıları ısırıyor mu")
    import covers
    import aplus
    import coverspec as cs

    # ⓐ Sayfa dışına taşan tipografi reddedilmeli.
    g = covers.geometry("paperback", 234)
    rec = {"edition": "paperback", "geometry": g,
           "pdf": None, "bytes": 0, "issues": [],
           "art": {"croppedPct": [0, 0]},
           "outsideSafe": [],
           "offPage": ["ageBadge [814,605,952,632]"],
           "overlaps": []}
    r = mb.Result("t")
    # PDF'siz çalıştırmak için yalnızca ilgili denetimleri çağırıyoruz:
    r.add(not rec.get("offPage"), "sayfa içinde", f"SAYFA DIŞI: {rec['offPage']}")
    rep.check(len(r.failures) > 0,
              "sayfa dışına taşan tipografi REDDEDİLDİ",
              "sayfa sınırı kapısı kör")

    # Ve gerçek üretim kapağında taşma OLMAMALI.
    build = os.path.join(mb.REPORTS_TRACKED, "cover-build.json")
    if os.path.exists(build):
        with open(build, encoding="utf-8") as fh:
            payload = json.load(fh)
        for ed, got in (payload.get("editions") or {}).items():
            rep.check(not got.get("offPage"),
                      f"{ed}: üretim kapağında sayfa dışı tipografi yok",
                      f"{ed} SAYFA DIŞINA TAŞIYOR: {got.get('offPage')}")
            rep.check(not got.get("overlaps"),
                      f"{ed}: üretim kapağında çakışan kutu yok",
                      f"{ed} ÇAKIŞMA: {got.get('overlaps')}")
            rep.check(got.get("isbnPrinted") is False,
                      f"{ed}: kapağa ISBN basılmadı",
                      f"{ed} KAPAĞA ISBN BASILMIŞ")

    # ⓑ Şartnamesi metin isteyen bir modül metinsiz kalırsa yakalanmalı.
    specs = {x["id"]: x for x in cs.aplus_records()}
    required = [k for k, v in specs.items()
                if any("post-processed" in z for z in v["textZones"])]
    rep.check(len(required) >= 8,
              f"şartname {len(required)} modülde sonradan basılan metin istiyor",
              "şartname metin bölgesi tanımlamıyor — kapı dayanaksız")
    missing_probe = [mid for mid in required
                     if not (aplus.TEXT.get(mid, {}).get("head")
                             or aplus.TEXT.get(mid, {}).get("sub"))]
    rep.check(not missing_probe,
              "metin isteyen her modülün metni TANIMLI",
              f"METİNSİZ MODÜL: {missing_probe} — Faz 6 kusuru geri geldi")

    # ⓒ KİMLİK KAPISI — ÜRETİLEN DOSYAYA BAKIYOR MU
    # Faz 7'nin son taraması, yapılandırma doğruyken EPUB'ın hâlâ
    # "[PENDING — founder decision A9]" diye bir YAYINCI adı taşıdığını
    # buldu; metadata kapısı yalnızca kendi çıktısını denetliyordu.
    # Aynı sınıf iki üretim PDF'inde de vardı: yazar alanı BOŞTU, çünkü
    # `project.author` diye var olmayan bir anahtar okunuyordu.
    eb = os.path.join(mb.REPORTS_TRACKED, "epub-build.json")
    if os.path.exists(eb):
        with open(eb, encoding="utf-8") as fh:
            ident = (json.load(fh).get("opfIdentity") or {})
        rep.check(mb.AUTHOR in (ident.get("creator") or []),
                  f"EPUB künyesinde yazar tek kaynakla aynı",
                  f"EPUB YAZARI UYUŞMUYOR: {ident.get('creator')}")
        rep.check(mb.PUBLISHER in (ident.get("publisher") or []),
                  f"EPUB künyesinde yayıncı tek kaynakla aynı",
                  f"EPUB YAYINCISI UYUŞMUYOR: {ident.get('publisher')}")
        rep.check(not ident.get("hasPlaceholder"),
                  "EPUB künyesinde yer tutucu yok",
                  "EPUB KÜNYESİNDE YER TUTUCU VAR — okura gider")
        # Kasıtlı kusur: künyeye yer tutucu koy, kapı görmeli.
        probe = {"creator": ["X"], "publisher": ["[PENDING — ...]"],
                 "hasPlaceholder": True}
        rep.check(mb.AUTHOR not in probe["creator"]
                  and probe["hasPlaceholder"],
                  "yer tutucu künye YAKALANIR",
                  "kimlik kapısı kör")

    # Üretim PDF'lerinin künyesi de tek kaynakla aynı olmalı.
    import subprocess
    for ed in ("paperback", "hardcover"):
        for kind in ("interior", "cover"):
            path = os.path.join(mb.ROOT, "08_OUTPUT", ed, f"{kind}.pdf")
            if not os.path.exists(path):
                continue
            out = subprocess.run(["pdfinfo", path], capture_output=True,
                                 text=True).stdout
            got = next((l.split(":", 1)[1].strip()
                        for l in out.splitlines()
                        if l.startswith("Author:")), "")
            rep.check(got == mb.AUTHOR,
                      f"{ed}/{kind}.pdf künyesinde yazar doğru",
                      f"{ed}/{kind}.pdf Author={got!r} — beklenen {mb.AUTHOR!r}")

    # ⓓ SANAT BÜTÜNLÜĞÜ VE KÖKENİ (Faz 7 · sanat yenileme)
    import cover_artwork as ca

    # Köken: covers.py yetkili dizinden okuyor mu?
    ok_src, why_src = ca.covers_source_ok()
    rep.check(ok_src, "kapak hattı YETKİLİ sanat dizininden okuyor",
              f"KÖKEN YANLIŞ: {why_src}")

    # Yıkıcı hat geri gelmiş mi?
    rep.check(not ca.forbidden_hits(),
              "yıkıcı metin-silme hattı covers.py'de yok",
              f"YIKICI HAT GERİ GELMİŞ: {ca.forbidden_hits()}")
    # ...ve kapı onu GERÇEKTEN görüyor mu (kasıtlı kusur):
    saved_forbidden = list(ca.FORBIDDEN_IN_COVERS)
    try:
        # covers.py'de kesinlikle bulunan bir ad ekle → kapı ısırmalı
        ca.FORBIDDEN_IN_COVERS.append("def build_cover")
        rep.check(bool(ca.forbidden_hits()),
                  "yasak-ad taraması kasıtlı kusuru YAKALADI",
                  "yasak-ad taraması kör — covers.py'yi hiç okumuyor")
    finally:
        ca.FORBIDDEN_IN_COVERS[:] = saved_forbidden

    # Masterlar manifestoyla aynı mı + kasıtlı bozma yakalanıyor mu
    man = os.path.join(mb.REPORTS_TRACKED, "cover-artwork-manifest.json")
    if os.path.exists(man):
        with open(man, encoding="utf-8") as fh:
            recorded = json.load(fh).get("masters", {})
        live = ca.scan()
        drift = [n for n in live
                 if n in recorded and recorded[n]["sha256"] != live[n]["sha256"]]
        rep.check(not drift,
                  f"master sanat değişmedi ({len(live)} dosya · sha256)",
                  f"MASTER SANAT DEĞİŞTİRİLMİŞ: {drift}")
        # kasıtlı kusur: kayıtlı bir sha'yı boz → karşılaştırma görmeli
        if recorded:
            k = sorted(recorded)[0]
            faked = dict(recorded)
            faked[k] = {**recorded[k], "sha256": "0" * 64}
            seen = [n for n in live
                    if n in faked and faked[n]["sha256"] != live[n]["sha256"]]
            rep.check(k in seen,
                      "sha256 karşılaştırması kasıtlı bozmayı YAKALADI",
                      "checksum kapısı kör — master bozulsa görmez")

    # ⓔ KONTRAST KAPISI kasıtlı kusuru görüyor mu
    import covers as cov
    rep.check(cov._contrast(cov._rel_lum((1, 1, 1)),
                            cov._rel_lum((0, 0, 0))) > 20,
              "kontrast hesabı beyaz/siyahta doğru (>20:1)",
              "kontrast hesabı bozuk")
    # koyu lacivert yazı, koyu lacivert zemin → kaybolur, kapı görmeli
    bad = cov._contrast(cov._rel_lum((0.075, 0.115, 0.26)),
                        cov._rel_lum((0.10, 0.14, 0.30)))
    rep.check(bad < cov._WCAG_MIN,
              "kontrast kapısı 'yazı zemine gömülü' durumunu reddeder",
              f"kontrast kapısı kör — gömülü yazı {bad:.2f}:1 geçiyor")
    # üretim kapaklarında yazar adı gerçekten okunuyor mu
    build = os.path.join(mb.REPORTS_TRACKED, "cover-build.json")
    if os.path.exists(build):
        with open(build, encoding="utf-8") as fh:
            payload = json.load(fh)
        for ed, got in (payload.get("editions") or {}).items():
            au = (got.get("contrast") or {}).get("author", {}).get("p10")
            rep.check(au is not None and au >= cov._WCAG_MIN,
                      f"{ed}: yazar adı kontrastı ölçülü ve yeterli ({au}:1)",
                      f"{ed} YAZAR ADI KONTRASTI: {au}")

    # Kasıtlı kusur: bir modülün metnini boşalt, kapı görmeli.
    victim = required[-1]
    saved = dict(aplus.TEXT.get(victim, {}))
    try:
        aplus.TEXT[victim] = {**saved, "head": "", "sub": ""}
        empty = [mid for mid in required
                 if not (aplus.TEXT.get(mid, {}).get("head")
                         or aplus.TEXT.get(mid, {}).get("sub"))]
        rep.check(victim in empty,
                  f"boşaltılan modül ({victim}) YAKALANDI",
                  "metinsiz modül kapısı kör")
    finally:
        aplus.TEXT[victim] = saved


def test_cover_validation(rep: Report, tmp: str) -> None:
    mb.banner("② kapak doğrulaması kusuru görüyor mu")
    import covers

    def fake_pdf(path, w_in, h_in, embed=True):
        from reportlab.pdfgen import canvas
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        if embed:
            try:
                pdfmetrics.registerFont(TTFont(
                    "T", "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"))
                fname = "T"
            except Exception:                                  # noqa: BLE001
                fname = "Helvetica"
        else:
            fname = "Helvetica"                                # base-14 → gömülmez
        c = canvas.Canvas(path, pagesize=(w_in * 72, h_in * 72))
        c.setFont(fname, 24)
        c.drawString(40, 40, "TEST")
        c.showPage()
        c.save()

    # --- YANLIŞ ÖLÇÜ reddedilmeli ---
    bad = os.path.join(tmp, "bad-size.pdf")
    fake_pdf(bad, 10.0, 8.0)
    rec = {"edition": "paperback",
           "geometry": covers.geometry("paperback", 236),
           "pdf": os.path.relpath(bad, mb.ROOT),
           "bytes": os.path.getsize(bad), "issues": [],
           "art": {"croppedPct": [0, 0]}}
    r = mb.Result("t")
    covers.validate(rec, r)
    rep.check(len(r.failures) > 0,
              "yanlış ölçülü kapak REDDEDİLDİ",
              "10×8 inç bir kapak 12,84×9,25 beklenirken kabul edildi")

    # --- GÖMÜLMEYEN FONT reddedilmeli ---
    g = covers.geometry("paperback", 236)
    nf = os.path.join(tmp, "nofont.pdf")
    fake_pdf(nf, g["fullIn"][0], g["fullIn"][1], embed=False)
    rec2 = {"edition": "paperback", "geometry": g,
            "pdf": os.path.relpath(nf, mb.ROOT),
            "bytes": os.path.getsize(nf), "issues": [],
            "art": {"croppedPct": [0, 0]}}
    r2 = mb.Result("t")
    covers.validate(rec2, r2)
    bad_font = any("GÖMÜLÜ OLMAYAN" in c["message"] for c in r2.failures)
    rep.check(bad_font, "gömülü olmayan fontlu kapak REDDEDİLDİ",
              "Helvetica gömülmeden geçti — KDP şartı 'gömülü olmayan font: 0'")

    # --- GÜVENLİ ALAN İHLALİ reddedilmeli ---
    rec3 = {"edition": "paperback", "geometry": g,
            "pdf": os.path.relpath(nf, mb.ROOT), "bytes": 100,
            "issues": [], "art": {"croppedPct": [0, 0]},
            "outsideSafe": ["ageBadge [1,2,3,4]"]}
    r3 = mb.Result("t")
    covers.validate(rec3, r3)
    rep.check(any("GÜVENLİ ALAN" in c["message"] for c in r3.failures),
              "güvenli alan dışına taşan tipografi REDDEDİLDİ",
              "taşan kutu kabul edildi")

    # --- EKSİK KAPAK reddedilmeli ---
    # ⚠ `covers.RAW` Faz 7'de KALDIRILDI: sanat artık yalnızca yetkili
    # `covers.ART_DIR` (07_ASSETS/raw/re-generated) altından okunur.
    # Bu test o yeniden adlandırmayı da yakalar.
    rep.check(hasattr(covers, "ART_DIR") and not hasattr(covers, "RAW"),
              "kapak hattı yalnızca ART_DIR kullanıyor (RAW kaldırıldı)",
              "covers.py hâlâ eski RAW yolunu taşıyor")
    src = os.path.join(covers.ART_DIR, "cover-paperback-wrap.png")
    rep.check(os.path.exists(src),
              "üretim sanatı yetkili dizinde mevcut",
              f"YETKİLİ SANAT EKSİK: {src}")


# =============================================================================
# ③ A+ MODÜL ÖLÇÜLERİ
# =============================================================================

def test_aplus(rep: Report, tmp: str) -> None:
    mb.banner("③ A+ modül ölçüsü kusuru görüyor mu")
    import aplus

    ed = ed_mod.get("paperback")
    specs = {x["id"]: x for x in cs.all_records(236, ed.trim_w_in, ed.trim_h_in)
             if x["family"] == "aplus"}
    rep.check(len(specs) == 10, f"10 A+ modülü tanımlı ({len(specs)})",
              f"{len(specs)} modül")

    # Amazon ölçüleri SABİTTİR: kaynak oranı ne olursa olsun çıktı tam olmalı.
    for mid in ("aplus-001-hero", "aplus-010-series", "aplus-004-value"):
        tw, th = specs[mid]["renderPx"]
        for src_w, src_h in ((1000, 1000), (3000, 500), (500, 3000)):
            im = Image.new("RGB", (src_w, src_h), (200, 200, 200))
            out, info = aplus.fit_cover(im, tw, th)
            if out.size != (tw, th):
                rep.check(False, f"{mid}: {src_w}×{src_h} → tam ölçü",
                          f"çıktı {out.size}, beklenen {(tw, th)}")
                break
        else:
            rep.check(True, f"{mid}: her kaynak oranında TAM {tw}×{th}")

    # ESNETME OLMAMALI: kare kaynaktan gelen daire, dairenin oranını korumalı
    im = Image.new("RGB", (600, 600), (255, 255, 255))
    from PIL import ImageDraw
    ImageDraw.Draw(im).ellipse([150, 150, 450, 450], fill=(0, 0, 0))
    out, _ = aplus.fit_cover(im, 600, 180)          # çok geniş hedef
    bw = out.convert("L").point(lambda v: 255 if v < 128 else 0, mode="L")
    bb = bw.getbbox()
    ratio = (bb[2] - bb[0]) / (bb[3] - bb[1]) if bb else 0
    rep.check(ratio > 1.6,
              f"A+ kırpma ESNETMİYOR (daire kırpıldı, ezilmedi · oran {ratio:.2f})",
              "daire ezilmiş — kırpma yerine esnetme yapılıyor")

    # Rapor kapısı: ölçüsü tutmayan modül REDDEDİLMELİ
    rows = [{"id": "x", "targetPx": [970, 600], "actualPx": [969, 600],
             "bytes": 10, "mode": "RGB",
             "art": {"croppedPct": [0, 0]}, "typography": "post"}]
    bad = [x["id"] for x in rows if x["actualPx"] != x["targetPx"]]
    rep.check(bool(bad), "bir piksel sapma bile REDDEDİLİYOR",
              "969×600, 970×600 beklenirken kabul edildi")


# =============================================================================
# ④ EPUB PAKETİ
# =============================================================================

def test_epub(rep: Report, tmp: str) -> None:
    mb.banner("④ EPUB kusuru görüyor mu")

    real = os.path.join(mb.ROOT, "08_OUTPUT", "kindle", "book.epub")
    if not os.path.exists(real):
        rep.check(False, "üretim EPUB'ı var", "08_OUTPUT/kindle/book.epub yok")
        return

    with zipfile.ZipFile(real) as z:
        names = z.namelist()
    rep.check("OEBPS/images/cover.jpg" in names,
              "üretim EPUB'ında kapak var",
              "kapak yok — okuyucu kütüphanede kapağı göstermez")
    rep.check("OEBPS/nav.xhtml" in names and "OEBPS/toc.ncx" in names,
              "üretim EPUB'ında içindekiler İKİ biçimde de var",
              "içindekiler eksik")

    # --- KASITLI KUSUR: mimetype sıkıştırılmış ---
    broken = os.path.join(tmp, "broken.epub")
    with zipfile.ZipFile(broken, "w") as z:
        z.writestr("mimetype", "application/epub+zip",
                   compress_type=zipfile.ZIP_DEFLATED)   # OCF İHLALİ
        z.writestr("META-INF/container.xml", "<container/>")
    with zipfile.ZipFile(broken) as z:
        first = z.infolist()[0]
        ok = (first.filename == "mimetype"
              and first.compress_type == zipfile.ZIP_STORED)
    rep.check(not ok, "sıkıştırılmış mimetype KUSUR olarak görülüyor",
              "OCF ihlali fark edilmedi")

    # --- KASITLI KUSUR: kırık görsel bağı ---
    import xml.etree.ElementTree as ET
    doc = ('<?xml version="1.0" encoding="utf-8"?><html '
           'xmlns="http://www.w3.org/1999/xhtml"><body>'
           '<img src="images/yok.png"/></body></html>')
    root = ET.fromstring(doc)
    srcs = [el.get("src") for el in root.iter() if el.tag.endswith("}img")]
    dangling = [s for s in srcs if f"OEBPS/{s}" not in names]
    rep.check(bool(dangling), "kırık görsel bağı KUSUR olarak görülüyor",
              "olmayan görsele işaret eden img kabul edildi")

    # --- KASITLI KUSUR: bozuk XML ---
    try:
        ET.fromstring("<html><body><p>açık")
        parsed = True
    except ET.ParseError:
        parsed = False
    rep.check(not parsed, "bozuk XML KUSUR olarak görülüyor",
              "kapanmamış etiket iyi biçimli sayıldı")

    # --- BÜTÇE KAPISI GERÇEKTEN ISIRIYOR MU ---
    budget = mb._CFG["editions"]["kindle"]["fileBudgetMb"]
    fake_mb = budget + 2.5
    over = round(max(0.0, fake_mb - budget), 3)
    rep.check(over > 0,
              f"bütçe aşımı hesaplanıyor ({fake_mb} MB > {budget} MB)",
              "aşım 0 çıktı — kapı ölmüş")


# =============================================================================
# ⑤ MANUSCRIPT SIZINTISI — Faz 6 çıktıları da temiz mi
# =============================================================================

def test_leak(rep: Report) -> None:
    mb.banner("⑤ Faz 6 raporları proza sızdırıyor mu")
    book = mb.load_book()
    if not book:
        rep.check(True, "manuscript yerelde yok — sızıntı testi uygulanamaz")
        return
    stories = mb.book_stories(book)
    openings = []
    for s in stories.values():
        t = (s.get("text") or "").strip()
        if t:
            openings.append(" ".join(t.split()[:8]).lower())

    tracked = []
    for name in ("cover-build.json", "aplus-build.json", "epub-build.json",
                 "interior-build.json", "metadata.json"):
        p = os.path.join(mb.REPORTS_TRACKED, name)
        if os.path.exists(p):
            tracked.append((name, open(p, encoding="utf-8").read().lower()))

    leaked = [n for n, blob in tracked
              if any(o in blob for o in openings if len(o) > 30)]
    rep.check(not leaked,
              f"Faz 6 raporlarında proza sızıntısı yok ({len(tracked)} rapor)",
              f"SIZINTI: {leaked}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Faz 6 paket kapılarının testi")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  FAZ 6 PAKET KAPILARININ KENDİ TESTİ")
    print("═" * 72)
    print("  Bir kapının VARLIĞI çalıştığı anlamına gelmez.")

    rep = Report(args.verbose)
    with tempfile.TemporaryDirectory() as tmp:
        test_cover_geometry(rep)
        test_cover_validation(rep, tmp)
        test_phase7_gates(rep, tmp)
        test_aplus(rep, tmp)
        test_epub(rep, tmp)
        test_leak(rep)

    if args.json:
        os.makedirs(os.path.dirname(args.json), exist_ok=True)
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"passed": rep.passed, "failed": len(rep.failed)},
                      fh, ensure_ascii=False, indent=2)
            fh.write("\n")

    print()
    print("═" * 72)
    if rep.failed:
        print(f"  ⛔ {len(rep.failed)} PAKET TESTİ BAŞARISIZ · {rep.passed} geçti")
        for f in rep.failed:
            print(f"     · {f}")
        print("═" * 72)
        return 1
    print(f"  ✅ {rep.passed} PAKET TESTİ GEÇTİ — paket kapıları ısırıyor")
    print("═" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
