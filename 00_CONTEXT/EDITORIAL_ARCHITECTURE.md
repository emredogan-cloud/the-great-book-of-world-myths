# EDITORIAL ARCHITECTURE — kitabın yapısı

> Bu belge kitabın **fiziksel ve editoryal mimarisini** taşır: bölümler,
> hikâye yerleşimi, ön/arka madde, sayfa modeli.
>
> Sayfa modelinin kendisi kod olarak `04_BUILD/page_budget.py`'dedir; bu
> belge o modelin **editoryal gerekçesini** yazar.
>
> Yazıldı: 8 Ağustos 2026 · Bootstrap
> Güncellendi: Faz 1 · **A4 → K27 ve A5 → K26 KARARA BAĞLANDI**

---

## 0. Faz 1 kararları — ölçümle verildi

**A5 → K26 · Bölüm mimarisi: BÖLGESEL.** Altı bölge, 45 hikâye, 22 kültür.
Bölgesel yapı yol haritasının zorunlu kıldığı tek görselle (dünya haritası)
birebir konuşur. Bölümler `01_RESEARCH/story_index.json` → `parts[]`
içindedir ve `validate_spec.py` her hikâyenin bölüm referansını denetler.

| # | Bölüm | Kültür | Hikâye |
|---:|---|---:|---:|
| 1 | The Wine-Dark Sea and the Frozen North | 4 | 10 |
| 2 | Between the Two Rivers | 3 | 6 |
| 3 | Where the Sun Comes Up | 5 | 10 |
| 4 | The Long River and the Forest Road | 4 | 8 |
| 5 | Ice, Maize, and the High Cold Mountains | 4 | 7 |
| 6 | The Sea Between the Islands | 2 | 4 |

**A4 → K27 · Kültür kartı: HİKÂYE KUYRUĞUNDAKİ BOŞLUKTA — şık (f).**

Bu karar bir tercih değil, bir **ölçümün sonucudur** ve bootstrap'ın kendi
önerisini çürütmüştür.

### Ölçümün bulduğu şey

`04_BUILD/calibrate_pages.py` pilot hikâyenin **gerçek prozasını** gerçek
metin bloğuna (4,875″ × 7,5″), gerçek tipografiyle (12/16,5 pt) ve gerçek
yazı karakteri genişlik tablolarıyla dizdi:

| | Tahmin | **Ölçüm** | Fark |
|---|---:|---:|---:|
| Kelime/sayfa | 361,1 | **357,5** | −%1,0 |
| Karakter/kelime | 5,4 | **5,349** | −%0,9 |
| Genişlik oranı | 0,48 | **0,4895** | +%2,0 |

**Tipografi tahmini iyiydi.** Asıl sürpriz başka yerdeydi: **yazı karakteri
seçimi kelime/sayfa'yı %21 oynatıyor** (DejaVu Serif 282,8 · Times/Liberation
Serif 357,5). Yani sayfa bütçesinin en büyük belirsizliği model hatası değil,
**Faz 5'te verilecek yazı karakteri kararıdır** — ve bu, ölçüm yapılmadan
görülemezdi.

### Bootstrap'ın önerisi neden düştü

Bootstrap (a′) şıkkını öneriyordu: kültür kartı açık sayfa, **3 sayfa/hikâye**,
226 sayfa. O öneri `wordsPerPage ≈ 420` varsayımına dayanıyordu.

Ölçüm 357,5 verdi. 3 sayfa/hikâye için **≥380 kelime/sayfa** gerekiyor ve
12 pt bir **yaş kararıdır** (konfor değil): 8–12 yaş için 12/16,5 pt bölüm
kitabı normudur ve küçültülemez. Dolayısıyla **4 sayfa/hikâye kilitlidir**
ve (a′) 226 değil **272 sayfaya** çıkar — bütün şıkların en kötüsü.

### Kararın dayandığı boşluk

Ölçüm, ödenen ama kullanılmayan bir alan buldu:

```
hikâye içeriği   3,219 sayfa  ──┐
faturalanan      4,000 sayfa    │  boşluk 0,781 sayfa = 25 satır
                              ──┘  × 45 hikâye = 35 SAYFA, zaten ödeniyor
```

Kültürel not (~4 satır) düşüldükten sonra **~21 satır** kalır. Kültür kartı
(vinyet ≈ 10 satır + üç cümle ≈ 3 satır + harita işareti ≈ 2 satır ≈ **15
satır**) oraya **sığar**.

### Sonuç

| Şık | Sayfa | Hedeften | Ciltsiz telif | 22 vinyet görünür mü |
|---|---:|---:|---:|---|
| **(f) kuyruk boşluğu ← KARAR** | **228** | **%0,9** | **6,46 $** | ✅ evet |
| (b′) kart yok, vinyet başlıkta | 228 | %0,9 | 6,46 $ | ❌ süse döner |
| (a) tam sayfa kart | 250 | %8,7 | 6,19 $ | ✅ evet |
| (a′) açık sayfa kart | 272 | %18,3 | 5,93 $ | ✅ evet |

