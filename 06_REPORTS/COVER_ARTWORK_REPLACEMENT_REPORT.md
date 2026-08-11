# KAPAK SANATI DEĞİŞİM RAPORU

> **The Great Book of World Myths** · 10 Ağustos 2026 · kapı `phase5`
>
> | | |
> |---|---|
> | **ESKİ SANAT** | **devre dışı** — arşivde, silinmedi |
> | **YENİ SANAT** | **yetkili** — `07_ASSETS/raw/re-generated/` |
> | **TİPOGRAFİ** | **CLI ile üretildi** — `04_BUILD/covers.py` |
> | **ISBN** | **KDP ücretsiz ISBN** — hiçbir numara uydurulmadı |
> | **YAZAR** | **Emre Doğan** |
> | **YAYINCI** | **Vâliçe Press** |

---

## 1. Önceki kapak sorunu

İlk kapak sanatına, üreten model tarafından iki şey **basılmıştı**:

| # | Ne | Neden kabul edilemez |
|---|---|---|
| ① | **Yanlış başlık** — *"STORIES from the WHOLE WORLD"* | Kitabın adı **The Great Book of World Myths**. Yanlış adla basılmış bir kapak iade sebebidir. |
| ② | **Uydurulmuş ISBN barkodu** | Numara projeye ait değildi. Tarandığında **başka bir kitabı** gösterir. |

Kapak hattı bunları **algoritmayla siliyordu**:

```
harf maskesi → azalan yarıçaplı difüzyon → çok ölçekli gök modeli → pus
```

**Teknik olarak çalışıyordu.** Harfler gidiyordu. Ama **yanlış işti**: bir
üreticinin yaptığı resmi başka bir algoritmayla onarmak, her koşuda biraz
daha bozar. Ciltli kapakta gün batımı ve bulutlar bu yüzden düzleşmişti;
ilk sürümde bandın alt kenarı resmin ortasından geçen sert bir çizgi
olarak görünüyordu.

**Kurucu doğru kararı verdi ve bütün kapak sanatını metinsiz yeniden
ürettirdi.** Bu rapor o değişimi belgeler.

---

## 2. Yeni sanat envanteri

Konum: `07_ASSETS/raw/re-generated/` · **8 master** · 23,1 MB · **SALT OKUNUR**

| Dosya | Piksel | Oran | Mod | Boyut | sha256 (ilk 12) |
|---|---:|---:|---|---:|---|
| `cover-paperback-wrap.png` | 1478 × 1064 | 1,389 | RGBA | 2,84 MB | `601de02da6a1…` |
| `cover-hardcover-wrap.png` | 1465 × 1073 | 1,365 | RGBA | 2,96 MB | `8f69e531e8cc…` |
| `cover-paperback-front.png` | 1024 × 1536 | 0,667 | RGBA | 2,78 MB | `2f24b7389243…` |
| `cover-back-panel.png` | 1023 × 1537 | 0,666 | RGBA | 2,24 MB | `d23cc6235ab6…` |
| `cover-front-variant-figures.png` | 1023 × 1537 | 0,666 | RGBA | 3,10 MB | `7c5cd228e009…` |
| `cover-front-variant-object.png` | 1023 × 1537 | 0,666 | RGBA | 2,83 MB | `1afc34e0229f…` |
| `cover-thumbnail.png` | 959 × 1641 | 0,584 | RGBA | 3,20 MB | `6525cd128a8e…` |
| `cover-thumbnail-test.png` | 942 × 1670 | 0,564 | RGBA | 3,18 MB | `9fb180255681…` |

**Üretimde kullanılan iki master:** `cover-paperback-wrap` ve
`cover-hardcover-wrap`. Diğerleri varyant/yedek/testtir.

Hiçbir dosya yeniden adlandırılmadı. Hiçbir master'a yazılmadı.

---

## 3. Yeni sanatın doğrulanması

Her master **büyütülerek gözle incelendi**. Sonuçlar tek tek kayıtlıdır
(`cover_artwork.VISUAL_VERDICT`) ve kapı, kayıtsız bir master eklenirse
"incelenmemiş sanat" der.

