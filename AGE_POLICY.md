# AGE POLICY — 8–12 yaş editoryal güvenlik çerçevesi

> **Bu belge master yayıncılık yol haritası tarafından adıyla emredilmiştir.**
> PROJE 02 · Risk değerlendirmesi:
>
> > *"**Yaş uygunluğu (orta).** Mitler acımasızdır. Yanlış tonlanmış bir
> > sahne, ebeveyn yorumunda 'çocuğum için fazla karanlık' olarak geri
> > döner — ve **bu yorum silinemez**. Azaltma: **yazım öncesi
> > `AGE_POLICY.md`**; yayından önce en az iki ebeveyn okuması."*
>
> Bu, projenin **tanımlayıcı riskidir** ve bu belge onun azaltmasıdır.
> Bir ek belge değil, **CI kapısı olan birinci sınıf bir sistemdir**:
> `04_BUILD/qa_age.py`.
>
> Yazıldı: 8 Ağustos 2026 · Bootstrap · **kurucu onayı gerektirir**

---

## 0. Temel ilke — ve neyin yasak olduğu

Yol haritasının üslup kararı bu belgenin tek cümlelik özetidir:

> *"Şiddet ve trajedi **saklanmaz** ama **sahnelenmez**: sonuç anlatılır,
> dehşet betimlenmez."*

Bunun iki yarısı da bağlayıcıdır ve **ikisi de ihlal edilebilir**:

| İhlal | Nasıl görünür | Neden zararlı |
|---|---|---|
| **Aşırı sahneleme** | Kanın rengi, çığlığın sesi, parçalanmanın ayrıntısı | Ebeveyn yorumu: *"çocuğum için fazla karanlık"* — silinemez |
| **Aşırı saklama** | Ölüm "uykuya daldı" olur, kurban "hediye" olur, tanrı hep iyidir | **Kültürel sterilizasyon.** Mitin anlamı yok edilir; kitap bir başka yumuşak Yunan derlemesine döner ve varlık sebebini kaybeder |

> **Hedef: YAŞA UYGUN YENİDEN ANLATIM. Hedef DEĞİL: KÜLTÜREL
> STERİLİZASYON.**

**Mutlak yasak (herhangi bir kategoriden bağımsız):**

1. Bir mitin anlamını değiştirmek için olay örgüsünü değiştirmek.
2. Kaynakta olmayan bir "mutlu son" eklemek.
3. Bir kültürün anlatısını "ilkel", "vahşi" veya "garip" gösteren
   çerçeveleme.
4. Kaynakta olan ama kitapta örtülen bir şeyi **kaydetmemek**
   (`ageAdaptationNote` zorunludur).

---

## 1. Karar seviyeleri

Her içerik kategorisi dört seviyeden birine düşer:

| Seviye | Kod | Anlamı |
|---|---|---|
| **İZİN VERİLEN** | `ALLOW` | Doğrudan yazılabilir. Sahnelenebilir. |
| **İMA EDİLEN** | `IMPLY` | Olay **anlatılır**, ayrıntı **betimlenmez**. Sonuç görünür, süreç görünmez. |
| **ÇIKARILAN** | `OMIT` | Bu kitapta yer almaz. Gerekiyorsa hikâye değişir veya düşer. |
| **ÖZEL İNCELEME** | `REVIEW` | Yazılabilir ama **kurucu + iki ebeveyn okuyucusu** onayı olmadan yayına giremez. `03_EDITORIAL/AGE_REVIEW_LOG.md`'ye kaydedilir. |

`OMIT` bir sansür kararı değil, bir **kapsam** kararıdır: o malzemeyi
taşıyan hikâye ya farklı bir varyantla anlatılır ya listeden düşer ve
yerine başkası gelir (bkz. `LESSONS_FROM_CODEX_BESTIARIUM.md` § J7).

---

## 2. On yedi kategori

### 2.1 · Şiddet · `IMPLY`

| | |
|---|---|
| **İzin verilen** | Dövüş, kovalamaca, silah, güç gösterisi, yenilgi, yaralanma gerçeği ("kolundan yaralandı"), savaşın olduğu, kimin kazandığı |
| **İma edilen** | Öldürme anı — **darbe anlatılır, sonucu anlatılır, arası anlatılmaz.** *"Kılıç indi. Canavar bir daha kalkmadı."* |
| **Çıkarılan** | Yaranın anatomisi, kan miktarı ve rengi, acı çekmenin uzatılmış betimi, işkence, sakatlamanın ayrıntısı |
| **Özel inceleme** | Bir çocuğa veya hayvana yönelen şiddet |

