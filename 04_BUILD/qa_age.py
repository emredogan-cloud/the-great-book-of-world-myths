#!/usr/bin/env python3
"""
YAŞ POLİTİKASI KAPISI — bu projenin EN ÖNEMLİ metin kapısı
================================================================================
Master yayıncılık yol haritası, PROJE 02'nin tanımlayıcı riskini ve
azaltmasını adıyla yazmıştır:

    "Yaş uygunluğu (orta). Mitler acımasızdır. Yanlış tonlanmış bir sahne,
     ebeveyn yorumunda 'çocuğum için fazla karanlık' olarak geri döner —
     ve BU YORUM SİLİNEMEZ. Azaltma: yazım öncesi AGE_POLICY.md; yayından
     önce en az iki ebeveyn okuması."

Bu betik o politikanın makine tarafıdır. AGE_POLICY.md § 4'ün eşiklerini
uygular.

⚠ İKİ YÖNLÜ KAPIDIR. Aşırı sahneleme kadar AŞIRI SAKLAMA da kusurdur:
ölüm örtmecesi (qa_voice) ve zorla mutlu son bu kitapta kültürel
sterilizasyondur (AGE_POLICY § 0).

Kapının kendisi 05_TESTS/selftest.py ile sınanır. 45 hikâyeyi otomatik
reddetme yetkisi olan bir kapı, doğru çalıştığı kanıtlanmadan kullanılamaz.
"""

from __future__ import annotations

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb


def word_hits(text: str, terms: list[str]) -> list[str]:
    """Kelime sınırına saygılı arama. Alt dize araması 'Devi'yi 'Devil'
    içinde bulur — Bestiarium D42'nin düzelttiği kusur."""
    found = []
    low = text.lower()
    for t in terms:
        pattern = r"\b" + re.escape(t.lower()).replace(r"\ ", r"\s+") + r"\b"
        for m in re.finditer(pattern, low):
            snippet = text[max(0, m.start() - 35):m.end() + 35].replace("\n", " ")
            found.append(f"“{t}” → …{snippet}…")
    return found


def intense_runs(text: str) -> list[tuple[int, int]]:
    """AGE_POLICY § 2.1: ardışık yoğun eylem cümlesi ≤3."""
    sents = mb.sentences(text)
    flags = []
    for s in sents:
        low = s.lower()
        hit = any(re.search(r"\b" + re.escape(v) + r"\b", low) for v in mb.INTENSE_VERBS)
        flags.append(hit)

    runs, start = [], None
    for i, f in enumerate(flags):
        if f and start is None:
            start = i
        elif not f and start is not None:
            runs.append((start, i - start))
            start = None
    if start is not None:
        runs.append((start, len(flags) - start))
    return runs


