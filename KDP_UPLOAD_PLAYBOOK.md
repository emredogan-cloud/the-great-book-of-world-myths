# KDP YÜKLEME EL KİTABI — The Great Book of World Myths

> **Bu belge kurucu içindir ve düğme düğme yazılmıştır.**
>
> Üç format, üç ayrı yükleme: **Kindle e-kitap · Ciltsiz · Ciltli.**
> Üçü de aynı KDP hesabından, aynı "Kitap Rafı"nda ama **ayrı kayıtlar**
> olarak yaşar.
>
> ⚠ **ARAYÜZ DEĞİŞİR.** Aşağıda iki işaret kullanılıyor:
>
> | İşaret | Anlamı |
> |---|---|
> | 🟢 **MEVCUT** | Ağustos 2026 itibarıyla panelde görülmüş hâli |
> | 🟡 **DEĞİŞEBİLİR** | Amazon bu etiketi/konumu haber vermeden değiştirir — **panelde teyit edin** |
>
> Bir etiket bulamazsanız **tahmin etmeyin**: KDP yardım sayfasında arayın
> veya ekran görüntüsüyle kayıt açın. Yanlış bir kutu, yayını günlerce
> geciktirebilir.
>
> Son güncelleme: 8 Ağustos 2026 · Faz 5'te yeniden doğrulanacak

---

## 0. Yüklemeden önce — hazırlık kontrol listesi

Bunlar **elinizde olmadan** panele girmeyin.

| # | Ne | Nereden |
|---:|---|---|
| 1 | `08_OUTPUT/kindle/book.epub` (≤ **3,0 MB**) | `build.yml` |
| 2 | `08_OUTPUT/paperback/interior.pdf` | `build.yml` |
| 3 | `08_OUTPUT/paperback/cover.pdf` | Faz 5 kapak |
| 4 | `08_OUTPUT/hardcover/interior.pdf` | `build.yml` |
| 5 | `08_OUTPUT/hardcover/cover.pdf` | Faz 5 kapak |
| 6 | `08_OUTPUT/kindle/cover.jpg` (en az 2560 px yükseklik) | Faz 5 kapak |
| 7 | `08_OUTPUT/metadata.json` — başlık, alt başlık, açıklama, 7 anahtar kelime, kategoriler | Faz 5 metadata |
| 8 | Doğrulama raporları — **hepsi yeşil** | `qa_all.sh` |
| 9 | Vergi bilgisi (W-8BEN) tamamlanmış | KDP hesap ayarları |
| 10 | Banka bilgisi girilmiş | KDP hesap ayarları |

**Sayfa sayısı teyidi:** ciltli KDP'de **75–550 sayfa** arası olmak
zorundadır. `04_BUILD/page_budget.py` çıktısındaki "FATURALANAN" sayısı bu
aralıkta değilse **yüklemeye başlamayın**.

---

## 1. Ortak metadata — üç formatta da AYNI yazılır

Bir kelimesi bile farklı olursa Amazon üç kaydı **aynı ürün sayfasında
birleştirmez** ve serinin gücü kaybolur.

| Alan | Değer | Sınır |
|---|---|---|
| **Book Title** | `The Great Book of World Myths` | 200 karakter |
| **Subtitle** | `45 Stories of Gods, Heroes, and Monsters from 22 Cultures — Retold for Young Readers` | 200 karakter |
| **Series** | `The Great Book of…` 🟡 | — |
| **Author** | *(Codex serisiyle **aynı ad**)* | — |
| **Publisher** | *(A9 kararına göre)* | — |
| **Language** | English | — |
| **Age range** | **8–12** | — |
| **Grade range** | 3–7 🟡 | — |

> **Alt başlıktaki "(Ages 8–12)"** — yol haritasının verdiği tam alt başlık
> bunu içerir, ama KDP'nin **ayrı bir yaş aralığı alanı** vardır ve orada
> zaten seçilir. Alt başlıkta da tekrarlamak 200 karakterden yer yer ve
> Amazon bazı kategorilerde tekrarı gereksiz bulur.
> **Karar Faz 5'e bırakılmıştır** — iki biçim de yol haritasına uygundur.

