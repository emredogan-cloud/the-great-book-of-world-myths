# NİHAİ SÜRÜM RAPORU — FAZ 7

> **The Great Book of World Myths** · 10 Ağustos 2026 · kapı `phase5`
>
> # TEKNİK OLARAK HAZIR — KURUCU EYLEMİ GEREKİYOR
>
> Bu rapor Faz 7'nin tek yetkili raporudur ve Faz 6 raporunun
> (`FAZ_6_RAPORU.md`) yerine geçer.
>
> **Kitap yayımlanmadı.** Hiçbir panel işlemi yapılmadı, hiçbir ISBN
> atanmadı, hiçbir dosya yüklenmedi, `v1.0.0` **etiketlenmedi** (§ 11).

---

## 1. Executive summary

Faz 6 *"KDP UPLOAD READY"* diyordu ve bütün kapıları yeşildi. Faz 7 aynı
pakete **dışarıdan** baktı — dosyaları rasterize etti, pikselleri ölçtü,
manuscript'in 45 hikâyesini satır satır okuttu — ve **üretime gitmiş
olacak on bir kusur** buldu.

**En pahalısı baskıya gidiyordu:**

> Ön kapaktaki `AGES 8–12` rozeti **14 punto ile ölçülmüş, 27 punto ile
> çizilmişti**. Yazı güvenli alandan 54 punto, ciltsizde **kâğıdın
> kenarından 27 punto (0,38 inç)** taşıyordu. Basılan kitapta rozet
> **kesilmiş** olacaktı.
>
> Güvenli alan kapısı vardı, yeşildi ve **yanlış şeye bakıyordu**:
> `boxes` listesindeki **planlanan** kutuyu ölçüyordu, çizileni değil.

Sebep tek bir cümleydi: reportlab'da **font bir durumdur** ve ölçüm ile
çizim arasına giren `setFont(27)` bir daha geri alınmamıştı. Bu, projenin
kendi Faz 6 raporunda *alfa için* öğrendiği dersin **aynısıdır** — ders
öğrenilmiş ama **genelleştirilmemişti**.

| | Faz 6 | **Faz 7** |
|---|---|---|
| Kapak kusuru | 0 bilinen | **5 bulundu, 5 düzeltildi** |
| A+ kusuru | 0 bilinen | **3 bulundu** (iki modül tamamen metinsizdi) |
| Manuscript kusuru | denetlenmedi | **275 düzeltme**, 7'si kritik |
| Yazar adı tutarlılığı | kapak ≠ metadata | **tek kaynak** |
| Kapak sanatı çözünürlüğü | ölçülmedi | **ölçüldü: 115 / 106 dpi** ⚠ |
| Kapı sayısı | 83 + 23 | **91 + 41** |

---

## 2. Line Editor sonuçları

Tam rapor: [`LINE_EDITOR_REPORT.md`](LINE_EDITOR_REPORT.md).

45 hikâyenin tamamı, **altı bağımsız geçişte** satır satır okundu: beş
dilim ve kitap genelini gören bir **çapraz denetim**.

| | |
|---|---:|
| Değerlendirilen bulgu | 311 |
| **Uygulanan** | **275** |
| Uygulanmayan (gerekçeli) | 36 |
| Dokunulan hikâye | 43 / 45 |
| Yeniden yazılan kültürel not | 8 |

### Yedi kritik kusur

| # | Ne |
|---|---|
| 1 | Bir hikâyede **iki ardışık paragraf aynı cümleyle başlıyordu** |
| 2 | Bir diyalogda **sahipsiz, kopya bir replik** duruyordu |
| 3 | Bir cümlede **zamirin öncülü yoktu** — sahne tersine okunuyordu |
| 4 | Aynı tanrının adı **iki komşu hikâyede iki farklı biçimde** yazılmıştı, üstelik metin "aynı tanrı" diyordu |
| 5 | **İki konuşmacının replikleri tek paragrafta** birleşmişti |
| 6 | Bir hikâye **kitabın başka bir hikâyesine gönderme** yapıyordu (üslup § 2.2) |
| 7 | **On beş kültürel not**, hikâyenin son paragrafını neredeyse kelimesi kelimesine tekrar ediyordu |

