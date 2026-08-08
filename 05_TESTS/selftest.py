#!/usr/bin/env python3
"""
KAPILARIN KENDİ TESTİ — bu hattın EN ÖNEMLİ testi
================================================================================
Metin yokken yeşil kalan bir hat, KUSUR GELDİĞİNDE DE YEŞİL KALABİLİR.

Bu test o riski kapatır: her kapı için TAM BİR KUSUR taşıyan kurgu bir kitap
çalıştırılır ve kapının o kusuru YAKALADIĞI kanıtlanır.

Bu projede daha da kritiktir, çünkü `qa_age.py` 45 hikâyeyi otomatik
reddetme yetkisine sahiptir ve o yetki, doğru çalıştığı kanıtlanmadan
kullanılamaz.

Dört bölüm:
  ①  temiz kurgu BÜTÜN kapılardan geçer          (yanlış pozitif yok)
  ②  her kusurlu kurgu İLGİLİ kapıda yakalanır   (körlük yok)
  ③  kapı seviyeleri gerçekten kilitliyor        (şema kapıları)
  ④  her muafiyet en az bir kez DEVREYE GİRİYOR  (ölü kural yok)

Dördüncüsü Bestiarium'un üç ölü kuralına doğrudan cevaptır.
"""

from __future__ import annotations

import argparse
import copy
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BUILD = os.path.join(ROOT, "04_BUILD")
sys.path.insert(0, BUILD)
sys.path.insert(0, HERE)

import mythbook as mb
import make_fixtures as fx

# qa_crossref BİLEREK DIŞARIDA: manuscript'i GERÇEK story_index.json ile
# karşılaştırır, yani bağımsız bir kurgu onu tanım gereği ihlal eder.
# Kendi kusurlu-kurgu testi Faz 1'de, envanter kilitlenince eklenir.
GATES = ["qa_length", "qa_voice", "qa_readability", "qa_age", "qa_echo",
         "qa_diacritics", "qa_drift"]


def run_gate(gate: str, book_path: str | None) -> tuple[int, str]:
    env = dict(os.environ)
    if book_path:
        env["MYTHBOOK_BOOK_JSON"] = book_path
    else:
        env.pop("MYTHBOOK_BOOK_JSON", None)
    out = subprocess.run([sys.executable, os.path.join(BUILD, f"{gate}.py")],
                         capture_output=True, text=True, env=env, timeout=120)
    return out.returncode, out.stdout + out.stderr


def write_book(book: dict, tmp: str, name: str) -> str:
    path = os.path.join(tmp, name)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(book, fh, ensure_ascii=False)
    return path


class Report:
    def __init__(self, verbose: bool):
        self.verbose = verbose
        self.failed: list[str] = []
        self.passed = 0

    def check(self, ok: bool, label: str, detail: str = ""):
        if ok:
            self.passed += 1
            if self.verbose:
                print(f"  ✓ {label}")
        else:
            self.failed.append(f"{label} — {detail}" if detail else label)
            print(f"  ✗ {label}" + (f"\n      {detail}" if detail else ""))


# =============================================================================
# ① TEMİZ KURGU BÜTÜN KAPILARDAN GEÇER
# =============================================================================

def test_clean(tmp: str, rep: Report) -> None:
    mb.banner("① temiz kurgu bütün kapılardan geçmeli (yanlış pozitif yok)")

    collisions = fx.verify_generator()
    rep.check(not collisions, "kurgu üreteci kendini tekrarlamıyor",
              f"{len(collisions)} çakışan öbek — düzeltilecek olan betik değil "
              "KURGUDUR (Bestiarium B4)")

    path = write_book(fx.build(None), tmp, "clean.json")
    for gate in GATES:
        code, out = run_gate(gate, path)
        rep.check(code == 0, f"{gate}: temiz kurguyu geçiriyor",
                  "\n      ".join(l for l in out.splitlines() if "✗" in l)[:400])


# =============================================================================
# ② HER KUSUR YAKALANIR
# =============================================================================

def test_defects(tmp: str, rep: Report) -> None:
    mb.banner("② her kusurlu kurgu ilgili kapıda yakalanmalı (körlük yok)")

    for defect, (gate, _, description) in fx.DEFECTS.items():
        path = write_book(fx.build(defect), tmp, f"{defect}.json")
        code, out = run_gate(gate, path)
        rep.check(code != 0,
                  f"{gate} ← {defect}: {description}",
                  "KAPI KUSURU GÖRMEDİ. Kapı kör — bu kusur üretime sızabilir.\n"
                  f"      Kapı çıktısı: {out.strip().splitlines()[-1] if out.strip() else '—'}")