### Yedi anahtar kelime

Her kutu **50 karakter**. Başlıkta geçen kelimeyi tekrarlamak **slot
israfıdır** — Amazon başlığı zaten indeksler.

Kutular Faz 5'te `04_BUILD` metadata aracıyla doldurulur ve karakter
sayımı orada denetlenir.

### Kategoriler

Format başına **3** kategori (e-kitap 3 + ciltsiz 3 = 6 raf).

> ⚠ Nisan 2026'da 958 yeni kategori eklendi ve **büyük kısmı düşük
> trafiklidir**. Küçük ama gerçekten okur trafiği olan kategoriler seçilir;
> yeni eklenenlerin çoğu tuzaktır.

---

## 2. KINDLE E-KİTAP — 27 adım

### Açılış

**1.** Tarayıcıda `https://kdp.amazon.com` adresine gidin ve giriş yapın.

**2.** Üst menüden 🟢 **Bookshelf** (Kitap Rafı) sekmesine tıklayın.

**3.** 🟢 **+ Create** düğmesine tıklayın.
> 🟡 Bu düğme bazı hesaplarda **"Create a New Title"** yazar.

**4.** Açılan seçeneklerden 🟢 **Kindle eBook** kutusuna tıklayın.

### Kindle eBook Details sayfası

**5. Language** — açılır listeden **English** seçin.

**6. Book Title** — `The Great Book of World Myths`
> Kopyala–yapıştır kullanın. Elle yazmak tire ve kesme farkı üretir.

**7. Subtitle** — `45 Stories of Gods, Heroes, and Monsters from 22 Cultures — Retold for Young Readers`
> ⚠ Uzun tire **em dash (—)** olmalı, kısa tire değil.

**8. Series** 🟡 — "This book is part of a series" kutusunu işaretleyin ve
seri adını girin.
> İlk kitap olduğu için seri numarası **1**.

**9. Edition Number** — boş bırakın (ilk baskı).

**10. Author** — Primary Author alanına yazar adını girin.
> Codex serisiyle **birebir aynı** yazılmalı; farklı yazılırsa Amazon iki
> ayrı yazar sayfası oluşturur ve backlist etkisi kaybolur.

**11. Contributors** — bu kitapta yok. Boş bırakın.
> 🟡 İllüstratör olarak kendinizi eklemek isterseniz "Illustrator" rolü
> seçilebilir; **AI beyanı ayrıca yapılır** ve bu alan onun yerine geçmez.

**12. Description** — ürün açıklamasını yapıştırın (4000 karakter).
> 🟢 Panel basit HTML kabul eder: `<b>`, `<i>`, `<br>`, `<ul>`.
> İlk **iki satır** kritiktir — "Read more" katlanmadan önce görünen kısım.

**13. Publishing Rights** — 🟢 **"I own the copyright and I hold the
necessary publishing rights"** seçeneğini işaretleyin.

**14. Primary Audience** 🟡
- "Is this book intended for children ages 12 and under?" → **Yes**
- **Minimum age: 8** · **Maximum age: 12**
- 🟡 Bazı hesaplarda burada ayrıca **Grade Range** çıkar → 3–7

**15. Keywords** — yedi kutuyu doldurun (her biri ≤50 karakter).

**16. Categories** — 🟢 **Choose categories** düğmesine tıklayın, üç kategori
seçin, **Save** deyin.

**17. AI Content Disclosure** 🟢 — **ZORUNLU.**
> Ekran şunu sorar: *"Did you use AI-based tools in creating this content?"*
>
> Bu kitapta **metin ve görsel** için AI kullanıldı:
> - **Text: Yes → AI-generated (with substantial human editing)** 🟡
> - **Images: Yes → AI-generated** 🟡
> - **Translation: No**
>
> ⚠ **AI destekli** (fikir, dilbilgisi, düzeltme) beyan gerektirmez;
> **AI ile üretilmiş** metin ve görsel **gerektirir**. 2026'da denetim
> başlık düzeyinden **hesap düzeyine** çıktı — yanlış beyan hesabı riske
> atar. Beyanın ekran görüntüsünü alın ve `09_ARCHIVE/` altına koyun.

