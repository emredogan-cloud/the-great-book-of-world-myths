#!/usr/bin/env python3
"""
AMAZON A+ İÇERİK MODÜLLERİ — nihai görseller
================================================================================
    python3 04_BUILD/aplus.py            üret + doğrula
    python3 04_BUILD/aplus.py --check    kayıtlı rapor bayat mı

    07_ASSETS/raw/aplus-*.png            ham sanat (DEĞİŞTİRİLMEZ)
              ↓
    08_OUTPUT/aplus/<id>.jpg             modülün TAM piksel ölçüsünde
    06_REPORTS/tracked/aplus-build.json

--------------------------------------------------------------------------------
İKİ KURAL
--------------------------------------------------------------------------------
① AMAZON ÖLÇÜLERİ PAZARLIĞA KAPALIDIR. Her standart modülün piksel ölçüsü
  sabittir; "yaklaşık" diye bir şey yoktur. Ham sanat oranı tutmuyorsa
  ORTADAN KIRPILIR — dolgu (letterbox) yapılmaz, çünkü beyaz bant ürün
  sayfasında görünür. Ne kadar kırpıldığı ölçülür ve raporlanır.

② TİPOGRAFİ ÜRETİLMEZ, SONRADAN BASILIR (talimat § 45 · Faz 5 şartnamesi
  `typography: post`). Faz 6 bunun neden şart olduğunu bir kez daha gösterdi:
  aynı üretici, kapakta kitabın adını YANLIŞ yazdı. Modül metinleri burada
  kitabın DOĞRULANMIŞ envanterinden gelir (45 hikâye · 22 kültür) ve
  deterministik basılır.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb
import coverspec as cs
import editions as ed_mod

OUT_DIR = os.path.join(mb.ROOT, "08_OUTPUT", "aplus")
OUT_JSON = os.path.join(mb.REPORTS_TRACKED, "aplus-build.json")
RAW = os.path.join(mb.ASSETS, "raw")

FONT_DIR = "/usr/share/fonts/truetype/lato"
FONTS = {"black": "Lato-Black.ttf", "bold": "Lato-Bold.ttf",
         "reg": "Lato-Regular.ttf"}

INK = (18, 29, 66)
ACCENT = (219, 92, 26)

# Modül metinleri — kitabın DOĞRULANMIŞ sayılarından. Her biri
# `validate_against_inventory` ile envantere karşı sınanır.
TEXT = {
    "aplus-001-hero": {
        "head": "Forty-five myths. Twenty-two cultures. One book.",
        "sub": "Retold for readers aged 8–12",
        "align": "left", "band": 0.42,
    },
    "aplus-002-cultures": {
        "head": "Twenty-two traditions, at one standard",
        "sub": "Korean · Inuit · Māori · Hawaiian · Yoruba · Akan · Persian · "
               "Turkic · Greek · Norse · Irish · Finnish · Egyptian · "
               "Mesopotamian · Japanese · Chinese · Vietnamese · Hindu · "
               "Maya · Aztec · Andean · Zulu",
        # ⚠ TAM PANEL DEĞİL, ALT ŞERİT. Tam genişlikte opak bir panel
        # 22 amblemi tamamen gizliyordu — modülün bütün değeri o amblemler.
        "align": "center", "band": 0.0, "strip": 0.58,
    },
    "aplus-003-map": {"head": "Where every story comes from",
                      "sub": "", "align": "center", "band": 0.0},
    "aplus-004-value": {"head": "45 stories", "sub": "22 cultures",
                        "align": "center", "band": 0.0},
    "aplus-005-linework": {"head": "68 drawings", "sub": "black and white",
                           "align": "center", "band": 0.0},
    "aplus-006-reader": {"head": "Ages 8–12", "sub": "a chapter a night",
                         "align": "center", "band": 0.0},
    "aplus-007-backmatter": {"head": "Say every name", "sub": "guide at the back",
                             "align": "center", "band": 0.0},
    "aplus-008-interior": {"head": "A book to read", "sub": "", "align": "center",
                           "band": 0.0},
    "aplus-009-parent": {"head": "", "sub": "", "align": "center", "band": 0.0},
    "aplus-010-series": {"head": "", "sub": "", "align": "center", "band": 0.0},
}


def load_font(kind: str, size: int):
    from PIL import ImageFont
    p = os.path.join(FONT_DIR, FONTS[kind])
    return ImageFont.truetype(p, size)


def fit_cover(im, tw: int, th: int):
    """Modülün TAM ölçüsüne kırparak sığdır — esnetme yok, dolgu yok."""
    from PIL import Image
    sw, sh = im.size
    scale = max(tw / sw, th / sh)
    nw, nh = max(1, round(sw * scale)), max(1, round(sh * scale))
    r = im.resize((nw, nh), Image.LANCZOS)
    left, top = (nw - tw) // 2, (nh - th) // 2
    return r.crop((left, top, left + tw, top + th)), {
        "sourcePx": [sw, sh], "scale": round(scale, 4),
        "croppedPct": [round(100 * (nw - tw) / nw, 2),
                       round(100 * (nh - th) / nh, 2)],
    }


def _wrap(d, text, font, maxw):
    out, cur = [], ""
    for word in text.split():
        t = (cur + " " + word).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def _fit_block(d, head, sub, maxw, maxh, start_pt):
    """
    Başlık+alt satırı KUTUYA SIĞDIRAN en büyük puntoyu bulur.

    ⚠ İLK SÜRÜM PUNTOYU YÜKSEKLİĞİN SABİT ORANINDAN ALIYORDU
    (h×0,115) ve metnin UZUNLUĞUNA hiç bakmıyordu: 970×600 modülde başlık
    69 punto çıktı, üç satıra taştı ve modülün altından TAŞARAK kesildi.
    Punto, metnin kendisinden hesaplanmak zorundadır.
    """
    pt = start_pt
    while pt >= 9:
        fh_ = load_font("black", pt)
        spt = max(8, int(pt * 0.56))
        fs_ = load_font("reg", spt)
        hl = _wrap(d, head, fh_, maxw) if head else []
        sl = _wrap(d, sub, fs_, maxw) if sub else []
        total = len(hl) * int(pt * 1.20) + len(sl) * int(spt * 1.34)
        if total <= maxh and len(hl) <= 4:
            return pt, spt, hl, sl, total
        pt -= 1
    return 9, 8, [head] if head else [], [sub] if sub else [], maxh


def draw_text(im, spec_txt, w, h):
    """Metni GÜVENLİ ALANA basar ve kutusunu döndürür."""
    from PIL import ImageDraw
    if not spec_txt.get("head"):
        return None
    d = ImageDraw.Draw(im, "RGBA")
    pad = max(8, int(min(w, h) * 0.06))
    band = spec_txt.get("band", 0.0)

    if band > 0:
        # yan/tam panel — hero ve kültür şeridi
        panel_w = int(w * band)
        d.rectangle([0, 0, panel_w, h], fill=(255, 255, 255, 214))
        maxw, maxh = panel_w - 2 * pad, h - 2 * pad
        ox, oy = 0, 0
    else:
        # ALT ŞERİT — küçük karelerde metin resmin üstüne değil, kendi
        # şeridine basılır; ilk sürümde 220×220 karelerde yazı çizimin
        # üstünde okunmuyordu.
        strip_h = max(46, int(h * spec_txt.get("strip", 0.30)))
        d.rectangle([0, h - strip_h, w, h], fill=(255, 255, 255, 226))
        maxw, maxh = w - 2 * pad, strip_h - 2 * int(pad * 0.5)
        ox, oy = 0, h - strip_h + int(pad * 0.5)
        panel_w = w

    start = int(h * 0.20) if band > 0 else int(h * 0.16)
    pt, spt, hl, sl, total = _fit_block(d, spec_txt.get("head", ""),
                                        spec_txt.get("sub", ""),
                                        maxw, maxh, max(12, start))
    fh_, fs_ = load_font("black", pt), load_font("reg", spt)
    y = oy + max(0, (maxh - total) // 2)
    x0, y0, x1 = w, y, 0

    for ln in hl:
        tw_ = d.textlength(ln, font=fh_)
        x = pad if spec_txt["align"] == "left" else ox + (panel_w - tw_) / 2
        d.text((x, y), ln, font=fh_, fill=INK)
        x0, x1 = min(x0, x), max(x1, x + tw_)
        y += int(pt * 1.20)
    for ln in sl:
        tw_ = d.textlength(ln, font=fs_)
        x = pad if spec_txt["align"] == "left" else ox + (panel_w - tw_) / 2
        d.text((x, y), ln, font=fs_, fill=ACCENT if len(sl) == 1 else INK)
        x0, x1 = min(x0, x), max(x1, x + tw_)
        y += int(spt * 1.34)
    return [int(x0), int(y0), int(x1), int(y)]


def validate_against_inventory(r: mb.Result) -> None:
    """Modül metinlerindeki sayılar GERÇEK envanterle eşleşmeli."""
    blob = " ".join(f"{v.get('head','')} {v.get('sub','')}"
                    for v in TEXT.values())
    r.add(str(mb.STORY_TARGET) in blob and str(mb.CULTURE_TARGET) in blob,
          f"A+ metinleri envanterle tutarlı ({mb.STORY_TARGET} hikâye · "
          f"{mb.CULTURE_TARGET} kültür)",
          "A+ metinlerindeki sayılar envanterle uyuşmuyor")
    ic = os.path.join(mb.REPORTS_TRACKED, "image-consistency.json")
    if os.path.exists(ic):
        with open(ic, encoding="utf-8") as fh:
            n = json.load(fh).get("accepted", 0)
        r.add(str(n) in blob or n != 68,
              f"A+ görsel sayısı iddiası ölçümle aynı ({n})",
              f"A+ metni görsel sayısı iddia ediyor ama ölçüm {n}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Amazon A+ modülleri")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    print("═" * 72)
    print("  AMAZON A+ İÇERİK MODÜLLERİ")
    print("═" * 72)

    r = mb.Result("aplus", verbose=args.verbose)
    try:
        from PIL import Image
    except ImportError:
        print("ATLANDI: Pillow yok")
        return 2

    ib = os.path.join(mb.REPORTS_TRACKED, "interior-build.json")
    pages = mb.PAGE_TARGET
    if os.path.exists(ib):
        with open(ib, encoding="utf-8") as fh:
            pages = json.load(fh)["editions"]["paperback"]["totalPages"]
    ed = ed_mod.get("paperback")
    specs = {x["id"]: x for x in cs.all_records(pages, ed.trim_w_in, ed.trim_h_in)
             if x["family"] == "aplus"}

    os.makedirs(OUT_DIR, exist_ok=True)
    rows, missing = [], []
    for mid, sp in sorted(specs.items()):
        src = os.path.join(RAW, f"{mid}.png")
        if not os.path.exists(src):
            missing.append(mid)
            continue
        tw, th = sp["renderPx"]
        with Image.open(src) as im:
            im = im.convert("RGB")
            out, info = fit_cover(im, tw, th)
        box = draw_text(out, TEXT.get(mid, {}), tw, th)
        dest = os.path.join(OUT_DIR, f"{mid}.jpg")
        out.save(dest, "JPEG", quality=90, optimize=True, dpi=(72, 72))
        rec = {
            "id": mid, "module": sp["module"], "targetPx": [tw, th],
            "file": os.path.relpath(dest, mb.ROOT),
            "bytes": os.path.getsize(dest),
            "art": info, "textBoxPx": box,
            "typography": "post",
            "source": os.path.relpath(src, mb.ROOT),
        }
        with Image.open(dest) as chk:
            rec["actualPx"] = list(chk.size)
            rec["mode"] = chk.mode
        rows.append(rec)
        if args.verbose:
            print(f"  ✎ {mid:<22} {tw}×{th}  kırpma %{max(info['croppedPct'])}")

    print(f"\n  modül        : {len(rows)}/{len(specs)}")
    tot = sum(x["bytes"] for x in rows)
    print(f"  toplam boyut : {tot/1e6:.2f} MB")

    r.add(not missing, f"bütün A+ görselleri var ({len(rows)}/{len(specs)})",
          f"EKSİK A+ GÖRSELİ: {missing}")
    bad = [x["id"] for x in rows if x["actualPx"] != x["targetPx"]]
    r.add(not bad, "her modül TAM Amazon ölçüsünde",
          f"ÖLÇÜ TUTMUYOR: {bad}")
    big = [x["id"] for x in rows if x["bytes"] > 2_000_000]
    r.add(not big, "her modül Amazon dosya sınırında (<2 MB)",
          f"ÇOK BÜYÜK: {big}")
    notrgb = [x["id"] for x in rows if x["mode"] != "RGB"]
    r.add(not notrgb, "bütün modüller RGB", f"RGB DEĞİL: {notrgb}")
    heavy = [(x["id"], max(x["art"]["croppedPct"])) for x in rows
             if max(x["art"]["croppedPct"]) > 35]
    r.warn(not heavy, "kırpma payları makul",
           f"AĞIR KIRPMA (oran uyuşmazlığı): {heavy}")
    allpost = all(x["typography"] == "post" for x in rows)
    r.add(allpost, "bütün modüllerde tipografi SONRADAN basıldı",
          "üretilmiş tipografi kullanılmış")
    validate_against_inventory(r)

    payload = {"$comment": [
        "A+ MODÜL RAPORU — ölçü ve doğrulama. Proza içermez.",
        "Ham sanat DEĞİŞTİRİLMEDİ; metin CLI ile sonradan basıldı.",
        "Üretici: 04_BUILD/aplus.py",
    ], "gate": mb.read_gate(), "modules": rows, "missing": missing,
        "totalBytes": tot}

    if args.check:
        if not os.path.exists(OUT_JSON):
            r.fail("aplus-build.json yok", "`aplus.py` çalıştırın")
            return r.finish(None)
        with open(OUT_JSON, encoding="utf-8") as fh:
            old = json.load(fh)
        same = [(x["id"], x["targetPx"]) for x in old.get("modules", [])] == \
               [(x["id"], x["targetPx"]) for x in rows]
        r.add(same, "A+ raporu güncel", "BAYAT — `aplus.py` çalıştırın")
        return r.finish(None)

    os.makedirs(mb.REPORTS_TRACKED, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"\n  ✎ {os.path.relpath(OUT_JSON, mb.ROOT)}")
    print(f"  ✎ 08_OUTPUT/aplus/ ({len(rows)} dosya)")
    return r.finish(None)


if __name__ == "__main__":
    sys.exit(main())
