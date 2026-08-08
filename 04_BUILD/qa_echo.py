#!/usr/bin/env python3
"""
TEKRAR TARAMASI
================================================================================
Hikâyeler arası 8+ kelimelik birebir tekrar ve benzer cümle iskeletleri.

Bestiarium'un Faz 4'te EN ÇOK ÇALIŞAN kapısıydı: 19 kusur yakaladı, hepsi
gerçekti, ve üç ayrı kalıplaşma türü ortaya çıkardı.

BU PROJEDE İKİ FARK:

① KÜLTÜREL NOT MUAF TUTULMAZ (karar K13). Bestiarium kaynak notunu muaf
   tutuyordu ve gerekçesi doğruydu — bir başvuru cildinde künye biçimi
   TUTARLI olmak zorundadır. Ama kültürel not künye değildir: okura giden
   bir metindir ve kalıplaşırsa okur onu atlamayı öğrenir.

② MUAFİYETLER KAPSAMA İLİŞKİSİYLE ÇALIŞIR, birebir eşitlikle değil.
   Bestiarium'un ALLOWED_ECHOES'u ÜÇÜNCÜ ÖLÜ KURALDI: 8 kelimelik gram'ın
   4 kelimelik bir öğeye BİREBİR EŞİT olması aranıyordu — muafiyet hiç
   devreye girmemişti. selftest her muafiyetin en az bir kez devreye
   girdiğini ayrıca sınar.
"""

from __future__ import annotations

import argparse
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb

# Muaf öbekler — KAPSAMA ilişkisiyle çalışır. Her biri bir gerekçeyle burada.
# Yeni bir muafiyet eklemek selftest'te bir kanıt gerektirir.
# ⚠ MUAFİYETLER İKİ YÖNLÜ KAPSAMA ile çalışır: bir n-gram ya muaf öbeği
# İÇERİR ya da muaf öbeğin İÇİNDE geçer. Tek yönlü kapsama, muaf öbek
# n-gram'dan uzun olduğunda hiç devreye girmez — Bestiarium'un Ö1 ölü
# kuralının tam mekanizması. selftest her muafiyetin canlı olduğunu
# ayrıca kanıtlar.
ALLOWED_ECHOES = [
    # Aynı kaynağın künyesi 45 hikâyede TUTARLI olmak zorundadır; künyeyi
    # hikâyeden hikâyeye değiştirmek kusurun ta kendisidir (Bestiarium D34).
    "as it is told in the collection made by",
    "the oldest written record of this story comes from",
    "this telling follows the version written down by",
]


def is_exempt(phrase: str) -> bool:
    """İki yönlü kapsama."""
    low = phrase.lower()
    return any(a in low or low in a for a in (x.lower() for x in ALLOWED_ECHOES))


def ngrams(words: list[str], n: int):
    for i in range(len(words) - n + 1):
        yield i, tuple(w.lower() for w in words[i:i + n])


def skeleton(sentence: str) -> str:
    """Cümle iskeleti: içerik sözcükleri atılır, yapı sözcükleri kalır."""
    ws = [w.lower() for w in mb.words(sentence)]
    return " ".join(w if len(w) <= 3 else "·" for w in ws)


def main() -> int:
    ap = argparse.ArgumentParser(description="Tekrar taraması")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  TEKRAR TARAMASI")
    print("═" * 72)

    r = mb.Result("qa_echo", verbose=args.verbose)
    book = mb.load_book()
    stories = mb.book_stories(book)

    if not stories:
        r.ok("metin yok — kapı boş koştu", "körlüğü 05_TESTS/selftest.py sınar")
        return r.finish(args.json)

    n = mb.BANDS["echo_ngram"]

    # ------------------------------------------------- hikâyeler arası birebir
    seen: dict[tuple, list[str]] = collections.defaultdict(list)
    for sid, s in sorted(stories.items()):
        blob = "\n\n".join(filter(None, [s.get("text", ""), s.get("culturalNote", "")]))
        ws = mb.words(blob)
        for _, gram in ngrams(ws, n):
            phrase = " ".join(gram)
            if is_exempt(phrase):
                continue
            if sid not in seen[gram]:
                seen[gram].append(sid)

    cross = {g: ids for g, ids in seen.items() if len(ids) > 1}
    r.add(not cross,
          f"hikâyeler arası {n}+ kelimelik birebir tekrar yok "
          f"({len(stories)} hikâye tarandı)",
          "tekrar:\n         " + "\n         ".join(
              f"“{' '.join(g)}” → {ids}" for g, ids in list(cross.items())[:10]))

    # ---------------------------------------------------- hikâye İÇİ tekrar
    internal = []
    for sid, s in sorted(stories.items()):
        ws = mb.words(s.get("text", ""))
        counter = collections.Counter(g for _, g in ngrams(ws, n))
        for gram, count in counter.items():
            phrase = " ".join(gram)
            if count > 1 and not is_exempt(phrase):
                internal.append(f"{sid}: “{phrase}” ×{count}")
    r.warn(not internal,
           "hikâye içi birebir tekrar yok",
           "tekrar (sözlü gelenekte KASITLI tekrar meşrudur — gözden geçirin):\n         "
           + "\n         ".join(internal[:10]))

    # ------------------------------------------------ paragraf düzeyinde kopya
    paras: dict[str, list[str]] = collections.defaultdict(list)
    for sid, s in sorted(stories.items()):
        for p in mb.paragraphs(s.get("text", "")):
            key = re.sub(r"\W+", " ", p.lower()).strip()
            if len(key.split()) >= 12:
                paras[key].append(sid)
    dupe_paras = {k: v for k, v in paras.items() if len(v) > 1}
    r.add(not dupe_paras, "yinelenen paragraf yok",
          f"yinelenen: {[v for v in list(dupe_paras.values())[:5]]}")

    # --------------------------------------------------------- cümle iskeleti
    skeletons: dict[str, list[str]] = collections.defaultdict(list)
    for sid, s in sorted(stories.items()):
        for sent in mb.sentences(s.get("text", "")):
            if mb.word_count(sent) >= 10:
                skeletons[skeleton(sent)].append(sid)
    shared = {k: v for k, v in skeletons.items() if len(set(v)) > 2}
    r.warn(not shared,
           "cümle iskeletleri çeşitli",
           f"üç veya daha fazla hikâyede aynı iskelet: "
           f"{[(k[:40], sorted(set(v))) for k, v in list(shared.items())[:5]]}")

    return r.finish(args.json)


if __name__ == "__main__":
    sys.exit(main())