7 numara yalnızca çapraz denetimin görebileceği kusurdu ve en pahalısıydı:
notun iki satırı boşa gidiyor, okur **notları atlamayı öğreniyordu**.

Düzeltme yönü **hikâyenin uzunluğuna göre** seçildi: uzun hikâyelerde
gövdeden kesildi, tabana yakın olanlarda **not yeniden yazıldı**. Yeni not
içeriği `01_RESEARCH/research/*.md` kayıtlarındaki **gerçek kaynaklardan**
alındı (derleyici, yıl, varyant, kaydın sınırı). **Hiçbir olgu
uydurulmadı.**

> ⚠ İlk denemede iki Inuit hikâyesi kesim yüzünden 800 kelime tabanının
> altına düştü. Çapraz denetim bunu **önceden uyarmıştı**: *"kesim değil
> takas"*. Kesimler geri alındı, sorun not tarafından çözüldü.
> **Kapı hatayı yakaladı; sayı uydurulmadı.**

### Kapsam sınırı — dürüstçe

Hikâye **19–27**'yi denetleyecek iki alt ajan, hesap oturum sınırına
takılıp **çöktü**. O dokuz hikâye **ana ajan tarafından elle** denetlendi
(16 düzeltme, 4 not yeniden yazımı). Denetim yapıldı ama **bağımsız bir
ikinci gözle değil** — bu bir sınırdır ve raporlanmaktadır.

### Açık kalan 24 olgu sorusu

Line Editor bunları **değiştirmedi** ve bu doğrudur: kaynağa bakmadan
"düzeltmek" uydurmakla aynı şeydir. Dördü ana ajan tarafından araştırma
kaydına bakılarak çözüldü (bir lehçe tuzağı, bir doğa bilgisi hatası, bir
olgu aşırılığı, bir tutulamayacak söz). **Kalan 20'si bir sonraki
araştırma geçişinin işidir** ve hiçbiri yayını bloklamaz.

---

## 3. Manuscript QA

| Kapı | Sonuç |
|---|---|
| Kelime bandı (800–1100) | ✅ 45/45 · bant dışı **0** |
| Yaş politikası | ✅ |
| Okunabilirlik (FK 4,0–6,5) | ✅ kitap geneli **4,29** |
| Ses ve yasak kalıp | ✅ en uzun cümle **23** kelime |
| Tekrar taraması | ✅ |
| Diakritik ve adlandırma | ✅ |
| Çapraz referans ve kapsam | ✅ |
| Üslup sürüklenmesi | ✅ |
| Araştırma kayıtları | ✅ 45/45 |

| | Önce | Sonra |
|---|---:|---:|
| Hikâye metni | 40.392 kelime | **39.985** |
| Hikâye ortalaması | 898 | 889 |
| İç blok sayfa | 236 | **234** |

Kısalma kasıtlıdır: kesilenlerin çoğu, notun ya da başka bir hikâyenin
zaten söylediği cümlelerdi.

---

## 4. Kapak QA

### Bulunan beş kusur

| # | Kusur | Nasıl bulundu | Durum |
|---|---|---|---|
| ① | **Yaş rozeti kâğıdın kenarından 27 pt taşıyordu** — 14 pt ölçülüp 27 pt çizilmişti | PDF rasterize edildi, yazı kutuları ölçüldü | ✅ |
| ② | **Üretilmiş yanlış başlığı örten bant düz bir bloktu** — ciltlide gün batımını, bulutları ve dağ tepesini yok ediyor, resmin ortasından sert bir çizgi geçiriyordu | ciltli kapak 100 dpi'de gözle incelendi | ✅ |
| ③ | **Sırt yazısı okunmuyordu** — koyu lacivert yazı, sırtın alt yarısındaki koyu yeşil ormanın üstünde kayboluyordu | sırt 300 dpi'de kırpılıp incelendi | ✅ |
| ④ | **Arka kapak paneli sabit yükseklikteydi** — ciltlide dar sütun daha çok satır üretiyor ve son paragraf panelden taşıyordu | ciltli arka kapak incelendi | ✅ |
| ⑤ | **Pus tuvalin kenarına kadar gitmiyordu** — sarımda dikey bir **dikiş** görünüyordu | sağ kenar 200 dpi'de kırpıldı | ✅ |

