# FAZ 3 · GENİŞLEME — TAMAMLANMA RAPORU

> **The Great Book of World Myths** · `v0.3.0` · kapı `phase3`
> 9 Ağustos 2026
>
> Faz 2 sesin **on altı hikâyede** mekanikleşmeden var olabildiğini
> kanıtladı. Faz 3'ün sorusu başkaydı: **aynı ses on dört kültüre yayılınca
> hâlâ tek bir kitabın sesi mi?**
>
> Bu rapor tek yetkili Faz 3 raporudur. Ölçüm dosyaları:
> `06_REPORTS/*.json` · `06_REPORTS/tracked/*.json`

---

## 0. Tek bakışta

| | Hedef | Ölçülen | |
|---|---:|---:|---|
| Yeni hikâye | 15 | **15** | ✅ |
| Kümülatif hikâye | 31 / 45 | **31 / 45** | ✅ |
| Yeni kelime | ~14.250 | **13.739** | ✅ (−%3,6) |
| Kümülatif kelime | ~29.450 | **28.712** | ✅ (−%2,5) |
| Hikâye ortalaması | 950 | **916** | ✅ bant içi |
| Bant dışı hikâye | 0 | **0** | ✅ |
| Kültür kartı metni | 22 | **22** | ✅ |
| Telaffuz rehberi | tam | **166 kayıt · 45/45 hikâye** | ✅ |
| "Kim kimdir" sözlüğü | tam | **125 madde · 45/45 hikâye** | ✅ |
| İkinci ara prova | evet | **31 hikâye dizildi** | ✅ |
| Sayfa modeli yeniden ölçüm | evet | **363,7 kelime/sayfa · 228 sayfa** | ✅ |
| Sürüklenme | ölçülsün | **%+19,6** (eşik %35) | ✅ |
| Kapıların kendi testi | geçsin | **78 / 78** | ✅ |
| Manuscript sızıntısı | 0 | **0** | ✅ |
| **Ham görsel** | 40 | **0 / 40** | ⏳ **KURUCU (H7)** |

---

## 1. Yazılan on beş hikâye

| # | Hikâye | Kültür | Kelime | FK | Ad |
|---:|---|---|---:|---:|---:|
| 16 | The One-Eyed Giant of the Oghuz | Turkic | 932 | 4,3 | 4 |
| 17 | The Baby Who Mistook the Sun for Fruit | Hindu | 960 | 4,4 | 3 |
| 18 | The River That Had to Be Slowed Down | Hindu | 882 | 4,6 | 4 |
| 19 | The Woman Who Patched the Sky | Chinese | 927 | 4,2 | 1 |
| 20 | The Archer and the Woman on the Moon | Chinese | 1012 | 4,0 | 3 |
| 22 | The Boy Who Told the Fish to Rise | Korean | 864 | 4,5 | 5 |
| 23 | The Door That Was Opened by Laughing | Japanese | 932 | 4,0 | 5 |
| 24 | Eight Heads and Eight Bowls of Wine | Japanese | 966 | 4,0 | 4 |
| 25 | The Hundred Children in the Egg Sac | Vietnamese | 924 | 4,1 | 5 |
| 26 | Why the River Rises Every Year | Vietnamese | 865 | 4,0 | 5 |
| 27 | Eighty Years of Arguing | Ancient Egyptian | 881 | 4,3 | 6 |
| 28 | The Name the Sun God Would Not Say | Ancient Egyptian | 891 | 3,7 | 3 |
| 29 | The Island That Was Not There Afterwards | Ancient Egyptian | 1002 | 3,4 | 1 |
| 30 | The Chain Let Down from the Sky | Yoruba | 871 | 3,8 | 5 |
| 31 | The One They Left Out | Yoruba | 830 | 4,1 | 3 |

**13.739 kelime · ortalama 916 · FK ortalaması 4,10 · bant dışı 0.**

### Kapsam sonucu

**Bölüm 2** (*Between the Two Rivers*) tamamlandı · **Bölüm 3**
(*Where the Sun Comes Up*) **10/10 tamamlandı** · **Bölüm 4**
(*The Long River and the Forest Road*) **5/8 açıldı**.

Yeni kültürler: **Hindu · Çin · Japon · Vietnam · Mısır · Yoruba**.
Kitap artık **14 kültür** taşıyor (22'nin 14'ü) ve dört makro bölgeye
yayılıyor.

