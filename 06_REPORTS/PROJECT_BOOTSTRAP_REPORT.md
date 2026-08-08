# PROJE BOOTSTRAP RAPORU

**The Great Book of World Myths** · PROJE 02 · Hacim ve kitle genişletme

> Tarih: 8 Ağustos 2026 · Kapı: `phase0` · Etiket: `v0.0.1`
> Depo: https://github.com/emredogan-cloud/the-great-book-of-world-myths (**PUBLIC**)
> CI: **YEŞİL** — dört iş akışı, dört başarı

---

## 1. Proje keşfi

İki kaynak okundu; hiçbiri özetten değil, **dosyanın kendisinden**.

| Kaynak | Ne için |
|---|---|
| `CODEX_MYTHOLOGICA/AMAZON_KDP_PUBLISHING_COMPANY_ROADMAP_2026.html` | Ürün kararları — BÖLÜM 01.1, 02b, **03 · PROJE 02**, 04, 06, 08, 11 |
| `CODEX_BESTIARIUM/` (v0.4.0, Faz 5 devam ediyor) | **Referans uygulama** — üretim disiplini, kapılar, CI, kayıtlı kusurlar |

**Bestiarium'un hiçbir dosyasına dokunulmadı.** Yalnızca okundu: roadmap,
CHANGELOG (46 karar kaydı), dört iş akışı, `.gitignore`, sızıntı denetimi,
`SOURCING_STANDARD`, `spec.json`, `editions.py`, QA betikleri, `qa_all.sh`.

---

## 2. Master yol haritası bulguları

PROJE 02 bölümü **eksiksiz** okundu ve her kararı çıkarıldı: başlık, alt
başlık, kitle, problem, konumlanma, rekabet, sayfa, trim, üç fiyat, üç
maliyet, üç telif, illüstrasyon, harita, ek malzeme, üslup, üretim saatleri,
takvim, kapak notu, gelir senaryoları, dört risk, uzun vadeli genişleme,
QR/e-posta stratejisi.

**Ayrıca portföy düzeyindeki bağlayıcı kararlar:** seri adı ayrımı
(BÖLÜM 06.2), yazar adı birliği (08.6), KU istisnası (08.5), AI beyanı
zorunluluğu (01.1), yazım hattı ve düşman denetçi rolü (04.2, 04.5).

### Çelişki bulunmadı — ama iki boşluk bulundu

Yol haritası **kendi içinde tutarlıydı**. Ancak iki şeyi **tanımlamıyor**:

| Boşluk | Ne yapıldı |
|---|---|
| 22 kültürün **16'sı** isimsiz | Uydurulmadı → `DECISIONS.md` § **A2**, aday listesi `status: "candidate"` |
| 45 hikâyenin **hiçbiri** sayılmamış | Uydurulmadı → § **A3**, `story_index.json` **kasıtlı olarak boş** |

Talimat § 31 gereği: *"If the master publishing roadmap does not define
something: DO NOT INVENT IT."* Toplam **dokuz açık karar** (A1–A9) kayda
geçti.

---

## 3. Proje 2 spesifikasyonu

Tam liste `PROJECT_CONTEXT.md` § 3 ve `BRIEF.md`'de. Özet:

45 hikâye · 22 kültür · ~950 kelime/hikâye · ~43.000 kelime · ~230 sayfa ·
6×9 inç · siyah-beyaz · 45 açılış + 22 vinyet + 1 harita · ciltsiz 16,99 $ ·
**ciltli 26,99 $ (lansmanla birlikte)** · Kindle 7,99 $ · Temmuz 2027.

Ek malzeme: telaffuz rehberi · "kim kimdir" sözlüğü · her hikâye sonunda
2 satırlık kültürel not.

Üslup: *"Sıcak, hızlı, sahneleyici. Cümleler kısa. Şiddet ve trajedi
saklanmaz ama sahnelenmez."*

---

## 4. Bestiarium dersleri — uygulananlar

Tam belge: `00_CONTEXT/LESSONS_FROM_CODEX_BESTIARIUM.md` (A–J).

