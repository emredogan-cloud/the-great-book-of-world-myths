#!/usr/bin/env python3
"""
ÜRETİLEN BELGELER — BOOK_STATS.md + ROADMAP_PROGRESS.md
================================================================================
    python3 04_BUILD/update_docs.py            üret
    python3 04_BUILD/update_docs.py --check    bayat mı (CI)

"Her faz sonunda güncelle, asla unutma" bir DİSİPLİN TALEBİDİR ve disiplin
unutulur. Mekanizma unutmaz.

--------------------------------------------------------------------------------
BESTIARIUM D38 — manuscript ölçüsü depoya alınır
--------------------------------------------------------------------------------
BOOK_STATS.md, manuscript'ten türeyen sayılar taşır; manuscript ise depoda
YOKTUR (.gitignore § ①). Aynı komut yerelde ve CI'da İKİ FARKLI BELGE
üretirdi ve her yazım commit'i "bayat belge" diye kırmızı yanardı.

Çözüm: 01_RESEARCH/manuscript_metrics.json — yalnızca SAYI içerir, tek bir
hikâye cümlesi bile değil. Depo varlığı değil, ÖLÇÜSÜNÜ taşır.
"""

from __future__ import annotations

import argparse
import collections
import difflib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb
import editions as ed_mod
import page_budget as pb

STAMP = "<!-- OTOMATİK ÜRETİLDİ — 04_BUILD/update_docs.py · ELLE DÜZENLEMEYİN -->"


# ⚠ ÜRETİLEN BELGELER GIT ÜST VERİSİ TAŞIMAZ.
#
# İlk sürüm koşusu bunu yakaladı: belgeler `git describe --tags` ve son
# commit tarihini basıyordu. Etiket atıldığı anda CI belgeleri YENİDEN
# üretiyor, farklı bir etiket adı çıkıyor ve "bayat belge" kapısı kırmızı
# yanıyordu — hâlbuki içerik değişmemişti.
#
# Bir üretilen belge YALNIZCA çalışma ağacının bir işlevi olmalıdır.
# Etiket ve tarih zaten git geçmişinde ve GitHub'da duruyor; onları
# belgenin İÇİNE koymak, belgeyi kendi üretim anına bağımlı kılar.


# =============================================================================
# MANUSCRIPT ÖLÇÜSÜ
# =============================================================================

def compute_metrics() -> dict:
    book = mb.load_book()
    stories = mb.book_stories(book)

    if not stories:
        return {"$comment": ("Manuscript ÖLÇÜSÜ. Yalnızca sayı içerir — tek bir "
                             "hikâye cümlesi bile değil (Bestiarium D38). "
                             "04_BUILD/update_docs.py üretir."),
                "written": 0, "words": 0, "avgWords": 0,
                "minWords": 0, "maxWords": 0, "outOfBand": 0,
                "culturalNotes": 0, "sentenceAvg": 0.0}

    counts, sent_avgs = [], []
    lo, hi = mb.BANDS["story_words"]
    out_of_band = 0
    notes = 0
    for s in stories.values():
        n = mb.word_count(s.get("text", ""))
        counts.append(n)
        if not (lo <= n <= hi):
            out_of_band += 1
        if (s.get("culturalNote") or "").strip():
            notes += 1
        lens = [mb.word_count(x) for x in mb.sentences(s.get("text", ""))]
        if lens:
            sent_avgs.append(sum(lens) / len(lens))

    return {
        "$comment": ("Manuscript ÖLÇÜSÜ. Yalnızca sayı içerir — tek bir hikâye "
                     "cümlesi bile değil (Bestiarium D38)."),
        "written": len(counts),
        "words": sum(counts),
        "avgWords": round(sum(counts) / len(counts)) if counts else 0,
        "minWords": min(counts) if counts else 0,
        "maxWords": max(counts) if counts else 0,
        "outOfBand": out_of_band,
        "culturalNotes": notes,
        "sentenceAvg": round(sum(sent_avgs) / len(sent_avgs), 1) if sent_avgs else 0.0,
    }


def load_metrics() -> dict:
    if os.path.exists(mb.METRICS):
        with open(mb.METRICS, encoding="utf-8") as fh:
            return json.load(fh)
    return compute_metrics()


# =============================================================================
# BOOK_STATS.md
# =============================================================================