### Üretilmiş yazı artık ÖRTÜLMÜYOR, ONARILIYOR

Ham sanatta yanlış bir başlık (*"STORIES from the WHOLE WORLD"*) ve
**uydurulmuş bir barkod** basılıydı. Faz 6 ikisini de **düz bir
dikdörtgenle örtüyordu**.

Faz 7 hattı üç adımlıdır ve hepsi ölçülebilir:

1. **Harf maskesi** — yazı, yerel zeminden koyu **ve** zemin açık olan
   piksellerdir. Bulut (zeminden açık) ve orman (zemin koyu) elenir.
2. **Satır kırpma** — maske yalnızca yazının gerçekten bulunduğu satır
   aralığında bırakılır; altındaki balık ve dağ tepesi **gerçek sanattır**.
3. **Onarım** — azalan yarıçaplı difüzyon + çok ölçekli gök modeli.

Üstüne, gökyüzünün **kendi rengiyle** üstten aşağı sönen ince bir pus.
Sonuç: bulutlar ve gün batımı **görünmeye devam ediyor**, harflerden iz
kalmıyor.

**Her iki ham kapakta da üretilmiş barkod bulundu ve onarıldı.**

### Ölçülen

| | Ciltsiz | Ciltli |
|---|---:|---:|
| Sayfa | 234 | 234 |
| **Sırt** | **0,585"** | **0,774"** ✅ KDP hesaplayıcısıyla doğrulandı |
| Tam kapak | 12,835 × 9,25 inç | 13,794 × 10,02 inç |
| Piksel @300 dpi | 3851 × 2775 | 4138 × 3006 |
| Gömülü olmayan font | **0** | **0** |
| Güvenli alan ihlali | **0** | **0** |
| **Sayfa dışına taşan tipografi** | **0** | **0** |
| Çakışan kutu | **0** | **0** |
| Basılan ISBN | **yok** | **yok** |
| Yayıncı | Vâliçe Press | Vâliçe Press |
| **Kapak sanatı etkin dpi** | **115** ⚠ | **106** ⚠ |

### 160 piksel testi (yol haritası § 18)

Kindle kapağı 120 · 160 · 250 piksele küçültülüp gözle sınandı:

| | 120 px | 160 px |
|---|---|---|
| `WORLD MYTHS` | ✅ | ✅ |
| `THE GREAT BOOK OF` | ✅ | ✅ |
| `Emre Doğan` | ✅ | ✅ |
| `AGES 8–12` | ✅ | ✅ |
| `22 Cultures` | ⚠ seçilebilir | ✅ |

---

## 5. A+ QA

**İki modül tamamen metinsiz çıkmıştı** ve hiçbir kapı görmemişti:

| Modül | Şartname diyor ki | Faz 6'da üretilen |
|---|---|---|
| `aplus-009-parent` | *"right side — value proposition text, post-processed"* | boş krem alan |
| `aplus-010-series` | *"right band — series wordmark, post-processed"* | sağı bomboş bir amblem |

Sebep: metin tablosunda boş dize duruyordu, çizim fonksiyonu sessizce
dönüyordu ve doğrulama **yalnızca ölçü, renk ve dosya boyutuna** bakıyordu.