**18. Pre-order** — bu yüklemede **"I am ready to release my book now"**.
> Ön sipariş kullanılacaksa yayın tarihi seçilir; ama ön siparişte
> **dosya değiştirme penceresi kapanır** (yayından 3 gün önce). İlk
> kitapta önerilmez.

**19.** Sayfanın altındaki 🟢 **Save and Continue** düğmesine basın.

### Kindle eBook Content sayfası

**20. Manuscript** — 🟢 **Upload eBook manuscript** düğmesine tıklayın ve
`08_OUTPUT/kindle/book.epub` dosyasını seçin.
> Yükleme sonrası "Upload and conversion successful" mesajını bekleyin.
> Hata verirse dosya boyutunu kontrol edin: **≤3,0 MB**.

**21. Kindle eBook Cover** — 🟢 **Upload your cover file** seçin ve
`08_OUTPUT/kindle/cover.jpg` dosyasını yükleyin.
> ⚠ **KDP Cover Creator KULLANMAYIN.** Kapak geometrisi bizim hattımızdan
> deterministik olarak üretiliyor.

**22. Kindle eBook Preview** — 🟢 **Launch Previewer** düğmesine tıklayın.

Previewer'da **sırayla** kontrol edin:

| # | Kontrol | Ne aranıyor |
|---:|---|---|
| a | **İçindekiler** | Tıklanabilir mi? 45 hikâye + kültür kartları görünüyor mu? |
| b | **Bölüm geçişleri** | Her hikâye yeni sayfada mı başlıyor? |
| c | **İllüstrasyonlar** | 68 görselin hepsi yerinde mi? Bulanık var mı? |
| d | **Dünya haritası** | Okunuyor mu? Kindle'da tek sayfaya sığmış mı? |
| e | **Telaffuz rehberi tablosu** | Tablo bozulmamış mı? |
| f | **Özel karakterler** | Väinämöinen · Ọ̀ṣun · Māui doğru görünüyor mu? |
| g | **Font** | Gömülü font uyarısı var mı? |
| h | **Tablet · telefon · e-ink** | Üç cihaz görünümünde de kontrol edin |

> Previewer'ın üstünde 🟡 **sarı uyarı şeridi** çıkabilir. **Hiçbirini
> görmezden gelmeyin** — her uyarıyı not alın ve düzelten commit'i hatta
> geri besleyin.

**23.** 🟢 **Book Preview'dan çıkın** ve **Save and Continue**.

### Kindle eBook Pricing sayfası

**24. KDP Select** 🟡 — kutuyu **işaretlemeyin**.
> Yol haritası: münhasırlık ileride kanalları kapatır. **İstisna:** çocuk
> kitabı için KU **test olarak** denenebilir — ama bu karar **yayından
> sonra**, ilk 90 günün verisiyle verilir (`DECISIONS.md` § A7).

**25. Territories** — 🟢 **"All territories (worldwide rights)"**.

**26. Royalty and Pricing**
- 🟢 **70%** seçeneğini işaretleyin
- **Amazon.com** fiyatı: **7.99** USD
- Diğer pazarlar "based on US price" ile otomatik dolar — **kontrol edin**
- Ekranda görünen **Royalty** sütununda beklenen değer: **~5,14 $**

> ⚠ Royalty 5,14 $'ın **belirgin altındaysa** dosya boyutu bütçeyi aşmış
> demektir. Teslim ücreti 0,15 $/MB'dir. Yükleme sayfasına dönüp EPUB'ı
> yeniden optimize edin — `04_BUILD/convert_images.py`.

**27. Terms & Publish**
- 🟢 **Book Lending** kutusu %70'te otomatik işaretlidir; bırakın.
- Sayfanın altında 🟢 **Publish Your Kindle eBook** düğmesine basın.

> Yayın **72 saate kadar** sürebilir. Bu sürede "In Review" durumundadır.

**Son adım:** Kayıt tamamlandıktan sonra ürün sayfasının URL'sini,
ASIN'ini ve AI beyan ekranının görüntüsünü `08_OUTPUT/kdp-state.md`
dosyasına yazın.

---

