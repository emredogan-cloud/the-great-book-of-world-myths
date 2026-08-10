# LINE EDITOR RAPORU — Faz 7

> **The Great Book of World Myths** · 10 Ağustos 2026 · kapı `phase5`
>
> ⚠ **BU DOSYA PROZA İÇERMEZ.** Depo public'tir ve kitabın metni
> `.gitignore` § ① ile dışarıdadır. Bulguların TAM hâli — her
> `eski → yeni` çifti — takip edilmeyen
> `06_REPORTS/editorial/LINE_EDITOR_FINDINGS.md` dosyasındadır.

---

## 1. Ne yapıldı

Manuscript'in **45 hikâyesinin tamamı** satır satır denetlendi. Denetim
altı bağımsız geçişe bölündü: beş dilim (her biri 9 hikâye) ve bir
**çapraz denetim** — tek bir dilim okuyucusunun göremeyeceği kitap
genelindeki yakınsamayı arayan ayrı bir geçiş.

Bulgular körlemesine uygulanmadı. Her biri araştırma kaydına, üslup
kurallarına ve kültürel kısıtlılık notlarına karşı gözden geçirildi;
reddedilenler gerekçesiyle kayıtlıdır.

| | |
|---|---:|
| Değerlendirilen bulgu | **311** |
| Uygulanan | **275** |
| Uygulanmayan | 36 |
| Dokunulan hikâye | 44 / 45 |
| Yeniden yazılan kültürel not | 12 |

### Geçişe göre

| Geçiş | Uygulanan |
|---|---:|
| Hikâye 1–9 | 98 |
| Hikâye 10–18 | 52 |
| Hikâye 37–45 | 52 |
| Hikâye 28–36 | 37 |
| Çapraz denetim (45/45) | 16 |
| Ana ajan (hikâye 19–27) | 16 |
| Ana ajan (olgu düzeltmesi) | 4 |

### Ağırlığa göre

| Ağırlık | Uygulanan |
|---|---:|
| critical | 7 |
| major | 50 |
| minor | 202 |
| ana ajan | 16 |

### Kusur sınıfına göre

| Sınıf | Uygulanan |
|---|---:|
| repetition | 85 |
| awkward | 48 |
| readability | 34 |
| continuity | 26 |
| grammar | 19 |
| ana ajan · olgu/üslup | 16 |
| other | 14 |
| naming | 11 |
| meta | 5 |
| meta-language | 5 |
| factual | 4 |
| typography | 3 |
| punctuation | 3 |
| terminology | 1 |
| title | 1 |

---

## 2. Bulunan yedi KRİTİK kusur

Hepsi üretime gitmiş olurdu ve hiçbiri bir kapıya takılmıyordu.

| # | Kusur | Neden kritik |
|---|---|---|
| 1 | Bir hikâyede **iki ardışık paragraf aynı cümleyle başlıyordu** ve aynı bilgiyi iki kez veriyordu | Üretim artığı; okur için görünür bir hata |
| 2 | Bir diyalog paragrafında **sahipsiz, kopya bir replik** duruyordu | Konuşmacısı olmayan satır; sayfada anlamsız |
| 3 | Bir cümlede **zamirin öncülü yoktu** ve cümle kendi kendine belge uzatan bir karakter üretiyordu | Sahne tersine okunuyordu |
| 4 | Aynı tanrının adı **iki komşu hikâyede iki farklı biçimde** yazılmıştı — üstelik metin 'aynı tanrı' diyordu | Telaffuz rehberi tek biçim taşıyabilir; çocuk iki ad görüyordu |
| 5 | **İki ayrı konuşmacının replikleri tek paragrafta** birleşmişti | Kim konuşuyor belirsizdi |
| 6 | Bir hikâye **kitabın başka bir hikâyesine göndermede bulunuyordu** | Üslup § 2.2'nin adıyla yasakladığı sınıf (Bestiarium'da 57 örnek) |
| 7 | **On beş kültürel not**, hikâyenin son paragrafını neredeyse kelimesi kelimesine tekrar ediyordu | Notun iki satırı boşa gidiyor; okur notları atlamayı öğreniyor |

---

## 3. En pahalı bulgu: kültürel not tekrarı

Çapraz denetimin tek başına bulabileceği kusur buydu. Kitabın en
belirgin sistemik sorunu: hikâye gövdesi **kitabın sesiyle** bitiyor
(kayıt, anlatıcılar, gidilebilecek bir yer), sonra kültürel not **aynı
şeyi** söylüyor.

Düzeltme iki yönlü yapıldı ve yön **hikâyenin uzunluğuna** göre seçildi:

