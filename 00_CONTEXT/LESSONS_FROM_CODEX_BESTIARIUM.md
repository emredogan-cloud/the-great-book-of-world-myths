# DERSLER — Codex Bestiarium referans uygulaması

> **Bu belge bir kopyalama listesi değildir.** Codex Bestiarium bu
> projenin *referans uygulamasıdır*: üretim disiplini, araştırma
> doğrulaması, yazım QA'sı, CI/CD, dizgi ve KDP hazırlığı orada çalışır
> hâlde vardır. Buradaki iş, o sistemin **hangi parçasının bir çocuk
> mitoloji antolojisine uyduğunu**, hangisinin **yeniden tasarlanması**
> gerektiğini ve hangisinin **kesinlikle taşınmaması** gerektiğini
> ayırmaktır.
>
> İncelenen sürüm: `v0.4.0` · 88/112 madde yazılmış · Faz 5 devam ediyor.
> **Bestiarium'un hiçbir dosyasına dokunulmadı.** Yalnızca okundu.
>
> Yazıldı: 8 Ağustos 2026 · Bootstrap

---

## A. NE İŞE YARADI

### A1. `.gate` — tek dosyalık faz kapısı

Depo kökünde tek satırlık bir dosya (`phase3`) ve onu okuyan her betik.
CI ilk işinde okuyor, çıktı olarak sonraki işlere veriyor. Kapılar
**kümülatiftir**: bir kapı açıldıktan sonra kapanamaz.

Bunun asıl değeri şu: bir ajanın "hangi fazdayım" sorusuna verdiği cevap
artık bir **tahmin değil, bir dosya okuması**. Hafızası olmayan bir ajan
için bu her şeydir.

→ **Devralındı**, altı seviyeye genişletilerek (`phase0`…`release`).

### A2. `selftest.py` — kapıların kendi testi

Bestiarium'un en değerli tek mekanizması. Kendi yorumu:

> *"Metin yokken yeşil kalan bir hat, kusur geldiğinde de yeşil
> kalabilir. Bu test o riski kapatır: kasıtlı kusurlu bir kurgu kitap
> çalıştırılır ve her kapının o kusuru YAKALADIĞI doğrulanır."*

Bu, "test yazdım" demenin çok ötesinde bir şey: kapıların **körlüğüne
karşı** bir kapı. Bu projede kaçınılmaz olarak daha da kritik, çünkü
yaş politikası kapısı 45 hikâyeyi otomatik reddetme yetkisine sahip
olacak ve o yetkinin doğru çalıştığı kanıtlanmadan kullanılamaz.

→ **Devralındı ve genişletildi**: yaş, okunabilirlik ve kültürel
kısıtlılık kapıları için ayrı kusurlu kurgular eklendi.

### A3. Kalite kapıları standart kütüphaneyle

CI'ın ana doğrulama işi hiçbir `pip install` yapmıyor ve saniyeler içinde
bitiyor. Ağır bağımlılıklar (Pillow, numpy, reportlab) yalnızca görsel
ölçümü ve dizgi işlerinde.

Sonucu ölçülebilir: `validate.yml` beş paralel iş çalıştırıyor ve
neredeyse hiçbiri kurulum beklemiyor. Yazım fazlarında günde onlarca push
olur; her push'ta iki dakika kurulum beklemek disiplini öldürür.

→ **Devralındı** (karar K7).

### A4. Üretilen belge bayatlık kapısı

`update_docs.py --check`, `make_prompts.py --check`, `classify.py --check`
— üretilen her belge CI'da yeniden üretilip diff'i alınıyor. Bayatsa
kırmızı, ve `if: failure()` adımı **farkı ekrana basıyor**.

Bestiarium'un kendi gerekçesi tam yerinde:

> *"'Her faz sonunda güncelle, asla unutma' bir disiplin talebidir ve
> disiplin unutulur. Mekanizma unutmaz."*

→ **Devralındı** (karar K15).

### A5. Türetilen veri, elle yazılmayan veri

`spec.json` elle yazılmadı; master yol haritası HTML'inden `seed_import.py`
ile **türetildi** ve `--check` moduyla ayrışma CI'da yakalanıyor. 120 kaydı
elle yazmak bir transkripsiyon hatası kaynağıdır.

Aynı mantık prompt kütüphanesinde de var (D7): üslup gövdesi tek yerde
durur, değişirse 120 prompt birlikte değişir. "Tek çizgi dili" şartı ancak
böyle tutulabilir.

