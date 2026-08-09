#!/usr/bin/env python3
"""
ARA PROVA DİZGİSİ — FAZ 2 MÜHENDİSLİK PROVASI
================================================================================
    python3 04_BUILD/proof_interior.py            prova üret + rapor yaz
    python3 04_BUILD/proof_interior.py --check    kayıtlı rapor bayat mı

⚠ BU KDP ÜRETİMİ DEĞİLDİR. Nihai dizgi Faz 5'in işidir (yol haritası § 16).
Buradaki amaç YAPISAL REGRESYON AVIDIR: taşma, kırpılma, eksik görsel,
yanlış hikâye sırası, bozuk başlık, sayfa geometrisi, beklenmedik uzunluk.

NE ÜRETİR
  08_OUTPUT/paperback/proof-interior.pdf   ← PROZA İÇERİR, DEPODA DURMAZ
  06_REPORTS/tracked/proof-interior.json   ← YALNIZCA SAYI, depoda durur

İkinci dosyanın içinde tek bir hikâye cümlesi bile yoktur (Bestiarium D38 /
karar K21): manuscript depo dışındadır ve bir rapor onu geri sızdıramaz.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb
import editions as ed_mod
import page_budget as pb

OUT_PDF = os.path.join(mb.ROOT, "08_OUTPUT", "paperback", "proof-interior.pdf")
OUT_JSON = os.path.join(mb.REPORTS_TRACKED, "proof-interior.json")

BODY_FONT = "Times-Roman"
HEAD_FONT = "Times-Bold"


def layout() -> dict:
    """Gerçek tipografiyle dizer ve YAPISAL kusur arar."""
    from reportlab.lib.pagesizes import inch
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase.pdfmetrics import stringWidth

    book = mb.load_book()
    stories = mb.book_stories(book)
    if not stories:
        return {}

    index = mb.load_stories()
    by_id = {s["id"]: s for s in index.get("stories", [])}
    parts = {p["id"]: p for p in index.get("parts", [])}

    ed = ed_mod.get("paperback")
    t = ed.typography
    target_pages = mb.PAGE_TARGET

    w_in, h_in = ed_mod.text_block(ed, target_pages)
    width_pt, height_pt = w_in * 72, h_in * 72
    gutter = ed_mod.required_gutter(target_pages)
    lead = t.leading_pt
    lines_per_page = ed_mod.lines_per_page(ed, target_pages)

    # Açılış illüstrasyonu sayfanın ÜST YARISINI kaplar (page_budget MODEL)
    illo_share = pb.MODEL["opening_illustration_page_share"]
    illo_lines = int(lines_per_page * illo_share)

    os.makedirs(os.path.dirname(OUT_PDF), exist_ok=True)
    c = canvas.Canvas(OUT_PDF, pagesize=(ed.trim_w_in * inch, ed.trim_h_in * inch))

    written = sorted(
        (s for s in stories.items()),
        key=lambda kv: by_id.get(kv[0], {}).get("number") or 999,
    )

    # ⚠ PARAGRAF ARALIĞI BİR TASARIM KARARIDIR VE SAYFA SAYISINI OYNATIR.
    #
    # `page_budget` modeli metin sayfasını `kelime / kelime-sayfa` olarak
    # hesaplar; bu, paragrafların GİRİNTİYLE ayrıldığı ve aralarında BOŞ
    # SATIR OLMADIĞI standart kitap dizgisini varsayar. İlk prova sürümü
    # her paragraftan sonra boş satır bırakıyordu ve 16 hikâyenin 11'ini
    # modelin bir sayfa üstüne çıkardı. Kusur modelde değil, provanın
    # varsayımındaydı — ama DUYARLILIK gerçektir ve rapora yazılır:
    # hikâye başına ~24 paragraf, boş satırlı dizgide ~0,74 sayfa demektir
    # ve 45 hikâyede ~33 sayfa eder. Faz 4 nihai kilidi verirken bu sayıyı
    # bilerek verir (§ 26: ölç, anomaliyi kaydet, erken kilitleme).
    INDENT_PT = 12.0

    def wrap(text: str, font: str, size: float, maxw: float,
             blank_between: bool = False) -> list[tuple[str, bool]]:
        """(satır, girintili_mi) listesi."""
        out: list[tuple[str, bool]] = []
        for para in mb.paragraphs(text):
            cur, first = "", True
            avail = maxw - INDENT_PT
            for word in para.split():
                trial = word if not cur else cur + " " + word
                if stringWidth(trial, font, size) <= avail:
                    cur = trial
                else:
                    out.append((cur, first)); first = False; avail = maxw; cur = word
            if cur:
                out.append((cur, first))
            if blank_between:
                out.append(("", False))
        return out

    per_story, page_no, issues = [], 0, []
    card_issues: list[str] = []
    prev_number = 0

    # --- KÜLTÜR KARTI: K27'nin varsayımını GERÇEK METİNLE sına ---
    #
    # K27 kültür kartına ayrı sayfa vermez; kart, hikâyenin kuyruğunda ZATEN
    # ÖDENEN boşlukta durur. Karar verilirken o boşluğa "vinyet ≈ 10 satır +
    # üç cümle ≈ 3 satır + harita işareti ≈ 2 satır" sığacağı varsayılmıştı.
    #
    # "Üç cümle ≈ 3 satır" bir TAHMİNDİ ve ölçülemezdi, çünkü kart metinleri
    # Faz 3'ün teslimidir: karar verildiğinde ölçülecek metin yoktu. Şimdi var.
    cultures_idx = mb.load_cultures()
    card_by_culture = {c["id"]: c for c in cultures_idx.get("cultures", [])
                       if c.get("status") == "locked"}
    # Kart, o kültürün İLK hikâyesinin kuyruğunda durur.
    first_story_of_culture: dict[str, str] = {}
    for _sid, _s in written:
        cid = by_id.get(_sid, {}).get("cultureId")
        if cid and cid not in first_story_of_culture:
            first_story_of_culture[cid] = _sid
    card_host = {v: k for k, v in first_story_of_culture.items()}

    for sid, s in written:
        rec = by_id.get(sid, {})
        number = rec.get("number")
        # --- YAPISAL: hikâye sırası artıyor mu ---
        if number is not None:
            if number <= prev_number:
                issues.append(f"{sid}: hikâye sırası geriye gitti ({prev_number} → {number})")
            prev_number = number

        # --- YAPISAL: başlık var mı ---
        title = (s.get("title") or "").strip()
        if not title:
            issues.append(f"{sid}: başlık yok")
        title_lines = []
        cur = ""
        for word in title.split():
            trial = word if not cur else cur + " " + word
            if stringWidth(trial, HEAD_FONT, 18) <= width_pt:
                cur = trial
            else:
                title_lines.append(cur); cur = word
        if cur:
            title_lines.append(cur)
        # Uzun başlık bir kusur değildir; İKİ SATIRA sığmaması kusurdur.
        if len(title_lines) > 2:
            issues.append(f"{sid}: başlık iki satıra sığmıyor ({len(title_lines)} satır)")

        # --- YAPISAL: görsel eşlemesi ---
        image_id = rec.get("imageId")
        if not image_id:
            issues.append(f"{sid}: imageId yok — açılış görseli eşlenmemiş")
        raw = os.path.join(mb.ROOT, "07_ASSETS", "raw", f"{image_id}.png") if image_id else None
        image_present = bool(raw and os.path.exists(raw))

        body = wrap(s.get("text", ""), BODY_FONT, t.body_pt, width_pt)
        note = wrap(s.get("culturalNote") or "", BODY_FONT, t.body_pt - 1, width_pt)
        # DUYARLILIK: aynı metin, paragraf arası boş satırlı dizgide
        body_spaced = wrap(s.get("text", ""), BODY_FONT, t.body_pt, width_pt,
                           blank_between=True)

        # --- dizgi: her hikâye YENİ SAYFADA başlar ---
        page_no += 1
        first_page_lines = lines_per_page - illo_lines - 3   # görsel + başlık bloğu
        cursor = 0
        story_pages = 1

        c.setFont(HEAD_FONT, 18)
        x = gutter * 72
        y = (ed.trim_h_in - t.margin_top_in) * 72
        # illüstrasyon yeri: çerçeve çiz (üretimde görsel gelecek)
        c.rect(x, y - illo_lines * lead, width_pt, illo_lines * lead)
        c.setFont(HEAD_FONT, 9)
        c.drawString(x + 6, y - illo_lines * lead + 6,
                     f"[{image_id or '—'}] {'RAW PRESENT' if image_present else 'RAW PENDING'}")
        c.setFont(HEAD_FONT, 18)
        ty = y - illo_lines * lead - 24
        for tl in title_lines[:2]:
            c.drawString(x, ty, tl); ty -= 22
        yy = ty - lead
        c.setFont(BODY_FONT, t.body_pt)

        avail = first_page_lines
        while cursor < len(body):
            if avail <= 0:
                c.showPage(); page_no += 1; story_pages += 1
                yy = (ed.trim_h_in - t.margin_top_in) * 72
                avail = lines_per_page
                c.setFont(BODY_FONT, t.body_pt)
            line, indented = body[cursor]; cursor += 1
            if line:
                c.drawString(x + (INDENT_PT if indented else 0), yy, line)
            yy -= lead; avail -= 1

        # kültürel not — hikâyenin sonunda, tipografik olarak ayrı
        if avail < len(note) + 2:
            c.showPage(); page_no += 1; story_pages += 1
            yy = (ed.trim_h_in - t.margin_top_in) * 72
            avail = lines_per_page
        yy -= lead
        c.setFont(BODY_FONT, t.body_pt - 1)
        for line, _ in note:
            if line:
                c.drawString(x, yy, line)
            yy -= lead; avail -= 1

        # --- YAPISAL: taşma denetimi ---
        bottom_limit = t.margin_bottom_in * 72
        if yy < bottom_limit - lead:
            issues.append(f"{sid}: metin alt marjın altına TAŞTI")

        modelled = pb.compute(354.2)["billedPagesPerStory"]

        # --- KÜLTÜR KARTI KUYRUĞA SIĞIYOR MU (K27) ---
        #
        # ⚠ KUYRUK BOŞLUĞU FATURALANAN SAYFAYA GÖRE ÖLÇÜLÜR (Faz 4 düzeltmesi).
        #
        # Faz 3'te bu satır `max(0, avail)` yazıyordu — yani KULLANILAN son
        # sayfada kalan satır. O ölçü, hikâye 4 sayfadan AZ tuttuğunda yanlış
        # cevap verir: `inuit-sedna` 3 sayfada dizildi ve ölçü "3 satır boş"
        # dedi, oysa model o hikâye için 4 SAYFA FATURALIYOR ve dördüncü
        # sayfanın 32 satırı da ödenmiş boşluktur.
        #
        # K27'nin bütün argümanı "boşluk zaten ödeniyor" üzerine kuruludur,
        # dolayısıyla doğru payda FATURALANAN kapasitedir, kullanılan değil.
        # Yanlış ölçü iki kültürü (inuit, maya) haksız yere "sığmıyor"
        # göstermişti.
        used_lines = (first_page_lines + (story_pages - 1) * lines_per_page) - avail
        billed_capacity = first_page_lines + (modelled - 1) * lines_per_page
        tail_free = max(0, billed_capacity - used_lines)
        card_lines = None
        card_fits = None
        cid = card_host.get(sid)
        if cid and card_by_culture.get(cid, {}).get("cardText"):
            ct = card_by_culture[cid]["cardText"]
            sentences = " ".join(ct[k] for k in ("whoTells", "where", "today"))
            heading = f"{card_by_culture[cid]['name']} — {ct['language']}"
            card_text_lines = (len(wrap(sentences, BODY_FONT, t.body_pt - 1, width_pt))
                               + len(wrap(heading, HEAD_FONT, t.body_pt, width_pt)))
            card_lines = (card_text_lines
                          + pb.MODEL["culture_card_vignette_lines"]
                          + pb.MODEL["culture_card_map_lines"]
                          + pb.MODEL["culture_card_gap_lines"])
            card_fits = card_lines <= tail_free
            if not card_fits:
                card_issues.append(
                    f"{sid}: {cid} kartı kuyruğa sığmıyor "
                    f"({card_lines} satır gerekiyor, {tail_free} satır boş)")

        c.showPage()

        # boş satırlı dizgide kaç sayfa ederdi (ölçüm, uygulanmadı)
        spaced_lines = len(body_spaced)
        spaced_pages = 1 + max(0, -(-(spaced_lines - first_page_lines) // lines_per_page))
        per_story.append({
            "id": sid, "number": number, "part": rec.get("partId"),
            "words": mb.word_count(s.get("text", "")),
            "paragraphs": len(mb.paragraphs(s.get("text", ""))),
            "pages": story_pages, "modelledPages": modelled,
            "pagesIfParagraphSpaced": spaced_pages,
            "imageId": image_id, "rawPresent": image_present,
            "tailLinesFree": tail_free,
            "cultureCardId": cid, "cultureCardLines": card_lines,
            "cultureCardFits": card_fits,
        })
        if story_pages > modelled + 1:
            issues.append(f"{sid}: {story_pages} sayfa — model {modelled} diyor (beklenmedik uzunluk)")

    c.save()

    over = [p for p in per_story if p["pages"] > p["modelledPages"]]
    return {
        "$comment": [
            "ARA PROVA — FAZ 2 MÜHENDİSLİK PROVASI. KDP üretimi DEĞİLDİR.",
            "Bu dosya YALNIZCA SAYI içerir; tek bir hikâye cümlesi bile yoktur",
            "(karar K21 · Bestiarium D38). PDF depo dışındadır.",
            "Üretici: 04_BUILD/proof_interior.py",
        ],
        "gate": mb.read_gate(),
        "isKdpProduction": False,
        "geometry": {
            "trimIn": [ed.trim_w_in, ed.trim_h_in],
            "textBlockIn": [round(w_in, 4), round(h_in, 4)],
            "gutterIn": gutter, "bodyPt": t.body_pt, "leadingPt": lead,
            "linesPerPage": lines_per_page, "illustrationLines": illo_lines,
        },
        "stories": len(per_story),
        "bodyPages": page_no,
        "perStory": per_story,
        "storiesOverModel": len(over),
        "cardIssues": card_issues,
        "cultureCards": {
            "measured": sum(1 for p in per_story if p["cultureCardLines"] is not None),
            "fit": sum(1 for p in per_story if p["cultureCardFits"] is True),
            "tightest": min(
                ((p["tailLinesFree"] - p["cultureCardLines"], p["cultureCardId"])
                 for p in per_story if p["cultureCardLines"] is not None),
                default=(None, None))[0],
        },
        "rawImagesPresent": sum(1 for p in per_story if p["rawPresent"]),
        "rawImagesExpected": len(per_story),
        "issues": issues,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Ara prova dizgisi")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    print("═" * 72)
    print("  ARA PROVA DİZGİSİ · FAZ 2 (KDP ÜRETİMİ DEĞİL)")
    print("═" * 72)

    r = mb.Result("proof_interior", verbose=args.verbose)

    try:
        data = layout()
    except ImportError:
        r.ok("reportlab yok — prova atlandı", "ağır bağımlılık; ana doğrulama işi etkilenmez")
        return r.finish(None)

    if not data:
        # Manuscript yoksa bu bir HATA DEĞİL, "uygulanamaz"dır (K21: depo public,
        # manuscript değil). Ama kayıtlı rapor DEPODA olmak zorundadır.
        print("\n  manuscript yerelde yok — prova UYGULANAMAZ (K21).")
        r.add(os.path.exists(OUT_JSON),
              "kayıtlı prova raporu depoda (06_REPORTS/tracked/)",
              "proof-interior.json yok — denetlenecek rapor depoda durmuyorsa "
              "o denetim ÖLÜ KURALDIR (karar K18)")
        return r.finish(None)

    g = data["geometry"]
    print(f"\n  metin bloğu   : {g['textBlockIn'][0]}\" × {g['textBlockIn'][1]}\" · "
          f"{g['linesPerPage']} satır/sayfa · illüstrasyon {g['illustrationLines']} satır")
    print(f"  hikâye        : {data['stories']}")
    print(f"  gövde sayfası : {data['bodyPages']}")
    print(f"  ham görsel    : {data['rawImagesPresent']}/{data['rawImagesExpected']}")
    print()
    for p in data["perStory"]:
        flag = "  ←" if p["pages"] > p["modelledPages"] else ""
        print(f"    {str(p['number']).rjust(3)} {p['id'][:30]:<30} "
              f"{p['words']:>5}w  {p['pages']} sayfa (model {p['modelledPages']}){flag}")

    if args.check:
        if not os.path.exists(OUT_JSON):
            r.fail("proof-interior.json yok", "`proof_interior.py` çalıştırın")
            return r.finish(None)
        with open(OUT_JSON, encoding="utf-8") as fh:
            old = json.load(fh)
        same = (old.get("perStory") == data["perStory"]
                and old.get("geometry") == data["geometry"])
        r.add(same, "prova raporu güncel",
              "BAYAT — proza veya tipografi değişmiş; `proof_interior.py` çalıştırın")
        return r.finish(None)

    r.add(not data["issues"], f"yapısal kusur yok ({data['stories']} hikâye dizildi)",
          "PROVA KUSURLARI:\n         " + "\n         ".join(data["issues"][:12]))
    r.add(data["storiesOverModel"] == 0,
          "hiçbir hikâye sayfa modelini aşmıyor",
          f"modeli aşan: {data['storiesOverModel']} hikâye — sayfa bütçesi yeniden ölçülmeli")
    # --- KÜLTÜR KARTI KUYRUK UYUMU — K27'nin gerçek metinle ilk sınavı ---
    #
    # Şiddet seviyesi KAPIYA BAĞLIDIR ve bu, yol haritasının sayfa bütçesi
    # için zaten kullandığı kuralın aynısıdır: § 16 Faz 4 "sayfa bütçesi
    # artık UYARI DEĞİL HATA" der. Gerekçe: A4/K27 bir KURUCU KARARIDIR ve
    # yol haritası onun KİLİTLENMESİNİ Faz 4'e koyar. Faz 3'ün işi ölçmek ve
    # sapmayı belgelemek; Faz 4'ün işi karar vermek ve kilitlemek.
    gate = mb.read_gate()
    cards = data["cultureCards"]
    card_ok = not data["cardIssues"]
    card_msg = (f"kültür kartları hikâye kuyruğuna sığıyor "
                f"({cards['fit']}/{cards['measured']} ölçüldü)")
    card_detail = ("SIĞMAYAN KART:\n         " + "\n         ".join(data["cardIssues"][:12])
                   + "\n         K27 kart için EK SAYFA ayırmaz: kart, hikâyenin ZATEN "
                     "ÖDENEN kuyruk boşluğunda durur. Sığmazsa kitap 228 sayfayı aşar "
                     "ve ciltsiz telif düşer. Kartın yeri kültürün İLK hikâyesidir — "
                     "kart kültürü tanıtır, dolayısıyla daha bol kuyruklu bir hikâyeye "
                     "kaydırmak editoryal olarak yanlıştır.")
    if mb.gate_at_least(gate, "phase4"):
        r.add(card_ok, card_msg, card_detail)
    else:
        r.warn(card_ok, card_msg, card_detail)

    r.warn(data["rawImagesPresent"] == data["rawImagesExpected"],
           f"açılış görselleri hazır ({data['rawImagesPresent']}/{data['rawImagesExpected']})",
           f"{data['rawImagesExpected'] - data['rawImagesPresent']} ham görsel bekliyor — "
           "kurucu üretimi (yol haritası § 21 · H7). Yazım fazını BLOKLAMAZ.")

    os.makedirs(mb.REPORTS_TRACKED, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"\n  ✎ {os.path.relpath(OUT_JSON, mb.ROOT)}")
    print(f"  ✎ {os.path.relpath(OUT_PDF, mb.ROOT)}  (DEPO DIŞINDA — proza içerir)")
    return r.finish(None)


if __name__ == "__main__":
    sys.exit(main())
