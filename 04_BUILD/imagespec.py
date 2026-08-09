"""
GÖRSEL ŞARTNAMESİ — 68 GÖRSELİN TEK DOĞRULUK KAYNAĞI
================================================================================
İLLÜSTRASYON BU PROJEDE ZORUNLUDUR (karar K4).

Yol haritası bunu bir öneri olarak değil, FİYAT MODELİNİN DAYANAĞI olarak
karara bağlamış:

    İllüstrasyon: "45 bölüm açılış çizimi + 22 kültür vinyeti, SİYAH-BEYAZ"
    Gerekçe: "Renkli baskı bu sayfa sayısında maliyeti 15,95 $'a çıkarır —
              fiyatı 39,99 $'a iter, KATEGORİDEN ÇIKARIR."
    Harita: "1 dünya haritası (22 kültürün konumu) — ön veya arka iç kapak"
    Gerekçe: "Ebeveynin 'eğitici' algısını tek görselde kurar."

45 + 22 + 1 = 68.

--------------------------------------------------------------------------------
ÜSLUP GÖVDESİ TEK YERDE DURUR (Bestiarium D7 / karar K16)
--------------------------------------------------------------------------------
Prompt kütüphanesi ÜRETİLİR, elle yazılmaz. Üslup gövdesi değişirse 68
prompt birlikte değişir. "Tek çizgi dili" şartı ancak böyle tutulabilir.

--------------------------------------------------------------------------------
BESTIARIUM'DAN TAŞINMAYAN ŞEY
--------------------------------------------------------------------------------
Bestiarium'un çizgi dili ANTİKA GRAVÜRDÜR ve 120 plakanın aynı tarama
geometrisinde olması ürünün kendisidir; ölçümü tarama açısı ve darbe/periyot
üzerineydi. Bu kitabın çizgi dili ÇOCUK İLLÜSTRASYONUDUR. Ölçülecek şey
tarama frekansı değil: kadraj, kontrast, mürekkep yoğunluğu ve BASKIDA
OKUNABİLİRLİK.
"""

from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mythbook as mb


# =============================================================================
# 1. ÜSLUP GÖVDESİ — 68 PROMPTTA AYNI
# =============================================================================
# Bu dizeler prompt kütüphanesinin imzasıdır. make_prompts.py --check
# hepsinin 68 promptta da geçtiğini kanıtlar; geçmiyorsa "tek çizgi dili"
# şartı ihlal edilmiş demektir ve CI kırmızı yanar.

# ⚠ OLUMSUZ LİSTE UZADIKÇA TERSİNE ÇALIŞIR (Faz 5 ölçümü).
# İkinci deneme "no cream or beige tint, no sepia, no toned background"
# ekledi ve model tam olarak KAHVERENGİ BİR ZEMİN GRADYANI çizdi: mürekkep
# yoğunluğu %60,6, orta ton %42,8. Modern görsel modelleri olumsuzu zayıf,
# OLUMLUYU güçlü işler; istenmeyen şeyi adıyla anmak onu çağırır.
#
# Bu yüzden zemin kuralı artık OLUMLU ve ÖNDE: "flat pure white background".
# Olumsuz liste yalnızca YAŞ POLİTİKASI kısıtlarını taşır (AGE_POLICY § 2.17
# onları zorunlu kılar) ve üslup pazarlığı olumlu tarafta yapılır.
STYLE_BODY = (
    "black and white pen-and-ink line drawing for a children's book on a "
    "flat pure white background, clean confident outlines of varied weight, "
    "the white of the paper is the only background there is, "
    "open uncluttered composition, warm and inviting rather than frightening, "
    "shadows suggested by a few short separated strokes, never by filling an "
    "area, so the drawing stays crisp when printed small"
)

STYLE_SIGNATURE = "black and white pen-and-ink line drawing for a children's book"