**Ölçü:** bir şiddet sahnesi **üç cümleyi** geçmez ve içinde **en fazla bir**
duyusal ayrıntı bulunur.

### 2.2 · Ölüm · `ALLOW`

| | |
|---|---|
| **İzin verilen** | Ölüm gerçeği, açıkça ve dürüstçe. *"öldü"* kelimesi. Kahramanın ölümü. Tanrının ölümü. Ölülerin diyarı. Ölümsüzlüğün kaybı. |
| **İma edilen** | Cesedin durumu; ölüm anının fizyolojisi |
| **Çıkarılan** | Çürüme betimi; cesetle etkileşim ayrıntısı |
| **Özel inceleme** | Bir çocuk karakterin ölümü |

> Ölüm **örtmece ile geçiştirilmez.** *"Uykuya daldı"*, *"gitti"*,
> *"aramızdan ayrıldı"* bu kitapta yasaktır. 8–12 yaş ölümü anlar ve
> örtmece ona ölümün utanılacak bir şey olduğunu öğretir. Ayrıca
> mitolojinin yarısı ölüm hakkındadır; onu örtmek kitabı boşaltır.

### 2.3 · Yas ve keder · `ALLOW`

| | |
|---|---|
| **İzin verilen** | Ağlamak, özlemek, aramak, öfkelenmek, kabullenememek, teselli bulamamak. **Çözülmemiş yas.** Demeter'in kışı. Izanagi'nin dönüşü. |
| **İma edilen** | — |
| **Çıkarılan** | — |
| **Özel inceleme** | — |

Yas bu kitabın **en değerli** duygusal malzemesidir ve kısıtlanmaz.
8–12 yaş kaybı yaşamış olabilir; mit ona kaybın anlatılabilir olduğunu
gösterir. **Yasın zorla çözülmesi yasaktır**: kaynakta çözülmüyorsa
kitapta da çözülmez.

### 2.4 · Canavarlar · `ALLOW`

| | |
|---|---|
| **İzin verilen** | Korkutucu görünüş, tuhaf anatomi, devasa ölçek, tehlike, canavarın kazanması |
| **İma edilen** | Canavarın **yeme** eylemi — yaptığı söylenir, çiğneme betimlenmez |
| **Çıkarılan** | Beden parçalarının ayrıntılı dökümü; iç organ; "yarı yenmiş" imgesi |
| **Özel inceleme** | — |

**Kural:** canavar **silüetle ve etkiyle** korkutur, envanterle değil.
*"Gölgesi köyün üstünü kapattı"* > *"üç sıra dişi ve altı gözü vardı"*.

### 2.5 · Dönüşüm (transformation) · `ALLOW`

| | |
|---|---|
| **İzin verilen** | Şekil değiştirme, insandan hayvana, hayvandan insana, taşa dönme, yıldıza dönüşme, ceza olarak dönüşüm |
| **İma edilen** | Dönüşümün **acısı** — bir cümle, betim yok |
| **Çıkarılan** | Kemik kırılması, deri değişimi, "eti eridi" tipi beden korku ayrıntısı |
| **Özel inceleme** | Rıza dışı dönüşümün bir tecavüz anlatısıyla bağlı olduğu durumlar (§ 2.8) |

Dönüşüm 8–12 yaş için mitolojinin **en çekici** unsurudur ve serbesttir.
Sınır **beden korkusudur** (body horror), dönüşümün kendisi değil.

### 2.6 · Yamyamlık · `IMPLY` / kısmen `OMIT`

| | |
|---|---|
| **İzin verilen** | Bir yaratığın "insan yediği" bilinmesi; korkunun sebebi olarak varlığı |
| **İma edilen** | Kronos'un çocuklarını yutması gibi **anlatının çekirdeğinde** olan olaylar — *yutar*, sahne kurulmaz |
| **Çıkarılan** | Yeme sahnesinin betimi; pişirme, hazırlama, tat, ses; kurbanın bilinçli hâlde yenmesi |
| **Özel inceleme** | Aile içi yamyamlık (ebeveyn ↔ çocuk) — **her örnek ayrı ayrı incelenir** |

Yamyamlık mitolojide yaygındır ve tamamen çıkarılamaz; ama bu kitapta
**asla sahne değildir**, yalnızca **olay**tır.

### 2.7 · Kurban (sacrifice) · `IMPLY` + `REVIEW`

