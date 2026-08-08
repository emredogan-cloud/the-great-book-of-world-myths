"""
THE GREAT BOOK OF WORLD MYTHS — KİTAP KAYIT DEFTERİ
================================================================================
Bu dosya bütün kalite kapılarının TEK doğruluk kaynağıdır. Hiçbir betikte
"sihirli sayı" yoktur; hepsi buradan okunur.

    from mythbook import BANDS, GATE_LEVELS, GRAPHIC_TERMS

Bir eşiği değiştirmek = burayı değiştirmek + AGE_POLICY/STYLE'ı güncellemek
+ selftest kurgusunu güncellemek. Üçü birlikte yapılmazsa belge ile kapı
ayrışır; ayrışan kapı ÖLÜ KURALDIR ve ölü kural yanlış kuraldan tehlikelidir
(bkz. LESSONS_FROM_CODEX_BESTIARIUM § D).

Bağımlılık: yok. Standart kütüphane (karar K7).
"""

from __future__ import annotations

import json
import os
import re
import unicodedata

# =============================================================================
# 0. YOLLAR
# =============================================================================

BUILD = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BUILD)

CONTEXT     = os.path.join(ROOT, "00_CONTEXT")
RESEARCH    = os.path.join(ROOT, "01_RESEARCH")
MANUSCRIPT  = os.path.join(ROOT, "02_MANUSCRIPT")
EDITORIAL   = os.path.join(ROOT, "03_EDITORIAL")
TESTS       = os.path.join(ROOT, "05_TESTS")
REPORTS     = os.path.join(ROOT, "06_REPORTS")
REPORTS_TRACKED = os.path.join(REPORTS, "tracked")
ASSETS      = os.path.join(ROOT, "07_ASSETS")
OUTPUT      = os.path.join(ROOT, "08_OUTPUT")
ARCHIVE     = os.path.join(ROOT, "09_ARCHIVE")

CULTURE_INDEX = os.path.join(RESEARCH, "culture_index.json")
STORY_INDEX   = os.path.join(RESEARCH, "story_index.json")
METRICS       = os.path.join(RESEARCH, "manuscript_metrics.json")
CONFIG        = os.path.join(ROOT, "project_config.json")
GATE_FILE     = os.path.join(ROOT, ".gate")

# Manuscript depo DIŞINDA yaşar (.gitignore § ①). Varsa okunur, yoksa metin
# kapıları boş koşar ve 0 döner (karar K9) — körlük riskini selftest kapatır.
BOOK_JSON = os.path.join(MANUSCRIPT, "book.json")
BOOK_EDITED_JSON = os.path.join(MANUSCRIPT, "book-edited.json")


# =============================================================================
# 1. KAPI SEVİYELERİ
# =============================================================================
# Kümülatif: bir kapı açıldıktan sonra kapanamaz (karar K8).

GATE_LEVELS = ["phase0", "phase1", "phase2", "phase3", "phase4", "phase5", "release"]


def gate_rank(level: str) -> int:
    try:
        return GATE_LEVELS.index(level)
    except ValueError:
        raise ValueError(f"bilinmeyen kapı seviyesi: {level!r} — GATE_LEVELS: {GATE_LEVELS}")


def read_gate() -> str:
    """.gate dosyasını oku. Yoksa phase0."""
    if not os.path.exists(GATE_FILE):
        return "phase0"
    with open(GATE_FILE, encoding="utf-8") as fh:
        level = fh.read().strip()
    gate_rank(level)          # geçersizse burada patlar
    return level


def gate_at_least(level: str, minimum: str) -> bool:
    return gate_rank(level) >= gate_rank(minimum)


# =============================================================================
# 2. PROJE YAPILANDIRMASI
# =============================================================================

def load_config() -> dict:
    with open(CONFIG, encoding="utf-8") as fh:
        return json.load(fh)


_CFG = load_config()

STORY_TARGET   = _CFG["scope"]["stories"]              # 45
CULTURE_TARGET = _CFG["scope"]["cultures"]             # 22
WORD_TARGET    = _CFG["scope"]["storyWordTarget"]      # 950
PAGE_TARGET    = _CFG["scope"]["pageTarget"]           # 230
MANUSCRIPT_WORD_TARGET = _CFG["scope"]["manuscriptWordTarget"]