# AGE_POLICY § 2.17 doğrudan buraya iner. "Look Inside"da görünen ilk şey
# bir illüstrasyondur ve ebeveynin ilk izlenimini o kurar (yol haritası R4).
NEGATIVE_PROMPT = (
    "no blood, no gore, no wounds, no corpses, no severed limbs, "
    "no visible entrails, no torture, no nudity, no sexualised figures, "
    "no terrified faces in close-up, no photorealism, no colour, "
    "no grey wash, no digital gradients, no text, no lettering, "
    "no watermark, no signature, no modern objects, no cultural pastiche, "
    "no generic fantasy armour, no stereotyped features, "
    # ⚠ FAZ 5 — KINDLE BÜTÇESİNİN KÖK SEBEBİ.
    # İlk teslimatın hikâye görselleri kalem gölgelemesiyle geldi: piksellerin
    # %13,9'u orta tonda (vinyetlerde %1,8, şartnameye uyan kurguda %0).
    # Sürekli ton, PNG süzgeçlerinin kestiremediği bir gürültüdür ve Kindle
    # payını 3,0 MB bütçeye karşı 5,62 MB'ye çıkardı — ama o sınıf artık
    # OLUMSUZ tarafta değil, STYLE_BODY'nin OLUMLU zemin kuralıyla kapatılıyor
    # (yukarıdaki ölçüme bakın: olumsuz saymak kahverengi zemin ÜRETTİ).
    "no engraving texture"
)

# Her promptta bulunması zorunlu iki teknik işaret
#
# ⚠ FAZ 5 KÖK SEBEP DÜZELTMESİ.
# Burada eskiden `"upper half of a 6x9 inch page"` yazıyordu ve üretici tam
# olarak onu çizdi: 1024×1536 (yani BİREBİR 6:9) bir SAYFA, çizim üstte,
# altı boş. 45 hikâye görselinin tamamı böyle geldi.
#
# Kusur teslimatta değil, PROMPTTA'ydı. İşaret, görselin İÇİNDE duracağı
# sayfayı tarif ediyordu; oysa üreticiden istenen şey SAYFA DEĞİL, GÖRSELİN
# KENDİSİDİR. Yeni işaret çizimin kendi geometrisini tarif eder ve "sayfa"
# kelimesini hiç kullanmaz — üreticiye çizecek bir sayfa verilirse sayfa
# çizer.
#
# Kenar payı bilinçli olarak istenir: `images.measure()` dış %3'lük bantta
# koyu piksel ararsa kadrajı reddeder ve teslimatın 44/45'i tam o yüzden
# düşmüştü (çerçeve kenara yapışıyordu).
COMPOSITION_MARKER = (
    "a standalone horizontal illustration in 3:2 landscape proportions, "
    "the whole scene composed inside the frame with a clean margin of white "
    "paper on all four sides"
)
VIGNETTE_MARKER = "small spot illustration, no frame"


# =============================================================================
# 2. GÖRSEL TÜRLERİ
# =============================================================================

