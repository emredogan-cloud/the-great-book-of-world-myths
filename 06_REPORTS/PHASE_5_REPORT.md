# FAZ 5 · ÜRETİM HAZIRLIĞI — RAPOR

> **The Great Book of World Myths** · kapı `phase3` · 9 Ağustos 2026
>
> **DURUM: ÜRETİM DOĞRULANDI — FAZ 6'YA HAZIR.**
> `v1.0.0` ÇIKMADI ve Faz 5'te çıkmaz: K31 ile sürüm Faz 6'ya aittir.
>
> Bu rapor tek yetkili Faz 5 raporudur.

---

## 0. Tek bakışta

| | Hedef | Ölçülen | |
|---|---:|---:|---|
| Ham görsel | 68 | **68 / 68** | ✅ |
| Görsel eşlemesi | 68 | **68 / 68** | ✅ |
| Baskı türevi (600 dpi gri TIFF) | 68 | **68** | ✅ |
| Kindle türevi | 68 | **68** | ✅ |
| Web türevi (WebP) | 68 | **68** | ✅ |
| Görsel ölçümü kabul | 68 | **68 / 68** | ✅ |
| Ölçüm kalibrasyonu | geçsin | **26 / 26 · hata %0,00** | ✅ |
| Ciltsiz iç blok | üretilsin | **236 sayfa** | ✅ |
| Ciltli iç blok | üretilsin | **236 sayfa** | ✅ |
| Kindle EPUB | ≤3,0 MB | **1,95 MB** | ✅ |
| Gömülü olmayan font | 0 | **0** | ✅ |
| Sayfa ölçüsü | 6×9 inç | **432 × 648 pt** | ✅ |
| İç marj | ≥0,500" | **0,500"** (işlenmiş sayfadan) | ✅ |
| Dış/üst/alt marj | ≥0,25" | **≥0,44"** | ✅ |
| Kırpılan görsel | 0 | **0** | ✅ |
| Kültür kartı (K30) | 5 ayrı / 17 kuyruk | **5 / 17** | ✅ |
| Sayfa bütçesi sapması | ≤%5 | **%+2,6** (236 vs 230) | ✅ |
| Kapı testleri | geçsin | **83 / 83** | ✅ |
| Manuscript sızıntısı | 0 | **0** | ✅ |
| Yerel QA | yeşil | **BÜTÜN KAPILAR YEŞİL** | ✅ |
| CI | yeşil | **validate · images · build YEŞİL** | ✅ |
| Kapak promptu | hazırlansın | **7** | ✅ |
| A+ promptu | hazırlansın | **10** | ✅ |
| **İki ebeveyn okuması** | 2 | **0** | ⛔ **KURUCU (H8)** |
| **Kapak sanat yönü** | onay | **—** | ⛔ **KURUCU (H9)** |

---

## 1. Faz 5 kapsamı ve K31

Yol haritası § 16 Faz 5'i tek parça tarif eder: *"Üretim · Dizgi, KDP
Dosyaları ve Lansman."* Kurucu bu fazı **iki teslimata** böldü ve karar
`DECISIONS.md` § K31'e geçti:

- **Faz 5** — üretim hazırlığı: varlık işleme · iç blok dizgisi · prova ·
  doğrulama · metadata hazırlığı · kapak ve A+ prompt şartnamesi
- **Faz 6** — nihai KDP paketleme: kapak üretimi ve tipografisi · sırt
  hesabı · taşma/sarım · nihai Kindle paketi · ticari çıktı · `v1.0.0`

Yol haritasının Faz 5 **kapsamı değişmedi**; iki teslimata ayrıldı.
Gerekçe ölçülmüştür: iç blok, EPUB, metadata ve prompt şartnamesi kurucu
bağımlılıkları (H8 · H9 · A9) olmadan da üretilip doğrulanabilir. Tek fazda
tutmak, tamamlanabilir işi tamamlanamaz işe bağlar.

---

## 2. Faz 4'ten devralınan

| Devir | Durum |
|---|---|
| 45/45 hikâye · 22/22 kültür · 6/6 bölge | ✅ değişmedi |
| Sayfa modeli 232 · sapma %0,9 | ✅ gerçek dizgiyle sınandı (§ 8) |
| K30 kart mimarisi | ✅ korundu |
| D40 sürüklenme %+26,0 | ✅ ölçüldü, %+29,6 (§ 11) |
| **H7 — 68 ham görsel** | ✅ **KAPANDI** (§ 3) |
| **#33 "spider-shaped"** | ✅ **KAPANDI** (§ 10) |
| H8 — iki ebeveyn okuması | ⛔ açık |
| A6 · A7 · A9 | ⛔ açık |

---

## 3. Ham varlık envanteri

Kurucu 68 PNG teslim etti. `04_BUILD/asset_inventory.py` (Faz 5'te
yazıldı) tek tek saydı:

| Denetim | Sonuç |
|---|---|
| Dosya sayısı | **68 / 68** — 45 hikâye · 22 vinyet · 1 harita |
| PNG bütünlüğü (imza · chunk · CRC · IEND) | 68/68 sağlam |
| Bayt-birebir yinelenen | 0 |
| Kimlik çakışması | 0 |
| Yetim / eksik / tanınmayan | 0 / 0 / 0 |
| Boş veya neredeyse boş | 0 |
| Gerçek saydamlık | 0 (alfa var ama tamamen opak) |
| Renk kaçağı | 0 |
| Eşleme (`story_index.imageId` · `culture_index.vignetteId`) | 68/68 |

