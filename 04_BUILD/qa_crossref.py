#!/usr/bin/env python3
"""
ÇAPRAZ REFERANS VE KAPSAM KAPISI
================================================================================
Bestiarium'un çapraz referans kapısı "akraba imgeler" bağlarını denetliyordu
— bir BESTİYERDE okurun aradığı şey odur. Bir HİKÂYE ANTOLOJİSİNDE hikâyeler
arası zorunlu gönderme anlatıyı böler (LESSONS § G).

Buradaki soru başka: yol haritasının ek malzeme vaadi tutuyor mu?

    "Ek malzeme: Telaffuz rehberi · 'kim kimdir' sözlüğü · her hikâye
     sonunda 2 satırlık kültürel not"
    Gerekçe: "Öğretmen ve kütüphaneci için satın alma gerekçesi;
              İADE ORANINI DÜŞÜRÜR."

Yani bu üçü ticari vaattir. Eksik bir telaffuz kaydı, tam da satın alma
gerekçesini çürütür.
"""

from __future__ import annotations

import argparse
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb


def main() -> int:
    ap = argparse.ArgumentParser(description="Çapraz referans ve kapsam kapısı")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  ÇAPRAZ REFERANS VE KAPSAM")
    print("═" * 72)

    r = mb.Result("qa_crossref", verbose=args.verbose)
    gate = mb.read_gate()

    index = mb.load_stories()
    cultures = mb.load_cultures()
    entries = [s for s in index.get("stories", []) if s.get("status") != "dropped"]
    culture_map = mb.culture_by_id(cultures)
    locked_cultures = [c for c in cultures.get("cultures", []) if c.get("status") == "locked"]

    if not entries:
        r.ok("hikâye dizini boş — kapsam denetimi boş koştu",
             f"kapı {gate}; envanter Faz 1'in birinci işi")
        # Kültür tarafı yine de denetlenebilir
    # --------------------------------------------------- telaffuz benzersizliği
    pron_names = collections.defaultdict(set)
    for s in entries:
        for p in (s.get("pronunciationEntries") or []):
            pron_names[p.get("name", "")].add(p.get("pronunciation", ""))
    conflicting = {k: sorted(v) for k, v in pron_names.items() if len(v) > 1}
    r.add(not conflicting, f"her ad için tek telaffuz ({len(pron_names)} ad)",
          f"çelişen telaffuz: {list(conflicting.items())[:6]} — "
          "telaffuz rehberi kendi içinde çelişemez")

    # --------------------------------------------------- sözlük kimlik çakışması
    glossary = collections.defaultdict(set)
    for s in entries:
        for c in (s.get("characters") or []):
            if c.get("glossary", True):
                glossary[c.get("name", "")].add(s["id"])
    r.ok(f"'kim kimdir' sözlüğü {len(glossary)} kişi taşıyor")

    # --------------------------------------------- kültür kartı / vinyet kapsamı
    if mb.gate_at_least(gate, "phase1"):
        no_vignette = [c["id"] for c in locked_cultures if not c.get("vignetteId")]
        r.add(not no_vignette, f"her kilitli kültürün vinyeti tanımlı ({len(locked_cultures)})",
              f"vinyetsiz: {no_vignette[:10]} — yol haritası 22 kültür vinyeti diyor")

        no_map = [c["id"] for c in locked_cultures if not c.get("mapPoint")]
        r.add(not no_map, "her kilitli kültürün harita noktası var",
              f"harita noktası olmayan: {no_map[:10]} — dünya haritası yol haritasının "
              "zorunlu kıldığı TEK görseldir ve 22 kültürün konumunu gösterir")

    # ------------------------------------------------------- metin tarafı
    book = mb.load_book()
    stories = mb.book_stories(book)
    if not stories:
        r.ok("metin yok — metin kapsamı boş koştu")
        return r.finish(args.json)

    by_id = {s["id"]: s for s in entries}

    # ① metindeki her özel ad telaffuz rehberinde mi
    missing_pron, missing_gloss = [], []
    for sid, s in sorted(stories.items()):
        entry = by_id.get(sid)
        if not entry:
            r.fail(f"{sid} metinde var ama dizinde yok", "story_index.json ile ayrışma")
            continue
        # ⚠ KÜNYE ↔ METİN TOKENIZER'I TEK YERDEN GELİR (Faz 3 düzeltmesi).
        # Eskiden künye adı burada elle parçalanıyordu ve metin tarafı
        # `mb.words()` kullanıyordu — iki ayrı tokenizer, garantili ayrışma.
        # Kesme işaretini HARF olarak kullanan adlar ("Chang’e", "K’iche’")
        # hiçbir zaman eşleşemiyordu. Gerekçe: mythbook.declared_tokens().
        declared = {p["name"] for p in (entry.get("pronunciationEntries") or [])}
        declared_words = mb.declared_tokens(declared)
        gloss = {c["name"] for c in (entry.get("characters") or [])}
        gloss_words = mb.declared_tokens(gloss)

        # ⚠ D32 DÜZELTMESİ (Faz 1) — DOĞRU METNİ REDDEDEN CETVEL.
        #
        # Burada eskiden `mb.is_proper_name()` ham hâliyle sayılıyor, cümle
        # başı ise şu koruma ile eleniyordu:
        #     re.search(r"(?<![.!?…]\s)\b" + name + r"\b", text)
        # Bu korumanın kör noktası PARAGRAF BAŞIDIR: bir sözcük "\n\n"den
        # sonra geliyorsa kendinden önce ".!?…" + boşluk YOKTUR, koruma
        # devreye girmez ve sıradan sözcük özel ad sayılır. Pilot hikâye
        # kapıyı tam olarak böyle kırmızı yaktı: “The” (×21), “Twice” (×3),
        # “They” (×2) — üçü de paragraf başı, üçü de özel ad değil.
        #
        # `mythbook.proper_names()` bu işi zaten DOĞRU yapıyor (cümlenin ilk
        # sözcüğünü atlar) ve kendi docstring'i "gerçek özel adlar için
        # proper_names() kullanın" diye uyarıyor. qa_readability onu
        # kullanıyordu; bu kapı kullanmıyordu. Tek doğruluk kaynağına
        # bağlandı — iki ayrı ad tespiti tutmak, ikisinin ayrışmasını
        # garanti eder.
        real_names = mb.proper_names(s.get("text", ""))
        counts = collections.Counter(mb.words(s.get("text", "")))
        for name in sorted(real_names):
            if len(name) < 3:
                continue
            count = counts[name]
            # ⚠ İYELİK EKİ DÜZELTMESİ (Faz 2) — D32 sınıfının aynısı.
            #
            # `declared_words` kurulurken künye adı kesme işaretinden BÖLÜNÜR
            # ("Arachne" → {"Arachne"}), ama metinden gelen belirteç
            # BÖLÜNMEZ: "Arachne’s" tek parça gelir ve hiçbir zaman eşleşmez.
            # Sonuç: doğru yazılmış bir iyelik, telaffuz rehberinde EKSİK
            # sanılır. Pilot hikâyede özel ad iyelik hâlinde hiç geçmediği
            # için Faz 1'de görünmedi; ölçek bunu ilk Yunan partisinde
            # ortaya çıkardı — Faz 2'nin var oluş sebebi tam olarak budur.
            #
            # Kapı KÖRLEŞMEZ: yalnızca iyelik eki soyulur, ad hâlâ
            # künyelenmiş olmak zorundadır (selftest iki yönlü sınar).
            base = re.sub(r"[’']s$", "", name)
            if name not in declared_words and base not in declared_words:
                missing_pron.append(f"{sid}: “{name}” (×{count})")
            if not ({name, base} & (gloss_words | declared_words)):
                missing_gloss.append(f"{sid}: “{name}” (×{count})")

    r.add(not missing_pron, "metindeki her özel ad telaffuz rehberinde",
          "eksik:\n         " + "\n         ".join(missing_pron[:12])
          + "\n         Yol haritası telaffuz rehberini TİCARİ bir gerekçeyle koydu: "
            "'öğretmen ve kütüphaneci için satın alma gerekçesi; iade oranını düşürür.'")

    r.warn(not missing_gloss, "metindeki adlar 'kim kimdir' sözlüğünde",
           f"sözlükte olmayan: {missing_gloss[:10]}")

    # ② kültürel not kapsamı
    no_note = [sid for sid, s in stories.items() if not (s.get("culturalNote") or "").strip()]
    r.add(not no_note, "her hikâyenin kültürel notu var", f"eksik: {no_note[:10]}")

    # ③ dizinde yazılı işaretli ama metni olmayan hikâyeler
    written_flag = {s["id"] for s in entries
                    if s.get("status") in {"written", "edited", "age-reviewed", "final"}}
    ghosts = sorted(written_flag - set(stories))
    r.add(not ghosts, "yazılı işaretli her hikâyenin metni var",
          f"metni olmayan: {ghosts[:10]} — dizin ile manuscript ayrışmış")

    return r.finish(args.json)


if __name__ == "__main__":
    sys.exit(main())