| | |
|---|---|
| **İzin verilen** | Kurbanın **varlığı** ve **anlamı**: neden yapıldığı, topluluğun ne umduğu, neye mal olduğu. Gönüllü fedakârlık. Hayvan kurbanı. |
| **İma edilen** | İnsan kurbanının gerçekleştiği — olay söylenir, tören betimlenmez |
| **Çıkarılan** | Tören ayrıntısı (yöntem, aletler, sıra), kurbanın acısı, kalabalığın tepkisinin uzatılması |
| **Özel inceleme** | **Çocuk kurbanı** ve **yaşayan bir dine ait tören** — ikisi de kurucu + iki ebeveyn okuması gerektirir |

> **Kritik ayrım:** bir kültürün kurban pratiğini anlatmak onu
> "vahşi" göstermek değildir — **çerçeveleme** her şeydir. Kurban her
> zaman bir **maliyet** olarak sunulur: topluluk bir şeyi göze aldı.
> "Onlar böyleydi" cümlesi yasaktır.

### 2.8 · Cinsellik · `OMIT`

| | |
|---|---|
| **İzin verilen** | Aşk, evlilik, kur, kıskançlık, doğum gerçeği, "çocukları oldu" |
| **İma edilen** | — |
| **Çıkarılan** | Cinsel eylem her biçimde; çıplaklığın betimi; arzunun bedensel betimi; doğurganlık ritüelinin ayrıntısı |
| **Özel inceleme** | — |

**Zorunlu ek kural — mitolojinin en sık yaş sorunu:**