### 3.1 · İlk teslimatın dört kusuru

**① Ad sapması.** `story-43.png` — beklenen `story-043.png`. Ham dizin
değişmezdir (K5 · talimat § 32), dolayısıyla dosya yeniden adlandırılmadı;
**hat** düzeltildi (`imagespec.canonical_id`) ve sapma envanterde ayrı satır
olarak görünüyor. Sessiz bir düzeltme ikinci bir doğruluk kaynağı yaratırdı.

**② 45 hikâye görseli yanlış geometride.** 1024×1536 portre geldi;
şartname 3:2 yatay istiyor. **Kök sebep boyut seçimi değil, PROMPTTU** —
§ 4.

**③ `culture-008` yanlış kültür.** Hawai'i yuvasında bir **Fin** sahnesi
vardı (Väinämöinen ormanda kantele çalıyor), üstelik kare değil yatay.
Yani Hawai'i vinyetsiz, Fin ise iki kez temsil ediliyordu. Hiçbir otomatik
kalite kapısı bunu yakalayamaz: dosya kusursuzdu, yalnızca **yanlış
kültüre bağlıydı**. Envanterin eşleme denetimi tam bu sınıf içindir.

**④ `map-001` olgusal olarak yanlış.** Üretilen harita şu etiketleri
taşıyordu: **Haudenosaunee · Inca · Guaraní · Celtic · Aboriginal** —
beşi de kitabın kilitli 22 kültüründe **yok**. Buna karşılık **Korean ·
Hawaiian · Akan · Persian · Aztec · Finnish · Irish** eksikti.

> **`Aboriginal` etiketi yalnızca yanlış değil, KARARA AYKIRIYDI.**
> Yol haritası § 5 Avustralya Aborjin geleneklerini **kasıtlı olarak
> dışarıda bırakır** ve bu karar okura **arka maddede söylenir**. Kitabın
> ön maddesindeki harita, arka maddesindeki cümleyi yalanlıyordu.

---

## 4. Kök sebep: prompt

45 hikâye görselinin tamamı 1024×1536 geldi. O ölçü **birebir 6:9'dur** ve
sebebi promptun kendisiydi:

```
… upper half of a 6x9 inch page …
```

Üretici tam olarak bunu çizdi: bir **6×9 sayfa**, çizim üstte, altı boş.
İşaret, görselin içinde duracağı **sayfayı** tarif ediyordu; oysa
üreticiden istenen şey sayfa değil **görselin kendisidir**. Üreticiye
çizecek bir sayfa verilirse sayfa çizer.

Yeni işaret çizimin kendi geometrisini tarif eder ve "sayfa" kelimesini
hiç kullanmaz:

```
a standalone horizontal illustration in 3:2 landscape proportions,
the whole scene composed inside the frame with a clean margin of white
paper on all four sides
```

### 4.1 · İkinci kök sebep — sürekli ton

İlk teslimatın hikâye görselleri kalem gölgelemesiyle geliyordu:

| | orta ton payı (%60–200) |
|---|---:|
| Şartnameye uyan kurgu | **%0,0** |
| Kültür vinyetleri | **%1,8** |
| Hikâye açılışları (ilk teslimat) | **%13,9** |

Sürekli ton, PNG süzgeçlerinin kestiremediği bir gürültüdür ve Kindle
payını **3,0 MB bütçeye karşı 10,71 MB'ye** çıkarmıştı.

### 4.2 · Ölçülmüş bulgu: olumsuz liste uzadıkça tersine çalışır

Zemin sorununu olumsuz kısıtla çözmeye çalışmak **kusuru büyüttü**:

| Deneme | Eklenen | Sonuç |
|---|---|---|
| 1 | — | orta ton %15,2 |
| 2 | `no cream or beige tint, no sepia, no toned background` | **kahverengi zemin gradyanı** · mürekkep %60,6 · orta ton %42,8 |
| 3 | olumsuzlar KALDIRILDI, zemin kuralı **olumluya** taşındı | orta ton %10,9 ✅ |

Modern görsel modelleri olumsuzu zayıf, **olumluyu güçlü** işler;
istenmeyen şeyi adıyla anmak onu çağırır. Zemin kuralı artık
`flat pure white background` olarak **olumlu ve önde**; olumsuz liste
yalnızca **yaş politikası** kısıtlarını taşıyor (AGE_POLICY § 2.17 onları
zorunlu kılar ve hiçbiri kaldırılmadı).

---

## 5. Yeniden üretim

`04_BUILD/generate_images.py` — standart kütüphaneyle OpenAI Images
(karar K7: yeni bağımlılık yok), sert bütçe tavanı, dosya başına
doğrulama, eskisini silmeden arşivleme.

| | |
|---|---:|
| Yeniden üretilen | **47** (45 hikâye + `culture-008` + `map-001`) |
| Üretim ölçüsü | 1536×1024 (hikâye · harita) · 1024×1024 (vinyet) |
| Toplam API çağrısı | 55 (kalibrasyon denemeleri ve 6 yeniden deneme dâhil) |
| **Tahmini gider** | **3,423 $** |
| Kurucu tavanı | 4,00 $ · durma eşiği 3,50 $ |
| Durum | **eşikte durduruldu** — talimat § 5 |

