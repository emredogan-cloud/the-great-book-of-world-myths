# FAZ 2 · GÖRSEL HATTI HAZIRLIK RAPORU

> **Bu rapor bir tamamlanma beyanı DEĞİLDİR.**
>
> Faz 2'nin 16 görselinin **hiçbiri üretilmedi**, çünkü ham görsel üretimi
> kurucunun işidir (yol haritası § 21 · **H7** — GPT Image) ve bu ajanın
> çalıştığı ortamda görsel üretme yeteneği **yoktur**.
>
> Talimat § 21 ve § 35 açık: *"Do not claim that you physically generated
> an image if the current environment has no image-generation capability."*
> Bu rapor tam olarak neyin **HAZIR**, neyin **BEKLEDİĞİ**ni ayırır.
>
> Faz 2 · 8 Ağustos 2026

---

## 1. Neden bu Faz 2'yi bloklamıyor

Yol haritası § 21 bunu adıyla karara bağlamıştır:

> *"**H7 hiçbir yazım fazını BLOKLAMAZ** (Bestiarium D39 ile aynı gerekçe):
> hat hazır ve kalibre; ham girdi geldiği anda **tek komut yeter**."*

Yani Faz 2'nin görsel yükümlülüğü **hattın hazır ve kalibre olması**dır.
Ham PNG'lerin varlığı Faz 5'in (üretim) kapısıdır, yazım fazının değil.

**Bu rapor o hazırlığın kanıtıdır.**

---

## 2. Durum tablosu — ölçülmüş

| Kalem | Durum | Kanıt |
|---|---|---|
| Prompt kütüphanesi üretildi | ✅ | `make_prompts: 8 geçti · 0 uyarı` |
| 16 hikâyenin promptu mevcut | ✅ **16/16** | aşağıdaki tablo |
| Prompt konusu hikâyeye ÖZGÜ | ✅ **16/16** | her konu o hikâyenin **dönüm** anından türetildi |
| Üslup gövdesi tek yerde | ✅ | `04_BUILD/imagespec.py` — 68 promptun tamamında aynı imza |
| Ölçüm cetveli kalibre | ✅ | `image_selftest: 12 kalibrasyon testi geçti` (hata %0,00) |
| Format bütçeleri hesaplı | ✅ | `convert_images: 2 geçti · 0 uyarı` |
| Kindle dosya bütçesi | ✅ **1,08 MB / 3,00 MB** | görsel 0,48 + metin 0,60 |
| Kültürel güvenlik kısıtları | ✅ | negatif promptta zorunlu |
| **Ham PNG üretimi** | ⏳ **0 / 16 — KURUCU BEKLİYOR** | `07_ASSETS/raw/` boş |
| İşlenmiş format üretimi | ⏳ ham girdi bekliyor | hat hazır |
| Tolerans dışı görsel | **0** | ölçülecek görsel yok |

---

## 3. Kurucunun üretmesi gereken tam liste

Her biri `07_ASSETS/IMAGE_PROMPT_LIBRARY.html` içinde **kopyalama düğmesiyle**
hazır bekliyor. Ham çıktı **PNG**, 2400 × 1600 px, 3:2 yatay (karar K5).

| Dosya | Hikâye | Kültür |
|---|---|---|
| `story-001.png` | The Girl Who Ate Six Seeds | Greek |
| `story-002.png` | The Weaver Who Would Not Look Down | Greek |
| `story-003.png` | Wings Made in a Locked Room | Greek |
| `story-004.png` | The Bride Who Ate an Ox | Norse |
| `story-005.png` | The Goddess Who Kept the Apples | Norse |
| `story-006.png` | The Ribbon That Held a Wolf | Norse |
| `story-007.png` | The Boy Who Took the Hound's Place | Irish |
| `story-008.png` | Nine Hundred Years on the Water | Irish |
| `story-009.png` | The Machine Nobody Can Describe | Finnish |
| `story-010.png` | The Harp Made from a Fish | Finnish |
| `story-011.png` | The Plant at the Bottom of the Sea | Mesopotamian |
| `story-012.png` | The Eagle and the Snake Who Swore an Oath | Mesopotamian |
| `story-013.png` | The Baby Left on the Mountain | Persian |
| `story-014.png` | The Blacksmith's Apron | Persian |
| `story-015.png` | The Boy Who Fought the Bull | Turkic |
| `story-021.png` | The Bear Who Waited in the Dark | Korean |

> Sıra numarası kitabın sırasıdır. `story-021` pilot hikâyedir ve Faz 1'de
> yazıldığı için Faz 2'nin 16'sına dâhildir.

---

## 4. Ham girdi geldiğinde çalışacak tek komut zinciri

```bash
# 1) ham PNG'ler 07_ASSETS/raw/ altına konur (kurucu)
# 2) üretim formatlarını türet
python3 04_BUILD/convert_images.py

# 3) ölç ve kayıtlı raporu yaz
python3 04_BUILD/images.py --measure --json 06_REPORTS/tracked/image-consistency.json

# 4) bütün kapılar
./04_BUILD/qa_all.sh
```

Hat **ham dosyanın üzerine asla yazmaz** (K5). Üç üretim formatı
(`print/*.tif` 600 dpi gri · `kindle/*.png` · `web/*.webp`) türetilir.

---

## 5. Kültürel güvenlik — § 22 karşılığı

Her promptun negatif kısmı şunları **açıkça yasaklar** ve bu yasak
`imagespec.py` içindeki **tek üslup gövdesinden** gelir:

```
no modern objects, no cultural pastiche, no generic fantasy armour,
no stereotyped features, no text, no lettering, no watermark
```

Ayrıca yaş politikası görsele iner (`AGE_POLICY` § 2.17): açılış
illüstrasyonları **"Look Inside"da ebeveynin gördüğü ilk şeydir**, bu yüzden
parçalanmış beden, kan, ceset ve dehşet ifadesi görsel şartnamede yasaktır.

**Bu rapor bir uyarı taşır:** promptlar kültürel doğruluğu *garanti etmez*,
yalnızca yanlışın en yaygın biçimlerini dışarıda tutar. Üretilen her görsel
kültürel isabet için **ayrıca gözden geçirilmelidir** ve o inceleme
Faz 2'nin değil, görselin geldiği anın işidir.

---

## 6. Dürüst özet

```
Prompt hattı        : HAZIR      16/16 · konular hikâyeye özgü
Ölçüm cetveli       : KALİBRE    12/12 test · hata %0,00
Format bütçeleri    : HESAPLI    Kindle 1,08 / 3,00 MB
Ham görsel          : 0 / 16     KURUCU ÜRETECEK (H7)
İşlenmiş görsel     : 0 / 48     ham girdi bekliyor
Tolerans dışı       : 0          ölçülecek dosya yok
```

**HAZIRLANDI ≠ ÜRETİLDİ.** Bu ayrım talimat § 35'in emridir ve bu raporun
tek amacı odur.