**(f) tek şıktır ki hem hedefi tutturur hem 22 vinyeti görünür bırakır.**
Bedeli Faz 5'e düşer: dizgi daha zordur, çünkü kart hikâyenin son sayfasını
paylaşır.

> `page_budget.py` içinde `culture_card_pages = 0` yazar. **Bu "kart yok"
> demek değildir** — 22 kartın hepsi vardır, hiçbiri EK SAYFA tüketmez.

---

## 1. Kitabın şekli

| | |
|---|---|
| Trim | 6 × 9 inç (KDP normal trim) |
| Hikâye | 45 |
| Kültür | 22 |
| Hikâye uzunluğu | ~950 kelime |
| Gövde puntosu | 12 pt / 16,5 pt satır aralığı |
| Sayfa hedefi | ~230 |
| Sürümler | ciltsiz · ciltli · Kindle (üçü de lansmanda) |

**12 pt bir konfor kararı değil, bir yaş kararıdır.** Yetişkin cildi 10,5–11
pt kullanır. 8–12 yaş bölüm-kitabı normu 12/16,5'tir ve bunun altına inmek
sayfa kazandırır ama okuru kaybeder.

---

## 2. Hikâye sayfasının geometrisi

```
┌─────────────────────────────┐
│                             │
│      AÇILIŞ İLLÜSTRASYONU   │   ← sayfanın üst yarısı
│         (siyah-beyaz)       │
│                             │
├─────────────────────────────┤
│  HİKÂYE BAŞLIĞI             │
│  kültür · bölge             │
│                             │
│  Metin buradan başlar…      │
└─────────────────────────────┘
```

**Her hikâye yeni sayfada başlar.** Rekto (tek sayfa) zorunluluğu **yoktur**:
45 hikâyede rekto kuralı ortalama 22 boş sayfa demektir ve baskı maliyetine
kopya başına ~0,26 $ ekler. Kazanç estetiktir; bedel doğrudan teliftendir.

Hikâyenin sonunda, tipografik olarak ayrılmış:

```
─────────────────────
 A NOTE ON THIS STORY
 İki satır. Kim anlatır, nerede anlatılır, hangi varyantı vardır.
```

---

## 3. Sayfa modelinin bulduğu şey — ve neden önemli

`04_BUILD/page_budget.py` çalıştırıldığında ortaya çıkan sonuç:

> **230 sayfa, varsayılan yapıyla ULAŞILAMAZ.**

Sebep aritmetik değil **yapısal**: her hikâye yeni sayfada başlar ve sayfa
sayısı yukarı yuvarlanır, bu yüzden hikâye başına maliyet **3 ↔ 4 sayfa
arasında zıplar**. Aradaki bütün toplamlar ulaşılamazdır.

| Ulaşılabilir toplam | Hikâye/sayfa | Gereken kelime/sayfa | Hedeften |
|---:|---:|---|---:|
| 204 | 3 | 380–600 | −26 |
| **250** | 4 | 272–379 | **+20** ← varsayılan |
| 294 | 5 | 212–271 | +64 |

**Tipografiyi ayarlamak bu boşluğu açmaz.** Ancak yapısal bir karar açar:

| Seçenek | Kelime/sayfa | Kültür kartı | Bölüm açılışı | Hikâye/sayfa | Toplam |
|---|---:|---:|---:|---:|---:|
| **(a′)** | ~420 | **2 sayfa** | 2 | 3 | **226** ✓ |
| (b′) | ~280 | 0 | 2 | 4 | 228 ✓ |

**Öneri: (a′).** Kültür kartını açık sayfa (spread) yapmak vinyeti, harita
işaretini ve üç cümleyi rahat taşır; (b′) 22 vinyetin görünürlüğünü yok eder
ve yol haritasının illüstrasyon bütçesini gerekçesiz bırakır.

**(a′) = 226 sayfa** → ciltsiz maliyet 3,71 $ · telif 6,48 $
**varsayılan = 250 sayfa** → ciltsiz maliyet 4,00 $ · telif 6,19 $
**Fark: kopya başına +0,29 $.**

> ⚠ `wordsPerPage` **hâlâ kalibre değildir**. Faz 1 gerçek dizgiyle ölçtükten
> sonra tablo değişebilir. Karar Faz 1'in ölçümünden **sonra** verilir
> (`DECISIONS.md` § A4).

---

## 4. Bölüm (part) mimarisi — A5

**Öneri: bölgesel.** Altı bölüm, dünya haritasıyla birebir konuşan.

| # | Öneri | Kapsadığı makro bölgeler |
|---:|---|---|
| 1 | The Cold Edges | Kutup · Kuzey Amerika |
| 2 | The Great Rivers | Batı Asya · Afrika |
| 3 | The Steppe and the Mountain | Orta Asya · Güney Asya |
| 4 | The Eastern Seas | Doğu Asya · Güneydoğu Asya |
| 5 | The Islands | Okyanusya |
| 6 | The Old West | Avrupa · Mezoamerika · Güney Amerika |

