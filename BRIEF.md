# BRIEF — The Great Book of World Myths

> Ürün, kitle, konumlanma ve ticari model. Bütün sayılar master yayıncılık
> yol haritasının **PROJE 02** bölümünden alınmıştır; hiçbiri bu belgede
> uydurulmadı. Yol haritasının vermediği her şey § 9'da **AÇIK** olarak
> işaretlidir.
>
> Kaynak: `CODEX_MYTHOLOGICA/AMAZON_KDP_PUBLISHING_COMPANY_ROADMAP_2026.html`
> § BÖLÜM 02b, BÖLÜM 03 · PROJE 02, BÖLÜM 06, BÖLÜM 08, BÖLÜM 11

---

## 1. Tek cümlede

> Yunan'a boğulmuş çocuk mitoloji rafına, 22 kültürden 45 hikâyeyi aynı
> kalitede, uzun soluklu okunacak biçimde sunan bir cilt.

---

## 2. Başlık ve neden

| | |
|---|---|
| **Çalışma adı** | World Myths for Young Readers |
| **Nihai başlık** | The Great Book of World Myths |
| **Alt başlık** | 45 Stories of Gods, Heroes, and Monsters from 22 Cultures — Retold for Young Readers (Ages 8–12) |

Yol haritasının gerekçesi, birebir:

> *"Çocuk kitabı rafında alıcı ebeveyndir ve ebeveyn üç şeyi tarar: yaş
> aralığı, hikâye sayısı, kapsam. Üçü de alt başlıkta. 'World' kelimesi,
> rafın Yunan'a boğulmuş olmasına karşı doğrudan bir konumlanmadır."*

Bunun mühendislik sonucu: **alt başlıktaki üç sayı ürünün kendisidir.**
"45" ve "22" birer pazarlama süsü değil, doğrulanabilir vaattir. Bu yüzden
`validate_spec.py` hikâye ve kültür sayısını kapıya bağlar: kitap 44
hikâyeyle çıkarsa alt başlık yalan söyler.

---

## 3. Kitle

| Rol | Kim |
|---|---|
| **Alıcı** | ebeveyn · büyükanne/büyükbaba · öğretmen · okul kütüphanecisi |
| **Okur** | 8–12 yaş; Percy Jackson'ı bitirmiş ve "daha fazla mit" arayan çocuk |

Alıcı ile okurun ayrı kişiler olması bu kitabın **temel ticari gerçeğidir**:

- **Okur** hikâyeyi ister → sıcak, hızlı, sahneleyici anlatı.
- **Alıcı** güven ister → yaş aralığı, kültürel çeşitlilik, "ekransız",
  eğitici algı, telaffuz rehberi, kültürel not.

Ürün ikisini birden karşılamak zorundadır. `AGE_POLICY.md` alıcı tarafını,
`CHILDREN_WRITING_STYLE.md` okur tarafını korur.

---

## 4. Çözdüğü problem

> *"Çocuk mitoloji rafının yaklaşık %80'i Yunan. Bir çocuk Yunan'ı
> bitirdiğinde önüne konan şey genellikle başka bir Yunan kitabı oluyor.
> Kore, İnuit, Polinezya, Batı Afrika, Fars ve Türk anlatılarını aynı
> ciltte, aynı kalitede sunan bir kitap neredeyse yok."*

**Bu cümle bir kapsam kısıtıdır.** Yol haritası altı kültürü adıyla
sayıyor; bu altısı kitapta **bulunmak zorundadır**:

1. Kore
2. İnuit
3. Polinezya
4. Batı Afrika
5. Fars
6. Türk

Kalan 16 kültür Faz 1'de kilitlenir → `01_RESEARCH/culture_index.json`.
Bu bir **AÇIK KARARDIR** (§ 9 · A2).

---

## 5. Neden satın alınır

Yol haritasının dört gerekçesi:

1. **Arama hacmi devasa ve niyet çok net.**
2. **Hediye ürünü** — doğum günü, yılbaşı, karne.
3. **Okul ve kütüphane alımı** (ciltli sürüm).
4. **Ebeveyn için "ekransız" ve "kültürel çeşitlilik"** — 2026'nın iki
   doğrulanmış eğilimi.

---

## 6. Rakip neden başarısız