KINDS = {
    "story": {
        "count": mb.STORY_TARGET,
        "prefix": "story",
        "purpose": "Hikâye açılış çizimi — sayfanın üst yarısı",
        "placement": "Hikâyenin ilk sayfasının üst yarısı",
        "aspect": "3:2 (yatay)",
        "raw_px": (2400, 1600),
        "generator_px": (1536, 1024),
        "print_dpi": 600,
        "print_px": (3000, 2000),
        "kindle_px": (1200, 800),
        "web_px": (1400, 933),
        "marker": COMPOSITION_MARKER,
    },
    "culture": {
        "count": mb.CULTURE_TARGET,
        "prefix": "culture",
        "purpose": "Kültür vinyeti — kültür kartında",
        "placement": "Kültür kartı (DECISIONS § A4)",
        "aspect": "1:1 (kare)",
        "raw_px": (1600, 1600),
        "generator_px": (1024, 1024),
        "print_dpi": 600,
        "print_px": (1800, 1800),
        "kindle_px": (800, 800),
        "web_px": (900, 900),
        "marker": VIGNETTE_MARKER,
    },
    "map": {
        "count": 1,
        "prefix": "map",
        "purpose": "Dünya haritası — 22 kültürün konumu",
        "placement": "Ön veya arka iç kapak (açık sayfa)",
        # ⚠ 2:1 → 3:2 · ÖLÇÜLMÜŞ DÜZELTME (Faz 5).
        # Eski değer "2:1 (açık sayfa)" idi ve bu kitapta HİÇBİR GERÇEK
        # GEOMETRİYE karşılık gelmiyordu:
        #     açık sayfa TRIM      : 12,0 × 9,0  = 1,333
        #     açık sayfa BASILABİLİR: 10,75 × 7,5 = 1,433
        #     şartnamenin dediği    :             2,000
        # 2:1 bir açık sayfayı değil, iki kat daha geniş bir şeyi tarif
        # ediyordu; o oranda üretilen bir harita sayfaya yerleşirken
        # yükseklikte yarı yarıya küçülürdü. 3:2 (1,500) her iki gerçek
        # ölçüye de 2:1'den daha yakındır ve üreticinin verebildiği orandır.
        #
        # BASKI ÇÖZÜNÜRLÜĞÜ DÜŞÜRÜLMEDİ: `print_px` hâlâ 600 dpi hedefidir
        # (6450 px ÷ 600 = 10,75 inç, yani basılabilir açık sayfanın tam eni).
        "aspect": "3:2 (açık sayfa)",
        "raw_px": (3600, 2400),
        "generator_px": (1536, 1024),
        "print_dpi": 600,
        "print_px": (6450, 4300),
        "kindle_px": (1200, 800),
        "web_px": (2000, 1333),
        "marker": "double-page spread map",
    },
}

# -----------------------------------------------------------------------------
# GENERATOR_PX — ÜRETİCİNİN GERÇEKTEN VEREBİLDİĞİ BOYUT (Faz 5 bulgusu)
# -----------------------------------------------------------------------------
# `raw_px` ŞARTNAMEDİR: 600 dpi baskı için gereken piksel. `generator_px` ise
# kurucunun elindeki üreticinin (GPT Image) GERÇEKTEN ÜRETEBİLDİĞİ en yakın
# boyuttur — o üretici yalnızca 1024×1024, 1536×1024 ve 1024×1536 verir.
#
# ⚠ İKİSİ ÇELİŞİYOR VE BU BİR KAPI KUSURUDUR, ASSET KUSURU DEĞİL.
# `raw_px` hiçbir kurucu teslimatının GEÇEMEYECEĞİ bir eşiktir: 2400 px
# genişlik istenmiş, üretici en fazla 1536 verebiliyor. Yani "asgari
# çözünürlük" kuralı, DOĞRU ÜRETİLMİŞ 68 GÖRSELİN TAMAMINI reddeder —
# Bestiarium'un B1 kusurunun birebir aynısı, bu sefer şartname tarafında.
#
# Bu dosya kuralı TEK BAŞINA DEĞİŞTİRMEZ. Çelişki ölçülür, raporlanır ve
# kurucu kararına bırakılır (Faz 5 raporu § açık bağımlılıklar). Buradaki
# `generator_px` yalnızca ÇELİŞKİYİ MAKİNE OKUNUR yapar.
GENERATOR = "GPT Image"
GENERATOR_NATIVE_SIZES = ((1024, 1024), (1536, 1024), (1024, 1536))

TOTAL = sum(k["count"] for k in KINDS.values())

# Üretim formatları — RAW ASLA ÜZERİNE YAZILMAZ (karar K5)
FORMATS = {
    "print":  {"dir": "print",  "ext": "tif",  "mode": "L", "dpi": 600,
               "note": "Baskı iç bloğu — gri tonlama TIFF, sıkıştırmasız"},
    "kindle": {"dir": "kindle", "ext": "png",  "mode": "1", "dpi": 300,
               "bilevel": True, "threshold": 190,
               "note": "Kindle — 1 bit çizgi sanatı (3,0 MB toplam bütçe)"},
    "web":    {"dir": "web",    "ext": "webp", "mode": "L", "dpi": 144,
               "note": "A+ içerik ve pazarlama — kayıpsız"},
}