| Master | Başlık | Yazar | Yayıncı | Sahte ISBN/barkod | Filigran | **Sonuç** |
|---|---|---|---|---|---|---|
| `cover-paperback-wrap` | yok | yok | yok | yok | yok | ✅ **temiz** |
| `cover-hardcover-wrap` | yok | yok | yok | yok | yok | ✅ **temiz** |
| `cover-paperback-front` | yok | yok | yok | yok | yok | ✅ temiz |
| `cover-back-panel` | yok | yok | yok | yok | yok | ✅ temiz |
| `cover-front-variant-figures` | yok | yok | yok | yok | yok | ✅ temiz |
| `cover-front-variant-object` | yok | yok | yok | yok | yok | ✅ temiz |
| `cover-thumbnail` | yok | yok | yok | yok | yok | ✅ temiz |
| `cover-thumbnail-test` | **VAR** | yok | yok | yok | yok | 🔴 **ARTWORK_REQUIRES_REGENERATION** |

### 🔴 `cover-thumbnail-test.png` — metin bulundu, DOKUNULMADI

Bu dosyada üretilmiş tipografi vardır ve **resme basılıdır**:

- `The Great Book of` / `WORLD MYTHS` / `22 Cultures`
- `8–12 YEARS` rozeti

**Talimat § 3 uygulandı: metin KALDIRILMADI, maskelenmedi, onarılmadı.**
Kurucu bu sanatı zaten yeniden üretmişti; temiz hâli
**`cover-thumbnail.png`** olarak aynı dizindedir.

**Yayını bloklamaz:** üretim varlığı değildir. `coverspec.py` bu kaydı
*"ÜRETİM VARLIĞI DEĞİL, TESTTİR"* diye işaretler (160 piksel okunabilirlik
prosedürünü görünür tutmak için vardır) ve `covers.py` onu **hiç okumaz**.

> ### ⚠ MAKİNE METİNSİZLİĞİ KANITLAYAMAZ — VE BU DÜRÜSTÇE SÖYLENMELİDİR
>
> Otomatik bir "bu görselde tipografi var mı" kapısı **denendi ve
> başarısız oldu.** "Yerel zeminden koyu + zemin açık" maskesinin satır
> bandı imzası, **yer gerçeğiyle** sınandığında metinli ve metinsiz sanatı
> ayıramadı:
>
> | Sanat | Gerçek | Bant skoru |
> |---|---|---:|
> | `back-panel` | **metinsiz** | %6,04 |
> | `thumbnail-test` | **metinli** | %1,63 |
> | `hardcover-wrap` (yeni) | metinsiz | %7,90 |
> | `paperback-wrap` (eski) | metinli | %0,00 |
>
> Dağ silueti, orman kenarı ve bulut da "açık zemin üstünde koyu leke"dir.
> **Ayırt edemeyen bir kapı ölü kuraldır ve yeşil yanarak yalan söyler**
> (`LESSONS_FROM_CODEX_BESTIARIUM` § D). Bu yüzden **konulmadı**.
>
> Metinsizlik kararı **gözle** verilmiştir ve yukarıdaki tablo o kararın
> kaydıdır. Makinenin garanti ettikleri § 13'tedir.

---

## 4. Güncellenen formatlar

| Format | Dosya | Sanat kaynağı |
|---|---|---|
| Ciltsiz kapak | `08_OUTPUT/paperback/cover.pdf` | `re-generated/cover-paperback-wrap.png` |
| Ciltli kapak | `08_OUTPUT/hardcover/cover.pdf` | `re-generated/cover-hardcover-wrap.png` |
| Kindle kapağı | `08_OUTPUT/kindle/cover.jpg` | ciltsiz kapak PDF'inin ön yüzünden rasterize |
| Kindle EPUB | `08_OUTPUT/kindle/book.epub` | yeni kapak gömüldü |

**A+ modülleri DEĞİŞTİRİLMEDİ.** Ölçüldü: on modülün onu da kendi
`07_ASSETS/raw/aplus-*.png` kaynağından üretiliyor; **hiçbiri kapak
sanatından türemiyor**. Talimat § 14 gereği dokunulmadı.

---

## 5. Tipografi değişiklikleri