# =============================================================================
# ③ KAPI SEVİYELERİ GERÇEKTEN KİLİTLİYOR
# =============================================================================

def test_gate_levels(rep: Report) -> None:
    """
    ⚠ Bestiarium B3/D20: bu test SABİT SEVİYE VARSAYMAMALI.
    "Bir üst kapı kapalı olmalı" varsayımı, o kapı açıldığı anda kendini
    yanlışlıyordu. Test .gate'i OKUR ve BİR ÜSTÜNÜN kapalı olduğunu sınar.
    """
    mb.banner("③ kapı seviyeleri kilitliyor mu")

    current = mb.read_gate()
    rank = mb.gate_rank(current)

    code = subprocess.run(
        [sys.executable, os.path.join(BUILD, "validate_spec.py"), "--gate", current],
        capture_output=True, text=True, timeout=120).returncode
    rep.check(code == 0, f"mevcut kapı ({current}) geçiyor",
              "mevcut kapı kırmızı — depo kendi seviyesini karşılamıyor")

    if rank + 1 < len(mb.GATE_LEVELS):
        nxt = mb.GATE_LEVELS[rank + 1]
        out = subprocess.run(
            [sys.executable, os.path.join(BUILD, "validate_spec.py"), "--gate", nxt],
            capture_output=True, text=True, timeout=120)
        rep.check(out.returncode != 0,
                  f"bir üst kapı ({nxt}) KAPALI",
                  f"'{nxt}' kapısı zaten geçiyor — kapı bir şey KİLİTLEMİYOR. "
                  "Kümülatif kapı sistemi anlamsızlaşır (karar K8).")
    else:
        rep.check(True, "en üst kapıdayız — üstü sınanmadı")

    # geçersiz seviye reddedilmeli
    out = subprocess.run(
        [sys.executable, os.path.join(BUILD, "validate_spec.py"), "--gate", "phase99"],
        capture_output=True, text=True, timeout=60)
    rep.check(out.returncode != 0, "geçersiz kapı seviyesi reddediliyor",
              "'phase99' kabul edildi — kapı adı doğrulanmıyor")


# =============================================================================
# ④ HER MUAFİYET DEVREYE GİRİYOR — ölü kural avı
# =============================================================================