# -----------------------------------------------------------------------------
# KINDLE NEDEN 1 BİT (Faz 5 ölçümü)
# -----------------------------------------------------------------------------
# Hat, Kindle türevini üç faz boyunca `quantize(colors=16)` ile üretti. O seçim
# Bestiarium D27'den geliyordu — "kayıplı kodlayıcı ince taramada en kötü
# durumdur" — ve TONLU sanat için doğrudur. Ama bu kitabın şartname dili
# TONLU DEĞİL, ÇİZGİDİR: siyah çizgi, beyaz kâğıt, arada bir şey yok.
#
# Gerçek görselle ölçüldü (story-001, 1200×800):
#     16 renk : 242 KB  → 45 hikâyede 11,2 MB   (bütçe 3,0 MB)
#     1 bit   :  33 KB  → 45 hikâyede  1,5 MB   ✅
# Yedi kat fark ve GÖRÜNÜR KAYIP YOK: eşiklenmiş çıktı, 16 renkli referansla
# yan yana konduğunda çizgileri birebir taşıyor (kıyas görüntüsü Faz 5
# raporunda). Çünkü kaybedilen tek şey kenar yumuşatmasının gri pikselleriydi
# ve Kindle'ın e-ink ekranı onları zaten göstermiyor.
#
# ⚠ `quantize(colors=2)` KULLANILMAZ. Denendi ve BOŞ GÖRÜNTÜ üretti
# (mürekkep 0,0000): median-cut, piksellerin %85'i beyaz olduğu için İKİ
# BEYAZA yakın renk seçiyor. Doğru araç eşiklemedir, nicemleme değil —
# ve bu tam olarak sessizce boş sayfa basacak türden bir kusurdur.
#
# BASKI DEĞİŞMEDİ: iç blok hâlâ 600 dpi GRİ TIFF'tir. 1 bit yalnızca
# Kindle'a aittir.

RAW_FORMAT = "png"
RAW_DIR = os.path.join(mb.ASSETS, "raw")
PROCESSED_DIR = os.path.join(mb.ASSETS, "processed")


# =============================================================================
# 3b. BASKI ÖNCESİ HAZIRLIK — KÂĞIT GÜRÜLTÜSÜNÜN TEMİZLENMESİ
# =============================================================================
# Faz 5 ölçümü: teslim edilen 68 dosyanın "beyaz" zemini beyaz DEĞİLDİR.
# `culture-001` zemininin yalnızca %1,4'ü saf beyaz (255); %93'ü 250–254
# arasına yayılmış bir benek. Bunun üç sonucu var ve üçü de gerçek:
#
#   ① BASKIDA GRİ SİS. 253/255 ≈ %1 gri, siyah-beyaz iç blokta krem kâğıdın
#      üstünde görünür bir tül olur. Üslup gövdesi bunu adıyla yasaklar:
#      "no grey wash, no digital gradients".
#   ② SIKIŞTIRMA ÇÖKER. Her satır komşusundan farklı olduğu için PNG
#      süzgeçleri kestiremez. Kindle payı 10,11 MB çıktı — bütçe 3,0 MB.
#      Yalnızca bu temizlik payı 10,11 → 5,62 MB'ye indiriyor.
#   ③ ÖLÇÜM YANILIR. Histogramda temiz bir beyaz tepe olmadığı için
#      `contrast` ve `bimodality` gerçekte olduğundan kötü ölçülür.
#
# MÜDAHALE EN AZ OLANDIR: eşiğin ÜSTÜ beyaza KENETLENİR, altındaki hiçbir
# ton DEĞİŞMEZ. Doğrusal yeniden ölçekleme (v × 255/wp) denendi ve
# REDDEDİLDİ: orta tonları da açar, yani çizimin kendi gölgesini soldurur.
# Kenetleme yalnızca "kâğıt" dediğimiz şeyi kâğıt yapar.
#
# 246 eşiği ölçümle seçildi: gürültü tabanı 248–254'te oturuyor, gerçek
# çizim tonları ≤240'ta başlıyor; 240–246 aralığı bütün envanterde
# pikselin %2'sinden azını taşıyor. Ham dosya DEĞİŞMEZ — bu adım yalnızca
# türetilmiş formatlara uygulanır.
PREPRESS = {
    "white_point": 246,
    "$comment": "Üstü beyaza kenetlenir; altındaki tonlara DOKUNULMAZ.",
}