**Tipografi katmanı yeniden yazılmadı** — Faz 7'de zaten CLI'ya taşınmıştı
ve doğru çalışıyordu. Yeni sanata iki uyarlama yapıldı:

| Değişiklik | Gerekçe |
|---|---|
| **Metin silme hattı tamamen kaldırıldı** (~130 satır) | Yeni sanat metinsiz; silinecek şey yok ve silmek zarar verir |
| **WCAG kontrast ölçümü eklendi** | "Okunuyor mu" bir fikir değil bir sayıdır (§ 6) |
| Yaş rozeti levha rengi `0.86/0.36/0.10` → `0.78/0.30/0.06` | Ölçüm: beyaz yazı 3,78:1 veriyordu; AA-normal eşiği 4,5:1. Şimdi **4,69:1** |

Basılan metinlerin hepsi **CLI ile** üretildi; hiçbiri sanatın parçası değil:

| Yer | Metin |
|---|---|
| Ön kapak | `THE GREAT BOOK OF` / `WORLD MYTHS` |
| Alt başlık | `45 Stories of Gods, Heroes, and Monsters from 22 Cultures` |
| Byline | `Retold for Young Readers` |
| **Yazar** | **`Emre Doğan`** |
| Yaş rozeti | `AGES 8–12` — köşede (yol haritası § 18) |
| Sırt | `THE GREAT BOOK OF WORLD MYTHS` + `Emre Doğan` |
| Arka kapak | tanıtım metni + **`Vâliçe Press`** |
| Barkod alanı | **boş** — hiçbir numara basılmadı |

---

## 6. Yazar adı yerleşimi — ölçülerek çözüldü

Talimat § 7: yazar adı sanatın içinde **kaybolmamalı**, yeterli **kontrasta**
sahip olmalı, başlıkla **yarışmamalı**.

**Bu artık göze bırakılmıyor.** Her yazı kutusunun kendi zeminine karşı
WCAG kontrast oranı ölçülüyor (`covers.measure_contrast`) ve **p10**
(en kötü %10) kapıya bağlı. Ortalama değil p10 kullanılıyor: metnin
%10'u koyu bir buluta düşerse o kısım kaybolur.

| Öğe | Ciltsiz | Ciltli | Eşik |
|---|---:|---:|---|
| Başlık satır 1 | 7.22 | 6.8 | ≥4,5 |
| Başlık satır 2 | 9,56 | 8,23 | ≥4,5 |
| Alt başlık | 11,66 | 10,03 | ≥4,5 |
| Byline | 12,55 | 11,45 | ≥4,5 |
| **YAZAR** | **13.33** | **12.76** | ≥4,5 |
| Yaş rozeti (levha üstünde) | 4,69 | 4,69 | ≥4,5 |

> **Yazar adı 13,33:1 ve 12,73:1 kontrastla basılıyor** — WCAG **AAA**
> eşiği 7:1'dir. Sorun çözüldü ve **sayıyla** kanıtlandı.

### Hiyerarşi

Yazar adı **üst blokta**, başlığın altında, alt başlık ve byline'dan sonra:

```
THE GREAT BOOK OF        ← 57 pt · Lato Black
WORLD MYTHS
45 Stories of Gods…      ← 15,5 pt · Bold
Retold for Young Readers ← 14 pt · Italic
Emre Doğan               ← 21,7 pt · Bold  (başlığın %38'i)
```

Ne sanatın üstünde bir "çip" var, ne de ortada yüzen bir panel. Yazar adı
gökyüzünün temiz bandında duruyor; **çocuğun ve tilkinin üstüne
düşmüyor**. Kutu çakışması **ölçülüyor** ve sıfır.

---

## 7. Ciltsiz geometri

Hepsi **güncel 234 sayfadan** türetildi.

| | Değer |
|---|---|
| Sayfa | **234** (KDP sınırı 24–828) |
| Trim | 6 × 9 inç · normal |
| Taşma | 0,125" |
| **Sırt** | **0,585"** (`234 × 0,0025`) |
| Tam kapak | **12,835 × 9,25 inç** |
| Piksel @300 dpi | 3851 × 2775 |
| PDF sayfa ölçüsü | 924,12 × 666,00 pt ✅ |
| Güvenli alan | 0,25" |
| Barkod bölgesi | 2 × 1,2" · alttan 0,885" · **temiz** |
| Gömülü olmayan font | **0** |
| Zemin kırpma | **%0,10** |
| Etkin çözünürlük | 115 dpi ⚠ |