### Devralınan mekanizmalar

`.gate` faz kapısı · kapıların kendi testi · standart-kütüphane QA hattı ·
üretilen belge bayatlık kapısı · manuscript sızıntısı (yol + içerik) ·
kaynak katmanları ve doğrulama seviyeleri · sayfa bütçesinin **ölçülerek**
kurulması · üretilen prompt kütüphanesi · karar kaydı disiplini.

### Baştan düzeltilerek gelen kusurlar

| Bestiarium | Kusur | Buradaki hâli |
|---|---|---|
| D32 | `re.I` taraması "long" sözcüğünü hata sandı | Büyük/küçük harfe **duyarlı** |
| D35 | Doğru yazılmış `Lamia`yı reddediyordu | D35 muafiyeti baştan var |
| D34 / Ö1 | `ALLOWED_ECHOES` **ölü kuraldı** | **İki yönlü kapsama** + canlılık kanıtı |
| D28 / Ö2 | `LIVING_TRADITIONS` iki ölü kimlik | Muafiyet listesi **kaldırıldı** (K20) |
| B3 / D20 | `selftest` kendini yanlışlıyordu | `.gate`i okur, sabit seviye varsaymaz |
| B4 | Kurgu üreteci kendini tekrarlıyordu | LCG akış + `--verify` |
| B5 | Desen tablosu kendi kaynağını kirletiyordu | Kaçış dizisi |
| B6 | Satır içi kod "çift boşluk" sanılıyordu | Yer tutucu maskeleme |
| B7 | Negatif `.gitignore` kalıbı çalışmıyordu | `09_ARCHIVE/*` biçimi |
| B8 | Koşullu pip kuran işte `cache: pip` çöküyordu | Önbellek yok |
| B1 | Plaka ölçümü √2 yanlıştı | `image_selftest.py` — hata **%0,00** |

### Taşınmayanlar (çocuk kitabına uygun değil)

Thompson motif kodu kapısı · yedi bölümlü sabit madde yapısı ·
"ünlem = 0" kuralı · yetişkin cümle bandı (14–18) · zorunlu karşılıklı
çapraz referans · gravür tarama geometrisi · `ALLOWED_ECHOES` eski biçimi.

### Bu proje tarafından BULUNAN kusur — Bestiarium'da hâlâ açık

**Ö3.** `CODEX_BESTIARIUM/.gitignore` `06_REPORTS/*.json` diyor;
`plates.yml` → `consistency` işi `06_REPORTS/plate-consistency.json`
denetlemeye çalışıyor. Dosya CI'da **hiçbir zaman bulunamaz** → adım her
koşuda sessizce `exit 0`. *"Tolerans dışı plaka rapora girmişse derleme
kırmızı yanar"* vaadi CI'da **hiç işlemiyor**.

İzolasyon kuralı gereği **düzeltilmedi**, kurucuya bildirildi. Bu projedeki
karşılığı **K18**: denetlenen rapor `06_REPORTS/tracked/` altında depoda
durur, ve `selftest` bunu ayrıca sınar.

---

## 5. Depo

| | |
|---|---|
| URL | https://github.com/emredogan-cloud/the-great-book-of-world-myths |
| Görünürlük | **PUBLIC** |
| Dal | `main` |
| Commit | 3 |
| Takip edilen dosya | 77 |
| Etiket | `v0.0.1` (ön sürüm) |
| Lisans | MIT (**yalnızca yazılım**; kitap metni ve görselleri kapsam dışı) |

---

## 6. Dizin yapısı

```
00_CONTEXT/   bağlam · üslup · editoryal mimari · Bestiarium dersleri
01_RESEARCH/  kültür/hikâye dizinleri · şemalar · araştırma kayıtları
02_MANUSCRIPT/ kitabın prozası — DEPO DIŞINDA (uzaktaki içerik: yalnızca .gitkeep)
03_EDITORIAL/ yaş incelemesi · ebeveyn okumaları · düzeltme kayıtları
04_BUILD/     18 üretim ve doğrulama aracı
05_TESTS/     kapıların kendi testi
06_REPORTS/   ölçümler (tracked/ altındakiler DEPODA durur — K18)
07_ASSETS/    raw/ → processed/ · prompt kütüphanesi
08_OUTPUT/    nihai KDP dosyaları
09_ARCHIVE/   düşürülen malzeme ve gerekçeleri
```