**Eski dosyalar silinmedi**: `07_ASSETS/raw/superseded/20260809-phase5/`
altına taşındı. Yol prompt kütüphanesinin üç fazdır kurucuya söylediği
yoldur; uydurulmadı.

**Gizlilik.** `.env` `.gitignore` § 105'te, takip edilmiyor ve **git
geçmişine hiç girmemiş** (doğrulandı). Anahtar hiçbir yere basılmadı,
raporda yok, maliyet defterinde yok (defter tarandı: 0 eşleşme).

### 5.1 · Kısıtlılık taraması prompta indi

`culture-008` ilk yeniden üretimde bir **ki'i** (heiau tapınak figürü)
olarak geldi. Oysa `culture_index.hawaiian.restrictionNote` açıkça
*"heiau ritüel ayrıntısı KULLANILMAZ"* diyor ve kültürün kısıtlılık riski
**yüksek**, geleneği **yaşıyor**.

Konu elle yazılmadı; **dizine bağlandı**. `culture_index.json`'a
`vignetteSubject` alanı eklendi — kısıtlılık değerlendirmesi zaten orada
duruyor, vinyet konusu da orada durmalı. Hawai'i için kısıtsız ve
tanınabilir bir amblem seçildi: **yelkenli kano (waʻa)**. Diğer 21 kültür
etkilenmedi (alan yoksa genel konu kullanılır).

### 5.2 · Harita: işaretleri üretici koyamaz

Üretici 22 kültürün kim olduğunu **bilemez** — § 3.1 ④ bunun bedelini
gösterdi. Doğru mimari, talimat § 44–45'in haritaya uygulanmış hâlidir:

- **Üretici** etiketsiz zemin haritasını verir (kıtalar · adalar · pusula)
- **CLI** 22 işareti `culture_index.json → mapPoint` enlem/boylamından
  **deterministik** basar

Doğru cevap zaten depoda duruyordu ve modele sorulması gereksizdi. Bu
mimaride § 3.1 ④'teki hata sınıfı **yapısal olarak imkânsızdır**.

İzdüşüm çerçeveye değil **çizimin mürekkep sınırına** oturtulur; çerçeveye
göre hesaplayınca Mısır Levant'a, Zulu okyanusa düşüyordu. 22 işaretin
tamamı basılı sayfada gözle doğrulandı.

---

## 6. Hattın beş kusuru

Hepsi yalnızca **gerçek teslimat geldiğinde** görünür oldu; üçü de üç faz
boyunca yeşil yanmıştı. Ayrıntılı gerekçeler `DECISIONS.md` § Faz 5'te.

### 6.1 · Üç ölü kural

| # | Kural | Neden ölüydü | Bulunca ne oldu |
|---|---|---|---|
| ① | eksik ham görsel | `Result.ok()` **koşulsuz geçer**; ikinci argüman eşik değil metindir. "eksik: 40" yazan hat da yeşildi | `r.add` ile kapıya bağlandı |
| ② | Kindle 3,0 MB bütçesi | yalnızca `--calibrate` yolunda denetleniyordu, o yol da yalnızca **görsel yokken** koşuyor — bütçe sınanması gereken tek anda hiç sınanmıyordu | canlandırıldı; **ilk ölçümü 10,71 MB** (kopya başına **0,41 $** telif kaybı) |
| ③ | aynı bütçe, `--check` yolunda | CI `--check` çağırıyor; kural CI'da yine ölüydü | denetim yolu diskteki türevlerden ölçüyor |

### 6.2 · İki yanlış cetvel (Bestiarium B1'in bu projedeki hâli)

| Ölçü | Kusur | Düzeltme |
|---|---|---|
| `contrast` | `(p95−p5)/255` — mürekkep payı %5'in altındaysa **p5 de kâğıda düşer** ve "kâğıt − kâğıt ≈ 0" verir. `culture-001`in mürekkebi neredeyse saf siyah (medyan 11) ama ölçü **0,2157** diyor ve kapı reddediyordu | kâğıt seviyesi ile **mürekkebin medyanı** karşılaştırılıyor → 0,9529 |
| `minStrokePx` | 10. yüzdelik yalnızca **kurgu** görselde doğru (orada bütün çizgiler dik ve eşit kalınlıkta). Gerçek çizimde çapraz çizgiler bir satırı tek pikselde keser: `story-002`de 11.184 koşunun **4.529'u 1 piksel** ve hiçbiri çizgi değil | **medyan** tipik çizgiyi verir ve kurgularda **aynı** cevabı üretir — kalibrasyon bozulmadan geçerli |
| `asgari çözünürlük` | `raw_px`e (2400 px) bağlıydı; o sayı **600 dpi baskı hedefidir** ve üretici en fazla 1536 px verir. Kural **doğru üretilmiş her ham dosyayı** reddediyordu — 68/68 | ham `generator_px`e karşı ölçülür. **Baskı şartnamesi (3000×2000 @ 600 dpi) DEĞİŞMEDİ** |
| `kenar payı` | tek piksele bakıyordu; bilinçli kompozisyonu (çerçeveden taşan bir saçak) kusur sayıyordu | bandın **payına** çevrildi, **uyarı** sınıfına indi — kör nokta açmadığı selftest ile kanıtlanıyor (§ 6.4) |