def test_exemptions_live(tmp: str, rep: Report) -> None:
    """
    Bestiarium'un ÜÇ ölü kuralı da sessizdi:
      Ö1 ALLOWED_ECHOES  — 8-gram'ın 4 kelimelik öğeye BİREBİR eşitliği aranıyordu
      Ö2 LIVING_TRADITIONS — iki kimlik hiçbir geleneğe denk gelmiyordu
      Ö3 06_REPORTS/*.json — denetlenen rapor depoda hiç bulunmuyordu

    Ölü kural, yanlış kuraldan tehlikelidir: yanlış kural hata verir,
    ölü kural HİÇBİR ŞEY DEMEZ.
    """
    mb.banner("④ her muafiyet en az bir kez devreye giriyor mu (ölü kural avı)")

    # --- qa_echo muafiyeti: muaf öbek TEKRAR EDİLEBİLMELİ ---
    import qa_echo
    rep.check(bool(qa_echo.ALLOWED_ECHOES), "qa_echo muafiyet listesi boş değil")

    for idx, phrase in enumerate(qa_echo.ALLOWED_ECHOES):
        book = fx.build(None)
        # Muaf öbeği İKİ hikâyeye koy. PAYLAŞILAN TEK ŞEY öbeğin KENDİSİ olsun:
        # kuyruklar farklı, böylece sınırı aşan n-gram'lar paylaşılmaz ve
        # yalnızca öbeğin İÇİNDEKİ n-gram'lar sınanır.
        book["stories"]["fx-000"]["text"] += f"\n\n{phrase} Aro of the alder quarry."
        book["stories"]["fx-001"]["text"] += f"\n\n{phrase} Beki near the birch harbour."
        path = write_book(book, tmp, f"exempt-{idx}.json")
        code, out = run_gate("qa_echo", path)
        rep.check(code == 0, f"qa_echo muafiyeti canlı: “{phrase}”",
                  "muafiyet DEVREYE GİRMEDİ — kural ölü olabilir (Bestiarium Ö1). "
                  "Muafiyet İKİ YÖNLÜ KAPSAMA ile çalışmalı: muaf öbek n-gram'dan "
                  "uzunsa tek yönlü kapsama hiç devreye girmez.\n      "
                  + "\n      ".join(l for l in out.splitlines() if "→" in l)[:300])

    # --- qa_echo muafiyeti KÖRLEŞTİRMEMELİ ---
    book = fx.build(None)
    # Muaf öbeğin YANINA gerçek bir tekrar koy — kapı onu YAKALAMALI.
    leaked = (f"\n\n{qa_echo.ALLOWED_ECHOES[0]} and then the lantern was carried "
              "down to the water before the tide turned again that evening.")
    book["stories"]["fx-002"]["text"] += leaked
    book["stories"]["fx-003"]["text"] += leaked
    path = write_book(book, tmp, "exempt-not-blind.json")
    code, _ = run_gate("qa_echo", path)
    rep.check(code != 0, "qa_echo muafiyeti kapıyı KÖRLEŞTİRMİYOR",
              "muaf öbeğin YANINDAKİ gerçek tekrar da kaçtı — muafiyet çok geniş")

    # --- ÖLÜ MUAFİYET AVI: sızıntı taramasının muaf listesi (Faz 1) ---
    # `LEAK_SCAN_SKIP` içerik taramasından muaf tutulan dosyaları sayar.
    # Takip EDİLMEYEN bir dosya için muafiyet tutmak anlamsızdır ve daha
    # kötüsü yanıltıcıdır: liste "bu dosyayı düşündük" der ama dosya zaten
    # taramaya hiç girmez. Faz 1'de tam olarak bu bulundu —
    # 02_MANUSCRIPT/README.md muaf listesindeydi ama .gitignore onu
    # sessizce dışarıda tutuyordu (sonraki kural öncekini eziyordu).
    import validate_structure as vst
    _tracked = set(vst.tracked_files() or [])
    if _tracked:
        dead_exempt = sorted(p for p in vst.LEAK_SCAN_SKIP
                             if p not in _tracked
                             and os.path.exists(os.path.join(ROOT, p)))
        rep.check(not dead_exempt,
                  f"sızıntı taraması muafiyetlerinin hepsi canlı ({len(vst.LEAK_SCAN_SKIP)})",
                  f"ÖLÜ MUAFİYET: {dead_exempt} — dosya diskte var ama takip "
                  "edilmiyor; muafiyet hiçbir zaman devreye girmiyor (K14/D28)")

    # --- ÖZ-TESTİN KENDİ CANLILIK TESTİ (Faz 1'de bulundu) ---
    # Bu, bu dosyadaki EN ÖNEMLİ denetimdir, çünkü kendisini denetler.
    #
    # `mb.load_book()` eskiden diskteki manuscript'i enjekte edilen kurgudan
    # ÖNCE okuyordu. Faz 0'da disk boştu ve kimse fark etmedi. Faz 1'in ilk
    # pilot hikâyesi diske yazıldığı an bütün öz-test sistemi ÖLDÜ: kusurlu
    # kurgu enjekte ediliyor, yok sayılıyor, her kapı gerçek TEMİZ metni
    # görüp yeşil yanıyordu. Yani kapıların kendi testi, koruduğu şey var
    # olduğu anda çalışmayı bırakıyordu — sessizce.
    #
    # Bu denetim onu bir daha sessiz bırakmaz.
    _probe = os.path.join(tmp, "precedence-probe.json")
    with open(_probe, "w", encoding="utf-8") as fh:
        json.dump({"meta": {"probe": True},
                   "stories": {"probe-000": {"title": "Probe", "text": "x", "culturalNote": "y"}}},
                  fh, ensure_ascii=False)
    _saved = os.environ.get("MYTHBOOK_BOOK_JSON")
    os.environ["MYTHBOOK_BOOK_JSON"] = _probe
    try:
        _got = mb.book_stories(mb.load_book())
    finally:
        if _saved is None:
            os.environ.pop("MYTHBOOK_BOOK_JSON", None)
        else:
            os.environ["MYTHBOOK_BOOK_JSON"] = _saved
    _disk = os.path.exists(mb.BOOK_JSON) or os.path.exists(mb.BOOK_EDITED_JSON)
    rep.check(set(_got) == {"probe-000"},
              "enjekte edilen kurgu diskteki manuscript'i EZİYOR"
              + (" (diskte gerçek manuscript VAR — test anlamlı)" if _disk
                 else " (diskte manuscript yok — test zayıf ama geçerli)"),
              "load_book() enjeksiyonu yok saydı: bütün öz-test sistemi ÖLÜ. "
              "Kapılar kusurlu kurgu yerine gerçek metni görür ve yeşil yanar.")

    # --- D32 REGRESYONU: özel ad tespiti DOĞRU METNİ REDDETMEMELİ ---
    # Faz 1 pilot hikâyesi qa_crossref'i kırmızı yaktı ve suç metinde değil
    # CETVELDEYDİ: kapı kendi ad tespitini yapıyor, cümle başını elemek için
    # `(?<![.!?…]\s)` koruması kullanıyordu. O korumanın kör noktası PARAGRAF
    # BAŞIDIR — "\n\n"den sonra gelen sözcüğün önünde ".!?…"+boşluk yoktur.
    # Sonuç: “The”, “Twice”, “They” özel ad sayıldı ve telaffuz rehberinde
    # aranmaya başlandı. Kapı, DOĞRU YAZILMIŞ bir hikâyeyi reddediyordu.
    #
    # Bu test iki yönlüdür ve ikisi de gereklidir: tespit sıradan sözcüğü
    # ALMAMALI ama gerçek adı KAÇIRMAMALI. Yalnızca birincisini sınamak,
    # "hiçbir şeyi ad saymayan" bir düzeltmeyi de geçirirdi.
    d32 = ("The bear waited in the dark.\n\n"
           "Twice she walked to the entrance.\n\n"
           "They called him Dangun, and Hwanung heard her.")
    found = mb.proper_names(d32)
    rep.check(not ({"The", "Twice", "They"} & found),
              "özel ad tespiti paragraf başındaki sıradan sözcüğü AD SAYMIYOR (D32)",
              f"“The/Twice/They” ad sanıldı: {sorted(found)} — kapı doğru metni "
              "reddediyor (Bestiarium D32)")
    rep.check({"Dangun", "Hwanung"} <= found,
              "özel ad tespiti gerçek adı KAÇIRMIYOR",
              f"gerçek ad bulunamadı: {sorted(found)} — düzeltme kapıyı KÖRLEŞTİRMİŞ")

    # qa_crossref bu tespiti KENDİSİ yapmamalı: iki ayrı ad tespiti tutmak
    # ikisinin ayrışmasını garanti eder ve ayrışan kapı ölü kuraldır.
    import qa_crossref
    _src = open(os.path.join(ROOT, "04_BUILD", "qa_crossref.py"), encoding="utf-8").read()
    rep.check("mb.proper_names(" in _src,
              "qa_crossref ad tespitini mythbook.proper_names()'e devrediyor",
              "qa_crossref kendi ad tespitini yapıyor — tek doğruluk kaynağı bozuldu")

    # --- qa_diacritics D35 muafiyeti ---
    import qa_diacritics
    index = mb.load_stories()
    canonical, real_plain = qa_diacritics.collect_names(index)
    rep.check(True, f"qa_diacritics: {len(canonical)} diakritikli ad, "
                    f"{len(real_plain)} D35 muafiyeti kayıtlı")

    # --- kimlik listeleri gerçek kayıtlara denk geliyor mu (Ö2) ---
    import validate_spec as vs
    cultures = mb.load_cultures()
    macro_ids = {m["id"] for m in cultures.get("macroRegions", [])}
    dead_macro = [c["id"] for c in cultures.get("cultures", [])
                  if c.get("macroRegion") not in macro_ids]
    rep.check(not dead_macro, "kültür → makro bölge referansları canlı",
              f"ölü referans: {dead_macro} (Bestiarium Ö2)")

    policy_keys = set(vs.POLICY_LEVEL)
    rep.check(policy_keys == vs.CONTENT_FLAGS,
              "AGE_POLICY seviye tablosu içerik işaretleriyle birebir",
              f"ayrışma: {policy_keys ^ vs.CONTENT_FLAGS} — bir kategori "
              "seviyesiz kalırsa o kategori HİÇ DENETLENMEZ")

    # --- denetlenen rapor dizini var mı (Ö3) ---
    gi = open(os.path.join(ROOT, ".gitignore"), encoding="utf-8").read()
    rep.check("!06_REPORTS/tracked/" in gi and os.path.isdir(mb.REPORTS_TRACKED),
              "denetlenen rapor dizini depoda (karar K18)",
              "Bestiarium Ö3: denetlenecek bir rapor depoda durmuyorsa "
              "o denetim CI'da HER KOŞUDA sessizce boş geçer")

    # --- yasak kalıpların hepsi gerçekten derlenebiliyor mu ---
    import re
    bad = []
    for name, pattern, _ in mb.FORBIDDEN_PATTERNS:
        try:
            re.compile(pattern)
        except re.error as exc:
            bad.append(f"{name}: {exc}")
    rep.check(not bad, f"{len(mb.FORBIDDEN_PATTERNS)} yasak kalıp derleniyor", str(bad))


