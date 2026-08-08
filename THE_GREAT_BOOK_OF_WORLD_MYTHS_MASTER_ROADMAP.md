# THE GREAT BOOK OF WORLD MYTHS — MASTER YOL HARİTASI

> **Bu belge projenin TEK DOĞRULUK KAYNAĞIDIR.**
> Bir çelişki bulunursa kazanan bu belgedir; diğer belgeler ona göre
> düzeltilir. Bu belgenin kendisi ancak kurucu kararıyla değişir ve her
> değişiklik `DECISIONS.md` + `CHANGELOG.md`'ye geçer.
>
> Türetildiği kaynak:
> `CODEX_MYTHOLOGICA/AMAZON_KDP_PUBLISHING_COMPANY_ROADMAP_2026.html`
> § BÖLÜM 03 · ÜÇ KİTAP PROJESİ · **PROJE 02**
>
> Sürüm: **1.0 · Bootstrap** · 8 Ağustos 2026
> Durum: **FAZ 1 KURUCU ONAYINI BEKLİYOR — YAZIM BAŞLAMADI**

---

## İçindekiler

1. [Proje genel bakış](#1-proje-genel-bakış)
2. [Ürün spesifikasyonu](#2-ürün-spesifikasyonu)
3. [Kitle](#3-kitle)
4. [Editoryal tez](#4-editoryal-tez)
5. [Kültürel kapsam](#5-kültürel-kapsam)
6. [Hikâye mimarisi](#6-hikâye-mimarisi)
7. [Araştırma mimarisi](#7-araştırma-mimarisi)
8. [Yaş politikası](#8-yaş-politikası)
9. [Yazım üslubu](#9-yazım-üslubu)
10. [İllüstrasyon stratejisi](#10-illüstrasyon-stratejisi)
11. [Sayfa bütçesi](#11-sayfa-bütçesi)
12. [Kelime bütçesi](#12-kelime-bütçesi)
13. [Üretim mimarisi](#13-üretim-mimarisi)
14. [Git disiplini](#14-git-disiplini)
15. [CI/CD mimarisi](#15-cicd-mimarisi)
16. [Faz planı](#16-faz-planı)
17. [Definition of Done](#17-definition-of-done)
18. [KDP üretimi](#18-kdp-üretimi)
19. [KDP yükleme el kitabı](#19-kdp-yükleme-el-kitabı)
20. [Risk kaydı](#20-risk-kaydı)
21. [İnsan bağımlılıkları](#21-insan-bağımlılıkları)
22. [Sürüm stratejisi](#22-sürüm-stratejisi)
23. [Faz kapıları](#23-faz-kapıları)
24. [Nihai teslim](#24-nihai-teslim)

---

## 1. Proje genel bakış

**The Great Book of World Myths** — 8–12 yaş için, 22 kültürden 45 mitolojik
hikâyeyi yeniden anlatan bir antoloji. Yayınevi portföyünün **ikinci
kitabı** (PROJE 02 · Hacim ve kitle genişletme). Yayın hedefi **Temmuz 2027**.

Stratejik görevi: **kitleyi genişletmek.** Codex serisi yetişkin okura
satar; bu kitap yeni bir kitleye, yeni bir kapak diline ve yeni bir raf
konvansiyonuna girer. Portföyün en yüksek kaba ROI'sini taşır (%136).

### Ne DEĞİLDİR

| Değildir | Kaynak |
|---|---|
| *Codex Mythologica'nın basitleştirilmiş hâli* | *"Bu yetişkin cildinin bilinçli tersidir ve **ayrı bir yazım işidir — çeviri değil**."* |
| *Yetişkin metninin çocuk İngilizcesine çevirisi* | *"Bu bir çeviri değil, **yeni bir yazımdır**."* |
| *Şiddetli kelimeleri silinmiş bir metin* | *"Şiddet ve trajedi **saklanmaz** ama **sahnelenmez**."* |

Araştırma yetişkin cildinden devralınabilir (yol haritası: *"araştırma
20 saat — yetişkin cildinden devralınır"*); **proza devralınamaz.**

### İzolasyon

Bu depo **Codex Bestiarium'dan tamamen ayrıdır**. Bestiarium yalnızca
referans uygulama olarak okunmuştur
([`00_CONTEXT/LESSONS_FROM_CODEX_BESTIARIUM.md`](00_CONTEXT/LESSONS_FROM_CODEX_BESTIARIUM.md)).
Hiçbir betik onun dosyalarına yazmaz; kardeş dizinde bulunması **zorunlu
değildir**.

---

## 2. Ürün spesifikasyonu

Aşağıdaki her satır master yol haritasının **açık kararıdır** ve iş kısıtı
sayılır.

| Kalem | Karar |
|---|---|
| Çalışma adı | World Myths for Young Readers |
| **Nihai başlık** | **The Great Book of World Myths** |
| **Alt başlık** | 45 Stories of Gods, Heroes, and Monsters from 22 Cultures — Retold for Young Readers (Ages 8–12) |
| Seri | "The Great Book of…" (Codex serisinden **ayrı**) |
| Yazar adı | Codex serisiyle **aynı** |
| Trim | 6 × 9 inç (normal trim) |
| Sayfa | ~230 |
| Hikâye | 45 · ~950 kelime |
| Metin | ~43.000 kelime |
| İllüstrasyon | 45 açılış + 22 vinyet, **siyah-beyaz** |
| Harita | 1 dünya haritası |
| Ek malzeme | telaffuz rehberi · "kim kimdir" · her hikâye sonunda 2 satırlık kültürel not |
| Ciltsiz | 16,99 $ · maliyet 3,76 $ · telif 6,43 $ |
| Ciltli | 26,99 $ · maliyet 8,41 $ · telif 7,78 $ · **lansmanla birlikte** |
| Kindle | 7,99 $ · telif 5,14 $ · dosya bütçesi **3,0 MB** |
| Üretim | ~215 saat · lansman ~430 $ · 3,5 ay |
| Yayın | **Temmuz 2027** |

### Maliyet modeli DOĞRULANDI

`04_BUILD/editions.py` KDP'nin resmî tablolarından yol haritasının verdiği
her sayıyı **birebir** üretiyor:

| | Formül | Sonuç | Yol haritası |
|---|---|---:|---:|
| Ciltsiz maliyet | 1,00 $ + 0,012 $ × 230 | **3,76 $** | 3,76 $ ✓ |
| Ciltsiz telif | 16,99 $ × %60 − 3,76 $ | **6,43 $** | 6,43 $ ✓ |
| Ciltli maliyet | 5,65 $ + 0,012 $ × 230 | **8,41 $** | 8,41 $ ✓ |
| Ciltli telif | 26,99 $ × %60 − 8,41 $ | **7,78 $** | 7,78 $ ✓ |
| Kindle telif | 7,99 $ × %70 − 3,02 MB × 0,15 $ | **5,14 $** | 5,14 $ ✓ |

> **Bu doğrulama bir süs değil, bir kapıdır.** Sayfa sayısı değişirse
> maliyet ve telif otomatik olarak yeniden hesaplanır ve `page_budget.py`
> farkı kopya başına dolar olarak basar. Ayrıca Kindle dosya bütçesinin
> **3,0 MB olduğu buradan türetilmiştir** — seçilmemiştir.

---

## 3. Kitle

| Rol | Kim |
|---|---|
| **Alıcı** | ebeveyn · büyükanne/büyükbaba · öğretmen · okul kütüphanecisi |
| **Okur** | 8–12 yaş; Percy Jackson'ı bitirmiş, "daha fazla mit" arayan çocuk |

Alıcı ile okurun ayrı kişiler olması bu kitabın temel ticari gerçeğidir:
**okur hikâye ister, alıcı güven ister.** `AGE_POLICY.md` alıcı tarafını,
`CHILDREN_WRITING_STYLE.md` okur tarafını korur.

---

## 4. Editoryal tez

> Çocuk mitoloji rafının yaklaşık **%80'i Yunan**. Bir çocuk Yunan'ı
> bitirdiğinde önüne konan şey genellikle başka bir Yunan kitabıdır.

Markalı rakipler (DK, National Geographic Kids, Usborne) tam renkli, ağır
görsel tasarımlı ve 19,99–29,99 $ bandında. Yapamadıkları şey **uzun soluklu
okumadır**: kutucuk ve kolaj tasarımı, çocuğun oturup okuduğu bir kitap
üretmiyor.

**Bu kitap bir *bakılan* kitap değil, bir *okunan* kitaptır.** İllüstrasyon
anlatıyı açar, yerini almaz. Bu, illüstrasyon bütçesinin neden 45 + 22 ile
sınırlı tutulduğunu da açıklar.

---

## 5. Kültürel kapsam

**22 kültür.** Altısı yol haritasında **adıyla sayılmıştır ve kilitlidir**:

> *"**Kore, İnuit, Polinezya, Batı Afrika, Fars ve Türk** anlatılarını aynı
> ciltte, aynı kalitede sunan bir kitap neredeyse yok."*

Kalan 16 slot **AÇIK KARARDIR** (`DECISIONS.md` § A2) ve Faz 1'de
kilitlenir. `01_RESEARCH/culture_index.json` şu anda 6 kilitli + 23 aday
taşır; `validate_spec.py` `.gate` `phase1`'e yükseltilebilmesi için
**22'sinin de `locked`** olmasını şart koşar.

### Dağılım kuralları

- Her kilitli kültürün **en az bir** hikâyesi olmalı (kapı)
- Hiçbir kültür **4'ten fazla** hikâye almasın (uyarı — bu projenin önerisi)
- **Yunan payı en fazla 3** — kitabın varlık sebebi rafın %80 Yunan olması
- Eşit dağıtım **zorunlu değildir**; gerçek dağılım belgelenir

### Kasıtlı dışarıda bırakma

**Avustralya Aborjin gelenekleri.** Anlatı çoğunlukla topluluk
mülkiyetindedir ve kimin anlatabileceği kurala bağlıdır. Bu bir kusur değil
bir karardır ve **arka maddede okura söylenir**.

---

## 6. Hikâye mimarisi

**Sabit bölüm başlığı yoktur.** Her hikâye dört hareket taşır ve hareketler
görünmez: **① Kapı → ② Baskı → ③ Dönüm → ④ Sonuç.** Sonra, tipografik olarak
ayrı: **⑤ Kültürel not** (2 satır).

Kitap **altı bölgesel bölüme** ayrılır ve dünya haritasıyla birebir konuşur
(`00_CONTEXT/EDITORIAL_ARCHITECTURE.md` § 4 — A5 açık kararı).

Ölçüler: hikâye 800–1100 kelime (hedef 950) · cümle ortalaması 11–14 ·
en uzun cümle ≤25 · paragraf ≤6 cümle · **hikâye başına yeni özel ad ≤7**.

---

## 7. Araştırma mimarisi

Ölçüt: [`SOURCING_STANDARD.md`](SOURCING_STANDARD.md).

Her hikâyenin `01_RESEARCH/story_index.json` içinde bir kaydı ve
`01_RESEARCH/research/<id>.md` altında **üretilmiş** bir dosyası vardır.
Elle yazılan tek şey dizindir.

### Kapılar

| Kural | Kapı |
|---|---|
| ≥2 bağımsız kaynak (`index` ve `retelling` sayılmaz) | `validate_spec.py` |
| ≥1 `primary`/`scholarly` | `validate_spec.py` |
| ≥1 güçlü doğrulama (`fulltext`/`toc`/`canon`/`article`/`sv`) | `validate_spec.py` |
| Kanonik anlatım + **gerekçesi** | `validate_spec.py` |
| Kısıtlılık taraması — **MUAFİYETSİZ** | `validate_spec.py` |
| Yaş uyarlaması notu (IMPLY/OMIT/REVIEW kategorilerinde) | `validate_spec.py` |
| Her telaffuzun **kaynağı** | `validate_spec.py` |
| Her olgusal iddianın kaynağa bağlı olması | `validate_spec.py` |

### Bu projeye özgü iki şey

**① Kanonik anlatım seçimi.** Bir başvuru cildi *"varyantlar vardır"* der ve
geçer; bir hikâye **bir** anlatım seçmek zorundadır. Seçim ve gerekçesi
kaydedilir. *"Daha yumuşak olduğu için"* **tek başına geçersiz gerekçedir**
— o kültürel sterilizasyondur.

**② Yeniden anlatım asla kaynak sayılmaz.** Çocuk mitoloji rafı yeniden
anlatımlarla doludur ve onlardan yazmak kolaydır — ama bir yeniden anlatım
zaten bir **editoryal karar zinciridir** ve o kararları görmeden devralmak,
raftaki yaygın yanlışları kopyalamaktır.

### 45 sayısı düşürülemez

Bestiarium kapsamı 120 → 112'ye indirdi. **Burada bu yapılamaz**: 45 ve 22
**alt başlıkta yazıyor** ve alıcı tam olarak o iki sayıyı tarıyor. Düşen bir
hikâyenin yerine **başkası gelmek zorundadır** → Faz 1 aday listesi
**≥55 hikâye, ≥26 kültür** olmalıdır.

---

## 8. Yaş politikası

**Bu projenin tanımlayıcı riski budur** ve master yol haritası azaltmasını
adıyla yazmıştır:

> *"Mitler acımasızdır. Yanlış tonlanmış bir sahne, ebeveyn yorumunda
> 'çocuğum için fazla karanlık' olarak geri döner — ve **bu yorum
> silinemez**. Azaltma: **yazım öncesi AGE_POLICY.md**; yayından önce
> **en az iki ebeveyn okuması**."*

Tam çerçeve: [`AGE_POLICY.md`](AGE_POLICY.md) — **on yedi içerik kategorisi**,
her biri `ALLOW` / `IMPLY` / `OMIT` / `REVIEW`.

**Kapı iki yönlüdür.** Aşırı sahneleme kadar **aşırı saklama** da kusurdur:
ölüm örtmecesi ve zorla mutlu son bu kitapta **kültürel sterilizasyondur**.

> Hedef: **YAŞA UYGUN YENİDEN ANLATIM.** Hedef değil: **KÜLTÜREL
> STERİLİZASYON.**

Makine tarafı: `04_BUILD/qa_age.py` — ve o kapının kendisi
`05_TESTS/selftest.py` ile sınanır. 45 hikâyeyi otomatik reddetme yetkisi
olan bir kapı, doğru çalıştığı kanıtlanmadan kullanılamaz.

---

## 9. Yazım üslubu

Tam kural seti: [`00_CONTEXT/CHILDREN_WRITING_STYLE.md`](00_CONTEXT/CHILDREN_WRITING_STYLE.md).

> **Tek kural: çocuk sahneyi görmeli, yazarı görmemeli.**

| Ölçü | Hedef | Kapı |
|---|---|---|
| Hikâye | 950 kelime (800–1100) | `qa_length.py` |
| Cümle ortalaması | 11–14 | `qa_voice.py` |
| Flesch–Kincaid | **4,0–6,5** | `qa_readability.py` |
| Hece/kelime | 1,35–1,55 | `qa_readability.py` |
| Zor sözcük | ≤%6 | `qa_readability.py` |
| Yeni özel ad | ≤7 / hikâye | `qa_readability.py` |
| Diyalog payı | %5–30 | `qa_voice.py` |
| Ünlem | ≤3 / hikâye | `qa_age.py` |

**Alt sınırlar da bilerek vardır:** çok kısa cümle ve çok düşük sınıf
seviyesi 12 yaşındaki okuru **aşağılar** ve "Ages 8–12" vaadini üst uçtan
kırar.

**Özel adlar okunabilirlik hesabından çıkarılır** — aksi hâlde kapı, kitabın
**kültürel kapsamını cezalandırır**.

### Üretim disiplini

- **Tek seferde en fazla üç hikâye** (yol haritası § 4.2)
- **Yazan oturum denetlemez** — düşman denetçi ayrı oturumda, yalnızca
  bitmiş metni görerek, görevi **çürütmek**
- **Yaş incelemesi üçüncü bir gözle**
- **Her düzeltme koda yazılır** — elle düzenleme yeniden üretilebilirliği bitirir
- **Ölçülmüş ve etiketlenmiş metin gerekçesiz açılmaz**

---

## 10. İllüstrasyon stratejisi

### KARAR: **İLLÜSTRASYON ZORUNLUDUR** (K4)

Bu bir öneri değil, **fiyat modelinin dayanağıdır**:

> *"İllüstrasyon: 45 bölüm açılış çizimi + 22 kültür vinyeti, siyah-beyaz.
> Gerekçe: renkli baskı bu sayfa sayısında maliyeti 15,95 $'a çıkarır —
> fiyatı 39,99 $'a iter, **kategoriden çıkarır**."*
>
> *"Harita: 1 dünya haritası (22 kültürün konumu). Gerekçe: ebeveynin
> 'eğitici' algısını tek görselde kurar."*

**45 + 22 + 1 = 68 görsel.**

### Hat

```
07_ASSETS/IMAGE_PROMPT_LIBRARY.html   ← kopyalama düğmeli çalışma arayüzü
      ↓  kurucu · GPT Image
07_ASSETS/raw/<id>.png                ← HAM · ÜZERİNE ASLA YAZILMAZ
      ↓  04_BUILD/convert_images.py
07_ASSETS/processed/print/<id>.tif    ← 600 dpi gri TIFF
07_ASSETS/processed/kindle/<id>.png   ← dosya bütçesine optimize
07_ASSETS/processed/web/<id>.webp     ← A+ ve pazarlama
      ↓  04_BUILD/images.py --measure
06_REPORTS/tracked/image-consistency.json
```

**Kurucudan KDP'ye hazır dosya İSTENMEZ** (K5). Ham çıktı PNG'dir; üretim
formatlarını hat türetir.

**Üslup gövdesi tek yerde durur** (`04_BUILD/imagespec.py`) ve promptlar
**üretilir, elle yazılmaz** (K16) — "tek çizgi dili" şartı ancak böyle
tutulabilir. CI, üslup imzasının 68 promptun hepsinde geçtiğini denetler.

### Ölçüm kalibre edilmeden hiçbir görsel ölçülmez

`05_TESTS/image_selftest.py`, geometrisi **bilinen** kurgu görsellerde
ölçümün doğru sayıyı bulduğunu kanıtlar (ölçülen hata: **%0,00**) ve kapının
gerçekten ısırdığını sınar. Bestiarium'un plaka ölçümü bu test olmadan
√2 yanlıştı ve **doğru çizilmiş 112 plakanın tamamını** reddedecekti.

---

## 11. Sayfa bütçesi

Deterministik model: `04_BUILD/page_budget.py`.

**SAYFA BÜTÇESİ FİYAT MODELİNİN KENDİSİDİR.** 230 yerine 280 sayfa
maliyeti 0,60 $ artırır ve telifi %9 düşürür — her satılan kopyada.

| Bileşen | Sayfa |
|---|---:|
| Ön madde | 14 |
| Bölüm açılışları (6 × 2) | 12 |
| Kültür kartları (22 × 1) | 22 |
| Hikâyeler (45 × 4) | 180 |
| Arka madde | 21 |
| **Model toplamı** | **250** |
| Yol haritası hedefi | 230 |

### Modelin bulduğu şey

**230 sayfa mevcut varsayılan yapıyla ULAŞILAMAZ.** Her hikâye yeni sayfada
başlar ve yukarı yuvarlanır → hikâye başına maliyet **3 ↔ 4 arasında zıplar**
ve aradaki toplamlar ulaşılamazdır (204 · 250 · 294 · 340).

Hedefi tutturan iki yapısal seçenek:

| Seçenek | Kültür kartı | Hikâye/sayfa | Toplam | Ciltsiz telif |
|---|---:|---:|---:|---:|
| **(a′)** kültür kartı açık sayfa | 2 | 3 | **226** | 6,48 $ |
| (b′) vinyet başlıkta, kart yok | 0 | 4 | 228 | 6,46 $ |

**Öneri (a′).** Karar `DECISIONS.md` § A4'te ve **Faz 1'in gerçek dizgi
ölçümünden sonra** verilir.

> ⚠ Model **kalibre değildir**: `wordsPerPage` tipografi tahmininden geliyor.
> Bestiarium D36: dolguyla ölçmek *"modeli modele karşı sınamaktır"*.
> Faz 1 bir hikâyeyi gerçekten dizip ölçer (K3).

---

## 12. Kelime bütçesi

| | |
|---|---:|
| Hikâye × hedef | 45 × 950 = **42.750** |
| Kültürel notlar | 45 × ~35 = 1.575 |
| Kültür kartı metni | 22 × ~60 = 1.320 |
| Ön madde | ~900 |
| Arka madde (sözlük + telaffuz + notlar) | ~3.500 |
| **Toplam** | **~50.000** |
| Yol haritası (hikâye metni) | **~43.000** ✓ |

Hikâye metni hedefi **42.750 ≈ 43.000** — yol haritasıyla birebir. Ek
malzeme o hedefin dışındadır ve sayfa modeline ayrıca girer.

### Faz dağılımı

| Faz | Hikâye | Kümülatif | Kelime | Kümülatif |
|---:|---:|---:|---:|---:|
| 1 | **1** (pilot) | 1 | 950 | 950 |
| 2 | 15 | 16 | 14.250 | 15.200 |
| 3 | 15 | 31 | 14.250 | 29.450 |
| 4 | **14** | **45** | 13.300 | **42.750** |
| 5 | — | 45 | — | 42.750 |

**Yazım Faz 4'te biter.** Faz 5 üretimdir; hiçbir hikâye oraya ertelenmez.

---

## 13. Üretim mimarisi

```
THE-GREAT-BOOK-OF-WORLD-MYTHS/
├── 00_CONTEXT/     proje bağlamı · üslup · editoryal mimari · Bestiarium dersleri
├── 01_RESEARCH/    kültür/hikâye dizinleri · şemalar · araştırma kayıtları
├── 02_MANUSCRIPT/  kitabın prozası — DEPO DIŞINDA (.gitignore § ①)
├── 03_EDITORIAL/   yaş incelemesi · ebeveyn okumaları · düzeltme kayıtları
├── 04_BUILD/       bütün üretim ve doğrulama araçları
├── 05_TESTS/       KAPILARIN KENDİ TESTİ — kasıtlı kusurlu kurgu kitap
├── 06_REPORTS/     ölçüm raporları (tracked/ altındakiler DEPODA durur — K18)
├── 07_ASSETS/      raw/ (ham PNG) → processed/ (üretim formatları)
├── 08_OUTPUT/      nihai KDP dosyaları — üretilir, depoda durmaz
├── 09_ARCHIVE/     düşürülen malzeme ve gerekçeleri
└── .github/        CI/CD
```

Her dizinin bir üretim amacı vardır; `validate_structure.py` ağacı denetler.

---

## 14. Git disiplini

**Üretim dalı: `main`.** Faz dalları: `faz/**`. Düzeltme: `fix/**`.

Her faz için değişmez sıra:

```
① faz işini bitir
② YEREL QA:  ./04_BUILD/qa_all.sh          → YEŞİL olmalı
③ commit
④ push
⑤ GitHub Actions'ı BEKLE
⑥ CI'ı incele
⑦ YEŞİL şart
⑧ .gate yükselt · CHANGELOG yaz · etiket at
⑨ ancak o zaman sonraki faz
```

**CI KIRMIZIYKEN İLERLEME YOKTUR.** Kırmızıysa: dur → teşhis → düzelt →
uygunsa **regresyon testi ekle** → commit → push → bekle → yeşil → devam.

### Public depo, private manuscript

Depo **public**'tir. Manuscript **değildir**. İki hatlı koruma:

1. `.gitignore` § ① — **yol** kalıbı
2. `validate_structure.check_manuscript_leak()` — **içerik** taraması:
   takip edilen dosyalarda hikâye açılış cümlesi görürse CI kırmızı yanar

İkinci hat, birincinin yakalayamadığını yakalar: yeni bir ada konan proza
dosyası. Ve `selftest.py` **kasıtlı bir sızıntıyla** ikinci hattın gerçekten
ısırdığını kanıtlar.

> Politika disipline değil **mekanizmaya** bağlanır: disiplin unutulur,
> mekanizma unutmaz.

---

## 15. CI/CD mimarisi

Dört iş akışı. Hafif kapılar hiçbir paket kurmaz (K7) ve saniyeler içinde
biter; ağır bağımlılıklar yalnızca görsel ve dizgi işlerindedir.

| İş akışı | Ne zaman | Ne yapar |
|---|---|---|
| `validate.yml` | her push · PR | kapı seviyesi · veri · depo · **kapıların kendi testi** · metin kapıları · üretim modeli · bayat belge |
| `images.yml` | görsel dosyaları değişince | ölçüm kalibrasyonu · prompt senkronu · **tek üslup gövdesi** · format bütçeleri · kayıtlı rapor |
| `build.yml` | kaynak/araç değişince | modül import testi · KDP kısıtları · dizgi (Faz 5) |
| `release.yml` | `v*` etiketi | etiket ↔ `.gate` ↔ CHANGELOG tutarlılığı · bütün kapılar · GitHub Release |

### Denetlenen kontroller

**YAPISAL** şema · metadata · zorunlu dosya · yinelenen kimlik · eksik hikâye ·
eksik kültür · bozuk kayıt · **ölü referans avı**

**YAZIM** kelime sayısı · hikâye uzunluğu · cümle uzunluğu · yasak kalıp ·
yer tutucu · TODO · yinelenen paragraf · tekrar eden öbek · noktalama ·
tırnak dengesi · kesme · em dash · Unicode/diakritik · başlık tutarlılığı

**ARAŞTIRMA** kaynak tamlığı · künye bütünlüğü · kaynak durumu ·
desteksiz olgusal iddia · eksik araştırma kaydı · **kısıtlılık taraması**

**YAŞ QA** yaş politikası ihlali · grafik betimleme · yasaklı içerik ·
uygunsuz sözcük dağarcığı · yetişkin tonu · korku eşiği · **son sayfa kuralı** ·
geçmiş zaman tuzağı · kültürel genelleme

**EDİTORYAL** üslup sürüklenmesi · ses tutarlılığı · tekrar · aynı açılış ·
aynı kapanış · **kültürel not şablonlaşması**

**YAPI** hikâye sayısı · kültür sayısı · bölüm sırası · sözlük kapsamı ·
telaffuz kapsamı · kültürel not kapsamı · harita kapsamı

**ÇAPRAZ REFERANS** kişiler · kültürler · sözlük bağları · telaffuz kayıtları

**GÖRSEL** eşleme · dosya varlığı · boyut · DPI · renk modu · format ·
yinelenen · yetim · eksik · **ölçüm kalibrasyonu**

**KDP / ÜRETİM** sayfa ölçüsü · taşma · marj · sayfa sayısı · görsel
çözünürlüğü · dosya boyutu · **telif doğrulaması** · metadata tutarlılığı

**GÜVENLİK** gizli bilgi · API anahtarı · **manuscript sızıntısı** ·
özel yol · ikili çöp · geçici dosya

---

## 16. Faz planı

**Beş faz** (K1). Yazım üç faza dağıtılmıştır (K2) ve **Faz 4'te biter**.

---

### FAZ 1 — Temel · Kapsam, Araştırma Mimarisi ve Ses Kalibrasyonu
`v0.1.0` · kapı `phase1`

**1. Amaç.** Kitabın **neyden oluştuğunu** kilitlemek ve **nasıl
konuştuğunu** ölçmek. Faz 1 bitince 45 hikâye ve 22 kültür belli, her biri
kaynaklanmış ve taranmış, ve kitabın sesi **gerçek metinle** kalibre edilmiş
olur.

**2. Hikâye / sayfa / kelime.** **1 hikâye** (ses kalibrasyon pilotu) ·
~950 kelime · 45 araştırma kaydı.

> **Neden tam olarak bir hikâye (K3).** İki gerekçe:
> ① `CHILDREN_WRITING_STYLE.md`'nin ses kalibrasyon örnekleri **gerçek
> metinden** gelmek zorundadır ve bu kitabın devralacağı bir çocuk sesi
> **yoktur** (yetişkin cildi bilinçli tersidir).
> ② Sayfa modeli **gerçek prozayla** kalibre edilmeli — Bestiarium D36:
> dolguyla ölçmek *"modeli modele karşı sınamaktır"*.
> Bir hikâye ikisini de çözer ve Faz 1'i "yalnızca araştırma" olmaktan
> çıkarır (talimat § 13'ün açık yasağı).

**3. Araştırma işi.** 22 kültürün kilitlenmesi (A2) · 45 hikâyenin
kilitlenmesi (A3) · ≥55 hikâye ve ≥26 kültür aday havuzu · her hikâye için
≥2 bağımsız kaynak · kanonik anlatım + gerekçe · **kısıtlılık taraması
(muafiyetsiz)** · telaffuz + kaynağı · kişiler.

**4. Editoryal iş.** Bölüm mimarisi (A5) · kültür vinyeti yerleşimi (A4) ·
`AGE_POLICY.md` kurucu onayı · `CHILDREN_WRITING_STYLE.md` ses kalibrasyon
örneklerinin **gerçek metinle** doldurulması · pilot hikâyenin yaş incelemesi.

**5. Altyapı işi.** — *(bootstrap'ta tamamlandı)* · `.gate` → `phase1` ·
araştırma kayıtlarının üretilmesi.

**6. Test altyapısı.** `qa_crossref` için kusurlu kurgu (envanter
kilitlenince mümkün) · pilot hikâyeyle bütün metin kapılarının **gerçek
metne** karşı ilk koşusu.

**7. CI kapıları.** `validate_spec --gate phase1` · `validate_research` ·
bütün metin kapıları · `selftest` · `page_budget` (kalibre edilmiş).

**8–10. DoD / PASS / FAIL.** → [§ 17](#17-definition-of-done)

**11. Beklenen dosyalar.** `culture_index.json` (22 locked) ·
`story_index.json` (45 locked, ≥55 aday) · `01_RESEARCH/research/*.md` (45) ·
`00_CONTEXT/CHILDREN_WRITING_STYLE.md` (3 kalibrasyon örneği) ·
`03_EDITORIAL/AGE_REVIEW_LOG.md` · `06_REPORTS/tracked/page-calibration.json`

**12. Beklenen commit'ler.** kapsam kilidi · araştırma partileri (kültür
başına) · pilot hikâye · ses kalibrasyonu · sayfa ölçümü · faz kapanışı

**13. Sürüm.** `v0.1.0` — "Temel"

**14. Claude notları.** Araştırma ve yazım **ayrı oturumlar**. Kısıtlılık
taraması bir onay kutusu değil, **okuma işidir**. Hiçbir hikâye kaynağı
bulunmadan listeye alınmaz. **Telaffuz uydurulmaz.**

**15. Riskler.** Kısıtlılık taraması bir kültürü düşürebilir → aday havuzu
yedekli · pilot hikâye sesi yanlış kurabilir → kurucu onayı zorunlu

**16. Bağımlılıklar.** A1 (manuscript nerede duracak) **Faz 1 başlamadan
kapanmalı** · A2 ve A3 Faz 1'in çıktısı

**17. İnsan girdisi.** `AGE_POLICY.md` onayı · 22 kültür onayı ·
45 hikâye onayı · pilot hikâyenin sesi onayı

**18. Geri alma.** Kapsam kilidi bir commit'tir; geri alınabilir. Pilot
hikâye beğenilmezse **yeniden yazılır** — Faz 2 başlamaz.

**19. DURMA KOŞULU.** `.gate` = `phase1` · `v0.1.0` etiketi · CI yeşil ·
**kurucu Faz 2 onayı verene kadar dur.**

---

### FAZ 2 — Çekirdek Yazım · İlk On Beş Hikâye
`v0.2.0` · kapı `phase2`

**Amaç.** Kitabın sesini **ölçekte** kurmak ve görsel hattını gerçek
girdiyle çalıştırmak.

**Hedef.** 15 hikâye (kümülatif **16/45**) · ~14.250 kelime · 16 görsel

**İş.** Faz 1'de kilitlenen ilk iki bölgesel bölümün hikâyeleri · her hikâye
için yaş incelemesi · kültürel notlar · ilk 16 ham görsel (kurucu) →
dönüşüm → ölçüm · ara prova dizgisi.

**CI kapıları.** `phase2` + bütün metin kapıları + `qa_drift` (her 5
hikâyede) + görsel ölçümü.

**Risk.** İlk ölçekte yazımda üslup sürüklenmesi. **Düzeltilmez, ölçülür**
(D40) ve her ölçüm commit iletisine geçer.

**DURMA KOŞULU.** 16/45 · CI yeşil · `v0.2.0` · kurucu onayı.

---

### FAZ 3 — Genişleme · İkinci On Beş Hikâye
`v0.3.0` · kapı `phase3`

**Amaç.** Kapsamı yarıdan fazlaya taşımak; kültürel çeşitliliğin gerçekten
tuttuğunu ölçmek.

**Hedef.** 15 hikâye (kümülatif **31/45**) · ~14.250 kelime · 40 görsel

**İş.** Üçüncü ve dördüncü bölge · **kültür kartı metinleri** · telaffuz
rehberi ve sözlüğün ilk tam üretimi · ikinci ara prova dizgisi ·
sayfa modelinin **yeniden ölçülmesi**.

**CI kapıları.** `phase3` + `qa_crossref` (telaffuz/sözlük kapsamı artık
anlamlı) + sayfa bütçesi.

**DURMA KOŞULU.** 31/45 · CI yeşil · `v0.3.0` · kurucu onayı.

---

### FAZ 4 — Tamamlama · Son On Dört Hikâye ve Editoryal İnceleme
`v0.4.0` · kapı `phase4`

**Amaç.** **Kitabı bitirmek** ve bütününü bir kez, birlikte ele almak.

**Hedef.** 14 hikâye → **45/45** · ~13.300 kelime · **68/68 görsel**

**İş.**
- Kalan iki bölge
- **Üslup uyumlama geçişi** — D40'ın ertelediği düzeltme buraya aittir;
  45 hikâye **birlikte** ele alınır (16'yı ayrı, 45'i ayrı düzeltmek iki
  farklı üslup üretir)
- **Düşman olgu denetimi** — ayrı oturum, yalnızca bitmiş metin, görev
  doğrulamak değil **çürütmek**
- **İki ebeveyn okuması** (A8) — yol haritasının zorunlu azaltması
- Arka maddenin tamamlanması
- Sayfa bütçesinin **son kez** ölçülmesi; A4/A5 kararlarının kilitlenmesi

**CI kapıları.** `phase4` + **sayfa bütçesi artık UYARI DEĞİL HATA** +
`03_EDITORIAL/PARENT_READINGS.md` iki imzalı kayıt.

**DURMA KOŞULU.** **45/45** · 68/68 görsel · iki ebeveyn okuması kayıtlı ·
CI yeşil · `v0.4.0` · kurucu onayı.

---

### FAZ 5 — Üretim · Dizgi, KDP Dosyaları ve Lansman
`v1.0.0` · kapı `phase5` → `release`

**Amaç.** **Anahtar teslim KDP dosyaları** üretmek ve doğrulamak.

**Hedef.** Yazım yok. Üç format · kapaklar · metadata · doğrulama raporları.

**İş.**
- İç blok dizgisi: ciltsiz PDF · ciltli PDF · Kindle EPUB
- Kapak: ciltsiz + ciltli (**çocuk kitabı konvansiyonu — "koyu kodeks"
  dili burada işlemez**)
- Görsellerin üretim formatlarına dönüşümü ve yerleştirilmesi
- KDP doğrulaması: gömülü font · marj · taşma · sayfa sayısı · dosya boyutu
- Metadata: başlık · alt başlık · açıklama · 7 anahtar kelime · kategoriler ·
  yaş aralığı · **AI beyanı**
- QR sayfası ve "22 kültür haritası" indirmesi
- `KDP_UPLOAD_PLAYBOOK.md` ile adım adım yükleme
- Sürüm manifestosu ve yükleme kontrol listesi

**CI kapıları.** `release` + `build.yml` tam dizgi + KDP kısıtları +
`release.yml` etiket doğrulaması.

**DURMA KOŞULU.** Üç formatın dosyaları **üretilmiş ve doğrulanmış** ·
prova kopyası elde · CI yeşil · `v1.0.0`.

---

## 17. Definition of Done

### Faz 1 DoD — ölçülebilir, tamamı

| # | Ölçüt | Kapı |
|---:|---|---|
| 1 | `.gate` = `phase1` ve `project_config.gates.current` ile aynı | `validate_structure` |
| 2 | Public depo `main` dalında, CI **yeşil** | GitHub Actions |
| 3 | **22/22** kültür `locked` | `validate_spec --gate phase1` |
| 4 | 22 kültürün **hepsinde** `restrictionAssessment ≠ pending` | `validate_spec` |
| 5 | Yol haritasının altı kültürü dizinde ve `locked` | `validate_spec` |
| 6 | **45/45** hikâye `locked` | `validate_spec` |
| 7 | Aday havuzu **≥55** hikâye · **≥26** kültür | `validate_spec` (uyarı) |
| 8 | Her kilitli kültürün **≥1** hikâyesi | `validate_spec` |
| 9 | Hiçbir kültür >4 hikâye · Yunan ≤3 | `validate_spec` (uyarı) |
| 10 | Her hikâyede **≥2 bağımsız** kaynak | `validate_spec` |
| 11 | Her hikâyede **≥1 primary/scholarly** | `validate_spec` |
| 12 | Her hikâyede **≥1 güçlü doğrulama** | `validate_spec` |
| 13 | **0** hikâye `retelling` kaynak kullanıyor | `validate_spec` |
| 14 | Her hikâyede kanonik anlatım **+ gerekçesi** | `validate_spec` |
| 15 | **45/45** kısıtlılık taraması, her biri ≥20 karakter gerekçeyle | `validate_spec` |
| 16 | IMPLY/OMIT/REVIEW kategorili her hikâyede `ageAdaptationNote` | `validate_spec` |
| 17 | Her özel adın telaffuzu **ve kaynağı** | `validate_spec` |
| 18 | Her olgusal iddia bir kaynağa bağlı | `validate_spec` |
| 19 | **45/45** araştırma kaydı üretilmiş ve güncel | `validate_research` |
| 20 | `AGE_POLICY.md` **kurucu onaylı** | insan |
| 21 | `CHILDREN_WRITING_STYLE.md`'de **3 gerçek** kalibrasyon paragrafı | `validate_structure` |
| 22 | **1/45** hikâye yazılmış ve bütün metin kapılarından geçmiş | `qa_*` |
| 23 | Pilot hikâye: 800–1100 kelime · FK 4,0–6,5 · ≤7 özel ad · ünlem ≤3 | `qa_length`,`qa_readability`,`qa_age` |
| 24 | Pilot hikâyenin `ageReviewStatus` ≠ `pending` | `validate_spec` |
| 25 | Sayfa modeli **gerçek dizgiyle kalibre** edilmiş | `page_budget` |
| 26 | A4 ve A5 karara bağlanmış, `EDITORIAL_ARCHITECTURE.md` güncel | `validate_structure` |
| 27 | Telif üç sürümde de **pozitif** | `editions` |
| 28 | Manuscript sızıntısı: **0** — kasıtlı sızıntı testiyle sınanmış | `selftest` |
| 29 | Kapıların kendi testi: **hepsi geçiyor** | `selftest` |
| 30 | Üretilen belgelerin hiçbiri bayat değil | `update_docs --check` |
| 31 | `CHANGELOG.md`'de `[0.1.0]` bloğu ve **her `K##` kararı anılmış** | `update_docs` |
| 32 | `v0.1.0` etiketi ve GitHub Release | `release.yml` |

**PASS:** 32 ölçütün **tamamı**.
**FAIL:** herhangi biri. Kısmi geçiş yoktur; "çoğu tamam" bir durum değildir.

> *"Looks good" · "mostly complete" · "reasonable"* tamamlanma ölçütü
> **değildir**.

### Faz 2–4 DoD

Her yazım fazı için, yukarıdakilere **ek olarak**:

- Kümülatif hikâye hedefi tam olarak tutuyor
- Bant dışı hikâye: **0**
- Yasak kalıp: **0** · yaş politikası ihlali: **0**
- Hikâyeler arası 8+ kelimelik tekrar: **0**
- Kültürel not şablonlaşması: **0**
- Sürüklenme ölçülmüş ve commit iletisine geçmiş
- Faz görsel hedefi tutmuş, tolerans dışı görsel **0**
- Sayfa bütçesi yeniden ölçülmüş

### Faz 5 DoD

- Üç formatın dosyaları **üretilmiş**
- Gömülü olmayan font: **0**
- EPUB ≤ **3,0 MB** · PDF ≤ 650 MB
- İç marj sayfa sayısına göre doğru
- Kapak 160 piksel testinden geçmiş
- Metadata karakter sınırlarında · **AI beyanı hazır**
- **İki ebeveyn okuması** kayıtlı
- Prova kopyası elde tutulmuş
- `v1.0.0` etiketi

---

## 18. KDP üretimi

### Formatlar

| Format | Trim | Fiyat | Maliyet | Telif | Lansmanda |
|---|---|---:|---:|---:|---|
| **Ciltsiz** | 6×9 · s-b · krem | 16,99 $ | 3,76 $ | 6,43 $ | ✅ |
| **Ciltli** | 6×9 · s-b · case laminate | 26,99 $ | 8,41 $ | 7,78 $ | ✅ |
| **Kindle** | reflowable EPUB | 7,99 $ | — | 5,14 $ | ✅ |
| Büyük punto | 6×9 · 16 pt | 19,99 $ | — | — | ❌ (A6/K6) |

> **"Ciltli" ve "Hardcover" AYNI ŞEYDİR.** Tek bir üretim hattı vardır;
> ikinci bir hat kurulmaz.

> **Büyük punto** yol haritasında *"uzun vadeli genişleme"* listesindedir,
> lansman formatlarında değil. `editions.py`'de **tanımlı ama devre dışı**
> tutulur: hattı bozmadan bekler, kurucu isterse tek satır değişikliğiyle açılır.

### Format başına şartname

| | Ciltsiz | Ciltli |
|---|---|---|
| Trim | 6 × 9 inç | 6 × 9 inç |
| Sayfa sınırı | 24–828 | **75–550** |
| İç marj (230 s.) | 0,500" | 0,500" |
| Dış/üst/alt asgari | 0,25" (taşmasız) | 0,25" |
| Taşma | iç blokta **yok** (tam sayfa görsel yok) | yok |
| Kâğıt | krem | krem |
| Mürekkep | siyah-beyaz | siyah-beyaz |
| Kapak | taşmalı, KDP şablonundan | case laminate + **sarım (wrap)** |
| Dosya | PDF/X uyumlu, **gömülü font** | aynı |
| Görsel | 600 dpi gri TIFF | aynı |

**Kindle:** reflowable EPUB · içindekiler tablosu **zorunlu** (Virtual Voice
için de şart) · görseller 1200 px genişlik · **toplam ≤3,0 MB**.

### Kapak — markanın bilinçli esnetildiği tek yer

> *"Çocuk kitabı kapağı tür konvansiyonuna uymak zorundadır ve bizim 'koyu
> kodeks' dilimiz burada **işlemez**; daha aydınlık, daha karakterli, yaş
> aralığı köşede net bir kapak gerekir."*

Kapak gereksinimleri: yaş aralığı köşede okunur · başlıktaki "World" ve
"22 Cultures" küçük resimde okunabilir · **160 piksel testi** (küçük resimde
başlık okunuyor mu) · ciltli için sarım payı.

### Doğrulama zinciri

```
04_BUILD/editions.py       → telif ve sayfa sınırı doğrulaması
04_BUILD/page_budget.py    → sayfa sayısı ve maliyet etkisi
04_BUILD/convert_images.py → format bütçeleri, Kindle MB
.github/workflows/build.yml→ gömülü font · dosya boyutu · KDP kısıtları
```

---

## 19. KDP yükleme el kitabı

Adım adım, düğme düğme: [`KDP_UPLOAD_PLAYBOOK.md`](KDP_UPLOAD_PLAYBOOK.md).

Üç formatın her biri için 27 adım; **mevcut KDP arayüzü** ile
**değişebilecek arayüz** açıkça ayrılmıştır.

---

## 20. Risk kaydı

### Yol haritasının dört riski

| # | Risk | Düzey | Azaltma | Bu depodaki karşılığı |
|---|---|---|---|---|
| **R1** | Markalı rekabet (DK, NatGeo Kids, Usborne) | yüksek | Kapsam ve okuma deneyimiyle yarış, görsel yoğunlukla değil | Alt başlıktaki "22 cultures" **kapıya bağlı**: 22 kültür kilitlenmeden Faz 1 kapanmaz |
| **R2** | **Yaş uygunluğu** | orta | `AGE_POLICY.md` (yazım öncesi) + **iki ebeveyn okuması** (yayın öncesi) | `qa_age.py` · 17 kategori · `selftest` · Faz 5 kapısında imzalı okuma kaydı |
| **R3** | Marka esnemesi | orta | Aynı yazar adı, ayrı seri adı | `project_config.series` = "The Great Book of…" |
| **R4** | İade oranı | düşük-orta | Look Inside'da **gerçek** bölüm açılışı ve **gerçek** illüstrasyon | İlk görseller ebeveynin gördüğü ilk şey → `AGE_POLICY` § 2.17 promptlara iner |

### Bu projenin kendi riskleri

| # | Risk | Düzey | Azaltma |
|---|---|---|---|
| R5 | **Kısıtlılık taraması bir kültürü düşürür** ve 22 tutmaz | orta | Aday havuzu ≥26; 45/22 alt başlıkta yazdığı için **düşürülemez**, yerine başkası gelir |
| R6 | **Kültürel not kalıplaşır** ve okur onu atlamayı öğrenir | orta-yüksek | `qa_echo` muaf tutmaz + `qa_voice` şablon benzerliği arar (Bestiarium'un Faz 4 dersi) |
| R7 | **Sayfa bütçesi hedefi tutmaz** ve telif düşer | orta | Model deterministik ve kalibre edilir; sapma dolar cinsinden basılır |
| R8 | **Ses yanlış kurulur** ve 45 hikâye yanlış tonda yazılır | yüksek | Faz 1 tek hikâye yazar ve kurucu onayı ister; onaysız Faz 2 başlamaz |
| R9 | **Telaffuz yanlış** ve satın alma gerekçesi çürür | orta | Her telaffuzun kaynağı zorunlu; kaynaksız telaffuz yazılmaz |
| R10 | **Görsel tutarsızlığı** kitabı "derleme" gösterir | orta | Üslup gövdesi tek yerde; 68 promptta imza denetimi; ölçüm kalibre |
| R11 | **Manuscript sızar** | düşük ama geri dönülemez | İki hatlı koruma + kasıtlı sızıntı testi |

---

## 21. İnsan bağımlılıkları

CI ile üretilemeyen, **kurucunun yapması gereken** işler:

| # | Ne | Ne zaman | Bloklar |
|---|---|---|---|
| H1 | **A1 kararı** — manuscript nerede duracak | **Faz 1 başlamadan** | Faz 1 |
| H2 | `AGE_POLICY.md` onayı | **Faz 1 başlamadan** | Faz 1 |
| H3 | 22 kültür listesi onayı | Faz 1 | Faz 1 kapanışı |
| H4 | 45 hikâye listesi onayı | Faz 1 | Faz 1 kapanışı |
| H5 | Pilot hikâyenin **sesi** onayı | Faz 1 sonu | Faz 2 |
| H6 | A4 (vinyet yeri) ve A5 (bölüm mimarisi) | Faz 1 | Faz 4 dizgi |
| H7 | **68 ham görselin üretimi** (GPT Image) | Faz 2–4 | Faz 5 |
| H8 | **İki ebeveyn okuyucusu** | Faz 4 başlamadan | Faz 5 sürümü |
| H9 | Kapak sanat yönü onayı | Faz 5 | yayın |
| H10 | ISBN kararı (A9) | Faz 5 | yayın |
| H11 | Prova kopyası siparişi ve incelemesi | Faz 5 | yayın |
| H12 | KDP hesabı, fiyatlama, **AI beyanı** | Faz 5 | yayın |

> H7 hiçbir yazım fazını **bloklamaz** (Bestiarium D39 ile aynı gerekçe):
> hat hazır ve kalibre; ham girdi geldiği anda tek komut yeter.

---

## 22. Sürüm stratejisi

| Etiket | Faz | Ne içerir |
|---|---|---|
| `v0.0.1` | Bootstrap | altyapı · kapılar · CI · yol haritası · **yazım yok** |
| `v0.1.0` | Faz 1 | kapsam kilidi · 45 araştırma kaydı · pilot hikâye |
| `v0.2.0` | Faz 2 | 16/45 hikâye · 16 görsel |
| `v0.3.0` | Faz 3 | 31/45 hikâye · 40 görsel |
| `v0.4.0` | Faz 4 | **45/45 hikâye** · 68 görsel · editoryal inceleme |
| `v1.0.0` | Faz 5 | **yayına hazır KDP dosyaları** |

`release.yml` her etikette şunları doğrular: `.gate` seviyesi etiketle
tutarlı mı · `CHANGELOG.md`'de o sürümün bloğu var mı · **bütün kapılar
yeşil mi**. Üçü de tutmuyorsa sürüm oluşmaz.

> Bir faz **ancak etiketlenerek kapanır.** "Faz bitti" demek ölçülebilir
> bir şeydir.

---

## 23. Faz kapıları

Makine okunur: `.gate` (tek satır) + `project_config.json` → `gates`.

```
phase0 → phase1 → phase2 → phase3 → phase4 → phase5 → release
```

**Kurallar:**

- **Tek aktif kapı.** `.gate` bir satır taşır.
- **Kümülatif.** `phase1`'in şartları `phase3`'te de aranır. Kalite geriye
  gidemez.
- **Atlama yok.** `release.yml` etiket ↔ kapı tutarlılığını denetler.
- **Geri gitme yok.** `validate_structure` `.gate` ile
  `project_config.gates.current`'ın aynı olmasını şart koşar; ikisi de elle
  değiştirilir ve fark CI'da görünür.
- **Kapı gerçekten kilitliyor mu?** `selftest.py` `.gate`i okur ve **bir
  üstünün kapalı olduğunu** sınar. Sabit seviye varsaymaz — Bestiarium'un
  D20 kusuru buydu: "phase1 kapalı olmalı" varsayımı Faz 1 bitince kendini
  yanlışlıyordu.

---

## 24. Nihai teslim

Faz 5 sonunda `08_OUTPUT/` altında:

```
paperback/  interior.pdf · cover.pdf · validation-report.json
hardcover/  interior.pdf · cover.pdf · validation-report.json
kindle/     book.epub · cover.jpg · validation-report.json
            metadata.json · upload-checklist.md · release-manifest.json
```

Ve elde:

- Prova kopyası (ciltsiz + ciltli), okunmuş
- İki ebeveyn okuma kaydı, imzalı
- KDP metadata'sı hazır, **AI beyanı dâhil**
- `KDP_UPLOAD_PLAYBOOK.md` ile adım adım yükleme
- `v1.0.0` etiketi ve GitHub Release

---

## Bu belge nasıl değişir

Kurucu kararı → `DECISIONS.md` (`K##`) → bu belge → `CHANGELOG.md` →
ilgili kapı → `selftest` kurgusu.

Beş adımın hepsi yapılmazsa belge ile kapı ayrışır. **Ayrışan bir kapı ölü
kuraldır** ve ölü kural yanlış kuraldan tehlikelidir: yanlış kural hata
verir, ölü kural hiçbir şey demez.