## 8. Ciltli geometri

| | Değer |
|---|---|
| Sayfa | **234** (KDP sınırı 75–550) |
| **Sırt** | **0,774"** ✅ KDP hesaplayıcısıyla doğrulandı (11 Ağu 2026) |
| Sarım | **0,591"** · Menteşe **0,394"** · Margin **0,125"** |
| Tam kapak | **14,349 × 10,417 inç** |
| Piksel @300 dpi | 4305 × 3125 |
| PDF sayfa ölçüsü | 983,88 × 721,44 pt ✅ |
| Barkod bölgesi | 2 × 1,2" · alttan 1,27" · **temiz** |
| Gömülü olmayan font | **0** |
| Zemin kırpma | **%0,82** (eskiden **%4,38**) |
| Etkin çözünürlük | 106 dpi ⚠ |

> **Yeni sanatın en büyük kazancı burada:** eski ciltli sanat hedef orana
> uzaktı ve kompozisyondan **%4,38 kırpılıyordu**. Yeni sanat 1,365 oranında
> üretildi (hedef 1,364) ve kırpma **%0,10'a** düştü. Kompozisyon artık
> neredeyse hiç kırpılmıyor — talimat § 8'in istediği tam olarak buydu.

✅ **CİLTLİ SIRT DOĞRULANDI** (11 Ağustos 2026) — KDP Cover Calculator
234 sayfa için **0,774 inç** verdi. Türetme 0,645" idi ve 0,129 inç
dardı. `coverspec.py` düzeltildi, kapak yeniden üretildi.

## 9. Kindle ölçüleri

| | Değer |
|---|---|
| Piksel | **1706 × 2560** (KDP önerisi 2560 yükseklik ✅) |
| Oran | 0,666 (hedef 0,667) |
| Dosya | 1,00 MB · RGB JPEG |
| Kaynak | **ciltsiz kapak PDF'inin ön yüzünden rasterize** |

Kindle kapağı ayrı üretilmez: basılı kapakla **birebir aynı tipografiyi**
taşır. Eski rasterize edilmiş kapak **yeniden üretildi**, korunmadı.

**Küçük resim testi** (yol haritası § 18) — 120 · 160 · 260 px:

| | 120 px | 160 px |
|---|---|---|
| `WORLD MYTHS` | ✅ | ✅ |
| `THE GREAT BOOK OF` | ✅ | ✅ |
| `Emre Doğan` | ✅ | ✅ |
| `AGES 8–12` | ✅ | ✅ |

## 10. Arka kapak doğrulaması

| Kontrol | Sonuç |
|---|---|
| Metin kendi kutusunda | ✅ panel **ölçülen metinden** büyür |
| Sırta taşma | ✅ yok |
| Taşma sınırına taşma | ✅ yok |
| Barkod bölgesine girme | ✅ yok |
| Güvenli alan | ✅ ihlal yok |
| Kontrast | ✅ beyaz panel (%88 opak) üstünde koyu lacivert |
| Yayıncı satırı | ✅ **Vâliçe Press** panelin içinde |
| Uydurulmuş pazarlama metni | ✅ **yok** — metin `covers.BACK_COPY`den, envantere karşı sınanmış |

## 11. Sırt doğrulaması

| | Ciltsiz | Ciltli |
|---|---:|---:|
| Sırt genişliği | 0,585" | **0,774"** |
| Yazı puntosu | 17 pt | 21 pt |
| Gereken uzunluk | 406.6 pt | 494.7 pt |
| Kullanılabilir | 612.0 pt | 556.6 pt |
| Pay | **+205 pt** | **+62 pt** |
| Başlık/yazar çakışması | **yok** | **yok** |

KDP kuralı: 100 sayfanın altında sırt yazısı basılmaz. **234 sayfada
basılır.** Sırt düz renk banttır ve yazı **beyazdır** — sanatın üstünde
koyu yazı okunmuyordu (Faz 7 bulgusu). Katlama payı için renk her iki
yana 0,06" yumuşatılarak taşırılır.