- **Gövdeden kesildi** — hikâye 800 kelime tabanının üstünde kalıyorsa.
- **Not yeniden yazıldı** — hikâye tabana yakınsa. Yeni not içeriği
  `01_RESEARCH/research/*.md` kayıtlarındaki **gerçek kaynaklardan**
  alındı (yayın yılı, derleyici, varyant, kaydın sınırı). Hiçbir olgu
  uydurulmadı.

⚠ İlk denemede iki Inuit hikâyesi kesim yüzünden 800 kelimenin altına
düştü (799 ve 791). Çapraz denetim bunu **önceden uyarmıştı**:
*"kesim değil TAKAS"*. Kesimler geri alındı ve tekrar not tarafından
çözüldü. Kapı bu hatayı yakaladı — sayı uydurulmadı, düzeltildi.

---

## 4. Uygulanmayanlar

### 24 açık soru — olgu doğrulaması gerekiyor

Line Editor bunları **değiştirmedi** ve değiştirmemesi doğrudur:
kaynağa bakmadan düzeltmek, uydurmakla aynı şeydir. Dördü ana ajan
tarafından araştırma kaydına bakılarak çözüldü; kalanlar kurucunun
ya da bir sonraki araştırma geçişinin işidir.

| Hikâye | Soru |
|---|---|
| `greek-persephone` | The Homeric Hymn gives Persephone one seed and does not, as far as I know, acknowledge rival versions; the disagreement over the number is visible acr… |
| `norse-thors-hammer` | Story 5 calls the same goddess's borrowed flying garment "the falcon cloak". Two names for what a child will read as one object; worth deciding whethe… |
| `norse-thors-hammer` | Story 1 in the same batch is "The Girl Who Ate Six Seeds"; two "The ___ Who Ate ___" titles this close together in the table of contents read as a pat… |
| `irish-cu-chulainn-name` | A lantern in an Iron Age Irish smith's doorway may be an anachronism; a torch or rushlight would be safer. Flagging rather than changing, since I do n… |
| `finnish-sampo` | The Kalevala's kirjokansi is usually rendered "many-coloured lid" or "decorated cover"; the star pattern may be an interpretation rather than somethin… |
| `meso-gilgamesh-plant` | The epic gives no interval between the wrestling match and the friendship; “inside a fortnight” looks like an added specific. Separately, “fortnight” … |
| `meso-etana-eagle` | In American English “buzzard” means vulture, so a large share of the readership will picture a carrion bird spiralling over a carcass — an unfortunate… |
| `meso-etana-eagle` | The cylinder seals usually identified with Etana — a man rising on an eagle above shepherds and flocks — are normally catalogued as Old Akkadian, seve… |
| `persian-zal-simorgh` | In the Shāhnāmeh the Simorgh gives Zal a single feather from her breast, and it is that one feather he burns at Rostam’s birth. Please check whether “… |
| `persian-zal-simorgh` | The Shāhnāmeh presents Zal as a great warrior and counsellor, but the superlative “strongest man of his generation” belongs to Sam before him and Rost… |
| `persian-kaveh` | Two of the note’s three clauses restate the story text: “That apron became the battle standard of the whole country and stayed that way for centuries”… |
| `turkic-boghach-khan` | Two stories earlier, an enormous bird does exactly this — saves a child abandoned on a mountain. As written the line reads as a wink back at the Simor… |
| `turkic-boghach-khan` | Both sentences are already in the story text, one of them almost word for word: “Among the Oghuz a boy carried no name until he had done something wor… |
| `turkic-basat-tepegoz` | A wary animal approaches from downwind, so it can smell what it is approaching and its own scent is carried away. “From upwind” appears to be reversed… |
| `hindu-ganga-descent` | India is the most populous country, but not the most crowded by density (Bangladesh, which the river also crosses before the sea, is far denser among … |
| `egyptian-isis-secret-name` | How many manuscript witnesses of the Isis-and-Ra charm are there? The argument leans on "several copies" all stopping in the same place; if the count … |
| `egyptian-shipwrecked-sailor` | The Shipwrecked Sailor papyrus (P. Hermitage 1115) is normally described as complete at the end, closing with a scribal colophon; it is the opening th… |
| `yoruba-osun-seventeenth` | "Three continents" is a hard number in a reference sentence, and it reads as a ceiling. Devotees travel to Òṣogbo from Africa, the Americas and Europe… |
| `akan-ananse-stories` | In the widely attested tellings Nyame's price is four captives (hornets, python, leopard, and Mmoatia), often with Ananse's mother added. This telling… |
| `inuit-sedna` | In most recorded tellings the father cuts the fingers off, joint by joint. The wording here attributes it to the boat's edge, which quietly removes hi… |
| `maya-maize-people` | The Popol Vuh gives noticeably more of the destruction of the wooden people than this page does (it names the beings that came out of the sky and what… |
| `aztec-fifth-sun` | INAH has kept the Pyramid of the Sun closed to climbing since 2020, so a reader who travels there may not be able to do this; please verify current ac… |
| `aztec-quetzalcoatl-maize` | Two things to decide together. “the older story” reads as a pointer to story 39 in this book; and the same god is spelled Nanahuatzin there and Nanahu… |
| `andean-llama-flood` | This sits directly under “The Ant Who Would Not Say Where” in the contents, so two consecutive stories are titled “The <animal> Who/That Would Not <ve… |

### 9 ana ajan reddi

İkisi aynı yere dokunan düzeltmeler; kaba olan kazandı.

### 3 kapsanmış

Daha geniş bir kesimin içinde kaldılar ve konusuz kaldılar.

---

## 5. Ana ajanın kendi düzeltmeleri

Line Editor'ün *soru* diye işaretleyip değiştirmediği, ama araştırma
kaydına bakıldığında **gerçek kusur** çıkan dört yer:

| Sınıf | Ne bulundu |
|---|---|
| Olgu aşırılığı | Bir nehrin geçtiği ülke için ölçülebilir olmayan bir üstünlük iddiası vardı; doğrulanabilir bir ifadeyle değiştirildi |
| Lehçe tuzağı | Bir kuş adı İngiliz ve Amerikan İngilizcesinde **farklı hayvan** demek; okurun yarısı yanlış imgeyi görecekti |
| Doğa bilgisi | Temkinli bir hayvanın rüzgâra göre yaklaşma yönü tersti |
| Tutulamayacak söz | Okura bir anıta tırmanabileceği söyleniyordu; erişim 2020'den beri kapalı |

---

## 6. Uygulanmayan yapısal öneriler

Çapraz denetim üç yapısal değişiklik daha önerdi. Uygulanmadılar ve
**gerekçe kayıtlıdır** — talimatın *"cilalama, tektipleştirme değil"*
kuralı bunları yazarın işi sayar:

| Öneri | Neden uygulanmadı |
|---|---|
| 4–5 hikâyenin **açılış cümlesini** yeniden kurmak (27/45 aynı sözdizimsel hamleyi kullanıyor) | Açılış cümlesi yazarın sesidir; satır editörü değil yazar değiştirir |
| Üç hikâyeyi daha **yeniden adlandırmak** (22/45 başlık 'The X Who/That Y' kalıbında) | Başlık değişikliği dizin, arka madde ve metadata'ya yayılır; biri (birebir aynı beş sözcüklük kuyruk) uygulandı, gerisi kurucu kararı |
| ~10 kültürel notu daha **yeniden yazmak** | Yeni not içeriği kaynak ister; kaynağı olmayan not uydurma olur |

Bunlar `06_REPORTS/editorial/LINE_EDITOR_FINDINGS.md` içinde tam
gerekçeleriyle durur ve bir sonraki editoryal geçişin girdisidir.

---

## 7. Uygulamadan sonra ölçülen

| | Önce | Sonra |
|---|---:|---:|
| Hikâye metni | 40.392 kelime | 39.985 kelime |
| Hikâye ortalaması | 898 | 889 |
| Bant dışı hikâye (800–1100) | 0 | **0** |
| En uzun cümle | 25 | **23** |
| İç blok sayfa | 236 | **234** |

Kısalma **kasıtlıdır**: kesilen şeylerin çoğu, notun ya da bir başka
hikâyenin zaten söylediği cümlelerdi.

⚠ Sayfa sayısı 236→234 düştüğü için **sırt genişliği değişti** ve
kapaklar yeniden üretildi. Sırtın sayfa sayısına bağlı olması bu
projede bir kapıdır (`package_selftest`) ve burada kendini kanıtladı.

---

## 8. Metin kapıları — uygulamadan sonra

| Kapı | Sonuç |
|---|---|
| kelime bandı | ✅ |
| yaş politikası | ✅ |
| okunabilirlik | ✅ |
| ses ve yasak kalıp | ✅ |
| tekrar taraması | ✅ |
| diakritik ve adlandırma | ✅ |
| çapraz referans | ✅ |
| üslup sürüklenmesi | ✅ |

İki regresyon uygulamadan sonra bulundu ve düzeltildi:

1. İki cümle 25 kelime tavanını aştı (netlik düzeltmeleri cümleyi
   uzatmıştı) — biri kısaltıldı, biri **ikiye bölündü**.
2. Bir düzeltme İngilizce hitap hâlini büyük harfe çevirdi ve çapraz
   referans kapısı onu *künyesiz özel ad* sandı. Kapı düzeltildi:
   akrabalık hitapları özel ad değildir. Muafiyetin kapıyı
   körleştirmediği **kasıtlı kusurla kanıtlandı** (`selftest` ⑥).