→ **Devralındı** (karar K16), ama bir farkla: bu projede yol haritası
45 hikâyeyi saymıyor (yalnızca sayıyı veriyor), bu yüzden `story_index`
türetilemez — **elle yazılır ama şemayla ve kapıyla korunur**.

### A6. Ölçülmüş sayfa bütçesi

Bestiarium sayfa bütçesini tahmin etmedi: madde sayfasını gerçekten dizdi
(`entry_page.py --proof`), ölçtü, ve 380 sayfalık tahmini **436**'ya
düzeltti (D26). Fark tek bir kuraldan geliyordu: plaka üst yarıya oturuyor
→ madde sayfa başından başlıyor → her madde 3 sayfa faturalanıyor.

Faz 3'te dolgu yerine gerçek metinle yeniden ölçtü (D36) ve model
**muhafazakâr** çıktı: gerçek metin dolgudan %16 daha az yer kaplıyordu
ama sayfa bütçesi değişmedi.

→ **Devralındı**. Bu projede aynı risk daha büyüktür: 45 hikâye × 950
kelime + 22 kültür kartı + ön/arka madde = 230 sayfa iddiası ve **fiyat
modeli o sayıya dayanıyor** (16,99 $ · maliyet 3,76 $).

### A7. Kaynak katmanları ve doğrulama seviyeleri

`SOURCING_STANDARD.md`'nin dört katmanı (`primary` · `scholarly` ·
`reference` · `index`) ve yedi doğrulama seviyesi (`fulltext` · `toc` ·
`article` · `sv` · `canon` · `catalog` · `secondary`) gerçekten
düşünülmüş bir sistemdir. En güçlü fikri:

> *"Güç ölçütü 'okudum mu' değil, **'okur gidip bakabilir mi'**dir."*

Ve en güçlü yasağı:

> *"Doğrulanmamış bir sayfa numarası yazmak, uydurma kaynak yazmakla
> **aynı şeydir** ve daha sinsidir çünkü doğru görünür."*

→ **Devralındı ve uyarlandı** — çocuk kitabına özgü iki katman eklendi
(§ H2).

### A8. Karar kaydı disiplini

46 numaralı karar (`D1`…`D46`), her biri gerekçesiyle, `CHANGELOG.md` ile
bağlı ve `update_docs.check_decision_links` ile kapıya bağlı. Altı ay
sonra "bunu neden böyle yapmıştık" sorusunun cevabı var.

→ **Devralındı** (`DECISIONS.md`, `K##`/`A#` numaralandırması).

---

## B. BAŞLANGIÇTA NE BAŞARISIZ OLDU

Bunların hepsi Bestiarium'un kendi `CHANGELOG.md`'sinde kayıtlı. Hiçbiri
tahmin değil.

