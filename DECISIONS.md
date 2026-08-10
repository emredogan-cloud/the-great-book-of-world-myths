# DECISIONS — karar kaydı

> Bu dosya iki şey taşır:
>
> 1. **Alınmış kararlar** (`K##`) — gerekçesiyle, tarihiyle.
> 2. **AÇIK KARARLAR** (`A#`) — kurucudan yanıt bekleyen sorular.
>
> Kural: bir varsayım sessizce proje gerekliliğine dönüşemez. Yol
> haritasının vermediği her şey **önce buraya** yazılır.

---

## AÇIK KARARLAR — kurucudan yanıt bekleyen

Durum tablosu · 8 Ağustos 2026 (Faz 1 koşusunda güncellendi)

| # | Soru | Aciliyet | Ne zaman kapanmalı | Durum |
|---|---|---|---|---|
| **A1** | Manuscript public depoda mı duracak? | **YÜKSEK** | **Faz 1 başlamadan** | ✅ **KAPANDI → K21** |
| **A2** | 22 kültürün tam listesi | YÜKSEK | Faz 1 | ✅ **KAPANDI → K23** |
| **A3** | 45 hikâyenin listesi ve kültür dağılımı | YÜKSEK | Faz 1 | ✅ **KAPANDI → K24, K25** |
| **A4** | 22 kültür vinyetinin sayfadaki yeri | ORTA | Faz 1 | ✅ **KAPANDI → K27** (ölçümden sonra) |
| **A5** | Bölüm (part) mimarisi | ORTA | Faz 1 | ✅ **KAPANDI → K26** |
| **A6** | Büyük punto sürümü v1.0'a girecek mi | DÜŞÜK | Faz 4 | AÇIK (bootstrap varsayımı: hayır → K6) |
| **A7** | KDP Select / KU testi | DÜŞÜK | yayın sonrası | AÇIK |
| **A8** | İki ebeveyn okuyucusu kim | **YÜKSEK** | Faz 4 başlamadan | ✅ **KAPANDI → K32** (kurucu beyanı · Faz 7) |
| **A9** | ISBN: KDP ücretsiz mi, kendi ISBN'imiz mi | DÜŞÜK | Faz 5 | ✅ **KAPANDI → K33** (KDP ücretsiz ISBN · Faz 7) |
| **A10** | Yayıncı / imprint adı | ORTA | Faz 6 | ✅ **KAPANDI → K34** (Vâliçe Press · Faz 7) |
| **A11** | Kapak sanatının etkin çözünürlüğü (115/105 dpi) kabul edilecek mi | ORTA | prova kopyasından sonra | **AÇIK** — ölçüldü, karar kurucunun |

> **Faz 1'in kapattığı beş karar.** A1 ve `AGE_POLICY.md` onayı yol haritasının
> § 21 H1/H2 maddelerine göre Faz 1'in **giriş** kapılarıydı ve iş başlamadan
> önce kurucuya soruldu. A2, A3, A4 ve A5 Faz 1'in **çıktısıdır**: araştırma
> yapıldı, öneri üretildi, kurucu onayladı.
>
> **Faz 7 üç kararı kapattı** (A8, A9, A10) ve bir yenisini açtı (A11).
> Geriye kalan açık kararların hiçbiri **yüksek** öncelikli değildir ve
> hiçbiri dosya üretimini bloklamaz: A6 devre dışı bir sürüm, A7 yayın
> sonrası veri işi, A11 ise prova kopyası görülmeden verilemeyecek bir
> zevk kararıdır.

---

### A1 · Manuscript public depoda mı duracak?

**Durum:** ✅ **KAPANDI → K27'den önce, K21.** Kurucu **(a)** şıkkını seçti;
bootstrap'ın varsayımı onaylandı. Aşağıdaki analiz kararın gerekçesi olarak
korunur.

Talimat depoyu **public** yapmayı emrediyor. Aynı talimat, yayımlanmamış
manuscript'in "repository public diye otomatik olarak public olmaması"nı da
emrediyor. Üç şık var:

| Şık | Ne demek | Sonuç |
|---|---|---|
| **(a)** | Depo public; **proza depo dışında yaşar** (`.gitignore` + içerik denetimi) | Bestiarium'un D8/D29 kararı. **Bootstrap bunu varsaydı.** |
| (b) | Depo public; proza şifreli/ayrı private submodule'de | Karmaşık; iki depo yönetimi |
| (c) | Depo private; yalnızca yayından sonra public | Talimatın "public repository" emriyle çelişir |

**Bootstrap'ın varsayımı: (a).** Gerekçe Bestiarium'un ölçülmüş gerekçesidir
— üç somut risk: KDP fiyat eşleştirmesi, kamu malı yanlış sınıflandırması,
intihal / AI eğitim verisi. Bu kitapta **dördüncü** bir risk daha var:
metin çocuklara yöneliktir ve bağlamından koparılmış bir sahne alıntısı
(örneğin bir kurban anlatısı) sosyal medyada kitabın aleyhine kullanılabilir.

**Varsayım mekanizmaya bağlandı:** `04_BUILD/validate_structure.py` hem yol
kalıbını hem **içeriği** denetler. Kurucu (b) veya (c) derse mekanizma
değişmez, yalnızca `.gitignore` kuralları değişir.

> ⚠ Bu, "sessiz varsayım" değildir: mekanizma kurulmuştur, karar açıktır ve
> Faz 1 bu karar kapanmadan **başlamaz**.

---

### A2 · 22 kültürün tam listesi

**Durum:** ✅ **KAPANDI → K23.** 22 kültür kilitlendi; yol haritasının altı
geleneğinden ikisi daraltıldı (Polinezya → Māori + Hawai'i, Batı Afrika →
Yoruba + Akan). Aşağıdaki analiz kararın gerekçesi olarak korunur.

Master yol haritası **22** sayısını veriyor ve **altı** kültürü adıyla
sayıyor (BÖLÜM 03 · PROJE 02, "Çözdüğü problem"):

> *"**Kore, İnuit, Polinezya, Batı Afrika, Fars ve Türk** anlatılarını aynı
> ciltte, aynı kalitede sunan bir kitap neredeyse yok."*

Bu altısı **kilitlidir** — kitabın konumlanma iddiasının kanıtıdır.
Kalan 16 slot yol haritasında **tanımlı değildir**.

`01_RESEARCH/culture_index.json` şu anda:
- 6 kültür `status: "locked"`, `source: "master-roadmap"`
- 16+ kültür `status: "candidate"` — **aday listesidir, karar değildir**

`validate_spec.py` kapıyı şöyle tutar: `.gate` `phase1`'e yükseltilebilmesi
için **22 kültürün tamamı `locked`** olmalıdır. Yani bu karar Faz 1'i
kapatmadan verilmek zorundadır ve unutulamaz.

Aday listesinin gerekçeleri `00_CONTEXT/EDITORIAL_ARCHITECTURE.md` § 3'te.

---

### A3 · 45 hikâyenin listesi ve kültür dağılımı

**Durum:** ✅ **KAPANDI → K24 (kısıtlar kapıya bağlandı) ve K25 (45 hikâye
kilitlendi).** Aşağıdaki analiz kararın gerekçesi olarak korunur.

