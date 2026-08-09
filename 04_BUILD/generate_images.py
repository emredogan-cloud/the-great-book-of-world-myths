#!/usr/bin/env python3
"""
HAM GÖRSEL ÜRETİMİ — GPT Image (kurucu yetkisiyle)
================================================================================
    python3 04_BUILD/generate_images.py --ids story-001            tek görsel
    python3 04_BUILD/generate_images.py --kind story               45 hikâye
    python3 04_BUILD/generate_images.py --ids culture-008 map-001
    python3 04_BUILD/generate_images.py --kind story --dry-run     hiçbir şey harcamaz

⚠ BU BETİK PARA HARCAR. Kurucu Faz 5'te açık yetki verdi ve BİR TAVAN koydu:
  toplam ≈ 4,00 $. Betik o tavanı kendi kendine YÜKSELTEMEZ.

--------------------------------------------------------------------------------
NEDEN SDK YOK
--------------------------------------------------------------------------------
Karar K7: "kalite kapılarının hiçbiri bağımlılığa ihtiyaç duymaz." Bu betik
bir kapı değil ama aynı disipline uyar: OpenAI REST uç noktası tek bir POST
isteğidir ve Python standart kütüphanesi onu karşılar. Yeni bir paket
kurmamak, CI'ın hafif işini bozmamak demektir.

--------------------------------------------------------------------------------
GİZLİLİK
--------------------------------------------------------------------------------
Anahtar `.env`ten okunur, ASLA basılmaz, ASLA rapora yazılmaz, ASLA hata
mesajına konmaz. `.gitignore` § 105 `.env`i zaten dışlıyor ve git geçmişinde
hiç yer almamış olduğu doğrulandı. Bu betiğin ürettiği tek kayıt maliyet
defteridir ve içinde sır yoktur.

--------------------------------------------------------------------------------
HAM DOSYA YOK EDİLMEZ
--------------------------------------------------------------------------------
Yeniden üretim, eskisini SİLMEZ: `07_ASSETS/raw/superseded/<damga>/` altına
taşır. Bu klasörün adı uydurulmadı — prompt kütüphanesi kurucuya üç fazdır
tam olarak bu yolu söylüyor.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb
import imagespec as spec
import make_prompts

API_URL = "https://api.openai.com/v1/images/generations"
MODEL = "gpt-image-1"
LEDGER = os.path.join(mb.REPORTS_TRACKED, "image-generation-ledger.json")

# --- BÜTÇE ---------------------------------------------------------------
# Kurucu tavanı 4,00 $. Betik 3,50 $'a ULAŞINCA yeni istek göndermez; aradaki
# 0,50 $ fiyat sürprizine karşı kasıtlı marjdır.
BUDGET_CEILING_USD = 4.00
BUDGET_STOP_USD = 3.50

# gpt-image-1 liste fiyatları (görsel başına, USD). Fatura AYNEN bu olmayabilir;
# bu yüzden defter "estimated" der ve tavan muhafazakâr tutulur.
PRICE_USD = {
    ("low", "1024x1024"): 0.011, ("low", "1536x1024"): 0.016,
    ("low", "1024x1536"): 0.016,
    ("medium", "1024x1024"): 0.042, ("medium", "1536x1024"): 0.063,
    ("medium", "1024x1536"): 0.063,
    ("high", "1024x1024"): 0.167, ("high", "1536x1024"): 0.25,
    ("high", "1024x1536"): 0.25,
}

# Üreticinin verebildiği ölçüler — şartname `generator_px` ile eşleşir.
SIZE_FOR_KIND = {
    "story": "1536x1024",     # 3:2 YATAY — Faz 5 kök sebep düzeltmesi
    "culture": "1024x1024",   # 1:1 kare
    "map": "1536x1024",       # 3:2 yatay
}


def read_key() -> str | None:
    """`.env` → OPENAI_API_KEY. Değer HİÇBİR YERE basılmaz."""
    key = os.environ.get("OPENAI_API_KEY")
    if key:
        return key.strip()
    env = os.path.join(mb.ROOT, ".env")
    if not os.path.exists(env):
        return None
    with open(env, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            name, _, value = line.partition("=")
            if name.strip() == "OPENAI_API_KEY":
                return value.strip().strip('"').strip("'")
    return None


def load_ledger() -> dict:
    if os.path.exists(LEDGER):
        try:
            with open(LEDGER, encoding="utf-8") as fh:
                return json.load(fh)
        except (OSError, ValueError):
            pass
    return {"$comment": [
        "GÖRSEL ÜRETİM MALİYET DEFTERİ — sır İÇERMEZ.",
        "Fiyatlar liste fiyatından TAHMİN edilmiştir; fatura farklı olabilir.",
        "Üretici: 04_BUILD/generate_images.py",
    ], "ceilingUsd": BUDGET_CEILING_USD, "entries": []}


def spent(ledger: dict) -> float:
    return round(sum(e["estimatedUsd"] for e in ledger["entries"]), 4)


def prompt_for(rec: dict) -> str:
    """
    Prompt + olumsuz kısıtlar TEK metinde.

    gpt-image-1'in ayrı bir negative alanı yoktur; kütüphane ikisini ayrı
    tutar (insan okusun diye) ama API'ye giderken birleşirler. Birleştirmeyi
    burada yapmak, kütüphanenin iki alanlı yapısını bozmadan tek çağrı yeri
    bırakır.
    """
    return f"{rec['prompt']}\n\nAvoid entirely: {rec['negative']}."


def generate_one(key: str, rec: dict, size: str, quality: str,
                 timeout: int = 300) -> tuple[bytes | None, str | None, dict]:
    body = json.dumps({
        "model": MODEL,
        "prompt": prompt_for(rec),
        "size": size,
        "quality": quality,
        "n": 1,
        "output_format": "png",
    }).encode("utf-8")
    req = urllib.request.Request(
        API_URL, data=body, method="POST",
        headers={"Content-Type": "application/json",
                 "Authorization": f"Bearer {key}"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.load(resp)
    except urllib.error.HTTPError as exc:
        # ⚠ Gövde anahtar İÇEREBİLİR mi? Hayır — ama yine de kırpıyoruz ve
        # Authorization başlığı hiçbir yere yazılmıyor.
        detail = exc.read().decode("utf-8", "replace")[:300]
        return None, f"HTTP {exc.code}: {detail}", {}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return None, f"{type(exc).__name__}: {exc}", {}

    data = (payload.get("data") or [{}])[0]
    b64 = data.get("b64_json")
    if not b64:
        return None, "yanıtta b64_json yok", payload.get("usage") or {}
    return base64.b64decode(b64), None, payload.get("usage") or {}


def validate_png(path: str, kind: str) -> dict:
    """Üretilen dosyayı TEK TEK doğrula — 'yaklaşık doğru' kabul edilmez."""
    from PIL import Image
    out: dict = {"ok": False, "problems": []}
    try:
        with Image.open(path) as im:
            im.load()
            w, h = im.size
            out.update({"width": w, "height": h, "mode": im.mode,
                        "aspect": round(w / h, 4),
                        "bytes": os.path.getsize(path)})
            g = im.convert("L")
            hist = g.histogram()
            total = w * h
            out["inkCoverage"] = round(sum(hist[:128]) / total, 4)
            out["midtone"] = round(sum(hist[60:201]) / total, 4)
    except Exception as exc:                                # noqa: BLE001
        out["problems"].append(f"açılamadı: {type(exc).__name__}: {exc}")
        return out

    want_w, want_h = spec.KINDS[kind]["generator_px"]
    if (w, h) != (want_w, want_h):
        out["problems"].append(f"ölçü {w}×{h}, beklenen {want_w}×{want_h}")
    want_ratio = spec.KINDS[kind]["raw_px"][0] / spec.KINDS[kind]["raw_px"][1]
    if abs(out["aspect"] - want_ratio) > 0.02:
        out["problems"].append(
            f"en-boy oranı {out['aspect']}, beklenen {round(want_ratio, 3)}")
    lo, hi = spec.TOLERANCES.get("ink_coverage_by_kind", {}).get(
        kind, spec.TOLERANCES["ink_coverage"])
    if not lo <= out["inkCoverage"] <= hi:
        out["problems"].append(
            f"mürekkep yoğunluğu {out['inkCoverage']} bant dışı [{lo}, {hi}]")
    # ⚠ EŞİK %8'DEN %20'YE ÇIKARILDI VE GEREKÇESİ DEĞİŞTİ.
    #
    # İlk hâli Kindle bütçesini korumak içindi. O gerekçe artık GEÇERSİZ:
    # bütçe, Kindle türevinin 1 bit kodlanmasıyla çözüldü (242 KB → 33 KB) ve
    # orta ton payının dosya boyutuna etkisi kalmadı. Kuralı eski eşikte
    # bırakmak, ÇÖZÜLMÜŞ bir sorun için iyi görselleri reddetmek olurdu.
    #
    # Geriye kalan tek gerekçe BASKI NETLİĞİDİR ve o daha gevşektir. %20,
    # ölçülmüş iki uçtan geçer: kahverengi zemin felaketi %42,8 (reddedilmeli),
    # kabul edilebilir çizgi işi %10,9 (geçmeli).
    if out["midtone"] > 0.20:
        out["problems"].append(
            f"orta ton payı %{out['midtone'] * 100:.1f} — sürekli ton "
            "(eşik %20) baskıda gri bulamaç verir")
    out["ok"] = not out["problems"]
    return out


def archive_existing(image_ids: list[str], stamp: str) -> list[dict]:
    """Eskiyi SİLME — `raw/superseded/<damga>/` altına taşı."""
    moved = []
    dest_dir = os.path.join(spec.RAW_DIR, "superseded", stamp)
    for iid in image_ids:
        src = spec.raw_path(iid)
        if not src or os.path.dirname(src) != spec.RAW_DIR.rstrip("/"):
            continue
        os.makedirs(dest_dir, exist_ok=True)
        dest = os.path.join(dest_dir, os.path.basename(src))
        os.replace(src, dest)
        moved.append({"id": iid,
                      "from": os.path.relpath(src, mb.ROOT),
                      "to": os.path.relpath(dest, mb.ROOT)})
    return moved


def main() -> int:
    ap = argparse.ArgumentParser(description="Ham görsel üretimi (GPT Image)")
    ap.add_argument("--ids", nargs="*", default=None)
    ap.add_argument("--kind", choices=sorted(spec.KINDS), default=None)
    ap.add_argument("--quality", default="medium",
                    choices=["low", "medium", "high"])
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--dry-run", action="store_true",
                    help="hiçbir istek göndermez, yalnızca planı ve maliyeti basar")
    ap.add_argument("--stamp", default=None, help="arşiv damgası (yeniden üretim)")
    args = ap.parse_args()

    print("═" * 72)
    print("  HAM GÖRSEL ÜRETİMİ · GPT Image")
    print("═" * 72)

    records = {r["id"]: r for r in make_prompts.build_records()}
    if args.ids:
        targets = [i for i in args.ids]
    elif args.kind:
        targets = [i for i, r in records.items() if r["kind"] == args.kind]
    else:
        print("  --ids veya --kind verin.")
        return 2
    unknown = [i for i in targets if i not in records]
    if unknown:
        print(f"  ⛔ tanınmayan kimlik: {unknown}")
        return 2
    targets.sort()
    if args.limit:
        targets = targets[:args.limit]

    ledger = load_ledger()
    already = spent(ledger)
    plan = []
    running = already
    for iid in targets:
        kind = records[iid]["kind"]
        size = SIZE_FOR_KIND[kind]
        price = PRICE_USD[(args.quality, size)]
        plan.append({"id": iid, "kind": kind, "size": size, "price": price})
        running += price

    print(f"\n  hedef        : {len(plan)} görsel · kalite {args.quality}")
    print(f"  daha önce    : {already:.3f} $")
    print(f"  bu koşu      : {running - already:.3f} $ (tahmin)")
    print(f"  toplam olur  : {running:.3f} $")
    print(f"  durma eşiği  : {BUDGET_STOP_USD:.2f} $ · tavan "
          f"{BUDGET_CEILING_USD:.2f} $")

    if running > BUDGET_STOP_USD:
        print(f"\n  ⛔ BU PLAN DURMA EŞİĞİNİ AŞIYOR ({running:.3f} $ > "
              f"{BUDGET_STOP_USD:.2f} $).")
        print("     Betik bütçeyi kendi kendine yükseltmez. --limit ile "
              "küçültün veya --quality low deneyin.")
        return 1

    if args.dry_run:
        print("\n  --dry-run: hiçbir istek gönderilmedi.")
        for p in plan:
            print(f"    {p['id']:<14} {p['kind']:<8} {p['size']:<10} "
                  f"{p['price']:.3f} $")
        return 0

    key = read_key()
    print(f"\n  OPENAI_API_KEY {'detected' if key else 'NOT detected'}")
    if not key:
        print("  ⛔ anahtar yok — .env içine OPENAI_API_KEY ekleyin.")
        return 1

    stamp = args.stamp or time.strftime("%Y%m%dT%H%M%S")
    moved = archive_existing([p["id"] for p in plan], stamp)
    if moved:
        print(f"  ⇄ {len(moved)} eski ham dosya arşivlendi → "
              f"07_ASSETS/raw/superseded/{stamp}/")

    os.makedirs(spec.RAW_DIR, exist_ok=True)
    ok_count, failures = 0, []
    for i, p in enumerate(plan, 1):
        if spent(ledger) + p["price"] > BUDGET_STOP_USD:
            print(f"\n  ⛔ BÜTÇE DURMA EŞİĞİ — {spent(ledger):.3f} $ harcandı, "
                  f"{len(plan) - i + 1} görsel üretilmedi.")
            break
        rec = records[p["id"]]
        print(f"  [{i:>2}/{len(plan)}] {p['id']} … ", end="", flush=True)
        blob, err, usage = generate_one(key, rec, p["size"], args.quality)
        entry = {"id": p["id"], "kind": p["kind"], "size": p["size"],
                 "quality": args.quality, "estimatedUsd": p["price"],
                 "stamp": stamp, "ok": False, "error": err,
                 "usage": {k: v for k, v in (usage or {}).items()
                           if isinstance(v, (int, float))}}
        if err:
            print(f"HATA — {err[:80]}")
            entry["estimatedUsd"] = 0.0        # başarısız istek faturalanmaz
            failures.append((p["id"], err))
            ledger["entries"].append(entry)
            continue

        dest = os.path.join(spec.RAW_DIR, f"{p['id']}.{spec.RAW_FORMAT}")
        with open(dest, "wb") as fh:
            fh.write(blob)
        v = validate_png(dest, p["kind"])
        entry["ok"] = v["ok"]
        entry["validation"] = v
        ledger["entries"].append(entry)
        with open(LEDGER, "w", encoding="utf-8") as fh:
            json.dump(ledger, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        if v["ok"]:
            ok_count += 1
            print(f"✓ {v['width']}×{v['height']} · "
                  f"mürekkep {v['inkCoverage']:.3f} · "
                  f"orta ton %{v['midtone'] * 100:.1f} · "
                  f"{v['bytes'] / 1024:.0f} KB")
        else:
            print(f"✗ {'; '.join(v['problems'])[:100]}")
            failures.append((p["id"], "; ".join(v["problems"])))

    os.makedirs(mb.REPORTS_TRACKED, exist_ok=True)
    with open(LEDGER, "w", encoding="utf-8") as fh:
        json.dump(ledger, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print(f"\n  üretildi     : {ok_count}/{len(plan)}")
    print(f"  tahmini gider: {spent(ledger):.3f} $ "
          f"(tavan {BUDGET_CEILING_USD:.2f} $)")
    print(f"  ✎ {os.path.relpath(LEDGER, mb.ROOT)}")
    if failures:
        print(f"\n  ⛔ {len(failures)} başarısız:")
        for iid, why in failures[:10]:
            print(f"     · {iid}: {why[:90]}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