# SOURCING_STANDARD § 9 — 45 ve 22 alt başlıkta yazıyor ve DÜŞÜRÜLEMEZ,
# bu yüzden aday listesi hedefin üstünde tutulur.
STORY_CANDIDATE_MIN   = 55
CULTURE_CANDIDATE_MIN = 26


# =============================================================================
# 3. METİN BANTLARI — CHILDREN_WRITING_STYLE § 3.1 ve § 4
# =============================================================================

BANDS = {
    # hikâye gövdesi
    "story_words":          (800, 1100),
    "story_words_target":   950,
    # kültürel not — 2 satır (yol haritasının kararı)
    "cultural_note_words":  (25, 45),
    # cümle
    "sentence_avg":         (11.0, 14.0),
    "sentence_max":         25,
    # paragraf
    "paragraph_sentences":  (1, 6),
    "paragraph_avg":        (3.0, 5.0),
    # diyalog
    "dialogue_share":       (0.05, 0.30),
    # okunabilirlik — CHILDREN_WRITING_STYLE § 4
    "syllables_per_word":   (1.35, 1.55),
    "syllables_per_word_fail_high": 1.65,
    "hard_word_share":      0.06,
    "hard_word_share_fail": 0.09,
    "flesch_kincaid":       (4.0, 6.5),
    "flesch_kincaid_fail":  (3.0, 7.5),
    "passive_share":        0.08,
    "passive_share_fail":   0.15,
    # yaş — AGE_POLICY § 4
    "exclamations_per_story":   3,
    "intense_scene_sentences":  3,
    "intense_scenes_per_story": 2,
    "proper_names_per_story":   7,
    # sürüklenme — qa_drift
    "drift_warn_pct": 20.0,
    "drift_fail_pct": 35.0,
    # tekrar — qa_echo
    "echo_ngram": 8,
}


# =============================================================================
# 4. YASAK KALIPLAR — CHILDREN_WRITING_STYLE § 2.2
# =============================================================================
# Her kalıp bir gerekçeyle listede. Gerekçesi olmayan kalıp eklenmez;
# gerekçesiz bir yasak, yazarı sebepsiz kısıtlar.

FORBIDDEN_PATTERNS: list[tuple[str, str, str]] = [
    # (kimlik, regex, gerekçe)
    ("self-reference-chapter",
     r"\b(?:in this book|in this chapter|as we saw|as you (?:will )?(?:saw|see)|earlier in this|later in this)\b",
     "Kitabın kendine göndermesi — Bestiarium bu kusurdan 57 örnek yakaladı"),

    ("self-reference-story",
     r"\b(?:the (?:next|previous|last) story|another story in this)\b",
     "Kitabın kendine göndermesi"),

    ("condescending-narrator",
     r"\b(?:now you (?:will )?(?:see|know)|of course,? this (?:was|is) not|little (?:reader|ones)|as any child knows)\b",
     "Tepeden bakan anlatıcı — okuru çocuk yerine koyar"),

    ("moral-tag",
     r"\b(?:and so they learned that|the lesson (?:here )?is|which (?:just )?goes to show|the moral of)\b",
     "Ders veren kapanış — mit ders vermez"),

    ("analytic-register",
     r"\b(?:the function of this (?:story|tale)|what the tradition supplies|serves to remind us|in a sense,)\b",
     "Yetişkin analitik kayıt — Bestiarium'un üslup sürüklenmesinin kaynağı"),

    ("euphemism-death",
     r"\b(?:passed away|fell asleep forever|went to a better place|was no more)\b",
     "Ölüm örtmecesi — AGE_POLICY § 2.2 yasaklıyor"),

    ("hedge-pile",
     r"\b(?:some say that some|perhaps maybe|it is possible that perhaps)\b",
     "Belirsizlik yığını — varyantlar kültürel nota gider"),

    ("fairytale-opener",
     r"^\s*(?:once upon a time|long ago in a land far away|in a land far,? far away)\b",
     "Masal kalıbı — 22 kültürün 22 dünyasını tek kapıdan geçirmek onları siler"),

    ("anachronism",
     r"\b(?:skyscraper|football (?:field|pitch)|the size of a bus|like a rocket)\b",
     "Anakronizm — ölçek mitin kendi dünyasından verilir"),

    ("placeholder",
     r"\b(?:TODO|TBD|FIXME|XXX|LOREM IPSUM|\[placeholder\]|\?\?\?)\b",
     "Yer tutucu metne sızmış"),
]