Yol haritası 45 sayısını veriyor, hikâyeleri saymıyor. Faz 1'in birinci işi
budur. Kısıtlar:

- 22 kültür × en az 1 hikâye = en az 22
- 45 − 22 = 23 hikâye kültürler arasında dağıtılacak
- **Eşit dağıtım zorunlu değildir** (talimat § 14: *"Do not force equal
  numbers if the editorial concept does not justify it"*)
- Hiçbir kültür 4'ten fazla hikâye almasın — aksi hâlde "22 kültür" iddiası
  zayıflar ve kitap gizlice bir "5 kültür + ekler" kitabına döner
- Yunan payı **en fazla 3** — kitabın varlık sebebi rafın %80 Yunan olması

Son iki kısıt bu belgenin **önerisidir**, yol haritasının kararı değildir.
`validate_spec.py` bunları uyarı olarak basar; kurucu onaylarsa hataya
çevrilir.

---

### A4 · 22 kültür vinyetinin sayfadaki yeri

**Durum:** ✅ **KAPANDI → K27 · şık (f)** — kültür kartı hikâye kuyruğundaki
boşlukta durur, ek sayfa tüketmez.

> ⚠ **AŞAĞIDAKİ ANALİZ ÖLÇÜMDEN ÖNCEDİR VE ÖNERİSİ ÇÜRÜTÜLMÜŞTÜR.**
> Tarihsel kayıt olarak korunuyor. Bootstrap (a′) şıkkını öneriyordu ve o
> öneri `wordsPerPage ≈ 420` **tahminine** dayanıyordu. Faz 1'in gerçek
> dizgi ölçümü **357,5** verdi; 3 sayfa/hikâye imkânsız çıktı ve (a′) 226
> değil **272 sayfaya** yükseldi — bütün şıkların en kötüsü. Güncel
> gerekçe: **K27** ve `00_CONTEXT/EDITORIAL_ARCHITECTURE.md` § 0.

Yol haritası *"22 kültür vinyeti"* diyor ama yerini söylemiyor. Üç şık —
üçünün de sayfa maliyeti farklıdır ve sayfa modeli bu karara duyarlıdır:

| Şık | Ne | Sayfa maliyeti | Not |
|---|---|---:|---|
| **(a)** | Her kültür için 1 sayfalık "kültür kartı" (vinyet + 3 cümle + harita işareti) | **+22 sayfa** | Ebeveyn/öğretmen için en güçlü; "eğitici" algısını taşır |
| (b) | Vinyet, o kültürün ilk hikâyesinin başlık bloğunda küçük süs | +0 sayfa | En ucuz; vinyet neredeyse görünmez, 22 çizimin değeri kaybolur |
| (c) | Bölüm (part) açılış sayfalarında toplu | +6–8 sayfa | Vinyet sayısı bölüm sayısına eşit olmadığı için 22 vinyeti barındıramaz |

**Bu belgenin önerisi: (a).** Gerekçe ticaridir: yol haritası ek malzemeyi
*"öğretmen ve kütüphaneci için satın alma gerekçesi; **iade oranını
düşürür**"* diye tanımlıyor. Kültür kartı tam olarak o işi yapar ve
22 vinyetin üretim maliyetini görünür kılar.

#### ⚠ Sayfa modelinin bulduğu şey — A4 ile A5 birbirine bağlı

`04_BUILD/page_budget.py` çalıştırıldığında **230 sayfanın mevcut varsayılan
yapıyla ULAŞILAMAZ olduğu** çıktı. Sebep aritmetik değil, **yapısal**:

Her hikâye yeni sayfada başlar ve sayfa sayısı yukarı yuvarlanır. Bu yüzden
hikâye başına maliyet **3 ↔ 4 sayfa arasında zıplar** ve aradaki bütün
toplamlar ulaşılamazdır:

| Ulaşılabilir toplam | Hikâye/sayfa | Gereken kelime/sayfa | Hedeften |
|---:|---:|---|---:|
| 204 | 3 | 380–600 | −26 |
| **250** | 4 | 272–379 | **+20** ← varsayılan model |
| 294 | 5 | 212–271 | +64 |

**Tipografiyi ayarlamak bu boşluğu açmaz.** Yapısal iki seçenek hedefi
tutturuyor:

| Seçenek | Kelime/sayfa | Kültür kartı | Bölüm açılışı | Hikâye/sayfa | Toplam |
|---|---:|---:|---:|---:|---:|
| **(a′)** | ~420 | **2 sayfa** (açık sayfa) | 2 | 3 | **226** (−4) ✓ |
| (b′) | ~280 | **0** (vinyet başlıkta) | 2 | 4 | 228 (−2) ✓ |

**Bu belgenin güncellenmiş önerisi: (a′).** Kültür kartını tek sayfa değil
**açık sayfa (spread)** yapmak, vinyeti + harita işaretini + üç cümleyi
rahat taşır ve hedefi tutturur. (b′) 22 vinyetin görünürlüğünü yok eder ve
yol haritasının illüstrasyon bütçesini gerekçesiz bırakır.

**(a′) 250 yerine 226 sayfa demek**: ciltsiz maliyet 4,00 $ yerine 3,71 $,
telif 6,19 $ yerine 6,48 $ — **kopya başına +0,29 $**.

> Bu tablo bir tahmin değil, modelin çıktısıdır ve `page_budget.py` her
> koşuda yeniden üretir. Ama `wordsPerPage` **hâlâ kalibre değildir**;
> Faz 1 gerçek dizgiyle ölçtükten sonra tablo değişebilir. Karar Faz 1'in
> ölçümünden **sonra** verilir.

**Karar verilmeden Faz 4 (dizgi) başlayamaz.**

---

### A5 · Bölüm (part) mimarisi

**Durum:** ✅ **KAPANDI → K26 · şık (a) bölgesel.** Altı bölge; dağılım
`01_RESEARCH/story_index.json` → `parts[]` içindedir.

45 hikâyeyi düz bir liste hâlinde sunmak 8–12 yaş için yorucudur; okur
nerede olduğunu bilmek ister. İki şık:

| Şık | Ne | Artı | Eksi |
|---|---|---|---|
| **(a)** | **Bölgesel** — "Kuzeyin Buzları", "Büyük Nehirler", "Ada Denizleri"… | Harita ile birebir örtüşür; "dünya" iddiasını görselleştirir | Bölge sınırları tartışmalı olabilir |
| (b) | **Temalı** — "Yaratılış", "Kahramanlar", "Canavarlar", "Hileciler"… | Alt başlıkla ("Gods, Heroes, and Monsters") birebir örtüşür; karşılaştırma yapar | Aynı kültür kitabın dört yerine dağılır; kültür kartı yerleşimi zorlaşır |

**Bu belgenin önerisi: (a) bölgesel**, çünkü A4(a) kültür kartını gerektirir
ve kültür kartı ancak kültürler bir arada durursa işe yarar. Ayrıca dünya
haritası (yol haritasının zorunlu kıldığı tek görsel) bölgesel yapıyla
doğrudan konuşur.

---

### A6 · Büyük punto sürümü v1.0'a girecek mi

**Durum:** AÇIK — **bootstrap'ın varsayımı: HAYIR.**

Yol haritası büyük puntoyu *"uzun vadeli genişleme"* listesine koyuyor,
lansman formatlarına değil. Lansman formatları: **ciltsiz + ciltli +
Kindle** (ciltli lansmanla birlikte).

`04_BUILD/editions.py` büyük punto sürümünü **tanımlı ama devre dışı**
(`enabled: False`) tutar: hattı bozmadan bekletir, kurucu isterse tek satır
değişikliğiyle açılır.

---

### A7 · KDP Select / KU testi

**Durum:** AÇIK — Faz 5 sonrası.

Yol haritası BÖLÜM 08.5: *"İstisna: çocuk kitabı için KU denenebilir —
çocuk kitapları KU'da daha iyi performans gösterir."* Ama BÖLÜM 12'nin
"yapılmayacaklar" listesi de şunu diyor: *"KDP Select'e girmek (çocuk
kitabı hariç, o da test olarak). Münhasırlık ileride kanalları kapatır."*