## 3. CİLTSİZ (PAPERBACK) — 27 adım

**1–4.** Bookshelf → 🟢 **+ Create** → 🟢 **Paperback**.

> ⚠ **Kindle kaydını "Create Paperback" bağlantısıyla açarsanız** metadata
> otomatik kopyalanır ve iki kayıt bağlanır. 🟡 Bu bağlantı Kindle
> kaydının satırında **"+ Create paperback"** olarak görünür. **Bu yol
> tercih edilir** — metadata farkı riskini sıfırlar.

**5–19.** Metadata alanları Kindle ile **birebir aynı** doldurulur
(§ 2 · adım 5–19). Farklar:

**Ek 1 · ISBN** (Paperback Content sayfasında)
- 🟢 **"Get a free KDP ISBN"** → Publisher alanı *Independently published*
  olur
- veya 🟢 **"Use my own ISBN"** → kendi ISBN'inizi girin
> Karar `DECISIONS.md` § A9'da açıktır. Okul/kütüphane kanalı hedefleniyorsa
> **kendi ISBN'iniz** anlamlıdır.
> ⚠ **ISBN bir kez atandıktan sonra değiştirilemez.**

**Ek 2 · Print Options**
- **Ink and Paper Type**: 🟢 **Black & white interior with cream paper**
- **Trim Size**: 🟢 **6 x 9 in (15.24 x 22.86 cm)**
> ⚠ 6×9 **normal trim**'dir. Yanlış trim seçmek baskı maliyetini ve iç
> marj gereksinimini değiştirir.
- **Bleed Settings**: 🟢 **No Bleed**
> İç blokta tam sayfa taşan görsel **yoktur**; açılış illüstrasyonları
> metin bloğunun içinde durur.
- **Paperback cover finish**: 🟢 **Matte** 🟡
> Çocuk kitabı rafında mat kapak daha "kitap" görünür ve parmak izi
> tutmaz. Parlak (glossy) daha canlı görünür. Prova kopyasında ikisini
> de görmeden karar vermeyin.

**20. Manuscript** — 🟢 **Upload paperback manuscript** →
`08_OUTPUT/paperback/interior.pdf`

**21. Book Cover** — 🟢 **Upload a cover you already have (print-ready PDF)**
→ `08_OUTPUT/paperback/cover.pdf`

**22. Launch Previewer** — 🟢 **Launch Previewer**.

Baskı önizlemesinde **sırayla**:

| # | Kontrol | Ne aranıyor |
|---:|---|---|
| a | **Sayfa sayısı** | Panelde görünen sayı `page_budget.py` çıktısıyla aynı mı? |
| b | **İç marj (gutter)** | Metin cilde giriyor mu? 230 sayfada asgari **0,500"** |
| c | **Dış marj** | Kesim çizgisine en az 0,25" var mı? |
| d | **Taşma** | "No bleed" seçildi; kenara değen görsel **olmamalı** |
| e | **İllüstrasyon yerleşimi** | 45 açılış üst yarıda mı? Kaymış olan var mı? |
| f | **Kültür kartları** | Açık sayfa doğru tarafta mı (sol = vinyet)? |
| g | **Dünya haritası** | İki sayfaya doğru yayılmış mı? Cilt payında kayıp var mı? |
| h | **Sayfa numaraları** | Boş sayfalarda numara var mı? (olmamalı) |
| i | **Font** | 🟡 "Fonts are not embedded" uyarısı var mı? **Varsa DURUN** |
| j | **Kapak** | Sırt yazısı ortada mı? Barkod alanı boş mu? |

> **Sırt genişliği sayfa sayısına bağlıdır.** Sayfa sayısı değişirse kapak
> **yeniden üretilmelidir** — eski kapak sırtı kaydırır.

**23.** Previewer'dan çıkın → **Approve** → **Save and Continue**.

**24. Territories** — 🟢 **All territories**.

**25. Pricing**
- **Amazon.com** fiyatı: **16.99** USD
- Ekranda görünen **Royalty**: beklenen **~6,43 $**
- **Printing cost** sütunu: beklenen **~3,76 $**

