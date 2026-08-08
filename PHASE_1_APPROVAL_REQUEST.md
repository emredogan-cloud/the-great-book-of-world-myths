# FAZ 1 ONAY TALEBİ

> **Bootstrap tamamlandı. Kitabın tek kelimesi yazılmadı.**
>
> Bu belge kurucudan **Faz 1'i başlatma izni** ister. Faz 1 başlamadan
> kapanması gereken **üç karar** vardır ve onlar olmadan başlamak, sonradan
> geri alınması pahalı işler üretir.
>
> Tarih: 8 Ağustos 2026 · Kapı: `phase0` · Etiket: `v0.0.1`

---

## 1. Ne kuruldu

| Katman | Ne var |
|---|---|
| **Yol haritası** | Beş faz, 24 bölüm, faz başına 19 kalem — tek doğruluk kaynağı |
| **Yaş politikası** | 17 içerik kategorisi, her biri `ALLOW`/`IMPLY`/`OMIT`/`REVIEW` + 10 ölçülebilir eşik |
| **Yazım sistemi** | 8–12 yaş üslubu, dört hareketli hikâye yapısı, ölçülebilir bantlar |
| **Kaynak standardı** | 4 kaynak katmanı, 7 doğrulama seviyesi, çocuk mitolojisine özgü 3 ek kural |
| **Araştırma mimarisi** | Şema + kapılar; hikâye başına 18 zorunlu alan |
| **Kalite kapıları** | 13 betik, 20 kapı — hepsi standart kütüphaneyle, saniyeler içinde |
| **Kapıların testi** | **39 kontrol** — her kapının kusuru gerçekten yakaladığının kanıtı |
| **Görsel hattı** | 68 prompt üretildi, ölçüm kalibre edildi (**hata %0,00**) |
| **KDP modeli** | Yol haritasının **beş maliyet/telif sayısı da birebir doğrulandı** |
| **Sayfa modeli** | Deterministik; **gerçek bir yapısal sorun buldu** (§ 5) |
| **CI/CD** | 4 iş akışı, kapı seviyeli, manuscript sızıntısı korumalı |
| **Depo** | Public, `main`, korumalı |

---

## 2. Faz 1 tam olarak ne yapacak

### Hedef

| Ölçü | Hedef |
|---|---:|
| Kilitlenecek kültür | **22 / 22** |
| Kilitlenecek hikâye | **45 / 45** |
| Aday havuzu | ≥55 hikâye · ≥26 kültür |
| Araştırma kaydı | **45** |
| **Yazılacak hikâye** | **1** (ses kalibrasyon pilotu) |
| Kelime | ~950 |
| Görsel | 0 |

### Neden tam olarak bir hikâye

İki gerekçe, ikisi de mekanik:

**① Ses kalibrasyonu.** `CHILDREN_WRITING_STYLE.md`'nin kalibrasyon örnekleri
**gerçek metinden** gelmek zorundadır. Bu kitabın devralacağı bir çocuk sesi
**yoktur** — yetişkin cildi bilinçli tersidir. Referans projede ilk yazım
partisi cümle uzunluğu hedefini **iki kez ıskaladı**, çünkü ölçüyü ancak
yazdıktan sonra gördü.

**② Sayfa modeli.** Model şu an **kalibre değil**: kelime/sayfa tipografi
tahmininden geliyor. Referans projede dolguyla ölçmek *"modeli modele karşı
sınamak"* olarak kayda geçti ve sayfa bütçesi gerçek metinle **%15**
düzeltildi. Burada aynı riski taşıyoruz ve fiyat modeli o sayıya bağlı.

Bir hikâye ikisini de çözer ve Faz 1'i "yalnızca araştırma" olmaktan çıkarır.

### Faz 1'in bitiş koşulu

