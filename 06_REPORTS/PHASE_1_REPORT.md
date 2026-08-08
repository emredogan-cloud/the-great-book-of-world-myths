# FAZ 1 TAMAMLANMA RAPORU — Temel

> **Kapsam kilitlendi. Ses ve sayfa modeli gerçek metinle kalibre edildi.**
>
> Kapı: `phase1` · Etiket: `v0.1.0` · CI: **YEŞİL** · 8 Ağustos 2026
>
> Durum: **FAZ 1 TAMAM — FAZ 2 KURUCU ONAYINI BEKLİYOR**

---

## 1. Kapsam kararları

| Karar | Sonuç |
|---|---|
| **A1 → K21** | Manuscript depo **dışında** yaşar (şık *a*) |
| **AGE_POLICY → K22** | On yedi kategori **kurucu onaylı** — pilot yazılmadan önce |
| **A2 → K23** | 22 kültür kilitlendi; Polinezya → **Māori + Hawai'i**, Batı Afrika → **Yoruba + Akan** |
| **A3 → K24** | "kültür ≤4" ve "Yunan ≤3" artık **hata**, uyarı değil |
| **A3 → K25** | 45 hikâye kilitlendi |
| **A5 → K26** | Bölüm mimarisi **bölgesel** (altı bölge) |
| **A4 → K27** | Kültür kartı **hikâye kuyruğundaki boşlukta** — ölçümle verildi |

### K23 neden önemli

Yol haritası altı geleneği adıyla sayar. İkisi **kültür adı değildi**:
*Polinezya* bir kültür ailesidir ve *Batı Afrika*,
`CHILDREN_WRITING_STYLE.md` § 7'nin adıyla yasakladığı genellemenin ta
kendisidir (*"Afrikalılar…" değil, "Yoruba anlatıcıları…"*). Daraltma altı
geleneğin hepsini korur ve `project_config.roadmapTraditions` ile makine
okunur tutulur; `validate_spec.py` her geleneğin kilitli bir kültürle
karşılandığını **ayrıca** denetler. Yani daraltma bir kaçış yolu değil,
**ek bir kapıdır**.

---

## 2. Yirmi iki kültür

| Bölge | Kültürler |
|---|---|
| Avrupa | Greek · Norse · Irish · Finnish |
| Batı/Orta Asya | Mesopotamian · Persian · Turkic |
| Güney/Doğu Asya | Hindu · Chinese · Korean · Japanese · Vietnamese |
| Afrika | Ancient Egyptian · Yoruba · Akan · Zulu |
| Amerika + Kutup | Inuit · Maya · Aztec (Mexica) · Andean |
| Okyanusya | Māori · Hawaiian |

**Kısıtlılık taraması — muafiyetsiz (K20):** 22/22 tamam ·
14 `clear` · 8 `partial` · **0 `pending`**

Aday havuzu: **31 kayıt** (22 kilitli + 9 aday) — şart ≥26 ✓

### Kilitlenemeyen kültürler — bu bir kusur değil bir karardır

| Kültür | Sonuç | Gerekçe |
|---|---|---|
| Diné (Navajo) | `restricted` | Anlatıların önemli bölümü **mevsime** bağlıdır; kimin anlatabileceği kurala bağlıdır. Yayımlanmış olmak izinli olmak değildir. |
| Amazonian | `restricted` | "Amazon" tek kültür değil, yüzlerce ayrı halktır. |
| Australian Aboriginal | `excluded` | Anlatı topluluk mülkiyetindedir. |
| "African mythology" tek başlık | `excluded` | Bir kıtayı tek mitolojiye indirmek yasak genellemedir. |

---

## 3. Kırk beş hikâye

Altı bölgesel bölüm · her kilitli kültürün ≥1 hikâyesi ·
hiçbir kültür >3 · **Yunan tam 3** · kelime bütçesi **42.750** (hedef 43.000, sapma %0,6)

