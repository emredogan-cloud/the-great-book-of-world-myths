# SOURCING STANDARD — kaynak gösterme ölçütü

> **Bir çocuk kitabı olmak standardı düşürmez, yükseltir.**
>
> Hedef okur kaynakları kontrol edemez. Bir yetişkin *"bu Edda'da böyle
> mi geçiyor"* diye bakabilir; dokuz yaşındaki okur bakamaz. Dolayısıyla
> güven **tamamen yayıncıdadır** ve tek savunma izlenebilirliktir.
>
> Bu belge Codex Bestiarium'un `SOURCING_STANDARD.md`'sinden **uyarlandı**;
> § 6 ve § 7 bu projeye özgüdür ve orada karşılığı yoktur.
>
> Yazıldı: 8 Ağustos 2026 · Bootstrap · **kurucu onayı gerektirir**

---

## 1. Neden bu belge var

Rakip çocuk mitoloji kitaplarının çoğu kaynak göstermez. Bu, bizim
lehimize bir farktır ama **kırılgan** bir farktır: bir tek uydurma künye
onu bütün kitap için geçersiz kılar — ve bir öğretmen bunu bulur.

Ters yönde de bir tuzak var: doğrulayamadığı için hiçbir şey yazmayan bir
yazar kitabı yazamaz. Ölçüt net olmalı.

---

## 2. Kaynak katmanları

Her kaynak dört katmandan birine girer → `story_index.json` →
`sources[].type`.

| Katman | Ne | Örnek | Bağımsız sayılır mı |
|---|---|---|---|
| `primary` | Birincil metin veya saha etnografisi | *Poetic Edda*; *Kojiki*; Boas, *The Central Eskimo* (1888) | ✅ |
| `scholarly` | Hakemli akademik ikincil çalışma | Lindow, *Norse Mythology* (2001) | ✅ |
| `reference` | Yayımlanmış başvuru cildi / ansiklopedi | Leeming, *The Oxford Companion to World Mythology* (2005) | ✅ |
| `index` | Motif veya masal tipi tasnifi | Thompson, *Motif-Index*; ATU | ❌ **asla** |
| `retelling` | Başka bir yeniden anlatım (çocuk veya yetişkin) | herhangi bir mevcut derleme | ❌ **asla** |

### İki bağımsız kaynak kuralı

Bir hikâye `verified` olabilmek için **en az iki** bağımsız kaynağa
ihtiyaç duyar ve bunlardan **en az biri** `primary` veya `scholarly`
olmalıdır.

> İki ansiklopedi maddesi iki bağımsız kaynak **değildir** — ikisi de büyük
> ihtimalle aynı üçüncü kaynaktan türemiştir. Ansiklopedi bir *teyit*tir,
> bir *tanıklık* değil.

### `retelling` neden asla kaynak sayılmaz

Bu, bu projenin **en kolay ihlal edilecek** kuralıdır ve Bestiarium'da
karşılığı yoktur.

Çocuk mitoloji rafı yeniden anlatımlarla doludur ve onlardan yazmak
kolaydır. Ama bir yeniden anlatım **zaten bir editoryal karar zinciridir**:
başka biri hangi varyantı seçeceğine, neyi yumuşatacağına, neyi ekleyeceğine
çoktan karar vermiştir. Ondan yazmak, o kararları **görmeden devralmaktır**
— ve o kararların bir kısmı yanlıştır.

Daha kötüsü: raftaki yaygın yanlışlar (Yunan adlarının Roma karşılıklarıyla
karışması, "Loki'nin çocukları" listesindeki uydurmalar, Anansi
anlatılarının Batı Afrika ↔ Karayip kaynaklarının karıştırılması) tam da
yeniden anlatımdan yeniden anlatıma **kopyalanarak** yayılır.