# =============================================================================
# 5. YAŞ POLİTİKASI DESENLERİ — AGE_POLICY § 4
# =============================================================================
# Bu listeler qa_age.py'nin kapısıdır. Sözcük listeleri kaba araçlardır ve
# YANLIŞ POZİTİF üretebilirler; bu yüzden her biri kelime sınırına saygılı
# ve bağlam istisnalarıyla birlikte tanımlıdır (Bestiarium D32 dersi:
# "doğru metni reddeden bir cetvel" yazmayın).

# § 2.1 · Grafik şiddet — ÇIKARILAN
GRAPHIC_TERMS = [
    "disembowel", "disemboweled", "disembowelled", "eviscerate", "eviscerated",
    "entrails", "intestines", "gore", "gory",
    "mutilate", "mutilated", "mutilation",
    "dismember", "dismembered", "dismemberment",
    "decapitate", "decapitated",           # "beheaded" İMA seviyesinde serbest
    "blood-soaked", "bloodsoaked", "blood-drenched",
    "spurt", "spurted", "spurting",
    "writhing in agony", "screamed in agony",
    "torture", "tortured", "torturing",
    "flayed", "flaying",
    "rotting corpse", "rotting flesh", "putrid",
    "maggot", "maggots",
]

# § 2.8 · Cinsellik — ÇIKARILAN (mutlak)
SEXUAL_TERMS = [
    "rape", "raped", "raping", "ravish", "ravished", "ravishment",
    "seduce", "seduced", "seducing", "seduction",
    "naked", "nakedness", "nude", "nudity",
    "lust", "lustful", "aroused", "arousal",
    "consummate", "consummated", "impregnate", "impregnated",
    "concubine", "harem", "fornicate", "fornication",
    "virginity", "deflower",
]

# § 2.9 · İstismar — ÇIKARILAN
ABUSE_TERMS = [
    "molest", "molested", "molesting",
    "beat the child", "beat her senseless", "beat him senseless",
    "starved the child", "locked the child",
]

# İma edilebilir ama YOĞUN SAHNE sayılan fiiller. Ardışık kullanımları
# § 2.1'in "≤3 cümle" kuralını tetikler.
INTENSE_VERBS = [
    "kill", "killed", "killing", "slay", "slew", "slain", "slaughter",
    "stab", "stabbed", "strike", "struck", "smash", "smashed",
    "tear", "tore", "torn", "crush", "crushed", "devour", "devoured",
    "swallow", "swallowed", "burn", "burned", "burnt", "drown", "drowned",
    "bleed", "bled", "wound", "wounded", "blood",
]

# § 2.14 · "Son sayfa kuralı" — hikâyenin SON paragrafında çözümsüz korku
UNRESOLVED_FEAR_TERMS = [
    "still out there", "still waiting", "never found", "was never seen again and",
    "no one ever came", "waits for you", "is coming for", "will come for you",
    "and it is still", "and she is still hungry", "and he is still hungry",
]

# § 2.15 · Geçmiş zaman tuzağı — yaşayan inanç için
# (Kültür `livingTradition: true` ise bu kalıplar HATA)
LIVING_PAST_TENSE = [
    r"\b(?:they|people|the \w+s) (?:used to believe|once believed|believed)\b",
    r"\bin the old days,? (?:they|people) (?:worshipped|worshiped)\b",
    r"\bno longer believed\b",
]

# § 2.15 · Yaşayan gelenek için "myth" kelimesi kullanılmaz
LIVING_MYTH_WORD = r"\bmyths?\b"

# § 2.16 · Kısıtlı bilgi işaretçileri — metinde görünürse ÖZEL İNCELEME
RESTRICTED_MARKERS = [
    "initiation rite", "initiation ceremony", "secret name", "sacred bundle",
    "clan mark", "mask pattern", "the ceremony is performed by",
    "only initiates", "restricted knowledge",
]

# STYLE § 7 · Genelleme yasağı
GENERALISATION_PATTERNS = [
    r"\bAfricans (?:believe|believed|say|said|think|thought)\b",
    r"\bNative Americans (?:believe|believed|say|said)\b",
    r"\bAsians (?:believe|believed|say|said)\b",
    r"\bprimitive (?:people|tribes?|beliefs?)\b",
    r"\bsavage (?:tribes?|people)\b",
    r"\bexotic (?:tribes?|people|customs?)\b",
]


