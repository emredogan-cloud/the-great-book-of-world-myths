#!/usr/bin/env python3
"""
ÜSLUP SÜRÜKLENMESİ ÖLÇÜMÜ
================================================================================
En sık 50 içerik sözcüğünün hikâye bazında binde yoğunluğu; doğrusal eğim.

Bestiarium'un ölçtüğü şey: Faz 3 kapanışında %+21, Faz 4 kapanışında %+8,9.
Yükselen sözcükler yazarın kendi analitik kaydını gösteriyordu (about ·
rather · nothing · tradition · creature) — yani KİTABIN KENDİNE GÖNDERMESİ.

Bu bir KAPI değil bir ÖLÇÜDÜR (D40): sürüklenme yazım fazında düzeltilmez,
ölçülür ve belgelenir. Düzeltme editoryal inceleme geçişine aittir —
ölçülmüş ve etiketlenmiş metin gerekçesiz açılmaz.

Rapor YARGILADIĞI SAYIYI gösterir (D37): eğim ile ham uçlar yan yana
basılır, çünkü bir ölçüm okuyanı ikna edemiyorsa kapı olarak da işe yaramaz.
"""

from __future__ import annotations

import argparse
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb

STOPWORDS = set("""
a an and are as at be been being but by for from had has have he her hers him his
i if in into is it its me my no nor not of off on or our ours out over she so some
such than that the their theirs them then there these they this those to too up us
was we were what when where which while who whom why will with would you your yours
he's she's it's don't didn't couldn't wouldn't shouldn't am do does did done
""".split())


def content_words(text: str) -> list[str]:
    proper = mb.proper_names(text)
    return [w.lower() for w in mb.words(text)
            if w.lower() not in STOPWORDS
            and len(w) > 2
            and w not in proper]


def linear_slope(ys: list[float]) -> float:
    """En küçük kareler eğimi."""
    n = len(ys)
    if n < 2:
        return 0.0
    xs = list(range(n))
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs)
    return num / den if den else 0.0


def main() -> int:
    ap = argparse.ArgumentParser(description="Üslup sürüklenmesi ölçümü")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  ÜSLUP SÜRÜKLENMESİ")
    print("═" * 72)

    r = mb.Result("qa_drift", verbose=args.verbose)
    book = mb.load_book()
    stories = mb.book_stories(book)

    if len(stories) < 5:
        r.ok(f"ölçüm için yeterli metin yok ({len(stories)} hikâye)",
             "sürüklenme en az 5 hikâyeyle ölçülür")
        return r.finish(args.json)

    # Kitaptaki sırayı koru — sürüklenme SIRAYA bağlı bir ölçüdür
    index = {s["id"]: s.get("number", 9999) for s in mb.load_stories().get("stories", [])}
    order = sorted(stories, key=lambda sid: (index.get(sid, 9999), sid))

    per_story = {sid: content_words(stories[sid].get("text", "")) for sid in order}
    totals = collections.Counter()
    for ws in per_story.values():
        totals.update(ws)
    top50 = [w for w, _ in totals.most_common(50)]

    # her hikâyede top-50 yoğunluğu (binde)
    densities = []
    for sid in order:
        ws = per_story[sid]
        if not ws:
            continue
        hits = sum(1 for w in ws if w in top50)
        densities.append(hits / len(ws) * 1000)

    if len(densities) < 5:
        r.ok("ölçüm için yeterli veri yok")
        return r.finish(args.json)

    slope = linear_slope(densities)
    start_fit = densities[0]
    n = len(densities)
    mean = sum(densities) / n
    fitted_start = mean - slope * (n - 1) / 2
    fitted_end = mean + slope * (n - 1) / 2
    pct = (fitted_end - fitted_start) / fitted_start * 100 if fitted_start else 0.0

    warn, fail = mb.BANDS["drift_warn_pct"], mb.BANDS["drift_fail_pct"]

    print(f"\n  hikâye sayısı           : {n}")
    print(f"  uydurulan doğru başlangıç: {fitted_start:.1f}‰")
    print(f"  uydurulan doğru bitiş    : {fitted_end:.1f}‰")
    print(f"  EĞİM                     : %{pct:+.1f}   ← YARGILANAN SAYI")
    print(f"  ham uçlar (bilgi)        : {densities[0]:.1f}‰ → {densities[-1]:.1f}‰")
    print(f"  eşikler                  : uyarı %{warn:.0f} · başarısızlık %{fail:.0f}")

    # yükselen sözcükler — ilk yarı ↔ ikinci yarı
    half = n // 2
    first = collections.Counter()
    second = collections.Counter()
    for i, sid in enumerate(order[:len(densities)]):
        (first if i < half else second).update(per_story[sid])
    n1 = sum(first.values()) or 1
    n2 = sum(second.values()) or 1
    rising = sorted(
        ((w, second[w] / n2 * 1000 - first[w] / n1 * 1000) for w in top50),
        key=lambda x: -x[1])[:10]
    print("\n  yükselen sözcükler: " + ", ".join(f"{w} ({d:+.1f}‰)" for w, d in rising))

    r.add(abs(pct) <= fail, f"sürüklenme başarısızlık eşiğinin altında (%{pct:+.1f})",
          f"sürüklenme %{pct:+.1f} — eşik %{fail:.0f}. "
          "Yükselen sözcükler yazarın kendi kaydını gösteriyorsa kaynağı "
          "KİTABIN KENDİNE GÖNDERMESİDİR.")
    r.warn(abs(pct) <= warn, f"sürüklenme uyarı eşiğinin altında (%{pct:+.1f})",
           f"sürüklenme %{pct:+.1f} — uyarı eşiği %{warn:.0f}. "
           "D40: yazım fazında DÜZELTİLMEZ, ÖLÇÜLÜR ve commit iletisine geçer.")

    return r.finish(args.json)


if __name__ == "__main__":
    sys.exit(main())