# =============================================================================
# 3. KALİTE TOLERANSLARI
# =============================================================================
# Bestiarium B1 dersi: 45° taramada √2 yanlış ölçen bir cetvel, doğru
# çizilmiş 112 plakanın TAMAMINI reddedecekti. Ölçüm KALİBRE EDİLMEDEN
# hiçbir görsel ölçülmez → 05_TESTS/image_selftest.py

TOLERANCES = {
    # Mürekkep yoğunluğu: siyah piksel oranı. Çok düşük = boş sayfa hissi,
    # çok yüksek = baskıda blok hâline gelir ve kâğıt ıslanır.
    "ink_coverage": (0.04, 0.22),
    # ⚠ HARİTA YAPISAL OLARAK DAHA SEYREKTİR ve bu bir kusur değildir.
    # Bir dünya haritası açık okyanus üstünde kıyı çizgisidir; bir hikâye
    # sahnesi kadar mürekkep taşıyamaz. Ölçüm: etiketli ilk harita 0,0394,
    # etiketsiz yeni harita 0,0315 — İKİSİ DE 0,04 tabanının altında, yani
    # taban haritayı BAŞINDAN BERİ reddediyordu ve reddi hiç okunmamıştı,
    # çünkü zaten başka kurallardan da düşüyordu. Taban illüstrasyon için
    # kalibre edilmişti; harita için ayrı bant ölçüyle konur.
    # Vinyet de yapısal olarak seyrektir: BÜYÜK beyaz karede KÜÇÜK bir amblem
    # (şartname zaten "small spot illustration" istiyor). Ölçüm: 22 vinyetin
    # mürekkebi 0,0272–0,0884, medyan 0,046 — altısı 0,04 tabanının altında
    # ve altısı da kusursuz. Taban bir hikâye sahnesi için konmuştu.
    # Boş görsel yakalama görevi burada değil, `asset_inventory.BLANK_INK_FLOOR`
    # (0,005) üzerindedir ve orada duruyor.
    "ink_coverage_by_kind": {"map": (0.015, 0.15), "culture": (0.02, 0.22)},
    # Kontrast: en koyu ve en açık desilin farkı. Düşükse gri görünür.
    "contrast_min": 0.55,
    # Beyaz kenar payı (kadraj): çizim kenara YAPIŞMAMALI.
    "margin_share_min": 0.03,
    # ⚠ "SIFIR PİKSEL" DEĞİL, "BANDIN PAYI" (Faz 5).
    # Eski kural dış %3'lük bantta TEK bir koyu piksel görse reddediyordu.
    # Ölçüm: kabul edilebilir kompozisyonlarda bandın %0,0–1,05'i mürekkepli
    # (bir sütun, bir ağaç, bir kıyı çizgisi kenara değiyor) — kasıtlı kusur
    # kurgusunda (`edge_bleeding`) ise bandın ~%25'i dolu. Aradaki fark iki
    # BÜYÜKLÜK MERTEBESİ; eşik ortasına konur.
    # Baskı güvenliği açısından zaten sonuç yoktur: görsel metin bloğunun
    # İÇİNE yerleşir, yani sayfa kenarından ≥0,5 inç uzaktadır. Kural
    # tipografik bir kadraj tercihidir, taşma koruması değil.
    "margin_ink_max_share": 0.02,
    # İkili eşiğe uzaklık: çocuk illüstrasyonu YARI TONLU DEĞİL, çizgidir.
    # Piksellerin çoğu uçlarda olmalı.
    "bimodality_min": 0.80,
    # En küçük çizgi kalınlığı. Altındaki çizgiler 600 dpi baskıda KAYBOLUR
    # — Bestiarium'un "baskıda okunabilirlik" riskinin çocuk kitabı karşılığı.
    #
    # ⚠ ARTIK ORANDIR, SABİT PİKSEL DEĞİL (Faz 5).
    # Eski değer 3,0 pikseldi ve sessizce "ham dosya 2400 px geniştir"
    # varsayıyordu: 3/2400 = genişliğin binde 1,25'i. Ham 1536 px gelince
    # aynı sabit, FİZİKSEL OLARAK İKİ KAT KALIN bir çizgi istemeye başladı —
    # kural değişmeden şartname sertleşti. Oran, kuralın ASIL niyetini
    # (basılı sayfada ~0,006 inç) ham boyuttan bağımsız korur.
    "min_stroke_px": 3.0,               # geriye dönük uyumluluk için kalır
    "min_stroke_share": 3.0 / 2400.0,   # görsel genişliğinin oranı
    # Ölçüm doğruluğu — kalibrasyon testinin geçme eşiği
    "calibration_error_max": 0.05,
}