Üçüncü kusur: `aplus-002-cultures` metni **22 amblemin üstünü örtüyordu**
(alt şerit modül yüksekliğinin %58'iydi) ve üstteki %33 bomboştu. Satır
bandı hareketliliği ölçüldü — 0–33% düz · 33–66% amblemler · 66–100% düz —
ve metin **boş bantlara** taşındı.

| | Sonuç |
|---|---|
| Modül | **10 / 10** · hepsi tam Amazon ölçüsünde |
| Metin isteyen modülde metin var mı | ✅ **10/10** |
| Metin bölgesinden taşma | **0** |
| Toplam boyut | 0,34 MB |
| Renk uzayı | hepsi RGB |
| ⚠ Ağır kırpma | `aplus-010-series` %40 (oran uyuşmazlığı, bilinçli) |

---

## 6. Format QA

| Format | Dosya | Boyut | Ölçülen |
|---|---|---:|---|
| Ciltsiz iç blok | `08_OUTPUT/paperback/interior.pdf` | 121,0 MB | 234 s · 6×9 · gömülü font 100% |
| Ciltsiz kapak | `08_OUTPUT/paperback/cover.pdf` | 26.2 MB | 12,835 × 9,25" · sırt 0,585" |
| Ciltli iç blok | `08_OUTPUT/hardcover/interior.pdf` | 121,0 MB | 234 s |
| Ciltli kapak | `08_OUTPUT/hardcover/cover.pdf` | 32.5 MB | 13,794 × 10,02" · sırt **0,774"** ✅ |
| Kindle EPUB | `08_OUTPUT/kindle/book.epub` | **2,77 MB** | bütçe 3,00 · 60 belge · 68 görsel |
| Kindle kapağı | `08_OUTPUT/kindle/cover.jpg` | 0,83 MB | 1706 × 2560 px |
| A+ modülleri | `08_OUTPUT/aplus/` | 0,34 MB | 10 dosya |
| Ara prova | `08_OUTPUT/paperback/proof-interior.pdf` | 0,25 MB | yapısal regresyon avı |

**Büyük punto** yol haritasında *"uzun vadeli genişleme"* listesindedir,
lansman formatlarında değil (K6/A6). Tanımlı ama **devre dışıdır**;
roadmap'te olmayan sürüm **icat edilmedi**.

Kindle kapağı **ciltsiz kapağın ön yüzünden rasterize edilir** — yani
basılı kapakla birebir aynı tipografiyi taşır.

---

## 7. KDP uyumluluğu

| Ölçüt | KDP şartı | Ölçülen | |
|---|---|---|---|
| Ciltsiz sayfa | 24–828 | 234 | ✅ |
| Ciltli sayfa | 75–550 | 234 | ✅ |
| Trim | yayımlanmış liste | 6 × 9 (normal) | ✅ |
| Taşma | tutarlı | No bleed | ✅ |
| İç marj (234 s) | ≥ 0,375" | **0,500"** | ✅ |
| Dış/üst/alt marj | ≥ 0,25" | ≥ 0,44" | ✅ |
| Font gömme | zorunlu | **4/4 PDF'te %100** | ✅ |
| Kapak dosya boyutu | < 650 MB | 29,6 MB | ✅ |
| Barkod bölgesi | 2 × 1,2" temiz | temiz · numara yok | ✅ |
| Kindle kapak yüksekliği | ≥ 1000, önerilen 2560 | **2560** | ✅ |
| EPUB OCF | `mimetype` ilk ve sıkıştırmasız | ✅ | ✅ |
| EPUB gezinme | `nav.xhtml` + `toc.ncx` | ikisi de | ✅ |
| A+ modül ölçüleri | piksel tam | 10/10 | ✅ |
| **Kapak çözünürlüğü** | **≥ 300 dpi** | **115 / 105 dpi** | ⚠ **§ 14** |
| **Ciltli sırt** | KDP hesaplayıcısı | **türetildi** | ⚠ **§ 14** |

---

## 8. Fiyatlandırma önerisi

Tam rapor: [`PRICING_REPORT.md`](PRICING_REPORT.md). Bütün maliyet ve
telif sayıları **ölçülen 234 sayfadan** ve KDP'nin resmî tablolarından
hesaplanmıştır.

| Format | **Lansman** | Telif | Baskı maliyeti | Yerleşik fiyat |
|---|---:|---:|---:|---:|
| Kindle | **6,99 $** | 4,48 $ | — | 7,99 $ |
| Ciltsiz | **14,99 $** | 5,19 $ | 3,81 $ | 16,99 $ |
| Ciltli | **26,99 $** | 7,74 $ | 8,46 $ | 26,99 $ |

**Gerekçe özeti:** iki hacim formatı lansmanda indirimli açılır (yorum ve
sıralama satın almak için), ciltli tam fiyatta kalır — hem alıcısı fiyata
duyarsız olduğu için hem de 26,99 $'lık ciltli, 14,99 $'lık ciltsizi
**açık ara mantıklı seçim** yaptığı için. Zam 25 yorum ya da 90 günde,
**tek seferde**.

> ### 🛑 Kindle'da 9,99 $ bir duvardır
> Bir sent üstünde telif oranı **%70'ten %35'e düşer**:
> 9,99 $ → 6,58 $ · 10,99 $ → **3,85 $**.
> **Bir dolar zam telifin %41'ini siler.**

---

## 9. ISBN · Yayıncı · Yazar

Üçü de `project_config.json` § `founder` içinde **tek kaynakta** durur.

| Karar | Değer | Durum |
|---|---|---|
| **Yazar** | `Emre Doğan` | ✅ kapak · sırt · **iç blok PDF künyesi** · metadata · **EPUB** · teslim belgeleri — hepsi aynı |
| **Yayıncı** | `Vâliçe Press` | ✅ arka kapakta basılı · metadata · **EPUB künyesi** |
| **ISBN** | **KDP ücretsiz ISBN** | ⏳ numara **panelde atanacak** |

### Faz 6'nın sessiz kusuru

Yazar adı `covers.py`, `epub.py` ve `handoff.py` içinde **ayrı ayrı
gömülüydü**; `metadata.py` ise hâlâ `[PENDING — FOUNDER DECISION]`
basıyordu. **Kapak "Emre Doğan", metadata "[PENDING]" diyordu** ve hiçbir
kapı bunu görmüyordu.

Artık dizeler yalnızca yapılandırmada; `validate_structure` betikleri
gömülü değer için tarar (yorumlar muaf) ve `selftest` bunu kasıtlı kusurla
sınar.

**Aynı sınıftan iki kusur daha, son taramada bulundu:**

| Nerede | Ne diyordu | Neden hiçbir kapı görmedi |
|---|---|---|
| **EPUB künyesi** | yayıncı = `[PENDING — founder decision A9]` | Kimlik kapısı yalnızca `metadata.py`'nin **kendi çıktısını** denetliyordu; EPUB'ın İÇİNE bakan kapı yoktu |
| **İki üretim PDF'i** | yazar alanı **BOŞTU** | `project.author` diye **var olmayan** bir anahtar okunuyordu ve `.get()` sessizce boş dize döndürüyordu |

Kural genişletildi: kimlik kapısı artık **üretilen dosyaya** bakar —
EPUB'ın OPF künyesine ve dört üretim PDF'inin künyesine. `package_selftest`
bunu kasıtlı kusurla sınar (41 test).

### ISBN — hiçbir yerde numara yok

- Depoda **hiçbir dosyada** ISBN yoktur ve **uydurulmamıştır**.
- Kapaklardaki barkod alanı **bilerek boştur**; KDP kendi barkodunu basar.
- Her çıktı `PENDING — KDP-PROVIDED ISBN` taşır.
- Yeni kapı: takip edilen hiçbir dosyada **ISBN biçiminde** bir dize
  duramaz. **Bu kapı ilk koşusunda kendi teslim belgemizi yakaladı** —
  Faz 6'da açıklama amacıyla **kısaltılmış** bir sahte ISBN kalmıştı ve
  kısaltılmış hâli **hâlâ ISBN biçimindeydi, hâlâ kopyalanabilirdi**.
  Numara artık hiçbir biçimde tekrarlanmıyor.
- **Kapı bu raporu da yakaladı:** ilk taslakta kusuru anlatmak için o
  kısaltılmış numara alıntılanmıştı. Kapı haklıydı — bir kusuru anlatmak,
  onu tekrar etmeyi gerektirmez.

---

## 10. AI beyanı

**Bu bir olgu bildirimidir, tercih değil.** Kitabın gerçeği:

| Alan | Beyan | Olgu |
|---|---|---|
| **Text** | `AI-generated` | Proza yazılı bir editoryal şartname altında AI ajanı tarafından yazıldı, sonra otomatik kalite kapılarına karşı ölçüldü ve düzeltildi |
| **Images** | `AI-generated` | 68 iç görsel, dünya haritası ve kapak sanatı GPT Image ile yazılı promptlardan üretildi |
| **Translation** | `not applicable` | Çeviri yok |

> ## 🔴 KURUCU EYLEMİ
>
> KDP panelindeki **seçimi kurucu yapar**. Ajan hukuki bir bildirim
> veremez ve bu yüzden `founder.aiDisclosure.founderConfirmed` bayrağı
> **`false`** kalır; kapı bunu her koşuda açıkça basar.
>
> Olgular yukarıdadır. **Kutuya basacak olan sizsiniz.**

---

## 11. Git / CI durumu

| | |
|---|---|
| Dal | `main` |
| Çalışma ağacı | temiz |
| CI · `validate` | ✅ yeşil |
| CI · `images` | ✅ yeşil |
| CI · `build` | ✅ yeşil |
| Kapı (`.gate`) | **`phase5`** (Faz 7 başında `phase3`'tü) |
| Sürüm etiketi | **atılmadı** — gerekçe aşağıda |

### Kapı neden `phase3`'ten `phase5`'e yükseldi

`phase4` kapısı `03_EDITORIAL/PARENT_READINGS.md`'de iki imzalı okuma
arıyordu ve orada sıfır kayıt vardı. **Kurucu H8'i kapattı** (§ 9) ve kapı
beyanı kabul edecek biçimde genişletildi — **ama kanıtın cinsini
raporlayarak**. `phase4` ve `phase5` kapılarının tamamı ayrı ayrı
koşturuldu ve **hepsi yeşil**.

### ⚠ `v1.0.0` NEDEN ETİKETLENMEDİ

`release.yml`, `v1.*` etiketi için `.gate == release` ister. O seviyeye
çıkmak teknik olarak mümkündür — **ama doğru değildir.**

Talimat açık: *"Do not tag v1.0.0 merely because production files exist.
The release tag must represent actual publication readiness."*

**Teslim paketinde, gönderilen dosyaları DEĞİŞTİREBİLECEK iki bilinmeyen
duruyor:**

1. ~~Ciltli sırt türetilmiştir~~ → **ÇÖZÜLDÜ** (11 Ağustos 2026): KDP
   hesaplayıcısı 0,774" verdi, sırt düzeltildi, kapak yeniden üretildi.
2. **Kapak sanatının etkin çözünürlüğü 115/106 dpi'dir** (§ 14). Kurucu
   daha yüksek çözünürlüklü sanat sağlamayı seçerse **her iki kapak da
   yeniden üretilir**. `v1.0.0` için kalan tek engel budur.

Bir sürüm etiketi *"bu, basılan kitabın kaynağıdır"* demektir. Bu iki
soru kapanmadan o cümle **doğru değildir**.

**Etiket ne zaman atılabilir:** ciltli sırt KDP hesaplayıcısıyla
doğrulandığında **ve** kapak çözünürlüğü kararı verildiğinde (A11).
O anda `.gate` → `release`, CHANGELOG'a `## [1.0.0]` bloğu, sonra etiket.

---

## 12. Nihai varlık envanteri

```
08_OUTPUT/
├── paperback/
│   ├── interior.pdf        121,0 MB   234 s · 6×9 · krem · gömülü font
│   ├── cover.pdf            26.2 MB   12,835×9,25" · sırt 0,585"
│   └── proof-interior.pdf    0,3 MB   ara prova (KDP'ye YÜKLENMEZ)
├── hardcover/
│   ├── interior.pdf        121,0 MB   234 s
│   └── cover.pdf            32.5 MB   13,794×10,02" · sırt 0,774" ✅
├── kindle/
│   ├── book.epub             2,8 MB   bütçe 3,0 · 60 belge · 68 görsel
│   └── cover.jpg             0,8 MB   1706×2560 px
├── aplus/                   10 dosya  0,34 MB · tam Amazon ölçüleri
├── metadata.json                      7 anahtar kelime · 3 kategori
├── upload-checklist.md
└── handoff/
    ├── KDP_UPLOAD_HANDOFF.md          alan alan · her yol diske sınandı
    ├── COVER_HANDOFF.md
    └── A_PLUS_HANDOFF.md

KDP_UPLOAD_PLAYBOOK.md               düğme düğme · 27 adım × 3 format
06_REPORTS/PRICING_REPORT.md         fiyat · telif · taban · tavan
06_REPORTS/LINE_EDITOR_REPORT.md     editoryal denetim (prozasız)
```

Ham varlıklar `07_ASSETS/raw/` altında **korundu**; hiçbir ham dosya
değiştirilmedi. `superseded/` **silinmedi**.

### Yeniden üretim — tek zincir

```bash
python3 04_BUILD/research_gen.py    # araştırma kayıtları
python3 04_BUILD/make_index.py      # arka madde
python3 04_BUILD/interior.py        # iç bloklar  → sayfa sayısı
python3 04_BUILD/epub.py            # Kindle
python3 04_BUILD/metadata.py        # metadata
python3 04_BUILD/covers.py          # kapaklar    ← sayfa sayısına BAĞLI
python3 04_BUILD/aplus.py           # A+ modülleri
python3 04_BUILD/handoff.py         # teslim belgeleri
python3 04_BUILD/make_prompts.py    # prompt kütüphanesi
python3 04_BUILD/update_docs.py     # üretilen belgeler
./04_BUILD/qa_all.sh                # BÜTÜN KAPILAR
```

**Sıra önemlidir:** kapak sırtı gerçek sayfa sayısından türer.
Bu zincir Faz 7'de kendini kanıtladı — manuscript kısaldı, sayfa 236→234
düştü, sırt değişti ve kapaklar **otomatik olarak** geçersizleşti.

---

## 13. KURUCU EYLEMİ GEREKEN İŞLER

Ajan bunları **yapmadı ve yapamaz**. Sırayla:

| # | Eylem | Nerede | Hazırlık |
|---|---|---|---|
| ~~1~~ | ~~Ciltli sırtı doğrula~~ | ✅ **TAMAMLANDI** 11 Ağu 2026 → 0,774" | — |
| 2 | KDP hesabına giriş · vergi · banka | KDP hesap ayarları | Playbook § 0 |
| 3 | Üç kitap kaydı oluştur | Bookshelf | Playbook § 2–4 |
| 4 | **"Get a free KDP ISBN"** seç | Content sayfası | karar verildi (§ 9) |
| 5 | *Publisher* → **Vâliçe Press** | Details sayfası | karar verildi (§ 9) |
| 6 | **AI beyanı seçimi** | Details sayfası | olgular § 10'da |
| 7 | Kategori · anahtar kelime | Details sayfası | `metadata.json` |
| 8 | **Fiyat girişi** | Pricing sayfası | öneri § 8 |
| 9 | **KDP Select kararı** (A7) | Kindle Pricing | açık — yayın sonrası veriyle |
| 10 | **Previewer — her sayfa** | yükleme sonrası | Playbook § 22 · hangi uyarıda durulur |
| 11 | **Fiziksel prova siparişi ve okunması** | Proof | — |
| 12 | **Kapak çözünürlüğü kararı** (A11) | prova elde | § 14 |
| 13 | Atanan ISBN'i kaydet | `project_config.json § founder.isbn` | tek yer |
| 14 | **Publish** | KDP | — |

---

## 14. Nihai risk değerlendirmesi

| # | Risk | Seviye | Durum |
|---|---|---|---|
| R1 | ~~Ciltli sırt türetilmiştir~~ → **ÇÖZÜLDÜ** | ~~ORTA~~ **KAPANDI** | Kurucu KDP Cover Calculator'ı çalıştırdı (11 Ağu 2026): **0,774"**. Türetme 0,129" dardı ve reddedilirdi. Düzeltildi ve kapak yeniden üretildi. Kalan: sayfa sayısı değişirse çıpa kapısı yeniden doğrulama ister. |
| R2 | **Kapak sanatı etkin 115/105 dpi** — KDP 300 ister | **ORTA** | Ölçüldü ve raporlandı. Sebep fiziksel: ham sanatın azami çıktısı 1536 px ve 12,8 inçlik sarımı 300 dpi'de üretmeye yetmez. Previewer **uyaracaktır**. Karar prova kopyası görülmeden verilmemeli. |
| R3 | **H8 kanıtı beyandır**, imzalı okuyucu kaydı değil | **ORTA** | Kurucu kararı; kayıt dürüsttür ve kapı her koşuda kanıt cinsini basar. Sahte kanıt üretilmedi. |
| R4 | Hikâye 19–27 bağımsız ikinci gözle denetlenmedi | **DÜŞÜK-ORTA** | Ana ajan denetledi (16 düzeltme). Diğer 36 hikâye bağımsız denetimden geçti. |
| R5 | 20 olgu sorusu açık | **DÜŞÜK** | Hiçbiri yayını bloklamaz; hepsi kayıtlı ve bir sonraki araştırma geçişinin girdisi. |
| R6 | Kültürel notların ~10'u hâlâ gövdeyle örtüşüyor | **DÜŞÜK** | Kritik 8'i düzeltildi. Kalanlar kaynaklı yeni içerik ister; uydurulmadı. |
| R7 | Yaş uygunluğu (roadmap R2) | **ORTA** — projenin tanımlayıcı riski | `qa_age` yeşil · `AGE_POLICY` kapıya bağlı · H8 kurucu beyanıyla kapalı |
| R8 | Ciltsiz iç blok 121 MB | **DÜŞÜK** | KDP sınırı 650 MB |

---

## 15. NİHAİ DURUM

# TEKNİK OLARAK HAZIR — KURUCU EYLEMİ GEREKİYOR

**Teknik olarak tamamlanan:**

- 45/45 hikâye yazıldı, satır satır denetlendi, 275 düzeltme uygulandı
- 68/68 iç görsel + 7 kapak + 10 A+ modülü üretildi ve ölçüldü
- Üç formatın da yüklemeye hazır dosyaları üretildi ve **rasterize
  edilerek gözle doğrulandı**
- Yazar · yayıncı · ISBN stratejisi tek kaynakta, bütün çıktılarda tutarlı
- 91 + 41 = **132 kapı testi**, hepsi kasıtlı kusurla sınandı
- Bütün QA kapıları yeşil · CI yeşil · çalışma ağacı temiz

**Kurucuya kalan:** § 13'teki 14 madde.

**Bu rapor yayımlandığını iddia etmiyor.** Kitap yayımlanmadı, KDP
hesabına girilmedi, hiçbir dosya yüklenmedi, ISBN atanmadı, Previewer
çalıştırılmadı, prova sipariş edilmedi, Publish'e basılmadı, hiçbir sürüm
etiketlenmedi.

**Uydurulmuş hiçbir şey yoktur:** ISBN yok, barkod yok, ebeveyn okuma
kaydı yok, yayıncı bilgisi kurucudan geldi, yorum yok, okuyucu kimliği yok.

---

*Ölçümlerin ham hâli `06_REPORTS/tracked/` altındadır ve hepsi yeniden
üretilebilir.*
