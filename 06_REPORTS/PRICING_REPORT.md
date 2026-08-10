# FİYATLANDIRMA RAPORU — LANSMAN ÖNERİSİ

> **The Great Book of World Myths** · 10 Ağustos 2026 · kapı `phase5`
>
> Bütün maliyet ve telif sayıları **ölçülen 234 sayfadan** ve KDP'nin
> **resmî tablolarından** hesaplanmıştır (`04_BUILD/editions.py`).
> Satış tahminleri **TAHMİNDİR** ve öyle etiketlenmiştir.
>
> ⚠ Bu rapor bir **öneridir**. `project_config.json` hâlâ yol
> haritasının fiyatlarını taşır; değiştirmek kurucu kararıdır.

---

## 1. Girdiler — hepsi ölçülmüş

| | Değer | Kaynak |
|---|---:|---|
| İç blok sayfa | **234** | `interior-build.json` (işlenmiş PDF'ten) |
| Trim | 6 × 9 inç · normal | `project_config.json` |
| Kâğıt / mürekkep | krem · siyah-beyaz | üretim |
| EPUB dosya boyutu | **2,772 MB** | `epub-build.json` |
| Pazar | **Amazon.com (USD)** | — |

### KDP baskı maliyeti (resmî tablo, Ağustos 2026)

```
ciltsiz  110–828 s : 1,00 $ + 0,012 $/sayfa → 1,00 + 2,808 = 3,81 $
ciltli   110–550 s : 5,65 $ + 0,012 $/sayfa → 5,65 + 2,808 = 8,46 $
```

Telif oranı: **%60** (liste fiyatı ≥ 9,99 $) · **%50** (altında).
Kindle: **%70** (2,99–9,99 $ bandı) eksi **0,15 $/MB teslim ücreti**.

---

## 2. Fiyat–telif tabloları

### 2.1 Ciltsiz · baskı maliyeti 3,81 $

| Liste | Telif | Katkı payı | Başabaş ACOS |
|---:|---:|---:|---:|
| 12,99 $ | 3,99 $ | %30,7 | %30,7 |
| 13,99 $ | 4,59 $ | %32,8 | %32,8 |
| **14,99 $** | **5,19 $** | **%34,6** | **%34,6** |
| 15,99 $ | 5,79 $ | %36,2 | %36,2 |
| **16,99 $** | **6,39 $** | **%37,6** | **%37,6** |
| 17,99 $ | 6,99 $ | %38,8 | %38,8 |
| 19,99 $ | 8,19 $ | %41,0 | %41,0 |

### 2.2 Ciltli · baskı maliyeti 8,46 $

| Liste | Telif | Başabaş ACOS |
|---:|---:|---:|
| 22,99 $ | 5,34 $ | %23,2 |
| 24,99 $ | 6,54 $ | %26,2 |
| 25,99 $ | 7,14 $ | %27,5 |
| **26,99 $** | **7,74 $** | **%28,7** |
| 29,99 $ | 9,54 $ | %31,8 |

### 2.3 Kindle · teslim ücreti 0,42 $ (2,772 MB × 0,15 $)

| Liste | Telif | Net oran |
|---:|---:|---:|
| 4,99 $ | 3,08 $ | %61,7 |
| 5,99 $ | 3,78 $ | %63,1 |
| **6,99 $** | **4,48 $** | **%64,1** |
| **7,99 $** | **5,18 $** | **%64,8** |
| 9,99 $ | 6,58 $ | %65,8 |
| ~~10,99 $~~ | ~~3,85 $~~ | **%35 — UÇURUM** |

> ### ⚠ KINDLE'DA 9,99 $ BİR DUVARDIR
>
> 9,99 $'ın **bir sent üstünde** telif oranı %70'ten **%35'e düşer**.
> 9,99 $ **6,58 $** kazandırır; 10,99 $ yalnızca **3,85 $**.
> **Bir dolar zam, telifin %41'ini siler.** Bu kitabın Kindle fiyatı
> hiçbir koşulda 9,99 $'ı geçmemelidir.

---

## 3. ÖNERİ

### 3.1 Lansman (ilk 90 gün ya da ilk 25 yorum)

| Format | **Öneri** | Telif | Baskı maliyeti | Katkı |
|---|---:|---:|---:|---:|
| Kindle | **6,99 $** | 4,48 $ | — | 4,48 $ |
| Ciltsiz | **14,99 $** | 5,19 $ | 3,81 $ | 5,19 $ |
| Ciltli | **26,99 $** | 7,74 $ | 8,46 $ | 7,74 $ |

### 3.2 Yerleşik fiyat (yorumlar geldikten sonra)

| Format | **Öneri** | Telif | Değişim |
|---|---:|---:|---:|
| Kindle | **7,99 $** | 5,18 $ | +0,70 $/kopya |
| Ciltsiz | **16,99 $** | 6,39 $ | +1,20 $/kopya |
| Ciltli | **26,99 $** | 7,74 $ | değişmez |

---

## 4. Gerekçeler

### Ciltsiz — neden 14,99 $ ile açılıp 16,99 $'a çıkmalı

Yol haritası 16,99 $ diyor ve **yerleşik fiyat olarak doğrudur**: 234
sayfa, 45 hikâye, 68 çizim, %37,6 başabaş ACOS ile reklam rahat çalışır.

Ama lansmanda kitabın **sıfır yorumu** vardır ve rafta DK ile Usborne'un
marka gücü karşısındadır. Bu kitabın tezi *"okunacak bir kitap, karıştırılacak
bir resimli kitap değil"* — yani rakibi renkli başvuru cildi değil, **bölüm
kitabı antolojisidir** ve o raf daha aşağıda fiyatlanır.

14,99 $ üç şeyi birden yapar:

1. **9,99 $ eşiğinin çok üstünde kalır** → telif oranı %60'ta kalır.
2. Kopya başına yalnızca **1,20 $** feda eder (5,19 $ / 6,39 $).
3. 26,99 $'lık ciltlinin yanında ciltsizi **açık ara mantıklı seçim**
   yapar — ciltli burada bir çapadır, bir hacim ürünü değil.

**Ne zaman 16,99 $'a çıkılmalı:** 25 doğrulanmış yorum ya da 90 gün,
hangisi önce gelirse. Zam tek seferde yapılmalı; kademeli zam sıralamayı
iki kez sarsar.

### Ciltli — neden 26,99 $ değişmiyor

Ciltli bu kitapta **hediye ve kütüphane formatıdır** ve alıcısı fiyata en
duyarsız olan segmenttir. Ayrıca 8,46 $'lık baskı maliyeti taban fiyatı
yukarı iter: 19,99 $'ta telif yalnızca **3,54 $** kalır.

26,99 $'ta katkı **7,74 $** ve başabaş ACOS **%28,7** — üç formatın en iyi
reklam matematiği. Yol haritasının rakamı burada düzeltme istemiyor.

### Kindle — neden 6,99 $ ile açılmalı

7,99 $ ile 6,99 $ arasındaki fark kopya başına **0,70 $**. Kindle bu kitapta
**keşif formatıdır**: siyah-beyaz çizimli, akışkan bir metin. Görevi para
kazanmak değil, ilk okurları ve ilk yorumları getirmektir.

6,99 $ hâlâ %64,1 net bırakır. **9,99 $'ın üstüne asla çıkılmamalıdır** (§ 2.3).

---

## 5. Taban ve tavan

| Format | Ekonomik taban | Gerekçe | Prim tavanı | Gerekçe |
|---|---:|---|---:|---|
| Ciltsiz | **12,99 $** | Altında başabaş ACOS %30'un altına iner; reklam kendini ödeyemez | **19,99 $** | Yorumsuz, siyah-beyaz iç bloklu bir çocuk kitabı bunun üstünde durur |
| Ciltli | **19,99 $** | Telif 3,54 $'a düşer — 8,46 $ maliyetle anlamsız | **29,99 $** | Üstü kütüphane bütçesinin dışına çıkar |
| Kindle | **4,99 $** | Altında telif reklamı kaldırmaz | **9,99 $** | **SERT SINIR** — bir sent üstü telifi %41 siler |

**Mutlak matematiksel başabaş** (telif = 0):
ciltsiz 6,35 $ · ciltli 14,10 $. Bunlar fiyat önerisi değil, **sıfır çizgisidir**.

---

## 6. Ne zaman yeniden bakılmalı

| Tetik | Eylem |
|---|---|
| 25 yorum ya da 90 gün | Ciltsiz 14,99 → 16,99 $ · Kindle 6,99 → 7,99 $ |
| Ciltli satış, ciltsizin **%15'inin altında** kalırsa (90 gün) | Ciltli 24,99 $'a indirilsin (telif 6,54 $) |
| Reklam ACOS **%30'un altında** kararlıysa | Ciltsizi 17,99 $'a taşımayı dene — talep esnekliği düşük demektir |
| İade oranı **%3'ü aşarsa** | Fiyat değil **beklenti** sorunudur: A+ içeriği ve açıklama gözden geçirilsin |
| KDP baskı maliyeti tablosu değişirse | `editions.py` tek parametre; bütün tablo yeniden hesaplanır |

---

## 7. Bu raporun sınırları

- Bütün telif ve maliyet sayıları **hesaplanmıştır** ve KDP'nin yayımlanmış
  tablolarına dayanır. Bunlar tahmin değildir.
- **Satış hacmi, dönüşüm oranı ve yorum hızı TAHMİNDİR** ve bu raporda
  sayısal bir hacim tahmini bilerek verilmemiştir: elde bir gün bile
  gerçek veri yoktur.
- Fiyat önerisinin kendisi bir **yargıdır**, ölçüm değil. Ölçüm olan
  kısım § 2'deki tablolardır; § 3 onlardan çıkarılmış bir tercihtir.
- Sayılar **yalnızca Amazon.com (USD)** içindir. Diğer pazarların kendi
  baskı tabloları vardır ve KDP onları liste fiyatından türetir.
- **Genişletilmiş dağıtım (Expanded Distribution)** hesaba katılmamıştır;
  telif oranı %40'a düşer ve bu kitapta önerilmez.