| # | Ne oldu | Nasıl bulundu | Bu projeye etkisi |
|---|---|---|---|
| B1 | **Plaka ölçümü 45° taramada √2 yanlıydı.** Şartnameye birebir uyan kurgu plakası reddediliyordu — hat, doğru çizilmiş 112 plakanın **tamamını** geri çevirecekti. Hata %41 → %0,3. | `plate_selftest.py` (kalibrasyon testi) | Görsel ölçümü **kalibre edilmeden** hiçbir görsel ölçülmez. Aynı kural burada. |
| B2 | **Plaka şartnamesi kendi kendisiyle çelişiyordu**: "22–28 çizgi/cm" ve "çizgi kalınlığı 1,4 pt" aynı anda imkânsız (periyot 4,72 px, darbe 5,83 px). | aynı kalibrasyon | Görsel şartnamesi **sayısal olarak tutarlı** olmak zorunda; `images.py --calibrate` denetler. |
| B3 | **`selftest` her faz kapanışında kendini yanlışlıyordu.** "Bir üst kapı kapalı olmalı" varsayımı, kapı açılınca kırmızıya dönüyordu. | Faz 1 ve Faz 2 kapanışında iki kez | Kapı testi `.gate`i okuyup **dinamik** kurulur, sabit seviye varsaymaz. |
| B4 | **Test kurgusu kendi kendini tekrarlıyordu.** Sabit adımlı sayaç (31 kelimelik sözlük, 7 adım, gcd=1) aynı diziyi üretiyor, iki bölüm aynı 8-gram'ı taşıyordu. `qa_echo` bunu **doğru** yakaladı — düzeltilen betik değil kurgu oldu. | `qa_echo` | Kurgu üreteci **rastgele değil, çakışmasız** olmalı. |
| B5 | **`validate_structure.py` kendi kaynağını kirletiyordu.** Görünmez karakter tablosu o karakterleri doğrudan içeriyordu; tarama kendini yakaladı. | kendisi | Desen tabloları **kaçış dizisiyle** yazılır. |
| B6 | **Satır içi kod çift boşluk sanılıyordu.** Tipografi taraması kod bloklarını *silerek* maskeliyordu: `` `a` b `` → `  b`. | tipografi kapısı | Maskeleme **yer tutucuya** çevrilir, silmeye değil. |
| B7 | **Boş klasörler depoya girmiyordu.** `.gitignore` `09_ARCHIVE/` dizinini komple yok sayıyordu; negatif kalıp (`!.gitkeep`) dizin dışlandığında **çalışmaz**. | ilk commit | `09_ARCHIVE/*` biçimi kullanılır — bu projede baştan doğru yazıldı. |
| B8 | **`plates.yml` pip önbelleği koşulsuzdu.** İş yalnızca plaka varsa pip kuruyor; kurmadığında `setup-python`'ın post adımı "cache folder doesn't exist" diye çöküyordu. | CI kırmızı | Koşullu kurulum yapan işte `cache: pip` **kullanılmaz**. |
| B9 | **Türkçe `İ` çıpayı kırıyordu.** `İ` küçültülünce `i` + U+0307 olur; slugifier birleşen işareti atıyor ve doğru bir bağlantıyı kırık sanıyordu. | bağlantı kapısı | Proje kökü zaten `MY-DİGİTAL-BOOK` altında. Slug normalizasyonu **NFD + combining-mark temizliği** ile yazıldı. |
| B10 | **`qa.py` Cilt 1'e özgüydü ve import anında çöküyordu.** Yol haritası onu "devralınacak" sayıyordu ama modül düzeyinde `build/book.json` okuyor ve Mythologica'nın kimliklerine sabitlenmişti. | import testi | **Devralınan betik diye bir şey yok** — bu proje hiçbir betiği kopyalamadı, hepsi yeniden yazıldı. `build.yml` yine de "bütün modüller import edilebiliyor" testini taşıyor. |

---

## C. HANGİ QA HATALARI BULUNDU (kapılar kendileri kusurluydu)

Bu bölüm en pahalı derstir: **bir kapı, yanlış çalıştığında sessizdir.**

### C1. `qa_diacritics` doğru metni reddediyordu — iki kez

**D32:** Tarama `re.I` (büyük/küçük harf duyarsız) koşuyordu. `Lóng`un
diakritiksiz hâli `Long`dur ve İngilizcenin en sık sözcüklerinden biriyle
çakışır: *"…long after it has gone"* cümlesi diakritik hatası olarak
raporlandı. 78.400 kelimelik bir kitapta bu kapı yazarı "long" sözcüğünü
**hiç kullanmamaya zorlardı**.

**D35:** Kitapta iki ayrı madde vardı: `Lámia` (Hellenic) ve `Lamia`
(Euskal). Bask olanın adında aksan **yoktur**. Kapı, doğru yazılmış
"Lamia"yı "Lámia"nın düşürülmüş hâli sanıp reddediyordu — yani Bask
maddesinin **yazılmasını engelliyordu**.

> Bestiarium'un kendi teşhisi: *"doğru metni reddeden bir cetvel."*

