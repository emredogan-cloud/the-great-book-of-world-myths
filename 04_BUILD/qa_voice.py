#!/usr/bin/env python3
"""
SES VE YASAK KALIP KAPISI
================================================================================
CHILDREN_WRITING_STYLE § 2, § 3.1, § 6.

Ölçtükleri:
  · yasak kalıplar (kitabın kendine göndermesi, ders veren kapanış, …)
  · cümle ortalaması ve en uzun cümle
  · paragraf uzunluğu
  · diyalog payı
  · tipografi (tırnak dengesi, düz kesme, em dash, çift boşluk)
  · KÜLTÜREL NOT ŞABLONLAŞMASI  ← Bestiarium'un en pahalı Faz 4 dersi

Son madde bu projeye özgüdür. Bestiarium'da etik kısıt cümlesi üç yerde
boilerplate'e döndü: "kısıt cümlesi kalıplaşırsa okur onu ATLAMAYI ÖĞRENİR."
Bu kitapta 45 kültürel not var ve hepsi kalıplaşmaya açık.
"""

from __future__ import annotations

import argparse
import collections
import os
import re
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb

DIALOGUE = re.compile(r"[“\"][^”\"]{2,}[”\"]")


def sentence_stats(text: str):
    sents = mb.sentences(text)
    lengths = [mb.word_count(s) for s in sents if mb.word_count(s) > 0]
    return sents, lengths


def note_skeleton(note: str) -> str:
    """
    Kültürel notun 'iskeleti': içerik sözcükleri atılır, yapı kalır.
    İki not aynı iskeleti taşıyorsa aynı cümle kalıbıyla yazılmışlardır.
    """
    words = [w.lower() for w in mb.words(note)]
    # 4 harften uzun sözcükler içeriktir; kısa olanlar yapıdır
    return " ".join(w if len(w) <= 4 else "·" for w in words[:24])