# =============================================================================
# 6. TİPOGRAFİ — CHILDREN_WRITING_STYLE § 6
# =============================================================================

TYPOGRAPHY_RULES = [
    ("straight-apostrophe", r"(?<=[A-Za-z])'(?=[A-Za-z])",
     "düz kesme ' yerine tipografik ’ kullanılır"),
    ("straight-quote", r'(?<![=<])"',
     'düz tırnak " yerine “ ” kullanılır'),
    ("triple-dot", r"\.\.\.",
     "üç nokta … tek karakteriyle yazılır"),
    ("spaced-em-dash", r"\s—\s",
     "em dash boşluksuz kullanılır"),
    ("double-space", r"(?<=\S)  +(?=\S)",
     "çift boşluk"),
    ("double-hyphen", r"(?<!-)--(?!-)",
     "-- yerine em dash — kullanılır"),
]

# Görünmez / tehlikeli karakterler. Kaçış dizisiyle yazılır — Bestiarium'un
# validate_structure'ı bu tabloyu doğrudan yazdığı için KENDİ KAYNAĞINI
# kirletmişti (LESSONS § B5).
INVISIBLE_CHARS = {
    "\u200b": "ZERO WIDTH SPACE",
    "\u200c": "ZERO WIDTH NON-JOINER",
    "\u200d": "ZERO WIDTH JOINER",
    "\u200e": "LEFT-TO-RIGHT MARK",
    "\u200f": "RIGHT-TO-LEFT MARK",
    "\u00a0": "NO-BREAK SPACE",
    "\ufeff": "ZERO WIDTH NO-BREAK SPACE (BOM)",
    "\u2028": "LINE SEPARATOR",
    "\u2029": "PARAGRAPH SEPARATOR",
}


# =============================================================================
# 7. METİN YARDIMCILARI
# =============================================================================

_SENTENCE_END = re.compile(r"(?<=[.!?…])[\"'”’)\]]*\s+")
_WORD = re.compile(r"[A-Za-zÀ-ɏḀ-ỿ'’-]+")
_VOWEL_GROUP = re.compile(r"[aeiouy]+", re.I)


def sentences(text: str) -> list[str]:
    """Cümlelere böl. Kısaltmalar için kaba ama tutarlı."""
    text = re.sub(r"\s+", " ", text or "").strip()
    if not text:
        return []
    parts = _SENTENCE_END.split(text)
    return [p.strip() for p in parts if p.strip()]


def words(text: str) -> list[str]:
    return _WORD.findall(text or "")


def word_count(text: str) -> int:
    return len(words(text))


