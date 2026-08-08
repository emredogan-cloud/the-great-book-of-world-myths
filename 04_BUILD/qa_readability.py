#!/usr/bin/env python3
"""
OKUNABİLİRLİK KAPISI — 8–12 YAŞ
================================================================================
Codex Bestiarium'da bu kapı YOKTUR; ihtiyacı yoktu. Burada zorunludur:
"8–12 yaş" bir pazarlama etiketi değil, ÖLÇÜLEBİLİR bir okuma seviyesidir
ve "sıcak, hızlı" bir üslup iddiası ölçülmeden doğrulanamaz.

ALT SINIRLAR DA VARDIR ve bilerek konmuştur. Çok kısa cümle ve çok düşük
sınıf seviyesi 12 yaşındaki okuru AŞAĞILAR ve kitabı "küçüklere" iter —
alt başlıktaki "Ages 8–12" vaadini üst uçtan kırar. Yol haritasının okuru
"Percy Jackson'ı bitirmiş" çocuktur.

ÖZEL ADLAR HESAPTAN ÇIKARILIR. Aksi hâlde Väinämöinen ve Amaterasu kitabı
yapay olarak "zor" gösterir ve kapı, kitabın KÜLTÜREL KAPSAMINI cezalandırır.
Bu, Bestiarium'un D32 kusurunun aynı sınıfıdır: doğru metni reddeden bir
cetvel.
"""

from __future__ import annotations

import argparse
import os
import re
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb

PASSIVE = re.compile(
    r"\b(?:was|were|is|are|been|being|be)\s+(?:\w+ly\s+)?\w+(?:ed|en|wn|ne)\b", re.I
)


