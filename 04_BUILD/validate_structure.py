#!/usr/bin/env python3
"""
DEPO, BELGE VE VARLIK BÜTÜNLÜĞÜ
================================================================================
Denetlediği:
  · dizin ağacı ve zorunlu dosyalar
  · Markdown bağları (kırık iç bağlantı)
  · kodlama, görünmez karakter, tipografi
  · veri dosyalarının okunabilirliği
  · belge ↔ kod tutarlılığı (aynı sayı iki belgede farklı yazılmış mı)
  · STYLE.md'nin işaret levhası olarak kalması
  · MANUSCRIPT SIZINTISI  ← public depo politikasının mekanizması
  · gizli bilgi taraması
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb

ROOT = mb.ROOT

# =============================================================================
# BEKLENEN AĞAÇ
# =============================================================================

REQUIRED_DIRS = [
    "00_CONTEXT", "01_RESEARCH", "02_MANUSCRIPT", "03_EDITORIAL",
    "04_BUILD", "05_TESTS", "06_REPORTS", "07_ASSETS", "08_OUTPUT",
    "09_ARCHIVE", ".github/workflows",
]

REQUIRED_FILES = [
    ".gate",
    ".gitignore",
    "LICENSE",
    "README.md",
    "PROJECT_CONTEXT.md",
    "BRIEF.md",
    "STYLE.md",
    "AGE_POLICY.md",
    "SOURCING_STANDARD.md",
    "DECISIONS.md",
    "CHANGELOG.md",
    "BOOK_STATS.md",
    "ROADMAP_PROGRESS.md",
    "KDP_UPLOAD_PLAYBOOK.md",
    "THE_GREAT_BOOK_OF_WORLD_MYTHS_MASTER_ROADMAP.md",
    "project_config.json",
    "00_CONTEXT/LESSONS_FROM_CODEX_BESTIARIUM.md",
    "00_CONTEXT/CHILDREN_WRITING_STYLE.md",
    "00_CONTEXT/EDITORIAL_ARCHITECTURE.md",
    "01_RESEARCH/culture_index.json",
    "01_RESEARCH/story_index.json",
    "01_RESEARCH/culture_index.schema.json",
    "01_RESEARCH/story_index.schema.json",
    "01_RESEARCH/RESEARCH_RECORD_TEMPLATE.md",
    "04_BUILD/qa_all.sh",
    "05_TESTS/selftest.py",
    "07_ASSETS/IMAGE_PROMPT_LIBRARY.md",
    ".github/workflows/validate.yml",
]

DATA_FILES = [
    "project_config.json",
    "01_RESEARCH/culture_index.json",
    "01_RESEARCH/story_index.json",
    "01_RESEARCH/culture_index.schema.json",
    "01_RESEARCH/story_index.schema.json",
]

TEXT_EXTS = (".md", ".json", ".yml", ".yaml", ".py", ".sh", ".txt", ".html")

SKIP_DIRS = {".git", "__pycache__", ".venv", "node_modules", ".pytest_cache"}


def walk_files() -> list[str]:
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in filenames:
            full = os.path.join(dirpath, f)
            out.append(os.path.relpath(full, ROOT))
    return sorted(out)


def read(path: str) -> str:
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        return fh.read()


def strip_code(md: str) -> str:
    """Kod bloklarını ve satır içi kodu YER TUTUCUYA çevirir, SİLMEZ.
    Bestiarium B6: silmek `a` b ifadesini '  b' yapıyor ve 'çift boşluk'
    olarak raporlanıyordu."""
    md = re.sub(r"```.*?```", "", md, flags=re.S)
    md = re.sub(r"`[^`\n]*`", "", md)
    return md


# =============================================================================
# DENETİMLER
# =============================================================================

def check_tree(r: mb.Result) -> None:
    mb.banner("dizin ağacı ve zorunlu dosyalar")

    missing_dirs = [d for d in REQUIRED_DIRS if not os.path.isdir(os.path.join(ROOT, d))]
    r.add(not missing_dirs, f"bütün dizinler var ({len(REQUIRED_DIRS)})",
          f"eksik dizin: {missing_dirs}")

    missing_files = [f for f in REQUIRED_FILES if not os.path.isfile(os.path.join(ROOT, f))]
    r.add(not missing_files, f"bütün zorunlu dosyalar var ({len(REQUIRED_FILES)})",
          f"eksik dosya: {missing_files}")

    # .gate geçerli mi
    try:
        gate = mb.read_gate()
        r.ok(f".gate geçerli: {gate}")
    except ValueError as exc:
        r.fail(".gate geçersiz", str(exc))


def check_data_files(r: mb.Result) -> None:
    mb.banner("veri dosyaları")
    for path in DATA_FILES:
        full = os.path.join(ROOT, path)
        if not os.path.exists(full):
            r.fail(f"{path} yok")
            continue
        try:
            with open(full, encoding="utf-8") as fh:
                json.load(fh)
            r.ok(f"{path} geçerli JSON")
        except json.JSONDecodeError as exc:
            r.fail(f"{path} bozuk JSON", str(exc))


def check_encoding(files: list[str], r: mb.Result) -> None:
    mb.banner("kodlama ve görünmez karakterler")

    bad_encoding, invisible, trailing, no_newline = [], [], [], []
    for path in files:
        if not path.endswith(TEXT_EXTS):
            continue
        full = os.path.join(ROOT, path)
        try:
            with open(full, "rb") as fh:
                raw = fh.read()
        except OSError:
            continue
        try:
            body = raw.decode("utf-8")
        except UnicodeDecodeError:
            bad_encoding.append(path)
            continue
        # Bu betiğin KENDİSİ desen tablosunu taşır — kaçış dizisiyle yazıldığı
        # için tabloda gerçek karakter yoktur ve tarama kendini yakalamaz.
        if path in ("04_BUILD/mythbook.py", "04_BUILD/validate_structure.py"):
            continue
        for ch, label in mb.INVISIBLE_CHARS.items():
            if ch in body:
                invisible.append(f"{path}: {label}")
        if re.search(r"[ \t]+\n", body):
            trailing.append(path)
        if raw and not raw.endswith(b"\n"):
            no_newline.append(path)

    r.add(not bad_encoding, "bütün metin dosyaları UTF-8", f"UTF-8 değil: {bad_encoding}")
    r.add(not invisible, "görünmez karakter yok", f"bulundu: {invisible[:10]}")
    r.warn(not trailing, "satır sonu boşluğu yok", f"boşluklu: {trailing[:10]}")
    r.warn(not no_newline, "dosyalar satır sonuyla bitiyor", f"bitmiyor: {no_newline[:10]}")


def check_links(files: list[str], r: mb.Result) -> None:
    mb.banner("Markdown bağları")

    broken = []
    for path in files:
        if not path.endswith(".md"):
            continue
        body = strip_code(read(path))
        base = os.path.dirname(os.path.join(ROOT, path))
        for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)\)", body):
            target = m.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#")[0]
            if not target:
                continue
            resolved = os.path.normpath(os.path.join(base, target))
            if not os.path.exists(resolved):
                broken.append(f"{path} → {target}")
    r.add(not broken, "Markdown iç bağları çalışıyor", f"kırık bağ: {broken[:10]}")


def check_typography(files: list[str], r: mb.Result) -> None:
    mb.banner("belge tipografisi")

    issues = []
    for path in files:
        if not path.endswith(".md"):
            continue
        body = strip_code(read(path))
        if re.search(r"(?<=\S)  +(?=\S)", body):
            issues.append(f"{path}: çift boşluk")
        if "\t" in body:
            issues.append(f"{path}: sekme karakteri")
    r.warn(not issues, "belge tipografisi temiz", f"sorunlar: {issues[:10]}")


def check_style_signpost(r: mb.Result) -> None:
    """STYLE.md bir İŞARET LEVHASIDIR. Buraya kural yazılırsa iki doğruluk
    kaynağı doğar — Bestiarium D17'nin ta kendisi (§ 3 ile § 4 birbiriyle
    çelişiyordu ve çelişki aylar sonra fark edildi)."""
    mb.banner("STYLE.md işaret levhası mı")

    body = read("STYLE.md")
    words = mb.word_count(body)
    r.add(words <= 400,
          f"STYLE.md işaret levhası olarak kalmış ({words} kelime)",
          f"STYLE.md {words} kelimeye çıkmış — kural listesi buraya taşınmış olabilir. "
          "Tek doğruluk kaynağı 00_CONTEXT/CHILDREN_WRITING_STYLE.md'dir.")
    r.add("00_CONTEXT/CHILDREN_WRITING_STYLE.md" in body,
          "STYLE.md tek doğruluk kaynağına yönlendiriyor",
          "STYLE.md CHILDREN_WRITING_STYLE.md'ye bağ vermiyor")


# Nitelenmiş sayılar bir toplam İDDİASI değildir ve hata sayılmaz.
QUALIFIERS = (
    "kalan", "diğer", "başka", "ek ", "yeni", "her ", "ikinci", "cilt ",
    "aday", "kilitli", "yalnızca", "sadece", "en fazla", "en az", "≥", "≤",
    "'sı", "'si", "'ü", "'u", "slot", "yedek", "üstünde", "altında",
)
QUALIFIERS_AFTER = (" daha", " ekle", " slot", " yedek")


def check_doc_consistency(r: mb.Result) -> None:
    """Aynı sayı iki belgede farklı yazılmış mı.
    Talimat § 23: 'code says 45 stories, documentation says 40' asla."""
    mb.banner("belge ↔ kod tutarlılığı")

    docs = {p: read(p) for p in
            ("README.md", "PROJECT_CONTEXT.md", "BRIEF.md",
             "THE_GREAT_BOOK_OF_WORLD_MYTHS_MASTER_ROADMAP.md")
            if os.path.exists(os.path.join(ROOT, p))}

    for label, value, patterns in (
        ("hikâye sayısı", mb.STORY_TARGET, [r"(\d+)\s+(?:hikâye|Stories|stories)\b"]),
        ("kültür sayısı", mb.CULTURE_TARGET, [r"(\d+)\s+(?:kültür|[Cc]ultures)\b"]),
    ):
        wrong = []
        for path, body in docs.items():
            plain = strip_code(body)
            for pattern in patterns:
                for m in re.finditer(pattern, plain):
                    n = int(m.group(1))
                    # Yalnızca HEDEFTEN KÜÇÜK ve yakın sayılar şüphelidir;
                    # "45 hikâye daha" (Cilt II) bir çelişki değildir.
                    if n == value or n > value or abs(n - value) > 15:
                        continue
                    # NİTELENMİŞ sayı bir iddia değildir: "Kalan 16 kültür",
                    # "22'nin 6'sı", "45 hikâye daha". Bunları hata saymak,
                    # DOĞRU METNİ REDDEDEN bir cetvel olur (Bestiarium D32).
                    before = plain[max(0, m.start() - 24):m.start()].lower()
                    after = plain[m.end():m.end() + 12].lower()
                    if any(q in before for q in QUALIFIERS) or \
                       any(q in after for q in QUALIFIERS_AFTER):
                        continue
                    snippet = plain[max(0, m.start() - 40):m.end() + 20].replace("\n", " ")
                    wrong.append(f"{path}: “{m.group(0)}” (kod {value} diyor) …{snippet}…")
        r.add(not wrong, f"{label} belgelerde tutarlı ({value})",
              "ayrışma:\n         " + "\n         ".join(wrong[:6]))

    # project_config ↔ .gate
    gate = mb.read_gate()
    declared = mb._CFG["gates"]["current"]
    r.add(gate == declared, f"project_config.gates.current ↔ .gate ({gate})",
          f"project_config '{declared}', .gate '{gate}'")

    # illüstrasyon kararı ↔ varlık dizini
    if mb._CFG["illustration"]["required"]:
        r.add(os.path.isdir(os.path.join(ROOT, "07_ASSETS", "raw")),
              "illüstrasyon ZORUNLU ve ham görsel dizini var",
              "illüstrasyon zorunlu ama 07_ASSETS/raw yok")
        r.add(os.path.exists(os.path.join(ROOT, "07_ASSETS", "IMAGE_PROMPT_LIBRARY.md")),
              "prompt kütüphanesi var",
              "illüstrasyon zorunlu ama IMAGE_PROMPT_LIBRARY.md yok")


def check_secrets(files: list[str], r: mb.Result) -> None:
    mb.banner("gizli bilgi taraması")

    patterns = [
        ("AWS anahtarı", r"AKIA[0-9A-Z]{16}"),
        ("özel anahtar", r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        ("GitHub jetonu", r"gh[pousr]_[A-Za-z0-9]{36,}"),
        ("Slack jetonu", r"xox[baprs]-[A-Za-z0-9-]{10,}"),
        ("OpenAI anahtarı", r"sk-[A-Za-z0-9]{32,}"),
        ("Anthropic anahtarı", r"sk-ant-[A-Za-z0-9_-]{20,}"),
        ("gömülü parola", r"(?i)\b(?:password|passwd|secret)\s*[:=]\s*[\"'][^\"'\s]{8,}[\"']"),
    ]
    hits = []
    for path in files:
        if not path.endswith(TEXT_EXTS) or path == "04_BUILD/validate_structure.py":
            continue
        try:
            body = read(path)
        except (OSError, UnicodeDecodeError):
            continue
        for label, pattern in patterns:
            if re.search(pattern, body):
                hits.append(f"{path}: {label}")
    r.add(not hits, f"gizli bilgi yok ({len(patterns)} desen tarandı)",
          f"BULUNDU: {hits[:10]} — depo PUBLIC'tir")

    # ikili çöp
    junk = [p for p in files
            if p.endswith((".pyc", ".pyo", ".so", ".o", ".class", ".DS_Store"))]
    r.add(not junk, "ikili çöp yok", f"bulundu: {junk[:10]}")


# =============================================================================
# MANUSCRIPT SIZINTISI — public depo politikasının MEKANİZMASI
# =============================================================================
#
# .gitignore bir YOL listesidir ve başka bir ada konan proza dosyasını
# YAKALAMAZ. Bu denetim ikinci hattır ve İÇERİĞE bakar.
#
# Politikayı bir disiplin talebi olmaktan çıkarıp mekanizmaya bağlar:
# disiplin unutulur, mekanizma unutmaz.

PROSE_PATHS = [
    "02_MANUSCRIPT/",
    "01_RESEARCH/book.json",
    "01_RESEARCH/edits.json",
]

# İçerik taramasından muaf: bu denetimin KENDİSİ ve politikayı anlatan
# belgeler yol adlarını yazmak zorundadır.
LEAK_SCAN_SKIP = {
    ".gitignore",
    "04_BUILD/validate_structure.py",
    "05_TESTS/selftest.py",
    "02_MANUSCRIPT/README.md",
    "THE_GREAT_BOOK_OF_WORLD_MYTHS_MASTER_ROADMAP.md",
    "00_CONTEXT/LESSONS_FROM_CODEX_BESTIARIUM.md",
    "DECISIONS.md",
    "README.md",
}


def tracked_files() -> list[str] | None:
    try:
        out = subprocess.run(["git", "-C", ROOT, "ls-files"],
                             capture_output=True, text=True, timeout=30, check=False)
    except (OSError, subprocess.SubprocessError):
        return None
    if out.returncode != 0:
        return None
    return [l for l in out.stdout.splitlines() if l.strip()]


def check_manuscript_leak(r: mb.Result) -> None:
    mb.banner("manuscript sızıntısı (public depo politikası)")

    tracked = tracked_files()
    if tracked is None:
        r.ok("sızıntı denetimi atlandı", "git deposu okunamadı")
        return

    # --- ① .gitignore kuralları hâlâ yerinde mi ---
    gi = read(".gitignore") if os.path.exists(os.path.join(ROOT, ".gitignore")) else ""
    missing = [p for p in PROSE_PATHS if p.rstrip("/") not in gi]
    r.add(not missing, ".gitignore proza yollarını dışarıda tutuyor",
          f"eksik kural: {missing} — kural silinirse politika SESSİZCE düşer")

    # --- ② proza yolları takip ediliyor mu ---
    leaked = [f for f in tracked
              if any(f == p or f.startswith(p) for p in PROSE_PATHS)
              and not f.endswith((".gitkeep", "README.md"))]
    r.add(not leaked, "proza dosyası takip edilmiyor",
          f"SIZINTI: {leaked[:10]} — `git rm --cached` ile çıkarın")

    # --- ③ İÇERİK: hikâye prozası takip edilen bir dosyaya sızmış mı ---
    book = mb.load_book()
    stories = mb.book_stories(book)
    if not stories:
        r.ok("içerik taraması", "yerelde manuscript yok — taranacak metin yok")
        return

    # Ölçüt: her hikâyenin AÇILIŞ cümlesi benzersizdir (qa_voice bunu ayrıca
    # garanti eder). Açılış cümlesi takip edilen bir dosyada birebir geçiyorsa
    # proza sızmıştır.
    needles = []
    for sid, s in stories.items():
        opening = (mb.sentences(s.get("text", "")) or [""])[0].strip()
        if len(opening) >= 40:
            needles.append((sid, opening))

    hits = []
    for path in tracked:
        if path in LEAK_SCAN_SKIP or not path.endswith(TEXT_EXTS):
            continue
        full = os.path.join(ROOT, path)
        if not os.path.isfile(full):
            continue
        try:
            body = read(path)
        except (OSError, UnicodeDecodeError):
            continue
        for sid, opening in needles:
            if opening in body:
                hits.append(f"{path} ← “{sid}” açılış cümlesi")

    r.add(not hits,
          f"hikâye prozası takip edilen dosyalara sızmamış ({len(needles)} hikâye tarandı)",
          "SIZINTI:\n         " + "\n         ".join(hits[:10]))


def check_reports_tracked(r: mb.Result) -> None:
    """Karar K18 — Bestiarium'un ÜÇÜNCÜ ölü kuralı burada tekrarlanmasın.

    Orada `06_REPORTS/*.json` toptan .gitignore'daydı ama plates.yml
    `06_REPORTS/plate-consistency.json` dosyasını denetlemeye çalışıyordu.
    Dosya depoda hiç bulunmadığı için o adım CI'da HER KOŞUDA sessizce
    boş geçiyordu.
    """
    mb.banner("denetlenen raporlar depoda mı (karar K18)")

    gi = read(".gitignore")
    r.add("!06_REPORTS/tracked/" in gi,
          ".gitignore denetlenen rapor dizinini muaf tutuyor",
          "`!06_REPORTS/tracked/` kuralı yok — denetlenecek bir rapor depoda "
          "durmuyorsa o denetim ÖLÜ KURALDIR")
    r.add(os.path.isdir(mb.REPORTS_TRACKED),
          "06_REPORTS/tracked/ dizini var",
          "denetlenen rapor dizini yok")


# =============================================================================
# GİRİŞ NOKTASI
# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description="Depo, belge ve varlık bütünlüğü")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  DEPO, BELGE VE VARLIK BÜTÜNLÜĞÜ")
    print("═" * 72)

    r = mb.Result("validate_structure", verbose=args.verbose)
    files = walk_files()

    check_tree(r)
    check_data_files(r)
    check_encoding(files, r)
    check_links(files, r)
    check_typography(files, r)
    check_style_signpost(r)
    check_doc_consistency(r)
    check_secrets(files, r)
    check_manuscript_leak(r)
    check_reports_tracked(r)

    return r.finish(args.json)


if __name__ == "__main__":
    sys.exit(main())