## 12. Barkod / ISBN doğrulaması

| Kontrol | Sonuç |
|---|---|
| Kapağa basılan ISBN | **YOK** (`isbnPrinted: false`) |
| Kapağa basılan barkod | **YOK** |
| Barkod bölgesi | **temiz** · 2 × 1,2 inç · KDP belgesinden |
| Uydurulmuş numara | **YOK** — depoda ISBN biçimi taraması da yeşil |
| Strateji | **KDP ücretsiz ISBN** — numara panelde atanır |

Yeni sanatta **uydurulmuş barkod yok** — eski sanatta vardı ve hattın onu
silmesi gerekiyordu. Artık silinecek bir şey yok.

## 13. Sanat bütünlüğü doğrulaması

`04_BUILD/cover_artwork.py` — **her koşuda**, CI dâhil.

| # | Garanti | Nasıl | Kasıtlı kusurla sınandı |
|---|---|---|---|
| ① | **Masterlar değişmedi** | 8 dosyanın sha256'sı manifestoyla karşılaştırılır | ✅ kayıtlı sha bozuldu → yakalandı |
| ② | **Köken doğru** | `covers.py` yalnızca `re-generated/` okur | ✅ |
| ③ | **Yıkıcı hat geri gelemez** | Silme fonksiyonlarının **adı bile** covers.py'de aranır | ✅ var olan bir ad eklendi → yakalandı |
| ④ | Her master **gözle incelendi** | Kayıtsız master → "incelenmemiş sanat" | ✅ |
| ⑤ | Üretim masterları **metinsiz** | Metinli üretim master'ı → HATA | ✅ |

**Doğrulama sonucu:** 8 master · **0 değişiklik** · manifesto eşleşiyor.

`07_ASSETS/raw/re-generated/` **salt okunurdur** ve bu betik oraya yazmaz.
Türetilmiş üretim varlıkları (ölçek, kırpma, renk, format) elbette
dönüştürülür — ama **kaynak dokunulmaz kalır**.

## 14. Eski kapak temizliği

Yeni kapaklar **üretildi, doğrulandı, render edildi ve ölçüldü** — ancak
ondan sonra eski sanat arşive alındı.

```
07_ASSETS/raw/superseded/20260810-cover-regeneration/
├── README.md                          ← neden devre dışı, gerekçesiyle
├── cover-paperback-wrap.png           ← metinli · eski
├── cover-hardcover-wrap.png           ← metinli · eski
├── cover-paperback-front.png
├── cover-back-panel.png
├── cover-front-variant-figures.png
├── cover-front-variant-object.png
└── cover-thumbnail-test.png
```

**Silinmedi.** Denetim izidir: kusurun ne olduğunu ve kararın neden
verildiğini gösteren tek kanıt bunlardır. `07_ASSETS/raw` salt okunurdur
(karar K5).

Korunanlar: yeniden üretilen masterlar · build betikleri · şartnameler ·
tipografi yapılandırması · denetim kayıtları.

## 15. Yapılan testler

| Test | Sonuç |
|---|---|
| `cover_artwork.py --check` | ✅ 8 geçti · 1 uyarı |
| `covers.py` | ✅ 27 geçti · 4 uyarı |
| `package_selftest.py` | ✅ **51/51** (41 → 51, on yeni kasıtlı kusur) |
| `selftest.py` | ✅ **91/91** |
| `asset_inventory.py` | ✅ 18 geçti · 2 uyarı |
| `epub.py` · `handoff.py` | ✅ |
| **`qa_all.sh` (bütün kapılar)** | ✅ **YEŞİL** · kapı `phase5` |

### Yeni kasıtlı kusur testleri

- kayıtlı sha256 bozuldu → **checksum kapısı yakaladı**
- covers.py'de var olan bir ad yasak listeye eklendi → **tarama yakaladı**
- koyu yazı / koyu zemin → **kontrast kapısı reddetti** (WCAG hesabı
  beyaz-siyahta 21:1 veriyor, doğru)
- üretim kapaklarında yazar kontrastı ≥4,5:1 → **ölçülü ve geçti**