def render_book_stats() -> str:
    cfg = mb._CFG
    cultures = mb.load_cultures()
    index = mb.load_stories()
    metrics = load_metrics()
    gate = mb.read_gate()

    cul = cultures.get("cultures", [])
    locked_c = [c for c in cul if c.get("status") == "locked"]
    cand_c = [c for c in cul if c.get("status") == "candidate"]

    st = [s for s in index.get("stories", []) if s.get("status") != "dropped"]
    locked_s = [s for s in st if s.get("status") not in ("candidate", "researching")]

    screened = [c for c in locked_c if c.get("restrictionAssessment") not in (None, "pending")]

    # sayfa modeli
    paperback = ed_mod.get("paperback")
    wpp = ed_mod.words_per_page(paperback, mb.PAGE_TARGET)
    model = pb.compute(wpp)
    cost = ed_mod.print_cost("paperback", model["billed"])
    roy = ed_mod.print_royalty(paperback.price_usd, cost)

    per_macro = collections.Counter(c["macroRegion"] for c in locked_c)
    macro_names = {m["id"]: m["nameTr"] for m in cultures.get("macroRegions", [])}

    L = []
    a = L.append
    a("# BOOK STATS — The Great Book of World Myths")
    a("")
    a(STAMP)
    a("")
    a(f"> Kapı: `{gate}` · ölçüm anı için git geçmişine bakın")
    a("")
    a("Buradaki her sayı **ölçülmüştür**. Hiçbiri elle yazılmadı.")
    a("")
    a("## 1. Tek bakışta")
    a("")
    a("| | Ölçülen | Hedef |")
    a("|---|---:|---:|")
    a(f"| Kilitli kültür | **{len(locked_c)}** | {mb.CULTURE_TARGET} |")
    a(f"| Aday kültür | {len(cand_c)} | ≥{mb.CULTURE_CANDIDATE_MIN - mb.CULTURE_TARGET} yedek |")
    a(f"| Kilitli hikâye | **{len(locked_s)}** | {mb.STORY_TARGET} |")
    a(f"| Aday hikâye | {len(st)} | ≥{mb.STORY_CANDIDATE_MIN} |")
    a(f"| Yazılmış hikâye | **{metrics['written']}** | {mb.STORY_TARGET} |")
    a(f"| Hikâye metni | {metrics['words']:,} kelime | {mb.MANUSCRIPT_WORD_TARGET:,} |")
    a(f"| Hikâye ortalaması | {metrics['avgWords']} | {mb.WORD_TARGET} |")
    a(f"| Bant dışı hikâye | {metrics['outOfBand']} | 0 |")
    a(f"| Kültürel not | {metrics['culturalNotes']} | {mb.STORY_TARGET} |")
    a(f"| Cümle ortalaması | {metrics['sentenceAvg']} | "
      f"{mb.BANDS['sentence_avg'][0]}–{mb.BANDS['sentence_avg'][1]} |")
    a(f"| Kısıtlılık taraması | {len(screened)}/{len(locked_c)} | "
      f"{len(locked_c)}/{len(locked_c)} (muafiyetsiz) |")
    a(f"| Görsel | 0 | {cfg['illustration']['total']} |")
    a("")
    a("## 2. Sayfa ve fiyat modeli")
    a("")
    a(f"> ⚠ Model **{'KALİBRE' if paperback.typography.calibrated else 'KALİBRE DEĞİL'}**"
      f" — kelime/sayfa tipografi tahmininden geliyor. Faz 1 gerçek dizgiyle ölçer (K3).")
    a("")
    a("| | |")
    a("|---|---:|")
    a(f"| Kelime/sayfa (tahmin) | {model['wordsPerPage']} |")
    a(f"| Hikâye başına faturalanan | {model['billedPagesPerStory']} sayfa |")
    a(f"| Ön madde · bölüm · kültür kartı | {model['front']} · {model['partOpeners']} · {model['cultureCards']} |")
    a(f"| Gövde | {model['body']} |")
    a(f"| Arka madde | {model['back']} |")
    a(f"| **Modelin sayfa sayısı** | **{model['billed']}** |")
    a(f"| Yol haritası hedefi | {mb.PAGE_TARGET} |")
    a(f"| Sapma | %{abs(model['billed'] - mb.PAGE_TARGET) / mb.PAGE_TARGET * 100:.1f} |")
    a(f"| Ciltsiz baskı maliyeti | {cost:.2f} $ |")
    a(f"| Ciltsiz telif | {roy:.2f} $ |")
    a("")
    a("## 3. Sürümler")
    a("")
    a("| Sürüm | Durum | Fiyat | Telif | Not |")
    a("|---|---|---:|---:|---|")
    for ed in ed_mod.EDITIONS.values():
        status = "lansman" if (ed.enabled and ed.launch) else ("etkin" if ed.enabled else "devre dışı")
        if ed.binding == "kindle":
            rr = ed_mod.ebook_royalty(ed.price_usd, ed.file_budget_mb or 0)
        elif ed.enabled:
            rr = ed_mod.print_royalty(ed.price_usd, ed_mod.print_cost(ed.binding, model["billed"]))
        else:
            rr = 0.0
        a(f"| {ed.label} | {status} | {ed.price_usd:.2f} $ | "
          f"{rr:.2f} $ | {ed.notes.split('.')[0][:60]} |")
    a("")
    a("## 4. Kültürel dağılım")
    a("")
    if locked_c:
        a("| Makro bölge | Kilitli kültür |")
        a("|---|---:|")
        for mid, n in sorted(per_macro.items(), key=lambda x: -x[1]):
            a(f"| {macro_names.get(mid, mid)} | {n} |")
    else:
        a("*Henüz kilitli kültür yok — envanter Faz 1'in birinci işidir "
          "(`DECISIONS.md` § A2).*")
    a("")
    a("---")
    a("")
    a("*Bu dosya `04_BUILD/update_docs.py` tarafından üretilir.*")
    return "\n".join(L) + "\n"