def paragraphs(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", text or "") if p.strip()]


def syllables(word: str) -> int:
    """Yaklaşık hece sayısı (İngilizce). Okunabilirlik için yeterli."""
    w = word.lower().strip("'’-")
    if not w:
        return 0
    groups = _VOWEL_GROUP.findall(w)
    n = len(groups)
    # sondaki sessiz -e
    if w.endswith("e") and n > 1 and not w.endswith(("le", "ee", "ye")):
        n -= 1
    # -ed eki genelde hece eklemez
    if w.endswith("ed") and n > 1 and not re.search(r"[td]ed$", w):
        n -= 1
    return max(1, n)


def is_proper_name(word: str) -> bool:
    """Büyük harfle başlıyor ve tamamı büyük harf değil.

    ⚠ TEK BAŞINA YETMEZ: her cümle büyük harfle başlar. Bir metindeki
    gerçek özel adlar için proper_names() kullanın."""
    return bool(word) and word[0].isupper() and not word.isupper()


def proper_names(text: str) -> set[str]:
    """
    Metindeki GERÇEK özel adlar: cümle BAŞI OLMAYAN bir konumda büyük
    harfle geçen sözcükler.

    Bu ayrım olmadan kapı, her cümlenin ilk sözcüğünü özel ad sayar ve
    hikâye başına 7 ad tavanını hemen aşar — yani DOĞRU METNİ REDDEDEN
    bir cetvel olur (Bestiarium D32'nin aynı sınıfı).
    """
    found: set[str] = set()
    for sentence in sentences(text):
        toks = words(sentence)
        for w in toks[1:]:                    # ilk sözcük ATLANIR
            if is_proper_name(w) and len(w) >= 2:
                found.add(w)
    return found


def strip_diacritics(s: str) -> str:
    """NFD + birleşen işaret temizliği. Türkçe İ tuzağına dikkat (LESSONS § B9)."""
    s = s.replace("ı", "i").replace("İ", "I")
    nfd = unicodedata.normalize("NFD", s)
    return "".join(c for c in nfd if not unicodedata.combining(c))


def slugify(s: str) -> str:
    s = strip_diacritics(s).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


# =============================================================================
# 8. VERİ YÜKLEME
# =============================================================================

def load_cultures() -> dict:
    with open(CULTURE_INDEX, encoding="utf-8") as fh:
        return json.load(fh)


def load_stories() -> dict:
    with open(STORY_INDEX, encoding="utf-8") as fh:
        return json.load(fh)


def load_book() -> dict | None:
    """Manuscript. Depoda YOKTUR (.gitignore § ①). Yoksa None."""
    for path in (BOOK_EDITED_JSON, BOOK_JSON):
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                return json.load(fh)
    # Test kurgusu bir çevre değişkeniyle enjekte edilir; selftest böyle
    # gerçek kapıları gerçek kusurlu metne karşı koşturur.
    override = os.environ.get("MYTHBOOK_BOOK_JSON")
    if override and os.path.exists(override):
        with open(override, encoding="utf-8") as fh:
            return json.load(fh)
    return None


def book_stories(book: dict | None) -> dict:
    if not book:
        return {}
    return book.get("stories", {}) or {}


def culture_by_id(cultures: dict) -> dict:
    return {c["id"]: c for c in cultures.get("cultures", [])}


# =============================================================================
# 9. RAPOR YARDIMCISI
# =============================================================================

class Result:
    """Kapı sonuçlarını toplar, basar, JSON'a yazar."""

    def __init__(self, name: str, verbose: bool = False):
        self.name = name
        self.verbose = verbose
        self.checks: list[dict] = []

    def add(self, ok: bool, passed_msg: str, failed_msg: str = "", warn: bool = False):
        entry = {
            "ok": bool(ok),
            "warn": bool(warn and not ok),
            "message": passed_msg if ok else (failed_msg or passed_msg),
            "rule": passed_msg,
        }
        self.checks.append(entry)
        if self.verbose or not ok:
            if ok:
                print(f"  ✓ {passed_msg}")
            elif warn:
                print(f"  ⚠ {entry['message']}")
            else:
                print(f"  ✗ {entry['message']}")
        return ok

    def ok(self, msg: str, detail: str = ""):
        return self.add(True, msg + (f" — {detail}" if detail else ""))

    def fail(self, msg: str, detail: str = ""):
        return self.add(False, msg, f"{msg} — {detail}" if detail else msg)

    def warn(self, ok: bool, passed_msg: str, failed_msg: str = ""):
        return self.add(ok, passed_msg, failed_msg, warn=True)

    @property
    def failures(self) -> list[dict]:
        return [c for c in self.checks if not c["ok"] and not c["warn"]]

    @property
    def warnings(self) -> list[dict]:
        return [c for c in self.checks if c["warn"]]

    def write_json(self, path: str | None):
        if not path:
            return
        os.makedirs(os.path.dirname(path), exist_ok=True)
        payload = {
            "gate": self.name,
            "checks": self.checks,
            "passed": len(self.checks) - len(self.failures) - len(self.warnings),
            "failed": len(self.failures),
            "warnings": len(self.warnings),
        }
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=2)
            fh.write("\n")

    def finish(self, json_path: str | None = None) -> int:
        self.write_json(json_path)
        n_fail, n_warn = len(self.failures), len(self.warnings)
        n_pass = len(self.checks) - n_fail - n_warn
        print()
        if n_fail:
            print(f"  ⛔ {self.name}: {n_fail} başarısız · {n_warn} uyarı · {n_pass} geçti")
            return 1
        print(f"  ✅ {self.name}: {n_pass} geçti · {n_warn} uyarı")
        return 0


def banner(title: str) -> None:
    print()
    print("─" * 72)
    print(f"▸ {title}")
    print("─" * 72)