Bu projede risk daha yüksek: 22 kültür demek çok daha fazla diakritik
demek (Kore romanizasyonu, Farsça, Türkçe, Yoruba ton işaretleri,
Hawai'ice ʻokina ve kahakō, İnuktitut). Ve **çocuk kitabında telaffuz
rehberi bir satış argümanıdır** — yani adlar hem doğru hem tutarlı olmak
zorunda.

→ Kapı **baştan büyük/küçük harfe duyarlı** ve **"düz biçimi başka bir
adın gerçek yazımı olan dizeler bayraklanmaz"** kuralıyla yazıldı (K12).

### C2. `qa_echo` tutarlı künyeyi kusur sayıyordu

**D34:** Aynı başvuru eseri 112 maddenin çoğunda anılır ve künye biçimi
**tutarlı olmak zorundadır** — bir başvuru cildinde künyeyi maddeden
maddeye değiştirmek kusurun ta kendisidir. Kapı bunu "üslup tekrarı"
sayıyordu.

→ Kaynak notu maddeler arası öbek taramasından muaf tutuldu.

Bu projede **ikinci bir muafiyet** gerekiyor: her hikâyenin sonundaki
2 satırlık kültürel not kısa ve yapısal olarak benzer olabilir. Ama
muafiyet burada tehlikelidir (bkz. C4).

### C3. `ALLOWED_ECHOES` — üçüncü ölü kural

**D34'ün ikinci yarısı:** Muafiyet listesi, 8 kelimelik bir gram'ın
kümedeki bir öğeye **birebir eşit** olmasını arıyordu; kümedeki en uzun
öğe **4 kelimeydi**. Yani muafiyet **hiç devreye girmemişti**.

Ölü kural, yanlış kuraldan daha tehlikelidir: yanlış kural hata verir,
ölü kural **hiçbir şey demez**.

### C4. Etik kapı boilerplate'e döndü

Faz 4'ün `qa_echo` bulgusu, üç ayrı yerde **YAŞAYAN GELENEK** kısıt
cümlesinin kalıplaştığını gösterdi. Bestiarium'un kendi yorumu:

> *"Kısıt cümlesi kalıplaşırsa okur onu **atlamayı öğrenir**. Etik kapı
> her maddede yeniden kurulmak zorundadır."*

Bu, bu proje için doğrudan bir uyarıdır: 45 hikâyenin **her birinde**
2 satırlık kültürel not var. O not kalıplaşırsa (*"Bu hikâye X halkının
geleneğinden gelir ve bugün de anlatılır."* × 45) kitabın en güçlü satış
argümanı en ölü sayfası olur.

→ `qa_echo` kültürel notu **muaf tutmaz**; ayrıca `qa_voice` kültürel
notlar arasında şablon benzerliği arar.

### C5. `LIVING_TRADITIONS` iki ölü kimlik taşıyordu

**D28:** Listedeki `ityop-ya` ve `ma-ohi` hiçbir gelenek kimliğine denk
gelmiyordu (`spec.json` `ityopya` ve `maohi` yazıyor). Sonuç: kitabın
**en hassas etik notunu** taşıyan madde (Buda — tarihsel olarak Beta
Israel'e ve zanaatkâr kastlara yöneltilmiş, gerçek insanlara zarar vermiş
bir suçlama) zorunlu kısıtlılık kapısının **dışında** kaldı.

Bestiarium'un teşhisi mükemmel:

> *"Kapının sessizliği, kalitenin kanıtı değil, araştırmacının
> titizliğinin gölgesiydi."*

→ İki karşılık: (K14) her kimlik listesi gerçek bir kayda denk gelmek
zorunda, `validate_spec.py` denetler; (K20) kültürel kısıtlılık taraması
bu projede **muafiyetsizdir** — 22 kültürün neredeyse tamamı yaşayan
gelenektir, muafiyet listesi tutmak hem daha pahalı hem daha riskli.

### C6. Araştırma hattı yazım durumunun sahibi olmuştu

**D31:** `research_gen.sync_spec` durumu koşulsuz `verified` yazıyordu.
Bir madde `written` işaretlendiği an `--check` bayat yanıyor,
`qa_all.sh --fix` ise durumu **sessizce geri alıyordu**: tamamlanmış
yazım işi her tazeleme koşusunda kayboluyordu.

→ Durum makinesi tek sahipli olmalı: araştırma kapısı düşerse durum
`draft`'a iner (kalite geriye gidemez), geçerse yazım durumu korunur.

### C7. Ölçüm kendi kendisiyle çelişiyor görünüyordu

**D37:** `qa_drift` raporu aynı cümlede "başlangıç ~72‰, bitiş ~71‰" ve
"%+21 artış" diyordu. İkisi de doğruydu ama farklı şeylerdi (biri
uydurulan doğru, diğeri iki tek maddenin uçları).

→ Rapor **yargıladığı sayıyı** gösterir. Bir ölçüm, okuyanı ikna
edemiyorsa kapı olarak da işe yaramaz.

### C8. Kapak/pazarlama artefaktına proje dili sızdı

**D44:** Kin-Images Chart bir **okur mıknatısıdır** — okura gider ve
kitabın dilinde (İngilizce) olmak zorundadır. Veri dosyası cümleyi
yalnızca Türkçe taşıyordu ve grafik ilk üretimde **Türkçe bastı**.

Bu projede aynı risk daha büyük: proje belgeleri Türkçe, kitap İngilizce,
ve **QR kodun götüreceği "22 kültür haritası"** okura gidecek bir
artefakttır.

→ Okura giden her artefakt (`en`) ile proje belgesi (`tr`) alanları
şemada **ayrı** ve ikisi de zorunlu.

---

## D. HANGİ ÖLÜ KURALLAR BULUNDU

Toplamda **üç** ölü kural bulundu ve hepsi sessizdi:

| # | Ölü kural | Neden ölüydü | Bu projede karşılığı |
|---|---|---|---|
| Ö1 | `ALLOWED_ECHOES` (D34) | 8-gram'ın 4 kelimelik öğeye birebir eşitliği aranıyordu — imkânsız | Muafiyet listeleri **kapsama** ilişkisiyle çalışır ve `selftest` her muafiyetin en az bir kez devreye girdiğini sınar |
| Ö2 | `LIVING_TRADITIONS` iki kimlik (D28) | Kimlikler gerçek gelenek kimlikleriyle eşleşmiyordu | K14 — her kimlik listesi doğrulanır |
| Ö3 | **`06_REPORTS/*.json` `.gitignore`'da ama `plates.yml` onu denetliyor** | `plate-consistency.json` depoda **hiç bulunmuyor**; CI'ın "kayıtlı raporu denetle" adımı her koşuda sessizce boş geçiyor | **Bu proje tarafından bulundu**, Bestiarium'un kendi kaydında yok. Karar K18: denetlenen rapor `06_REPORTS/tracked/` altında **depoda durur** |

> Ö3 hâlâ Bestiarium'da açıktır. Bu belge onu bildirmek için yazılıyor;
> **düzeltmek bu ajanın işi değil** (izolasyon kuralı). Kurucuya not
> olarak bırakılmıştır.

---

## E. HANGİ KAPILAR GÜÇLENDİRİLDİ

| Ne zaman | Kapı | Nasıl güçlendi |
|---|---|---|
| Faz 1 (D20) | `selftest` | Sabit seviye varsaymayı bıraktı, `.gate`i okuyup bir üstünü sınıyor |
| Faz 2 (D25) | plaka ölçümü | Ayırt edemeyen "dış hat kalınlığı" kapı olmaktan **çıkarıldı**, yerine ölçülebilir "tarama darbesi/periyot" geldi |
| Faz 2 (D28) | kısıtlılık | Kapının kendisi denetlenmeye başlandı (ölü kimlik avı) |
| Faz 3 (D30) | manuscript sızıntısı | Yol kalıbına ek olarak **içerik** taraması geldi ve kasıtlı bir sızıntıyla sınandı |
| Faz 3 (D31) | araştırma ↔ durum | Durum makinesi tek sahipli oldu |
| Faz 4 (D42) | çapraz referans | Göz işi olan "6. bölüm ↔ crossRefs" denetimi **koda bağlandı**; ilk koşuda dört gerçek kusur buldu |
| Faz 4 (D45) | sayfa bütçesi | Elle yapılan ara prova ölçümü mekanizmaya çevrildi (`--measure-all`) |

**Ortak örüntü:** her güçlendirme, bir kapının **yakalayamadığı** bir şey
görüldükten sonra geldi. Bu projede aynı örüntüyü beklemek ve her fazın
DoD'sine *"bu fazda hangi kapı yetersiz kaldı"* sorusunu koymak doğru olur.

---

## F. HANGİ CI KONTROLLERİ DEĞERLİYDİ

Ölçülmüş getiri sırasına göre:

1. **`selftest` — kapıların kendi testi.** Tek başına en değerlisi.
   Hiçbir hat, kendi cetvelini sınamadan 45 hikâyeyi reddetme yetkisine
   sahip olmamalı.
2. **`qa_echo` — tekrar taraması.** Faz 4'ün en çok çalışan kapısı:
   **19 kusur yakaladı, hepsi gerçekti.** Üç ayrı kalıplaşma türü ortaya
   çıkardı ve yazarın kendi analitik kalıplarını gösterdi.
3. **Üretilen belge bayatlık kapısı.** Belge ↔ kod ayrışmasını
   imkânsızlaştırır.
4. **Manuscript sızıntısı (içerik taraması).** Public depo politikasını
   mekanizmaya bağlar.
5. **Import testi** (`build.yml`). Metin ve font olmadan da bütün
   modüllerin import edilebildiğini sınar — *"bir betik açılışta
   çöküyorsa bunu metin geldiği gün değil BUGÜN bilmek isteriz."*
6. **`qa_drift` — üslup sürüklenmesi.** 15 ölçüm boyunca %21 → %8,9
   düşüşü belgeledi. Kapı olarak değil, **ölçü** olarak değerli.
7. **KDP kısıt denetimi** (EPUB MB, PDF boyutu, gömülü font). Ucuz ve
   yayın gününde pahalı bir sürprizi önlüyor.
8. **Sürüm doğrulaması** (`release.yml`): etiket ↔ `.gate` ↔ CHANGELOG
   üçlüsü tutarlı değilse sürüm çıkmıyor.

---

## G. HANGİ KONTROLLER BU PROJEYE UYGUN DEĞİL

Bunlar **taşınmadı** ve taşınmama gerekçeleri kayıtlıdır.

| Bestiarium kontrolü | Neden uygun değil |
|---|---|
| **Thompson motif kodu doğrulaması** (`motifVerified`, 24.975 kodluk dizin) | Motif dizini bir **başvuru cildinin** aygıtıdır. 8–12 yaş bir çocuk `B31.1` görmez ve görmemeli. Araştırma kaydında **bilgi olarak** tutulabilir ama kapı değildir; kapı olursa 45 hikâyeyi akademik bir tasnife tabi tutmak için saatler harcanır ve okur bundan **hiçbir şey** kazanmaz. |
| **Yedi bölümlü sabit madde yapısı** (ad → nerede anlatılır → ne yapar → neden korkulur → akraba imgeler → kaynak) | Bu bir **ansiklopedi maddesi** iskeletidir. Hikâye bu iskeletle yazılamaz; hikâyenin yapısı sahne, çatışma, dönüm, sonuçtur. Sabit bölüm dayatmak 45 hikâyeyi birbirine benzetir — çocuk kitabında ölümcül. |
| **"Ünlem işareti = 0" kuralı** | Bestiarium'un bildirici, yumuşatmayan sesi için doğru. 8–12 yaş için **yanlış**: diyalog var, heyecan var, sesli okuma var. Ünlem **bandı** olur (hikâye başına ≤3), yasak olmaz. |
| **Cümle ortalaması 14–18 kelime** | Yetişkin bandı. Bu kitapta hedef bant **11–14** ve tavan daha sert. |
| **Karşılıklı çapraz referans zorunluluğu** (181 bağ, madde başına 3,23) | Bir bestiyerde "akraba imgeler" okurun aradığı şeydir. Bir hikâye antolojisinde hikâyeler arası zorunlu gönderme anlatıyı böler. Karşılaştırma **kültür kartına** ve arka maddeye taşınır, hikâyenin içine değil. |
| **Plaka çizgi dili ölçümü** (tarama açısı, darbe/periyot, kontrast, tuval oranı) | Bestiarium'un çizgi dili **antika gravürdür** ve 120 plakanın aynı tarama geometrisinde olması ürünün kendisidir. Bu kitabın çizgi dili çocuk illüstrasyonudur; ölçülecek şey tarama frekansı değil **kadraj, kontrast, mürekkep yoğunluğu ve baskıda okunabilirlik**. Ölçüm devralındı, **parametreleri tamamen değiştirildi**. |
| **`ALLOWED_ECHOES` muafiyet listesi** | Ölü kural olduğu kanıtlandı (Ö1). Devralınmadı; yerine kapsama ilişkisi + `selftest` muafiyet kanıtı geldi. |
| **Kindle dosya boyutu 6 MB bütçesi** | Bestiarium'da 120 plaka var; burada 68 var ve sayfa sayısı yarısı. Bütçe yeniden hesaplandı, kopyalanmadı. |

---

## H. HANGİ SİSTEMLER YENİDEN KULLANILIYOR

| Sistem | Nasıl geldiği |
|---|---|
| `.gate` faz kapısı | aynı fikir, altı seviye |
| `selftest` kapı testi | aynı fikir, yeni kusurlarla |
| Standart-kütüphane QA hattı | aynı ilke |
| Üretilen belge bayatlık kapısı | aynı mekanizma |
| Manuscript sızıntısı (yol + içerik) | aynı mekanizma |
| Kaynak katmanları / doğrulama seviyeleri | uyarlandı (§ H2) |
| Sayfa bütçesinin **ölçülerek** kurulması | aynı ilke, yeni geometri |
| KDP marj tablosu ve sürüm kayıt defteri (`editions.py`) | **yeniden yazıldı**, KDP verileri aynı |
| Görsel prompt kütüphanesinin üretilmesi | aynı ilke, HTML arayüz + kopyalama düğmeleri |
| `qa_length` · `qa_voice` · `qa_drift` · `qa_echo` · `qa_diacritics` | aynı beş kapı, **çocuk kitabı parametreleriyle** |
| Karar kaydı + CHANGELOG bağı | aynı disiplin |

### H2. Kaynak standardının uyarlanması

Bestiarium'un standardı bir **başvuru cildi** için yazıldı. Bir çocuk
antolojisi iki ek şey ister:

1. **Kanonik anlatım seçimi.** Bir mitin beş varyantı varsa, bestiyer
   *"varyantlar vardır"* der ve geçer. Bir hikâye **bir** anlatım seçmek
   zorundadır. O seçim gerekçelendirilmeli ve kaydedilmeli:
   `canonicalVersion` + `variantNote`.
2. **Yaş uyarlaması izi.** Kaynakta olan ama kitapta olmayan/örtülen
   şey **kaydedilir**: `ageAdaptationNote`. Bu, ebeveyn veya öğretmen
   *"bu hikâyenin sonu böyle değil"* dediğinde verilecek cevaptır — ve
   cevap "kaynağı bilmiyorduk" olamaz.

Bestiarium'un varyant ilkesi burada da geçerli ve **daha da değerli**:

> *"Çelişkiler saklanmaz, gösterilir. Mitolojide varyantlar kuraldır.
> 'Bu anlatının şu bölgede farklı bir sonu vardır' cümlesi bir kusur
> değil, kitabın **otoritesinin kanıtıdır**."*

Çocuk kitabında bu cümle **kültürel notun** işidir.

---

## I. HANGİ SİSTEMLER YENİDEN TASARLANDI

| Sistem | Neden yeniden tasarlandı |
|---|---|
| **Yaş kapısı (`qa_age.py`)** | Bestiarium'da **yok** — ihtiyacı yoktu. Bu projede en önemli metin kapısı. Yol haritası riski (`R2`) ve azaltmasını (`AGE_POLICY.md`) adıyla yazmış. |
| **Okunabilirlik kapısı (`qa_readability.py`)** | Bestiarium'da **yok**. "8–12 yaş" ölçülebilir bir okuma seviyesidir; "sıcak ve hızlı" iddiası ölçülmeden doğrulanamaz. |
| **Kültürel kısıtlılık taraması** | Bestiarium'da muafiyet listeli. Burada **evrensel** (K20). |
| **Çapraz referans sistemi** | Hikâyeler arası bağ değil; **telaffuz · sözlük · kültürel not · harita** kapsamı. Farklı soru, farklı kapı (`qa_crossref.py`). |
| **Görsel tutarlılık ölçümü** | Gravür geometrisi değil; kadraj, kontrast, mürekkep yoğunluğu, baskı okunabilirliği. |
| **Sayfa modeli** | Madde geometrisi değil; hikâye açılış sayfası + kültür kartı + ön/arka madde. Ve **`.gitignore`'daki rapor kuralı düzeltildi** (Ö3 → K18). |
| **Faz sayısı** | Altı değil beş; ve **yazım üç faza dağıtıldı** (Bestiarium yazımı Faz 3–5'e dağıttı ama Faz 1–2 tamamen yazımsızdı; burada Faz 1 bir pilot hikâye yazar — K3). |

---

## J. BU PROJEDE NE DAHA SIKI OLMALI

Sekiz madde. Hepsinin gerekçesi ya yol haritasında ya Bestiarium'un kendi
kayıtlarındadır.

### J1. Yaş uygunluğu bir kapıdır, bir niyet değil
Yol haritası riski adıyla koydu ve azaltmasını adıyla yazdı. `AGE_POLICY.md`
17 içerik kategorisini **İZİN VERİLEN / İMA EDİLEN / ÇIKARILAN / ÖZEL
İNCELEME** olarak ayırır; `qa_age.py` desenlerini kapıya bağlar; her
hikâye kaydında `ageReviewStatus` alanı vardır ve boş bırakılamaz.

### J2. Kültürel kısıtlılık taramasında muafiyet yok
Bestiarium'un D28 kusuru bu kitapta 22 kez tekrarlanabilir. Muafiyet
listesi tutmak, listeyi doğru tutma yükümlülüğü doğurur; taramayı
evrensel yapmak o yükümlülüğü ortadan kaldırır (K20).

### J3. Kalıplaşma etik kapıyı öldürür
C4'ün doğrudan sonucu. 45 kültürel not, 45 hikâye açılışı ve 45 hikâye
kapanışı **kalıplaşmaya en açık** üç yerdir. `qa_echo` bunları muaf
tutmaz ve `qa_voice` şablon benzerliği arar.

### J4. Telaffuz doğruluğu bir satış argümanıdır — ve kapıdır
Yol haritası telaffuz rehberini ek malzemenin ilk kalemi sayıyor ve
gerekçesi ticari: *"öğretmen ve kütüphaneci için satın alma gerekçesi;
iade oranını düşürür."* Yanlış bir telaffuz, tam da satın alma
gerekçesini çürütür. Her özel ad için telaffuz **zorunludur**
(`qa_crossref.py`) ve kaynağı kaydedilir.

### J5. Kaynak izlenebilirliği yetişkin cildindeki kadar sıkı
Çocuk kitabı olması standardı düşürmez, **yükseltir**: hedef okur
kaynakları kontrol edemez, dolayısıyla güven tamamen yayıncıdadır. Aynı
iki-bağımsız-kaynak kuralı, artı `canonicalVersion` ve
`ageAdaptationNote` (H2).

### J6. Uydurma yasağı mutlaktır
Bestiarium D41'in emri değişmeden geçerli:

> *"Never invent mythology. Never invent historical claims. Never
> fabricate references."*

Ve bir ekle: **hikâye uydurulmaz.** Bir mitin boşluğunu anlatı akıcılığı
için doldurmak, çocuk kitabında yetişkin kitabından daha zararlıdır —
çünkü çocuk okuduğunu doğru sanar ve o yanlışı yıllarca taşır. Boşluk
varsa `variantNote` ile **gösterilir**.

### J7. Bir hikâye kaynağı yoksa yazılmaz
Bestiarium'un "120 sayısı kutsal değildir; doğruluk kutsaldır" kuralı
burada da geçerli: **45 sayısı kutsal değildir.** Ama bir fark var —
45 sayısı **alt başlıkta yazıyor** ve alıcı onu tarıyor. Yani düşen bir
hikâyenin yerine **başka bir hikâye gelmek zorunda**, sayı düşürülemez.
Bu yüzden Faz 1'in aday listesi 45'ten fazla olmalıdır (yedekli).

### J8. Sayfa bütçesi fiyat modelinin kendisidir
16,99 $ fiyatı 3,76 $ baskı maliyetine dayanıyor ve o maliyet sayfa
sayısının doğrudan fonksiyonu (1,00 $ + 0,012 $/sayfa). 230 sayfa yerine
280 sayfa, maliyeti 0,60 $ artırır ve telifi 6,43 $'dan ~5,83 $'a düşürür
— %9 telif kaybı. Bestiarium bu dersi 380 → 436 düzeltmesiyle öğrendi
(D26). Burada sayfa modeli Faz 1'de **gerçek metinle** kalibre edilir
(K3) ve her fazda yeniden ölçülür.

---

## Kurucuya not — Bestiarium'da açık kalan bir bulgu

İzolasyon kuralı gereği **düzeltilmedi**, yalnızca bildiriliyor:

`CODEX_BESTIARIUM/.gitignore` § ⑥ satırı `06_REPORTS/*.json` diyor.
`CODEX_BESTIARIUM/.github/workflows/plates.yml` → `consistency` işi →
`kayıtlı raporu denetle` adımı `06_REPORTS/plate-consistency.json`
dosyasını arıyor ve bulamazsa *"henüz tutarlılık raporu yok"* deyip
`exit 0` veriyor.

Dosya `.gitignore`'da olduğu için CI'da **hiçbir zaman** bulunamaz. Yani
"tolerans dışı bir plaka rapora girmişse derleme kırmızı yanar" vaadi
CI'da **hiç işlemiyor** — yalnızca yerelde, `qa_all.sh` koşarken işliyor.

Faz 5 plaka ölçümlerini üreteceği için bu, düzeltilmesi en anlamlı an.
Öneri: raporu `06_REPORTS/tracked/plate-consistency.json`'a yazmak ve
`.gitignore`'a `!06_REPORTS/tracked/` eklemek.
