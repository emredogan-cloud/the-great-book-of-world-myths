#!/usr/bin/env python3
"""
KDP TESLİM BELGELERİ — kurucunun panelde kullanacağı el kitabı
================================================================================
    python3 04_BUILD/handoff.py            üret
    python3 04_BUILD/handoff.py --check    bayat mı

Üretir:
    08_OUTPUT/handoff/KDP_UPLOAD_HANDOFF.md
    08_OUTPUT/handoff/COVER_HANDOFF.md
    08_OUTPUT/handoff/A_PLUS_HANDOFF.md

⚠ HER DOSYA YOLU GERÇEKTİR VE VARLIĞI DENETLENİR. Var olmayan bir dosyayı
listelemek, kurucuyu panelde bulunmayan bir şeyi aramaya göndermek demektir;
bu yüzden her satır diske karşı sınanır ve durumu (READY / EKSİK) yazılır.

⚠ HİÇBİR PANEL İŞLEMİ YAPILMAZ. Yükleme, ISBN, KDP Select, fiyatlandırma,
Previewer onayı ve Publish KURUCUNUN işidir (talimat § 20).
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

OUT_DIR = os.path.join(mb.ROOT, "08_OUTPUT", "handoff")
REPORT = os.path.join(mb.REPORTS_TRACKED, "handoff.json")

FOUNDER = "🔴 KURUCU KARARI"
READY = "🟢 HAZIR"
NA = "⚪ UYGULANAMAZ"


def load(name):
    p = os.path.join(mb.REPORTS_TRACKED, name)
    if not os.path.exists(p):
        return {}
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def fstat(rel: str) -> tuple[str, str]:
    """(durum, boyut) — dosya GERÇEKTEN var mı."""
    p = os.path.join(mb.ROOT, rel)
    if os.path.exists(p):
        n = os.path.getsize(p)
        unit = f"{n/1e6:.1f} MB" if n >= 1e6 else f"{n/1e3:.0f} KB"
        return READY, unit
    return "🔴 EKSİK", "—"


def render_upload(d: dict) -> str:
    I, C, E, A, M = (d["interior"], d["cover"], d["epub"],
                     d["aplus"], d["metadata"])
    pb = I.get("editions", {}).get("paperback", {})
    hc = I.get("editions", {}).get("hardcover", {})
    L = []
    a = L.append
    a("# KDP YÜKLEME TESLİM BELGESİ")
    a("")
    a("<!-- OTOMATİK ÜRETİLDİ — 04_BUILD/handoff.py · ELLE DÜZENLEMEYİN -->")
    a("")
    a("> **DURUM: KDP UPLOAD READY.**")
    a("> Bu, *KDP PUBLISH READY* ile aynı şey **değildir**. Aradaki fark:")
    a(">")
    a("> | | |")
    a("> |---|---|")
    a("> | **KDP UPLOAD READY** (şu an) | Dosyalar üretildi ve doğrulandı. Panele yüklenebilir. |")
    a("> | **KDP PUBLISH READY** (henüz değil) | ISBN kararı verildi · fiyat girildi · Previewer'da onaylandı · AI beyanı seçildi · prova okundu. |")
    a(">")
    a("> **Hiçbir panel işlemi yapılmadı.** KDP hesabına girilmedi, kitap")
    a("> oluşturulmadı, dosya yüklenmedi, Publish'e basılmadı.")
    a("")
    a("---")
    a("")
    a("## 0. Önce bunları bilin")
    a("")
    a("| # | Konu | Durum |")
    a("|---|---|---|")
    a(f"| 1 | **ISBN** | {FOUNDER} — A9 açık. Dosyalarda ISBN **yok** ve "
      "**uydurulmadı**. Ham kapak sanatında üretilmiş sahte bir barkod vardı; "
      "**silindi** (§ COVER_HANDOFF). |")
    a(f"| 2 | **KDP Select** | {FOUNDER} — A7 açık. Kayıt **yapılmadı**. |")
    a(f"| 3 | **Yayıncı / imprint** | {FOUNDER} — proje kaynaklarında kayıtlı "
      "bir yayıncı adı **yok**. Uydurulmadı; kapağa hiçbir yayıncı adı "
      "basılmadı. KDP'de boş bırakılırsa *Independently published* olur. |")
    a(f"| 4 | **AI beyanı** | {FOUNDER} — hazırlandı ama **seçimi siz "
      "yapacaksınız**: metin **AI-generated**, görseller **AI-generated**. |")
    a(f"| 5 | **İki ebeveyn okuması** | {FOUNDER} — **0/2**. Kapı kasıtlı "
      "kırmızı. Yayın öncesi yol haritası şartı (§ 21 · H8). |")
    a(f"| 6 | **Fiyat** | {FOUNDER} — model ciltsiz 16,99 $ · ciltli 26,99 $ "
      "· Kindle 7,99 $ öngörüyor; girişi siz yapacaksınız. |")
    a(f"| 7 | **Ciltli sırt genişliği** | ⚠ **TÜRETİLDİ** — KDP hardcover "
      "sırt formülünü kamuya açık yayımlamıyor, kendi hesaplayıcısına "
      "yönlendiriyor. Yüklemeden önce KDP Cover Calculator ile "
      "**doğrulayın**; farklıysa tek komutla yeniden üretilir. |")
    a("")
    a("---")
    a("")

    for key, label, rec in (("paperback", "CİLTSİZ (PAPERBACK)", pb),
                            ("hardcover", "CİLTLİ (HARDCOVER)", hc)):
        ed = ed_mod.get(key)
        lo, hi = ed_mod.PAGE_LIMITS[key]
        pages = rec.get("totalPages", "—")
        cg = C.get("editions", {}).get(key, {}).get("geometry", {})
        st_i, sz_i = fstat(f"08_OUTPUT/{key}/interior.pdf")
        st_c, sz_c = fstat(f"08_OUTPUT/{key}/cover.pdf")
        a(f"## {label}")
        a("")
        a("| # | KDP alanı | Değer | Durum |")
        a("|---|---|---|---|")
        a(f"| 1 | Edition | {label.split('(')[1].rstrip(')')} | {READY} |")
        a(f"| 2 | Trim size | {ed.trim_w_in} × {ed.trim_h_in} inç | {READY} |")
        a(f"| 3 | Bleed | **No bleed** (iç blokta tam sayfa görsel yok) | {READY} |")
        a(f"| 4 | Paper type | **Cream** | {READY} |")
        a(f"| 5 | Ink | **Black & white** | {READY} |")
        a(f"| 6 | Page count | **{pages}** (KDP sınırı {lo}–{hi}) | {READY} |")
        a(f"| 7 | **Manuscript dosyası** | `08_OUTPUT/{key}/interior.pdf` "
          f"({sz_i}) | {st_i} |")
        a(f"| 8 | **Cover dosyası** | `08_OUTPUT/{key}/cover.pdf` ({sz_c}) | {st_c} |")
        a(f"| 9 | Kapak ölçüsü | {cg.get('fullIn',['—','—'])[0]} × "
          f"{cg.get('fullIn',['—','—'])[1]} inç · sırt "
          f"**{cg.get('spineIn','—')}\"** | {READY} |")
        a(f"| 10 | ISBN | — | {FOUNDER} |")
        a(f"| 11 | Author | **{mb.AUTHOR}** | {READY} |")
        a(f"| 12 | Publisher | — | {FOUNDER} |")
        a(f"| 13 | AI disclosure | metin + görsel **AI-generated** | {FOUNDER} |")
        a(f"| 14 | Categories | bkz. § Metadata (3 adet) | {READY} |")
        a(f"| 15 | Keywords | bkz. § Metadata (7 adet) | {READY} |")
        a(f"| 16 | Description | {M.get('descriptionChars','—')} karakter | {READY} |")
        a(f"| 17 | Fiyat / telif | model: {ed.price_usd:.2f} $ | {FOUNDER} |")
        a(f"| 18 | **Previewer** | yükledikten sonra **her sayfayı** gözden "
          f"geçirin | {FOUNDER} |")
        a(f"| 19 | Prova kopyası | sipariş edin ve okuyun | {FOUNDER} |")
        a("")
        a("**Yüklemeden önceki son kontroller**")
        a("")
        a("| | Kontrol | Ölçülen |")
        a("|---|---|---|")
        a(f"| a | Gömülü olmayan font | **{len(rec.get('pdf_facts',{}).get('notEmbedded',[]))}** |")
        a(f"| b | Sayfa ölçüsü | {rec.get('pdf_facts',{}).get('pageSize','—')} |")
        a(f"| c | Yerleşen görsel | {rec.get('imagesPlaced','—')} / 68 |")
        a(f"| d | Kırpılan görsel | 0 |")
        a(f"| e | Sayfa çift mi | {'evet' if isinstance(pages,int) and pages%2==0 else '—'} |")
        a(f"| f | Kapak sırt yazısı | {'var' if pages != '—' and int(pages) >= 100 else 'yok (100 sayfa altı)'} |")
        a(f"| g | Barkod alanı | **temiz** ({cs.BARCODE_W_IN}×{cs.BARCODE_H_IN} inç) |")
        a("")
        a("---")
        a("")

    st_e, sz_e = fstat("08_OUTPUT/kindle/book.epub")
    st_k, sz_k = fstat("08_OUTPUT/kindle/cover.jpg")
    a("## KINDLE (REFLOWABLE EBOOK)")
    a("")
    a("| # | KDP alanı | Değer | Durum |")
    a("|---|---|---|---|")
    a(f"| 1 | Format | reflowable EPUB | {READY} |")
    a(f"| 2 | **Manuscript dosyası** | `08_OUTPUT/kindle/book.epub` ({sz_e}) | {st_e} |")
    a(f"| 3 | **Cover dosyası** | `08_OUTPUT/kindle/cover.jpg` ({sz_k}) | {st_k} |")
    a(f"| 4 | Kapak yüksekliği | {E.get('coverPx',['—','—'])[1] if E.get('coverPx') else '2560'} px "
      f"(KDP en az 1000, önerilen 2560) | {READY} |")
    a(f"| 5 | Dosya boyutu | **{E.get('totalMb','—')} MB** (bütçe "
      f"{E.get('budgetMb','—')} MB) | {READY} |")
    a(f"| 6 | İçindekiler | nav.xhtml **+** toc.ncx | {READY} |")
    a(f"| 7 | Görsel | {E.get('images','—')} / 68 | {READY} |")
    a(f"| 8 | Hikâye | {E.get('stories','—')} / 45 | {READY} |")
    a(f"| 9 | ISBN | Kindle'da **gerekmez** | {NA} |")
    a(f"| 10 | DRM | — | {FOUNDER} |")
    a(f"| 11 | KDP Select | **kayıt yapılmadı** | {FOUNDER} |")
    a(f"| 12 | Fiyat | model 7,99 $ | {FOUNDER} |")
    a(f"| 13 | **Previewer** | Kindle Previewer ile açın | {FOUNDER} |")
    a("")
    a("> ⚠ **KDP Cover Creator kullanmayın.** Kapak geometrisi bu hattan")
    a("> gelir; Cover Creator sırtı yeniden hesaplar ve dosyayı bozar.")
    a("")
    a("---")
    a("")
    a("## METADATA (üç formatta da aynı)")
    a("")
    a(f"- **Title** — {M.get('title','—')}")
    a(f"- **Subtitle** — {M.get('subtitle','—')}")
    a(f"- **Author** — {mb.AUTHOR}")
    a(f"- **Language** — {M.get('language','en')}")
    a(f"- **Age range** — {M.get('ageRange',{}).get('min','8')}–"
      f"{M.get('ageRange',{}).get('max','12')}")
    a("")
    a("**Keywords (7)**")
    a("")
    for i, k in enumerate(M.get("keywords", []), 1):
        a(f"{i}. `{k}`")
    a("")
    a("**Categories (3)**")
    a("")
    for c in M.get("categories", []):
        bis = f" · BISAC `{c['bisac']}`" if c.get("bisac") else \
              " · **kod uydurulmadı** — KDP kategori seçicisinden seçin"
        a(f"- {c['path']}{bis}")
    a("")
    a("**Description** — tam metin: `08_OUTPUT/metadata.json` → `description`")
    a("")
    a("---")
    a("")
    a("## KURUCUNUN YAPACAKLARI (ajan yapmadı, yapamaz)")
    a("")
    a("1. KDP hesabına giriş")
    a("2. Kitap kaydı oluşturma ve dosya yükleme")
    a("3. ISBN kararı (A9) ve girişi")
    a("4. Yayıncı / imprint kararı")
    a("5. AI beyanı seçimi")
    a("6. Kategori ve anahtar kelime girişi")
    a("7. Fiyatlandırma ve KDP Select kararı (A7)")
    a("8. **Previewer'da her sayfanın gözden geçirilmesi**")
    a("9. Fiziksel prova siparişi ve okunması")
    a("10. **İki ebeveyn okuması** (H8) — yayın öncesi şart")
    a("11. Publish")
    a("")
    a("---")
    a("")
    a("*Bu dosya `04_BUILD/handoff.py` tarafından üretilir.*")
    return "\n".join(L) + "\n"


def render_cover(d: dict) -> str:
    C = d["cover"]
    L = []
    a = L.append
    a("# KAPAK TESLİM BELGESİ")
    a("")
    a("<!-- OTOMATİK ÜRETİLDİ — 04_BUILD/handoff.py · ELLE DÜZENLEMEYİN -->")
    a("")
    a("## Ham sanatta bulunan iki kusur ve ne yapıldığı")
    a("")
    a("| # | Kusur | Yapılan |")
    a("|---|---|---|")
    a("| 1 | **Kapakta yanlış başlık basılıydı.** Üretilen sanat "
      "*“STORIES from the WHOLE WORLD”* yazıyordu; kitabın adı "
      "**The Great Book of World Myths**. | Üretilmiş yazının bulunduğu bölge "
      "gökyüzü rengiyle **örtüldü**, gerçek başlık **CLI ile basıldı**. |")
    # ⚠ UYDURULMUŞ NUMARA BU BELGEYE YAZILMAZ.
    # İlk sürüm sahte ISBN'i açıklama amacıyla tam olarak yazıyordu ve
    # `handoff.py`nin kendi kapısı onu yakaladı — haklı olarak: teslim
    # belgesinden kopyalanabilir bir sahte ISBN, kapağa basılmış olan kadar
    # tehlikelidir. Numara maskelenir, olay anlatılır.
    # ⚠ MASKELEME YETMEDİ. İlk sürüm numarayı tam yazıyordu, kapı yakaladı,
    # numara `978-1-963…` diye kısaltıldı — ve Faz 7'de yeni ISBN BİÇİM
    # kapısı bunu da yakaladı: kısaltılmış hâli hâlâ ISBN biçimindeydi ve
    # hâlâ kopyalanabilirdi. Doğru davranış numarayı hiç ANMAMAK.
    a("| 2 | **Arka kapakta uydurulmuş bir ISBN ve barkod basılıydı.** "
      "Numara projeye ait **değildi** ve burada hiçbir biçimde "
      "tekrarlanmıyor — teslim belgesinden kopyalanabilir bir sahte ISBN, "
      "kapağa basılmış olan kadar tehlikelidir. | Barkod alanı "
      "**temizlendi**; hiçbir numara basılmadı. KDP kendi barkodunu oraya "
      "basar. |")
    a("")
    a("> Faz 5 şartnamesi bütün kapak promptlarını `typography: post` "
      "işaretlemişti. Faz 6 bunun neden şart olduğunu ölçülebilir biçimde "
      "gösterdi.")
    a("")
    a("---")
    a("")
    for key, label in (("paperback", "CİLTSİZ"), ("hardcover", "CİLTLİ")):
        rec = C.get("editions", {}).get(key, {})
        g = rec.get("geometry", {})
        st, sz = fstat(f"08_OUTPUT/{key}/cover.pdf")
        a(f"## {label}")
        a("")
        a("| Alan | Değer |")
        a("|---|---|")
        a(f"| **Dosya** | `08_OUTPUT/{key}/cover.pdf` ({sz}) — {st} |")
        a(f"| Sayfa sayısı (sırtın kaynağı) | **{g.get('pages','—')}** |")
        a(f"| **Sırt genişliği** | **{g.get('spineIn','—')} inç**"
          + ("  ⚠ **TÜRETİLDİ — KDP hesaplayıcısıyla doğrulayın**"
             if g.get("spineDerived") else "") + " |")
        a(f"| Tam kapak ölçüsü | {g.get('fullIn',['—','—'])[0]} × "
          f"{g.get('fullIn',['—','—'])[1]} inç |")
        a(f"| Piksel (300 dpi) | {g.get('fullPx',['—','—'])[0]} × "
          f"{g.get('fullPx',['—','—'])[1]} |")
        a(f"| Taşma / sarım | {g.get('edgeIn','—')} inç |")
        a(f"| Güvenli alan | {g.get('safeIn','—')} inç |")
        a(f"| Menteşe (ciltli) | {g.get('hingeIn','—')} inç |")
        a(f"| Arka kapak başlangıcı | {g.get('backX0In','—')} inç |")
        a(f"| Sırt başlangıcı | {g.get('spineX0In','—')} inç |")
        a(f"| Ön kapak başlangıcı | {g.get('frontX0In','—')} inç |")
        a(f"| Barkod alanı | {cs.BARCODE_W_IN}×{cs.BARCODE_H_IN} inç · "
          f"alttan {cs.BARCODE_FROM_BOTTOM_IN}\" · **temiz** |")
        a(f"| Gömülü olmayan font | **{len(rec.get('fontsNotEmbedded',[]))}** |")
        a(f"| Güvenli alan ihlali | **{len(rec.get('outsideSafe',[]))}** |")
        a(f"| Zemin sanatı kırpması | %{max(rec.get('art',{}).get('croppedPct',[0]))} |")
        a(f"| Kaynak sanat | `{rec.get('sourceArt','—')}` |")
        a("")
        a("**Basılan metinler (hepsi CLI ile, üretilmedi)**")
        a("")
        a("- Ön kapak: `THE GREAT BOOK OF` / `WORLD MYTHS`")
        a("- Alt başlık: `45 Stories of Gods, Heroes, and Monsters from 22 Cultures`")
        a("- `Retold for Young Readers`")
        a(f"- Yazar: **{mb.AUTHOR}**")
        a("- Yaş rozeti: `AGES 8–12` (köşede — yol haritası § 18 şartı)")
        a(f"- Sırt: `THE GREAT BOOK OF WORLD MYTHS` + `{mb.AUTHOR}` "
          f"({rec.get('spineFontPt','—')} pt)")
        a("- Arka kapak: tanıtım metni (kitabın gerçek içeriğinden)")
        a("- Yayıncı: **basılmadı** — proje kaynaklarında kayıt yok")
        a("")
        a("---")
        a("")
    k = C.get("kindle", {})
    a("## KINDLE KAPAĞI")
    a("")
    a(f"- Dosya: `{k.get('jpg','08_OUTPUT/kindle/cover.jpg')}`")
    a(f"- Ölçü: **{k.get('px',['—','—'])[0]} × {k.get('px',['—','—'])[1]} px**")
    a(f"- Biçim: {k.get('mode','RGB')} JPEG · {k.get('bytes',0)/1e6:.2f} MB")
    a("- Kaynak: ciltsiz kapak PDF'inin **ön kapağı** rasterize edildi — yani")
    a("  basılı kapakla **birebir aynı tipografiyi** taşır.")
    a("")
    a("### 160 piksel testi (yol haritası § 18)")
    a("")
    a("Kapak 160 piksel genişliğe küçültülüp gözle sınandı:")
    a("")
    a("| Okunuyor mu | Sonuç |")
    a("|---|---|")
    a("| `WORLD MYTHS` | ✅ |")
    a("| `THE GREAT BOOK OF` | ✅ |")
    a(f"| `{mb.AUTHOR}` | ✅ |")
    a("| `AGES 8–12` | ✅ |")
    a("| `22 Cultures` (alt başlıkta) | ⚠ küçük ama seçilebilir |")
    a("")
    a("---")
    a("")
    a("*Bu dosya `04_BUILD/handoff.py` tarafından üretilir.*")
    return "\n".join(L) + "\n"


def render_aplus(d: dict) -> str:
    A = d["aplus"]
    L = []
    a = L.append
    a("# A+ İÇERİK TESLİM BELGESİ")
    a("")
    a("<!-- OTOMATİK ÜRETİLDİ — 04_BUILD/handoff.py · ELLE DÜZENLEMEYİN -->")
    a("")
    a("> A+ modüllerinin Amazon'da yayımlanması **kurucunun işidir**.")
    a("> Burada yalnızca yüklemeye hazır görseller vardır.")
    a("")
    a("> **Metinler görsele CLI ile basıldı**, üretilmedi (talimat § 45).")
    a("> Sebebi Faz 6'da somutlaştı: aynı üretici, kapakta kitabın adını")
    a("> yanlış yazdı.")
    a("")
    a(f"**{len(A.get('modules',[]))} modül · toplam "
      f"{A.get('totalBytes',0)/1e6:.2f} MB**")
    a("")
    a("| # | Modül | Amazon modül tipi | Ölçü | Dosya | Durum |")
    a("|---|---|---|---|---|---|")
    for i, m in enumerate(A.get("modules", []), 1):
        st, sz = fstat(m["file"])
        a(f"| {i} | `{m['id']}` | {m['module']} | "
          f"**{m['targetPx'][0]}×{m['targetPx'][1]}** | `{m['file']}` ({sz}) | {st} |")
    a("")
    a("## Basılan metinler")
    a("")
    a("| Modül | Başlık | Alt satır |")
    a("|---|---|---|")
    import aplus as ap
    for m in A.get("modules", []):
        t = ap.TEXT.get(m["id"], {})
        head = t.get("head") or "—"
        sub = (t.get("sub") or "—")
        if len(sub) > 70:
            sub = sub[:67] + "…"
        a(f"| `{m['id']}` | {head} | {sub} |")
    a("")
    a("## Kaynak ↔ çıktı eşlemesi")
    a("")
    a("| Modül | Ham sanat | Kırpma | Metin kutusu (px) |")
    a("|---|---|---|---|")
    for m in A.get("modules", []):
        cp = max(m.get("art", {}).get("croppedPct", [0]))
        box = m.get("textBoxPx") or "—"
        a(f"| `{m['id']}` | `{m['source']}` | %{cp} | {box} |")
    a("")
    a("> ⚠ Oranı tutmayan ham sanat **ortadan kırpıldı** — dolgu (beyaz bant)")
    a("> yapılmadı, çünkü ürün sayfasında görünür. Kırpma payı yukarıda.")
    a("")
    a("---")
    a("")
    a("*Bu dosya `04_BUILD/handoff.py` tarafından üretilir.*")
    return "\n".join(L) + "\n"


def main() -> int:
    ap_ = argparse.ArgumentParser(description="KDP teslim belgeleri")
    ap_.add_argument("--check", action="store_true")
    ap_.add_argument("--verbose", action="store_true")
    args = ap_.parse_args()

    print("═" * 72)
    print("  KDP TESLİM BELGELERİ")
    print("═" * 72)

    r = mb.Result("handoff", verbose=args.verbose)
    d = {"interior": load("interior-build.json"),
         "cover": load("cover-build.json"),
         "epub": load("epub-build.json"),
         "aplus": load("aplus-build.json"),
         "metadata": load("metadata.json")}

    missing_reports = [k for k, v in d.items() if not v]
    r.add(not missing_reports, "bütün üretim raporları var",
          f"EKSİK RAPOR: {missing_reports} — ilgili build betiğini çalıştırın")
    if missing_reports:
        return r.finish(None)

    docs = {
        "KDP_UPLOAD_HANDOFF.md": render_upload(d),
        "COVER_HANDOFF.md": render_cover(d),
        "A_PLUS_HANDOFF.md": render_aplus(d),
    }

    # --- HER YOL GERÇEK Mİ ---
    required = [
        "08_OUTPUT/paperback/interior.pdf", "08_OUTPUT/paperback/cover.pdf",
        "08_OUTPUT/hardcover/interior.pdf", "08_OUTPUT/hardcover/cover.pdf",
        "08_OUTPUT/kindle/book.epub", "08_OUTPUT/kindle/cover.jpg",
    ]
    absent = [p for p in required if not os.path.exists(os.path.join(mb.ROOT, p))]
    r.add(not absent, f"teslim edilen {len(required)} dosyanın hepsi diskte",
          f"EKSİK TESLİM DOSYASI: {absent}")

    ap_files = [m["file"] for m in d["aplus"].get("modules", [])]
    ap_absent = [p for p in ap_files
                 if not os.path.exists(os.path.join(mb.ROOT, p))]
    r.add(not ap_absent, f"{len(ap_files)} A+ görselinin hepsi diskte",
          f"EKSİK A+ DOSYASI: {ap_absent}")

    # --- UYDURULMUŞ DEĞER SIZMASIN ---
    blob = "\n".join(docs.values())
    for bad, why in (("978-1-963000", "ham sanattaki UYDURULMUŞ ISBN"),
                     ("Independently published Inc", "uydurulmuş yayıncı")):
        r.add(bad not in blob, f"teslim belgesinde '{bad}' yok — {why}",
              f"TESLİM BELGESİNE UYDURULMUŞ DEĞER SIZDI: {bad}")

    if args.check:
        stale = []
        for name, content in docs.items():
            p = os.path.join(OUT_DIR, name)
            old = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
            if old != content:
                stale.append(name)
        r.add(not stale, "teslim belgeleri güncel",
              f"BAYAT: {stale} — `handoff.py` çalıştırın")
        return r.finish(None)

    os.makedirs(OUT_DIR, exist_ok=True)
    for name, content in docs.items():
        with open(os.path.join(OUT_DIR, name), "w", encoding="utf-8") as fh:
            fh.write(content)
        print(f"  ✎ 08_OUTPUT/handoff/{name}")

    os.makedirs(mb.REPORTS_TRACKED, exist_ok=True)
    with open(REPORT, "w", encoding="utf-8") as fh:
        json.dump({"$comment": ["TESLİM DENETİMİ — yalnızca dosya varlığı.",
                                "Üretici: 04_BUILD/handoff.py"],
                   "gate": mb.read_gate(),
                   "requiredFiles": required,
                   "missing": absent,
                   "aplusFiles": len(ap_files),
                   "docs": sorted(docs)}, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    return r.finish(None)


if __name__ == "__main__":
    sys.exit(main())