def main() -> int:
    ap = argparse.ArgumentParser(description="Yaş politikası kapısı (AGE_POLICY.md)")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  YAŞ POLİTİKASI · 8–12 YAŞ")
    print("═" * 72)

    r = mb.Result("qa_age", verbose=args.verbose)
    book = mb.load_book()
    stories = mb.book_stories(book)
    cultures = mb.culture_by_id(mb.load_cultures())
    index = {s["id"]: s for s in mb.load_stories().get("stories", [])}

    if not stories:
        r.ok("metin yok — kapı boş koştu",
             "AGE_POLICY yazım ÖNCESİ hazırdır; kapının körlüğünü selftest sınar")
        return r.finish(args.json)

    graphic, sexual, abuse = [], [], []
    intense_long, intense_many = [], []
    exclamation, unresolved = [], []
    living_past, living_myth, restricted, generalisation = [], [], [], []

    for sid, s in sorted(stories.items()):
        text = s.get("text", "")
        note = s.get("culturalNote", "") or ""
        blob = text + "\n\n" + note

        # --- § 2.1 / 2.8 / 2.9 · ÇIKARILAN sözcükler ---
        for hit in word_hits(blob, mb.GRAPHIC_TERMS):
            graphic.append(f"{sid} · {hit}")
        for hit in word_hits(blob, mb.SEXUAL_TERMS):
            sexual.append(f"{sid} · {hit}")
        for hit in word_hits(blob, mb.ABUSE_TERMS):
            abuse.append(f"{sid} · {hit}")

        # --- § 2.1 · yoğun sahne uzunluğu ve sayısı ---
        runs = intense_runs(text)
        cap = mb.BANDS["intense_scene_sentences"]
        for start, length in runs:
            if length > cap:
                intense_long.append(f"{sid}: {length} ardışık yoğun cümle "
                                    f"(cümle {start + 1}'den itibaren · tavan {cap})")
        scenes = [x for x in runs if x[1] >= 2]
        if len(scenes) > mb.BANDS["intense_scenes_per_story"]:
            intense_many.append(f"{sid}: {len(scenes)} yoğun sahne "
                                f"(tavan {mb.BANDS['intense_scenes_per_story']})")

        # --- § 4 · ünlem ---
        n_excl = text.count("!")
        if n_excl > mb.BANDS["exclamations_per_story"]:
            exclamation.append(f"{sid}: {n_excl} ünlem "
                               f"(tavan {mb.BANDS['exclamations_per_story']})")

        # --- § 2.14 · SON SAYFA KURALI ---
        paras = mb.paragraphs(text)
        if paras:
            last = paras[-1]
            for hit in word_hits(last, mb.UNRESOLVED_FEAR_TERMS):
                unresolved.append(f"{sid} · son paragraf: {hit}")

        # --- § 2.15 · geçmiş zaman tuzağı ve "myth" kelimesi ---
        entry = index.get(sid, {})
        culture = cultures.get(entry.get("cultureId", ""), {})
        if culture.get("livingTradition"):
            for pattern in mb.LIVING_PAST_TENSE:
                for m in re.finditer(pattern, blob, re.I):
                    living_past.append(
                        f"{sid} ({culture.get('name')}) · …{blob[max(0,m.start()-30):m.end()+30]}…")
            for m in re.finditer(mb.LIVING_MYTH_WORD, blob, re.I):
                living_myth.append(
                    f"{sid} ({culture.get('name')}) · …{blob[max(0,m.start()-30):m.end()+30]}…")

        # --- § 2.16 · kısıtlı bilgi işaretçileri ---
        for hit in word_hits(blob, mb.RESTRICTED_MARKERS):
            restricted.append(f"{sid} · {hit}")

        # --- STYLE § 7 · genelleme ---
        for pattern in mb.GENERALISATION_PATTERNS:
            for m in re.finditer(pattern, blob, re.I):
                generalisation.append(f"{sid} · …{blob[max(0,m.start()-25):m.end()+25]}…")

    # ---------------------------------------------------------------- sonuçlar
    r.add(not graphic, f"grafik şiddet sözcüğü yok ({len(mb.GRAPHIC_TERMS)} terim tarandı)",
          "AGE_POLICY § 2.1 ÇIKARILAN:\n         " + "\n         ".join(graphic[:10]))
    r.add(not sexual, f"cinsel içerik sözcüğü yok ({len(mb.SEXUAL_TERMS)} terim)",
          "AGE_POLICY § 2.8 ÇIKARILAN (mutlak):\n         " + "\n         ".join(sexual[:10]))
    r.add(not abuse, "istismar sahnesi işaretçisi yok",
          "AGE_POLICY § 2.9 ÇIKARILAN:\n         " + "\n         ".join(abuse[:10]))

    r.add(not intense_long,
          f"yoğun sahneler ≤{mb.BANDS['intense_scene_sentences']} cümle",
          "AGE_POLICY § 2.1 — 'sonuç anlatılır, dehşet betimlenmez':\n         "
          + "\n         ".join(intense_long[:10]))
    r.warn(not intense_many,
           f"hikâye başına yoğun sahne ≤{mb.BANDS['intense_scenes_per_story']}",
           "art arda gerilim yorar:\n         " + "\n         ".join(intense_many[:10]))

    r.warn(not exclamation, f"ünlem ≤{mb.BANDS['exclamations_per_story']} / hikâye",
           "aşan: " + "; ".join(exclamation[:10]))

    r.add(not unresolved, "hiçbir hikâye çözümsüz korkuyla bitmiyor",
          "AGE_POLICY § 2.14 SON SAYFA KURALI — hikâye korkuyla açılabilir, "
          "korkuyla ilerleyebilir, ama KORKUYLA BİTMEZ:\n         "
          + "\n         ".join(unresolved[:10]))

    r.add(not living_past, "yaşayan gelenekler şimdiki zamanda anlatılıyor",
          "AGE_POLICY § 2.15 GEÇMİŞ ZAMAN TUZAĞI — 'inanırdı' bir kültürü müzeye "
          "koyar:\n         " + "\n         ".join(living_past[:10]))
    r.add(not living_myth, "yaşayan gelenekler için 'myth' kelimesi kullanılmıyor",
          "AGE_POLICY § 2.15 — kitabın BAŞLIĞI 'myths' der; metin içinde yaşayan "
          "bir gelenek için 'story/telling/tradition' kullanılır:\n         "
          + "\n         ".join(living_myth[:10]))

    r.add(not restricted, "kısıtlı bilgi işaretçisi yok",
          "AGE_POLICY § 2.16 — kısıtlı anlatı ANLATILMAZ, kısıtlı olduğu "
          "SÖYLENİR:\n         " + "\n         ".join(restricted[:10]))

    r.add(not generalisation, "kültürel genelleme yok",
          "STYLE § 7 — 'Afrikalılar…' değil, 'Yoruba anlatıcıları…':\n         "
          + "\n         ".join(generalisation[:10]))

    # ------------------------------------- inceleme kaydı (REVIEW kategorileri)
    review_needed, review_logged = [], []
    log_path = os.path.join(mb.EDITORIAL, "AGE_REVIEW_LOG.md")
    log = ""
    if os.path.exists(log_path):
        with open(log_path, encoding="utf-8") as fh:
            log = fh.read()

    for sid in stories:
        entry = index.get(sid, {})
        flags = set(entry.get("contentFlags") or [])
        if flags & {"sacrifice", "religious", "culturally-sensitive"}:
            review_needed.append(sid)
            if sid in log:
                review_logged.append(sid)

    missing_log = sorted(set(review_needed) - set(review_logged))
    r.add(not missing_log, f"ÖZEL İNCELEME gerektiren hikâyeler kayıtlı ({len(review_needed)})",
          f"03_EDITORIAL/AGE_REVIEW_LOG.md'de kaydı olmayan: {missing_log[:10]}")

    return r.finish(args.json)


if __name__ == "__main__":
    sys.exit(main())