Yunan, Roma, Hint, Kelt ve Japon mitolojisinde çok sayıda anlatı **rıza
dışı birleşmeyle** başlar (Zeus'un dönüşümleri, Persephone'nin kaçırılışı,
Medusa'nın kaderi, Daphne). Bu anlatılar bu kitapta **iki yoldan biriyle**
ele alınır:

1. **Hikâye o unsuru gerektirmiyorsa** — anlatı, olayın *sonucundan*
   başlar (*"Persephone yeraltına götürüldü"* — nasıl değil, ne oldu).
   `ageAdaptationNote` kaynakta ne olduğunu **kaydeder**.
2. **Hikâye o unsura dayanıyorsa** — hikâye bu kitaba **alınmaz**.
   Yerine aynı kültürden başka bir hikâye gelir.

Bu kurala **istisna yoktur** ve `qa_age.py` bunu bir kapı olarak arar.

### 2.9 · İstismar · `OMIT`

| | |
|---|---|
| **İzin verilen** | Haksızlık, zorbalık, adaletsiz ceza, güçlünün güçsüzü ezmesi — **çocuğun tanıyabileceği** biçimde |
| **İma edilen** | — |
| **Çıkarılan** | Çocuk istismarı her biçimde; ev içi şiddetin sahnelenmesi; tekrarlayan aşağılamanın uzatılması; "hak etti" çerçevelemesi |
| **Özel inceleme** | Üvey anne/baba zulmü içeren halk anlatıları (yaygın ve kaçınılmaz) — **ceza ölçülü, sonuç adil** olmalı |

### 2.10 · Kaçırma · `ALLOW` (sınırlı)

| | |
|---|---|
| **İzin verilen** | Kaçırılma olayı; aramak; kurtarmak; geri dönememek |
| **İma edilen** | Esaret koşulları |
| **Çıkarılan** | Kaçırılanın çaresizliğinin uzatılmış betimi; "kimse gelmeyecek" tonunun sürdürülmesi |
| **Özel inceleme** | Bir **çocuğun** kaçırılması — bir hikâyede en fazla **bir kez** ve mutlaka çözümle |

> Gerekçe: 8–12 yaş için kaçırılma en yakın gerçek korkulardan biridir.
> Mit onu işleyebilir ama **çözümsüz bırakamaz**.

### 2.11 · Savaş · `ALLOW`

| | |
|---|---|
| **İzin verilen** | Savaşın olması, orduların çarpışması, kuşatma, kahramanlık, yenilgi, savaşın bedeli |
| **İma edilen** | Savaş alanının hâli |
| **Çıkarılan** | Katliam betimi; sivil ölümlerin sahnelenmesi; "zafer sarhoşluğu" tonu |
| **Özel inceleme** | Yaşayan bir halkın tarihsel travmasına dokunan anlatılar |

**Kural:** savaş bu kitapta **hiçbir zaman şanlı değildir.** Kaynak
kahramanı yüceltiyorsa kitap onu anlatır, ama savaşın bedelini de anlatır.

### 2.12 · İntikam · `ALLOW`

| | |
|---|---|
| **İzin verilen** | İntikam arzusu, planı, gerçekleşmesi, gerçekleşmemesi, boşa çıkması |
| **İma edilen** | İntikamın şiddet ayrıntısı (§ 2.1) |
| **Çıkarılan** | İntikamın **onaylandığı** çerçeveleme (*"böylece hak ettiğini buldu ve herkes mutlu oldu"*) |
| **Özel inceleme** | — |

İntikam mitolojinin motorudur ve serbesttir. Kısıt **ahlaki
çerçevelemededir**: kitap intikamı ne över ne yargılar, **anlatır** ve
bedelini gösterir.

### 2.13 · Ceza · `ALLOW` / `IMPLY`

| | |
|---|---|
| **İzin verilen** | İlahi ceza, sürgün, dönüşüm cezası, unutulma, sonsuz görev (Sisifos, Tantalos, Prometheus) |
| **İma edilen** | Bedensel cezanın uygulanışı — *"her gün geri geliyordu"* yeter |
| **Çıkarılan** | Süregelen işkencenin duyusal betimi; ceza sahnesinin tekrarlanarak uzatılması |
| **Özel inceleme** | — |

### 2.14 · Doğaüstü korku · `IMPLY`

| | |
|---|---|
| **İzin verilen** | Hayalet, ruh, lanet, kehanet, uğursuzluk, karanlık, yalnızlık, "bir şey var" hissi |
| **İma edilen** | Dehşet anı — **tepki** yazılır, **görüntü** yazılmaz |
| **Çıkarılan** | Ceset imgesi; yavaş yaklaşan tehdidin uzatılması; okuru irkiltmeye yönelik ani sahne (jump scare); uykuya götürülecek son cümlede çözümsüz korku |
| **Özel inceleme** | Bir hikâyenin **korku** tonuyla bitmesi |

**Kural — "son sayfa kuralı":** bir hikâye korkuyla **açılabilir**,
korkuyla **ilerleyebilir**, ama **korkuyla bitmez**. Son paragraf her
zaman bir zemin verir: bir sonuç, bir anlam, bir sabah.

### 2.15 · Dinî malzeme · `REVIEW`

| | |
|---|---|
| **İzin verilen** | Tanrılar, yaratılış, kozmoloji, ritüel varlığı, kutsal yerler, inanç pratiğinin **anlatılması** |
| **İma edilen** | — |
| **Çıkarılan** | Bir inancın doğru/yanlış ilan edilmesi; "eskiden inanılırdı ama artık biliyoruz ki" tonu; yaşayan bir dinin kutsalıyla alay |
| **Özel inceleme** | **Bugün yaşayan bir dine ait** her anlatı (Hindu, Şinto, Yahudilik, Hristiyanlık, İslam, yerli inanç sistemleri) |

**İki mutlak kural:**

1. **Geçmiş zaman tuzağı yok.** *"Eski Yunanlılar Zeus'a inanırdı"*
   yazılabilir; *"Hindular Ganeşa'ya inanırdı"* yazılamaz — çünkü hâlâ
   inanılıyor. Yaşayan inanç **şimdiki zamanda** anlatılır.
2. **"Mit" kelimesi yaşayan inanç için kullanılmaz.** Kitabın başlığı
   *myths* der; metin içinde yaşayan bir gelenek için *story*, *telling*,
   *tradition* kullanılır.

### 2.16 · Kültürel olarak hassas pratikler · `REVIEW`

| | |
|---|---|
| **İzin verilen** | Yayımlanmış ve kısıtlanmamış malzeme |
| **İma edilen** | — |
| **Çıkarılan** | **Kısıtlı bilgi**: başlatma (initiation) anlatısı, tören nesnesi ayrıntısı, klan işareti, maske deseni, yer-özel kutsal anlatı, kimin anlatabileceği kurala bağlı olan malzeme |
| **Özel inceleme** | 22 kültürün **tamamı** — muafiyet yoktur (karar K20) |

**Kısıtlı olduğu bilinen anlatı anlatılmaz — kısıtlı olduğu söylenir.**
Bu, Bestiarium'dan devralınan kuraldır ve burada muafiyetsizdir.

Her araştırma kaydında `restrictionScreened: true` ve **açık bir cümleyle**
ne tarandığı yazılır. `validate_research.py` boş bırakılmasına izin vermez.

**Kasıtlı dışarıda bırakma** bir kusur değil, bir karardır ve arka maddede
**okura söylenir** (Bestiarium'un Sonsöz pratiği).

### 2.17 · Korkutucu imgelem · `IMPLY`

| | |
|---|---|
| **İzin verilen** | Karanlık, fırtına, derin su, uçurum, orman, yalnız yol, kapalı yer, kaybolma |
| **İma edilen** | Tehlikenin yakınlığı |
| **Çıkarılan** | Görsel olarak **çizilecek** korkutucu imge (illüstrasyon şartnamesine geçer): parçalanmış beden, kan, ceset, dehşet ifadesi |
| **Özel inceleme** | Hikâye açılış illüstrasyonunun konusu — **kapak ve açılış görselleri "Look Inside"da görünür** ve ebeveynin ilk izlenimini kurar |

> Yol haritası R4 (iade oranı) azaltmasını hatırlatır: *"'Look Inside'
> örneğinde **gerçek** bir bölüm açılışı ve **gerçek** bir illüstrasyon."*
> Yani ilk illüstrasyonlar ebeveynin gördüğü ilk şeydir.

---

## 3. Özet tablo

| # | Kategori | Seviye |
|---|---|---|
| 1 | Şiddet | `IMPLY` |
| 2 | Ölüm | `ALLOW` |
| 3 | Yas ve keder | `ALLOW` |
| 4 | Canavarlar | `ALLOW` |
| 5 | Dönüşüm | `ALLOW` |
| 6 | Yamyamlık | `IMPLY` / kısmen `OMIT` |
| 7 | Kurban | `IMPLY` + `REVIEW` |
| 8 | Cinsellik | `OMIT` |
| 9 | İstismar | `OMIT` |
| 10 | Kaçırma | `ALLOW` (sınırlı) |
| 11 | Savaş | `ALLOW` |
| 12 | İntikam | `ALLOW` |
| 13 | Ceza | `ALLOW` / `IMPLY` |
| 14 | Doğaüstü korku | `IMPLY` |
| 15 | Dinî malzeme | `REVIEW` |
| 16 | Kültürel hassasiyet | `REVIEW` (muafiyetsiz) |
| 17 | Korkutucu imgelem | `IMPLY` |

---

## 4. Ölçülebilir eşikler — `qa_age.py` bunları kapıya bağlar

Bir politika ancak ölçülebiliyorsa kapı olabilir.

| Ölçü | Eşik | Neden |
|---|---|---|
| Grafik şiddet sözcük yoğunluğu | **0** yasaklı sözcük | Liste `04_BUILD/mythbook.py` → `GRAPHIC_TERMS` |
| Cinsel içerik sözcükleri | **0** | `SEXUAL_TERMS` |
| Şiddet sahnesi uzunluğu | ardışık **≤3 cümle** yoğun eylem | § 2.1 |
| Bir hikâyede yoğun sahne sayısı | **≤2** | Ritim; art arda gerilim yorar |
| Hikâye son paragrafı | çözümsüz korku **yok** | "Son sayfa kuralı" § 2.14 |
| Yetişkin sözcük dağarcığı | **≤%2** zor sözcük | `qa_readability.py` ile ortak |
| Ünlem işareti | hikâye başına **≤3** | Yetişkin cildinin 0 kuralı burada yanlış (§ G); ama abartı da yorucudur |
| `ageReviewStatus` alanı | **boş bırakılamaz** | Her hikâye kaydında |
| `REVIEW` kategorili hikâye | `03_EDITORIAL/AGE_REVIEW_LOG.md` kaydı **zorunlu** | İzlenebilirlik |
| Ebeveyn okuması | Faz 5 kapısında **≥2 imzalı kayıt** | Yol haritasının emri |

> **Kapının kendisi sınanır.** `05_TESTS/selftest.py` her eşik için
> kasıtlı bir ihlal üretir ve kapının onu yakaladığını kanıtlar. Bu
> mekanizma olmadan yaş kapısı bir niyet beyanıdır, bir kapı değil.

---

## 5. Bu politika neyi YAPMAZ

- **Kültürel sterilizasyon yapmaz.** Bir kültürün anlatısı, rahatsız edici
  bulunduğu için değiştirilmez. Değiştirilmesi gerekiyorsa **hikâye
  değişir**, kültür değil.
- **Yumuşatma yapmaz.** Kaynakta trajikse trajik kalır.
- **Ahlak dersi vermez.** Mit ders vermek için anlatılmaz; sonunda
  *"böylece öğrendiler ki…"* yoktur.
- **Homojenleştirme yapmaz.** 22 kültür 22 farklı ton taşır. Politika
  **tavanı** belirler, sesi değil.

---

## 6. Onay ve değiştirme

Bu belge **kurucu onayı** gerektirir ve Faz 1 başlamadan onaylanmalıdır
(yol haritası: *"**yazım öncesi** AGE_POLICY.md"*).

Değişiklik: kurucu kararı → `DECISIONS.md`'ye `K##` → `CHANGELOG.md` →
`qa_age.py` eşiği → `selftest.py` kurgusu. **Beş adımın hepsi**, yoksa
politika ile kapı ayrışır ve ayrışan bir kapı ölü kuraldır.