> ⚠ Bu iki sayı `04_BUILD/editions.py` çıktısıyla **birebir** tutmalıdır.
> Tutmuyorsa sayfa sayısı modelden farklı çıkmış demektir — dosyayı
> yüklemeden önce `page_budget.py`'yi yeniden koşturun.

**26. Expanded Distribution** 🟡 — kutuyu **işaretleyin**.
> Telif %40'a düşer ama **kütüphane ve okul kanalı** buradan geçer ve bu
> kitap tam olarak o kanalı hedefliyor.

**27.** 🟢 **Publish Your Paperback Book**.

> ⚠ **Yayınlamadan önce prova kopyası sipariş edin.** Panelde
> 🟢 **"Order Author Copies"** bağlantısı vardır. Ekranda gördüğünüz ile
> elinizdeki kâğıt aynı şey değildir — özellikle siyah-beyaz çizgi
> illüstrasyonlarda.

---

## 4. CİLTLİ (HARDCOVER) — 27 adım

> **"Ciltli" ve "Hardcover" AYNI FORMATTIR.** İkinci bir üretim hattı
> yoktur; aynı iç blok, farklı kapak geometrisi.

**1–4.** Bookshelf → Ciltsiz kaydının satırında 🟡 **"+ Create hardcover"**
bağlantısına tıklayın.
> Bu yol metadata'yı kopyalar. Bulamazsanız **+ Create → Hardcover**.

**5–19.** Metadata **birebir aynı**.

**Ek · ISBN** — 🟢 Ciltli **AYRI BİR ISBN** ister. Ciltsizin ISBN'i
kullanılamaz.

**Ek · Print Options**
- **Ink and Paper**: 🟢 **Black & white interior with cream paper**
- **Trim Size**: 🟢 **6 x 9 in**
- **Bleed**: 🟢 **No Bleed**
- **Cover finish**: 🟢 **Case Laminate** (ciltlide tek seçenek)

> ⚠ **KDP ciltlide STANDART RENKLİ SUNMAZ.** Bu kitap zaten siyah-beyaz.
> ⚠ **Sayfa sınırı 75–550.** 230 sayfa güvenli aralıkta.

**20. Manuscript** — `08_OUTPUT/hardcover/interior.pdf`
> İç blok ciltsizle **aynı içeriktir** ama kapak geometrisi farklı olduğu
> için ayrı üretilir.

**21. Book Cover** — `08_OUTPUT/hardcover/cover.pdf`

> ⚠ **Ciltli kapak "sarım" (wrap) taşır**: kapak kartonun etrafına dolanıp
> içeri yapışır. Kesim payı ciltsizden **farklıdır** ve KDP'nin ciltli
> şablonundan ölçülür. Ciltsiz kapağı ciltliye yükleyemezsiniz.

**22. Launch Previewer** — ciltsizdeki a–j kontrollerine **ek olarak**:

| # | Kontrol | Ne aranıyor |
|---:|---|---|
| k | **Sarım payı** | Ön kapaktaki görsel/yazı sarıma giriyor mu? |
| l | **Menteşe (hinge) bölgesi** | Sırt yanındaki canlı içerik güvenli bantta mı? |
| m | **Başlık bandı** 🟡 | 120 sayfa üstünde KDP başlık bandı (head band) ekler |
| n | **Karton payı (square)** | Kapak iç bloktan taşıyor — kesim doğru mu? |

**23.** Approve → Save and Continue.

**24. Territories** — All territories.

**25. Pricing**
- **Amazon.com** fiyatı: **26.99** USD
- Beklenen **Royalty**: **~7,78 $**
- Beklenen **Printing cost**: **~8,41 $**

**26. Expanded Distribution** — 🟡 Ciltlide bu seçenek **bulunmayabilir**.
Varsa işaretleyin.

**27.** 🟢 **Publish Your Hardcover Book**.

---

## 5. Yayın sonrası — ilk 72 saat