Yani KU **yasak değil, test**. Karar yayından sonra, ilk 90 günün verisiyle
verilir. Bootstrap bunu bir üretim kararı saymaz.

---

### A8 · İki ebeveyn okuyucusu kim

**Durum:** ✅ **KAPANDI (Faz 7 · 10 Ağustos 2026) → K32.**
Kurucu okumaların **tamamlandığını beyan etti**.

> ⚠ **Kanıtın cinsi kayıtlıdır ve gizlenmemiştir:** elde **kurucu beyanı**
> vardır, imzalı okuyucu kaydı **yoktur**. Okuyucu adı, tarihi, imzası,
> alıntısı ve okuma günlüğü **uydurulmamıştır**
> (`03_EDITORIAL/PARENT_READINGS.md` § 6). Kapı beyanı kabul eder ve
> her koşuda "kanıt kurucu beyanıdır" **uyarısını basar**.

Aşağıdaki gerekçe tarihsel kayıt olarak durur.

Master yol haritası R2'nin (yaş uygunluğu) azaltmasını iki parçalı
yazıyor: *"yazım öncesi `AGE_POLICY.md`; **yayından önce en az iki ebeveyn
okuması**."*

Birinci parça bu bootstrap'ta yapıldı. İkincisi **kurucunun bulacağı iki
gerçek insandır** ve CI ile üretilemez. `04_BUILD/validate_structure.py`
**FAZ 4** kapısında `03_EDITORIAL/PARENT_READINGS.md` dosyasını arar; iki
imzalı okuma kaydı yoksa sürüm çıkmaz.

> ⚠ **Bu cümle Faz 4'e kadar YANLIŞTI ve kapı ÖLÜYDÜ.** Burada "Faz 5"
> yazıyordu, yol haritası § 16 ise kapıyı **Faz 4**'ün CI kapıları arasında
> sayıyor — ve kod ikisini de yapmıyordu: `validate_structure.py` bu dosyayı
> **hiçbir kapıda aramıyordu**. Yol haritası kazandı (§ 1). Kapı Faz 4'te
> yazıldı, `selftest` ile sınandı ve iki gerçek okuyucu bulunana kadar
> **kasıtlı olarak kırmızı** duruyor.

---

### A9 · ISBN

**Durum:** ✅ **KAPANDI (Faz 7 · 10 Ağustos 2026) → K33 — KDP ücretsiz ISBN.**

Kurucu kararı: **Amazon/KDP'nin ücretsiz ISBN'i** kullanılacaktır.
Numara **KDP panelinde atanır**; bu depoda hiçbir dosyada ISBN yoktur ve
uydurulmamıştır. `validate_structure` takip edilen dosyalarda ISBN
biçiminde bir dize ararsa CI **kırmızı yanar** — ve bu kapı ilk koşusunda
teslim belgesindeki maskelenmiş sahte ISBN'i yakaladı.

Numara alındığında **tek yere** yazılır:
`project_config.json` → `founder.isbn.paperback` / `.hardcover`.

Aşağıdaki gerekçe tarihsel kayıt olarak durur.

KDP ücretsiz ISBN verir ama "Publisher" alanı *Independently published*
olur. Kendi ISBN'imiz (TR: Kültür Bakanlığı ISBN Ajansı) yayınevi adını
taşır ve okul/kütüphane kanalında anlamlıdır — bu kitap tam olarak o
kanala girmeyi hedefliyor.

Karar Faz 5'te verilir; her iki hâlde de üretim dosyaları aynıdır.

---

### A10 · Yayıncı / imprint adı

**Durum:** ✅ **KAPANDI (Faz 7 · 10 Ağustos 2026) → K34 — Vâliçe Press.**

Faz 6 bu adı projede **arayıp bulamamış** ve hiçbir ad uydurmamıştı;
kapağa yayıncı satırı basılmamıştı. Kurucu adı verdi: **Vâliçe Press**.

Ad artık `project_config.json` § `founder.publisher` içindedir, arka
kapak panelinde basılıdır ve metadata'da kayıtlıdır. KDP'de *Publisher*
alanına birebir bu ad girilir.

---

### A11 · Kapak sanatının etkin çözünürlüğü kabul edilecek mi

**Durum:** **AÇIK** — ölçüldü, karar kurucunun.

Kapak sanatı bir görsel üreticiden geldi ve o üreticinin azami çıktısı
**1536 pikseldir**. 12,8 inçlik sarım kapağı 300 dpi'de üretmek o
boyuttan **mümkün değildir**:

| | Ham sanat | Üretim tuvali | Etkin |
|---|---:|---:|---:|
| Ciltsiz | 1478 × 1064 px | 3851 × 2775 px | **115 dpi** |
| Ciltli | 1465 × 1073 px | 4100 × 3006 px | **107 dpi** |

⚠ **Yeniden üretilen sanat bu sayıyı DEĞİŞTİRMEDİ** — üreticinin azami
çıktısı hâlâ ~1536 pikseldir. Ama **kırpma kaybı neredeyse sıfıra indi**
(ciltli %4,38 → %0,10) çünkü yeni sanat hedef orana çok daha yakın
üretildi. Kompozisyon artık kırpılmıyor.

Faz 6 bu oranı **hiç ölçmemişti**; çıktıyı 300 dpi etiketliyordu ve
büyütmeyi görmüyordu. Faz 7 kapıyı ekledi (uyarı seviyesinde — sayı ham
sanattan gelir, hattın kusuru değildir).

**Seçenekler:** (A) kabul et — baskıda kapak bir miktar yumuşak görünür;
(B) daha yüksek çözünürlüklü kapak sanatı sağla — `covers.py` tek
komutla yeniden üretir, tipografi aynen korunur.

**Karar prova kopyası görülmeden verilmemelidir.**

---

## ALINMIŞ KARARLAR

### Faz 7 — 10 Ağustos 2026

#### K32 · H8 kurucu beyanıyla kapandı

İki ebeveyn okuması **kurucu tarafından tamamlanmış** ilan edildi.
Kapı iki kanıt cinsini ayrı tutar: imzalı okuyucu kaydı (en güçlü) ve
kurucu beyanı (kabul edilir, ama **cinsi raporlanır**). Ajan bu kapıyı
kendi kararıyla açamaz — bayrak `project_config.json`'dadır.
**Hiçbir sahte kanıt üretilmedi.**