Her dizinin bir üretim amacı var ve `validate_structure.py` ağacı denetliyor.

---

## 7. Araştırma mimarisi

`SOURCING_STANDARD.md` Bestiarium'dan **uyarlandı**; § 5, 6, 7, 8 bu
projeye özgü.

**Devralınan:** 4 kaynak katmanı · 7 doğrulama seviyesi · iki-bağımsız-kaynak
kuralı · sayfa numarası kuralı · "okur gidip bakabilir mi" ölçütü.

**Yeni:**

| # | Kural | Neden |
|---|---|---|
| ① | **Yeniden anlatım ASLA kaynak sayılmaz** | Çocuk rafı yeniden anlatımlarla dolu; onlardan yazmak, başkasının editoryal kararlarını **görmeden devralmaktır** ve raftaki yaygın yanlışlar tam böyle yayılır |
| ② | **Kanonik anlatım + gerekçesi** zorunlu | Bir başvuru cildi "varyantlar vardır" der; bir hikâye **seçmek** zorundadır. *"Daha yumuşak"* tek başına geçersiz gerekçedir — o kültürel sterilizasyondur |
| ③ | **Yaş uyarlaması izi** zorunlu | Bir ebeveyn *"bu hikâyenin sonu böyle değil"* dediğinde verilecek cevap; *"kaynağı bilmiyorduk"* olamaz |
| ④ | **Kısıtlılık taraması muafiyetsiz** | Bestiarium'un D28 kusuru burada 22 kez tekrarlanabilirdi |
| ⑤ | **Telaffuz kaynağı** zorunlu | Yol haritası telaffuzu ticari gerekçeyle koydu; yanlış telaffuz tam o gerekçeyi çürütür |
| ⑥ | **45 düşürülemez** | Bestiarium 120→112 indi; burada 45 ve 22 **alt başlıkta yazıyor** → aday havuzu ≥55 / ≥26 |

Şema: hikâye başına **18 zorunlu alan**, hepsi `validate_spec.py` kapısında.

---

## 8. Editoryal mimari

Dört hareketli hikâye yapısı (Kapı → Baskı → Dönüm → Sonuç), **sabit bölüm
başlığı yok**. Altı bölgesel bölüm önerisi, kültür kartı, ön/arka madde
tasarımı: `00_CONTEXT/EDITORIAL_ARCHITECTURE.md`.

---

## 9. Yaş politikası

`AGE_POLICY.md` — **on yedi kategori**, her biri `ALLOW` / `IMPLY` / `OMIT`
/ `REVIEW`:

şiddet · ölüm · yas · canavarlar · dönüşüm · yamyamlık · kurban · cinsellik ·
istismar · kaçırma · savaş · intikam · ceza · doğaüstü korku · dinî malzeme ·
kültürel hassasiyet · korkutucu imgelem

**On ölçülebilir eşik** `qa_age.py`'ye bağlı. Üç kuralın özellikle
vurgulanması gerekiyor:

- **Kapı iki yönlüdür.** Aşırı sahneleme kadar **aşırı saklama** da kusur:
  ölüm örtmecesi ve zorla mutlu son **kültürel sterilizasyondur**.
- **"Son sayfa kuralı"** — hikâye korkuyla açılabilir ve ilerleyebilir ama
  **korkuyla bitmez**.
- **"Geçmiş zaman tuzağı"** — yaşayan bir inanç için *"inanırdı"* yazılamaz;
  o cümle bir kültürü müzeye koyar. Kapı bunu `livingTradition` alanından
  türetip arıyor.