def main() -> int:
    ap = argparse.ArgumentParser(description="Ses ve yasak kalıp kapısı")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  SES VE YASAK KALIP")
    print("═" * 72)

    r = mb.Result("qa_voice", verbose=args.verbose)
    book = mb.load_book()
    stories = mb.book_stories(book)

    if not stories:
        r.ok("metin yok — kapı boş koştu", "körlüğü 05_TESTS/selftest.py sınar")
        return r.finish(args.json)

    # ---------------------------------------------------------------- kalıplar
    hits = []
    for sid, s in sorted(stories.items()):
        blob = "\n\n".join(filter(None, [s.get("text", ""), s.get("culturalNote", "")]))
        for name, pattern, reason in mb.FORBIDDEN_PATTERNS:
            for m in re.finditer(pattern, blob, re.I | re.M):
                snippet = blob[max(0, m.start() - 30):m.end() + 30].replace("\n", " ")
                hits.append(f"{sid} · {name}: …{snippet}… ({reason})")
    r.add(not hits, f"yasak kalıp yok ({len(mb.FORBIDDEN_PATTERNS)} kalıp tarandı)",
          "bulundu:\n         " + "\n         ".join(hits[:12]))

    # ------------------------------------------------------------------- cümle
    all_avgs, long_sentences = [], []
    for sid, s in sorted(stories.items()):
        _, lengths = sentence_stats(s.get("text", ""))
        if not lengths:
            continue
        all_avgs.append(statistics.mean(lengths))
        for i, n in enumerate(lengths):
            if n > mb.BANDS["sentence_max"]:
                long_sentences.append(f"{sid} · cümle {i + 1}: {n} kelime")

    lo, hi = mb.BANDS["sentence_avg"]
    if all_avgs:
        book_avg = statistics.mean(all_avgs)
        r.add(lo <= book_avg <= hi,
              f"kitap geneli cümle ortalaması {book_avg:.1f} (bant {lo}–{hi})",
              f"cümle ortalaması {book_avg:.1f} — bant {lo}–{hi} dışında. "
              "Alt sınır da bilerek var: çok kısa cümle 12 yaşındaki okuru aşağılar")
        out = [f"{sid}: {statistics.mean(sentence_stats(s.get('text',''))[1] or [0]):.1f}"
               for sid, s in sorted(stories.items())
               if sentence_stats(s.get("text", ""))[1]
               and not (lo <= statistics.mean(sentence_stats(s.get("text", ""))[1]) <= hi)]
        r.warn(not out, "her hikâye cümle bandında", f"bant dışı: {out[:10]}")

    r.add(not long_sentences,
          f"en uzun cümle ≤{mb.BANDS['sentence_max']} kelime",
          "aşan:\n         " + "\n         ".join(long_sentences[:10]))

    # ---------------------------------------------------------------- paragraf
    long_paragraphs = []
    for sid, s in sorted(stories.items()):
        for i, p in enumerate(mb.paragraphs(s.get("text", ""))):
            n = len(mb.sentences(p))
            if n > mb.BANDS["paragraph_sentences"][1]:
                long_paragraphs.append(f"{sid} · paragraf {i + 1}: {n} cümle")
    r.add(not long_paragraphs,
          f"paragraflar ≤{mb.BANDS['paragraph_sentences'][1]} cümle",
          "aşan:\n         " + "\n         ".join(long_paragraphs[:10]))

    # ----------------------------------------------------------------- diyalog
    dlo, dhi = mb.BANDS["dialogue_share"]
    dialogue_problems = []
    for sid, s in sorted(stories.items()):
        text = s.get("text", "")
        total = mb.word_count(text)
        if not total:
            continue
        spoken = sum(mb.word_count(m.group(0)) for m in DIALOGUE.finditer(text))
        share = spoken / total
        if not (dlo <= share <= dhi):
            dialogue_problems.append(f"{sid}: %{share * 100:.0f} (bant %{dlo*100:.0f}–%{dhi*100:.0f})")
    r.warn(not dialogue_problems, "diyalog payı bantta",
           f"bant dışı: {dialogue_problems[:10]} — diyalog nefes verir ve karakteri gösterir")

    # --------------------------------------------------------------- tipografi
    typo_hits = []
    for sid, s in sorted(stories.items()):
        blob = "\n\n".join(filter(None, [s.get("text", ""), s.get("culturalNote", "")]))
        for name, pattern, reason in mb.TYPOGRAPHY_RULES:
            n = len(re.findall(pattern, blob))
            if n:
                typo_hits.append(f"{sid} · {name}: {n} örnek ({reason})")
        # tırnak dengesi 1:1
        if blob.count("“") != blob.count("”"):
            typo_hits.append(f"{sid} · tırnak dengesi: {blob.count('“')} açık, {blob.count('”')} kapalı")
        for ch, label in mb.INVISIBLE_CHARS.items():
            if ch in blob:
                typo_hits.append(f"{sid} · görünmez karakter: {label}")
    r.add(not typo_hits, "tipografi temiz",
          "sorunlar:\n         " + "\n         ".join(typo_hits[:12]))

    # --------------------------------------- KÜLTÜREL NOT ŞABLONLAŞMASI (J3)
    skeletons = collections.defaultdict(list)
    for sid, s in sorted(stories.items()):
        note = (s.get("culturalNote") or "").strip()
        if mb.word_count(note) >= 12:
            skeletons[note_skeleton(note)].append(sid)
    templated = {k: v for k, v in skeletons.items() if len(v) > 1}
    r.add(not templated,
          f"kültürel notlar kalıplaşmamış ({len(skeletons)} not tarandı)",
          "aynı cümle kalıbını paylaşan notlar:\n         "
          + "\n         ".join(f"{v}" for v in list(templated.values())[:8])
          + "\n         Kısıt/bağlam cümlesi kalıplaşırsa okur onu ATLAMAYI ÖĞRENİR "
            "(Bestiarium Faz 4 dersi).")

    # ------------------------------------------------- açılış/kapanış kalıpları
    for label, take in (("açılış", lambda t: (mb.sentences(t) or [""])[0]),
                        ("kapanış", lambda t: (mb.sentences(t) or [""])[-1])):
        firsts = collections.defaultdict(list)
        for sid, s in sorted(stories.items()):
            sent = take(s.get("text", ""))
            key = " ".join(w.lower() for w in mb.words(sent)[:5])
            if key:
                firsts[key].append(sid)
        dupes = {k: v for k, v in firsts.items() if len(v) > 1}
        r.add(not dupes, f"hikâye {label} cümleleri farklı kalıplarda",
              f"aynı {label} kalıbı: {list(dupes.items())[:6]}")

    return r.finish(args.json)


if __name__ == "__main__":
    sys.exit(main())
