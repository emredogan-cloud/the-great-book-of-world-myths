#!/usr/bin/env python3
"""
DİAKRİTİK VE ADLANDIRMA TUTARLILIĞI
================================================================================
22 kültür demek çok sayıda diakritik demektir: Kore romanizasyonu, Farsça,
Türkçe, Yoruba ton işaretleri, Hawaiʻice ʻokina ve kahakō, İnuktitut.
Ve bu kitapta TELAFFUZ REHBERİ BİR SATIŞ ARGÜMANIDIR — adlar hem doğru hem
tutarlı olmak zorunda.

⚠ BU KAPI BESTIARIUM'DA İKİ KEZ YANLIŞ POZİTİF ÜRETTİ. İkisi de baştan
düzeltilmiş hâliyle geldi (karar K12):

  D32 · Tarama re.I ile koşuyordu. `Lóng`un diakritiksiz hâli `Long`dur ve
        İngilizcenin en sık sözcüklerinden biriyle çakışır: "…long after it
        has gone" diakritik hatası olarak raporlandı. Kapı yazarı "long"
        sözcüğünü HİÇ KULLANMAMAYA zorlardı — doğru metni reddeden cetvel.
        → Tarama BÜYÜK/KÜÇÜK HARFE DUYARLI.

  D35 · İki ayrı maddenin adı `Lámia` (Hellenic) ve `Lamia` (Euskal) idi;
        Bask olanın adında aksan YOKTUR. Kapı doğru yazılmış "Lamia"yı
        "Lámia"nın düşürülmüş hâli sanıp reddediyordu.
        → Düz biçimi BAŞKA BİR ADIN GERÇEK YAZIMI olan dizeler bayraklanmaz.
"""

from __future__ import annotations

import argparse
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb


def collect_names(index: dict) -> tuple[dict, set]:
    """
    Dönüş: (diakritikli ad → kanonik yazım), (gerçek yazımların düz biçimleri)

    İkinci küme D35 muafiyetidir: bir dizenin düz biçimi başka bir adın
    GERÇEK yazımıysa, o dize bir 'düşürülmüş diakritik' değildir.
    """
    canonical: dict[str, str] = {}
    real_plain: set[str] = set()

    for s in index.get("stories", []):
        names = [p.get("name", "") for p in (s.get("pronunciationEntries") or [])]
        names += [c.get("name", "") for c in (s.get("characters") or [])]
        for c in (s.get("characters") or []):
            names += c.get("altNames") or []
        for name in names:
            for token in re.split(r"[\s’'()]+", name or ""):
                token = token.strip(".,;:")
                if len(token) < 3 or not token[:1].isupper():
                    continue
                plain = mb.strip_diacritics(token)
                if plain != token:
                    canonical[plain] = token
                else:
                    real_plain.add(token)
    return canonical, real_plain


# =============================================================================
# OKURA GİDEN DİZELERDE TİPOGRAFİ — Faz 3'te eklendi
# =============================================================================
# CHILDREN_WRITING_STYLE § 6 düz kesmeyi ve düz tırnağı YASAKLAR. `qa_voice`
# o kuralı uyguluyordu ama YALNIZCA manuscript'e: hikâye gövdesi ve kültürel
# not. Oysa okura giden dizelerin bir kısmı manuscript'te değil DİZİNDE durur
# — başlık (içindekiler + hikâye başlığı), telaffuz rehberi adları, "kim
# kimdir" rolleri, kültür adı ve bölgesi. O dizeler HİÇBİR kapının kapsamında
# değildi.
#
# Faz 3 taraması 33 kusur buldu, üç ayrı türde:
#   ① İngilizce iyelik:  “The Blacksmith's Apron”, “Osiris's son”
#   ② Ortografik kesme:  “Chang'e”, “K'iche'”, “Q'ukumatz”, “Man'yōshū”
#   ③ KENDİ İÇİNDE TUTARSIZ: “K’iche' is spoken by…” — aynı adın iki
#      karakteri, tek cümlede. Kalıcı kanıt: bu sınıf elle tutulamaz.
#
# Kitap tek kesme karakteri kullanır: ’ (U+2019). Ortografik kesme için
# dilbilimsel olarak U+02BC de savunulabilir (Maya dilleri, ALMG); karar ve
# gerekçe DECISIONS.md § K28'de, ve `mythbook._WORD` her ikisini de HARF
# sayar — yani kurucu isterse karar tek yerde değişir.

READER_STORY_FIELDS = ("title", "culturalNote", "variantNote", "region")
STRAIGHT_TYPOGRAPHY = re.compile("[\"']")


def reader_strings(index: dict, cultures: dict):
    """(yol, dize) — BASILI SAYFAYA giden her dize.

    Araştırma künyesi (`sources`, `pronunciationSource`, `restrictionNote`,
    `canonicalRationale`) ve Türkçe iç rehber (`endonymNote`) BİLEREK
    dışarıdadır: onlar okura değil ekibe gider ve kaynak künyesinin yazımı
    KAYNAĞIN kendi yazımıdır — düzeltilmesi alıntıyı bozar.
    """
    for s in index.get("stories", []):
        sid = s.get("id", "?")
        for f in READER_STORY_FIELDS:
            if s.get(f):
                yield f"{sid}.{f}", s[f]
        for i, e in enumerate(s.get("pronunciationEntries") or []):
            for f in ("name", "pronunciation"):
                if e.get(f):
                    yield f"{sid}.pronunciationEntries[{i}].{f}", e[f]
        for i, c in enumerate(s.get("characters") or []):
            for f in ("name", "role"):
                if c.get(f):
                    yield f"{sid}.characters[{i}].{f}", c[f]
            for j, a in enumerate(c.get("altNames") or []):
                if a:
                    yield f"{sid}.characters[{i}].altNames[{j}]", a
    for cu in cultures.get("cultures", []):
        for f in ("name", "region"):
            if cu.get(f):
                yield f"culture:{cu['id']}.{f}", cu[f]