Ayrıca § 2.8'in ikinci maddesi mutlaktır: bir anlatı rıza dışı birleşmeye
**dayanıyorsa** ve o unsur çıkarılamıyorsa, hikâye **kitaba alınmaz**.

---

## 10. Yazım sistemi

`00_CONTEXT/CHILDREN_WRITING_STYLE.md` — tek kural: **çocuk sahneyi
görmeli, yazarı görmemeli.**

Ölçülebilir bantlar: hikâye 800–1100 · cümle 11–14 · en uzun ≤25 ·
Flesch–Kincaid **4,0–6,5** · hece/kelime 1,35–1,55 · zor sözcük ≤%6 ·
**özel ad ≤7** · diyalog %5–30 · ünlem ≤3.

**Alt sınırlar bilerek var:** çok kolay metin 12 yaşındaki okuru aşağılar
ve "Ages 8–12" vaadini üst uçtan kırar.

`STYLE.md` kasıtlı olarak bir **işaret levhasıdır** ve öyle kalması bir
kapıya bağlı — iki dosyada iki kural listesi tutmak Bestiarium'un D17
çelişkisini davet ederdi.

---

## 11. Görsel kararı

### **İLLÜSTRASYON ZORUNLU** (karar K4)

Bu bir öneri değil, **fiyat modelinin dayanağı**: yol haritası renkli
baskının maliyeti 15,95 $'a çıkarıp fiyatı 39,99 $'a iteceğini ve kitabı
**kategoriden çıkaracağını** hesaplamış.

**45 + 22 + 1 = 68 görsel**, hepsi siyah-beyaz.

---

## 12. Görsel hattı

```
IMAGE_PROMPT_LIBRARY.html  →  GPT Image  →  raw/*.png
   →  convert_images.py  →  processed/{print,kindle,web}/
   →  images.py --measure  →  06_REPORTS/tracked/
```

- **68 prompt üretildi** (elle yazılmadı — K16); üslup gövdesi
  `imagespec.py`'de **tek yerde**; CI imzanın 68'inde de geçtiğini denetliyor
- HTML arayüz: süzgeç, arama, **136 kopyalama düğmesi**, açık/koyu tema
- **Ham PNG'nin üzerine asla yazılmaz** (K5)
- Kurucudan **KDP'ye hazır dosya istenmiyor**
- Ölçüm kalibre edildi: **12 test, hata %0,00**, kapı beş kusurlu kurguyu
  reddediyor ve şartnameye uyanı kabul ediyor

---

## 13. Sayfa modeli

Deterministik model kuruldu ve **gerçek bir yapısal sorun buldu**:

> **230 sayfa, varsayılan yapıyla ULAŞILAMAZ.**

Her hikâye yeni sayfada başlar ve yukarı yuvarlanır → hikâye başına maliyet
**3 ↔ 4 arasında zıplar**; ulaşılabilir toplamlar 204 · **250** · 294 · 340.
Tipografi ayarı aradaki sayıları **açmaz**.

İki yapısal çözüm hedefi tutturuyor (226 / 228); öneri **kültür kartını açık
sayfa yapmak** — kopya başına **+0,29 $**. Karar `DECISIONS.md` § A4'te ve
**Faz 1'in gerçek dizgi ölçümünden sonra** verilir.

Model şu an **kalibre değil** ve bunu kendisi bildiriyor.

---

## 14. CI/CD

Dört iş akışı. Hafif kapılar **hiçbir paket kurmuyor** ve ~25 saniyede
bitiyor.

| İş akışı | İş sayısı | Süre | Sonuç |
|---|---:|---:|---|
| `validate` | 7 | 24 sn | ✅ |
| `images` | 3 | 19 sn | ✅ |
| `build` | 2 | 55 sn | ✅ |
| `release` | 2 | 33 sn | ✅ |

---

## 15. QA kapıları