# =============================================================================
# ROADMAP_PROGRESS.md
# =============================================================================

def bar(done: int, total: int, width: int = 16) -> str:
    if total <= 0:
        return "░" * width
    filled = int(round(done / total * width))
    return "█" * filled + "░" * (width - filled)


def render_progress() -> str:
    cfg = mb._CFG
    metrics = load_metrics()
    gate = mb.read_gate()
    index = mb.load_stories()
    cultures = mb.load_cultures()

    written = metrics["written"]
    locked_c = len([c for c in cultures.get("cultures", []) if c.get("status") == "locked"])
    locked_s = len([s for s in index.get("stories", [])
                    if s.get("status") not in ("candidate", "researching", "dropped")])

    L = []
    a = L.append
    a("# ROADMAP PROGRESS — The Great Book of World Myths")
    a("")
    a(STAMP)
    a("")
    a(f"> Kapı: `{gate}` · etiketler için GitHub Releases'e bakın")
    a("")
    a("Kaynak: [`THE_GREAT_BOOK_OF_WORLD_MYTHS_MASTER_ROADMAP.md`]"
      "(THE_GREAT_BOOK_OF_WORLD_MYTHS_MASTER_ROADMAP.md)")
    a("")
    a("## Faz durumu")
    a("")
    a("| Faz | Başlık | Yazım ilerlemesi | Kilometre taşı | Etiket |")
    a("|---:|---|---|---|---|")
    for p in cfg["phases"]:
        target = p["storiesCumulative"]
        done = min(written, target)
        pct = int(done / target * 100) if target else 100
        prog = f"`{bar(done, target)}` {done}/{target} (%{pct})" if target else "`" + "░" * 16 + "` —"
        a(f"| **{p['number']}** | {p['title']} | {prog} | "
          f"{p['storiesWritten']} hikâye · {p['images']} görsel | `{p['tag']}` |")
    a("")
    a("## Kapı durumu")
    a("")
    a(f"Aktif kapı: **`{gate}`** · sıra {mb.gate_rank(gate) + 1}/{len(mb.GATE_LEVELS)}")
    a("")
    a("| Kapı | Komut | Ne zaman açılır |")
    a("|---|---|---|")
    for name, cmd, when in (
        ("Yapılandırma ve veri", "`validate_spec.py`", "her push"),
        ("Depo ve belge", "`validate_structure.py`", "her push"),
        ("Manuscript sızıntısı", "`validate_structure.py`", "her push"),
        ("Kapıların kendi testi", "`05_TESTS/selftest.py`", "her push"),
        ("Araştırma", "`validate_research.py`", "Faz 1'den itibaren"),
        ("Kelime bandı", "`qa_length.py`", "metin geldiğinde"),
        ("**Yaş politikası**", "`qa_age.py`", "metin geldiğinde"),
        ("**Okunabilirlik**", "`qa_readability.py`", "metin geldiğinde"),
        ("Ses ve yasak kalıp", "`qa_voice.py`", "metin geldiğinde"),
        ("Tekrar", "`qa_echo.py`", "metin geldiğinde"),
        ("Diakritik", "`qa_diacritics.py`", "her zaman"),
        ("Çapraz referans", "`qa_crossref.py`", "her zaman"),
        ("Sürüklenme", "`qa_drift.py`", "her 5 hikâyede"),
        ("Sayfa bütçesi", "`page_budget.py`", "her zaman · Faz 4'ten itibaren HATA"),
        ("Görsel", "`images.py --measure`", "görsel geldiğinde"),
    ):
        a(f"| {name} | {cmd} | {when} |")
    a("")
    a("## Envanter")
    a("")
    a("| | Ölçülen | Hedef |")
    a("|---|---:|---:|")
    a(f"| Kilitli kültür | {locked_c} | {mb.CULTURE_TARGET} |")
    a(f"| Kilitli hikâye | {locked_s} | {mb.STORY_TARGET} |")
    a(f"| Yazılmış hikâye | {written} | {mb.STORY_TARGET} |")
    a("")
    a("## Sonraki eylem")
    a("")
    if gate == "phase0":
        a("**Faz 1 kurucu onayını bekliyor.**")
        a("")
        a("Bootstrap tamamlandı: altyapı, kapılar, CI ve yol haritası hazır. "
          "Yazım **başlamadı**.")
        a("")
        a("Onay istenen belge: [`PHASE_1_APPROVAL_REQUEST.md`](PHASE_1_APPROVAL_REQUEST.md)")
        a("")
        a("Faz 1 başlamadan kapanması gereken açık kararlar: "
          "**A1** (manuscript nerede duracak) · **A2** (22 kültür) · **A3** (45 hikâye).")
    else:
        a(f"**Faz {mb.gate_rank(gate)} yürürlükte.** {written}/{mb.STORY_TARGET} hikâye yazıldı.")
        a("")
        a("Tek seferde en fazla üç hikâye — daha fazlası üslup sürüklenmesi üretir.")
    a("")
    a("---")
    a("")
    a("*Bu dosya `04_BUILD/update_docs.py` tarafından üretilir.*")
    return "\n".join(L) + "\n"


