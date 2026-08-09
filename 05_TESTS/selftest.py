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

    # --- KÜNYELİ AD REGRESYONU (Faz 2) — kapı kendi üslup kuralını cezalandırmamalı ---
    # `mb.proper_names()` cümlenin ilk sözcüğünü atlar (doğru bir koruma).
    # Bedeli: cümle başında duran GERÇEK bir ad kaçar ve zor bir sıradan
    # sözcük sayılır. CHILDREN_WRITING_STYLE § 2.1 ise adların sık ve zamir
    # yerine kullanılmasını EMREDER. Düzeltilmeden önce okunabilirlik kapısı,
    # kitabın zorunlu tuttuğu üslubu cezalandırıyordu.
    import qa_readability as _qr
    _txt = ("Demeter walked to the well. Demeter sat down there. "
            "Demeter waited a long time. The barley did not grow at all.")
    _without = _qr.analyse(_txt)
    _with = _qr.analyse(_txt, {"Demeter"})
    rep.check(_without["hard_word_share"] > _with["hard_word_share"],
              "künyelenmiş ad okunabilirlik hesabından çıkarılıyor (cümle başında bile)",
              "künyeli ad hâlâ 'zor sıradan sözcük' sayılıyor — kapı, üslup kuralının "
              "emrettiği ad kullanımını cezalandırır (D32 sınıfı)")
    rep.check(_qr.analyse(_txt, {"Barleycorn"})["hard_word_share"]
              == _without["hard_word_share"],
              "künyesiz ad muaf DEĞİL (kapı körleşmiyor)",
              "künyelenmemiş bir ad de muaf tutuluyor — muafiyet çok geniş")

    # --- İYELİK REGRESYONU (Faz 2) — künyeli adın iyeliği EKSİK SAYILMAMALI ---
    # Künye adı kesme işaretinden bölünür ("Arachne" → {"Arachne"}), ama
    # metin belirteci bölünmez ("Arachne’s"). Düzeltilmezse doğru yazılmış
    # bir iyelik telaffuz rehberinde eksik sanılır. Pilot hikâyede özel ad
    # iyelik hâlinde hiç geçmediği için Faz 1'de görünmedi.
    rep.check("[’']s$" in _src or '[’\']s$' in _src,
              "qa_crossref iyelik ekini soyuyor (künyeli adın iyeliği eksik sayılmaz)",
              "iyelik eki soyulmuyor — “Arachne’s” künyeli olmasına rağmen EKSİK sanılır (D32 sınıfı)")

    # --- SÖZCÜK SINIFI REGRESYONU (Faz 3) — cetvel kültürel kapsamı kesmemeli ---
    # `mb._WORD` birleşen işaretleri (U+0300–U+036F) ve ʻokinayı (U+02BB)
    # sözcük karakteri saymıyordu. Sonuç: üslup belgesinin ÖRNEK OLARAK
    # verdiği adlar parçalanıyordu —
    #     “Ọ̀ṣun”     → ['Ọ', 'ṣun']    (ad ikiye bölünüyor, sözcük sayısı şişiyor)
    #     “Hiʻiaka”   → ['Hi', 'iaka']  (ʻokina Hawaiʻicede HARFTİR)
    # ve `qa_crossref` doğru yazılmış adı “telaffuz rehberinde eksik” sanıyordu.
    #
    # Test iki yönlüdür: ad BÜTÜN kalmalı ama tokenizer sıradan noktalamayı
    # yutmamalı — aksi hâlde "her şeyi tek sözcük sayan" bir düzeltme de geçerdi.
    for _name in ("Ọ̀ṣun", "Ilé-Ifẹ̀", "Hiʻiaka", "Nāmakaokahaʻi", "Chang’e", "Māui"):
        rep.check(mb.words(_name) == [_name],
                  f"sözcük sınıfı adı bütün tutuyor: “{_name}”",
                  f"parçalandı → {mb.words(_name)} — cetvel, kitabın KÜLTÜREL "
                  "KAPSAMINI cezalandırıyor (Bestiarium D32 sınıfı)")
    rep.check(mb.words("bir, iki; üç.") == ["bir", "iki", "üç"],
              "sözcük sınıfı sıradan noktalamayı yutmuyor",
              "tokenizer fazla geniş — noktalama sözcüğe karışıyor, "
              "bütün sözcük sayıları ve bantlar bozulur")

    # --- KÜNYE TOKENIZER REGRESYONU (Faz 3) — ortografik kesme taşıyan adlar ---
    # `qa_crossref` künye adını kesme işaretinden bölüyordu, metin tarafı
    # bölmüyordu: iki ayrı tokenizer, garantili ayrışma. Kesmeyi ORTOGRAFİK
    # olarak kullanan diller (Maya dilleri, pinyin, Hepburn) toptan
    # cezalandırılıyordu.
    for _n in ("Chang’e", "K’iche’", "Q’ukumatz", "Man’yōshū"):
        rep.check(_n in mb.declared_tokens({_n}),
                  f"künye tokenizer’ı ortografik kesmeyi koruyor: “{_n}”",
                  f"künye {sorted(mb.declared_tokens({_n}))} üretti; metin belirteci "
                  f"“{_n}” hiçbirine eşleşmez → DOĞRU YAZILMIŞ ad eksik sanılır")
    rep.check("Korkut" in mb.declared_tokens({"Dede Korkut"}),
              "künye tokenizer’ı çok sözcüklü adı hâlâ parçalıyor",
              "çok sözcüklü ad parçalanmıyor — “Korkut” tek başına geçtiğinde eksik sanılır")
    rep.check("Nowhere" not in mb.declared_tokens({"Dede Korkut"}),
              "künye tokenizer’ı künyesiz adı üretmiyor (kapı körleşmiyor)",
              "künye kümesi künyelenmemiş ad taşıyor — muafiyet çok geniş")

    # --- OKURA GİDEN TİPOGRAFİ KAPISI ISIRIYOR MU (Faz 3) ---
    # Başlık, telaffuz adı ve “kim kimdir” rolü BASILI SAYFAYA gider ama
    # manuscript'te değil DİZİNDE durur; `qa_voice` yalnızca manuscript'i
    # tarar. Bu sınıf Faz 3'e kadar HİÇBİR kapının kapsamında değildi ve
    # tarama 33 kusur buldu — biri kendi içinde tutarsızdı (“K’iche' ”).
    import qa_diacritics as _qd
    _defective = {"stories": [{"id": "fx-typo", "title": "The Blacksmith's Apron",
                               "pronunciationEntries": [], "characters": []}]}
    _clean = {"stories": [{"id": "fx-typo", "title": "The Blacksmith’s Apron",
                           "pronunciationEntries": [], "characters": []}]}
    rep.check(bool(_qd.straight_typography_hits(_defective, {"cultures": []})),
              "okura giden tipografi kapısı düz kesmeyi YAKALIYOR",
              "kapı düz kesmeyi görmedi — basılı başlıkta ' ile ’ karışır")
    rep.check(not _qd.straight_typography_hits(_clean, {"cultures": []}),
              "okura giden tipografi kapısı doğru tipografiyi geçiriyor",
              "kapı yanlış pozitif üretiyor — doğru metni reddeden cetvel")
    _internal = {"stories": [{"id": "fx-typo", "title": "Clean",
                              "pronunciationEntries": [{"name": "Ra", "pronunciation": "RAH",
                                                        "pronunciationSource": "Faulkner's dictionary"}],
                              "characters": []}]}
    rep.check(not _qd.straight_typography_hits(_internal, {"cultures": []}),
              "kaynak künyesi tipografi taramasının DIŞINDA",
              "künye taranıyor — kaynağın kendi yazımını düzeltmek ALINTIYI BOZAR")

    # --- İKİ EBEVEYN OKUMASI KAPISI (Faz 4) — ÜÇ FAZ BOYUNCA ÖLÜYDÜ ---
    # Yol haritası § 16 Faz 4 CI kapısı olarak PARENT_READINGS.md'yi adıyla
    # sayıyordu ve DECISIONS § A8 "validate_structure Faz 5'te arar" diyordu.
    # İkisi de yanlıştı: kod bu dosyayı HİÇBİR kapıda aramıyordu. Yol
    # haritasının R2 azaltmasının insan yarısı mekanizmasızdı.
    import validate_structure as _vs
    rep.check(not _vs.parent_readings_signed("okuma yapıldı, herkes memnun"),
              "ebeveyn okuması kapısı İMZASIZ metni saymıyor",
              "imzasız düzyazı 'okuma' sayıldı — kayıt uydurulabilir hâle gelir")
    _one = "<!-- PARENT-READING:SIGNED A. Reader -->"
    _two = _one + "\n<!-- PARENT-READING:SIGNED B. Reader -->"
    rep.check(len(_vs.parent_readings_signed(_one)) == 1,
              "ebeveyn okuması kapısı tek imzayı tek sayıyor",
              "imza sayımı yanlış")
    rep.check(len(_vs.parent_readings_signed(_two)) == 2,
              "ebeveyn okuması kapısı iki imzayı görüyor",
              "iki imzalı kayıt tanınmıyor — kapı hiçbir zaman geçilemez olur")
    # ŞABLONUN KENDİSİ KAPIYI BESLEMEMELİ: imza biçimi dosyada örnekle
    # anlatılıyor ve o örnek bir kod çitinin içinde. Sökülmezse şablonu
    # kopyalayan biri hiç okuma yapmadan iki imza toplardı.
    _fenced = "```\n" + _two + "\n```\n"
    rep.check(not _vs.parent_readings_signed(_fenced),
              "ebeveyn okuması kapısı KOD BLOĞUNDAKİ örneği saymıyor",
              "şablonun kendi örneği imza sayıldı — dosyayı kopyalamak kapıyı "
              "geçmeye yeterdi ve R2'nin insan kontrolü anlamsızlaşırdı")
    # Gerçek dosya: şu anda SIFIR imza olmalı (kurucu bağımlılığı)
    _real = os.path.join(ROOT, _vs.PARENT_READINGS)
    if os.path.exists(_real):
        with open(_real, encoding="utf-8") as _fh:
            _n = len(_vs.parent_readings_signed(_fh.read()))
        rep.check(_n == 0,
                  f"PARENT_READINGS.md gerçek imza taşımıyor ({_n}) — kurucu bağımlılığı",
                  f"{_n} imza görünüyor; UYDURULMUŞ imza olup olmadığı ELLE doğrulanmalı")

    # --- KÜLTÜR KARTI KAPISI ISIRIYOR MU (Faz 3) ---
    # Kart üç cümle taşır ve ÜÇÜNCÜSÜ bir kapıdır: yaşayan bir gelenek için
    # o cümle şimdiki zamanda olmak zorundadır (AGE_POLICY § 2.15). Ayrıca
    # 22 kart 22 ayrı cümle kurmak zorundadır (K13 sınıfı).
    import validate_spec as vs

    def _card(**kw):
        base = dict(language="X",
                    whoTells="Named narrators carry this account and have done so for a very long time indeed, without writing much of it down.",
                    where="It belongs to a particular valley with a slow river running along the bottom and terraces cut into both sides of it.",
                    today="People keep the practice now and teach it to their children every single year, in the same language it started in.")
        base.update(kw); return base

    def _probe(cultures):
        rr = mb.Result("card-probe", verbose=False)
        vs.check_culture_cards(cultures, "phase3", rr)
        return rr.failures

    _clean = [dict(id="a", status="locked", livingTradition=True, cardText=_card()),
              dict(id="b", status="locked", livingTradition=True, cardText=_card(
                  whoTells="Two compilations hold it, and the older one disagrees with the newer about the order of events in several places.",
                  where="Islands strung along a cold coast, where the weather decides what anybody does that week and nobody argues with it.",
                  today="Speakers of the language broadcast it, print it, and put it on the school syllabus for children of about nine."))]
    rep.check(not _probe(_clean), "kültür kartı kapısı temiz kartı geçiriyor",
              f"yanlış pozitif: {[f['message'][:90] for f in _probe(_clean)]}")

    _past = [_clean[0], dict(id="b", status="locked", livingTradition=True,
                             cardText=_card(today="People used to believe this a long time ago, before the missionaries came up the valley and the singing stopped."))]
    rep.check(_probe(_past), "kültür kartı kapısı GEÇMİŞ ZAMAN tuzağını yakalıyor",
              "yaşayan gelenek için 'used to believe' geçti — AGE_POLICY § 2.15: "
              "geçmiş zaman bir kültürü MÜZEYE KOYAR")

    _templated = [_clean[0], dict(id="b", status="locked", livingTradition=True, cardText=_card())]
    rep.check(_probe(_templated), "kültür kartı kapısı KALIPLAŞMAYI yakalıyor",
              "iki kart aynı cümleyi paylaştı ve kapı görmedi — 22 kart 22 ayrı "
              "cümle kurmalı, yoksa okur kartı ATLAMAYI ÖĞRENİR (R6 · K13)")

    _missing = [_clean[0], dict(id="b", status="locked", livingTradition=True, cardText=None)]
    rep.check(_probe(_missing), "kültür kartı kapısı EKSİK kartı yakalıyor",
              "kart metni olmayan kilitli kültür geçti")

    _dead = [dict(id="a", status="locked", livingTradition=False, cardText=_card(
                 today="Nobody has made an offering to these gods for fifteen hundred years, and the last temple closed before that."))]
    rep.check(not _probe(_dead), "geçmiş zaman kuralı YAŞAMAYAN gelenek için uygulanmıyor",
              "yaşamayan bir gelenek şimdiki zamana zorlanıyor — kapı yanlış "
              "kültüre karşı çalışıyor")

    # --- EDİLGEN ÇATI REGRESYONU (Faz 3) — sıfat ortaç sayılmamalı ---
    # Desen yalnızca sözcük SONUNA bakıyordu: “was open”, “was red”, “was one”,
    # “was alone”, “was fifteen” hepsi edilgen sayılıyordu. 22 hikâye üzerinde
    # ölçüldüğünde eşleşmelerin altıda biri hiçbir fiilin ortacı değildi ve
    # ölçü %18 şişiyordu — kısa somut cümle yazan prozayı, yani üslup
    # belgesinin EMRETTİĞİ prozayı, daha edilgen gösteriyordu.
    for _phrase in ("The sky was open at one corner.", "It was red.",
                    "He was alone.", "She was fifteen.", "The door was gone."):
        rep.check(not _qr.passive_hits(_phrase),
                  f"edilgen taraması sıfatı ortaç saymıyor: “{_phrase}”",
                  f"“{_phrase}” edilgen sayıldı — hiçbiri bir fiilin ortacı değil "
                  "(D32 sınıfı: doğru metni cezalandıran cetvel)")
    for _phrase in ("The chain was carried outside.", "The boy was taken by the river.",
                    "The stones were melted together."):
        rep.check(_qr.passive_hits(_phrase),
                  f"edilgen taraması gerçek edilgeni KAÇIRMIYOR: “{_phrase}”",
                  "muafiyet listesi kapıyı körleştirmiş — gerçek edilgen çatı geçiyor")

    # --- YAŞ İNCELEMESİ SONUÇ KAYDI (Faz 3) — kuyruk kaydı kapıyı BESLEMEMELİ ---
    # Kapı eskiden kimliğin defterde bir yerde geçmesini arıyordu; "bekleyen
    # inceleme kuyruğu" tablosu bu şartı sağlıyordu. Yani hiç incelenmemiş bir
    # hikâye, yalnızca kuyrukta durduğu için geçebiliyordu.
    import qa_age as _qa
    _queue_only = ("## bekleyen kuyruk\n| 30 | `yoruba-obatala-land` | Yoruba |\n")
    _recorded = (_queue_only
                 + "\n<!-- AGE-REVIEW:RECORDED -->\n"
                 + "| 30 | `yoruba-obatala-land` | `cleared` | sonuç cümlesi |\n"
                 + "<!-- /AGE-REVIEW:RECORDED -->\n")
    rep.check("yoruba-obatala-land" not in _qa.recorded_reviews(_queue_only),
              "yaş incelemesi kapısı KUYRUK kaydını sonuç saymıyor",
              "kuyrukta durmak 'incelendi' sayılıyor — hiç incelenmemiş bir "
              "hikâye REVIEW kategorisiyle üretime geçebilir (AGE_POLICY § 1)")
    rep.check("yoruba-obatala-land" in _qa.recorded_reviews(_recorded),
              "yaş incelemesi kapısı SONUÇ kaydını görüyor",
              "sonuç bloğu okunmuyor — kapı hiçbir zaman geçilemez hâle gelir")

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