> Bir yeniden anlatımı **okumak** serbesttir ve yararlıdır. Onu **kaynak
> olarak künyelemek** yasaktır. Onun kaynaklarına **gitmek** teşvik
> edilir.

Aynı kural Wikipedia için de geçerlidir.

---

## 3. Künye biçimi ve sayfa numarası kuralı

Bu, en kolay ihlal edilen kuraldır. **Doğrulanmamış bir sayfa numarası
yazmak, uydurma kaynak yazmakla aynı şeydir** ve daha sinsidir çünkü doğru
görünür.

| Kaynak tipi | Doğru künye | Neden |
|---|---|---|
| Numaralı birincil metin | *Völuspá* 45–47 · *Kalevala* runo 26 · *Kojiki* I.iii | Numaralandırma metnin kendisinden gelir; baskıdan bağımsızdır |
| Başvuru cildi / ansiklopedi | Leeming (2005), **s.v.** "Amaterasu" | Madde başlığıyla künye vermek standarttır |
| Bölümlü monografi | Boas (1888), **Bölüm VI** ("Religious Ideas") | Bölüm başlığı doğrulandıysa yeter |
| Makale | *Journal of American Folklore* 92:365 (1979), 285–301 | Sayfa aralığı künyenin parçası ve doğrulanabilir |
| **Sayfası doğrulanmamış kitap** | sayfa **YAZILMAZ** | Uydurma sayfa = uydurma kaynak |

> **Kural:** sayfa numarası ancak (a) metnin kendi numaralandırmasıysa,
> (b) makale künyesinin parçasıysa veya (c) **gerçekten görüldüyse**
> yazılır. Aksi hâlde `s.v.` veya bölüm başlığı kullanılır. **Boş
> bırakmak, uydurmaktan her zaman iyidir.**

---

## 4. Doğrulama seviyeleri

Her kaynağın `verification` alanı, künyenin **nasıl** teyit edildiğini
söyler ve **boş bırakılamaz**.

| Seviye | Anlamı | Güç |
|---|---|---|
| `fulltext` | Dijital nüshanın tam metni görüldü | güçlü |
| `toc` | İçindekiler veya bölüm başlığı görüldü | güçlü |
| `article` | Cilt, sayı, sayfa ve kalıcı kimliği (DOI/JSTOR) doğrulanmış hakemli makale | güçlü |
| `sv` | Alfabetik başvuru cildinde madde başlığı (*sub verbo*) | güçlü |
| `canon` | Kendi iç numaralandırması olan standart eleştirel metin | güçlü |
| `catalog` | Kütüphane/arşiv kataloğunda künye doğrulandı (varlık kesin, içerik değil) | zayıf |
| `secondary` | Başka bir yayımlanmış çalışmanın atfı üzerinden bilinir | zayıf |

Bir hikâyenin iki bağımsız kaynağından **en az birinin** doğrulaması
`fulltext`, `toc`, `canon`, `article` veya `sv` olmalıdır.

> **Güç ölçütü "okudum mu" değil, "okur gidip bakabilir mi"dir.**
> *Völuspá* 45 her baskıda aynı kıtadır. "Şu kitap vardır ve konuyu
> işler" demek okuru 400 sayfaya gönderir — bu zayıftır.

---

## 5. Kanonik anlatım seçimi — bu projeye özgü

Bir başvuru cildi *"varyantlar vardır"* der ve geçer. **Bir hikâye bir
anlatım seçmek zorundadır.**

Bu seçim bir editoryal karardır ve kaydedilir:

| Alan | Ne taşır |
|---|---|
| `canonicalVersion` | Hangi kaynağın hangi anlatımı esas alındı |
| `canonicalRationale` | **Neden** o anlatım seçildi (en eski? en tam? en yaygın? yaşa en uygun?) |
| `variants[]` | Bilinen diğer anlatımlar, kaynağıyla |
| `variantNote` | Kültürel notta okura söylenecek cümle |