> *"Markalı rakipler (DK, National Geographic Kids, Usborne) tam renkli,
> ağır görsel tasarımlı ve 19,99–29,99 $ bandında. Onların yapamadığı şey
> **uzun soluklu okuma**: kutucuk ve kolaj tasarımı, çocuğun oturup
> okuduğu bir kitap üretmiyor. Bölüm-kitabı uzunluğunda, iyi yazılmış,
> dünya kapsamlı bir cilt boşta."*

**Ürün sonucu:** bu kitap bir *bakılan* kitap değil, bir *okunan*
kitaptır. İllüstrasyon anlatıyı **açar**, yerini almaz. Sayfa tasarımı
kutucuk/kolaj değil, sürekli metindir. Bu, illüstrasyon bütçesinin neden
45 + 22 ile sınırlı tutulduğunu da açıklar.

---

## 7. Ürün spesifikasyonu — yol haritasının tablosu

| Kalem | Karar | Gerekçe (yol haritası) |
|---|---|---|
| Sayfa sayısı | ~230 (45 hikâye × ~950 kelime ≈ 43 bin) | 8–12 yaş için doğru kalınlık: ciddi ama yıldırmayan |
| Trim | 6 × 9 inç | Seri tutarlılığı; normal trim maliyeti |
| Ciltsiz | 16,99 $ · maliyet 3,76 $ · telif 6,43 $ | Başabaş ACOS %37,8 |
| Ciltli | 26,99 $ · maliyet 8,41 $ · telif 7,78 $ | **Bu kitapta ciltli lansmanla birlikte açılmalı** — okul/kütüphane ve hediye alımı ciltliye gider |
| Kindle | 7,99 $ · telif ~5,14 $ | Çocuk kitabında e-kitap payı düşüktür ama sıfır maliyetlidir |
| İllüstrasyon | 45 bölüm açılış çizimi + 22 kültür vinyeti, **siyah-beyaz** | Renkli baskı bu sayfa sayısında maliyeti 15,95 $'a çıkarır — fiyatı 39,99 $'a iter, kategoriden çıkarır |
| Harita | 1 dünya haritası (22 kültürün konumu) — ön veya arka iç kapak | Ebeveynin "eğitici" algısını tek görselde kurar |
| Ek malzeme | Telaffuz rehberi · "kim kimdir" sözlüğü · her hikâye sonunda 2 satırlık kültürel not | Öğretmen ve kütüphaneci için satın alma gerekçesi; **iade oranını düşürür** |
| Üslup | Sıcak, hızlı, sahneleyici. Cümleler kısa. Şiddet ve trajedi saklanmaz ama **sahnelenmez**: sonuç anlatılır, dehşet betimlenmez | Bu yetişkin cildinin bilinçli tersidir ve **ayrı bir yazım işidir — çeviri değil** |

### Üretim, maliyet, takvim

| Kalem | Saat |
|---|---:|
| Araştırma (yetişkin cildinden devralınır) | 20 |
| Yazım | 75 |
| Editörlük ve yaş uygunluğu | 35 |
| İllüstrasyon | 45 |
| Dizgi | 18 |
| Kapak | 12 |
| Metadata | 10 |
| **Toplam** | **~215** |

Lansman maliyeti **~430 $**. Takvim **3,5 ay**. Yayın **Temmuz 2027**.

> **Kapak karmaşıklığı: orta-yüksek** — çocuk kitabı kapağı tür
> konvansiyonuna uymak zorundadır ve *"bizim 'koyu kodeks' dilimiz burada
> **işlemez**; daha aydınlık, daha karakterli, yaş aralığı köşede net bir
> kapak gerekir. Bu, markanın bilinçli olarak esnetildiği tek yerdir."*

> **Yayın zamanlaması kritik:** hediye sezonu için 8 hafta kuralı geçerli.
> Temmuz 2027 yayını, Kasım–Aralık 2027 sezonuna dört ay önceden hazır
> olmak demektir.

---

## 8. Ticari model

### Gelir senaryoları — ilk 12 ay

Karma birim telif **6,22 $**. *"Çocuk kitabı daha çok adet, daha düşük
birim telif üretir."* (Yol haritası: **tahmin**, doğrulanmış hesaplama değil.)

| Senaryo | Olasılık | 12 ay adet | Brüt telif |
|---|---:|---:|---:|
| Muhafazakâr | %30 | 280 | ~1.740 $ |
| **Temel** | **%55** | **800** | **~4.975 $** |
| İyimser | %15 | 2.300 | ~14.300 $ |

