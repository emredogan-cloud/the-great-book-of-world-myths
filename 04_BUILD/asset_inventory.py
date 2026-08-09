#!/usr/bin/env python3
"""
HAM VARLIK ENVANTERİ — 68 PNG'nin tek tek sayımı ve bütünlük denetimi
================================================================================
    python3 04_BUILD/asset_inventory.py            envanteri çıkar + rapor yaz
    python3 04_BUILD/asset_inventory.py --check    kayıtlı rapor bayat mı

HAM DİZİN SALT OKUNURDUR (karar K5 · talimat § 32). Bu betik ham dizine
YAZMAZ, YENİDEN ADLANDIRMAZ, OPTİMİZE ETMEZ. Yalnızca okur ve sayar.

--------------------------------------------------------------------------------
NEDEN AYRI BİR BETİK
--------------------------------------------------------------------------------
`images.py` KALİTEYİ ölçer (mürekkep, kontrast, çizgi). `convert_images.py`
FORMAT üretir. İkisi de "68 dosya gerçekten var mı, bozuk mu, yinelenmiş mi,
hangi hikâyeye/kültüre bağlanıyor" sorusunu sormaz — ve o soru sorulmadan
diğer ikisinin cevabı eksiktir: yanlış kültüre bağlanmış kusursuz bir vinyet,
bütün kalite kapılarından geçer.

Envanterin denetlediği şey EŞLEME ve BÜTÜNLÜKTÜR:
  · dosya sayısı        45 + 22 + 1 = 68
  · PNG bütünlüğü       imza · chunk · CRC · kesiklik
  · yinelenen           bayt-birebir (sha256) ve kimlik çakışması
  · yetim / eksik       şartnamedeki 68 kimliğe karşı
  · ad sapması          `story-43.png` → `story-043` (normalize edilir, GİZLENMEZ)
  · eşleme              story_index.imageId · culture_index.vignetteId
  · boş / neredeyse boş  mürekkep yoğunluğu tabanı
  · saydamlık           baskıda beyaz kâğıda düzleşir mi
  · üretici boyutu      şartname ile üreticinin verebildiği boyut çelişiyor mu

Bağımlılık: Pillow. Yoksa çıkış 2 (ATLANDI).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import zlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb
import imagespec as spec

try:
    from PIL import Image
except ImportError:
    print("ATLANDI: Pillow yok — `pip install -r 04_BUILD/requirements.txt`")
    sys.exit(2)

REPORT = os.path.join(mb.REPORTS_TRACKED, "asset-inventory.json")

# Boş sayfa tabanı. `images.py` tolerans bandından AYRIDIR: orada soru
# "baskıda iyi görünür mü", burada "bu dosya gerçekten bir çizim mi".
BLANK_INK_FLOOR = 0.005


# =============================================================================
# PNG BÜTÜNLÜĞÜ — Pillow'un açabildiği dosya sağlam demek DEĞİLDİR
# =============================================================================

def png_integrity(path: str) -> dict:
    """
    Pillow bozuk CRC'li bir PNG'yi sessizce açabilir. Chunk zinciri ve CRC
    elle yürünür: imza → (uzunluk, tür, veri, CRC)* → IEND.
    """
    out = {"signature": False, "crcOk": True, "truncated": False,
           "chunks": [], "iend": False}
    with open(path, "rb") as fh:
        data = fh.read()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        return out
    out["signature"] = True
    i = 8
    while i + 8 <= len(data):
        length = int.from_bytes(data[i:i + 4], "big")
        ctype = data[i + 4:i + 8].decode("latin-1", "replace")
        if i + 12 + length > len(data):
            out["truncated"] = True
            break
        payload = data[i + 8:i + 8 + length]
        stored = int.from_bytes(data[i + 8 + length:i + 12 + length], "big")
        if zlib.crc32(data[i + 4:i + 8] + payload) & 0xFFFFFFFF != stored:
            out["crcOk"] = False
        out["chunks"].append(ctype)
        i += 12 + length
        if ctype == "IEND":
            out["iend"] = True
            break
    if not out["iend"]:
        out["truncated"] = True
    return out


# =============================================================================
# EŞLEME — kimliğin SAHİBİ dizinlerdir, dosya adı değil
# =============================================================================

def build_mapping() -> dict[str, dict]:
    """
    68 kimliğin her birini projedeki kimliğine bağlar.

    ⚠ Dosya adına GÜVENİLMEZ (talimat § 8). Hikâye eşlemesi
    `story_index.json → imageId`, kültür eşlemesi
    `culture_index.json → vignetteId` alanından okunur; ikisi de
    `make_prompts.py`'nin prompt kütüphanesini ürettiği alanların AYNISIDIR,
    yani envanter ile prompt kütüphanesi aynı kaynaktan konuşur.
    """
    mapping: dict[str, dict] = {}

    stories = mb.load_stories().get("stories", [])
    for s in stories:
        iid = s.get("imageId")
        if not iid:
            continue                      # aday havuzu — kilitli değil
        mapping[iid] = {
            "kind": "story", "targetId": s["id"], "targetName": s.get("title"),
            "cultureId": s.get("cultureId"), "number": s.get("number"),
        }

    cultures = [c for c in mb.load_cultures().get("cultures", [])
                if c.get("status") == "locked"]
    cultures.sort(key=lambda c: c["name"])
    for i, c in enumerate(cultures, 1):
        vid = c.get("vignetteId") or f"culture-{i:03d}"
        mapping[vid] = {
            "kind": "culture", "targetId": c["id"], "targetName": c.get("name"),
            "cultureId": c["id"], "number": i,
        }

    mapping["map-001"] = {
        "kind": "map", "targetId": "world-map",
        "targetName": f"{mb.CULTURE_TARGET} kültürün dünya haritası",
        "cultureId": None, "number": 1,
    }
    return mapping


# =============================================================================
# ENVANTER
# =============================================================================

def inventory() -> dict:
    mapping = build_mapping()
    rows: list[dict] = []
    by_hash: dict[str, list[str]] = {}
    by_id: dict[str, list[str]] = {}

    names = sorted(n for n in os.listdir(spec.RAW_DIR)
                   if n.lower().endswith(f".{spec.RAW_FORMAT}")) \
        if os.path.isdir(spec.RAW_DIR) else []

    for name in names:
        path = os.path.join(spec.RAW_DIR, name)
        stem = name.rsplit(".", 1)[0]
        image_id, renamed = spec.canonical_id(stem)
        kind = image_id.split("-")[0]
        rec: dict = {
            "file": name,
            "id": image_id,
            "kind": kind if kind in spec.KINDS else None,
            "nameDeviation": renamed,
            "bytes": os.path.getsize(path),
        }
        with open(path, "rb") as fh:
            rec["sha256"] = hashlib.sha256(fh.read()).hexdigest()

        integ = png_integrity(path)
        rec["png"] = integ

        try:
            with Image.open(path) as im:
                im.load()
                w, h = im.size
                rec.update({
                    "width": w, "height": h,
                    "aspect": round(w / h, 4),
                    "mode": im.mode,
                    "dpiMeta": list(im.info["dpi"]) if "dpi" in im.info else None,
                    "textMetadata": sorted(k for k, v in im.info.items()
                                           if isinstance(v, str)),
                })
                alpha = None
                if "A" in im.mode:
                    lo, hi = im.getchannel("A").getextrema()
                    alpha = {"present": True, "min": lo, "max": hi,
                             "meaningful": lo != 255}
                elif "transparency" in im.info:
                    alpha = {"present": True, "min": None, "max": None,
                             "meaningful": True}
                else:
                    alpha = {"present": False, "meaningful": False}
                rec["alpha"] = alpha

                g = im.convert("L")
                hist = g.histogram()
                total = w * h
                rec["inkCoverage"] = round(sum(hist[:128]) / total, 4)
                rec["distinctLevels"] = sum(1 for n_ in hist if n_)
                rec["blank"] = rec["inkCoverage"] < BLANK_INK_FLOOR
                # Renk kaçağı: siyah-beyaz kitapta renkli piksel bir kusurdur.
                #
                # ⚠ ÖLÇÜ "EN BÜYÜK KANAL FARKI" DEĞİL, "GERÇEKTEN RENKLİ
                # PİKSELİN PAYI"DIR. Faz 5 ölçümü: üretici görsellerinin
                # tamamı nötr çizim, ama kâğıt tonunda 16/255'e (%6) varan
                # ılık bir tül taşıyor. Tek pikselin en büyük farkına bakan
                # eşik bunu "renk kaçağı" sayıyordu — oysa aynı envanterde
                # delta>16 olan piksel oranı 0,0000, yani HİÇBİR ALAN renkli
                # değil ve hat `convert("L")` ile tülü zaten atıyor.
                #
                # Kuralın sorduğu soru "renkli bir görsel mi geldi"dir; onu
                # ölçen istatistik paydır, gürültüye duyarlı tepe değeri değil.
                if im.mode in ("RGB", "RGBA"):
                    small = im.convert("RGB").resize((64, 64))
                    px = list(small.getdata())
                    deltas = [max(abs(r - gg), abs(gg - b), abs(r - b))
                              for r, gg, b in px]
                    rec["maxChannelDelta"] = max(deltas)
                    rec["colourPixelShare"] = round(
                        sum(1 for d in deltas if d > 16) / len(deltas), 4)
                else:
                    rec["maxChannelDelta"] = 0
                    rec["colourPixelShare"] = 0.0
            rec["opens"] = True
            rec["error"] = None
        except Exception as exc:                       # noqa: BLE001
            rec["opens"] = False
            rec["error"] = f"{type(exc).__name__}: {exc}"

        # şartname karşılaştırması
        if rec["kind"]:
            k = spec.KINDS[rec["kind"]]
            want_w, want_h = k["raw_px"]
            gen_w, gen_h = k["generator_px"]
            rec["spec"] = {
                "rawPx": [want_w, want_h],
                "generatorPx": [gen_w, gen_h],
                "aspectWant": round(want_w / want_h, 4),
                "aspectOk": (rec.get("width") is not None
                             and abs(rec["aspect"] - want_w / want_h) < 0.02),
                "meetsRawPx": bool(rec.get("width", 0) >= want_w),
                "meetsGeneratorPx": bool(rec.get("width", 0) >= gen_w),
            }

        m = mapping.get(image_id)
        rec["mapping"] = m
        rows.append(rec)
        by_hash.setdefault(rec["sha256"], []).append(name)
        by_id.setdefault(image_id, []).append(name)

    expected = spec.expected_ids()
    have = {r["id"] for r in rows if r["kind"]}
    unrecognised = [r["file"] for r in rows if not r["kind"]]

    return {
        "$comment": [
            "HAM VARLIK ENVANTERİ — 07_ASSETS/raw salt okunur (K5 · § 32).",
            "Bu rapor yalnızca ÖLÇÜ içerir; hiçbir hikâye cümlesi taşımaz (K21).",
            "Üretici: 04_BUILD/asset_inventory.py",
        ],
        "gate": mb.read_gate(),
        "expected": spec.TOTAL,
        "actual": len(rows),
        "byKind": {k: sum(1 for r in rows if r["kind"] == k) for k in spec.KINDS},
        "expectedByKind": {k: v["count"] for k, v in spec.KINDS.items()},
        "missing": sorted(expected - have),
        "orphans": sorted(have - expected),
        "unrecognised": unrecognised,
        "duplicateBytes": {h: f for h, f in by_hash.items() if len(f) > 1},
        "duplicateIds": {i: f for i, f in by_id.items() if len(f) > 1},
        "nameDeviations": [{"file": r["file"], "canonicalId": r["id"]}
                           for r in rows if r["nameDeviation"]],
        "unmapped": [r["id"] for r in rows if r["kind"] and not r["mapping"]],
        "corrupt": [r["file"] for r in rows
                    if not r["opens"] or not r["png"]["signature"]
                    or not r["png"]["crcOk"] or r["png"]["truncated"]],
        "blank": [r["file"] for r in rows if r.get("blank")],
        # %0,5'ten fazla piksel gerçekten renkliyse bu bir RENKLİ görseldir.
        "colourLeak": [r["file"] for r in rows
                       if r.get("colourPixelShare", 0) > 0.005],
        "meaningfulAlpha": [r["file"] for r in rows
                            if (r.get("alpha") or {}).get("meaningful")],
        "belowRawPx": [r["id"] for r in rows
                       if r.get("spec") and not r["spec"]["meetsRawPx"]],
        "belowGeneratorPx": [r["id"] for r in rows
                             if r.get("spec") and not r["spec"]["meetsGeneratorPx"]],
        "aspectMismatch": [r["id"] for r in rows
                           if r.get("spec") and not r["spec"]["aspectOk"]],
        "assets": rows,
    }


def report(data: dict, r: mb.Result) -> None:
    print(f"\n  beklenen : {data['expected']}")
    print(f"  bulunan  : {data['actual']}")
    for k in spec.KINDS:
        print(f"    {k:>8}: {data['byKind'][k]:>2} / {data['expectedByKind'][k]}")

    r.add(data["actual"] == data["expected"],
          f"{data['actual']}/{data['expected']} ham görsel var",
          f"ham dizinde {data['actual']} dosya var, {data['expected']} bekleniyor")

    for kind, want in data["expectedByKind"].items():
        got = data["byKind"][kind]
        r.add(got == want, f"{kind}: {got}/{want}",
              f"{kind}: {got}/{want} — 45+22+1=68 fiyat modelinin dayanağıdır (K4)")

    r.add(not data["missing"], "eksik ham görsel yok",
          f"EKSİK: {data['missing'][:12]}")
    r.add(not data["orphans"], "yetim ham görsel yok",
          f"YETİM (şartnamede karşılığı yok): {data['orphans'][:12]}")
    r.add(not data["unrecognised"], "tanınmayan dosya yok",
          f"TANINMAYAN: {data['unrecognised'][:12]}")
    r.add(not data["duplicateBytes"], "bayt-birebir yinelenen dosya yok",
          f"YİNELENEN: {list(data['duplicateBytes'].values())[:5]}")
    r.add(not data["duplicateIds"], "kimlik çakışması yok",
          f"AYNI KİMLİĞE İKİ DOSYA: {list(data['duplicateIds'].items())[:5]}")
    r.add(not data["corrupt"], "bütün PNG'ler sağlam (imza · CRC · IEND)",
          f"BOZUK: {data['corrupt'][:12]}")
    r.add(not data["blank"], "boş/neredeyse boş görsel yok",
          f"BOŞ: {data['blank'][:12]}")
    r.add(not data["unmapped"], "her görsel bir proje kimliğine bağlandı",
          f"EŞLENMEMİŞ: {data['unmapped'][:12]}")
    r.add(not data["colourLeak"], "renk kaçağı yok (kitap siyah-beyaz)",
          f"RENKLİ PİKSEL: {data['colourLeak'][:12]}")

    r.warn(not data["meaningfulAlpha"], "gerçek saydamlık taşıyan dosya yok",
           f"saydam dosya: {data['meaningfulAlpha'][:12]} — hat beyaza düzleştirir")
    r.warn(not data["nameDeviations"],
           "bütün dosya adları kanonik biçimde",
           f"AD SAPMASI (normalize edildi, ham dosya DEĞİŞMEDİ): "
           f"{[d['file'] + ' → ' + d['canonicalId'] for d in data['nameDeviations']]}")

    # --- ŞARTNAME ÇELİŞKİSİ: raw_px üreticinin verebildiğinden büyük ---
    #
    # Bu iki satırın ŞİDDET SEVİYESİ FARKLIDIR ve fark bilinçlidir:
    #   · generator_px altındaki dosya  → KUSURLU TESLİMAT (kurucu yanlış boyut seçti)
    #   · raw_px altındaki dosya        → ŞARTNAME ÇELİŞKİSİ (üretici o boyutu veremez)
    # İkincisini HATA yapmak, doğru üretilmiş her dosyayı da reddeder.
    r.add(not data["belowGeneratorPx"],
          "bütün görseller üreticinin en büyük uygun boyutunda",
          f"ÜRETİCİ BOYUTUNUN ALTINDA: {data['belowGeneratorPx'][:12]} — "
          f"{spec.GENERATOR} bu tür için daha büyüğünü verebilirdi")
    r.warn(not data["belowRawPx"],
           "bütün görseller şartname çözünürlüğünde",
           f"{len(data['belowRawPx'])} görsel `raw_px` altında — "
           f"şartname 600 dpi için o pikseli istiyor ama {spec.GENERATOR} "
           f"en fazla {max(w for w, _ in spec.GENERATOR_NATIVE_SIZES)} px veriyor. "
           "KURUCU KARARI (Faz 5 raporu).")
    r.add(not data["aspectMismatch"],
          "bütün görseller şartname en-boy oranında",
          f"EN-BOY ORANI ŞARTNAMEYE UYMUYOR: {data['aspectMismatch'][:12]}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Ham varlık envanteri")
    ap.add_argument("--check", action="store_true", help="kayıtlı rapor bayat mı")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    print("═" * 72)
    print("  HAM VARLIK ENVANTERİ")
    print("═" * 72)
    print("  07_ASSETS/raw SALT OKUNURDUR — bu betik oraya yazmaz.")

    r = mb.Result("asset_inventory", verbose=args.verbose)

    if not os.path.isdir(spec.RAW_DIR):
        r.ok("ham dizin yok — envanter uygulanamaz")
        return r.finish(args.json)

    data = inventory()

    if args.check:
        if not os.path.exists(REPORT):
            r.fail("asset-inventory.json yok", "`asset_inventory.py` çalıştırın")
            return r.finish(args.json)
        with open(REPORT, encoding="utf-8") as fh:
            old = json.load(fh)
        r.add(old.get("assets") == data["assets"], "envanter raporu güncel",
              "BAYAT — ham dizin değişmiş; `asset_inventory.py` çalıştırın")
        return r.finish(args.json)

    report(data, r)

    os.makedirs(mb.REPORTS_TRACKED, exist_ok=True)
    with open(args.json or REPORT, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"\n  ✎ {os.path.relpath(args.json or REPORT, mb.ROOT)}")

    return r.finish(None)


if __name__ == "__main__":
    sys.exit(main())