**Neden bölgesel, temalı değil:**

- Dünya haritası yol haritasının **zorunlu kıldığı tek görseldir** ve
  bölgesel yapı onunla doğrudan konuşur.
- Kültür kartı ancak kültürler bir arada durursa işe yarar (A4).
- Temalı yapı ("Yaratılış / Kahramanlar / Canavarlar") alt başlıkla iyi
  örtüşür ama **aynı kültürü kitabın dört ayrı yerine dağıtır** ve
  "22 kültür" iddiasını görünmez kılar.

> Bölüm başlıkları **okura gider → İngilizcedir**. Yukarıdaki liste bir
> öneridir; Faz 1'de kültür listesi kilitlenince yeniden düzenlenir.

---

## 5. Ön madde

| Sayfa | İçerik |
|---:|---|
| 1 | Yarım başlık |
| 2 | boş |
| 3 | Başlık sayfası |
| 4 | Künye · **AI beyanı burada görünür** |
| 5 | İthaf |
| 6 | boş |
| 7–9 | İçindekiler (45 hikâye + 22 kültür kartı) |
| 10–11 | **Dünya haritası** (açık sayfa) |
| 12–14 | "How to Read This Book" |

**14 sayfa.**

"How to Read This Book" üç iş yapar: telaffuz rehberinin nerede olduğunu
söyler, kültürel notların ne olduğunu açıklar ve **varyant fikrini** okura
tanıtır — *"Bu hikâyelerin çoğunun birden fazla anlatımı vardır. Bu kitap
birini seçti ve hangisini seçtiğini söylüyor."*

---

## 6. Arka madde

| Sayfa | İçerik | Neden |
|---:|---|---|
| 6 | **How to Say the Names** | Yol haritası: satın alma gerekçesi |
| 8 | **Who's Who** | Yol haritası: satın alma gerekçesi |
| 4 | Notes and Sources | Kaynak izlenebilirliği · varyantlar |
| 1 | Kasıtlı dışarıda bırakma notu | Bir kusur değil, bir karar |
| 1 | Yazar hakkında | |
| 1 | Teşekkür | |

**21 sayfa.**

### QR sayfası — portföyün en değerli tek sayfası

Yol haritasının kendi cümlesi:

> *"Çocuk kitabı, e-posta listesi kurmak için portföydeki **en iyi
> araçtır**: kitabın arkasındaki QR kod, ebeveyni ücretsiz bir '22 kültür
> haritası' indirmeye götürür ve liste orada büyür."*

Harita zaten üretiliyor olacak; ek maliyeti ~sıfırdır. Bu sayfa **arka
maddenin son sayfasıdır** ve ebeveyne hitap eder, çocuğa değil.

---

## 7. Kültür kartı — A4

Öneri: **açık sayfa (2 sayfa)**, o kültürün ilk hikâyesinden önce.

```
┌──────────────────┬──────────────────┐
│                  │  KÜLTÜR ADI      │
│   VİNYET         │  bölge · dil     │
│   (siyah-beyaz)  │                  │
│                  │  Üç cümle:       │
│                  │  · kim anlatır   │
│  ─── harita ───  │  · nerede        │
│  konum işareti   │  · bugün         │
│                  │                  │
│                  │  Bu bölümdeki    │
│                  │  hikâyeler: …    │
└──────────────────┴──────────────────┘
```

**Üç cümle neden bu üç cümle:** ebeveyn/öğretmen üç şeyi arar — kimin
anlatısı, nereden, hâlâ canlı mı. Üçüncüsü aynı zamanda `AGE_POLICY` §
2.15'in geçmiş zaman tuzağını **sayfada görünür** kılar: yaşayan bir
gelenek için o cümle şimdiki zamandadır.

---

## 8. İllüstrasyon dağılımı

| Tür | Adet | Yerleşim |
|---|---:|---|
| Hikâye açılışı | 45 | Hikâyenin ilk sayfasının üst yarısı |
| Kültür vinyeti | 22 | Kültür kartının sol sayfası |
| Dünya haritası | 1 | Ön maddede açık sayfa |
| **Toplam** | **68** | hepsi **siyah-beyaz** |

Renk yasağının gerekçesi yol haritasının kendi hesabıdır: *"Renkli baskı bu
sayfa sayısında maliyeti 15,95 $'a çıkarır — fiyatı 39,99 $'a iter,
**kategoriden çıkarır**."*

Şartname ve promptlar: `04_BUILD/imagespec.py` →
`07_ASSETS/IMAGE_PROMPT_LIBRARY.html`.

---

## 9. Bu belge nasıl değişir

A4 ve A5 kapandığında bu belge **güncellenir** ve `page_budget.py`'nin
`MODEL` sözlüğü onunla birlikte değişir. İkisi ayrışırsa
`validate_structure.py` belge–kod tutarlılığı denetiminde kırmızı yanar.