def straight_typography_hits(index: dict, cultures: dict) -> list[tuple[str, str]]:
    """Okura giden dizelerde düz kesme / düz tırnak."""
    return [(path, value) for path, value in reader_strings(index, cultures)
            if STRAIGHT_TYPOGRAPHY.search(value)]


def main() -> int:
    ap = argparse.ArgumentParser(description="Diakritik ve adlandırma tutarlılığı")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  DİAKRİTİK VE ADLANDIRMA")
    print("═" * 72)

    r = mb.Result("qa_diacritics", verbose=args.verbose)
    index = mb.load_stories()
    cultures = mb.load_cultures()
    canonical, real_plain = collect_names(index)

    # --- ⓪ okura giden dizelerde düz kesme / düz tırnak ---
    straight = straight_typography_hits(index, cultures)
    r.add(not straight,
          "okura giden dizelerde düz kesme/tırnak yok "
          f"({sum(1 for _ in reader_strings(index, cultures))} dize tarandı)",
          "düz tipografi:\n         "
          + "\n         ".join(f"{p}: {v[:70]}" for p, v in straight[:12])
          + "\n         CHILDREN_WRITING_STYLE § 6: kitap tek kesme kullanır — ’ (U+2019). "
            "Başlık, telaffuz adı ve 'kim kimdir' rolü BASILI SAYFAYA gider ve "
            "qa_voice yalnızca manuscript'i tarar.")

    # --- ① dizinin kendi tutarlılığı: aynı ad iki farklı yazımda mı? ---
    spellings: dict[str, set] = collections.defaultdict(set)
    for s in index.get("stories", []):
        for p in (s.get("pronunciationEntries") or []):
            name = p.get("name", "")
            spellings[mb.strip_diacritics(name).lower()].add(name)
    inconsistent = {k: sorted(v) for k, v in spellings.items() if len(v) > 1}
    # D35: farklı yazımlar KASITLI olabilir (Lámia ≠ Lamia). Uyarı, hata değil.
    r.warn(not inconsistent,
           f"telaffuz rehberi adları tutarlı ({len(spellings)} ad)",
           f"aynı düz biçim, farklı yazım: {list(inconsistent.items())[:6]} — "
           "KASITLI olabilir (D35: Lámia/Hellenic ≠ Lamia/Euskal). "
           "Kasıtlıysa sözlükte çapraz gönderme ZORUNLU.")

    # --- ② metinde düşürülmüş diakritik ---
    book = mb.load_book()
    stories = mb.book_stories(book)

    if not stories:
        r.ok("metin yok — metin taraması boş koştu",
             f"{len(canonical)} diakritikli ad kayıtlı ve tarama hazır")
        return r.finish(args.json)

    if not canonical:
        r.ok("dizinde diakritikli ad yok — taranacak bir şey yok")
        return r.finish(args.json)

    dropped = []
    for sid, s in sorted(stories.items()):
        blob = "\n\n".join(filter(None, [s.get("text", ""), s.get("culturalNote", "")]))
        for plain, correct in canonical.items():
            # D35 MUAFİYETİ: düz biçim başka bir adın gerçek yazımıysa geç
            if plain in real_plain:
                continue
            # D32: BÜYÜK/KÜÇÜK HARFE DUYARLI, kelime sınırına saygılı
            for m in re.finditer(r"\b" + re.escape(plain) + r"\b", blob):
                snippet = blob[max(0, m.start() - 30):m.end() + 30].replace("\n", " ")
                dropped.append(f"{sid}: “{plain}” → “{correct}” · …{snippet}…")

    r.add(not dropped,
          f"metinde düşürülmüş diakritik yok ({len(canonical)} ad tarandı, "
          f"{len(real_plain)} ad D35 muafiyetinde)",
          "düşürülmüş:\n         " + "\n         ".join(dropped[:10]))

    # --- ③ dizinde olmayan bir adın metinde tutarsız kullanımı ---
    # (bir ad kitapta TEK biçimde yazılır — CHILDREN_WRITING_STYLE § 5)
    used: dict[str, set] = collections.defaultdict(set)
    for sid, s in sorted(stories.items()):
        for w in mb.words(s.get("text", "")):
            if mb.is_proper_name(w) and len(w) >= 4:
                used[mb.strip_diacritics(w).lower()].add(w)
    varied = {k: sorted(v) for k, v in used.items()
              if len(v) > 1 and not all(x in real_plain for x in v)}
    r.warn(not varied, "metinde her ad tek biçimde yazılmış",
           f"birden çok yazım: {list(varied.items())[:6]}")

    return r.finish(args.json)


if __name__ == "__main__":
    sys.exit(main())