| Bölüm | Kültür | Hikâye |
|---|---:|---:|
| 1 · The Wine-Dark Sea and the Frozen North | 4 | 10 |
| 2 · Between the Two Rivers | 3 | 6 |
| 3 · Where the Sun Comes Up | 5 | 10 |
| 4 · The Long River and the Forest Road | 4 | 8 |
| 5 · Ice, Maize, and the High Cold Mountains | 4 | 7 |
| 6 · The Sea Between the Islands | 2 | 4 |

Aday havuzu: **59 hikâye** (45 kilitli + 14 aday) — şart ≥55 ✓

---

## 4. Araştırma doğrulaması

| Ölçüt | Sonuç |
|---|---|
| Araştırma kaydı | **59** üretildi (45 kilitli + 14 aday) |
| Kaynak künyesi | **163** · hikâye başına 2,8 |
| Katman | `primary` **82** · `scholarly` **58** · `reference` **23** |
| **`retelling`** | **0** — SOURCING_STANDARD § 2 |
| **`index`** | **0** |
| Doğrulama | `toc` 82 · `canon` 42 · `sv` 21 · `fulltext` 16 · `article` 2 |
| ≥2 bağımsız kaynak | 45/45 ✓ |
| ≥1 `primary`/`scholarly` | 45/45 ✓ |
| ≥1 güçlü doğrulama | 45/45 ✓ |
| Kanonik anlatım + gerekçe | 45/45 ✓ |
| Telaffuz kaydı | **198** giriş, hepsi kaynaklı ✓ |
| Kişi kaydı | **154** ✓ |

**Zayıf doğrulama (`catalog`/`secondary`) kullanılmadı.** Her hikâyenin en
az bir kaynağı okurun gidip bakabileceği bir yere işaret eder.

### Telaffuz uydurulmadı

Her telaffuzun kaynağı vardır ve kaynaklar **sistem** düzeyindedir: Kore
için Revised Romanization (fonemik), Japonca için Hepburn, Çince için
Hanyu Pinyin, Māori için Te Aka, Hawai'i için Pukui & Elbert, Yoruba için
Abraham, Zulu için Doke & Vilakazi, Nahuatl için Karttunen, K'iche' için
Christenson, Quechua için Academia Mayor.

**Mısır özel bir dürüstlük borcu taşır:** Mısırca ünlüleri yazmaz. Rehber,
okumanın bir **Mısırbilim konvansiyonu** olduğunu (Allen, *Middle Egyptian*
§ 2.7) açıkça söyler — bir yeniden yapılandırma gibi sunmaz.

---

## 5. Yaş politikası

`AGE_POLICY.md` **kurucu onaylı** ve pilot yazılmadan **önce** onaylandı
(yol haritası § 21 H2).

45 kilitli hikâyenin: **29** `cleared` · **16** `needs-review`
→ hepsi `03_EDITORIAL/AGE_REVIEW_LOG.md`'de kayıtlı, kilit kararlarıyla.

Kayda geçen zor uyarlamalardan üçü:

- **Sedna** (35) — parmakların kesilmesi anlatının **merkezidir ve
  çıkarılamaz**. Tek cümle; dönüşüm sahnedir, yara değil. Baba aklanmaz.
- **Horus ve Seth** (27) — kaynaktaki cinsel bölümler **tamamen dışarıda**
  (§ 2.8, istisnasız); anlatı mahkeme ve kılık değiştirme üzerinden taşınır.
- **Ọbàtálá** (30) — kaynaklarda anlatının engelliliğe bağlanan bir
  aitiyolojisi var; **kullanılmadı**, çünkü engelli okuru bir hata olarak
  çerçeveler. Kaynakta olan ama kitapta olmayan şey **kaydedildi**.

---

## 6. Pilot hikâye — ses kalibrasyonu

**`korean-dangun` · "The Bear Who Waited in the Dark" · 972 kelime**

