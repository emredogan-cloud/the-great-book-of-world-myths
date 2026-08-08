#!/usr/bin/env python3
"""
ARKA MADDE DİZİNLERİNİ ÜRET
================================================================================
Üç dizin, üçü de yol haritasının ZORUNLU KILDIĞI ek malzeme:

    "Ek malzeme: Telaffuz rehberi · 'kim kimdir' sözlüğü · her hikâye
     sonunda 2 satırlık kültürel not"
    Gerekçe: "Öğretmen ve kütüphaneci için satın alma gerekçesi;
              İADE ORANINI DÜŞÜRÜR."

Çıktı: 06_REPORTS/tracked/BACK_MATTER_PREVIEW.md — dizgiden ÖNCE
okunabilir hâli. Nihai dizgi Faz 5'in işidir.

⚠ ÇIKTI OKURA GİDER → İNGİLİZCEDİR.
Bestiarium D44: proje belgelerinin dili (Türkçe) pazarlama artefaktına
sızmıştı ve grafik ilk üretimde Türkçe basmıştı. Bu dosyanın başlıkları
İngilizcedir çünkü kitabın arka maddesidir.
"""

from __future__ import annotations

import argparse
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb

OUT = os.path.join(mb.REPORTS_TRACKED, "BACK_MATTER_PREVIEW.md")

STAMP = "<!-- OTOMATİK ÜRETİLDİ — 04_BUILD/make_index.py · ELLE DÜZENLEMEYİN -->"


def sort_key(name: str) -> str:
    return mb.strip_diacritics(name).lower()


def render() -> str:
    index = mb.load_stories()
    cultures = mb.load_cultures()
    entries = [s for s in index.get("stories", []) if s.get("status") != "dropped"]
    cmap = mb.culture_by_id(cultures)
    macro = {m["id"]: m["name"] for m in cultures.get("macroRegions", [])}

    L = []
    a = L.append
    a("# Back Matter — preview")
    a("")
    a(STAMP)
    a("")
    a("> Bu dosya **okura giden** üç dizinin dizgiden önceki hâlidir ve bu")
    a("> yüzden **İngilizcedir** (Bestiarium D44). Nihai dizgi Faz 5'in işidir.")
    a("")

    # ------------------------------------------------ 1. Pronunciation Guide
    a("## How to Say the Names")
    a("")
    pron = {}
    for s in entries:
        for p in (s.get("pronunciationEntries") or []):
            pron.setdefault(p["name"], p)
    if pron:
        a("| Name | Say it | Culture |")
        a("|---|---|---|")
        for name in sorted(pron, key=sort_key):
            p = pron[name]
            owners = [cmap.get(s["cultureId"], {}).get("name", "")
                      for s in entries
                      if any(x["name"] == name for x in (s.get("pronunciationEntries") or []))]
            a(f"| **{name}** | {p['pronunciation']} | {', '.join(sorted(set(owners)))} |")
        a("")
        a(f"*{len(pron)} entries.*")
    else:
        a("*Empty — the story inventory is Phase 1's first task "
          "(`DECISIONS.md` § A3).*")
    a("")

    # ---------------------------------------------------- 2. Who's Who
    a("## Who's Who")
    a("")
    glossary = {}
    for s in entries:
        for c in (s.get("characters") or []):
            if not c.get("glossary", True):
                continue
            rec = glossary.setdefault(c["name"], {"role": c.get("role", ""),
                                                  "alt": set(), "stories": []})
            rec["alt"] |= set(c.get("altNames") or [])
            rec["stories"].append(s.get("title", s["id"]))
    if glossary:
        a("| Name | Also called | Who they are | Appears in |")
        a("|---|---|---|---|")
        for name in sorted(glossary, key=sort_key):
            g = glossary[name]
            a(f"| **{name}** | {', '.join(sorted(g['alt'])) or '—'} | "
              f"{g['role']} | {', '.join(g['stories'][:3])} |")
        a("")
        a(f"*{len(glossary)} entries.*")
    else:
        a("*Empty — Phase 1.*")
    a("")

    # ------------------------------------------------- 3. Cultures and Map
    a("## The Twenty-Two Cultures")
    a("")
    locked = [c for c in cultures.get("cultures", []) if c.get("status") == "locked"]
    by_macro = collections.defaultdict(list)
    for c in locked:
        by_macro[c["macroRegion"]].append(c)
    if locked:
        for mid in sorted(by_macro, key=lambda m: macro.get(m, m)):
            a(f"### {macro.get(mid, mid)}")
            a("")
            for c in sorted(by_macro[mid], key=lambda x: x["name"]):
                n = len([s for s in entries if s.get("cultureId") == c["id"]])
                point = c.get("mapPoint") or {}
                loc = f" · map: {point.get('label')}" if point else ""
                a(f"- **{c['name']}** — {c.get('region', '')} · {n} stor"
                  f"{'y' if n == 1 else 'ies'}{loc}")
            a("")
        a(f"*{len(locked)} of {mb.CULTURE_TARGET} cultures locked.*")
    else:
        a(f"*0 of {mb.CULTURE_TARGET} cultures locked — Phase 1 "
          f"(`DECISIONS.md` § A2). Six are already fixed by the master roadmap.*")
    a("")

    # -------------------------------------------- 4. A note on what is not here
    excluded = cultures.get("excluded") or []
    if excluded:
        a("## A Note on What Is Not in This Book")
        a("")
        a("> Bu bölüm okura **kasıtlı dışarıda bırakmayı** anlatır. Bir kusur")
        a("> değil, bir karardır (SOURCING_STANDARD § 7).")
        a("")
        for ex in excluded:
            a(f"- **{ex['name']}** — {ex['disposition']}")
        a("")

    a("---")
    a("")
    a("*Generated by `04_BUILD/make_index.py`.*")
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Arka madde dizinlerini üret")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  ARKA MADDE DİZİNLERİ" + (" · BAYATLIK" if args.check else ""))
    print("═" * 72)

    r = mb.Result("make_index", verbose=args.verbose)
    os.makedirs(mb.REPORTS_TRACKED, exist_ok=True)

    new = render()
    old = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""

    if args.check:
        r.add(old == new, "arka madde önizlemesi güncel",
              "BAYAT — `python3 04_BUILD/make_index.py` çalıştırın")
    else:
        with open(OUT, "w", encoding="utf-8") as fh:
            fh.write(new)
        print(f"  ✎ {os.path.relpath(OUT, mb.ROOT)}")
        r.ok("arka madde önizlemesi üretildi")

    return r.finish(args.json)


if __name__ == "__main__":
    sys.exit(main())