# =============================================================================
# ⑤ MANUSCRIPT SIZINTISI KAPISI GERÇEKTEN ISIRIYOR MU
# =============================================================================

def test_leak_gate(tmp: str, rep: Report) -> None:
    mb.banner("⑤ manuscript sızıntısı kapısı ısırıyor mu")

    import validate_structure as vst

    book = fx.build(None)
    opening = mb.sentences(book["stories"]["fx-000"]["text"])[0]
    rep.check(len(opening) >= 40, "kurgu açılış cümlesi tarama için yeterince uzun")

    # Kasıtlı sızıntı: takip edilen bir dosyaya hikâye açılışını koy
    leak_path = os.path.join(ROOT, "06_REPORTS", "tracked", "_leaktest.md")
    os.makedirs(os.path.dirname(leak_path), exist_ok=True)
    book_path = write_book(book, tmp, "leak.json")
    os.environ["MYTHBOOK_BOOK_JSON"] = book_path
    try:
        with open(leak_path, "w", encoding="utf-8") as fh:
            fh.write("# sızıntı testi\n\n" + opening + "\n")

        tracked = vst.tracked_files()
        if tracked is None:
            rep.check(True, "sızıntı testi atlandı", "git deposu yok")
            return
        # git henüz bu dosyayı takip etmiyor olabilir; testi yalnızca
        # takip edildiğinde anlamlıdır.
        rel = os.path.relpath(leak_path, ROOT)
        subprocess.run(["git", "-C", ROOT, "add", "-f", rel],
                       capture_output=True, timeout=30)

        r = mb.Result("leak-probe", verbose=False)
        vst.check_manuscript_leak(r)
        rep.check(bool(r.failures), "kasıtlı sızıntı YAKALANDI",
                  "sızıntı kapısı hikâye metnini görmedi — public depo "
                  "politikası mekanizmaya bağlı DEĞİL")
    finally:
        os.environ.pop("MYTHBOOK_BOOK_JSON", None)
        subprocess.run(["git", "-C", ROOT, "rm", "--cached", "-q",
                        os.path.relpath(leak_path, ROOT)],
                       capture_output=True, timeout=30)
        if os.path.exists(leak_path):
            os.remove(leak_path)

    # temizlikten sonra kapı yeşile dönmeli
    r = mb.Result("leak-clear", verbose=False)
    vst.check_manuscript_leak(r)
    rep.check(not r.failures, "temizlikten sonra sızıntı kapısı yeşil",
              f"{[f['message'] for f in r.failures]}")


# =============================================================================
# GİRİŞ NOKTASI
# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description="Kapıların kendi testi")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  KAPILARIN KENDİ TESTİ")
    print("═" * 72)
    print("  Metin yokken yeşil kalan bir hat, kusur geldiğinde de yeşil")
    print("  kalabilir. Bu test o riski kapatır.")

    rep = Report(args.verbose)

    with tempfile.TemporaryDirectory() as tmp:
        test_clean(tmp, rep)
        test_defects(tmp, rep)
        test_gate_levels(rep)
        test_exemptions_live(tmp, rep)
        test_leak_gate(tmp, rep)

    print()
    print("═" * 72)
    if rep.failed:
        print(f"  ⛔ {len(rep.failed)} KAPI TESTİ BAŞARISIZ · {rep.passed} geçti")
        for f in rep.failed:
            print(f"     · {f}")
        print("═" * 72)
        print()
        print("  Kör bir kapı, olmayan bir kapıdan TEHLİKELİDİR: yeşil yanar.")
        return 1

    print(f"  ✅ {rep.passed} KAPI TESTİ GEÇTİ — kapılar gerçekten ısırıyor")
    print("═" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