| Ölçü | Değer | Bant | |
|---|---:|---|---|
| Kelime | 972 | 800–1100 (hedef 950) | ✓ |
| Cümle ortalaması | **11,85** | 11–14 | ✓ |
| En uzun cümle | **25** | ≤25 | ✓ |
| Hece/kelime | **1,359** | 1,35–1,55 | ✓ |
| Zor sözcük | **%4,84** | ≤%6 | ✓ |
| Flesch–Kincaid | **5,07** | 4,0–6,5 | ✓ |
| Paragraf | 3,9 cümle | 3–5 | ✓ |
| Özel ad | **4** | ≤7 | ✓ |
| Ünlem | **0** | ≤3 | ✓ |
| Kültürel not | 43 kelime | 25–45 | ✓ |

Sekiz metin kapısının **hepsinden** geçti: `qa_length` · `qa_readability` ·
`qa_voice` · `qa_age` · `qa_echo` · `qa_diacritics` · `qa_crossref` · `qa_drift`

**İlk taslak üç bandı ıskaladı** ve eşikler değil **proza** düzeltildi:
hece/kelime 1,209 → 1,359 · FK 3,18 → 5,07 · en uzun cümle 37 → 25.
Bu, `CHILDREN_WRITING_STYLE.md` § 2.3'ün neden gerçek metinden doldurulması
gerektiğinin kanıtıdır: **hedef bir sayı değil, okunabilir bir paragraftır.**

`CHILDREN_WRITING_STYLE.md` § 2.3'teki üç kalibrasyon örneği bu hikâyeden
gelir ve `validate_structure` artık ikisini birden denetler: örnek **dolu mu**
ve manuscript'te **birebir bulunuyor mu** (uydurulmuş örnek yakalanır).

---

## 7. Sayfa kalibrasyonu — gerçek dizgi

`04_BUILD/calibrate_pages.py` pilot prozasını gerçek metin bloğuna
(4,875″ × 7,5″), gerçek tipografiyle (12/16,5 pt) ve **gerçek yazı karakteri
genişlik tablolarıyla** dizip satırları saydı.

| | Tahmin | **Ölçüm** | Fark |
|---|---:|---:|---:|
| Kelime/sayfa | 361,1 | **357,5** | −%1,0 |
| Karakter/kelime | 5,4 | **5,349** | −%0,9 |
| Genişlik oranı | 0,48 | **0,4895** | +%2,0 |

**Tipografi tahmini iyiydi. Asıl bulgu başkaydı:** yazı karakteri seçimi
kelime/sayfa'yı **%21** oynatıyor (DejaVu Serif 282,8 · Times/Liberation
357,5). Sayfa bütçesinin en büyük belirsizliği model hatası değil, **Faz
5'te verilecek yazı karakteri kararıdır** — ve bu, ölçüm yapılmadan
görülemezdi.

### Ölçüm bootstrap'ın kendi önerisini çürüttü

Bootstrap (a′) şıkkını öneriyordu — kart açık sayfa, 3 sayfa/hikâye, 226
sayfa — ama o öneri `wpp ≈ 420` **tahminine** dayanıyordu. Ölçüm 357,5
verdi; 3 sayfa/hikâye için ≥380 gerekiyor ve **12 pt bir yaş kararıdır**
(konfor değil), küçültülemez. Yani **4 sayfa/hikâye kilitlidir** ve (a′)
226 değil **272 sayfaya** çıkar: bütün şıkların en kötüsü.

Ölçüm aynı anda çözümü de buldu: her hikâye 3,219 sayfa içerik taşıyıp
**4 sayfa faturalanıyor** → 0,781 sayfa (**25 satır**) *zaten ödeniyor*,
45 hikâyede **35 sayfa**. Kültür kartı (~15 satır) oraya sığar → **K27**.

| | Önce | **Sonra** |
|---|---:|---:|
| Sayfa | 250 | **228** |
| Hedeften sapma | %8,7 | **%0,9** |
| Ciltsiz maliyet | 4,00 $ | **3,74 $** |
| Ciltsiz telif | 6,19 $ | **6,46 $** |

**Telif yol haritasının kendi 6,43 $ rakamının 0,03 $ üstünde.**

---