### Kalan uyarılar (hepsi bilinen ve gerekçeli)

| Uyarı | Durum |
|---|---|
| Kapak sanatı etkin 115 / 107 dpi | ⚠ **A11 · kurucu kararı** — üreticinin azami çıktısı ~1536 px |
| Ciltli sırt türetilmiş | ⚠ KDP hesaplayıcısıyla doğrulanacak |
| `cover-thumbnail-test.png` metinli | ⚠ üretim varlığı değil · temizi mevcut |
| `cover-thumbnail` şartnamede yok | ⚠ kurucunun eklediği temiz dosya · yetim uyarısı |
| Başlık kontrastı 6,69 (ciltli) | ⚠ AA geçer, AAA'nın (7:1) hemen altında |

## 16. CI sonucu

| İş akışı | Sonuç |
|---|---|
| `validate` | ✅ *(kapak sanatı bütünlüğü adımı eklendi)* |
| `images` | ✅ |
| `build` | ✅ |

Çalışma ağacı temiz · kapı `phase5` · **sürüm etiketi atılmadı** (bu işlem
roadmap'te etiket gerektirmiyor).

## 17. Nihai varlık yolları

```
YETKİLİ SANAT (salt okunur)
  07_ASSETS/raw/re-generated/*.png                8 master · 23,1 MB

ÜRETİM ÇIKTILARI
  08_OUTPUT/paperback/cover.pdf                  26,2 MB · 12,835×9,25"
  08_OUTPUT/hardcover/cover.pdf                  32.5 MB · 14,349×10,417"
  08_OUTPUT/kindle/cover.jpg                      1,0 MB · 1706×2560
  08_OUTPUT/kindle/book.epub                      2,8 MB · kapak gömülü

DENETİM
  06_REPORTS/tracked/cover-artwork-manifest.json  sha256 · gözle karar
  06_REPORTS/tracked/cover-build.json             geometri · kontrast · kutular

ARŞİV
  07_ASSETS/raw/superseded/20260810-cover-regeneration/   eski sanat + README

HAT
  04_BUILD/covers.py            tipografi katmanı (silme hattı KALDIRILDI)
  04_BUILD/cover_artwork.py     bütünlük · köken · yasak fonksiyon
  04_BUILD/coverspec.py         geometri ve şartname
```

### Yeniden üretim komutları

```bash
python3 04_BUILD/cover_artwork.py --check   # masterlar bozulmamış mı
python3 04_BUILD/covers.py                  # üç kapak
python3 04_BUILD/epub.py                    # kapağı EPUB'a göm
python3 04_BUILD/handoff.py                 # teslim belgeleri
./04_BUILD/qa_all.sh                        # bütün kapılar
```

## 18. Kurucuya kalan işler

Bu işlemden **yeni bir kurucu görevi doğmadı**. Devam eden ikisi:

| # | Ne | Neden |
|---|---|---|
| ~~1~~ | ~~Ciltli sırtı doğrula~~ | ✅ **TAMAMLANDI** (11 Ağu 2026): 0,774" |
| 2 | **Kapak çözünürlüğü kararı (A11)** | Etkin 115/106 dpi. Previewer uyaracaktır. Prova kopyası görülmeden karar verilmemeli |

Her ikisi de `KDP_UPLOAD_PLAYBOOK.md` içinde adım adım anlatılmıştır.

---

## Özet

| | |
|---|---|
| **ESKİ SANAT** | **devre dışı** · arşivde · silinmedi |
| **YENİ SANAT** | **yetkili** · `07_ASSETS/raw/re-generated/` · salt okunur |
| **TİPOGRAFİ** | **CLI ile üretildi** · sanat katmanına dokunulmadı |
| **ISBN** | **KDP ücretsiz ISBN** · hiçbir numara uydurulmadı |
| **YAZAR** | **Emre Doğan** · kontrast 13,33:1 / 12,73:1 |
| **YAYINCI** | **Vâliçe Press** |

**Silme hattı kaldırıldı ve geri gelemez.** Sanat katmanına bir daha
dokunulmayacak — bu artık bir niyet değil, üç kapıya bağlı bir mekanizma.