**Yaşa uygunluk tek başına yeterli bir seçim gerekçesi değildir.** Bir
varyant yalnızca daha yumuşak olduğu için seçilirse bu, kültürel
sterilizasyondur (`AGE_POLICY.md` § 0). Gerekçe metinsel olmalıdır —
"en eski kayıt", "en tam kayıt", "o kültürün kendi anlatıcılarının
tercih ettiği" gibi. Yaşa uygunluk **ikincil** gerekçe olabilir ve
`ageAdaptationNote`'a ayrıca yazılır.

> Bestiarium'un ilkesi burada da geçerli ve daha değerli:
> *"Çelişkiler saklanmaz, gösterilir. 'Bu anlatının şu bölgede farklı bir
> sonu vardır' cümlesi bir kusur değil, kitabın **otoritesinin
> kanıtıdır**."* — Çocuk kitabında bu cümle **kültürel notun** işidir.

---

## 6. Yaş uyarlaması izi — bu projeye özgü

Kaynakta olan ama kitapta **olmayan veya örtülen** her şey kaydedilir:

```
ageAdaptationNote: "Kaynakta X şöyle olur; bu anlatımda sonuç anlatılır,
                    sahne kurulmaz. Gerekçe: AGE_POLICY § 2.7."
```

**Bu alan neden zorunlu:** bir ebeveyn veya öğretmen *"bu hikâyenin sonu
böyle değil"* dediğinde verilecek cevap budur. Ve o cevap **"kaynağı
bilmiyorduk" olamaz**.

`validate_research.py` şunu denetler: `AGE_POLICY.md`'de `IMPLY`, `OMIT`
veya `REVIEW` seviyesindeki bir kategori hikâyenin `contentFlags`
listesindeyse, `ageAdaptationNote` **boş bırakılamaz**.

---

## 7. Kültürel kısıtlılık taraması — muafiyetsiz

**Her hikâye için zorunludur.** Bestiarium taramayı yalnızca bir "yaşayan
gelenekler" listesindeki maddeler için zorunlu tutuyordu ve **liste
hatalıydı** (D28): iki kimlik hiçbir geleneğe denk gelmiyordu, ve kitabın
en hassas etik notunu taşıyan madde kapının **dışında** kaldı.

Bu kitapta 22 kültürün neredeyse tamamı yaşayan gelenektir. Muafiyet
listesi tutmak, listeyi doğru tutma yükümlülüğü doğurur; taramayı
**evrensel** yapmak o yükümlülüğü ortadan kaldırır (karar K20).

### Tarama neyi arar

- Yalnızca **yayımlanmış ve kısıtlanmamış** malzeme kullanılır.
- Kısıtlı olduğu bilinen anlatı **anlatılmaz — kısıtlı olduğu söylenir**.
- **Kullanılmaz ve çizilmez:** başlatma (initiation) bilgisi, tören
  nesnesi ayrıntısı, klan işareti, maske deseni, yer-özel kutsal anlatı,
  kimin anlatabileceği kurala bağlı olan malzeme.
- Sonuç `restrictionScreened: true` **ve** `restrictionNote` alanında
  **açık bir cümleyle** kaydedilir. Boş bırakılamaz.

### Kasıtlı dışarıda bırakma

Bir kültürün malzemesi kısıtlıysa hikâye **düşer** ve bu bir kusur değil
bir karardır. Arka maddede okura **söylenir**.

> Bestiarium bunu Avustralya Aborjin gelenekleri için yaptı: anlatı
> çoğunlukla topluluk mülkiyetindedir ve kimin anlatabileceği kurala
> bağlıdır. Sonsöz'de bir **tercih** olarak yazılmıştır.
>
> Bu kitap için aynı değerlendirme **her aday kültür için Faz 1'de**
> yapılır ve sonucu `culture_index.json` → `restrictionAssessment`
> alanına yazılır.

---

## 8. Telaffuz kaynağı — bu projeye özgü