### 6.3 · İki sessiz kusur

- **`resize(target)` oranı korumuyordu** ama üstündeki yorum *"kesin oranı
  koru"* diyordu. Şartnameye uyan girdide fark yok (ikisi de 3:2), bu
  yüzden üç faz görünmedi; 1024×1536 gelince 3000×2000'e **esnetecekti** —
  45 hikâye açılışının tamamı yatayda %120 genişleyecekti.
- **Alfa `convert("L")` ile sessizce atılıyordu.** Teslimatın 68 dosyası da
  RGBA geldi (alfa opak, zararsız) — ama saydamlık gerçekten kullanılan bir
  dosyada siyah lekeler üretirdi. Artık **beyaza düzleştiriliyor**.

### 6.4 · Kadraj kuralının indirilmesi kör nokta açmıyor

Kural uyarıya indirildi ve gerekçesi **ölçülmüştür**:

- **Baskı sonucu yok.** Görsel metin bloğunun içine yerleşir; kâğıt
  kenarına en az 0,5 inç vardır. İç blokta taşma zaten yasaktır.
- **Kural iki şeyi ayırt edemiyor.** 68 görselin 63'ü bandın %2'sinin
  altında; kalan 5'i sıkışık kadraj değil, **bilinçli kompozisyon**.
- **Gerçek kusur başka kuralla yakalanıyor.** `edge_bleeding` kurgusu
  mürekkep yoğunluğundan düşüyor: **0,3121 > 0,22**. `image_selftest`
  bunu artık **açıkça sınıyor** — indirme ancak başka bir kural aynı
  kusuru yakalıyorsa meşrudur.

Uyarı veren beş görsel: `story-004` · `story-021` · `story-031` ·
`story-038` · `story-042`.

---

## 7. Görsel türevleri ve Kindle bütçesi

| Format | Ölçü | Adet | Toplam |
|---|---|---:|---:|
| Baskı | 3000×2000 · 1800×1800 · 6450×4300 · **gri TIFF 600 dpi** | 68 | **117 MB** (KDP sınırı 650 MB) |
| Kindle | 1200×800 · 800×800 · 1200×800 · **1 bit PNG 300 dpi** | 68 | **1,80 MB** |
| Web | 1400×933 · 900×900 · 2000×1333 · kayıpsız WebP | 68 | 13 MB |

### 7.1 · Kâğıt gürültüsünün temizlenmesi

Teslim edilen dosyaların "beyaz" zemini beyaz **değildi**: `culture-001`
zemininin yalnızca **%1,4'ü** saf beyaz, %93'ü 250–254 arasına yayılmış bir
benek. Üç sonucu vardı ve üçü de gerçek: baskıda **gri sis**, sıkışmanın
**çökmesi**, ölçümün **yanılması**.

Müdahale en az olanıdır: eşiğin (246) **üstü** beyaza kenetlenir, altındaki
hiçbir ton değişmez. Doğrusal yeniden ölçekleme denendi ve **reddedildi**:
orta tonları da açar, yani çizimin kendi gölgesini soldurur.

Tek başına bu adım Kindle payını **10,11 → 5,62 MB**'ye indirdi.

### 7.2 · Çizgi sanatı 1 bittir

Hat, Kindle türevini üç faz boyunca `quantize(colors=16)` ile üretiyordu.
O seçim Bestiarium D27'den geliyor ve **tonlu** sanat için doğrudur. Ama
bu kitabın şartname dili tonlu değil, **çizgidir**.

Gerçek görselle ölçüldü (`story-001`, 1200×800):

| Kodlama | Dosya | 45 hikâyede |
|---|---:|---:|
| 16 renk | 242 KB | 11,2 MB |
| **1 bit** | **33 KB** | **1,5 MB** |

Yedi kat fark ve **görünür kayıp yok** — eşiklenmiş çıktı 16 renkli
referansla yan yana konduğunda çizgileri birebir taşıyor. Kaybedilen tek
şey kenar yumuşatmasının gri pikselleriydi ve Kindle'ın e-ink ekranı
onları zaten göstermiyor.

> ⚠ **`quantize(colors=2)` KULLANILMADI.** Denendi ve **boş görüntü**
> üretti (mürekkep 0,0000): median-cut, piksellerin %85'i beyaz olduğu için
> **iki beyaza yakın renk** seçiyor. Doğru araç **eşiklemedir**. Sessizce
> boş sayfa basacak türden bir kusurdu ve ölçülmeden fark edilmezdi.

**Baskı değişmedi:** iç blok hâlâ 600 dpi **gri** TIFF'tir.

---

## 8. İç blok — ciltsiz ve ciltli