## 8. Kapı kusurları — altı ölü kural bulundu ve düzeltildi

Bunlar Faz 1'in en değerli çıktısıdır: hepsi **yeşil yanan** ama hiçbir şey
denetlemeyen mekanizmalardı.

| # | Kusur | Neden tehlikeliydi |
|---|---|---|
| 1 | `validate_spec` kültür aday havuzunu **yalnızca `phase0`'da** denetliyordu | Kapı `phase1`'e yükseldiği an denetim **kayboluyordu** — tam da yedek payının anlam kazandığı noktada. DoD ölçüt 7 kapısız bir belge cümlesiydi. |
| 2 | `story_index.schema.json` **≥55 aday havuzunu imkânsız kılıyordu** | `number` zorunlu tamsayı, tavan 45 → 46. kayıt şemayı ihlal ediyordu. Şema, `SOURCING_STANDARD` § 9'un **zorunlu kıldığı** şeyi yasaklıyordu. |
| 3 | `make_prompts.py` şemada **tanımlı olmayan** alanı okuyordu | `story.imagePrompt` + `additionalProperties: false` → dal hiçbir koşulda çalışamazdı. |
| 4 | **`mythbook.load_book()` öz-testi öldürüyordu** | Diskteki manuscript'i enjekte edilen kurgudan **önce** okuyordu. Faz 0'da disk boştu. **İlk gerçek hikâye yazıldığı an** 15 kapının hepsi temiz metni görüp yeşil yandı: kapıların kendi testi, **koruduğu şey var olduğu anda** çalışmayı bıraktı. |
| 5 | **`qa_crossref` doğru metni reddediyordu (D32)** | Kendi ad tespitini yapıyor, cümle başını eliyor ama **paragraf başını elemiyordu**. Pilot kapıyı “The” (×21), “Twice”, “They” ile kırmızı yaktı. |
| 6 | `.gitignore`'da **sonraki kural öncekini eziyordu** | `02_MANUSCRIPT/README.md` hiç takip edilmemişti — *"proza neden burada değil"* cevabı public depoda **hiç görünmedi**. `LEAK_SCAN_SKIP`'teki muafiyeti de ölüydü. |

**Dördüncüsü en ciddisidir** ve tam olarak Faz 1'in yazım işi sayesinde
ortaya çıktı: Faz 0'da görünmesi **imkânsızdı**.

### İnşa edilen kapılar

