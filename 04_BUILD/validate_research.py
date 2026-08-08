#!/usr/bin/env python3
"""
ARAŞTIRMA KAYDI KAPISI
================================================================================
01_RESEARCH/research/<story-id>.md dosyalarının varlığını ve story_index.json
ile senkron olduğunu denetler.

validate_spec.py kaynak KURALLARINI denetler (≥2 bağımsız, ≥1 güçlü, kısıtlılık
taraması). Bu betik ARAŞTIRMA DOSYALARININ kendisine bakar: üretildiler mi,
bayat mı, elle düzenlenmiş mi.

Kaynak kuralları için: SOURCING_STANDARD.md
"""

from __future__ import annotations

import argparse
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb
import research_gen

RESEARCH_DIR = os.path.join(mb.RESEARCH, "research")


def main() -> int:
    ap = argparse.ArgumentParser(description="Araştırma kaydı kapısı")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  ARAŞTIRMA KAYITLARI")
    print("═" * 72)

    r = mb.Result("validate_research", verbose=args.verbose)
    gate = mb.read_gate()
    index = mb.load_stories()
    entries = [s for s in index.get("stories", []) if s.get("status") != "dropped"]

    if not entries:
        r.ok("hikâye dizini boş — araştırma kaydı beklenmiyor",
             f"kapı {gate}; envanter Faz 1'in birinci işi")
        return r.finish(args.json)

    on_disk = {f[:-3] for f in os.listdir(RESEARCH_DIR) if f.endswith(".md")} \
        if os.path.isdir(RESEARCH_DIR) else set()
    expected = {s["id"] for s in entries}

    missing = sorted(expected - on_disk)
    orphan = sorted(on_disk - expected)

    r.add(not missing, f"her hikâyenin araştırma kaydı var ({len(expected)})",
          f"eksik kayıt: {missing[:10]} — `research_gen.py` çalıştırın")
    r.add(not orphan, "artık araştırma kaydı yok",
          f"dizinde olmayan hikâyenin kaydı: {orphan[:10]} — düşürüldüyse "
          "09_ARCHIVE/dropped-research/ altına taşıyın (yapılan iş kayıt altında kalır)")

    # --- bayatlık: dosya, dizinden yeniden üretildiğinde aynı çıkıyor mu ---
    stale = []
    for s in entries:
        path = os.path.join(RESEARCH_DIR, f"{s['id']}.md")
        if not os.path.exists(path):
            continue
        want = research_gen.render(s, index, mb.load_cultures())
        with open(path, encoding="utf-8") as fh:
            got = fh.read()
        if got != want:
            stale.append(s["id"])
    r.add(not stale, "araştırma kayıtları güncel",
          f"BAYAT: {stale[:10]} — kayıtlar ÜRETİLİR, elle düzenlenmez "
          "(elle yazılan şey story_index.json'dır)")

    # --- kaynak istatistiği ---
    total_sources = sum(len(s.get("sources") or []) for s in entries)
    by_type = collections.Counter(
        src.get("type") for s in entries for src in (s.get("sources") or []))
    print(f"\n  {len(entries)} hikâye · {total_sources} kaynak künyesi · "
          f"hikâye başına {total_sources / len(entries):.1f}")
    for t, n in by_type.most_common():
        print(f"    {t:>10}: {n}")

    return r.finish(args.json)


if __name__ == "__main__":
    sys.exit(main())