# =============================================================================
# KARAR ↔ CHANGELOG BAĞI
# =============================================================================

def check_decision_links(r: mb.Result) -> None:
    """Her K## kararı CHANGELOG'da anılmalı. Bestiarium'un
    update_docs.check_decision_links mekanizması."""
    decisions = set(re.findall(r"\*\*(K\d+)\*\*",
                               open(os.path.join(mb.ROOT, "DECISIONS.md"), encoding="utf-8").read()))
    changelog_path = os.path.join(mb.ROOT, "CHANGELOG.md")
    changelog = open(changelog_path, encoding="utf-8").read() if os.path.exists(changelog_path) else ""
    orphan = sorted(d for d in decisions if d not in changelog)
    r.add(not orphan, f"her karar CHANGELOG'da anılıyor ({len(decisions)} karar)",
          f"CHANGELOG'da geçmeyen: {orphan} — karar kaydı ile değişiklik kaydı ayrışmış")


# =============================================================================
# GİRİŞ NOKTASI
# =============================================================================

TARGETS = [
    ("BOOK_STATS.md", render_book_stats),
    ("ROADMAP_PROGRESS.md", render_progress),
]


def main() -> int:
    ap = argparse.ArgumentParser(description="Üretilen belgeler")
    ap.add_argument("--check", action="store_true", help="bayat mı (yazmaz)")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  ÜRETİLEN BELGELER" + (" · BAYATLIK DENETİMİ" if args.check else ""))
    print("═" * 72)

    r = mb.Result("update_docs", verbose=args.verbose)

    # manuscript ölçüsü
    metrics = compute_metrics()
    metrics_path = mb.METRICS
    old_metrics = {}
    if os.path.exists(metrics_path):
        with open(metrics_path, encoding="utf-8") as fh:
            old_metrics = json.load(fh)

    if args.check:
        # Manuscript yerelde YOKSA ölçüyü kırmızı yakma: CI'da her zaman
        # 0 çıkar ve depodaki gerçek ölçüyle ayrışırdı (Bestiarium D38).
        if mb.load_book() is not None:
            r.add(old_metrics == metrics, "manuscript ölçüsü güncel",
                  "manuscript_metrics.json bayat — `update_docs.py` çalıştırın")
        else:
            r.ok("manuscript ölçüsü denetlenmedi", "yerelde manuscript yok (D38)")
    else:
        with open(metrics_path, "w", encoding="utf-8") as fh:
            json.dump(metrics, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print(f"  ✎ {os.path.relpath(metrics_path, mb.ROOT)}")

    for name, render in TARGETS:
        path = os.path.join(mb.ROOT, name)
        new = render()
        old = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
        if args.check:
            fresh = old == new
            if not fresh and args.verbose:
                diff = difflib.unified_diff(old.splitlines(), new.splitlines(),
                                            fromfile=f"{name} (depoda)",
                                            tofile=f"{name} (üretilen)", lineterm="", n=1)
                print("\n".join(list(diff)[:40]))
            r.add(fresh, f"{name} güncel",
                  f"{name} BAYAT — `python3 04_BUILD/update_docs.py` çalıştırın")
        else:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new)
            print(f"  ✎ {name}")
            r.ok(f"{name} üretildi")

    check_decision_links(r)

    return r.finish(args.json)


if __name__ == "__main__":
    sys.exit(main())