# =============================================================================
# 4. KİMLİK NORMALİZASYONU — ham dosya adı ile şartname kimliği arasındaki köprü
# =============================================================================
# HAM DİZİN DEĞİŞMEZDİR (karar K5 · talimat § 32): yeniden adlandırma yasak.
# Ama kurucunun ürettiği dosya adı sıfır dolgusunu kaçırabilir — Faz 5
# teslimatında bir örnek geldi: `story-43.png` (beklenen `story-043.png`).
#
# Çözüm dosyayı DEĞİL, HATTI düzeltmektir: kimlik okunurken normalize edilir.
# Normalizasyon SESSİZ DEĞİLDİR — `canonical_id` sapmayı geri döndürür ve
# envanter raporu her sapmayı ayrı satır olarak basar. Sessiz bir düzeltme,
# ikinci bir doğruluk kaynağı yaratır ve tam da bu projenin "ölü kural"
# dediği şeyi üretir.

_ID_RE = re.compile(r"^(?P<kind>[a-z]+)-(?P<num>\d+)$")


def canonical_id(stem: str) -> tuple[str, bool]:
    """
    `story-43` → (`story-043`, True)   ← sapma vardı
    `story-043` → (`story-043`, False) ← sapma yok

    Tanınmayan biçim olduğu gibi döner; kimliği uydurmak yerine çağıran
    tarafın "tanınmayan tür" kapısına düşmesi gerekir.
    """
    m = _ID_RE.match(stem)
    if not m or m.group("kind") not in KINDS:
        return stem, False
    canon = f"{m.group('kind')}-{int(m.group('num')):03d}"
    return canon, canon != stem


def expected_ids() -> set[str]:
    """Şartnamenin beklediği 68 kimlik."""
    out: set[str] = set()
    for k in KINDS.values():
        out |= {f"{k['prefix']}-{n:03d}" for n in range(1, k["count"] + 1)}
    return out


def raw_path(image_id: str) -> str | None:
    """
    Kanonik kimlikten GERÇEK ham dosya yolunu bulur.

    `os.path.join(RAW_DIR, f"{image_id}.png")` YETMEZ: teslimattaki
    `story-43.png` kanonik `story-043` kimliğine normalize edilir ve o adla
    diskte dosya YOKTUR. Bu yardımcı olmadan her çağıran yeri kendi kontrolünü
    yazar ve biri unutur — nitekim `proof_interior.py` "1 ham görsel eksik"
    diyordu, oysa 68'i de yerindeydi.
    """
    if not os.path.isdir(RAW_DIR):
        return None
    direct = os.path.join(RAW_DIR, f"{image_id}.{RAW_FORMAT}")
    if os.path.exists(direct):
        return direct
    for name in os.listdir(RAW_DIR):
        if not name.lower().endswith(f".{RAW_FORMAT}"):
            continue
        cid, _ = canonical_id(name.rsplit(".", 1)[0])
        if cid == image_id:
            return os.path.join(RAW_DIR, name)
    return None