| Kapı | Betik |
|---|---|
| Veri, kimlik, kapsam, **ölü referans avı** | `validate_spec.py` |
| Depo, belge, **manuscript sızıntısı** | `validate_structure.py` |
| Araştırma kayıtları | `validate_research.py` |
| **Yaş politikası** | `qa_age.py` |
| **Okunabilirlik (8–12)** | `qa_readability.py` |
| Kelime bandı | `qa_length.py` |
| Ses, yasak kalıp, **kültürel not şablonlaşması** | `qa_voice.py` |
| Tekrar | `qa_echo.py` |
| Diakritik | `qa_diacritics.py` |
| Çapraz referans ve kapsam | `qa_crossref.py` |
| Üslup sürüklenmesi | `qa_drift.py` |
| Telif doğrulaması | `editions.py` |
| Sayfa bütçesi | `page_budget.py` |
| **Kapıların kendi testi** | `05_TESTS/selftest.py` — **39 kontrol** |
| **Ölçüm kalibrasyonu** | `05_TESTS/image_selftest.py` — **12 kontrol** |

Son iki satır bu sistemin omurgasıdır: **metin yokken yeşil kalan bir hat,
kusur geldiğinde de yeşil kalabilir.** `qa_age.py` 45 hikâyeyi otomatik
reddetme yetkisine sahip ve o yetki doğruluğu kanıtlanmadan kullanılamaz.

---

## 16. Git akışı

`main` üretim dalı · `faz/**` faz dalları · her faz: iş → yerel QA → commit
→ push → CI bekle → **YEŞİL** → `.gate` yükselt → CHANGELOG → etiket.

**CI kırmızıyken ilerleme yok.** `release.yml` etiket ↔ `.gate` ↔ CHANGELOG
üçlüsünü doğrulamadan sürüm oluşturmuyor — bu bootstrap sırasında
**gerçekten çalıştı** (§ 27).

---

## 17. Güvenlik ve manuscript koruması

İki hatlı koruma:

1. `.gitignore` § ① — yol kalıbı
2. `validate_structure.check_manuscript_leak()` — **içerik** taraması:
   takip edilen dosyalarda hikâye açılış cümlesi arar

**Sınandı:** `selftest.py` takip edilen bir dosyaya kasıtlı sızıntı koyuyor
ve kapının yakaladığını, temizlikten sonra yeşile döndüğünü kanıtlıyor.

**Uzaktan doğrulandı:** `02_MANUSCRIPT/` içeriği yalnızca `.gitkeep`.

Ayrıca 7 gizli-bilgi deseni, ikili çöp taraması ve `.env`/anahtar kalıpları.

---

## 18. Faz yol haritası

| Faz | Başlık | Hikâye | Kümülatif | Görsel | Etiket |
|---:|---|---:|---:|---:|---|
| 1 | Temel · Kapsam, Araştırma, Ses Kalibrasyonu | **1** | 1 | 0 | `v0.1.0` |
| 2 | Çekirdek Yazım | 15 | 16 | 16 | `v0.2.0` |
| 3 | Genişleme | 15 | 31 | 40 | `v0.3.0` |
| 4 | Tamamlama + Editoryal İnceleme | 14 | **45** | 68 | `v0.4.0` |
| 5 | Üretim · Dizgi, KDP, Lansman | — | 45 | 68 | `v1.0.0` |

**Yazım Faz 4'te biter.** Faz 5 üretimdir; hiçbir hikâye oraya ertelenmez
(talimat § 13). Faz 1'in tek hikâyesi bir "araştırma-yalnızca" fazını
önlüyor ve iki mekanik ihtiyacı karşılıyor (ses kalibrasyonu + sayfa
modeli).

---

## 19. Faz 1 Definition of Done

**32 ölçülebilir kriter** — tam liste yol haritası § 17'de. Kısmi geçiş
yok: PASS = 32/32.

Örnekler: 22/22 kültür `locked` · 45/45 hikâye `locked` · ≥55 aday ·
45/45 kısıtlılık taraması ≥20 karakter gerekçeyle · 0 hikâye `retelling`
kaynak kullanıyor · her telaffuzun kaynağı · 3 gerçek ses kalibrasyon
paragrafı · sayfa modeli **gerçek dizgiyle kalibre** · manuscript
sızıntısı 0 (kasıtlı sızıntı testiyle sınanmış) · her `K##` kararı
CHANGELOG'da anılmış.