#### K33 · ISBN — KDP ücretsiz ISBN

Gerekçe: kurucu kararı. Numara panelde atanır; depoda ISBN biçimi
**yasaktır** ve kapıya bağlanmıştır.

#### K34 · Yayıncı — Vâliçe Press

Gerekçe: kurucu kararı. Tek kaynak `project_config.json § founder`.

#### K35 · Okura giden dizeler betiklere GÖMÜLEMEZ

Faz 6'da yazar adı `covers.py`, `epub.py` ve `handoff.py` içinde ayrı
ayrı gömülüydü; `metadata.py` ise yer tutucu basıyordu. **Kapak ile
metadata farklı yazar taşıyordu ve hiçbir kapı görmüyordu.**

Kural: yazar ve yayıncı yalnızca `project_config.json § founder` içinde
yazılır. `validate_structure.check_founder_strings_not_hardcoded`
betikleri tarar (yorumlar muaf — kusurun tarihi anlatılabilmelidir) ve
`selftest` bunu kasıtlı kusurla sınar.

Bu, Bestiarium D17'nin (aynı kuralı iki dosyada tutmak) aynı sınıfıdır.

#### K37 · Kapak sanatı METİNSİZ yeniden üretildi — silme hattı kaldırıldı

**Kurucu kararı · 10 Ağustos 2026.**

