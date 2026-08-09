#!/usr/bin/env python3
"""
KINDLE / REFLOWABLE EPUB
================================================================================
    python3 04_BUILD/epub.py            EPUB üret + doğrula
    python3 04_BUILD/epub.py --check    kayıtlı rapor bayat mı

    02_MANUSCRIPT/book.json              proza (DEPO DIŞINDA)
    07_ASSETS/processed/kindle/*.png     1200 px görseller
              ↓
    08_OUTPUT/kindle/book.epub           ← PROZA İÇERİR, DEPODA DURMAZ
    06_REPORTS/tracked/epub-build.json   ← YALNIZCA SAYI, depoda durur

--------------------------------------------------------------------------------
İÇİNDEKİLER TABLOSU ZORUNLUDUR
--------------------------------------------------------------------------------
Yol haritası § 18: "reflowable EPUB · içindekiler tablosu ZORUNLU (Virtual
Voice için de şart)". Bu yüzden İKİ gezinme yapısı da yazılır: EPUB 3'ün
`nav.xhtml`'i ve eski okuyucuların hâlâ aradığı `toc.ncx`. Birini yazıp
diğerini atlamak, cihaz filosunun bir kısmında içindekileri yok eder.

--------------------------------------------------------------------------------
DOSYA BÜTÇESİ TÜRETİLMİŞTİR
--------------------------------------------------------------------------------
3,0 MB seçilmedi, HESAPLANDI: 7,99 $ × %70 = 5,593 $; yol haritasının verdiği
5,14 $ telif 0,453 $ teslim ücreti demektir; 0,15 $/MB'de bu 3,02 MB eder.
Aşılırsa telif HER SATILAN KOPYADA düşer — bu yüzden kapı, uyarı değil ölçüdür
ve aşım dolar cinsinden basılır.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb
import imagespec as spec

OUT_EPUB = os.path.join(mb.ROOT, "08_OUTPUT", "kindle", "book.epub")
OUT_JSON = os.path.join(mb.REPORTS_TRACKED, "epub-build.json")
KINDLE_DIR = os.path.join(spec.PROCESSED_DIR, "kindle")

# Sabit kimlik: aynı kitabın her yeniden üretimi AYNI EPUB kimliğini taşır.
# Rastgele UUID, her koşuda farklı bir "yeni kitap" üretirdi ve okuyucunun
# kütüphanesinde çift kayıt olurdu.
AUTHOR = "Emre Doğan"

BOOK_UID = "urn:uuid:6d7b1f4e-0000-4000-8000-677772626f6d"

CSS = """\
html, body { margin: 0; padding: 0; }
body { font-family: serif; line-height: 1.45; }
h1 { font-size: 1.5em; margin: 1em 0 0.2em; text-align: left; page-break-before: always; }
h2 { font-size: 1.2em; margin: 1.2em 0 0.4em; }
p { margin: 0; text-indent: 1.2em; }
p.first { text-indent: 0; }
p.note { font-style: italic; margin-top: 1em; text-indent: 0; font-size: 0.95em; }
div.illo { text-align: center; margin: 0 0 1em; page-break-inside: avoid; }
div.illo img { max-width: 100%; height: auto; }
div.card { margin: 1.5em 0; padding-top: 0.5em; border-top: 1px solid #999; }
div.card p { text-indent: 0; font-size: 0.95em; }
.center { text-align: center; }
dl.pron dt { font-weight: bold; margin-top: 0.5em; }
dl.pron dd { margin: 0 0 0 1.2em; }
"""


def esc(s: str) -> str:
    return html.escape(s or "", quote=False)


def xhtml(title: str, body: str) -> str:
    return (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" '
        'xmlns:epub="http://www.idpf.org/2007/ops" lang="en" xml:lang="en">\n'
        f'<head><meta charset="utf-8"/><title>{esc(title)}</title>'
        '<link rel="stylesheet" type="text/css" href="style.css"/></head>\n'
        f'<body>\n{body}\n</body>\n</html>\n'
    )


def paras(text: str, cls_first: bool = True) -> str:
    out = []
    for i, p in enumerate(mb.paragraphs(text or "")):
        cls = ' class="first"' if (i == 0 and cls_first) else ""
        out.append(f"<p{cls}>{esc(p)}</p>")
    return "\n".join(out)


# =============================================================================
# ÜRETİM
# =============================================================================

def build() -> dict:
    book = mb.load_book()
    if not book:
        return {}
    prose = mb.book_stories(book)
    idx = mb.load_stories()
    by_id = {s["id"]: s for s in idx.get("stories", [])}
    parts = sorted(idx.get("parts", []), key=lambda x: x.get("order") or 99)
    cultures = {c["id"]: c for c in mb.load_cultures().get("cultures", [])
                if c.get("status") == "locked"}
    cfg = mb._CFG["project"]

    written = sorted(prose.items(),
                     key=lambda kv: by_id.get(kv[0], {}).get("number") or 999)
    first_of_culture: dict[str, str] = {}
    for sid, _ in written:
        cid = by_id.get(sid, {}).get("cultureId")
        if cid and cid not in first_of_culture:
            first_of_culture[cid] = sid
    card_host = {v: k for k, v in first_of_culture.items()}

    files: dict[str, str] = {}          # ad → xhtml
    nav: list[tuple[str, str, int]] = []   # (başlık, dosya, seviye)
    images_used: list[str] = []
    missing_images: list[str] = []

    def use_image(image_id: str, alt: str) -> str:
        src = os.path.join(KINDLE_DIR, f"{image_id}.png")
        if not os.path.exists(src):
            missing_images.append(image_id)
            return ""
        if image_id not in images_used:
            images_used.append(image_id)
        return (f'<div class="illo"><img src="images/{image_id}.png" '
                f'alt="{esc(alt)}"/></div>')

    # --- kapak ---
    # Kindle kapağı EPUB'ın İÇİNDE de bulunmalı: `properties="cover-image"`
    # olmadan okuyucu kütüphanede kapağı göstermez. Dosya `covers.py`nin
    # ürettiği GERÇEK kapaktır (doğru başlık, basılmış tipografi) — ham
    # sanat değil.
    cover_src = os.path.join(mb.ROOT, "08_OUTPUT", "kindle", "cover.jpg")
    has_cover = os.path.exists(cover_src)
    if has_cover:
        files["cover.xhtml"] = xhtml(cfg["title"], (
            '<div class="illo" style="text-align:center">'
            '<img src="images/cover.jpg" alt="Cover"/></div>'))
        nav.append(("Cover", "cover.xhtml", 1))

    # --- başlık ---
    files["title.xhtml"] = xhtml(cfg["title"], (
        f'<h1 class="center" style="page-break-before:auto">{esc(cfg["title"])}</h1>\n'
        f'<p class="center">{esc(cfg["subtitle"])}</p>\n'
        f'<p class="center">{esc(AUTHOR)}</p>'))
    nav.append((cfg["title"], "title.xhtml", 1))

    # --- harita ---
    files["map.xhtml"] = xhtml("The Twenty-Two Cultures", (
        '<h1>The Twenty-Two Cultures</h1>\n'
        + use_image("map-001", "World map showing where the twenty-two "
                               "traditions in this book come from")
        + "\n<ul>" + "".join(
            f"<li>{esc(c['name'])} — "
            f"{esc((c.get('macroRegion') or c.get('region') or '').replace('-', ' '))}</li>"
            for c in sorted(cultures.values(), key=lambda x: x["name"]))
        + "</ul>"))
    nav.append(("The Twenty-Two Cultures", "map.xhtml", 1))

    # --- giriş ---
    files["intro.xhtml"] = xhtml("Before You Start", (
        "<h1>Before You Start</h1>\n" + paras(
            "Most books of myths for young readers are Greek books. This one "
            "is not. Greek stories are here — three of them — but so are "
            "stories from twenty-one other places, and none of them is a "
            "footnote to the Greek ones.\n\n"
            "Every story in this book is a retelling. Where the tellers "
            "disagree about what happened, this book picks one version and "
            "says so rather than pretending there was only ever one.\n\n"
            "Names that look hard are not hard. At the back there is a guide "
            "that tells you how to say every one of them.")))
    nav.append(("Before You Start", "intro.xhtml", 1))

    # --- bölümler ve hikâyeler ---
    per_story = []
    for part in parts:
        pfile = f"part-{part['id']}.xhtml"
        files[pfile] = xhtml(part["title"], (
            f'<h1>{esc(part["title"])}</h1>\n'
            f'<p class="note">{esc(part.get("epigraph") or "")}</p>'))
        nav.append((part["title"], pfile, 1))

        for sid, s in written:
            rec = by_id.get(sid, {})
            if rec.get("partId") != part["id"]:
                continue
            sfile = f"story-{rec.get('number'):03d}.xhtml"
            cid = card_host.get(sid)
            body = []
            if rec.get("imageId"):
                body.append(use_image(rec["imageId"], f"Illustration: {s['title']}"))
            body.append(f"<h1>{esc(s['title'])}</h1>")
            body.append(paras(s.get("text", "")))
            if s.get("culturalNote"):
                body.append(f'<p class="note">{esc(s["culturalNote"])}</p>')
            if cid and cultures.get(cid):
                c = cultures[cid]
                ct = c.get("cardText") or {}
                card = ['<div class="card">']
                if c.get("vignetteId"):
                    card.append(use_image(c["vignetteId"],
                                          f"{c['name']} emblem"))
                card.append(f"<h2>{esc(c['name'])} — {esc(ct.get('language', ''))}</h2>")
                card.append("<p>" + esc(" ".join(
                    ct.get(k, "") for k in ("whoTells", "where", "today")).strip())
                    + "</p>")
                card.append("</div>")
                body.append("\n".join(card))
            files[sfile] = xhtml(s["title"], "\n".join(body))
            nav.append((f"{rec.get('number')}. {s['title']}", sfile, 2))
            per_story.append({"id": sid, "number": rec.get("number"),
                              "file": sfile,
                              "words": mb.word_count(s.get("text", "")),
                              "hasImage": bool(rec.get("imageId")),
                              "hasCard": bool(cid)})

    # --- arka madde ---
    entries = [s for s in idx.get("stories", [])
               if s.get("status") not in ("dropped", "candidate") and s.get("number")]

    def sk(n: str) -> str:
        return mb.strip_diacritics(n).lower()

    seen, pron = set(), []
    for s in entries:
        for e in s.get("pronunciationEntries") or []:
            if e["name"] not in seen:
                seen.add(e["name"])
                pron.append(e)
    files["pronunciation.xhtml"] = xhtml("Say These Names", (
        "<h1>Say These Names</h1>\n<dl class=\"pron\">"
        + "".join(f"<dt>{esc(e['name'])}</dt><dd>{esc(e.get('pronunciation',''))}</dd>"
                  for e in sorted(pron, key=lambda x: sk(x["name"])))
        + "</dl>"))
    nav.append(("Say These Names", "pronunciation.xhtml", 1))

    seen, who = set(), []
    for s in entries:
        for ch in s.get("characters") or []:
            if ch.get("glossary") and ch["name"] not in seen:
                seen.add(ch["name"])
                who.append(ch)
    files["whoswho.xhtml"] = xhtml("Who's Who", (
        "<h1>Who's Who</h1>\n<dl class=\"pron\">"
        + "".join(f"<dt>{esc(c['name'])}</dt><dd>{esc(c.get('role',''))}</dd>"
                  for c in sorted(who, key=lambda x: sk(x["name"])))
        + "</dl>"))
    nav.append(("Who's Who", "whoswho.xhtml", 1))

    cmap = mb.culture_by_id(mb.load_cultures())
    rows = []
    for s in sorted(entries, key=lambda x: x["number"]):
        srcs = [x for x in s.get("sources", [])
                if x.get("kind") not in ("index", "retelling")][:2]
        rows.append(f"<dt>{s['number']}. {esc(s['title'])} — "
                    f"{esc(cmap.get(s['cultureId'], {}).get('name',''))}</dt>"
                    f"<dd>{esc('; '.join(x.get('citation','')[:160] for x in srcs))}</dd>")
    files["sources.xhtml"] = xhtml("Where the Stories Come From", (
        "<h1>Where the Stories Come From</h1>\n"
        '<p class="note">Australian Aboriginal traditions are deliberately '
        'not included in this book. Those stories are held by their '
        'communities, and who may tell them is decided by rule, not by '
        'preference.</p>\n<dl class="pron">' + "".join(rows) + "</dl>"))
    nav.append(("Where the Stories Come From", "sources.xhtml", 1))

    files["colophon.xhtml"] = xhtml("A Note on How This Book Was Made", (
        "<h1>A Note on How This Book Was Made</h1>\n" + paras(
            "Every story here was researched from published scholarship and "
            "primary collections. Retellings by other authors were not used "
            "as sources.\n\n"
            "Artificial intelligence tools were used in producing this book. "
            "The specific disclosure required by the retailer is filed with "
            "the publication record.")))
    nav.append(("A Note on How This Book Was Made", "colophon.xhtml", 1))

    # --- gezinme ---
    nav_items = "".join(
        f'<li><a href="{f}">{esc(t)}</a></li>' for t, f, lvl in nav if lvl == 1)
    files["nav.xhtml"] = xhtml("Contents", (
        '<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>'
        + "".join(f'<li><a href="{f}">{esc(t)}</a></li>' for t, f, _ in nav)
        + "</ol></nav>"))

    ncx = ('<?xml version="1.0" encoding="utf-8"?>\n'
           '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">\n'
           f'<head><meta name="dtb:uid" content="{BOOK_UID}"/></head>\n'
           f'<docTitle><text>{esc(cfg["title"])}</text></docTitle>\n<navMap>\n'
           + "".join(
               f'<navPoint id="n{i}" playOrder="{i + 1}">'
               f'<navLabel><text>{esc(t)}</text></navLabel>'
               f'<content src="{f}"/></navPoint>\n'
               for i, (t, f, _) in enumerate(nav))
           + '</navMap>\n</ncx>\n')

    spine_order = ((["cover.xhtml"] if has_cover else [])
                   + ["title.xhtml", "nav.xhtml", "map.xhtml", "intro.xhtml"]
                   + [f for f in files
                      if f.startswith(("part-", "story-"))]
                   + ["pronunciation.xhtml", "whoswho.xhtml", "sources.xhtml",
                      "colophon.xhtml"])
    spine_order = list(dict.fromkeys(spine_order))

    manifest = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" '
        'properties="nav"/>',
        '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
        '<item id="css" href="style.css" media-type="text/css"/>',
    ]
    for i, f in enumerate(spine_order):
        if f == "nav.xhtml":
            continue
        manifest.append(f'<item id="x{i}" href="{f}" '
                        'media-type="application/xhtml+xml"/>')
    for img in images_used:
        manifest.append(f'<item id="img-{img}" href="images/{img}.png" '
                        'media-type="image/png"/>')
    if has_cover:
        manifest.append('<item id="cover-image" href="images/cover.jpg" '
                        'media-type="image/jpeg" properties="cover-image"/>')

    opf = ('<?xml version="1.0" encoding="utf-8"?>\n'
           '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" '
           'unique-identifier="bookid" xml:lang="en">\n'
           '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
           f'<dc:identifier id="bookid">{BOOK_UID}</dc:identifier>\n'
           f'<dc:title>{esc(cfg["title"])}</dc:title>\n'
           f'<dc:language>en</dc:language>\n'
           f'<dc:description>{esc(cfg["subtitle"])}</dc:description>\n'
           f'<dc:creator>{esc(AUTHOR)}</dc:creator>\n'
           # EPUB 2 uyumluluğu: eski okuyucular kapağı `meta name="cover"`
           # ile bulur, EPUB 3'ün `properties="cover-image"` işaretiyle değil.
           # İkisi de yazılır.
           + ('<meta name="cover" content="cover-image"/>\n' if has_cover else '')
           + '<dc:publisher>[PENDING — founder decision A9]</dc:publisher>\n'
           '<meta property="dcterms:modified">2026-08-09T00:00:00Z</meta>\n'
           '<meta property="schema:typicalAgeRange">8-12</meta>\n'
           '</metadata>\n<manifest>\n' + "\n".join(manifest)
           + '\n</manifest>\n<spine toc="ncx">\n'
           + "".join(f'<itemref idref="x{i}"/>\n'
                     for i, f in enumerate(spine_order) if f != "nav.xhtml")
           + '</spine>\n</package>\n')

    # --- yaz ---
    os.makedirs(os.path.dirname(OUT_EPUB), exist_ok=True)
    with zipfile.ZipFile(OUT_EPUB, "w") as z:
        # mimetype ilk ve SIKIŞTIRMASIZ olmak zorunda (OCF şartı)
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip",
                   compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml",
                   '<?xml version="1.0" encoding="utf-8"?>\n'
                   '<container version="1.0" '
                   'xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n'
                   '<rootfiles><rootfile full-path="OEBPS/content.opf" '
                   'media-type="application/oebps-package+xml"/></rootfiles>\n'
                   '</container>\n', compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/content.opf", opf, zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/toc.ncx", ncx, zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/style.css", CSS, zipfile.ZIP_DEFLATED)
        for name, content in files.items():
            z.writestr(f"OEBPS/{name}", content, zipfile.ZIP_DEFLATED)
        for img in images_used:
            z.write(os.path.join(KINDLE_DIR, f"{img}.png"),
                    f"OEBPS/images/{img}.png", zipfile.ZIP_DEFLATED)
        if has_cover:
            z.write(cover_src, "OEBPS/images/cover.jpg", zipfile.ZIP_DEFLATED)

    # --- ölç ---
    total = os.path.getsize(OUT_EPUB)
    with zipfile.ZipFile(OUT_EPUB) as z:
        infos = z.infolist()
        img_bytes = sum(i.compress_size for i in infos
                        if i.filename.startswith("OEBPS/images/"))
        text_bytes = sum(i.compress_size for i in infos
                         if not i.filename.startswith("OEBPS/images/"))
        names = {i.filename for i in infos}

    budget = mb._CFG["editions"]["kindle"]["fileBudgetMb"]
    return {
        "$comment": [
            "EPUB RAPORU — yalnızca ÖLÇÜ içerir; tek bir hikâye cümlesi bile",
            "yoktur (K21). EPUB'ın kendisi depo dışındadır.",
            "Üretici: 04_BUILD/epub.py",
        ],
        "gate": mb.read_gate(),
        "epub": os.path.relpath(OUT_EPUB, mb.ROOT),
        "totalBytes": total,
        "totalMb": round(total / 1e6, 3),
        "imageBytes": img_bytes,
        "textBytes": text_bytes,
        "budgetMb": budget,
        "overBudgetMb": round(max(0.0, total / 1e6 - budget), 3),
        "royaltyLossUsd": round(max(0.0, total / 1e6 - budget) * 0.15, 3),
        "documents": len(files),
        "spine": len(spine_order),
        "navEntries": len(nav),
        "hasNavXhtml": "OEBPS/nav.xhtml" in names,
        "hasNcx": "OEBPS/toc.ncx" in names,
        "hasCover": "OEBPS/images/cover.jpg" in names,
        "images": len(images_used),
        "imagesExpected": spec.TOTAL,
        "missingImages": sorted(set(missing_images)),
        "stories": len(per_story),
        "storiesWithImage": sum(1 for p in per_story if p["hasImage"]),
        "storiesWithCard": sum(1 for p in per_story if p["hasCard"]),
        "perStory": per_story,
    }


def validate(data: dict, r: mb.Result) -> None:
    import zipfile as zf
    path = os.path.join(mb.ROOT, data["epub"])

    # --- OCF yapısı ---
    with zf.ZipFile(path) as z:
        names = z.namelist()
        first = z.infolist()[0]
        r.add(first.filename == "mimetype"
              and first.compress_type == zf.ZIP_STORED,
              "mimetype ilk girdi ve sıkıştırılmamış (OCF şartı)",
              "mimetype yanlış yerde veya sıkıştırılmış — bazı okuyucular reddeder")
        r.add("META-INF/container.xml" in names, "container.xml var",
              "container.xml yok — EPUB açılmaz")
        bad = z.testzip()
        r.add(bad is None, "zip bütünlüğü sağlam", f"bozuk girdi: {bad}")

        # her XHTML iyi biçimli mi + her img referansı dosyaya düşüyor mu
        import xml.etree.ElementTree as ET
        broken, dangling = [], []
        for n in names:
            if not n.endswith(".xhtml") and not n.endswith((".opf", ".ncx")):
                continue
            try:
                root = ET.fromstring(z.read(n))
            except ET.ParseError as exc:
                broken.append(f"{n}: {exc}")
                continue
            for el in root.iter():
                if el.tag.endswith("}img"):
                    src = el.get("src", "")
                    target = os.path.normpath(
                        os.path.join(os.path.dirname(n), src))
                    if target not in names:
                        dangling.append(f"{n} → {src}")
        r.add(not broken, f"bütün XHTML/OPF/NCX belgeleri iyi biçimli "
                          f"({sum(1 for n in names if n.endswith('.xhtml'))} belge)",
              "BOZUK XML:\n         " + "\n         ".join(broken[:8]))
        r.add(not dangling, "bütün görsel referansları dosyaya düşüyor",
              "KIRIK GÖRSEL BAĞI:\n         " + "\n         ".join(dangling[:8]))

    r.add(data["hasCover"],
          "Kindle kapağı EPUB'ın içinde (properties=cover-image)",
          "EPUB'da KAPAK YOK — okuyucu kütüphanede kapağı göstermez; "
          "`covers.py` çalıştırın")
    r.add(data["hasNavXhtml"] and data["hasNcx"],
          f"içindekiler İKİ biçimde de var (nav.xhtml + toc.ncx · "
          f"{data['navEntries']} girdi)",
          "içindekiler eksik — yol haritası § 18 onu ZORUNLU kılar "
          "(Virtual Voice için de şart)")
    r.add(data["stories"] == mb.STORY_TARGET,
          f"{data['stories']}/{mb.STORY_TARGET} hikâye EPUB'da",
          f"{data['stories']}/{mb.STORY_TARGET} hikâye")
    r.add(data["storiesWithImage"] == mb.STORY_TARGET,
          f"{data['storiesWithImage']}/{mb.STORY_TARGET} hikâyede açılış görseli",
          f"görselsiz hikâye: {mb.STORY_TARGET - data['storiesWithImage']}")
    r.add(data["storiesWithCard"] == mb.CULTURE_TARGET,
          f"{data['storiesWithCard']}/{mb.CULTURE_TARGET} kültür kartı",
          f"kart sayısı {data['storiesWithCard']}, {mb.CULTURE_TARGET} olmalı")
    r.add(not data["missingImages"],
          f"bütün görseller pakette ({data['images']}/{data['imagesExpected']})",
          f"EKSİK GÖRSEL: {data['missingImages'][:10]}")

    over = data["overBudgetMb"]
    r.add(over == 0,
          f"Kindle dosya bütçesi tutuyor "
          f"({data['totalMb']:.2f} ≤ {data['budgetMb']:.2f} MB)",
          f"EPUB {data['totalMb']:.2f} MB > {data['budgetMb']:.2f} MB "
          f"({over:.2f} MB aşım) — 0,15 $/MB teslim ücreti telifi "
          f"{data['royaltyLossUsd']:.2f} $/kopya düşürür")


def main() -> int:
    ap = argparse.ArgumentParser(description="Kindle EPUB")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    print("═" * 72)
    print("  KINDLE · REFLOWABLE EPUB")
    print("═" * 72)

    r = mb.Result("epub", verbose=args.verbose)
    data = build()
    if not data:
        print("\n  manuscript yerelde yok — EPUB UYGULANAMAZ (K21).")
        r.add(os.path.exists(OUT_JSON), "kayıtlı EPUB raporu depoda",
              "epub-build.json yok — denetlenecek rapor depoda durmuyorsa "
              "o denetim ÖLÜ KURALDIR (K18)")
        return r.finish(None)

    print(f"\n  belge      : {data['documents']}  (spine {data['spine']})")
    print(f"  görsel     : {data['images']}/{data['imagesExpected']}")
    print(f"  metin payı : {data['textBytes'] / 1e6:.2f} MB")
    print(f"  görsel payı: {data['imageBytes'] / 1e6:.2f} MB")
    print(f"  TOPLAM     : {data['totalMb']:.2f} MB  (bütçe {data['budgetMb']:.2f} MB)")

    validate(data, r)

    if args.check:
        if not os.path.exists(OUT_JSON):
            r.fail("epub-build.json yok", "`epub.py` çalıştırın")
            return r.finish(None)
        with open(OUT_JSON, encoding="utf-8") as fh:
            old = json.load(fh)
        r.add(old.get("perStory") == data["perStory"], "EPUB raporu güncel",
              "BAYAT — proza veya görsel değişmiş")
        return r.finish(None)

    os.makedirs(mb.REPORTS_TRACKED, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"\n  ✎ {os.path.relpath(OUT_JSON, mb.ROOT)}")
    print(f"  ✎ {data['epub']}  (DEPO DIŞINDA — proza içerir)")
    return r.finish(None)


if __name__ == "__main__":
    sys.exit(main())