Portföyün **en yüksek kaba ROI'si**: %136 (Bestiarium %73, Atlas %88).
Talep kesinliği **çok yüksek**; rekabet **yüksek**; marka uyumu
**esnetiliyor**.

### Risk değerlendirmesi — yol haritasının dört riski

| # | Risk | Düzey | Azaltma (yol haritasının kendi cümlesi) |
|---|---|---|---|
| R1 | **Markalı rekabet** | yüksek | *"Onların olmadığı yerde yarışın — kapsam ve okuma deneyimi, görsel yoğunluk değil. Alt başlıkta '22 cultures' bunu tek satırda söyler."* |
| R2 | **Yaş uygunluğu** | orta | *"Mitler acımasızdır. Yanlış tonlanmış bir sahne, ebeveyn yorumunda 'çocuğum için fazla karanlık' olarak geri döner — ve bu yorum silinemez. Azaltma: yazım öncesi `AGE_POLICY.md`; yayından önce **en az iki ebeveyn okuması**."* |
| R3 | **Marka esnemesi** | orta | *"Aynı yazar adı korunur (otorite birikimi en değerli varlıktır) ama ayrı seri adı kullanılır: Codex serisi yetişkin, 'Great Book of…' çocuk."* |
| R4 | **İade oranı** | düşük-orta | *"'Look Inside' örneğinde **gerçek** bir bölüm açılışı ve **gerçek** bir illüstrasyon; A+ içerikte yaş aralığı ve örnek sayfa."* |

> R2 bu projenin **tanımlayıcı riskidir** ve yol haritası çözümü adıyla
> yazmıştır: `AGE_POLICY.md`. Bu proje o belgeyi bir kapıya bağlar.

---

## 9. Yol haritasının vermediği — AÇIK KARARLAR

Bunlar **uydurulmadı**. Hepsi `DECISIONS.md`'de AÇIK KARAR olarak durur ve
Faz 1'de kurucu onayıyla kapanır.

| # | Açık soru | Ne zaman kapanır |
|---|---|---|
| A1 | Manuscript public depoda mı duracak? (Bestiarium'da cevap: hayır) | **Faz 1 başlamadan** |
| A2 | 22 kültürün tam listesi (6'sı yol haritasınca zorunlu, 16'sı açık) | Faz 1 |
| A3 | 45 hikâyenin tam listesi ve kültür başına dağılımı | Faz 1 |
| A4 | 22 kültür vinyetinin kitaptaki yeri (kültür kartı mı, bölüm başlığı mı, kenar süsü mü) | Faz 1 |
| A5 | Kitabın bölüm (part) mimarisi: bölgesel mi, temalı mı | Faz 1 |
| A6 | Büyük punto sürümü v1.0'a girecek mi (yol haritası onu "uzun vadeli genişleme"ye koyuyor) | Faz 4 |
| A7 | KDP Select / KU testi ne zaman (yol haritası bu kitabı istisna sayıyor) | yayın sonrası |
| A8 | İki ebeveyn okuyucusu kim (R2'nin zorunlu azaltması) | Faz 4 başlamadan |
| A9 | ISBN: KDP ücretsiz mi, kendi ISBN'imiz mi | Faz 5 |

---

## 10. Uzun vadeli genişleme

Yol haritasının listesi:

- Cilt II: 45 hikâye daha
- Aktivite / çalışma kitabı eşlikçisi
- **Sesli sürüm (bu kitapta özellikle güçlü)**
- Büyük punto / erken okur sürümü
- 5 dil (Kindle Translate — EN ↔ ES/DE/FR/IT/PT)
- Sınıf seti / öğretmen rehberi (PDF, kendi kanalımızda)

Ve portföy açısından en değerlisi:

> *"Çocuk kitabı, e-posta listesi kurmak için portföydeki **en iyi
> araçtır**: kitabın arkasındaki QR kod, ebeveyni ücretsiz bir '22 kültür
> haritası' indirmeye götürür ve liste orada büyür."*

**Üretim sonucu:** arka madde tasarımı bir QR kodu ve bir açılış sayfası
(landing) varsayar. Bu, Faz 5'in metadata işidir; harita zaten üretiliyor
olacağı için ek maliyeti ~sıfırdır.