İlk kapak sanatına üreten model **yanlış bir başlık** (*"STORIES from the
WHOLE WORLD"*) ve **uydurulmuş bir ISBN barkodu** basmıştı. Hat bunları
harf maskesi + difüzyon + çok ölçekli gök modeliyle **siliyordu**.

Teknik olarak çalışıyordu. Ama yanlış işti: **bir üreticinin yaptığı resmi
başka bir algoritmayla onarmak sanata zarar verir** ve her koşuda biraz
daha bozar. Ciltli kapakta gün batımı ve bulutlar bu yüzden düzleşmişti.

Kurucu bütün kapak sanatını **metinsiz yeniden ürettirdi**.

| | |
|---|---|
| Yetkili sanat | `07_ASSETS/raw/re-generated/` · SALT OKUNUR |
| Devre dışı | `07_ASSETS/raw/superseded/20260810-cover-regeneration/` |
| Silme hattı | `covers.py`den **tamamen kaldırıldı** (~130 satır) |

**Yeni kural:** sanat katmanına hiçbir şey yazılmaz ve sanat katmanından
hiçbir şey silinmez. Okunabilirlik metnin **kendi zeminiyle** sağlanır ve
kontrast **WCAG ile ölçülür** (`covers.measure_contrast`), göze bırakılmaz.

**Üç kapı bunu koruyor** (`cover_artwork.py`, hepsi kasıtlı kusurla sınandı):

1. **sha256** — masterlar değişirse kırmızı
2. **köken** — `covers.py` yetkili dizinden okumazsa kırmızı
3. **yasak fonksiyon** — silme hattının ADI bile geri gelirse kırmızı

⚠ **Makine, bir görselde tipografi olup olmadığını KANITLAYAMAZ.** Denendi
ve dürüstçe başarısız oldu: kontrast-bandı imzası, yer gerçeğiyle
sınandığında metinli ve metinsiz sanatı ayıramadı (temiz `back-panel`,
metinli `thumbnail-test`ten yüksek skor aldı). Ayırt edemeyen kapı ÖLÜ
KURALDIR; konulmadı. Metinsizlik **gözle** doğrulandı ve her master için
tek tek kaydedildi (`cover_artwork.VISUAL_VERDICT`).

#### K36 · Ölçülen kutu, planlanan kutu değildir

Faz 6 kapağında yaş rozeti **14 punto ile ölçülüp 27 punto ile
çizilmişti** (reportlab'da font bir DURUMDUR ve araya giren `setFont`
taşınır). Rozet güvenli alandan 54 pt, ciltsizde **kâğıdın kenarından
27 pt** taşıyordu — yani "AGES 8–12" baskıda kesilecekti.

Güvenli alan kapısı bunu **göremedi** çünkü `boxes` listesindeki
**planlanan** kutuyu ölçüyordu.

Kural: çizim ve ölçüm ayrılamaz. `covers.Pen` sınıfı her `drawString`
çağrısında aynı fontla ölçer ve **gerçek** kutuyu (ascent/descent)
kaydeder; kapı o kaydı denetler. Ayrıca **sayfa sınırı** ayrı bir kapıdır:
güvenli alan "kesilir mi" diye sorar, sayfa sınırı "kâğıtta mı" diye.

### Bootstrap (Faz 0) — 8 Ağustos 2026

| # | Karar | Gerekçe |
|---|---|---|
| **K1** | **Beş faz.** Faz 1 Temel · Faz 2–4 Yazım · Faz 5 Üretim | Talimat 4–6 faz istiyor ve 5'i tercih ediyor. Bestiarium altı faz kullandı ama onun kapsamı 112 madde ve 120 plaka; bu kitap 45 hikâye. Beş faz her fazı bir sürüm etiketi hak edecek büyüklükte tutuyor. |
| **K2** | **Yazım üç faza dağıtıldı**: 1 + 15 + 15 + 14 | Talimat § 13 açıkça yasaklıyor: *"Phase 1 = research only, Phase 2 = research only, Phase 3 = all writing."* Her yazım fazı ölçülebilir bir manuscript parçası üretir ve kendi etiketini alır. |
| **K3** | **Faz 1 tam olarak BİR hikâye yazar** (ses kalibrasyon pilotu) | İki gerekçe. ① `CHILDREN_WRITING_STYLE.md`'nin ses kalibrasyon örnekleri **gerçek metinden** gelmek zorundadır; bu kitabın devralacağı bir çocuk sesi yok (yetişkin cildi bilinçli tersidir). ② Bestiarium D36: dolguyla ölçmek "modeli modele karşı sınamaktır"; sayfa bütçesi gerçek prozayla kalibre edilmeli. Bir hikâye ikisini de çözer ve Faz 1'i "yalnızca araştırma" olmaktan çıkarır. |
| **K4** | **İllüstrasyon hattı ZORUNLU** | Yol haritası illüstrasyonu maliyet gerekçesiyle karara bağlamış: 45 + 22 + 1 harita = **68 görsel**, siyah-beyaz. Bu bir öneri değil, fiyat modelinin dayanağı. → `ILLUSTRATION_PIPELINE = REQUIRED` |
| **K5** | **Ham girdi PNG, üretim çıktısı türetilir** | Kurucu görselleri GPT Image ile üretecek ve çıktı PNG olacak. Hat `07_ASSETS/raw/` → `07_ASSETS/processed/{print,kindle,web}/`. **Ham dosya asla üzerine yazılmaz.** |
| **K6** | **Büyük punto v1.0'a girmez** (A6) | Yol haritası onu uzun vadeli genişlemeye koyuyor. `editions.py`'de tanımlı ama `enabled=False`. |
| **K7** | **Kalite kapıları standart kütüphaneyle yazıldı** | Bestiarium D4. CI'ın ana doğrulama işi kuruluma bağlı olmadan saniyeler içinde koşar. Ağır bağımlılıklar (Pillow, reportlab) yalnızca görsel ve dizgi işlerinde. |
| **K8** | **Kapılar kümülatif, `.gate` dosyasıyla yönetiliyor** | Bestiarium D5. Kalite geriye gidemez; açılan kapı kapanamaz. |
| **K9** | **Metin kapıları metin yokken 0 döner — ama `selftest` körlüğü kapatır** | Bestiarium D6 + en değerli mekanizma. Metin yokken yeşil kalan bir hat, kusur geldiğinde de yeşil kalabilir. `05_TESTS/selftest.py` kasıtlı kusurlu bir kurgu kitap çalıştırır ve her kapının o kusuru **yakaladığını** kanıtlar. |
| **K10** | **Yaş kapısı (`qa_age.py`) birinci sınıf bir kapıdır** | Yol haritasının R2 azaltması. Bestiarium'da böyle bir kapı yok çünkü ihtiyacı yoktu. Bu projede en önemli metin kapısıdır. |
| **K11** | **Okunabilirlik kapısı (`qa_readability.py`) eklendi** | Bestiarium'da yok. 8–12 yaş bir *ölçülebilir* okuma seviyesidir; "sıcak ve hızlı" bir üslup iddiası ölçülmeden doğrulanamaz. |
| **K12** | **`qa_diacritics` Bestiarium'dan devralınıyor ama D32 ve D35 kusurlarıyla birlikte** | Bestiarium iki kez yanlış pozitif üretti: `re.I` taraması "long" kelimesini `Lóng`un düşürülmüş hâli sandı (D32); iki ayrı maddenin adı `Lámia`/`Lamia` olduğunda doğru yazımı reddetti (D35). İkisi de baştan düzeltilmiş hâliyle geldi. |
| **K13** | **`qa_echo` kaynak notunu muaf tutar** | Bestiarium D34. Aynı başvuru eseri onlarca hikâyede anılır ve künye biçimi tutarlı olmak **zorundadır**. Ama bu kitapta ikinci bir muafiyet daha var: **kültürel not** kısa ve kalıplı olabilir. Muafiyet KAPSAMLIDIR ama kültürel notun kendi içinde kalıplaşmasını `qa_age`/`qa_voice` ayrıca arar (Bestiarium'un "yaşayan gelenek kapısı boilerplate'e döndü" kusuru). |
| **K14** | **Ölü kural avı bir kapıdır** | Bestiarium D28: `LIVING_TRADITIONS` listesindeki iki kimlik hiçbir geleneğe denk gelmiyordu — kapı o gelenekleri **hiç denetlemedi** ve hiçbir yerde hata görünmedi. Bu projede her kimlik listesi (`LIVING_TRADITIONS`, kültür referansları, hikâye referansları) gerçek bir kayda denk gelmek zorunda; `validate_spec.py` denetler. |
| **K15** | **Üretilen belgeler bayatlık kapısına bağlı** | Bestiarium'un `update_docs.py --check` mekanizması. *"Her faz sonunda güncelle, asla unutma"* bir disiplin talebidir ve disiplin unutulur. Mekanizma unutmaz. |
| **K16** | **Görsel prompt kütüphanesi ÜRETİLİR, elle yazılmaz** | Bestiarium D7. Üslup gövdesi tek yerde durur; değişirse 68 prompt birlikte değişir. "Tek çizgi dili" şartı ancak böyle tutulabilir. |
| **K17** | **Depo `main` dalında, faz dalları `faz/**`** | Talimat § 9. Her faz: iş → yerel QA → commit → push → CI → YEŞİL → etiket → sonraki faz. CI kırmızıyken ilerleme yok. |
| **K18** | **Bestiarium'un `06_REPORTS/*.json` `.gitignore` kuralı DÜZELTİLEREK devralındı** | Bestiarium'da `06_REPORTS/*.json` tümüyle yok sayılıyor, ama `plates.yml` "kayıtlı raporu denetle" adımında `06_REPORTS/plate-consistency.json` arıyor — dosya depoda hiç bulunmadığı için o adım CI'da **her zaman** boş geçiyor. Sessiz bir ölü kural. Burada karar: **denetlenen rapor depoda durur** (`06_REPORTS/tracked/`), koşuya özgü çıktı yok sayılır. |
| **K19** | **`.gate` seviyeleri**: `phase0` → `phase1` → `phase2` → `phase3` → `phase4` → `phase5` → `release` | Talimat § 22. Tek aktif faz; CI kapıyı okur; atlama ve geri gitme engellenir. |
| **K20** | **Kültürel kısıtlılık taraması her hikâye için ZORUNLU**, yalnızca "yaşayan gelenek" listesindekiler için değil | Bestiarium'da tarama yalnızca `LIVING_TRADITIONS` için zorunluydu ve liste hatalıydı (D28) — en hassas etik notu taşıyan madde kapının **dışında** kaldı. Bu kitapta 22 kültürün neredeyse tamamı yaşayan gelenektir; muafiyet listesi tutmaktansa taramayı evrensel yapmak hem daha ucuz hem daha güvenlidir. |

---

### Faz 1 — 8 Ağustos 2026

| # | Karar | Gerekçe |
|---|---|---|
| **K21** | **A1 kapandı: şık (a).** Depo public kalır; yayımlanmamış proza depo **dışında** yaşar (`02_MANUSCRIPT/`, `.gitignore` § ①). | Kurucu kararı. Mekanizma bootstrap'ta zaten kurulmuş ve **kasıtlı bir sızıntı testiyle** sınanmıştı; karar onu onaylar. Dört risk: KDP fiyat eşleştirmesi · kamu malı yanlış sınıflandırması · intihal / AI eğitim verisi · **ve bu kitaba özgü dördüncü risk**: metin çocuklara yöneliktir ve bağlamından koparılmış bir sahne alıntısı sosyal medyada kitabın aleyhine kullanılabilir. Yol haritası § 21 H1 bunu Faz 1'in **giriş** kapısı sayar; iş başlamadan soruldu. |
| **K22** | **`AGE_POLICY.md` kurucu onaylı.** On yedi kategorinin tamamı yazıldığı seviyelerde kilitlendi. | Yol haritası § 21 H2 ve DoD ölçüt 20: onay Faz 1 yazımından **önce** gerekiyordu ve pilot hikâye yazılmadan alındı. Politika artık `qa_age.py` eşikleriyle ve `selftest.py` kurgusuyla birlikte değişir — beş adımın hepsi yapılmadan seviye değiştirilemez (`AGE_POLICY.md` § 6). |
| **K23** | **A2 kapandı: 22 kültür kilitlendi.** Yol haritasının altı geleneğinden **ikisi daraltıldı**: Polinezya → **Māori + Hawai'i**, Batı Afrika → **Yoruba + Akan**. Bu sekiz kayıt + araştırmayla seçilen 14 kayıt = 22. | İki gerekçe. ① *Polinezya bir kültür değil bir kültür ailesidir*; Māori ve Hawai'i anlatıları aynı adları (Māui) taşısa da aynı hikâyeler değildir ve tek kayıtta birleştirmek ikisini de yanlış temsil eder. ② *"Batı Afrika" bir kültür adı değildir* ve `CHILDREN_WRITING_STYLE.md` § 7 tam olarak bu genellemeyi yasaklar: "Afrikalılar…" değil, "Yoruba anlatıcıları…". Daraltma altı geleneğin hepsini **korur**; `project_config.roadmapTraditions` örtüşmeyi makine okunur tutar ve `validate_spec.py` her geleneğin kilitli bir kültürle karşılandığını **ayrıca** denetler — yani daraltma bir kaçış yolu değil, **ek bir kapıdır**. |
| **K24** | **A3 kısıtları kapıya bağlandı: "kültür başına ≤4 hikâye" ve "Yunan ≤3" artık UYARI DEĞİL HATADIR.** | Kurucu kararı. Bu iki kural kitabın **editoryal tezinin ta kendisidir**: raf %80 Yunan olduğu için bu kitap var. Bir tezi uyarı seviyesinde tutmak onu unutulabilir kılar; kapıya bağlamak mekanizmaya bağlar (`project_config.scope.distributionCapsAreErrors = true`). |
| **K25** | **A3 kapandı: 45 hikâye kilitlendi**, 14 aday havuzuyla (toplam 59 kayıt). Dağılım: 3 kültür × 3 hikâye, 17 × 2, 2 × 1. | Her kilitli kültürün en az bir hikâyesi var; hiçbiri 4'ü aşmıyor; Yunan tam 3. Kelime bütçesi 45 × 950 = **42.750** ve yol haritasının 43.000 hedefinden %0,6 sapıyor. Aday havuzu SOURCING_STANDARD § 9'un zorunlu kıldığı yedektir: hiçbir aday kaynağı olmadan listeye alınmadı. |
| **K27** | **A4 kapandı: kültür kartı HİKÂYE KUYRUĞUNDAKİ BOŞLUKTA durur — şık (f).** 22 kartın hepsi vardır; hiçbiri **ek sayfa tüketmez**. Kitap **228 sayfa**, hedeften %0,9 sapma, ciltsiz telif **6,46 $**. | **Bu karar bir tercih değil, bir ÖLÇÜMÜN SONUCUDUR ve bootstrap'ın kendi önerisini çürütmüştür.** `calibrate_pages.py` pilot hikâyenin gerçek prozasını gerçek metin bloğuna gerçek yazı karakteri metrikleriyle dizdi: **357,5 kelime/sayfa** (tahmin 361,1 — %1,0 sapma). Tipografi tahmini iyiydi; asıl sürpriz **yazı karakteri seçiminin kelime/sayfa'yı %21 oynatmasıydı** (DejaVu 282,8 · Times/Liberation 357,5). Bootstrap (a′) şıkkını öneriyordu — kart açık sayfa, 3 sayfa/hikâye, 226 sayfa — ama o öneri `wpp ≈ 420` varsayımına dayanıyordu. Ölçüm 357,5 verdi; 3 sayfa/hikâye için ≥380 gerekiyor ve **12 pt bir yaş kararıdır**, küçültülemez. Yani 4 sayfa/hikâye kilitlidir ve (a′) 226 değil **272 sayfaya** çıkar: bütün şıkların **en kötüsü**. Ölçüm aynı anda çözümü de buldu: her hikâye 3,219 sayfa içerik taşıyıp **4 sayfa faturalanıyor** → 0,781 sayfa (25 satır) **zaten ödeniyor**, 45 hikâyede 35 sayfa. Kültürel not düşülünce kalan ~21 satıra kültür kartı (~15 satır) **sığar**. (f), hem hedefi tutturan hem 22 vinyeti görünür bırakan **tek** şıktır; bedeli Faz 5'in dizgi zorluğudur. |
| **K26** | **A5 kapandı: bölüm mimarisi BÖLGESELDİR** — altı bölge, 45 hikâye ve 22 kültür bu bölgelere dağıtıldı. | `DECISIONS.md` § A5'in önerisi doğrulandı. Bölgesel yapı yol haritasının **zorunlu kıldığı tek görselle** (dünya haritası) birebir konuşur ve kültür kartını mümkün kılar: kart ancak kültürler bir arada dururken işe yarar. Temalı yapı ("Yaratılış / Kahramanlar / Canavarlar") aynı kültürü kitabın dört yerine dağıtır ve kültür kartı yerleşimini imkânsızlaştırır. |

> **Faz 1'de düzeltilen üç ölü kural.** Bunlar karar değil **kusur** kayıtlarıdır
> ve K14'ün ("ölü kural avı bir kapıdır") gereğidir:
>
> 1. **DoD ölçüt 7 çalışmıyordu.** `validate_spec.py` kültür aday havuzunu
>    (≥26) yalnızca `phase0` dalında denetliyordu; kapı `phase1`'e yükseldiği
>    an denetim **kayboluyordu** — tam da yedek payının anlam kazandığı
>    noktada. Denetim her kapıya taşındı.
> 2. **`story_index.schema.json` ≥55 aday havuzunu İMKÂNSIZ kılıyordu.**
>    `number` alanı zorunlu tamsayıydı ve tavanı 45'ti; 46. kayıt şemayı
>    ihlal ediyordu. Yani şema, SOURCING_STANDARD § 9'un **zorunlu kıldığı**
>    şeyi yasaklıyordu. Alan aday kayıtlar için `null` kabul eder hâle geldi.
> 3. **`make_prompts.py` var olmayan bir alanı okuyordu.** `story.imagePrompt`
>    şemada tanımlı değil ve şema `additionalProperties: false` taşıyor —
>    o dal hiçbir koşulda çalışamazdı, sessizce başlığa düşüyordu. Konu artık
>    kilitli olay örgüsünün **dönüm** anından türetiliyor.
>
> Üçü de "hiçbir yerde hata görünmediği için doğru sanılan" sınıftandır —
> Bestiarium D28'in aynı ailesi.

---

### Faz 3 — 9 Ağustos 2026

| # | Karar | Gerekçe |
|---|---|---|
| **K28** | **Kitap tek kesme karakteri kullanır: `’` (U+2019)** — İngilizce iyelikte de, ortografik kesmede de (`Chang’e`, `K’iche’`, `Q’ukumatz`, `Man’yōshū`). Okura giden dizeler artık `qa_diacritics` kapısındadır. | `CHILDREN_WRITING_STYLE.md` § 6 düz `'` işaretini **yasaklar** ve § 5 her adın "kitabın seçtiği tek biçimde" yazılmasını şart koşar. `qa_voice` o kuralı uyguluyordu ama **yalnızca manuscript'e**; oysa okura giden dizelerin bir kısmı dizinde durur (başlık, telaffuz adı, "kim kimdir" rolü, kültür bölgesi) ve **hiçbir kapının kapsamında değildi**. Faz 3 taraması 33 kusur buldu, biri kendi içinde tutarsızdı: *"K’iche' is spoken by…"* — aynı adın iki karakteri, tek cümlede. Elle tutulamayan bir sınıf, kapıya bağlandı. **Kurucuya açık alternatif:** Maya dillerinde gırtlaksı durak dilbilimsel olarak bir **harftir** ve Unicode onun için U+02BC'yi önerir (`Kʼicheʼ`). Bu karar tipografik tutarlılığı ortografik saflığa tercih etti; `mythbook._WORD` her iki karakteri de harf sayar, yani karar tek yerde geri alınabilir. **Kaynak künyeleri taramanın DIŞINDADIR** — kaynağın kendi yazımını düzeltmek alıntıyı bozar. |
| **K29** | **Faz 3 sınırı SAYIYA göre çizilir, bölgeye göre değil: tam 15 hikâye, kümülatif 31/45.** Üçüncü bölge tamamlanır (10/10), dördüncü bölge **açılır** (5/8); kalan 3 hikâye Faz 4'e devreder. | Yol haritası § 16 Faz 3'ün **işini** "üçüncü ve dördüncü bölge" diye tarif eder, ama **hedefini** iki ayrı yerde sayıyla verir: § 12 dağılım tablosu ve § 16 "Hedef" satırı — ikisi de **15 hikâye · kümülatif 31**. Yazılmamış 3. + 4. bölge 18 hikâye taşır (+ 2. bölgeden devreden #16 = 19), yani iki okuma çelişir. Kazanan sayıdır, üç gerekçeyle: ① kümülatif hedef **DoD ölçütüdür** ("kümülatif hikâye hedefi tam olarak tutuyor"), bölge tarifi değildir; ② `project_config.phases` sayıyı makine okunur tutar ve `validate_spec` onu kapı yapar; ③ **Faz 2 aynı çelişkiyi aynı yönde çözdü** — #16 bölge sırasında olmasına rağmen ertelendi ki kümülatif dizi bozulmasın. Aritmetik birebir kapanıyor: Faz 4 = kalan 3 (4. bölge) + 5. bölge (7) + 6. bölge (4) = **14**, yani yol haritasının Faz 4 hedefi. Bölge tarifini kazandıran okuma Faz 3'ü 34'e, Faz 4'ü 11'e taşır ve **iki fazın da sayısal hedefini birden kırar**. |

> **Faz 3'te düzeltilen dört kusur — hepsi "doğru metni reddeden cetvel" sınıfı.**
> Üçü **tek bir hikâye yazılmadan önce**, ölçekten değil **ön denetimden**
> çıktı: Faz 3'ün ilk işi yazmak değil, kapıları hikâyelerin gerçek adlarına
> karşı sınamaktı.
>
> 1. **`mythbook._WORD` birleşen işaretleri sözcük karakteri saymıyordu**
>    (U+0300–U+036F). Yorubaca ton işareti taban harfin üstüne **ayrı bir kod
>    noktası** olarak biner ve `ẹ̀`/`ọ̀` için önceden birleştirilmiş kod noktası
>    Unicode'da **yoktur**. Sonuç: `Ọ̀ṣun` → `['Ọ', 'ṣun']`, `Ilé-Ifẹ̀` →
>    `['Ilé-Ifẹ']`. Yani sözcük sayısı şişiyor, `proper_names()` var olmayan
>    adlar üretiyor ve `qa_crossref` **doğru yazılmış** adı "telaffuz
>    rehberinde eksik" sanıyordu. Aynı sınıf ʻokinayı da vuruyordu (`Hiʻiaka`
>    → `['Hi', 'iaka']`) — oysa ʻokina Hawaiʻicede noktalama değil **harftir**.
>    En can alıcı yanı: `CHILDREN_WRITING_STYLE.md` § 5 korunacak diakritiklere
>    örnek olarak **tam da `Ọ̀ṣun` ve `Māui` adlarını** verir. Cetvel, üslup
>    belgesinin adıyla saydığı yazımları ölçemiyordu.
> 2. **`qa_crossref` künye adını metinden farklı tokenize ediyordu.** Künye
>    kesme işaretinden bölünüyor (`Chang’e` → `{Chang, e}`), metin
>    bölünmüyordu (`Chang’e` tek belirteç) — eşleşme imkânsızdı. Kapı,
>    kesmeyi **ortografik** kullanan dilleri (Maya dilleri, pinyin, Hepburn)
>    toptan cezalandırıyordu. Faz 2'nin iyelik eki düzeltmesiyle aynı sebep:
>    **iki ayrı tokenizer**. Tek doğruluk kaynağına bağlandı
>    (`mythbook.declared_tokens`).
> 3. **Okura giden dizelerde tipografi hiç denetlenmiyordu** → K28.
> 4. **Yaş incelemesi kapısı "kuyrukta" ile "incelendi"yi ayırt edemiyordu.**
>    `qa_age`, `REVIEW` kategorili yazılmış bir hikâye için yalnızca kimliğin
>    `AGE_REVIEW_LOG.md` içinde **bir yerde geçtiğini** arıyordu — ve defterin
>    "Faz 2+ için bekleyen kuyruk" tablosu bu şartı zaten sağlıyor. Yani bir
>    hikâye **hiç incelenmeden**, yalnızca kuyrukta durduğu için kapıdan
>    geçebilirdi. Faz 2'de kusur **tetiklenmedi** (yazılan 15 hikâyenin
>    hiçbiri `REVIEW` kategorisi taşımıyordu) ama Faz 3'ün 15 hikâyesinin
>    **altısı** taşıyor. Kapı, kuyruk kaydını değil **sonuç kaydını** arar
>    hâle getirildi (`<!-- AGE-REVIEW:RECORDED -->` çıpası) ve `selftest` iki
>    yönlü sınıyor: kuyruk tek başına **yetmemeli**, sonuç kaydı **yetmeli**.
>    Faz 2'nin 15 hikâyesi de geriye dönük olarak deftere işlendi.

### Faz 4 — 9 Ağustos 2026

| # | Karar | Gerekçe |
|---|---|---|
| **K30** | **A4/K27 YENİDEN KARARA BAĞLANDI · şık (iii).** Beş kültürün kartı **kendi sayfasını alır**: `greek`, `norse`, `korean`, `hindu`, `japanese`. Kalan 17 kültür K27'de kalır — kartları hikâye kuyruğundaki ödenmiş boşlukta durur. Model **232 sayfa**, ciltsiz telif **6,41 $** (hedeften −0,02 $/kopya). | **K27 bir varsayıma dayanıyordu ve 45/45 ölçümü onu beş kültürde çürüttü.** K27 kart için "vinyet 10 + üç cümle ≈ 3 + harita 2 ≈ 15 satır" hesaplıyordu; gerçek kart metniyle ölçülünce **20–21 satır** çıktı, çünkü üç cümle 3 değil **6–8 satır** tutuyor. Kuyruk boşluğu ayrıca **hikâye uzunluğuna bağlıdır** ve K27 ortalama hikâyeyi varsaymıştı. **Greek'te başka çıkış yoktu:** `greek-persephone` kitabın en uzun hikâyesidir (1030 kelime) ve kuyrukta **9 satır** bırakır — vinyetin kendisi 10 satır, yani kart metnini **sıfıra indirmek bile yetmiyordu**. Kurucuya dört şık ölçülmüş bedelleriyle sunuldu: (i) metni kısaltmak — Greek için **imkânsız**; (ii) vinyeti 10→6 satıra indirmek — 5'in 4'ünü çözer, Greek'i çözmez ve K27'nin (b′)'yi reddetme gerekçesini (22 vinyetin görünürlüğü) geri getirir; (iii) ayrı sayfa — 5/5 çözer, **−0,072 $/kopya**; (iv) hikâye sırasını değiştirmek — 5'in 3'ünü çözer ve ses kalibrasyon pilotunu (`korean-dangun`) Kore bölümünün başından alır. **Kurucu (iii)'ü seçti**: hikâye sırası ve 22 vinyetin görünürlüğü korunur, bedel ölçülmüş ve kabul edilmiştir. Kararın kaynağı `culture_index.json` → `cardOwnPage`; `page_budget.py` sayıyı oradan okur, iki yerde tutulmaz. |

> **Faz 4'te düzeltilen iki ÖLÜ KURAL.** Her ikisi de Bestiarium'un Ö-sınıfı:
> kural vardı, denetim vardı, ve denetim **hiçbir şey demiyordu**.
>
> 1. **`factualClaims` üç faz boyunca boş koştu.** Faz 1 DoD ölçüt 18 "her
>    olgusal iddia bir kaynağa bağlı" der ve `validate_spec` bunu denetler —
>    ama kitaptaki 45 hikâyenin **45'inde de liste boştu**, yani döngü boş
>    listede dönüyor ve kapı yeşil yanıyordu. Faz 4'ün düşman olgu denetimi
>    12 hikâyeye 27 iddia kaydetti ve `validate_spec` artık **mekanizmanın
>    canlılığını** da sınıyor.
> 2. **`PARENT_READINGS.md` kapısı hiç yazılmamıştı.** Yol haritası § 16 onu
>    Faz 4 CI kapısı olarak adıyla sayıyor; bu belgenin § A8'i ise "Faz 5
>    kapısında aranır" diyordu. **Kod hiçbir kapıda aramıyordu** — R2'nin
>    (yaş uygunluğu, projenin tanımlayıcı riski) insan yarısı mekanizmasızdı.
>    Yol haritası kazandı (§ 1): kapı **phase4**'e yazıldı ve § A8 düzeltildi.
>    Kapı **kasıtlı olarak kırmızıdır** ve iki gerçek okuyucu bulunana kadar
>    öyle kalır.

### Faz 5 — 9 Ağustos 2026

| # | Karar | Gerekçe |
|---|---|---|
| **K31** | **YÜRÜTME YAPISI ALTI FAZA AYRILDI.** Yol haritasının **Faz 5**'i ("Üretim · Dizgi, KDP Dosyaları ve Lansman") ikiye bölünür: **Faz 5 = üretim hazırlığı** (varlık işleme · iç blok dizgisi · prova · doğrulama · metadata hazırlığı · kapak ve A+ prompt şartnamesi) ve **Faz 6 = nihai KDP paketleme** (kapak üretimi ve tipografisi · sırt hesabı · taşma/sarım · nihai Kindle paketi · nihai KDP doğrulaması · ticari çıktı). Yol haritasının Faz 5 **kapsamı değişmedi**; yalnızca **iki teslimata** bölündü. `v1.0.0` etiketi ve `release` kapısı **Faz 6'ya** aittir. | **Kurucu kararı.** Gerekçe ölçülmüştür: Faz 5'in girdisi (68 ham görsel) ile çıktısı (basıma hazır kapak) arasında **kurucu bağımlılığı** vardır — kapak sanat yönü onayı (H9), ISBN (A9) ve iki ebeveyn okuması (H8) çözülmeden nihai paket üretilemez, ama **iç blok, EPUB, metadata ve prompt şartnamesi onlar olmadan da üretilebilir ve doğrulanabilir**. Tek fazda tutmak, tamamlanabilir işi tamamlanamaz işe bağlar ve fazın hiç kapanmamasına yol açar. Bölme, yol haritasının § 22 sürüm stratejisini **bozmaz**: `v1.0.0` hâlâ "yayına hazır KDP dosyaları" demektir, yalnızca Faz 6'da çıkar. Yol haritası § 16'nın Faz 5 tanımı **silinmedi** — bu satır onu iki teslimata böler ve tarihçe § 16'da durur. |

> **Faz 5'te düzeltilen üç ÖLÜ KURAL ve iki sessiz kusur.** Dördü de yalnızca
> GERÇEK TESLİMAT geldiğinde görünür oldu; üç faz boyunca yeşil yandılar.
>
> 1. **Eksik görsel koşulsuz geçiyordu.** `convert_images.py`
>    `r.ok(f"{len(have)}/68 görsel geldi", f"eksik: {len(want-have)}")` yazıyordu.
>    `Result.ok()` **her zaman geçer** — ikinci argüman bir eşik değil, bir
>    metindir. 40 görsel eksik olsa da kapı yeşildi. 45+22+1=68 fiyat modelinin
>    dayanağıdır (K4) ve artık `r.add` ile kapıya bağlıdır.
> 2. **Kindle dosya bütçesi yalnızca görsel YOKKEN denetleniyordu.** 3,0 MB
>    kontrolü `calibrate()` içindeydi ve `calibrate()` yalnızca ham görsel
>    bulunmadığında koşuyordu — yani bütçe, sınanması gereken **tek anda**
>    hiç sınanmıyordu. Kural canlandırıldığı gün ilk koşusunda **10,71 MB**
>    ölçtü (bütçe 3,0 MB): kopya başına **0,41 $ telif kaybı**, düzeltilmeden
>    yayınlanacaktı.
> 3. **`resize(target)` oranı KORUMUYORDU** ama üstündeki yorum "kesin oranı
>    koru" diyordu. Şartnameye uyan girdide fark yoktur (2400×1600 → 3000×2000,
>    ikisi de 3:2), bu yüzden kusur görünmedi. Gerçek teslimat 1024×1536 geldi
>    ve aynı satır onu 3000×2000'e **esnetecekti**: 45 hikâye açılışının
>    tamamı yatay olarak %120 genişleyecekti.
> 4. **Gömülü olmayan font, tek harf çizilmeden PDF'e giriyordu.** reportlab
>    her sayfanın açılış durumunu Helvetica ile yazar; Helvetica base-14'tür
>    ve **gömülmez**. `pdffonts` onu listeliyordu ve KDP'nin "gömülü olmayan
>    font: 0" şartı, hiçbir Helvetica metni olmadan düşüyordu.
>    Çözüm sayfa başında `setFont` değil — açılış durumu ondan **önce**
>    yazılıyor — `Canvas(initialFontName=…)`.
> 5. **Boş son sayfa PDF'e yazılmıyordu.** İç sayaç 236 derken PDF 235 sayfa
>    çıkıyordu ve tek/çift denetimi **yanlış sayı üzerinde** koşuyordu. Sayfa
>    sayısı fiyat modelidir; bir sayfalık sapma ölçülmeden geçemez.

---

## Karar numaralandırma kuralı

- `K##` — alınmış karar. Numara **tekrar kullanılmaz**.
- `A#` — açık karar. Kapandığında bir `K##` doğurur ve burada
  "→ K##" ile işaretlenir; satır silinmez.
- Her karar `CHANGELOG.md`'de o fazın bloğunda anılır. `update_docs.py`
  bu bağı denetler.