**32 ölçülebilir kriterin tamamı** — tam liste
[`THE_GREAT_BOOK_OF_WORLD_MYTHS_MASTER_ROADMAP.md` § 17](THE_GREAT_BOOK_OF_WORLD_MYTHS_MASTER_ROADMAP.md#17-definition-of-done).

Kısmi geçiş yoktur. *"Çoğu tamam"* bir durum değildir.

---

## 3. ⚠ ÜÇ KARAR — Faz 1 bunlar olmadan BAŞLAYAMAZ

### A1 · Manuscript public depoda mı duracak?

**Bootstrap (a) şıkkını varsayarak kurdu ve mekanizmayı yazdı, ama karar
sizindir.**

| Şık | Ne demek |
|---|---|
| **(a)** | Depo public; **proza depo dışında yaşar** ← bootstrap bunu varsaydı |
| (b) | Depo public; proza ayrı private depoda |
| (c) | Depo private; yayından sonra public |

**(a)'nın gerekçesi dört risk:** KDP fiyat eşleştirmesi · kamu malı yanlış
sınıflandırması · intihal / AI eğitim verisi · **ve bu kitaba özgü dördüncü
risk**: metin çocuklara yöneliktir ve bağlamından koparılmış bir sahne
alıntısı (örneğin bir kurban anlatısı) sosyal medyada kitabın aleyhine
kullanılabilir.

Mekanizma zaten kuruldu ve **kasıtlı bir sızıntıyla sınandı**: iki hatlı
koruma (yol kalıbı + içerik taraması) çalışıyor. Karar (b) veya (c) olursa
mekanizma değişmez, yalnızca kurallar değişir.

> **Onayınız:** (a) · (b) · (c)

---

### A2 · 22 kültürün listesi

Yol haritası **altısını adıyla** sayıyor ve bunlar kilitli:
**Kore · İnuit · Polinezya · Batı Afrika · Fars · Türk**

Kalan **16 slot** yol haritasında tanımlı değil. Bootstrap 23 aday listeledi
ve **hiçbirini karar saymadı** — hepsi `status: "candidate"`.

Faz 1 bunları araştırıp kilitleyecek. Sizden istenen: **aday listesini
gözden geçirmek** ve varsa eklemek/çıkarmak.

İki aday özel dikkat istiyor:

| Aday | Sorun |
|---|---|
| **Diné (Navajo)** | Anlatıların çoğu **mevsime ve anlatıcıya bağlıdır**; yayımlanmış olması kullanılabilir olduğu anlamına gelmez. Kısıtlılık taraması bunu düşürebilir. |
| **Polinezya** | Bir kültür değil bir kültür **ailesidir**. Tek kayıt mı (Māori/Hawaiʻi ağırlıklı), iki ayrı kayıt mı? İkisi 22 slotun ikisini kullanır. |

Ayrıca: yol haritası **"Batı Afrika"** diyor, ama üslup kılavuzu
genellemeyi yasaklıyor (*"Afrikalılar…" değil, "Yoruba anlatıcıları…"*).
Kaydı **Yoruba** ve/veya **Akan** olarak daraltmak kitabı **güçlendirir**
ama iki slot kullanır.

> **Onayınız:** aday listesi uygun mu? Polinezya ve Batı Afrika kayıtları
> daraltılsın mı?

---

### A3 · 45 hikâyenin dağılımı

Yol haritası 45 sayısını veriyor, hikâyeleri **saymıyor**. Bootstrap
hiçbirini uydurmadı — `story_index.json` **kasıtlı olarak boştur**.

Faz 1'in birinci işi bu. Bootstrap'ın **önerdiği** iki kısıt var ve bunlar
yol haritasının kararı değil:

- Hiçbir kültür **4'ten fazla** hikâye almasın — aksi hâlde kitap gizlice
  "5 kültür + ekler" kitabına döner
- **Yunan payı en fazla 3** — kitabın varlık sebebi rafın %80 Yunan olması

Şu an **uyarı** olarak çalışıyorlar. Onaylarsanız **hataya** çevrilir.

> **Onayınız:** iki kısıt kapıya bağlansın mı?

---

## 4. ⚠ Bir insan bağımlılığı şimdiden planlanmalı

### A8 · İki ebeveyn okuyucusu

Yol haritasının **kendi cümlesi**, R2 (yaş uygunluğu) riskinin azaltması:

> *"Azaltma: yazım öncesi `AGE_POLICY.md`; **yayından önce en az iki
> ebeveyn okuması**."*

Birinci parça bu bootstrap'ta yapıldı. İkincisi **iki gerçek insandır** ve
CI ile üretilemez. Faz 5 kapısında `03_EDITORIAL/PARENT_READINGS.md`
dosyasında iki imzalı okuma kaydı aranır; yoksa sürüm çıkmaz.

**Şimdi planlamanız gerekiyor**, Faz 4'te değil: iki kişi bulmak zaman alır
ve okuma 45 hikâyeyi kapsayacak.

---

## 5. Bootstrap'ın bulduğu iki şey

Bunlar tahmin değil, çalışan koddan çıktı.

### ① Ticari model doğrulandı — beş sayı da birebir

`04_BUILD/editions.py` KDP'nin resmî tablolarından yol haritasının verdiği
**her sayıyı** yeniden üretti:

| | Formül | Sonuç | Yol haritası |
|---|---|---:|---:|
| Ciltsiz maliyet | 1,00 $ + 0,012 × 230 | 3,76 $ | 3,76 $ ✓ |
| Ciltsiz telif | 16,99 × %60 − 3,76 | 6,43 $ | 6,43 $ ✓ |
| Ciltli maliyet | 5,65 + 0,012 × 230 | 8,41 $ | 8,41 $ ✓ |
| Ciltli telif | 26,99 × %60 − 8,41 | 7,78 $ | 7,78 $ ✓ |
| Kindle telif | 7,99 × %70 − teslim | 5,14 $ | 5,14 $ ✓ |

Ve **bir sayı türetti**: yol haritasında yazmayan **Kindle dosya bütçesi
3,0 MB**. 5,14 $ telif rakamından geriye hesaplandı. Bu bütçe aşılırsa
telif her satılan kopyada düşer; görsel hattı artık bu sayıya göre optimize
ediyor (mevcut projeksiyon: **1,08 MB** — rahat).

### ② Sayfa hedefi yapısal olarak ulaşılamaz — ve çözümü var

`04_BUILD/page_budget.py` şunu buldu: **230 sayfa, varsayılan yapıyla
ulaşılamaz.**

Sebep aritmetik değil yapısal. Her hikâye yeni sayfada başlar ve yukarı
yuvarlanır, bu yüzden hikâye başına maliyet **3 ↔ 4 sayfa arasında zıplar**:

| Ulaşılabilir toplam | Hikâye/sayfa | Hedeften |
|---:|---:|---:|
| 204 | 3 | −26 |
| **250** | 4 | **+20** ← varsayılan model |
| 294 | 5 | +64 |

**Tipografiyi ayarlamak bu boşluğu açmaz.** İki yapısal seçenek açar:

| Seçenek | Kültür kartı | Hikâye/sayfa | Toplam | Ciltsiz telif |
|---|---:|---:|---:|---:|
| **(a′)** kültür kartı **açık sayfa** | 2 sayfa | 3 | **226** | **6,48 $** |
| (b′) vinyet başlıkta, kart yok | 0 | 4 | 228 | 6,46 $ |
| — varsayılan | 1 sayfa | 4 | 250 | 6,19 $ |

**Öneri (a′).** Kültür kartını açık sayfa yapmak vinyeti, harita işaretini
ve üç cümleyi rahat taşır; (b′) 22 vinyetin görünürlüğünü yok eder ve yol
haritasının illüstrasyon bütçesini gerekçesiz bırakır.

**Fark: kopya başına +0,29 $** (250 → 226 sayfa).

> ⚠ Model **kalibre değil** — bu yüzden karar **Faz 1'in gerçek dizgi
> ölçümünden sonra** verilmeli. Şimdi karar vermeniz gerekmiyor; **bilmeniz**
> gerekiyor, çünkü Faz 1'in pilot hikâyesi tam olarak bu ölçümü üretecek.

---

## 6. Riskler — Faz 1'e özgü

| # | Risk | Azaltma |
|---|---|---|
| 1 | **Kısıtlılık taraması bir kültürü düşürür** ve 22 tutmaz | Aday havuzu ≥26; 22 alt başlıkta yazdığı için düşürülemez, yerine başkası gelir |
| 2 | **Pilot hikâye sesi yanlış kurar** ve 45 hikâye yanlış tonda yazılır | Faz 2 kurucu onayı olmadan başlamaz; pilot beğenilmezse **yeniden yazılır** |
| 3 | **Sayfa modeli kalibre edilince tablo değişir** | Model deterministik; her koşuda yeniden üretilir ve fark dolar cinsinden basılır |
| 4 | **45 hikâye için yeterli doğrulanmış kaynak bulunamaz** | ≥55 aday şartı; kaynağı olmayan hikâye listeye alınmaz |
| 5 | **Telaffuz kaynağı bulunamaz** | Kaynağı olmayan telaffuz yazılmaz; ad değişir veya hikâye değişir |

---

## 7. Faz 1'in beklenen çıktıları

```
01_RESEARCH/culture_index.json        22 kültür "locked", kısıtlılık taraması tamam
01_RESEARCH/story_index.json          45 hikâye "locked", ≥55 aday
01_RESEARCH/research/*.md             45 üretilmiş araştırma kaydı
00_CONTEXT/CHILDREN_WRITING_STYLE.md  3 GERÇEK ses kalibrasyon paragrafı
00_CONTEXT/EDITORIAL_ARCHITECTURE.md  A4 ve A5 karara bağlanmış
03_EDITORIAL/AGE_REVIEW_LOG.md        REVIEW kategorili hikâyelerin kaydı
02_MANUSCRIPT/book.json               1 hikâye (DEPO DIŞINDA)
06_REPORTS/tracked/page-calibration.json  gerçek dizgiyle ölçülmüş sayfa modeli
CHANGELOG.md                          [0.1.0] bloğu
.gate                                 phase1
etiket                                v0.1.0
```

---

## 8. Onayınızı istediğimiz şey

- [ ] **A1** — manuscript nerede duracak: **(a)** / (b) / (c)
- [ ] **A2** — 22 kültür aday listesi uygun mu? Polinezya ve Batı Afrika
      kayıtları daraltılsın mı?
- [ ] **A3** — "kültür başına ≤4 hikâye" ve "Yunan ≤3" kısıtları kapıya
      bağlansın mı?
- [ ] **`AGE_POLICY.md` onayı** — 17 kategorinin seviyeleri kabul mü?
      *(Yol haritası bunu yazım öncesi şart koşuyor.)*
- [ ] **A8** — iki ebeveyn okuyucusunu bulma işi başlasın mı?
- [ ] **Faz 1 başlasın mı?**

---

## 9. Şu anki durum

```
FAZ 0 · BOOTSTRAP           ████████████████  TAMAM
FAZ 1 · TEMEL               ░░░░░░░░░░░░░░░░  ONAY BEKLİYOR
FAZ 2 · ÇEKİRDEK YAZIM      ░░░░░░░░░░░░░░░░
FAZ 3 · GENİŞLEME           ░░░░░░░░░░░░░░░░
FAZ 4 · TAMAMLAMA           ░░░░░░░░░░░░░░░░
FAZ 5 · ÜRETİM              ░░░░░░░░░░░░░░░░

Yazılmış hikâye: 0 / 45
Kilitli kültür : 6 / 22   (6'sı yol haritasınca zorunlu)
Görsel         : 0 / 68
```

---

## ⛔ PHASE 1 NOT STARTED — FOUNDER APPROVAL REQUIRED

**Faz 1 BAŞLAMADI. Kurucu onayı gerekiyor.**

Hiçbir hikâye araştırılmadı. Hiçbir hikâye yazılmadı. Hiçbir görsel
üretilmedi. Hiçbir KDP dosyası oluşturulmadı.

Kurulmuş olan tek şey, Faz 1'in **güvenle başlayabilmesi** için gereken
sistemdir.
