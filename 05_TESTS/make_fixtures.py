#!/usr/bin/env python3
"""
KUSURLU KURGU KİTAP ÜRETECİ
================================================================================
Her kapı için TAM BİR KUSUR taşıyan kurgu bir kitap üretir. selftest.py bu
kurguları gerçek kapılardan geçirir ve kapının kusuru YAKALADIĞINI kanıtlar.

⚠ ÜRETEÇ KENDİ KENDİNİ TEKRARLAMAMALI.
Bestiarium'un ilk make_fixtures'ı sabit adımlı bir sayaçla kelime seçiyordu
(31 kelimelik sözlük, 7 adım, gcd=1); üreteç aynı diziyi tekrarlıyor ve iki
bölüm aynı 8-gram'ı taşıyordu. qa_echo bunu DOĞRU yakaladı — düzeltilen
betik değil KURGU oldu.

Burada çakışma, hikâye başına ayrı bir sözcük havuzu ve indeks kaydırmasıyla
önlenir; `--verify` bunu ayrıca sınar.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "04_BUILD"))
import mythbook as mb

FIXTURE_DIR = os.path.join(mb.TESTS, "fixtures")

# =============================================================================
# METİN ÜRETECİ
# =============================================================================
# Temiz kurgunun BÜTÜN kapılardan geçmesi gerekir — yoksa "kapı kusuru
# yakaladı" kanıtı işe yaramaz: yanlış pozitif ile gerçek kusur ayırt
# edilemez. Üretecin tutturmak ZORUNDA olduğu bantlar:
#
#   cümle ortalaması 11–14 · Flesch–Kincaid 4,0–6,5 · hece/kelime 1,35–1,55
#   zor sözcük ≤%6 · paragraf ≤6 cümle · diyalog %5–30 · 8-gram tekrar 0
#
# `--verify` hepsini sınar ve tutmuyorsa KIRMIZI yanar.
#
# ÇAKIŞMA NASIL ÖNLENİYOR (Bestiarium B4)
# ---------------------------------------
# Sabit adımlı bir sayaç (pool[k*a % N]) N kelimede bir aynı pencereyi
# üretir — Bestiarium'un ilk üreteci tam bu yüzden kendini tekrarladı.
# Burada indeks KAREseldir: i = (k² · b + k · a) mod N. Sayaç kitabın
# TAMAMINDA süreklidir, yani iki farklı k asla aynı 8-pencereyi vermez.

FUNC = "the a and of in on to by for with at from into over under".split()

CONTENT_1 = ("stone boat sand rope door path wind rain hill fire salt bird gate "
             "wave moon leaf root ship horn drum bowl cloak snow frost seed reed "
             "thorn crow hawk fox pike bear elk shell claw tide fen bog moss oak "
             "yew smoke bread milk hand foot bone dust ridge hearth night day").split()

CONTENT_2 = ("river willow lantern harbour cedar meadow ember basket kettle ladder "
             "thistle beacon paddle birch quarry valley pebble anvil rudder alder "
             "hollow candle bramble tinder sparrow otter heron badger shadow "
             "morning evening water mountain forest island winter summer thunder "
             "harvest anchor blanket window garden feather ribbon marble").split()

CONTENT_3 = "lanterns gathering wandering afterwards travellers remembering".split()

# Karışım okuma seviyesini belirler. %50 işlev sözcüğü (1 hece) + içerik
# havuzu → hece/kelime ≈ 1,4 · zor sözcük ≈ %5 · Flesch–Kincaid ≈ 5,3
CONTENT = CONTENT_1 * 3 + CONTENT_2 * 13 + CONTENT_3 * 6

VERBS = ("walked ran held took gave found lost kept knew saw came went stood sat "
         "carried waited counted opened lifted followed watched turned").split()

NAMES = ["Aro", "Beki", "Cira", "Doran", "Elin"]   # ≤7 — hikâye başına ad tavanı

SAID = ["said", "asked", "answered", "called", "whispered"]


class Stream:
    """
    Kitabın tamamında SÜREKLİ, deterministik sözcük akışı.

    ⚠ SABİT ADIMLI SAYAÇ KULLANILMAZ. pool[k·a mod N] biçimi N kelimede bir
    aynı pencereyi üretir; Bestiarium'un ilk üreteci tam bu yüzden kendini
    tekrarladı (B4) ve qa_echo onu DOĞRU yakaladı. Karesel indeks de küçük
    havuzlarda (özellikle 14 elemanlı işlev sözcüğü havuzunda) periyodiktir.

    Burada doğrusal eşleşik üreteç (LCG) kullanılır: deterministiktir —
    aynı tohum her koşuda aynı metni verir — ama 8 kelimelik pencere tekrarı
    pratikte imkânsızdır.
    """

    def __init__(self, seed: int = 0):
        self.state = (seed * 2654435761 + 12345) % 2**31

    def _next(self) -> int:
        self.state = (1103515245 * self.state + 12345) % 2**31
        return self.state

    def word(self, pool: list[str]) -> str:
        return pool[self._next() % len(pool)]

    def sentence(self, length: int) -> str:
        parts = []
        for j in range(length):
            parts.append(self.word(FUNC) if j % 2 == 0 else self.word(CONTENT))
        # Fiil, cümlenin ortasına — okur için bir omurga
        parts[length // 2] = self.word(VERBS)
        parts[0] = parts[0].capitalize()
        return " ".join(parts) + "."

    def dialogue(self, length: int) -> str:
        inner = self.sentence(max(4, length - 4)).rstrip(".")
        name = NAMES[self._next() % len(NAMES)]
        said = SAID[self._next() % len(SAID)]
        return f"“{inner},” {said} {name}."


def clean_story(idx: int, words: int = 950) -> str:
    """Bütün kapılardan GEÇMESİ gereken kurgu hikâye."""
    st = Stream(seed=idx + 1)
    paragraphs, count, i = [], 0, 0
    while count < words:
        sents, n = [], 3 + (i % 3)              # 3–5 cümlelik paragraf
        for _ in range(n):
            length = 11 + (i % 4)               # 11–14 kelime
            s = st.dialogue(length) if i % 7 == 3 else st.sentence(length)
            i += 1
            sents.append(s)
            count += mb.word_count(s)
            if count >= words:
                break
        paragraphs.append(" ".join(sents))
    return "\n\n".join(paragraphs)


# Kültürel not — 25–45 kelime, HER BİRİ FARKLI İSKELETTE.
# (qa_voice şablonlaşmayı arar: 45 not, 45 farklı cümle kalıbı. Bestiarium'un
# Faz 4 dersi: kalıplaşan bir bağlam cümlesini okur ATLAMAYI ÖĞRENİR.)
NOTE_SHAPES = [
    "Storytellers in {a} still tell this one, though the ending changes as you "
    "move north past the {b} and the older {c} that stands beyond it.",

    "This telling follows the {a} version. A {b} retelling gives the {c} a "
    "different name and a gentler end than the one you have just read here.",

    "Nobody wrote it down until late. The {a} who finally did had heard it "
    "from a {b} beside the {c}, many winters before anyone thought to ask.",

    "Where the {a} meets the {b}, the same story is told about a {c} instead. "
    "That is one reason so many of the older names have survived at all.",

    "The {a} version keeps a detail this one leaves out. Their {b} is counted "
    "twice: once for the living, and once again for the {c} left behind.",

    "Two families of tellers claim it. One sets the whole thing beside the "
    "{a}, the other beside the {b}, and neither will give up the {c}.",
]


def clean_note(idx: int) -> str:
    st = Stream(seed=1000 + idx)
    return NOTE_SHAPES[idx % len(NOTE_SHAPES)].format(
        a=st.word(CONTENT_2), b=st.word(CONTENT_2), c=st.word(CONTENT_1))


def base_book(n: int = 6) -> dict:
    return {
        "meta": {"fixture": True,
                 "$comment": "KURGU — 05_TESTS/make_fixtures.py üretir. Kitap metni DEĞİLDİR."},
        "stories": {
            f"fx-{i:03d}": {
                "title": f"Fixture {i}",
                "text": clean_story(i),
                "culturalNote": clean_note(i),
            } for i in range(n)
        },
    }


# =============================================================================
# KUSURLAR — her biri TAM BİR KAPI için
# =============================================================================
# Anahtar = kusurun kimliği. Değer = (kapı betiği, kitabı bozan işlev, açıklama)

def _too_short(book: dict) -> dict:
    book["stories"]["fx-000"]["text"] = clean_story(0, words=300)
    return book


def _forbidden_pattern(book: dict) -> dict:
    book["stories"]["fx-001"]["text"] += (
        "\n\nAnd so they learned that patience is its own reward. "
        "As we saw in this book, the tradition supplies what memory cannot.")
    return book


def _graphic_violence(book: dict) -> dict:
    book["stories"]["fx-002"]["text"] += (
        "\n\nHe was disembowelled on the stones and the entrails steamed in the cold. "
        "The blood-soaked ground would not drink it all.")
    return book


def _sexual_content(book: dict) -> dict:
    book["stories"]["fx-003"]["text"] += (
        "\n\nThe god took her against her will; the rape is told plainly in the older poem.")
    return book


def _unresolved_ending(book: dict) -> dict:
    book["stories"]["fx-004"]["text"] += (
        "\n\nNobody found the door again. It is still out there, and it waits for you.")
    return book


def _intense_run(book: dict) -> dict:
    book["stories"]["fx-005"]["text"] += (
        "\n\nHe struck and the bone broke. She stabbed and the shield split. "
        "They crushed the gate and burned the hall. He drowned the last of them "
        "and the blood ran to the sea.")
    return book


def _too_hard(book: dict) -> dict:
    book["stories"]["fx-000"]["text"] = (
        "The extraordinarily complicated genealogical considerations underlying "
        "this particular cosmological interpretation necessitate a preliminary "
        "examination of the fundamentally incompatible chronological frameworks "
        "which characterise the surviving documentary evidence, notwithstanding "
        "considerable methodological disagreements among contemporary "
        "commentators regarding the appropriate interpretative apparatus. " * 20)
    return book


def _cross_echo(book: dict) -> dict:
    shared = " The lantern was carried down to the water before the tide turned again."
    book["stories"]["fx-001"]["text"] += shared
    book["stories"]["fx-002"]["text"] += shared
    return book


def _templated_notes(book: dict) -> dict:
    for i in (0, 1, 2):
        book["stories"][f"fx-{i:03d}"]["culturalNote"] = (
            f"This story comes from the people of place {i} and they still tell it "
            f"today in the winter when the nights are long and cold.")
    return book


def _typography(book: dict) -> dict:
    book["stories"]["fx-003"]["text"] += (
        '\n\nShe said "wait" and the boy\'s hand fell... he did not wait -- he ran.')
    return book


def _long_sentence(book: dict) -> dict:
    book["stories"]["fx-004"]["text"] += (
        "\n\n" + " ".join(["river"] * 30) + " and the boat went on and on and on "
        "past every landing that anyone had ever named or counted or remembered.")
    return book


def _placeholder(book: dict) -> dict:
    book["stories"]["fx-005"]["text"] += "\n\nTODO: finish this scene."
    return book


def _duplicate_paragraph(book: dict) -> dict:
    para = mb.paragraphs(book["stories"]["fx-000"]["text"])[0]
    book["stories"]["fx-001"]["text"] += "\n\n" + para
    return book


def _missing_note(book: dict) -> dict:
    book["stories"]["fx-002"]["culturalNote"] = ""
    return book


def _generalisation(book: dict) -> dict:
    book["stories"]["fx-003"]["culturalNote"] = (
        "Africans believed that the river had a spirit, and primitive tribes "
        "still keep the custom in their villages far away.")
    return book


DEFECTS = {
    "too_short":          ("qa_length",      _too_short,          "hikâye bandın altında"),
    "missing_note":       ("qa_length",      _missing_note,       "kültürel not eksik"),
    "forbidden_pattern":  ("qa_voice",       _forbidden_pattern,  "ders veren kapanış + kitabın kendine göndermesi"),
    "typography":         ("qa_voice",       _typography,         "düz tırnak, düz kesme, üç nokta, çift tire"),
    "long_sentence":      ("qa_voice",       _long_sentence,      "cümle 25 kelimeyi aşıyor"),
    "placeholder":        ("qa_voice",       _placeholder,        "TODO metne sızmış"),
    "templated_notes":    ("qa_voice",       _templated_notes,    "kültürel notlar kalıplaşmış"),
    "graphic_violence":   ("qa_age",         _graphic_violence,   "grafik şiddet — AGE_POLICY § 2.1"),
    "sexual_content":     ("qa_age",         _sexual_content,     "cinsel içerik — AGE_POLICY § 2.8"),
    "unresolved_ending":  ("qa_age",         _unresolved_ending,  "çözümsüz korkuyla bitiş — § 2.14"),
    "intense_run":        ("qa_age",         _intense_run,        "yoğun sahne 3 cümleyi aşıyor — § 2.1"),
    "generalisation":     ("qa_age",         _generalisation,     "kültürel genelleme — STYLE § 7"),
    "too_hard":           ("qa_readability", _too_hard,           "okuma seviyesi 8–12 yaşın çok üstünde"),
    "cross_echo":         ("qa_echo",        _cross_echo,         "hikâyeler arası birebir tekrar"),
    "duplicate_paragraph":("qa_echo",        _duplicate_paragraph,"yinelenen paragraf"),
}


def build(defect: str | None = None) -> dict:
    book = base_book()
    if defect:
        book = DEFECTS[defect][1](book)
        book["meta"]["defect"] = defect
    return book


def write(defect: str | None) -> str:
    os.makedirs(FIXTURE_DIR, exist_ok=True)
    name = f"book-{defect or 'clean'}.json"
    path = os.path.join(FIXTURE_DIR, name)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(build(defect), fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    return path


def verify_generator() -> list[str]:
    """Üretecin kendi kendini tekrarlamadığını sına (Bestiarium B4)."""
    import collections
    book = base_book()
    n = mb.BANDS["echo_ngram"]
    seen = collections.defaultdict(set)
    for sid, s in book["stories"].items():
        ws = mb.words(s["text"])
        for i in range(len(ws) - n + 1):
            seen[tuple(w.lower() for w in ws[i:i + n])].add(sid)
    return [" ".join(g) for g, ids in seen.items() if len(ids) > 1]


def main() -> int:
    ap = argparse.ArgumentParser(description="Kusurlu kurgu kitap üreteci")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--defect", default=None)
    ap.add_argument("--verify", action="store_true", help="üreteç kendini tekrarlıyor mu")
    args = ap.parse_args()

    if args.verify:
        collisions = verify_generator()
        if collisions:
            print(f"⛔ ÜRETEÇ KENDİNİ TEKRARLIYOR — {len(collisions)} çakışan öbek")
            for c in collisions[:5]:
                print(f"   “{c}”")
            print("   Düzeltilecek olan betik değil KURGUDUR (Bestiarium B4).")
            return 1
        print("✅ üreteç çakışmasız — temiz kurgu qa_echo'dan geçer")
        return 0

    if args.all:
        paths = [write(None)] + [write(d) for d in DEFECTS]
        print(f"✎ {len(paths)} kurgu üretildi → {os.path.relpath(FIXTURE_DIR, mb.ROOT)}")
    else:
        print(f"✎ {write(args.defect)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