| # | Ne | Ne zaman |
|---:|---|---|
| 1 | Üç kaydın da **"Live"** olduğunu doğrulayın | 72 saat içinde |
| 2 | Üçünün **aynı ürün sayfasında** birleştiğini kontrol edin | Live olunca |
| 3 | Birleşmediyse KDP desteğine "link formats" talebi açın | 🟡 |
| 4 | **İndeksleme testi**: alt başlıktaki tam öbeği Amazon'da aratın | 48 saat sonra |
| 5 | Yazar sayfasında (Author Central) kitabın göründüğünü doğrulayın | 1 hafta |
| 6 | "Look Inside" açıldığında **gerçek bir illüstrasyon** görünüyor mu | Live olunca |
| 7 | Prova kopyasını elde tutun ve okuyun | yayından önce |
| 8 | KDP durumunu `08_OUTPUT/kdp-state.md` dosyasına kaydedin | hemen |

**Madde 6 önemlidir:** yol haritasının R4 (iade oranı) azaltması tam olarak
budur — *"'Look Inside' örneğinde **gerçek** bir bölüm açılışı ve **gerçek**
bir illüstrasyon."*

---

## 6. Kaydedilecek son durum

`08_OUTPUT/kdp-state.md` dosyasına:

```markdown
# KDP DURUMU — <tarih>

| Format | ASIN / ISBN | Fiyat | Telif | Durum | URL |
|---|---|---|---|---|---|
| Kindle    |  | 7,99 $  | 5,14 $ | Live |  |
| Ciltsiz   |  | 16,99 $ | 6,43 $ | Live |  |
| Ciltli    |  | 26,99 $ | 7,78 $ | Live |  |

## AI beyanı
- Metin: <beyan> · ekran görüntüsü: 09_ARCHIVE/ai-disclosure-<tarih>.png
- Görsel: <beyan>
- Çeviri: Hayır

## Previewer uyarıları
<hepsini yazın — görmezden gelinen uyarı yoktur>

## Yüklenen dosyaların sürümü
git etiketi: v1.0.0 · commit: <sha>
```

---

## 7. Sık yapılan hatalar

| Hata | Sonuç | Önlem |
|---|---|---|
| Üç formatta metadata'nın **bir kelimesi** farklı | Kayıtlar birleşmez, serinin gücü kaybolur | Kopyala–yapıştır; "+ Create paperback/hardcover" yolunu kullanın |
| Sayfa sayısı değişti, **kapak yenilenmedi** | Sırt kayar, baskı reddedilir | Sayfa sayısı değişirse kapağı **yeniden üretin** |
| **Gömülü olmayan font** | KDP reddeder | `build.yml` pdffonts denetimi; Previewer uyarısını okuyun |
| EPUB **3,0 MB'ı aştı** | Teslim ücreti telifi yer | `convert_images.py` ile yeniden optimize edin |
| Ciltsiz kapağı **ciltliye** yüklemek | Sarım payı tutmaz | İki ayrı kapak dosyası üretilir |
| **AI beyanı** atlandı veya yanlış | Hesap düzeyinde risk | Adım 17 zorunlu; ekran görüntüsü alın |
| **KDP Select** yanlışlıkla işaretlendi | 90 gün münhasırlık | Adım 24'te kutuyu işaretlemeyin |
| Prova kopyası **görülmeden** yayın | Baskıda görünmeyen kusur | "Order Author Copies" zorunlu adımdır |
| Yaş aralığı **girilmedi** | Kitap yanlış rafta çıkar | Adım 14: 8–12 |
| Kendi ISBN'i, **yanlış formata** atandı | Geri alınamaz | Her formatın ISBN'i AYRIDIR |

---

## 8. Bu belge nasıl güncellenir

KDP arayüzü değiştiğinde:

1. Değişen adımı bulun ve 🟡 işaretini 🟢'ye çevirin (veya tersi)
2. Ekran görüntüsünü `09_ARCHIVE/kdp-ui/<tarih>/` altına koyun
3. `CHANGELOG.md`'ye bir satır ekleyin
4. Değişiklik bir **kararı** etkiliyorsa `DECISIONS.md`'ye `K##` yazın

> **Tahmin etmeyin.** Bir etiketi bulamıyorsanız, bulamadığınızı yazın ve
> KDP yardım sayfasında arayın. Bu belgenin değeri **doğru olmasındadır**,
> eksiksiz görünmesinde değil.
