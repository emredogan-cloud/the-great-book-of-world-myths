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

Durum tablosu · 8 Ağustos 2026

| # | Soru | Aciliyet | Ne zaman kapanmalı |
|---|---|---|---|
| **A1** | Manuscript public depoda mı duracak? | **YÜKSEK** | **Faz 1 başlamadan** |
| **A2** | 22 kültürün tam listesi | YÜKSEK | Faz 1 |
| **A3** | 45 hikâyenin listesi ve kültür dağılımı | YÜKSEK | Faz 1 |
| **A4** | 22 kültür vinyetinin sayfadaki yeri | ORTA | Faz 1 |
| **A5** | Bölüm (part) mimarisi | ORTA | Faz 1 |
| **A6** | Büyük punto sürümü v1.0'a girecek mi | DÜŞÜK | Faz 4 |
| **A7** | KDP Select / KU testi | DÜŞÜK | yayın sonrası |
| **A8** | İki ebeveyn okuyucusu kim | **YÜKSEK** | Faz 4 başlamadan |
| **A9** | ISBN: KDP ücretsiz mi, kendi ISBN'imiz mi | DÜŞÜK | Faz 5 |

---

### A1 · Manuscript public depoda mı duracak?

**Durum:** AÇIK — bootstrap **(a) şıkkını varsayarak** kurulmuştur.

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

**Durum:** AÇIK — 6'sı kilitli, 16'sı aday.

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

**Durum:** AÇIK — A2'ye bağlı.

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

**Durum:** AÇIK.

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

**Durum:** AÇIK.

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

**Durum:** AÇIK — **bu bir insan bağımlılığıdır ve ertelenemez.**

Master yol haritası R2'nin (yaş uygunluğu) azaltmasını iki parçalı
yazıyor: *"yazım öncesi `AGE_POLICY.md`; **yayından önce en az iki ebeveyn
okuması**."*

Birinci parça bu bootstrap'ta yapıldı. İkincisi **kurucunun bulacağı iki
gerçek insandır** ve CI ile üretilemez. `04_BUILD/validate_structure.py`
Faz 5 kapısında `03_EDITORIAL/PARENT_READINGS.md` dosyasını arar; iki
imzalı okuma kaydı yoksa sürüm çıkmaz.

---

### A9 · ISBN

**Durum:** AÇIK — Faz 5.

KDP ücretsiz ISBN verir ama "Publisher" alanı *Independently published*
olur. Kendi ISBN'imiz (TR: Kültür Bakanlığı ISBN Ajansı) yayınevi adını
taşır ve okul/kütüphane kanalında anlamlıdır — bu kitap tam olarak o
kanala girmeyi hedefliyor.

Karar Faz 5'te verilir; her iki hâlde de üretim dosyaları aynıdır.

---

## ALINMIŞ KARARLAR

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

## Karar numaralandırma kuralı

- `K##` — alınmış karar. Numara **tekrar kullanılmaz**.
- `A#` — açık karar. Kapandığında bir `K##` doğurur ve burada
  "→ K##" ile işaretlenir; satır silinmez.
- Her karar `CHANGELOG.md`'de o fazın bloğunda anılır. `update_docs.py`
  bu bağı denetler.