def analyse(text: str) -> dict:
    sents = mb.sentences(text)
    all_words = mb.words(text)
    # Özel adlar çıkarılır — kültürel kapsam cezalandırılmaz.
    # Cümle başı büyük harfleri özel ad SAYILMAZ (mythbook.proper_names).
    proper_set = mb.proper_names(text)
    common = [w for w in all_words if w not in proper_set]
    proper = sorted(proper_set)

    if not sents or not common:
        return {}

    syl = [mb.syllables(w) for w in common]
    hard = [w for w, n in zip(common, syl) if n >= 3]

    words_per_sentence = len(all_words) / len(sents)
    syl_per_word = sum(syl) / len(common)

    # Flesch–Kincaid Grade Level
    fk = 0.39 * words_per_sentence + 11.8 * syl_per_word - 15.59

    passive = len(PASSIVE.findall(text))

    return {
        "sentences": len(sents),
        "words": len(all_words),
        "words_per_sentence": words_per_sentence,
        "syllables_per_word": syl_per_word,
        "hard_word_share": len(hard) / len(common),
        "flesch_kincaid": fk,
        "passive_share": passive / len(sents),
        "proper_names": proper,
        "paragraph_avg": (statistics.mean([len(mb.sentences(p)) for p in mb.paragraphs(text)])
                          if mb.paragraphs(text) else 0),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Okunabilirlik kapısı (8–12 yaş)")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  OKUNABİLİRLİK · 8–12 YAŞ")
    print("═" * 72)

    r = mb.Result("qa_readability", verbose=args.verbose)
    book = mb.load_book()
    stories = mb.book_stories(book)

    if not stories:
        r.ok("metin yok — kapı boş koştu", "körlüğü 05_TESTS/selftest.py sınar")
        return r.finish(args.json)

    fk_lo, fk_hi = mb.BANDS["flesch_kincaid"]
    fk_flo, fk_fhi = mb.BANDS["flesch_kincaid_fail"]
    syl_lo, syl_hi = mb.BANDS["syllables_per_word"]
    syl_fail = mb.BANDS["syllables_per_word_fail_high"]
    hard_warn = mb.BANDS["hard_word_share"]
    hard_fail = mb.BANDS["hard_word_share_fail"]
    pass_warn = mb.BANDS["passive_share"]
    pass_fail = mb.BANDS["passive_share_fail"]
    name_cap = mb.BANDS["proper_names_per_story"]

    fk_all, fk_fail, fk_warn = [], [], []
    syl_fail_list, syl_warn_list = [], []
    hard_fail_list, hard_warn_list = [], []
    passive_fail_list, passive_warn_list = [], []
    name_overflow, para_warn = [], []

    for sid, s in sorted(stories.items()):
        m = analyse(s.get("text", ""))
        if not m:
            continue
        fk_all.append(m["flesch_kincaid"])

        if not (fk_flo <= m["flesch_kincaid"] <= fk_fhi):
            fk_fail.append(f"{sid}: {m['flesch_kincaid']:.1f}")
        elif not (fk_lo <= m["flesch_kincaid"] <= fk_hi):
            fk_warn.append(f"{sid}: {m['flesch_kincaid']:.1f}")

        if m["syllables_per_word"] > syl_fail:
            syl_fail_list.append(f"{sid}: {m['syllables_per_word']:.2f}")
        elif not (syl_lo <= m["syllables_per_word"] <= syl_hi):
            syl_warn_list.append(f"{sid}: {m['syllables_per_word']:.2f}")

        if m["hard_word_share"] > hard_fail:
            hard_fail_list.append(f"{sid}: %{m['hard_word_share'] * 100:.1f}")
        elif m["hard_word_share"] > hard_warn:
            hard_warn_list.append(f"{sid}: %{m['hard_word_share'] * 100:.1f}")

        if m["passive_share"] > pass_fail:
            passive_fail_list.append(f"{sid}: %{m['passive_share'] * 100:.0f}")
        elif m["passive_share"] > pass_warn:
            passive_warn_list.append(f"{sid}: %{m['passive_share'] * 100:.0f}")

        if len(m["proper_names"]) > name_cap:
            name_overflow.append(f"{sid}: {len(m['proper_names'])} ad "
                                 f"({', '.join(m['proper_names'][:9])}…)")

        plo, phi = mb.BANDS["paragraph_avg"]
        if m["paragraph_avg"] and not (plo <= m["paragraph_avg"] <= phi):
            para_warn.append(f"{sid}: {m['paragraph_avg']:.1f} cümle/paragraf")

    r.add(not fk_fail,
          f"Flesch–Kincaid sınıf seviyesi güvenli aralıkta ({fk_flo}–{fk_fhi})",
          f"aralık dışı: {fk_fail[:10]} — ÜST uç kitabı 8 yaşındakiden, "
          f"ALT uç 12 yaşındakinden koparır")
    r.warn(not fk_warn, f"Flesch–Kincaid hedef bandında ({fk_lo}–{fk_hi})",
           f"hedef bandı dışında: {fk_warn[:10]}")

    r.add(not syl_fail_list, f"hece/kelime ≤{syl_fail}",
          f"aşan: {syl_fail_list[:10]}")
    r.warn(not syl_warn_list, f"hece/kelime hedef bandında ({syl_lo}–{syl_hi})",
           f"bant dışı: {syl_warn_list[:10]}")

    r.add(not hard_fail_list, f"zor sözcük oranı ≤%{hard_fail * 100:.0f}",
          f"aşan: {hard_fail_list[:10]} (özel adlar hesaba KATILMAZ)")
    r.warn(not hard_warn_list, f"zor sözcük oranı hedefte (≤%{hard_warn * 100:.0f})",
           f"hedef üstü: {hard_warn_list[:10]}")

    r.add(not passive_fail_list, f"pasif cümle oranı ≤%{pass_fail * 100:.0f}",
          f"aşan: {passive_fail_list[:10]}")
    r.warn(not passive_warn_list, f"pasif cümle oranı hedefte (≤%{pass_warn * 100:.0f})",
           f"hedef üstü: {passive_warn_list[:10]}")

    r.add(not name_overflow, f"hikâye başına yeni özel ad ≤{name_cap}",
          "aşan:\n         " + "\n         ".join(name_overflow[:10])
          + "\n         Sekiz yeni ad taşıyan bir hikâye 9 yaşındaki okuru kaybeder "
            "ve telaffuz rehberini kullanılmaz hâle getirir.")

    r.warn(not para_warn, "paragraf uzunluğu hedefte", f"hedef dışı: {para_warn[:10]}")

    if fk_all:
        print(f"\n  kitap geneli Flesch–Kincaid: {statistics.mean(fk_all):.2f} "
              f"(en düşük {min(fk_all):.1f} · en yüksek {max(fk_all):.1f})")

    return r.finish(args.json)


if __name__ == "__main__":
    sys.exit(main())
