#!/usr/bin/env python3
"""
KAPAK SANATI BÜTÜNLÜĞÜ VE KÖKENİ
================================================================================
    python3 04_BUILD/cover_artwork.py            manifesto üret
    python3 04_BUILD/cover_artwork.py --check    doğrula (CI bunu koşar)

    07_ASSETS/raw/re-generated/*.png   YETKİLİ SANAT MASTERLARI · SALT OKUNUR
              ↓
    06_REPORTS/tracked/cover-artwork-manifest.json

--------------------------------------------------------------------------------
NEDEN BU DOSYA VAR
--------------------------------------------------------------------------------
Faz 7'ye kadar kapak hattı, ham sanata BASILMIŞ yanlış başlığı ve uydurulmuş
barkodu **kaldırmaya** çalışıyordu: harf maskesi, difüzyon, çok ölçekli gök
modeli. Teknik olarak çalışıyordu ama **sanata zarar veriyordu** — bir
üreticinin yaptığı resmi başka bir algoritmayla onarmak, her koşuda biraz
daha bozar.

Kurucu doğru kararı verdi ve **bütün kapak sanatını metinsiz yeniden
ürettirdi**. Yeni masterlar `07_ASSETS/raw/re-generated/` altındadır.

Bundan sonra kural şudur:

    SANAT KATMANINA HİÇBİR ŞEY YAZILMAZ VE SANAT KATMANINDAN HİÇBİR ŞEY
    SİLİNMEZ. Tipografi ayrı bir katmandır ve CLI ile basılır.

--------------------------------------------------------------------------------
BU BETİK NEYİ GARANTİ EDER — VE NEYİ ETMEZ
--------------------------------------------------------------------------------
✅ GARANTİ EDER (makine kanıtı):

  ① MASTERLAR DEĞİŞMEDİ. Her dosyanın sha256'sı manifestoya yazılır ve her
     koşuda karşılaştırılır. Bir master'a tek piksel yazılsa kapı kırmızı yanar.

  ② KÖKEN DOĞRU. Kapak hattı sanatı YALNIZCA `re-generated/` altından okur.
     Eski (metinli) sanata dönüş sessizce olamaz.

  ③ YIKICI HAT GERİ GELEMEZ. `covers.py` içinde metin silme/onarma
     fonksiyonlarının ADI BİLE bulunmamalıdır. Biri onları geri eklerse
     kapı kırmızı yanar.

❌ GARANTİ ETMEZ:

  Bir görselde tipografi OLUP OLMADIĞINI makine ile kanıtlamaz.

  Denendi ve **dürüstçe başarısız oldu**: "yerel zeminden koyu + zemin açık"
  maskesinin satır bandı imzası, yer gerçeğiyle sınandığında metinli ve
  metinsiz sanatı AYIRAMADI — temiz `back-panel` (bant %6,0), metinli
  `thumbnail-test`ten (%1,6) daha yüksek skor aldı. Dağ silueti, orman ve
  bulut kenarı da "açık zemin üstünde koyu leke"dir.

  Ayırt edemeyen bir kapı, ÖLÜ KURALDIR ve yeşil yanarak yalan söyler
  (bkz. LESSONS_FROM_CODEX_BESTIARIUM § D). Bu yüzden buraya
  KONULMADI.

  Metinsizlik kararı **gözle verilmiştir** ve kanıtı rapordadır:
  `06_REPORTS/COVER_ARTWORK_REPLACEMENT_REPORT.md` § 3. Her master
  büyütülerek incelenmiş ve sonucu tek tek kaydedilmiştir.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb

ART_DIR = os.path.join(mb.ASSETS, "raw", "re-generated")
MANIFEST = os.path.join(mb.REPORTS_TRACKED, "cover-artwork-manifest.json")

# `covers.py` içinde ADI BİLE geçmemesi gereken yıkıcı işlemler.
# Bunlar Faz 7'de kaldırıldı; geri gelirlerse sanat yeniden bozulur.
FORBIDDEN_IN_COVERS = [
    "repair_generated_title",
    "clear_generated_barcode",
    "_letter_mask",
    "_trim_to_text_rows",
    "_diffuse",
]

# Gözle doğrulanmış metinsizlik kaydı. Bir master eklenirse buraya da
# eklenmelidir — aksi hâlde kapı "incelenmemiş sanat" der.
VISUAL_VERDICT = {
    "cover-paperback-wrap.png":        "clean",
    "cover-hardcover-wrap.png":        "clean",
    "cover-paperback-front.png":       "clean",
    "cover-back-panel.png":            "clean",
    "cover-front-variant-figures.png": "clean",
    "cover-front-variant-object.png":  "clean",
    # Aynı kompozisyonun METİNSİZ hâli — kurucu, aşağıdaki metinli dosyayı
    # görüp temizini üretti. Test varlığı olarak kullanılacak olan budur.
    "cover-thumbnail.png":             "clean",
    # ⚠ Bu dosyada ÜRETİLMİŞ TİPOGRAFİ VARDIR: "The Great Book of / WORLD
    # MYTHS / 22 Cultures" ve "8–12 YEARS" rozeti resme basılıdır.
    # Talimat § 3 gereği metin KALDIRILMADI ve kaldırılmayacaktır.
    # Üretim varlığı DEĞİLDİR: coverspec.py bu kaydı "ÜRETİM VARLIĞI
    # DEĞİL, TESTTİR" diye işaretler ve covers.py onu hiç okumaz.
    # YERİNE GEÇEN: cover-thumbnail.png (kurucu tarafından temiz üretildi).
    "cover-thumbnail-test.png":        "ARTWORK_REQUIRES_REGENERATION",
}

# Metinli olduğu tespit edilen bir master'ın YERİNE GEÇEN temiz dosya.
# Yerine geçen varsa kapı bunu bilir ve "yeniden üretim bekliyor" demez.
SUPERSEDED_BY = {
    "cover-thumbnail-test.png": "cover-thumbnail.png",
}

# Üretim hattının GERÇEKTEN okuduğu masterlar. Bunların metinli olması
# yayını bloklar; diğerleri yedek/varyanttır.
PRODUCTION_MASTERS = ["cover-paperback-wrap.png", "cover-hardcover-wrap.png"]


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def scan() -> dict:
    if not os.path.isdir(ART_DIR):
        return {}
    out = {}
    for name in sorted(os.listdir(ART_DIR)):
        if not name.lower().endswith(".png"):
            continue
        p = os.path.join(ART_DIR, name)
        entry = {"sha256": sha256(p), "bytes": os.path.getsize(p)}
        try:
            from PIL import Image
            with Image.open(p) as im:
                entry["px"] = list(im.size)
                entry["mode"] = im.mode
        except Exception:                                        # noqa: BLE001
            pass
        out[name] = entry
    return out


def covers_source_ok() -> tuple[bool, str]:
    """`covers.py` sanatı re-generated altından mı okuyor?"""
    p = os.path.join(mb.BUILD, "covers.py")
    with open(p, encoding="utf-8") as fh:
        src = fh.read()
    if 'ART_DIR' not in src:
        return False, "covers.py ART_DIR tanımlamıyor"
    if '"re-generated"' not in src and "'re-generated'" not in src:
        return False, "covers.py 're-generated' dizinini okumuyor"
    return True, ""


def forbidden_hits() -> list[str]:
    p = os.path.join(mb.BUILD, "covers.py")
    with open(p, encoding="utf-8") as fh:
        src = fh.read()
    return [n for n in FORBIDDEN_IN_COVERS if n in src]


def main() -> int:
    ap = argparse.ArgumentParser(description="Kapak sanatı bütünlüğü")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  KAPAK SANATI · BÜTÜNLÜK VE KÖKEN")
    print("═" * 72)

    r = mb.Result("cover_artwork", verbose=args.verbose)
    now = scan()

    # ⚠ HAM SANAT DEPODA DURMAZ (.gitignore § 07_ASSETS/raw/*) — büyük ikili
    # dosyalar public depoya girmez. Bu yüzden CI'da dizin YOKTUR ve bu bir
    # KUSUR DEĞİLDİR: depoya giren şey sanatın KENDİSİ değil, sha256
    # MANİFESTOSUDUR (06_REPORTS/tracked/, karar K18).
    #
    # Kapı bu durumda "uygulanamaz" der ve YEŞİL kalır — ama köken ve yasak
    # fonksiyon denetimleri KAYNAK KODA baktığı için CI'da da KOŞAR.
    # Yani CI, silme hattının geri gelmediğini yine de kanıtlar.
    have_art = bool(now)
    if not have_art:
        r.ok("ham sanat yerelde yok — bütünlük taraması uygulanamaz",
             f"{os.path.relpath(ART_DIR, mb.ROOT)} depoda durmaz; "
             "manifesto denetlenir, ikili dosyalar CI'da bulunmaz")

    if have_art:
        print(f"\n  master        : {len(now)}")
        total = sum(v["bytes"] for v in now.values())
        print(f"  toplam boyut  : {total/1e6:.1f} MB")

    # --- ② KÖKEN ---------------------------------------------------------
    ok, why = covers_source_ok()
    r.add(ok, "kapak hattı sanatı YETKİLİ dizinden okuyor",
          f"KÖKEN YANLIŞ: {why} — eski metinli sanata dönüş sessizce olamaz")

    # --- ③ YIKICI HAT GERİ GELDİ Mİ -------------------------------------
    hits = forbidden_hits()
    r.add(not hits,
          "yıkıcı metin-silme hattı covers.py'de YOK",
          f"YIKICI HAT GERİ GELMİŞ: {hits} — yeni sanat metinsizdir, "
          "silinecek bir şey yoktur ve silme sanata zarar verir")

    # --- gözle doğrulama kaydı -------------------------------------------
    unreviewed = [n for n in now if n not in VISUAL_VERDICT] if have_art else []
    r.add(not unreviewed,
          f"her master gözle incelenmiş ({len(now)})",
          f"İNCELENMEMİŞ SANAT: {unreviewed} — VISUAL_VERDICT'e ekleyin "
          "(makine metinsizliği kanıtlayamaz, bkz. modül başlığı)")

    flagged = ([n for n, v in VISUAL_VERDICT.items()
                if v != "clean" and n in now] if have_art else [])
    prod_flagged = [n for n in flagged if n in PRODUCTION_MASTERS]
    r.add(not prod_flagged,
          "üretim masterlarının hepsi metinsiz",
          f"ÜRETİM MASTER'INDA METİN VAR: {prod_flagged} — talimat § 3: "
          "metin KALDIRILMAZ, sanat YENİDEN ÜRETİLİR")
    for n in flagged:
        sup = SUPERSEDED_BY.get(n)
        if sup and sup in now:
            r.warn(False, "",
                   f"{n}: {VISUAL_VERDICT[n]} — metin kaldırılmadı ve "
                   f"kaldırılmayacak; YERİNE GEÇEN temiz dosya var: {sup}")
        else:
            r.warn(False, "",
                   f"{n}: {VISUAL_VERDICT[n]} — üretim varlığı değil "
                   "(coverspec: test kaydı); metin kaldırılmadı ve "
                   "kaldırılmayacak, YERİNE GEÇEN TEMİZ DOSYA YOK")
    payload_flagged = {n: {"verdict": VISUAL_VERDICT[n],
                           "supersededBy": SUPERSEDED_BY.get(n)}
                       for n in flagged}

    # --- ① MASTERLAR DEĞİŞTİ Mİ -----------------------------------------
    payload = {"$comment": [
        "KAPAK SANATI MANİFESTOSU — 07_ASSETS/raw/re-generated SALT OKUNUR.",
        "Bu dosya masterların DEĞİŞMEDİĞİNİ kanıtlar. Bir master'a tek",
        "piksel yazılsa sha256 değişir ve kapı kırmızı yanar.",
        "Üretici: 04_BUILD/cover_artwork.py",
    ], "gate": mb.read_gate(),
        "artDir": os.path.relpath(ART_DIR, mb.ROOT),
        "productionMasters": PRODUCTION_MASTERS,
        "visualVerdict": VISUAL_VERDICT,
        "flagged": payload_flagged,
        "supersededBy": SUPERSEDED_BY,
        "masters": now}

    if args.check and not have_art:
        r.ok("sha256 karşılaştırması uygulanamaz", "ham sanat yerelde yok")
        return r.finish(args.json)

    if args.check:
        if not os.path.exists(MANIFEST):
            r.fail("manifesto yok", "`cover_artwork.py` çalıştırın")
            return r.finish(args.json)
        with open(MANIFEST, encoding="utf-8") as fh:
            old = json.load(fh).get("masters", {})
        changed = [n for n in now
                   if n in old and old[n]["sha256"] != now[n]["sha256"]]
        removed = [n for n in old if n not in now]
        added = [n for n in now if n not in old]
        r.add(not changed,
              f"master sanat DEĞİŞMEDİ ({len(now)} dosya · sha256)",
              f"MASTER SANAT DEĞİŞTİRİLMİŞ: {changed} — "
              "07_ASSETS/raw/re-generated SALT OKUNURDUR (§ 16)")
        r.add(not removed, "hiçbir master silinmedi",
              f"MASTER SİLİNMİŞ: {removed}")
        r.warn(not added, "yeni master yok",
               f"yeni master eklendi: {added} — manifestoyu tazeleyin")
        if args.verbose:
            for n, v in sorted(now.items()):
                print(f"    {n:34} {v['sha256'][:16]}… "
                      f"{v.get('px','?')} {v['bytes']/1e6:.1f} MB")
        return r.finish(args.json)

    if not have_art:
        r.warn(False, "", "ham sanat yok — manifesto ÜRETİLMEDİ "
                          "(boş manifesto yazmak kaydı siler)")
        return r.finish(args.json)

    os.makedirs(mb.REPORTS_TRACKED, exist_ok=True)
    with open(MANIFEST, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"\n  ✎ {os.path.relpath(MANIFEST, mb.ROOT)}")
    return r.finish(args.json)


if __name__ == "__main__":
    sys.exit(main())