Telaffuz rehberi yol haritasının ek malzeme listesinin **ilk kalemidir**
ve gerekçesi ticaridir: *"öğretmen ve kütüphaneci için satın alma
gerekçesi; iade oranını düşürür."*

Yanlış bir telaffuz tam da o gerekçeyi çürütür. Bu yüzden:

| Alan | Kural |
|---|---|
| `pronunciation` | Basitleştirilmiş İngilizce hece gösterimi (*ah-mah-teh-RAH-soo*) |
| `pronunciationIpa` | IPA — varsa |
| `pronunciationSource` | **Zorunlu.** Nereden geldi: sözlük, akademik çalışma, dil kaynağı, ana dili konuşuru |

**Telaffuz uydurulmaz.** Kaynağı yoksa yazılmaz; ad değişir veya hikâye
değişir.

---

## 9. Bir hikâye ne zaman düşer

Aşağıdakilerden **herhangi biri** doğruysa hikâye listeden düşer ve
`DECISIONS.md`'ye gerekçesiyle yazılır:

- İkinci bağımsız kaynak bulunamadı
- Bütün kaynaklar `reference` katmanında ve hiçbiri `primary`/`scholarly` değil
- Bütün doğrulamalar `catalog` veya `secondary` seviyesinde kaldı
- Malzeme kısıtlı çıktı (§ 7)
- Hikâye `AGE_POLICY.md` § 2.8'in ikinci maddesine giriyor (anlatı rıza
  dışı birleşmeye dayanıyor ve o unsur çıkarılamıyor)
- Telaffuz kaynağı bulunamadı (§ 8)

### ⚠ Ama **45 sayısı düşürülemez**

Bestiarium'un kuralı *"120 sayısı kutsal değildir; doğruluk kutsaldır"*
idi ve kapsamı 120 → 112'ye indirdi.

**Burada bu yapılamaz.** 45 ve 22 **alt başlıkta yazıyor** ve alıcı
(ebeveyn) tam olarak o iki sayıyı tarıyor:

> *"Çocuk kitabı rafında alıcı ebeveyndir ve ebeveyn üç şeyi tarar: yaş
> aralığı, **hikâye sayısı**, **kapsam**."*

Yani düşen hikâyenin yerine **başkası gelmek zorundadır**. Sonuç:

> **Faz 1'in aday listesi 45'ten fazla olmalıdır.** Hedef: **≥55 aday**
> hikâye, ≥26 aday kültür. `validate_spec.py` Faz 1 kapısında yedek
> payını denetler.

Aynı şey kültür için de geçerli: 22 kültür kilitlenmeden önce her birinin
en az bir doğrulanmış hikâyesi olmalı.

---

## 10. Yasak

- Görmediğin bir sayfa numarasını yazmak
- "Muhtemelen şu kaynakta vardır" diye künye yazmak
- İki ansiklopediyi iki bağımsız kaynak saymak
- Motif dizinini bağımsız kaynak saymak
- **Başka bir yeniden anlatımı kaynak saymak** (§ 2)
- Wikipedia'yı künyelemek (kaynaklarına **gitmek** serbest ve teşvik edilir)
- Kısıtlı olduğu bilinen bir anlatıyı "zaten yayımlanmış" diye kullanmak
- Telaffuz uydurmak
- **Bir mitin boşluğunu anlatı akıcılığı için doldurmak**

Son madde bu projeye özgüdür ve en tehlikelisidir. Bestiarium'un D41
emri değişmeden geçerlidir:

> *"Never invent mythology. Never invent historical claims. Never
> fabricate references."*

Ve bir ekle: **hikâye uydurulmaz.** Yetişkin okur bir boşluğu fark eder;
dokuz yaşındaki okur okuduğunu doğru sanar ve o yanlışı yıllarca taşır.
Boşluk varsa `variantNote` ile **gösterilir**.
