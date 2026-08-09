# CHANGELOG — The Great Book of World Myths

Bu dosya [Keep a Changelog](https://keepachangelog.com/tr/1.1.0/) biçimini
izler ve [Semantic Versioning](https://semver.org/lang/tr/) kullanır.

Her faz **ancak etiketlenerek kapanır** ve her etiketin burada bir bloğu
olmak zorundadır — `release.yml` bunu denetler.

---

## [Yayımlanmamış]

### Sürüyor — Faz 3 · Genişleme (15 hikâye · kümülatif 31/45)

**Yazım öncesi kapı denetimi — dört kusur, üçü tek kelime yazılmadan bulundu**

Faz 3'ün ilk işi yazmak değil, kapıları **hikâyelerin gerçek adlarına karşı**
sınamak oldu. Dördü de "doğru metni reddeden cetvel" sınıfı:

- **`mythbook._WORD` birleşen işaretleri ve ʻokinayı sözcük karakteri
  saymıyordu.** `Ọ̀ṣun` → `['Ọ', 'ṣun']`, `Ilé-Ifẹ̀` → `['Ilé-Ifẹ']`,
  `Hiʻiaka` → `['Hi', 'iaka']`. Sözcük sayısı şişiyor, `proper_names()` var
  olmayan adlar üretiyor, `qa_crossref` doğru yazılmış adı "telaffuz
  rehberinde eksik" sanıyordu. `CHILDREN_WRITING_STYLE` § 5 korunacak
  diakritiklere örnek olarak **tam da bu adları** verir.
- **`qa_crossref` künye adını metinden farklı tokenize ediyordu** —
  kesmeyi ortografik kullanan diller (Maya dilleri, pinyin, Hepburn)
  toptan cezalandırılıyordu. Tek doğruluk kaynağı: `mythbook.declared_tokens()`.
- **Okura giden dizelerde tipografi hiç denetlenmiyordu** (**K28**).
  `qa_voice` yalnızca manuscript'i tarıyor; başlık, telaffuz adı, "kim
  kimdir" rolü ve kültür bölgesi **dizinde** durur. Tarama 33 kusur buldu,
  biri kendi içinde tutarsızdı: *"K’iche' is spoken by…"*.
- **Yaş incelemesi kapısı "kuyrukta" ile "incelendi"yi ayırt edemiyordu.**
  Kimlik defterde bir yerde geçince yetiyordu ve bekleyen kuyruk tablosu bu
  şartı zaten sağlıyordu. Kapı artık yalnızca `AGE-REVIEW:RECORDED` bloğunu
  okur; Faz 2'nin 15 hikâyesi geriye dönük olarak deftere işlendi.

**Kararlar**

- **K28** — kitap tek kesme karakteri kullanır: `’` (U+2019). Okura giden
  dizeler `qa_diacritics` kapısına bağlandı.
- **K29** — Faz 3 sınırı **sayıya** göre çizilir, bölgeye göre değil:
  tam 15 hikâye, kümülatif 31/45. Üçüncü bölge tamamlanır, dördüncü açılır.

**Kapıların kendi testi:** 47 → **65** test.

---

## [0.2.0] — 2026-08-08

**FAZ 2 · ÇEKİRDEK YAZIM — ses ÖLÇEKTE kuruldu.**

Faz 1 bir hikâyenin sistemden geçebildiğini kanıtladı. Faz 2 on altı
hikâyenin ses mekanikleşmeden var olabildiğini kanıtlar.

### Eklenenler

**Manuscript — 15 yeni hikâye (kümülatif 16/45)**
- Bölüm 1 · *The Wine-Dark Sea and the Frozen North* — 10 hikâye
- Bölüm 2 · *Between the Two Rivers* — 5 hikâye (6'ncısı Faz 3'e kaldı)
- **14.973 kelime** · ortalama **936** · bant dışı hikâye **0**
- Sekiz metin kapısının hepsi yeşil · kültürel not şablonlaşması **0**
- Depo **dışında** yaşar (K21); depoda yalnızca ölçüsü durur

**Sürüklenme — ölçüldü, düzeltilmedi (D40)**
- Kontrol noktaları: **%+29,5 → %+25,3 → %+1,7 → %+7,9**
- Hiçbirinde eşik (%35) aşılmadı; son üç ölçüm uyarı eşiğinin (%20) altında
- İlk ölçümün yüksekliği için "kültür çeşitliliği henüz dar" hipotezi
  kaydedildi ve **sonraki ölçümler onu doğruladı** — düzeltme yapılmadı,
  yalnızca daha fazla kültür yazıldı

**Ara prova dizgisi — yeni**
- `04_BUILD/proof_interior.py` — gerçek tipografiyle dizer ve **yapısal**
  kusur arar: taşma, hikâye sırası, başlık genişliği, görsel eşlemesi
- `06_REPORTS/tracked/proof-interior.json` — **yalnızca sayı**, proza yok
- PDF `08_OUTPUT/` altında ve **depo dışında** (proza içerir)
- Sonuç: 16 hikâye × **4 sayfa** — kalibre modelle **birebir**

**Görsel hattı — hazır, üretim kurucuda**
- `06_REPORTS/tracked/PHASE_2_VISUAL_READINESS.md`
- 16/16 prompt üretildi ve konular **hikâyeye özgü** (dönüm anından)
- Ölçüm cetveli kalibre (12/12 test) · Kindle bütçesi 1,08 / 3,00 MB
- **Ham PNG: 0/16 — kurucu üretecek (yol haritası § 21 · H7).**
  H7 yazım fazını **bloklamaz**; hat hazır ve tek komut yeter.

### Düzeltilenler — beş kapı kusuru, hepsi ÖLÇEKTE ortaya çıktı

- **`qa_crossref` künyeli adın İYELİK hâlini eksik sayıyordu.** Künye adı
  kesme işaretinden bölünüyor ("Arachne" → {"Arachne"}), metin belirteci
  bölünmüyordu ("Arachne’s"). Pilotta özel ad iyelik hâlinde hiç geçmediği
  için Faz 1'de görünmedi.
- **`qa_readability` kitabın KENDİ üslup kuralını cezalandırıyordu.**
  `proper_names()` cümlenin ilk sözcüğünü atlar, bu yüzden cümle başındaki
  gerçek ad "zor sıradan sözcük" sayılıyordu — "Demeter" bir hikâyede dört
  kez. Oysa `CHILDREN_WRITING_STYLE` § 2.1 adların **sık ve zamir yerine**
  kullanılmasını emreder. Künyelenmiş adlar artık her konumda tanınıyor.
- **Çok sözcüklü ad iki kez sayılıyordu.** "Cú Chulainn" iki ad, "Emain
  Macha" iki ad. Tavanın gerekçesi bellek yüküdür ve çocuğun öğrendiği şey
  addır; belirteç saymak tavanı **çok sözcüklü adı olan kültürlere karşı**
  çalıştırıyordu.
- **Artikel tuzağı** — yukarıdaki düzeltmenin kendi kusuru: "The Eagle"
  künyesindeki "The" ad parçası sanılıyordu.
- `make_prompts` prompt konusuna çift nokta koyuyordu.

### Düzeltilenler — Faz 1'den kalan iki gizli veri kusuru

İkisi de Faz 1'de görünemezdi, çünkü yalnızca **bir** hikâye yazılmıştı ve
her iki kapı da yalnızca **yazılmış** hikâyeleri denetler:

- **21/59 araştırma kaydında tipografi hatası** — kültürel notlarda 19 düz
  kesme, 14 düz tırnak, 9 boşluklu em dash. 130 alan kaynağında düzeltildi.
- **18/59 kültürel not bant dışıydı** (15–24 kelime; bant 25–45). Hepsi
  **kendi kayıtlarındaki olgularla** genişletildi — dolgu değil, kaynak
  bilgisi. Şablonlaşma **0** kaldı.

### Düzeltilenler — tek doğruluk kaynağı

`story_index.culturalNote` ile `book.culturalNote` ayrışabiliyordu. Kısa bir
süre yanlış yönde senkron yaptım ve **pilotun onaylı (H5) notunu ezdim**;
Faz 1'de inşa edilen kalibrasyon kapısı bunu anında yakaladı
("UYDURULMUŞ örnek"). Yön tersine çevrildi: yazılmış hikâyelerde dizin,
**manuscript'ten** senkronlanır.

### Çözülen iki belge çelişkisi

Talimat § 1 gereği ikisi de **sessizce seçilmedi**, kayda geçirildi. İkisinde
de kazanan **master yol haritasıdır**.

**① Faz 2 kaç hikâye yazar: 15 mi, 16 mı?**
Faz 2 kapsamı "ilk iki bölgesel bölüm" diye tanımlı ve o iki bölüm **16**
hikâye taşıyor. Ama pilot (`korean-dangun`, sıra 21) **üçüncü** bölümdedir,
dolayısıyla iki bölümün tamamı yazılsaydı kümülatif **17** olurdu — oysa
yol haritası ve `project_config` **15 yeni / 16 kümülatif** diyor.
**Karar:** yol haritasının sayısı kazanır. Hikâye 1–15 yazıldı; hikâye 16
(`turkic-basat-tepegoz`) Faz 3'e devredildi. Bu, sonraki fazların
aritmetiğini de tam oturtur: Faz 3 → 16–20 + 22–31 = 15 (kümülatif 31),
Faz 4 → 32–45 = 14 (kümülatif 45).

**② "16 görsel" Faz 2'yi bloklar mı?**
Faz 2 DoD'si "gerekli görsel sayısı karşılandı" diyor; yol haritası § 21 ise
**H7 için** şunu yazıyor: *"H7 hiçbir yazım fazını **BLOKLAMAZ** — hat hazır
ve kalibre; ham girdi geldiği anda tek komut yeter."*
**Karar:** yol haritası kazanır. Faz 2'nin görsel yükümlülüğü **hattın hazır
ve kalibre olması**dır ve o karşılandı (16/16 prompt, 12/12 ölçüm testi).
Ham PNG üretimi kurucunun işidir ve **Faz 5'in** kapısıdır.
**Bu sürüm hiçbir görselin üretildiğini iddia ETMEZ.**

### Tamamlananlar

- **H5 kapandı** — pilot hikâyenin sesi kurucu tarafından onaylandı
- **A8** — kurucu sorumluluğu aldı; **Faz 4 kapanmadan** gerçek kayıt gerekir

### Açık kalan tek kurucu bağımlılığı

**16 ham görsel (H7).** `06_REPORTS/tracked/PHASE_2_VISUAL_READINESS.md`
tam listeyi, hazır promptları ve ham girdi geldiğinde çalışacak tek komut
zincirini taşır.

---

## [0.1.0] — 2026-08-08

**FAZ 1 · TEMEL — kapsam kilitlendi, ses gerçek metinle kalibre edildi.**

Kitabın **neyden oluştuğu** ve **nasıl konuştuğu** bu sürümde belirlendi.
45 hikâye ve 22 kültür kaynaklandı, tarandı ve kilitlendi; ses ve sayfa
modeli **tek bir gerçek hikâyeyle** ölçüldü (**K3**).

### Eklenenler

**Kapsam — kilitli**
- `01_RESEARCH/culture_index.json` — **22 kültür `locked`** + 9 aday (31 kayıt);
  kısıtlılık taraması **22/22 tamam, muafiyetsiz** (**K20**)
- `01_RESEARCH/story_index.json` — **45 hikâye `locked`** + 14 aday (59 kayıt);
  altı **bölgesel bölüm** (**K26**)
- `01_RESEARCH/research/*.md` — **59 üretilmiş araştırma kaydı**,
  163 kaynak künyesi (82 `primary` · 58 `scholarly` · 23 `reference`),
  **0 `retelling` · 0 `index`**

**Kararlar**
- **K21** — A1 kapandı: manuscript depo **dışında** yaşar (şık *a*)
- **K22** — `AGE_POLICY.md` **kurucu onaylı**; on yedi kategori kilitlendi
- **K23** — A2 kapandı: 22 kültür; Polinezya → **Māori + Hawai'i**,
  Batı Afrika → **Yoruba + Akan** (`CHILDREN_WRITING_STYLE` § 7 genelleme yasağı)
- **K24** — A3 kısıtları **kapıya bağlandı**: kültür başına ≤4 ve Yunan ≤3
  artık **hata**, uyarı değil
- **K25** — A3 kapandı: 45 hikâye kilitlendi; kelime bütçesi **42.750**
- **K26** — A5 kapandı: **bölgesel** bölüm mimarisi (altı bölge)
- **K27** — A4 kapandı: kültür kartı **hikâye kuyruğundaki boşlukta** (şık *f*);
  22 kartın hepsi var, hiçbiri ek sayfa tüketmiyor → **228 sayfa**

**Ses ve sayfa kalibrasyonu — gerçek metinle (K3)**
- `00_CONTEXT/CHILDREN_WRITING_STYLE.md` § 2.3 — **üç gerçek kalibrasyon
  paragrafı**, pilot hikâyenin kendi prozasından; ölçüleriyle birlikte
- `04_BUILD/calibrate_pages.py` — **yeni**: pilot prozasını gerçek metin
  bloğuna gerçek yazı karakteri metrikleriyle dizer ve satırları sayar
- `06_REPORTS/tracked/page-calibration.json` — sayfa modeli artık
  **ölçülmüş**: 357,5 kelime/sayfa (tahmin 361,1 · sapma %1,0)
- `04_BUILD/editions.py` — `CHILD_BODY.calibrated = True`;
  `avg_chars_per_word` 5,4 → **5,349**, `avg_char_width_ratio` 0,48 → **0,4895**
- `03_EDITORIAL/AGE_REVIEW_LOG.md` — `REVIEW` kategorili 18 kaydın defteri
- **Sayfa hedefi tutturuldu**: 250 → **228** sayfa, hedeften %0,9;
  ciltsiz telif 6,19 $ → **6,46 $** (yol haritasının 6,43 $'ından **+0,03 $**)

**Manuscript**
- Pilot hikâye `korean-dangun` — **972 kelime**, bütün metin kapılarından geçti.
  Depo **dışında** yaşar (K21); depoda yalnızca ölçüsü durur.

### Düzeltilenler — beş ölü kural (**K14**)

- `validate_spec.py` kültür aday havuzunu (≥26) **yalnızca `phase0`'da**
  denetliyordu; kapı `phase1`'e yükseldiği an denetim kayboluyordu — yani
  DoD ölçüt 7 bir belge cümlesiydi, kapı değil. Her kapıya taşındı.
- `story_index.schema.json` **≥55 aday havuzunu imkânsız kılıyordu**:
  `number` zorunlu tamsayıydı ve tavanı 45'ti. Şema, `SOURCING_STANDARD` § 9'un
  zorunlu kıldığı şeyi yasaklıyordu. Aday kayıtlar için `null` kabul eder oldu.
- `make_prompts.py` şemada **tanımlı olmayan** `story.imagePrompt` alanını
  okuyordu (`additionalProperties: false`); dal hiçbir koşulda çalışamıyordu.
  Konu artık olay örgüsünün **dönüm** anından türetiliyor.
- **`mythbook.load_book()` öz-testi öldürüyordu.** Diskteki manuscript'i
  enjekte edilen kurgudan **önce** okuyordu. Faz 0'da disk boştu ve kusur
  görünmüyordu; **ilk gerçek hikâye yazıldığı an** `selftest.py`'nin
  kusurlu kurgusu yok sayıldı, on beş kapının hepsi gerçek temiz metni
  görüp yeşil yandı ve öz-test *"kapı kusuru görmedi"* demeye başladı.
  Yani kapıların kendi testi, **koruduğu şey var olduğu anda** çalışmayı
  bırakıyordu. Enjeksiyon artık her zaman kazanır.
- **`qa_crossref` doğru metni reddediyordu (D32).** Kendi özel ad tespitini
  yapıyor ve cümle başını `(?<![.!?…]\s)` ile eliyordu; o korumanın kör
  noktası **paragraf başıdır**. Pilot hikâye kapıyı “The” (×21), “Twice”,
  “They” ile kırmızı yaktı. Tespit `mythbook.proper_names()`'e devredildi.

### Eklenen kapılar

- `validate_spec` — yol haritasının **altı geleneğinin** kilitli bir kültürle
  karşılandığı denetimi (K23 daraltmasının kaçış yolu olmaması için)
- `validate_spec` — `restricted` taranan bir kültür **kilitlenemez**
- `validate_spec` — kilitli her kültürün kısıtlılık notu ≥20 karakter
- `validate_structure` — **DoD ölçüt 21**: üç kalibrasyon örneği dolu **ve**
  manuscript'te birebir bulunuyor (uydurulmuş örnek yakalanır)
- `validate_structure` — **DoD ölçüt 26**: A4/A5 `DECISIONS.md`'de `→ K##`
  ile kapanmış **ve** `EDITORIAL_ARCHITECTURE.md`'de yazılmış
- `validate_structure` — sayfa modeli kalibre mi · kalibrasyon raporu depoda mı
- `selftest` — **öz-testin kendi canlılık testi**: enjekte edilen kurgu
  diskteki manuscript'i eziyor mu (bu kusur bir kez oldu ve sessizdi)
- `selftest` — **D32 regresyonu**: ad tespiti paragraf başındaki sıradan
  sözcüğü ad saymıyor **ve** gerçek adı kaçırmıyor (iki yönlü)
- `qa_all.sh` — sayfa kalibrasyonu bayatlık denetimi

---

## [0.0.1] — 2026-08-08

**BOOTSTRAP TAMAMLANDI. Kitabın tek kelimesi yazılmadı.**

Üretim sisteminin kurulumu: yol haritası, kapılar, CI/CD, araştırma
mimarisi, yaş politikası, görsel hattı ve KDP üretim modeli.

### Eklenenler

**Belgeler**
- `THE_GREAT_BOOK_OF_WORLD_MYTHS_MASTER_ROADMAP.md` — beş faz, tek doğruluk kaynağı
- `PROJECT_CONTEXT.md` · `BRIEF.md` · `STYLE.md` (işaret levhası)
- `AGE_POLICY.md` — **on yedi içerik kategorisi**, ALLOW/IMPLY/OMIT/REVIEW
- `SOURCING_STANDARD.md` — çocuk mitolojisi için uyarlanmış kaynak ölçütü
- `00_CONTEXT/CHILDREN_WRITING_STYLE.md` — 8–12 yaş yazım sistemi
- `00_CONTEXT/EDITORIAL_ARCHITECTURE.md` — kitabın yapısı ve sayfa modeli
- `00_CONTEXT/LESSONS_FROM_CODEX_BESTIARIUM.md` — A–J dersleri
- `KDP_UPLOAD_PLAYBOOK.md` — üç format × 27 adım, düğme düğme
- `DECISIONS.md` — 20 karar (K1–K20) + 9 açık karar (A1–A9)

**Veri ve şema**
- `project_config.json` — makine okunur proje yapılandırması
- `01_RESEARCH/culture_index.json` — 6 kilitli + 23 aday kültür
- `01_RESEARCH/story_index.json` — **kasıtlı olarak boş** (Faz 1'in işi)
- `01_RESEARCH/culture_index.schema.json` · `story_index.schema.json`
- `01_RESEARCH/RESEARCH_RECORD_TEMPLATE.md`

**Kalite kapıları** — hepsi standart kütüphaneyle (**K7**)
- `04_BUILD/mythbook.py` — kayıt defteri: bantlar, eşikler, desenler
- `04_BUILD/validate_spec.py` — kapı seviyeli şema ve bütünlük, **ölü referans avı**
- `04_BUILD/validate_structure.py` — depo, belge, **manuscript sızıntısı**
- `04_BUILD/validate_research.py` — araştırma kaydı bütünlüğü
- `04_BUILD/qa_age.py` — **yaş politikası kapısı** (bu projenin en önemlisi)
- `04_BUILD/qa_readability.py` — 8–12 yaş okuma seviyesi
- `04_BUILD/qa_length.py` · `qa_voice.py` · `qa_echo.py` · `qa_drift.py` ·
  `qa_diacritics.py` · `qa_crossref.py`

**Üretim modeli**
- `04_BUILD/editions.py` — KDP sürüm kayıt defteri ve **telif doğrulaması**
- `04_BUILD/page_budget.py` — deterministik sayfa modeli ve ulaşılabilirlik analizi
- `04_BUILD/update_docs.py` · `research_gen.py` · `make_index.py`

**Görsel hattı**
- `04_BUILD/imagespec.py` — 68 görselin şartnamesi, **tek üslup gövdesi**
- `04_BUILD/make_prompts.py` — prompt kütüphanesi **üretilir** (**K16**)
- `07_ASSETS/IMAGE_PROMPT_LIBRARY.md` + `.html` (kopyalama düğmeli)
- `04_BUILD/convert_images.py` — ham PNG → baskı TIFF / Kindle PNG / web WebP
- `04_BUILD/images.py` — tutarlılık ölçümü

**Testler**
- `05_TESTS/selftest.py` — **kapıların kendi testi**, 39 kontrol
- `05_TESTS/make_fixtures.py` — 15 kusurlu kurgu, çakışmasız üreteç
- `05_TESTS/image_selftest.py` — ölçüm kalibrasyonu, 12 kontrol

**CI/CD**
- `.github/workflows/validate.yml` · `images.yml` · `build.yml` · `release.yml`
- `.gitignore` — iki hatlı manuscript koruması
- Issue ve PR şablonları

### Kararlar

Yirmi karar alındı: **K1–K20**. Tamamı gerekçeleriyle
[`DECISIONS.md`](DECISIONS.md)'de.

| # | Özet |
|---|---|
| **K1** | Beş faz: Temel · üç yazım fazı · Üretim |
| **K2** | Yazım üç faza dağıtıldı (1+15+15+14) — talimat § 13'ün açık yasağı |
| **K3** | Faz 1 tam olarak **bir hikâye** yazar: ses kalibrasyonu + sayfa modeli |
| **K4** | **İllüstrasyon ZORUNLU** — 68 görsel, fiyat modelinin dayanağı |
| **K5** | Ham girdi PNG; üretim formatı türetilir, ham dosya asla üzerine yazılmaz |
| **K6** | Büyük punto v1.0'a girmez — tanımlı ama devre dışı |
| **K7** | Kalite kapıları standart kütüphaneyle |
| **K8** | Kapılar kümülatif, `.gate` ile yönetiliyor |
| **K9** | Metin kapıları metin yokken 0 döner — körlüğü `selftest` kapatır |
| **K10** | **Yaş kapısı birinci sınıf** — yol haritasının R2 azaltması |
| **K11** | Okunabilirlik kapısı eklendi — Bestiarium'da yok |
| **K12** | `qa_diacritics` D32 ve D35 kusurlarıyla birlikte devralındı |
| **K13** | `qa_echo` kaynak notunu muaf tutar, **kültürel notu tutmaz** |
| **K14** | Ölü kural avı bir kapıdır — her kimlik referansı doğrulanır |
| **K15** | Üretilen belgeler bayatlık kapısına bağlı |
| **K16** | Görsel promptları **üretilir**, elle yazılmaz |
| **K17** | `main` üretim dalı; faz dalları `faz/**` |
| **K18** | Denetlenen rapor **depoda durur** (`06_REPORTS/tracked/`) |
| **K19** | Kapı seviyeleri: `phase0`…`release` |
| **K20** | Kültürel kısıtlılık taraması **muafiyetsiz** |

### Bestiarium'dan devralınan ve düzeltilerek gelen kusurlar

Referans uygulamanın kayıtlı kusurları, bu projede **baştan düzeltilmiş
hâliyle** geldi:

| Bestiarium | Ne oldu | Buradaki karşılığı |
|---|---|---|
| D32 | `qa_diacritics` `re.I` ile koşuyordu; "long" sözcüğünü hata sandı | Tarama **büyük/küçük harfe duyarlı** |
| D35 | Düz biçimi başka bir adın gerçek yazımı olan dizeler reddediliyordu | D35 muafiyeti baştan var |
| D34 / Ö1 | `ALLOWED_ECHOES` **ölü kuraldı** — birebir eşitlik aranıyordu | **İki yönlü kapsama** + `selftest` her muafiyetin canlı olduğunu kanıtlıyor |
| D28 / Ö2 | `LIVING_TRADITIONS` iki ölü kimlik taşıyordu | Muafiyet listesi **kaldırıldı** (K20); her kimlik referansı doğrulanıyor |
| B3 / D20 | `selftest` her faz kapanışında kendini yanlışlıyordu | Test `.gate`i okur, sabit seviye varsaymaz |
| B4 | Kurgu üreteci kendini tekrarlıyordu | LCG akış + `--verify` |
| B5 | Desen tablosu kendi kaynağını kirletiyordu | Kaçış dizisiyle yazıldı |
| B6 | Satır içi kod "çift boşluk" sanılıyordu | Maskeleme **yer tutucuya** |
| B7 | Negatif `.gitignore` kalıbı dizin dışlanınca çalışmıyordu | `09_ARCHIVE/*` biçimi |
| B8 | Koşullu pip kuran işte `cache: pip` çöküyordu | Önbellek yok |
| B1 | Plaka ölçümü √2 yanlıştı; doğru plakaları reddediyordu | `image_selftest.py` — ölçülen hata **%0,00** |

### Bu projede BULUNAN ve Bestiarium'da hâlâ açık olan kusur

**Ö3 — sessiz ölü kural.** `CODEX_BESTIARIUM/.gitignore` § ⑥
`06_REPORTS/*.json` diyor; `plates.yml` → `consistency` işi
`06_REPORTS/plate-consistency.json` dosyasını denetlemeye çalışıyor. Dosya
`.gitignore`'da olduğu için CI'da **hiçbir zaman bulunamaz** ve o adım her
koşuda sessizce `exit 0` veriyor.

İzolasyon kuralı gereği **düzeltilmedi**, kurucuya bildirildi
(`LESSONS_FROM_CODEX_BESTIARIUM.md` son bölüm). Bu projede karşılığı
**K18**'dir: denetlenen rapor `06_REPORTS/tracked/` altında depoda durur.

### Ölçülenler

| | |
|---|---:|
| Kilitli kültür | 6 / 22 |
| Aday kültür | 23 |
| Kilitli hikâye | 0 / 45 |
| **Yazılmış hikâye** | **0 / 45** |
| Üretilen prompt | **68** |
| Kalite kapısı betiği | 13 |
| Kapı kontrolü (`qa_all.sh`) | 20 |
| `selftest` kontrolü | **39** |
| Görsel kalibrasyon kontrolü | **12** |
| Görsel ölçüm hatası | **%0,00** |
| Yaş politikası kategorisi | **17** |
| Alınan karar | 20 |
| Açık karar | 9 |

### Doğrulanan ticari model

`04_BUILD/editions.py` KDP'nin resmî tablolarından yol haritasının verdiği
**beş sayının hepsini birebir** üretti: ciltsiz maliyet 3,76 $ · ciltsiz
telif 6,43 $ · ciltli maliyet 8,41 $ · ciltli telif 7,78 $ · Kindle telif
5,14 $.

Ve **bir sayı türetti**: Kindle dosya bütçesi **3,0 MB**. Yol haritası bunu
yazmıyordu; 5,14 $ telif rakamından geriye doğru hesaplandı
(7,99 $ × %70 − 5,14 $ = 0,453 $ teslim ücreti ÷ 0,15 $/MB = 3,02 MB).

### Bulunan yapısal sorun — sayfa bütçesi

`04_BUILD/page_budget.py`, **230 sayfanın varsayılan yapıyla ulaşılamaz**
olduğunu buldu. Sebep aritmetik değil yapısal: her hikâye yeni sayfada
başlar ve yukarı yuvarlanır, bu yüzden hikâye başına maliyet 3 ↔ 4 arasında
zıplar ve aradaki toplamlar (204 · **250** · 294 · 340 dışındakiler)
ulaşılamazdır.

İki yapısal seçenek hedefi tutturuyor; ayrıntı `DECISIONS.md` § A4.
**Karar Faz 1'in gerçek dizgi ölçümünden sonra verilir.**

### Açık kalanlar

- [ ] **A1** — manuscript public depoda mı duracak (**Faz 1 başlamadan**)
- [ ] **A2** — 22 kültürün tam listesi (Faz 1)
- [ ] **A3** — 45 hikâyenin listesi ve dağılımı (Faz 1)
- [ ] **A4** — kültür vinyetinin sayfadaki yeri (Faz 1)
- [ ] **A5** — bölüm (part) mimarisi (Faz 1)
- [ ] **A6** — büyük punto v1.0'a girecek mi (Faz 4)
- [ ] **A7** — KDP Select / KU testi (yayın sonrası)
- [ ] **A8** — iki ebeveyn okuyucusu kim (**Faz 4 başlamadan**)
- [ ] **A9** — ISBN kararı (Faz 5)
- [ ] `CHILDREN_WRITING_STYLE.md` ses kalibrasyon örnekleri (Faz 1)
- [ ] Sayfa modelinin gerçek dizgiyle kalibrasyonu (Faz 1)

---

[Yayımlanmamış]: https://github.com/emredogan-cloud/the-great-book-of-world-myths/compare/v0.0.1...HEAD
[0.0.1]: https://github.com/emredogan-cloud/the-great-book-of-world-myths/releases/tag/v0.0.1