- `validate_structure` — DoD 21: üç kalibrasyon örneği dolu **ve** manuscript'te birebir
- `validate_structure` — DoD 26: A4/A5 `→ K##` ile kapanmış **ve** mimari belgesinde yazılı
- `validate_spec` — yol haritasının altı geleneği kilitli bir kültürle karşılanıyor
- `validate_spec` — `restricted` taranan kültür **kilitlenemez**
- `selftest` — **öz-testin kendi canlılık testi** (kusur 4'ün regresyonu)
- `selftest` — **D32 regresyonu**, iki yönlü (kusur 5)
- `selftest` — **ölü muafiyet avı** (kusur 6)

`05_TESTS/selftest.py`: **44 kapı testi geçti** (bootstrap'ta 39).

---

## 9. CI ve Git

| Commit | Konu |
|---|---|
| `13664d5` | kapsam kilidi — 22 kültür, 45 hikâye, 59 araştırma kaydı |
| `bbfdc7d` | pilot hikâye, ses ve sayfa kalibrasyonu — kapı `phase1` |
| `79317a3` | düzeltme: sayfa kalibrasyonu manuscript'siz ortamda ölüyordu |

**Sürüm koşusu bir kusur yakaladı ve iyi ki yakaladı.** `calibrate_pages.py
--check`, manuscript bulunamayınca `SystemExit(1)` ile ölüyordu — ama depo
public, manuscript **değil** (K21): CI'da proza hiçbir zaman bulunmaz.
Kapı, projenin **kendi tasarım kararını** hata sayıyordu. Yerelde
görünmedi çünkü yerelde proza var.

Düzeltme *"uygulanamaz"* ile *"devre dışı"*yı ayırdı (talimat § M): ölçüm
ertelenir ama **kayıtlı raporun depoda olduğu ve `calibrated` bir model
taşıdığı yine de denetlenir**; manuscript varsa bayatlık denetimi eskisi
gibi ısırır.

**Son durum:** `validate` ✅ · `build` ✅ · `images` ✅ · `release` ✅
Etiket **`v0.1.0`** · GitHub Release yayımlandı.

---

## 10. Faz 1 Definition of Done — 32/32

Master yol haritası § 17'nin **otuz iki ölçütünün tamamı** karşılandı.
Kısmi geçiş yoktur ve burada da yoktur.

Doğrulanma biçimi: `.gate` = `phase1` = `project_config.gates.current` ·
`./04_BUILD/qa_all.sh` bütün kapılar yeşil · `selftest` 44/44 ·
GitHub Actions dört iş akışında yeşil · `v0.1.0` etiketi ve Release.

---

## 11. Kalan riskler

| # | Risk | Durum |
|---|---|---|
| R-a | **Yazı karakteri kararı sayfa bütçesini %21 oynatabilir** | Faz 5'e ait; ölçüm bunu **sayı olarak** kayda geçirdi. Faz 3'te yeniden ölçülecek. |
| R-b | Kalibrasyon **tek** hikâyeye dayanıyor | K3'ün kabul ettiği sınır. Faz 3'te 31 hikâyeyle yeniden ölçülür. |
| R-c | 16 hikâye `needs-review` | Kayıt altında; her biri yazımdan önce üçüncü bir göz gerektirir. |
| R-d | Kültür kartının kuyruk boşluğuna dizilmesi Faz 5'te zor | K27'nin bilinen bedeli; alternatifi 22 vinyeti görünmez yapmaktı. |
| R-e | **A8 açık** — iki ebeveyn okuyucusu | **Kurucu eylemi gerekiyor.** Faz 4 başlamadan kapanmalı. |

---

## 12. Kurucudan gereken

1. **Pilot hikâyenin sesi onayı** (yol haritası § 21 **H5**) — Faz 2'yi bloklar.
   Metin `02_MANUSCRIPT/book.json` içinde, yerelde.
2. **A8** — iki ebeveyn okuyucusunun kim olacağı. Faz 4 başlamadan.
   İki kişi bulmak zaman alır ve okuma 45 hikâyeyi kapsayacak.
3. **Faz 2 onayı.**

---

## 13. Faz 2 hazırlık durumu

```
FAZ 0 · BOOTSTRAP           ████████████████  TAMAM
FAZ 1 · TEMEL               ████████████████  TAMAM · v0.1.0
FAZ 2 · ÇEKİRDEK YAZIM      ░░░░░░░░░░░░░░░░  ONAY BEKLİYOR
FAZ 3 · GENİŞLEME           ░░░░░░░░░░░░░░░░
FAZ 4 · TAMAMLAMA           ░░░░░░░░░░░░░░░░
FAZ 5 · ÜRETİM              ░░░░░░░░░░░░░░░░

Kilitli kültür : 22 / 22
Kilitli hikâye : 45 / 45
Araştırma kaydı: 59
Yazılmış hikâye:  1 / 45
Görsel         :  0 / 68   (Faz 1 hedefi 0)
Sayfa modeli   : ÖLÇÜLDÜ · 228 sayfa
```

Faz 2 hedefi: **15 hikâye** (kümülatif 16/45) · ~14.250 kelime · 16 görsel.
İlk iki bölgesel bölüm hazır: *The Wine-Dark Sea and the Frozen North* (10)
ve *Between the Two Rivers* (6) — tam 16 hikâye.

---

## ⛔ FAZ 1 TAMAM · FAZ 2 BAŞLAMADI

Hiçbir Faz 2 hikâyesi yazılmadı. Hiçbir görsel üretilmedi. Hiçbir KDP
dosyası oluşturulmadı.

**Kurucu onayı bekleniyor.**