---

## 2. Kapsam çelişkisi ve çözümü — K29

Yol haritası Faz 3 için **iki farklı şey** söylüyor:

- § 12 dağılım tablosu ve § 16 "Hedef" satırı: **15 hikâye · kümülatif 31**
- § 16 "İş" satırı: **üçüncü ve dördüncü bölge**

Yazılmamış 3. + 4. bölge **18 hikâye** taşıyor, artı 2. bölgeden devreden
#16 = **19**. İki okuma çelişiyor.

**Kazanan sayıdır** (`DECISIONS.md` § K29), üç gerekçeyle:

1. Kümülatif hedef bir **DoD ölçütüdür** ("kümülatif hikâye hedefi tam
   olarak tutuyor"); bölge tarifi bir iş tanımıdır.
2. `project_config.phases` sayıyı **makine okunur** tutar ve
   `validate_spec` onu kapı yapar.
3. **Faz 2 aynı çelişkiyi aynı yönde çözdü** — #16 bölge sırasında
   olmasına rağmen ertelendi ki kümülatif dizi bozulmasın.

Aritmetik birebir kapanıyor: **Faz 4 = kalan 3 (4. bölge) + 5. bölge (7)
+ 6. bölge (4) = 14**, yani yol haritasının Faz 4 hedefi. Bölge tarifini
kazandıran okuma Faz 3'ü 34'e, Faz 4'ü 11'e taşır ve **iki fazın da
sayısal hedefini birden kırar**.

---

## 3. Kapı kusurları — altı tanesi, üçü tek kelime yazılmadan

Faz 3'ün ilk işi yazmak değil, kapıları **hikâyelerin gerçek adlarına
karşı** sınamak oldu. Hepsi aynı sınıftan: **doğru metni reddeden cetvel**
(Bestiarium D32).

### ① `mythbook._WORD` birleşen işaretleri ve ʻokinayı sözcük saymıyordu

```
Ọ̀ṣun          → ['Ọ', 'ṣun']        ad İKİYE bölünüyor
Ilé-Ifẹ̀       → ['Ilé-Ifẹ']         son ton işareti düşüyor
Hiʻiaka        → ['Hi', 'iaka']      ʻokina Hawaiʻicede HARFTİR
Nāmakaokahaʻi  → ['Nāmakaokaha','i']
```

Yorubaca ton işareti taban harfin üstüne **ayrı bir kod noktası** olarak
biner; `ẹ̀` ve `ọ̀` için önceden birleştirilmiş kod noktası Unicode'da
**yoktur**. Sonuç: sözcük sayısı şişiyor, `proper_names()` var olmayan
adlar üretiyor, `qa_crossref` **doğru yazılmış** bir adı "telaffuz
rehberinde eksik" sanıyor.

En can alıcı yanı: `CHILDREN_WRITING_STYLE.md` § 5 korunacak diakritiklere
örnek olarak **tam da `Ọ̀ṣun` ve `Māui` adlarını** verir. Cetvel, üslup
belgesinin **adıyla saydığı** yazımları ölçemiyordu.

**Düzeltme:** karakter sınıfı U+0300–U+036F ve U+02BB/U+02BC ile
genişletildi, **kaçış dizisiyle** yazıldı (LESSONS § B5: birleşen bir
işaret kaynağa doğrudan yazılırsa görünmez olur ve dosyanın kendisini
kirletir). Altı adlık iki yönlü regresyon testi eklendi.

### ② `qa_crossref` künyeyi metinden farklı tokenize ediyordu

Künye adı kesme işaretinden bölünüyordu, metin belirteci bölünmüyordu:

```
künye  “Chang’e”  → {“Chang”, “e”}
metin  “Chang’e”  → tek belirteç
sonuç  eşleşme YOK → doğru yazılmış ad “eksik” sanılıyor
```

Aynı tuzak `K’iche’`, `Q’ukumatz`, `Man’yōshū` adlarını da vuruyordu —
yani kapı, kesme işaretini **ortografik** kullanan dilleri (Maya dilleri,
pinyin, Hepburn) **toptan cezalandırıyordu**. Faz 2'nin iyelik eki
düzeltmesiyle aynı sebep: **iki ayrı tokenizer**.

**Düzeltme:** `mythbook.declared_tokens()` — künye ile metin tek kaynaktan.

### ③ Okura giden dizelerde tipografi hiç denetlenmiyordu → K28

`qa_voice` düz kesme kuralını uyguluyordu ama **yalnızca manuscript'e**.
Oysa okura giden dizelerin bir kısmı dizinde durur: **başlık** (içindekiler
ve hikâye başlığı), **telaffuz rehberi adı**, **"kim kimdir" rolü**,
**kültür adı ve bölgesi**. O dizeler hiçbir kapının kapsamında değildi.

Tarama **33 kusur** buldu, üç türde:

- İngilizce iyelik: *"The Blacksmith's Apron"*, *"Osiris's son"*
- Ortografik kesme: *"Chang'e"*, *"K'iche'"*, *"Man'yōshū"*
- **Kendi içinde tutarsız**: *"K’iche' is spoken by…"* — aynı adın iki
  karakteri, tek cümlede. Kalıcı kanıt: bu sınıf elle tutulamaz.

**Düzeltme:** K28 (tek kesme karakteri `’`) + `qa_diacritics` içinde yeni
kapı + üç yönlü selftest. Kaynak künyeleri (`pronunciationSource`,
`sources`) **bilerek dışarıda**: kaynağın kendi yazımını düzeltmek
alıntıyı bozar.

### ④ Yaş incelemesi kapısı "kuyrukta" ile "incelendi"yi ayırt edemiyordu

`qa_age`, `REVIEW` kategorili yazılmış bir hikâye için kimliğin
`AGE_REVIEW_LOG.md` içinde **bir yerde** geçmesini arıyordu — ve defterin
"bekleyen inceleme kuyruğu" tablosu bu şartı **zaten sağlıyordu**. Yani
bir hikâye **hiç incelenmeden**, sırf kuyrukta durduğu için kapıdan
geçebilirdi.

Faz 2'de kusur **tetiklenmedi**: yazılan 15 hikâyenin hiçbiri `REVIEW`
kategorisi taşımıyordu. **Faz 3'ün altısı taşıyor** — yani kusur tam da
yetkinin kullanılacağı anda ortaya çıkacaktı.

**Düzeltme:** kapı artık yalnızca `<!-- AGE-REVIEW:RECORDED -->` bloğunu
okur. `selftest` iki yönlü sınar: kuyruk kaydı **saymamalı**, sonuç kaydı
**saymalı**. Faz 1–2'nin 16 hikâyesi geriye dönük olarak deftere işlendi.

### ⑤ Edilgen çatı taraması sıfatı ortaç sayıyordu

Desen yalnızca sözcük **sonuna** bakıyordu (`-ed/-en/-wn/-ne`). 22 hikâye
üzerinde sayıldığında eşleşmelerin **altıda biri** hiçbir fiilin ortacı
değildi:

```
was open · was red · was one · was alone · was down
was often · was golden · was fifteen · was when · was medicine
```

Ölçü **%18 şişiyordu** ve şişme, **kısa somut cümle** yazan prozayı —
yani üslup belgesinin **emrettiği** prozayı — daha edilgen gösteriyordu.

**Düzeltme:** muafiyet listesi **manuscript taranarak** çıkarıldı, tahmin
edilmedi. Gerçekten tartışmalı olanlar (*"was frightened"*, *"was tired"*)
**bilerek dışarıda** — fiilleri geçişlidir, o kalıplar edilgen olabilir.
Düzeltmeden sonra `chinese-nuwa-sky`'ın "yüksek edilgen" uyarısı kayboldu:
**proza baştan doğruydu, cetvel yanlıştı.**

### ⑥ Arka madde ADAY havuzunu okura basıyordu

`make_index.py` `status != "dropped"` süzüyordu, yani **aday** hikâyeleri
de içeri alıyordu. Sonuç: telaffuz rehberinde **26 kayıt** ve "kim
kimdir"de **22 madde**, kitapta hiç geçmeyen hikâyelerden — *Baba Yaga*,
*Eurydice*, *Fionn*, *Gaṇeśa*, *Hayk*…

Bu, yol haritasının o iki eki koyma **gerekçesini** çürütür:

> *"Öğretmen ve kütüphaneci için satın alma gerekçesi; **iade oranını
> düşürür**."*

Rehberde bulup kitapta bulamamak, iade sebebidir. Kusur Faz 1'den beri
vardı ve görünmedi, çünkü rehberin **tam üretimi** ilk kez Faz 3'ün işidir.

**Düzeltme:** süzgeç düzeltildi + `qa_crossref` **üretilen dosyanın
kendisini** okuyan bir denetim kazandı (niyete değil **artefakta** bakar).
Kasıtlı kusurla ısırdığı kanıtlandı.

---

## 4. Kültür kartı metinleri — 22/22

`culture_index.schema.json` yeni bir alan kazandı: `cardText` — dil ·
kim anlatır · nerede · **bugün**.

**1.399 kelime** (bütçe § 12: 22 × ~60 = 1.320 · sapma %+6).

`validate_spec.check_culture_cards` dört şey denetler ve dördü de
`selftest` ile kanıtlıdır:

| Denetim | Neden |
|---|---|
| Her kilitli kültürün kartı var | yol haritası § 16 Faz 3 teslimi |
| Üç cümle bantta (45–85 kelime) | kelime bütçesi § 12 |
| **Yaşayan gelenek → "bugün" cümlesi şimdiki zamanda** | AGE_POLICY § 2.15; `EDITORIAL_ARCHITECTURE` § 7 bu cümleyi tam olarak geçmiş zaman tuzağını **sayfada görünür** kılmak için koydu |
| **Kalıplaşma yok** | 22 kart 22 ayrı cümle kurmak zorunda; kalıplaşırsa okur kartı **atlamayı öğrenir** (R6 · K13) |

Kapı yaşamayan gelenekleri (Yunan, İskandinav, Mısır…) şimdiki zamana
**zorlamaz** — selftest bunu ayrıca sınar.

---

## 5. Telaffuz rehberi ve sözlük — ilk tam üretim

| | Ölçülen |
|---|---:|
| Telaffuz kaydı | **166** |
| "Kim kimdir" maddesi | **125** |
| Kapsanan hikâye | **45 / 45** |
| Kaynaksız telaffuz | **0** |
| Rehberde olup kitapta olmayan | **0** |

`qa_crossref` `phase3`'ten itibaren **iki yönlü** çalışıyor:
kitaptaki her hikâyenin kaydı **var**, ve rehberde kitapta olmayan bir
kayıt **yok**.

Faz 3'te 8 telaffuz kaydı eklendi; hepsi **metinde geçen** ve künyede
eksik olan gerçek adlardı: `Oghuz` · `Buyeo` · `Ise` · `Suga` · `Phú Thọ`
· `Hùng` · `Egypt` · `Egyptian` · `Yoruba`.

### Editoryal kural — modern ülke adı hikâye metnine girmez

İlk taslaklarda `Japan`, `Vietnam`, `Nigeria`, `Brazil`, `Hanoi` proza
içindeydi ve `qa_crossref` onları eksik künye olarak yakaladı. Doğru çözüm
onları rehbere eklemek **değildi**: bir çocuk "Japan" adını aramaz ve
rehberi şişirmek satın alma gerekçesini zayıflatır. Ülke adı 8. yüzyıl
sahnesinde hafif **anakroniktir**; bugüne bağlanma işi **kültürel notun**
işidir.

**Ama `Egypt` istisnadır ve gerekçesi ayrıdır:** Mısır bu hikâyelerin
geçtiği yerdir ve üslup § 7 kültürün **adıyla** anılmasını emreder —
`Crete`, `Lydia`, `Uruk`, `Ásgarðr` ile aynı sınıf. Künyelendi.

---

## 6. Sayfa modeli — yeniden ölçüm

### 6.1 Kelime/sayfa ve sayfa sayısı

| | Faz 1 (1 hikâye) | Faz 3 (31 hikâye) | Fark |
|---|---:|---:|---:|
| Kelime/sayfa (tahmin) | 357,5 | 357,5 | — |
| Kelime/sayfa (**ölçüm**) | 357,5 | **363,7** | **+%1,7** |
| Hikâye/sayfa | 4 | **4** | 0 |
| Kitap sayfası | 228 | **228** | **0** |
| Ciltsiz telif | 6,46 $ | **6,46 $** | **0,00 $** |

**31/31 hikâye modelin öngördüğü 4 sayfada dizildi.** Gövde 124 sayfa.
Model 31 hikâyelik gerçek prozayla **tuttu**.

### 6.2 K27 gerçek metinle ilk kez sınandı ve TUTMADI

Bu, Faz 3'ün en önemli üretim bulgusudur.

K27 kültür kartına **ek sayfa ayırmaz**: kart, hikâyenin **zaten ödenen**
kuyruk boşluğunda durur. Karar verilirken oraya şunun sığacağı
varsayılmıştı:

```
vinyet ≈ 10 satır + ÜÇ CÜMLE ≈ 3 satır + harita işareti ≈ 2 satır = 15
```

**"Üç cümle ≈ 3 satır" ölçülemezdi**, çünkü kart metinleri **Faz 3'ün
teslimidir**: karar verildiğinde ölçülecek metin **yoktu**.

`proof_interior.py` artık gerçek kart metnini gerçek metin bloğuna dizer.
Ölçüm: üç cümle **6–8 satır** tutuyor, kart toplamı **20–21 satır**.

**14 kültürün 5'inin kartı kendi ilk hikâyesinin kuyruğuna sığmıyor:**

| Kültür | Kart gerekli | Kuyruk boş | Açık |
|---|---:|---:|---:|
| greek (`greek-persephone`, 1030 kelime) | 20 | 9 | **−11** |
| norse (`norse-thors-hammer`) | 21 | 18 | −3 |
| korean (`korean-dangun`) | 21 | 18 | −3 |
| hindu (`hindu-hanuman-sun`) | 21 | 20 | −1 |
| japanese (`japanese-amaterasu-cave`) | 21 | 20 | −1 |

**Kök sebep tek bir varsayım değil, ikisi birden:**

1. Kart metni tahmin edilenin **iki katı** uzunlukta.
2. Kuyruk boşluğu **hikâye uzunluğuna bağlı** — 1030 kelimelik bir hikâye
   870 kelimelikten **~13 satır az** boşluk bırakıyor. K27 ortalama
   hikâyeyi varsaydı.

**Kartı daha bol kuyruklu bir hikâyeye kaydırmak** 14 kültürün 12'sini
çözüyor (japanese ve norse yine sığmıyor) — ama bu **editoryal olarak
yanlıştır**: kart kültürü **tanıtır**, dolayısıyla o kültürün **ilk**
hikâyesinde durmak zorundadır. Üçüncü Yunan hikâyesinden sonra gelen bir
Yunan kartı okura geç kalır.

**Karar Faz 3'te VERİLMEDİ.** Yol haritası § 16 A4/K27'nin kilitlenmesini
**Faz 4'e** koyar ("sayfa bütçesinin son kez ölçülmesi; A4/A5 kararlarının
kilitlenmesi"). Faz 3'ün işi ölçmek ve sapmayı belgelemek.

Denetimin şiddeti aynı kurala bağlandı: `phase3`'te **uyarı**,
`phase4`'ten itibaren **hata** — yol haritasının sayfa bütçesi için zaten
kullandığı eşik yükseltmesinin (§ 16 Faz 4: *"sayfa bütçesi artık UYARI
DEĞİL HATA"*) aynısı.

**Faz 4 için kurucuya giden seçenekler** (hiçbiri Faz 3'te uygulanmadı):

| Şık | Ne yapar | Bedeli |
|---|---|---|
| (i) Kart metnini ~35 kelimeye indir | üç cümle → 3 satıra iner, K27 tutar | § 12 bütçesinin yarısı; "üç cümle" fiilen iki cümleye düşer |
| (ii) Vinyeti küçült (10 → 6 satır) | 4 satır kazandırır | 22 vinyetin görünürlüğü düşer — K27'nin (b′)'yi reddetme gerekçesi buydu |
| (iii) Kart taşan kültürlerde ayrı sayfaya çıksın | kesin çözüm | ~5 sayfa ekler → telif ~0,06 $/kopya düşer |
| (iv) O kültürün ilk hikâyesi kısa olan seçilsin | sıralama değişikliği | bölüm içi hikâye sırası editoryal karardır |

---

## 7. Üslup sürüklenmesi — ölçüldü, düzeltilmedi (D40)

| Kontrol | Hikâye | Eğim |
|---|---:|---:|
| Parti 1 | 19 | **%+14,7** |
| Parti 2 | 22 | **%+16,6** |
| Parti 3 | 25 | **%+14,8** |
| Parti 4 | 28 | **%+14,0** |
| **Parti 5 · faz kapanışı** | **31** | **%+19,6** |

Uyarı eşiği **%20**, başarısızlık eşiği **%35**. Hiçbir ölçümde uyarı
eşiği aşılmadı.

Yükselen sözcükler: `down` · `came` · `all` · `said` · `went` · `back` ·
`nobody` · `made` · `people` · `nothing`. **Hepsi anlatısal ve yapısal.**
Bestiarium'un Faz 3'te yakaladığı **analitik kayıt sınıfı** (*about ·
rather · nothing · tradition · creature* — yani **kitabın kendine
göndermesi**) bu ölçümde **yok**.

D40 gereği **düzeltme yapılmadı**. Düzeltme editoryal inceleme geçişine
aittir ve yol haritası onu **Faz 4'e** koyar (*"üslup uyumlama geçişi —
45 hikâye BİRLİKTE ele alınır"*).

### Ses kalibrasyonunun kendisi bir bulgudur

Faz 3'ün ilk taslakları kitabın kurulmuş sesinden **ölçülebilir biçimde
saptı** ve düzeltme üç geçiş aldı:

| | 1. taslak | 2. taslak | Yerleşen | Kitap tabanı (Faz 1–2) |
|---|---:|---:|---:|---:|
| Cümle ortalaması | 13,4–16,7 | 10,1–10,6 | **11,0–13,1** | 11,6 |
| Hece/kelime | 1,19–1,23 | 1,25–1,27 | **1,21–1,31** | 1,35 |
| Paragraf (cümle) | 2,2–2,8 | 2,3–2,9 | **2,3–3,5** | 3,4 |

Bütün düzeltmeler **sahne yeniden yazımıyla** yapıldı. Talimat § 29
uyarınca **hiçbir mekanik dönüşüm kullanılmadı**: toplu sözcük değişimi
yok, eşanlamlı ikamesi yok, ölçü güdümlü öbek enjeksiyonu yok.

---

## 8. Yaş politikası — bu fazın altı zor kararı

Faz 3'ün 15 hikâyesinin **altısı** `REVIEW` kategorisi taşıyor (Faz 2'de
**sıfırdı**). Tam kayıt: `03_EDITORIAL/AGE_REVIEW_LOG.md` § 2.3.

| Hikâye | Karar |
|---|---|
| `yoruba-obatala-land` | **ENGELLİLİK AİTİYOLOJİSİ KULLANILMADI.** Birkaç anlatımda Ọbàtálá'nın yarım bıraktığı iş, engelli doğan insanların açıklamasıdır. O açıklama kitapta **yoktur** — engelli okuru bir **hata** olarak çerçeveler. Yarım kalan iş korundu; açıklama düşürüldü ve karar **yazılı**, çünkü okur ona başka yerde rastlayabilir. |
| `egyptian-horus-seth` | **Cinsellik § 2.8 OMIT, istisnasız.** Chester Beatty I'in açık bölümleri ve sakatlama **tamamen dışarıda**. Anlatı mahkeme, kayık yarışı ve kılık değiştirme üzerinden taşınıyor — kaynak bunu **bütünüyle destekliyor**, yani çıkarma anlatıyı fakirleştirmedi. |
| `japanese-susanoo-orochi` | **Kurban § 2.7.** Yedi kızın alınmış olması **olaydır, sahne değildir**: okur bunu ağlayan iki ebeveynden öğrenir. Sekizinci kız bir kurban değil bir **kişidir**. Kılıç için § 2.16: kapalı olduğu **söylenir**, uydurulmaz. |
| `japanese-amaterasu-cave` | Susanoo'nun tahribatı özetlendi; atın derisinin yüzülmesi ve dokumacının ölümü **betimlenmez**. |
| `hindu-hanuman-sun` · `hindu-ganga-descent` | **Yaşayan din § 2.15.** "myth" sözcüğü metinde yok, geçmiş zaman tuzağı yok, ritüel talimatı yok. |
| `yoruba-osun-seventeenth` | Festivalin **dışarıdan görülen** kısmı anlatıldı; inisiyasyon ve divinasyon anlatılmadı, ve **neden anlatılmadığı okura söylendi**. |

Ayrıca `egyptian-isis-secret-name`, SOURCING_STANDARD § 10'un doğrudan
uygulamasıdır: **Ra'nın gizli adı hiçbir nüshada yazmıyor** ve kitap onu
uydurmuyor. Boşluk kapatılmadı, okura **gösterildi**.

---

## 9. Kapı sonuçları

| Kapı | Sonuç |
|---|---|
| `validate_spec --gate phase3` | ✅ 65 geçti · 0 uyarı |
| `validate_structure` | ✅ 37 geçti · 2 uyarı |
| `validate_research` | ✅ 3 geçti |
| **`selftest`** | ✅ **78 geçti / 0 başarısız** (Faz 2: 47) |
| `qa_length` | ✅ 4 geçti |
| `qa_age` | ✅ 12 geçti |
| `qa_readability` | ✅ 6 geçti · 4 uyarı |
| `qa_voice` | ✅ 8 geçti · 2 uyarı |
| `qa_echo` | ✅ 3 geçti · 1 uyarı |
| `qa_diacritics` | ✅ 4 geçti |
| `qa_crossref` | ✅ 8 geçti · 0 uyarı |
| `qa_drift` | ✅ 2 geçti |
| `editions` | ✅ 9 geçti |
| `page_budget` | ✅ |
| `proof_interior` | ✅ 2 geçti · 2 uyarı (biri **K27 kart uyumu**) |
| `make_prompts --check` · `make_index --check` · `update_docs --check` | ✅ |
| **Manuscript sızıntısı** | ✅ **0** (kasıtlı sızıntı testiyle sınandı) |

### Açık uyarılar — bilinçli

- **Okunabilirlik hedef bandı**: 4 hikâye FK 3,4–4,0 arasında (güvenli
  aralık 3,0–7,5, hedef bandı 4,0–6,5). En düşük `egyptian-shipwrecked-sailor`
  (3,4): papirüsün kendisi bir **çerçeve anlatısıdır** ve %30 diyalog
  taşır; kısa konuşma cümleleri FK'yı düşürür. Bu, hikâyenin **biçimidir**,
  kusuru değil.
- **Hece/kelime**: 10 hikâye 1,21–1,31 (bant 1,35–1,55). Kitap geneli
  Faz 1'den beri bandın altında (taban 1,31–1,38); bu bir **Faz 3 sapması
  değil, kitabın kendi seviyesidir**.
- **Paragraf uzunluğu**: 8 hikâye 2,3–2,9 (bant 3,0–5,0). Faz 3'ün
  prozası Faz 2'den daha **diyalog yoğun** ve tek cümlelik vuruş
  paragrafları kullanıyor.

Üçü de **ölçüldü ve kaydedildi**; hiçbiri Faz 3'te düzeltilmedi, çünkü
D40 ve yol haritası § 16 üslup uyumlamasını **Faz 4'e** koyar.

---

## 10. Görsel hattı — HAZIRLANDI ≠ ÜRETİLDİ

| Kalem | Durum |
|---|---|
| Prompt kütüphanesi | ✅ **68/68 üretildi** |
| Hikâye promptu konusu hikâyeye özgü | ✅ **45/45** (dönüm anından) |
| Kültür vinyeti promptu | ✅ **22/22** |
| Dünya haritası promptu | ✅ **1/1** |
| Üslup gövdesi tek yerde | ✅ `04_BUILD/imagespec.py` |
| Ölçüm cetveli kalibre | ✅ `image_selftest` |
| **HAM PNG** | ⏳ **0 / 40 — KURUCU BEKLİYOR (H7)** |
| İşlenmiş format | ⏳ ham girdi bekliyor |
| Tolerans dışı görsel | **0** (ölçülecek dosya yok) |

Faz 3'ün görsel kilometre taşı **40 görseldir** (31 hikâye açılışı +
9 kültür vinyeti). **Prompt tarafı 68/68 hazırdır**, yani 40'ın tamamını
kapsar. **Ham görsel üretimi kurucunun işidir** (yol haritası § 21 · H7)
ve bu ajanın çalıştığı ortamda görsel üretme yeteneği **yoktur**.

> Yol haritası § 21: *"**H7 hiçbir yazım fazını BLOKLAMAZ** — hat hazır ve
> kalibre; ham girdi geldiği anda **tek komut yeter**."*

**Bu bir tamamlanma beyanı değildir.** Üç durum ayrıdır ve ayrı tutulur:

```
PROMPT HAZIR          68 / 68   ✅
HAM VARLIK TESLİM      0 / 40   ⏳ KURUCU
İŞLENMİŞ VARLIK DOĞRULANDI  0   ⏳ ham girdi bekliyor
```

Ham girdi geldiğinde çalışacak zincir:

```bash
# 1) ham PNG'ler 07_ASSETS/raw/ altına konur (kurucu)
python3 04_BUILD/convert_images.py
python3 04_BUILD/images.py --measure --json 06_REPORTS/tracked/image-consistency.json
./04_BUILD/qa_all.sh
```

---

## 11. Kurucu bağımlılıkları

| # | Ne | Ne zaman | Durum |
|---|---|---|---|
| **H7** | **68 ham görselin üretimi** | Faz 2–4 | ⏳ **0/40 · en geç Faz 5 üretiminden önce** |
| **H8 / A8** | **İki ebeveyn okuyucusu** | **Faz 4 başlamadan** | ⏳ **AÇIK** |
| A4 / K27 | Kültür kartı yerleşiminin **yeniden kararı** | Faz 4 | ⏳ **§ 6.2'deki ölçümle birlikte kurucuya gitti** |
| — | **Faz 4 onayı** | şimdi | ⏳ bekliyor |

---

## 12. Definition of Done — Faz 3

| # | Ölçüt | Durum |
|---:|---|---|
| 1 | 15 yeni hikâye | ✅ 15 |
| 2 | Kümülatif 31/45 tam | ✅ 31 |
| 3 | ~14.250 yeni kelime | ✅ 13.739 (−%3,6) |
| 4 | Üçüncü bölge tamamlandı | ✅ 10/10 |
| 5 | Dördüncü bölge açıldı | ✅ 5/8 (kalan 3 → Faz 4, K29) |
| 6 | Kültür kartı metni üretildi | ✅ 22/22 |
| 7 | Telaffuz rehberi ilk tam üretim | ✅ 166 kayıt · 45/45 |
| 8 | Sözlük ilk tam üretim | ✅ 125 madde · 45/45 |
| 9 | İkinci ara prova | ✅ 31 hikâye dizildi |
| 10 | Sayfa modeli yeniden ölçüldü | ✅ 363,7 · 228 sayfa · K27 sapması kayıtlı |
| 11 | `qa_crossref` geçiyor | ✅ |
| 12 | Sayfa bütçesi geçiyor | ✅ |
| 13 | Bant dışı hikâye 0 | ✅ |
| 14 | Yasak kalıp 0 · yaş ihlali 0 | ✅ |
| 15 | Hikâyeler arası 8+ kelime tekrar 0 | ✅ |
| 16 | Kültürel not şablonlaşması 0 | ✅ |
| 17 | Sürüklenme ölçüldü ve commit'e geçti | ✅ 5 kontrol noktası |
| 18 | `selftest` geçiyor | ✅ 78/78 |
| 19 | Manuscript sızıntısı 0 | ✅ |
| 20 | Üretilen belgeler taze | ✅ |
| 21 | `.gate` = `phase3` | ✅ |
| 22 | CHANGELOG `[0.3.0]` + her `K##` anılmış | ✅ |
| 23 | `v0.3.0` etiketi | ✅ |
| 24 | **Görsel hedefi** | ⏳ **prompt 68/68 · ham 0/40 — H7, yazımı bloklamaz** |

**PASS** — yazım tarafının tamamı. Tek açık kalem **kurucuya ait
görsel teslimidir** ve yol haritası § 21 onu yazım fazını **bloklamayan**
bağımlılık olarak tanımlar.

---

## 13. Faz 4'e devreden

- **Hikâye:** #32 `akan-ananse-stories` · #33 `akan-ananse-wisdom` ·
  #34 `zulu-chameleon-message` (4. bölgenin kalanı) + 5. bölge (7) +
  6. bölge (4) = **14 hikâye → 45/45**
- **Kültür:** kalan 8 kültür (Akan, Zulu, Inuit, Maya, Aztec, Andean,
  Māori, Hawaiian) — kartları **yazıldı**, hikâyeleri yazılmadı
- **Üslup uyumlama geçişi** — D40'ın ertelediği düzeltme; 45 hikâye
  **birlikte** ele alınır
- **Düşman olgu denetimi** — ayrı oturum, görev çürütmek
- **İki ebeveyn okuması** (A8)
- **A4 / K27 kararı** — § 6.2'deki ölçümle
- **Sayfa bütçesi artık UYARI DEĞİL HATA**, ve kültür kartı uyumu da öyle

---

*Bu rapor Faz 3'ün tek yetkili kaydıdır. Ölçümlerin ham hâli
`06_REPORTS/` altındadır ve hepsi yeniden üretilebilir.*
