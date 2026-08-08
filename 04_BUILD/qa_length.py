#!/usr/bin/env python3
"""
KELİME BANDI KAPISI
================================================================================
Hikâye gövdesi 800–1100 (hedef 950) · kültürel not 25–45 kelime.

Metin yoksa 0 döner (karar K9). Körlük riskini 05_TESTS/selftest.py kapatır:
kasıtlı bant dışı bir kurgu çalıştırılır ve kapının yakaladığı kanıtlanır.
"""

from __future__ import annotations

import argparse
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb


def main() -> int:
    ap = argparse.ArgumentParser(description="Kelime bandı kapısı")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  KELİME BANDI")
    print("═" * 72)

    r = mb.Result("qa_length", verbose=args.verbose)
    book = mb.load_book()
    stories = mb.book_stories(book)

    if not stories:
        r.ok("metin yok — kapı boş koştu",
             "manuscript depo dışında yaşar (.gitignore § ①); "
             "kapının körlüğünü 05_TESTS/selftest.py sınar")
        return r.finish(args.json)

    lo, hi = mb.BANDS["story_words"]
    target = mb.BANDS["story_words_target"]
    nlo, nhi = mb.BANDS["cultural_note_words"]

    counts, out_of_band, note_problems, missing_note = [], [], [], []

    for sid, s in sorted(stories.items()):
        n = mb.word_count(s.get("text", ""))
        counts.append(n)
        if not (lo <= n <= hi):
            out_of_band.append(f"{sid}: {n} (bant {lo}–{hi})")

        note = (s.get("culturalNote") or "").strip()
        if not note:
            missing_note.append(sid)
        else:
            nn = mb.word_count(note)
            if not (nlo <= nn <= nhi):
                note_problems.append(f"{sid}: kültürel not {nn} (bant {nlo}–{nhi})")

    r.add(not out_of_band, f"bütün hikâyeler bantta ({len(counts)} hikâye)",
          "bant dışı:\n         " + "\n         ".join(out_of_band[:12]))
    r.add(not missing_note, "her hikâyenin kültürel notu var",
          f"eksik: {missing_note[:10]}")
    r.add(not note_problems, "kültürel notlar bantta",
          "bant dışı:\n         " + "\n         ".join(note_problems[:12]))

    if counts:
        avg = statistics.mean(counts)
        dev = abs(avg - target) / target * 100
        r.warn(dev <= 5,
               f"ortalama {avg:.0f} kelime (hedef {target} · sapma %{dev:.1f})",
               f"ortalama {avg:.0f}, hedef {target} — sapma %{dev:.1f} > %5")
        print(f"\n  toplam {sum(counts):,} kelime · "
              f"en kısa {min(counts)} · en uzun {max(counts)} · ortalama {avg:.0f}")

        # Manuscript hedefine göre projeksiyon — sayfa modeli buna dayanıyor
        if len(counts) < mb.STORY_TARGET:
            projected = avg * mb.STORY_TARGET
            print(f"  {mb.STORY_TARGET} hikâyeye izdüşüm: {projected:,.0f} kelime "
                  f"(hedef {mb.MANUSCRIPT_WORD_TARGET:,})")

    return r.finish(args.json)


if __name__ == "__main__":
    sys.exit(main())