`04_BUILD/interior.py` (Faz 5'te yazıldı). `proof_interior.py`'nin yerine
geçmez: o bir **mühendislik provasıdır** ve görsel yerine çerçeve çizer.

| | Ciltsiz | Ciltli |
|---|---:|---:|
| Sayfa | **236** | **236** |
| KDP sınırı | 24–828 ✅ | 75–550 ✅ |
| Sayfa çift mi | ✅ | ✅ |
| Trim | 432 × 648 pt = 6×9 inç ✅ | ✅ |
| Gömülü olmayan font | **0** ✅ | **0** ✅ |
| Yerleşen görsel | **68 / 68** | **68 / 68** |
| Kırpılan görsel | **0** | **0** |
| Dosya | 121 MB (< 650 MB) ✅ | 121 MB ✅ |

**Font:** Liberation Serif (Regular · Bold · Italic), üçü de **gömülü ve
alt kümelenmiş**. Seçim tipografi zevki değil **fiyat modelinin
parametresidir**: K27 yazı karakterinin kelime/sayfa'yı %21 oynattığını
ölçmüştü ve model Times/Liberation metriğiyle kalibre edildi. Kitabın
ihtiyaç duyduğu bütün diakritikleri taşıyor (ā · ō · ī · ʻokina · U+2019 ·
em dash) — basılı sayfada doğrulandı (`Ásgarðr` · `Âu Cơ` · `Bhagīratha` ·
`Cú Chulainn`).

### 8.1 · Üretilmiş PDF'in kendisi denetlendi

Talimat § 21: *"Yalnızca CSS/belge ayarlarına güvenmeyin. İşlenmiş
sayfaları ölçün."* İki dış araçla yapıldı ve **ikisi de gerçek kusur
buldu**:

- **`pdffonts` Helvetica'yı gömülü değil olarak listeledi** — tek harf
  Helvetica çizilmeden. reportlab her sayfanın açılış durumunu base-14
  fontla yazar ve **sayfa başında `setFont` çağırmak yetmez**: açılış
  durumu ondan önce yazılıyor. Kaynağı `Canvas(initialFontName=…)`.
  KDP şartı "gömülü olmayan font: 0" idi ve sessizce düşüyordu.
- **`pdfinfo` 235 sayfa dedi, iç sayaç 236.** Tamamen boş son sayfa PDF'e
  yazılmıyordu ve **tek/çift denetimi yanlış sayı üzerinde** koşuyordu.

### 8.2 · Marjlar işlenmiş sayfadan ölçüldü

Sayfalar ghostscript ile rasterize edildi ve mürekkebin trim kenarına
uzaklığı ölçüldü (9 sayfa örneklendi):

| | Şart | Ölçülen |
|---|---|---|
| İç marj (tek sayfa solda, çift sayfa sağda) | ≥0,500" | **0,500"** |
| Dış · üst · alt | ≥0,25" | **≥0,44"** |
| Taşma | yok | yok |

### 8.3 · Model ↔ gerçek uzlaştırması

Fark tahmin edilmedi, **kalem kalem çıkarıldı**:

| Bileşen | Model | Gerçek | Fark |
|---|---:|---:|---:|
| Ön madde | 14 | 14 | 0 |
| Bölüm açılışları | 12 | 12 | 0 |
| Kültür kartı (ayrı sayfa · K30) | 5 | 5 | 0 |
| Gövde | 180 | 178 | **−2** |
| Arka madde | 21 | 25 | **+4** |
| **Toplam** | **232** | **236** | **+4** |

Gövde modelin altında çünkü üç hikâye 4 değil **3 sayfada** dizildi. Arka
madde modelin üstünde çünkü telaffuz (180 kayıt) ve "kim kimdir"
(138 madde) gerçek dizgide modelin verdiğinden fazla yer tutuyor.

**Modelde satırı olmayan 14 boş sayfa var:** "sağ sayfada başla"
konvansiyonunun ürettiği 13 sayfa + tek/çift tamamlaması 1. Bunlar gerçek
dizgide vardır ve **sayfa sayısına, dolayısıyla fiyat modeline girerler**.
Model bileşen sayar, konvansiyon saymaz — fark buradan geliyor.

**Ekonomik sonuç:** 236 sayfa · hedeften **%+2,6** (tolerans %5) ·
ciltsiz baskı maliyeti 3,83 $ · **ciltsiz telif 6,36 $** (pozitif).

### 8.4 · Kültür kartı — K30 gerçek dizgide

5 kart kendi sayfasında, 17 kart kuyrukta. **Biri** (`inuit`) kuyruğa
sığmayıp sonraki sayfaya aktı — ama o sayfa hikâyenin **faturalanan
dördüncü sayfasıdır**, yani K27'nin bütün argümanı gereği **zaten
ödenmiştir**. Kusur değildir ve rapor bunu ayrı alan olarak tutuyor
(`flowedToNextPage`), çünkü doğru payda kullanılan sayfa değil
**faturalanan kapasitedir** — Faz 4'ün kendi düzeltmesi.

### 8.5 · Görsel yerleşimi ve DÜRÜST çözünürlük

| | Ölçülen |
|---|---:|
| Görsel kutusu | 4,875 × 3,667 inç (sayfanın üst yarısı) |
| Çizilen genişlik | **4,875 inç** (kutuyu dolduruyor) |
| Kutu doluluğu | **%88,6** |
| Türev çözünürlüğü | 615 dpi |
| **Optik çözünürlük** | **315 dpi** |

> **615 dpi yazmak yanlış olurdu.** Baskı TIFF'i 3000 px'tir ve 4,875 inçe
> basılınca 615 dpi verir — ama o piksellerin bir kısmını **hat üretti**;
> ham dosya 1536 px'ti ve büyütme bilgi eklemez. `opticalDpi` hamın **kendi**
> pikselini basılan inçe böler. Kâğıda gerçekten düşen bilgi **315 dpi**'dır:
> KDP'nin 300 dpi asgarisinin **üstünde**, projenin 600 dpi şartnamesinin
> **altında**. Şartname düşürülmedi; üreticinin tavanı 1536 px.

---

## 9. Kindle EPUB

| | Ölçülen |
|---|---:|
| Toplam | **1,946 MB** (bütçe 3,0 MB) ✅ |
| Görsel payı | 1,80 MB |
| Metin + iskelet | 0,13 MB |
| Belge | 59 |
| Hikâye | 45 / 45 |
| Kültür kartı | 22 / 22 |
| Görsel | 68 / 68 |
| İçindekiler | **nav.xhtml + toc.ncx** (ikisi de) ✅ |
| Kırık görsel bağı | 0 |
| Bozuk XML | 0 |
| OCF (`mimetype` ilk ve sıkıştırmasız) | ✅ |

İçindekiler **iki biçimde de** yazılır: yol haritası § 18 onu Virtual
Voice için de zorunlu kılıyor ve birini yazıp diğerini atlamak cihaz
filosunun bir kısmında içindekileri yok eder.

**Metin payı ölçüldü (0,13 MB) ve kalibrasyon tahmini (0,60 MB) dört kat
muhafazakârdı.** İki sayı artık ayrı tutulmuyor: `convert_images.py`
ölçülmüş değeri EPUB raporundan okuyor.

---

## 10. #33 "spider-shaped" — kapandı

Faz 4 bu deyimi *"ikinci bir göz"* için işaretlemişti. Arandı ve
**doğrulanamadı**: hiçbir kaynak Akan konuşurlarının fazla kurnaz birine
*"örümcek biçimli"* dediğini göstermiyor.

Doğrulanan şey **başka ve daha güçlü**: Rattray (*Akan-Ashanti Folk-Tales*,
Clarendon Press, 1930) Akan konuşurunun **bütün** masalları `anansesem`
(örümcek hikâyeleri) diye sınıfladığını, örümcek hikâyede geçmese bile
açıkça yazar. **Kaynak zaten hikâyenin künyesinde duruyordu.**

Proza ve kültürel not doğrulanmış olguyla değiştirildi; iddia
`factualClaims`e kaynağıyla kaydedildi. Metin kapıları düzeltmeden sonra
yeniden koştu: `qa_voice` ilk denemede **boşluklu em dash** yakaladı
(K28 boşluksuz kullanır) ve cümle yeniden kuruldu.

**Uydurulmuş bir şey eklenmedi, uydurulmuş bir şey de bırakılmadı.**

---

## 11. Sürüklenme

`qa_drift`: **%+29,6** · uyarı eşiği %20 · hata eşiği %35 → **kapı yeşil**.

Faz 4 bunu %+35,4'ten %+26,0'a indirmiş ve kalanı **bilerek bırakmıştı**:
son 14 hikâye kısadır ve Akan · Zulu · Inuit · Maya · Aztek · Polinezya
anlatıları sözlü kayda daha yakın, bilerek daha yalın bir sözcük dağarcığı
kullanır. Bu **kategori (A) — kasıtlı kültürel/anlatısal fark**.

Faz 5 ölçtü ve **mekanik düzeltme yapmadı**. Kurucu talimatı açık:
*"mekanik kelime değiştirme… kullanma. Metin kalitesi > metrik."* Sayıyı
%20'nin altına indirmek yalnızca kültürel sesleri tekdüzeleştirerek
mümkündü; talimat § 14 bunu açıkça yasaklıyor.

---

## 12. Metadata paketi

`04_BUILD/metadata.py` → `08_OUTPUT/metadata.json` ·
`08_OUTPUT/upload-checklist.md`

| Alan | Değer | Sınır |
|---|---|---:|
| Başlık | The Great Book of World Myths | 29/200 ✅ |
| Alt başlık | 45 Stories… 22 Cultures… (Ages 8–12) | 96/200 ✅ |
| Açıklama | 1.905 karakter | 4000 ✅ |
| Anahtar kelime | **7 / 7** | ≤50 kr ✅ |
| Kategori | 3 / 3 | ✅ |
| Yaş aralığı | 8–12 (BISAC 8-12 · sınıf 3-7) | ✅ |

Alt başlıktaki **45** ve **22** sayıları envanterle karşılaştırılıp kapıya
bağlandı: alıcı tam o iki sayıyı tarıyor (yol haritası R1).

**UYDURULMAYANLAR — dördü de açıkça kırmızı duruyor:**

| Alan | Durum |
|---|---|
| **ISBN** (A9) | yer tutucu · uydurulmadı (talimat § 41) |
| **KDP Select** (A7) | karar verilmedi · **kayıt yapılmadı** (§ 40) |
| **Yazar adı** | yol haritası "Codex serisiyle aynı" diyor, ad depoda yok |
| **AI beyanı** | metin **AI-generated** · görsel **AI-generated** olarak hazırlandı, **kurucu onayı yok** — hukuki bildirimi ajan veremez |

Emin olunmayan **BISAC kodu uydurulmadı**; KDP'nin kendi kategori
seçicisine bırakıldı (KDP 2023'ten beri zaten ham kod değil ağaçtan seçim
istiyor).

---

## 13. Kapak ve A+ prompt şartnamesi

Talimat § 26–30. `04_BUILD/coverspec.py` + `make_prompts.py`.

| Aile | Adet |
|---|---:|
| **Mevcut kitap görseli promptu** | **68 / 68** (değişmedi) |
| **Yeni kapak promptu** | **7** |
| **Yeni A+ promptu** | **10** |

> **Bunlar 68'e DÂHİL DEĞİLDİR** (talimat § 29). Ayrı bir ticari varlık
> ailesidir ve kimlik çakışması kapıya bağlandı.

**Kapaklar:** ciltsiz ön · ciltsiz tam sarım · **ciltli sarım (ayrı
dosya)** · iki ön kapak varyantı · arka kapak paneli · **160 piksel testi**.

**A+ modülleri uydurulmadı**: her kayıt gerçek bir Amazon standart
modülüne ve gerçek piksel ölçüsüne bağlı — Image Header with Text
(970×600) · Image & Light Text Overlay (970×300) · Four Image & Text
(220×220) · Three Images & Text (300×300) · Single Image & Sidebar
(300×400) · Single Left Image (300×300) · Company Logo (600×180).

**İki kural kapıya bağlandı:**

- **Kapak iç bloğun üslup gövdesini taşımaz.** Yol haritası § 18: *"çocuk
  kitabı kapağı… bizim 'koyu kodeks' dilimiz burada işlemez."* Sızarsa CI
  kırmızı yanar.
- **Tipografi üretilmez.** 17 promptun 17'sinde `typography: post`. Kesin
  başlık, alt başlık, yaş aralığı ve sırt yazısı **CLI ile sonradan**
  basılır (§ 44–45) ve prompt yalnızca **yer ayırır**.

**Kütüphanenin bütünlüğü:** yeni bölümler dosyanın **SONUNA** eklendi
(§ 28). 68 iç prompt değiştirilmedi, yeniden sıralanmadı, silinmedi.
**170 kopyalama düğmesi ↔ 170 blok**, yetim yok; HTML etiket dengesi
doğrulandı. Sırt genişliği **ölçülmüş sayfa sayısından** türetiliyor
(236 → 0,590"), modelden değil.

---

## 14. Kapı sonuçları

| Kapı | Sonuç |
|---|---|
| `validate_spec --gate phase3` | ✅ 65 |
| `validate_structure` | ✅ 37 · 2 uyarı |
| `validate_research` | ✅ 3 |
| **`selftest`** | ✅ **83 / 83** |
| **`image_selftest`** | ✅ **26 / 26** · hata %0,00 (Faz 4: 12) |
| `qa_length` · `qa_age` · `qa_readability` | ✅ |
| `qa_voice` · `qa_echo` · `qa_diacritics` | ✅ |
| `qa_crossref` | ✅ 11 |
| `qa_drift` | ✅ %+29,6 |
| `editions` · `page_budget` | ✅ |
| **`asset_inventory`** | ✅ |
| **`convert_images`** | ✅ 72 |
| **`images`** | ✅ **68 / 68 kabul** |
| **`interior`** | ✅ 23 |
| **`epub`** | ✅ 12 |
| **`metadata`** | ✅ 10 · 4 uyarı (kurucu alanları) |
| `make_prompts` · `make_index` · `update_docs` | ✅ |
| `calibrate_pages` · `proof_interior` · `research_gen` | ✅ |
| Manuscript sızıntısı | ✅ **0** |

**Yerel:** `BÜTÜN KAPILAR YEŞİL · kapı seviyesi phase3`
**CI:** `validate` ✅ · `images` ✅ · `build` ✅

---

## 15. Kurucu bağımlılıkları

| # | Ne | Durum | Neyi bloklar |
|---|---|---|---|
| **H7** | 68 ham görsel | ✅ **KAPANDI** | — |
| **H8 / A8** | **İki ebeveyn okuması** | ⛔ **0 / 2** | `v0.4.0` · kapı `phase4` |
| **H9** | **Kapak sanat yönü onayı** | ⛔ | Faz 6 kapak üretimi |
| **A6** | Büyük punto | ⛔ açık | — (devre dışı, hattı bozmuyor) |
| **A7** | KDP Select | ⛔ açık | yayın · **kayıt yapılmadı** |
| **A9** | ISBN | ⛔ açık | yayın metadata'sı |
| — | Yazar adı | ⛔ açık | kapak · künye · metadata |
| — | AI beyanı onayı | ⛔ açık | KDP formu |

> **H8 uydurulamaz ve uydurulmadı.** Ajan iki okuyucu üretemez. Kapı
> Faz 4'te yazıldı ve iki gerçek okuma kaydı gelene kadar **kasıtlı olarak
> kırmızı** duruyor. Faz 5 üretim işini **bloklamadı** (talimat § 5) ama
> kapıyı da **kapatmadı**.

---

## 16. Bilinen sınırlar

Bunlar kusur değil, **ölçülmüş ve kabul edilmiş** sınırlardır:

1. **Optik çözünürlük 315 dpi** (şartname 600, KDP asgarisi 300). Üreticinin
   tavanı 1536 px. Şartname düşürülmedi; `asset_inventory` bunu her koşuda
   uyarı olarak basıyor.
2. **Beş görselde çizim dış banda giriyor** (§ 6.4). Kompozisyon tercihi;
   baskı sonucu yok. Bütçe eşiğinde durulduğu için yeniden üretilmedi.
3. **Harita tek sayfada.** Model iki sayfa ayırıyor (harita + anahtar) ve
   ikisi de kullanılıyor; gerçek açık-sayfa yayılımı Faz 6'nın işi.
4. **Vinyet üslubu iki nesilden.** 21 vinyet ilk teslimattan, `culture-008`
   yeni üslupla. Ölçülen fark küçük (vinyetler zaten seyrek çizgi) ama
   kurucu isterse 22'si birlikte yenilenebilir (≈0,92 $).

---

## 17. Faz 6'ya devreden

**Hazır girdiler:**

- `07_ASSETS/processed/print/` — 68 × 600 dpi gri TIFF (117 MB)
- `07_ASSETS/processed/kindle/` — 68 × 1 bit PNG (1,80 MB)
- `07_ASSETS/processed/web/` — 68 × kayıpsız WebP (13 MB)
- `08_OUTPUT/paperback/interior.pdf` · `08_OUTPUT/hardcover/interior.pdf` — 236 sayfa
- `08_OUTPUT/kindle/book.epub` — 1,95 MB
- `08_OUTPUT/metadata.json` · `upload-checklist.md`
- `07_ASSETS/IMAGE_PROMPT_LIBRARY.html` — 68 + 7 kapak + 10 A+

**Faz 6'nın işi:**

1. Kapak görsellerinin üretimi (H9 onayından sonra)
2. Kapak tipografisinin **CLI ile** basılması — üretilmez (§ 44)
3. Sırt hesabının **KDP'nin kendi şablonundan** doğrulanması (236 sayfa →
   0,590" krem; Faz 5 hesabı prompt şartnamesi içindir)
4. Taşma ve ciltli sarım
5. A+ modüllerinin üretimi ve metninin sonradan basılması
6. Nihai KDP paket doğrulaması
7. Prova kopyası siparişi (H11)
8. `v1.0.0` etiketi ve GitHub Release

**Faz 6 başlamadan kapanması gerekenler:** H8 · H9 · A9 · yazar adı ·
AI beyanı onayı.

---

## 18. Definition of Done — Faz 5

| Ölçüt | Durum |
|---|---|
| 68 ham varlık envanterlendi | ✅ |
| 68 varlık eşlendi | ✅ |
| Ham varlıklar korundu (eskisi `superseded/` altında) | ✅ |
| Baskı · Kindle · web türevleri | ✅ 68 × 3 |
| Görsel ölçümü ve tutarlılık raporu | ✅ 68/68 kabul |
| `image_selftest` | ✅ 26/26 |
| Tam iç blok dizildi | ✅ |
| Ciltsiz · ciltli iç blok | ✅ 236 sayfa |
| Kindle EPUB | ✅ 1,95 MB |
| Fontlar gömülü | ✅ 0 gömülmemiş |
| Marjlar · sayfa ölçüsü · sayfa sayısı | ✅ işlenmiş sayfadan |
| Görsel çözünürlüğü | ✅ ölçüldü ve **dürüst** raporlandı (315 dpi) |
| Kırpılma · beklenmedik boş sayfa | ✅ 0 |
| K30 korundu · harita · telaffuz · sözlük yerinde | ✅ |
| Metadata paketi | ✅ |
| Manuscript sızıntısı | ✅ 0 |
| Tam QA | ✅ bütün kapılar yeşil |
| **CI** | ✅ **yeşil** |
| Kapak promptları | ✅ 7 |
| A+ promptları | ✅ 10 |
| Promptlar kütüphanenin SONUNA eklendi | ✅ |
| Mevcut 68 prompt korundu | ✅ |
| Faz 6 devri belgelendi | ✅ |
| Kurucu bağımlılıkları dürüst belgelendi | ✅ |
| **Sahte ebeveyn okuması yok** | ✅ **0 / 2 açıkça kırmızı** |

---

## 19. Durum

**ÜRETİM DOĞRULANDI — FAZ 6'YA HAZIR.**

**TİCARİ KARAR BEKLİYOR:** ISBN (A9) · KDP Select (A7) · yazar adı ·
AI beyanı onayı.

**İNSAN GİRDİSİ BEKLİYOR:** iki ebeveyn okuması (H8) · kapak sanat yönü (H9).

Bu Faz 5 **nihai KDP paketi değildir** ve öyle olduğunu iddia etmez.
Kapak yok, sırt basılmadı, KDP'ye hiçbir şey yüklenmedi, hiçbir sürüm
etiketlenmedi.

---

*Ölçümlerin ham hâli `06_REPORTS/tracked/` altındadır ve hepsi yeniden
üretilebilir. Görsel üretiminin maliyet defteri
`06_REPORTS/tracked/image-generation-ledger.json` — sır içermez.*