---

## 20. KDP üretim mimarisi

Üç lansman formatı: **ciltsiz · ciltli · Kindle**. Büyük punto tanımlı ama
devre dışı (yol haritası onu "uzun vadeli genişleme"ye koyuyor).

> "Ciltli" ve "Hardcover" **aynı formattır**; tek üretim hattı var.

### Ticari model **doğrulandı** — beş sayı da birebir

| | Formül | Sonuç | Yol haritası |
|---|---|---:|---:|
| Ciltsiz maliyet | 1,00 + 0,012 × 230 | 3,76 $ | 3,76 $ ✓ |
| Ciltsiz telif | 16,99 × %60 − 3,76 | 6,43 $ | 6,43 $ ✓ |
| Ciltli maliyet | 5,65 + 0,012 × 230 | 8,41 $ | 8,41 $ ✓ |
| Ciltli telif | 26,99 × %60 − 8,41 | 7,78 $ | 7,78 $ ✓ |
| Kindle telif | 7,99 × %70 − teslim | 5,14 $ | 5,14 $ ✓ |

Ve **bir sayı türetildi**: yol haritasında yazmayan **Kindle dosya bütçesi
3,0 MB**. Görsel hattı bu sayıya göre optimize ediyor; mevcut projeksiyon
**1,08 MB**.

---

## 21. KDP yükleme el kitabı

`KDP_UPLOAD_PLAYBOOK.md` — Türkçe, **düğme düğme**, üç format × 27 adım.

Mevcut arayüz (🟢) ile **değişebilecek** arayüz (🟡) açıkça ayrılmış;
kurucuya *"bir etiketi bulamıyorsanız tahmin etmeyin"* denmiş.

İçerik: hazırlık kontrol listesi · ortak metadata · Previewer kontrolleri
(Kindle 8 · ciltsiz 10 · ciltli 14 kalem) · **AI beyanı** · fiyat/telif
doğrulaması · yayın sonrası 8 adım · 10 sık hata.

---

## 22. Riskler

Yol haritasının dördü (R1–R4) + bu projenin yedisi (R5–R11), her biri
azaltmasıyla: yol haritası § 20.

**R2 (yaş uygunluğu) tanımlayıcı risktir** ve azaltması iki parçalı:
`AGE_POLICY.md` (**yapıldı**) + iki ebeveyn okuması (**A8, insan işi**).

---

## 23. İnsan bağımlılıkları

12 kalem (H1–H12). Faz 1'i **bloklayan üçü**:

- **A1** — manuscript nerede duracak
- **`AGE_POLICY.md` onayı** — yol haritası bunu yazım öncesi şart koşuyor
- **A2 / A3** — kültür ve hikâye listeleri (Faz 1'in çıktısı, ama aday
  listesi onayı Faz 1'i başlatır)

**A8** (iki ebeveyn okuyucusu) Faz 4'ü bloklar ama **şimdi planlanmalı**.

---

## 24. Oluşturulan dosyalar

**77 takip edilen dosya.** Özet:

| Kategori | Adet | Not |
|---|---:|---|
| Belgeler (Markdown) | 17 | ~28.800 kelime |
| Üretim betikleri | 18 | ~6.500 satır Python |
| Testler | 3 | 39 + 12 kontrol |
| Şema ve veri | 5 | JSON |
| CI/CD | 4 iş akışı + 5 şablon | |
| Görsel kütüphanesi | 2 | MD + HTML (68 prompt) |
| Üretilen belgeler | 3 | BOOK_STATS · ROADMAP_PROGRESS · BACK_MATTER_PREVIEW |

---

## 25. Değiştirilen dosyalar

**Bu projenin dışında HİÇBİRİ.**

`CODEX_BESTIARIUM/` ve `CODEX_MYTHOLOGICA/` **salt okunur** işlendi.
Bestiarium'un Faz 5 çalışması kesintiye uğratılmadı.

---

## 26. Commit'ler

| SHA | Ne |
|---|---|
| `2b8d4c5` | bootstrap: üretim sistemi kuruldu — kitabın tek kelimesi yazılmadı |
| `5de07b2` | duzeltme: görsel iş akışında iki ölü/yanlış kontrol — **ilk CI koşusu yakaladı** |
| `bfcd1f7` | duzeltme: üretilen belgeler git üst verisi taşımıyor — **sürüm koşusu yakaladı** |

---

## 27. CI sonuçları

**Dört iş akışı, dördü de YEŞİL** (`bfcd1f7`).

### CI iki gerçek kusur buldu — ve bu sistemin çalıştığının kanıtı

**① Kart sayımı süzgeç düğmelerini sayıyordu** (68 yerine 71). Basit bir
regex hatası; CI ilk koşuda yakaladı.

**② Üslup imzası kontrolü SESSİZCE ÖLÜ KURALDI.** İmza `children's`
içeriyor ve HTML'de `&#x27;` olarak kaçıyor; ham dizede aramak **0**
buluyordu. ① düzeltilmeseydi bu kontrol *"68 promptta olmalı, 0 var"*
diyecekti — ama fark edilene kadar **hiçbir şey demeyecekti**.

Bu tam olarak Bestiarium'un Ö1/Ö3 sınıfı bir kusurdur ve raporun geri
kalanının uyardığı şeyin canlı örneğidir: **yanlış yerde arayan bir kontrol
hiçbir şey demez.**

**③ Üretilen belgeler git üst verisi taşıyordu.** `v0.0.1` etiketi atıldığı
anda `release.yml` belgeleri yeniden üretti, "son etiket" satırı değişti ve
bayatlık kapısı kırmızı yandı — **içerik değişmemişti**. Bu, bayatlık
kapısının **kendi kusuruydu ve kapı çalıştığı için bulundu**. Üretilen
belgeler artık yalnızca çalışma ağacının bir işlevi; iki ardışık üretim
birebir aynı çıktıyı veriyor.

Üçü de düzeltildi, commit edildi, push edildi ve CI yeşile döndü.

---

## 28. Nihai durum

```
FAZ 0 · BOOTSTRAP           ████████████████  TAMAM · v0.0.1 · CI YEŞİL
FAZ 1 · TEMEL               ░░░░░░░░░░░░░░░░  ONAY BEKLİYOR
FAZ 2 · ÇEKİRDEK YAZIM      ░░░░░░░░░░░░░░░░
FAZ 3 · GENİŞLEME           ░░░░░░░░░░░░░░░░
FAZ 4 · TAMAMLAMA           ░░░░░░░░░░░░░░░░
FAZ 5 · ÜRETİM              ░░░░░░░░░░░░░░░░
```

| | |
|---|---:|
| Yazılmış hikâye | **0 / 45** |
| Araştırılmış hikâye | **0 / 45** |
| Kilitli kültür | 6 / 22 *(6'sı yol haritasınca zorunlu)* |
| Üretilmiş görsel | **0 / 68** |
| Üretilmiş KDP dosyası | **0** |
| Kapı | `phase0` |
| CI | **YEŞİL** |
| Açık karar | 9 |

---

## 29. ⛔ PHASE 1 NOT STARTED — FOUNDER APPROVAL REQUIRED

**FAZ 1 BAŞLAMADI — KURUCU ONAYI GEREKİYOR.**

45 hikâye araştırılmadı. 45 hikâye yazılmadı. Nihai manuscript
üretilmedi. Nihai illüstrasyonlar üretilmedi. Nihai KDP dosyaları
üretilmedi. Faz 2, 3, 4 ve 5 başlamadı.

Kurulmuş olan tek şey, Faz 1'in **güvenle başlayabilmesi** için gereken
sistemdir.

Onay talebi: [`PHASE_1_APPROVAL_REQUEST.md`](../PHASE_1_APPROVAL_REQUEST.md)
