# AGE REVIEW LOG — yaş incelemesi defteri

> **Bu defter bir onay kutusu değildir.** `AGE_POLICY.md` § 1'e göre `REVIEW`
> seviyesindeki malzeme, **kurucu + iki ebeveyn okuyucusu** onayı olmadan
> yayına giremez. Bu dosya o zincirin kaydıdır.
>
> Makine tarafı: `04_BUILD/qa_age.py` — **yazılmış** bir hikâye
> `sacrifice`, `religious` veya `culturally-sensitive` işareti taşıyorsa
> burada bir kaydı olmak **zorundadır**. Kaydı yoksa CI kırmızı yanar.
>
> Faz 1 · 8 Ağustos 2026 · kapı `phase1`

---

## 1. Nasıl okunur

| Sütun | Ne demek |
|---|---|
| **Durum** | `cleared` — inceleme yapıldı, uyarlama yeterli · `needs-review` — yazımdan önce ikinci göz gerekli · `founder-approved` / `parent-approved` — insan onayı alındı |
| **İşaret** | `AGE_POLICY.md` § 2'nin on yedi kategorisinden `REVIEW` seviyesinde olanlar |
| **Kilit** | Uyarlama kararının tek cümlelik özeti; tam gerekçe araştırma kaydındadır |

**Durum `needs-review` olan bir hikâye yazılabilir.** Anlamı şudur: yazan
oturum tek başına karar veremez, yazımdan önce uyarlama kararı ayrı bir
gözle doğrulanır (`CHILDREN_WRITING_STYLE.md` § 9: *"yaş incelemesi üçüncü
bir gözle"*).

---

## 2. Faz 1'de yazılan hikâye

| # | Hikâye (`id`) | Kültür | Durum | İşaret | Sonuç |
|---:|---|---|---|---|---|
| 21 | `korean-dangun` | Korean | `cleared` | — | `REVIEW` kategorisi taşımıyor. `transformation` **ALLOW** seviyesindedir (§ 2.5) ve dönüşüm hikâyenin kendisidir. Ayının mağaradaki yüz günü **sabırla** anlatılır, bedensel acıyla değil. Kaplanın ayrılışı yargılanmaz. Son paragraf çözümsüz korku taşımaz (§ 2.14). **Bütün metin kapılarından geçti.** |

> Pilot hikâyenin `REVIEW` kategorisi taşımaması **bilinçli bir seçimdir**:
> ses kalibrasyonu, aynı anda en zor yaş kararını da vermek zorunda
> bırakılmamalıydı. Zor kararlar Faz 2'den itibaren, kalibre edilmiş bir
> sesle verilir.

---

## 3. Faz 2+ için bekleyen inceleme kuyruğu

Aşağıdaki **18 kilitli hikâye** yazılmadan önce ikinci bir göz gerektirir.
Hiçbiri henüz yazılmamıştır; bu liste Faz 2'nin giriş kapısıdır.

### 3.1 · `REVIEW` kategorisi taşıyanlar — 9 hikâye

| # | Hikâye (`id`) | Kültür | İşaret | Kilit karar |
|---:|---|---|---|---|
| 17 | `hindu-hanuman-sun` | Hindu | `religious` | Yaşayan din: **şimdiki zaman zorunlu**, "Hindular inanırdı" **yasak** (§ 2.15). Vajra darbesi tek cümle. |
| 18 | `hindu-ganga-descent` | Hindu | `religious` | Yaşayan din; uyarlama gerekmiyor, **çerçeveleme** gerekiyor. Ritüel talimatı yok. |
| 23 | `japanese-amaterasu-cave` | Japanese | `religious` | Şinto yaşıyor; Ise bugün ziyaret ediliyor. Susanoo'nun tahribatı **özetlenir**, atın ve dokumacının ölümü betimlenmez. |
| 24 | `japanese-susanoo-orochi` | Japanese | `sacrifice` | Yedi kızın alınmış olması **olaydır, sahne değildir** (§ 2.7). Kılıç bugün de gösterilmeyen bir nesnedir; kapalı olduğu **söylenir**, uydurulmaz. |
| 30 | `yoruba-obatala-land` | Yoruba | `religious` · `culturally-sensitive` | **Engellilik aitiyolojisi kullanılmaz** — kaynakta var, kitapta yok; gerekçe araştırma kaydında. Òrìṣà ibadeti sürüyor: şimdiki zaman. |
| 31 | `yoruba-osun-seventeenth` | Yoruba | `religious` · `culturally-sensitive` | Divinasyon talimatı yok. Òṣogbo festivali **şimdiki zamanda** anılır. |
| 39 | `aztec-fifth-sun` | Aztec | `religious` · `sacrifice` | **En zor yaş kararı.** Kurban bir **maliyet** olarak sunulur, gösteri olarak değil. *"Onlar böyleydi"* cümlesi **mutlak yasak** (§ 0.3). |
| 45 | `hawaiian-pele-journey` | Hawaiian | `religious` | Pele bugün saygı görüyor; Kīlauea'ya bırakılan adaklar **şimdiki zamanda** anılır, prosedür betimlenmez. |
| 27 | `egyptian-horus-seth` | Egyptian | — | Kaynaktaki cinsel bölümler **tamamen dışarıda** (§ 2.8, istisnasız). Anlatı mahkeme, yarış ve kılık değiştirme üzerinden taşınır. |

### 3.2 · Şiddet / istismar uyarlaması gerektirenler — 9 hikâye

| # | Hikâye (`id`) | Kültür | Kilit karar |
|---:|---|---|---|
| 7 | `irish-cu-chulainn-name` | Irish | Bir **hayvana** yönelen şiddet (§ 2.1 özel inceleme). Ne yaptığı ve neye mal olduğu söylenir; yara betimlenmez. |
| 8 | `irish-children-of-lir` | Irish | **Üvey anne zulmü** (§ 2.9). Ceza ölçülü, sonuç adil; dayanma anlatılır, zulüm değil. |
| 13 | `persian-zal-simorgh` | Persian | Bir babanın yenidoğanı terk etmesi. Kitabın **kınadığı** haksızlıktır; iki cümle, zulüm sahnelenmez. |
| 14 | `persian-kaveh` | Persian | Zahhāk'ın yılanlarının beslenmesi **olgu olarak** söylenir; iştah betimlenmez (§ 2.1, § 2.6). |
| 15 | `turkic-boghach-khan` | Turkic | Babanın oğlunu yaralaması (§ 2.9). Anlatının çözdüğü haksızlık; tek cümle. |
| 16 | `turkic-basat-tepegoz` | Turkic | Yamyamlık **olaydır, sahne değildir** (§ 2.6). Kör etme tek cümle. Odysseia'ya tabi kılınmaz. |
| 35 | `inuit-sedna` | Inuit | **Parmakların kesilmesi anlatının merkezidir ve çıkarılamaz.** Tek cümle; dönüşüm sahnedir, yara değil. Baba aklanmaz, kaynakta olmayan barışma eklenmez. |
| 36 | `inuit-blind-boy-loon` | Inuit | Bir çocuğun aç bırakılması (§ 2.9). Kitabın yargıladığı zulüm; "hak etti" çerçevelemesi yasak. İntikamın bedeli görünür kalır. |
| 37 | `maya-hero-twins` | Maya | Ölüm ve tuzak evleri. Öldürmeler **sonuçlarıyla** anlatılır; evler içerikleriyle değil **yaptıklarıyla** betimlenir. |

---

## 4. Kısıtlılık taramasında **düşen** malzeme

Bu bir kusur değil bir karardır (`SOURCING_STANDARD.md` § 7) ve arka maddede
**okura söylenir**.

| Kültür | Sonuç | Gerekçe |
|---|---|---|
| Australian Aboriginal | **excluded** | Anlatı çoğunlukla topluluk mülkiyetindedir; kimin anlatabileceği kurala bağlıdır. |
| "African mythology" tek başlık olarak | **excluded** | Bir kıtayı tek mitolojiye indirmek `CHILDREN_WRITING_STYLE` § 7'nin yasakladığı genellemedir. Kıtanın dört ayrı kaydı vardır. |
| Diné (Navajo) | **restricted** — kilitlenemez | Anlatıların önemli bölümü **mevsime** bağlıdır ve kimin anlatabileceği kurala bağlıdır. Yayımlanmış olması izinli olduğu anlamına gelmez. |
| Amazonian | **restricted** — kilitlenemez | "Amazon" tek kültür değil yüzlerce ayrı halktır; anlatıların çoğu topluluk mülkiyetindedir. |
| Haudenosaunee | `partial` — aday kaldı | Gökyüzü Kadını anlatısı açık; Kayanerenkó:wa ve Handsome Lake öğretisi **kapalıdır** ve ayrıştırma danışma gerektirir. |

---

## 5. İnsan onayı — Faz 5 kapısı

`04_BUILD/validate_structure.py` Faz 5 kapısında
`03_EDITORIAL/PARENT_READINGS.md` dosyasını arar ve **iki imzalı okuma
kaydı** yoksa sürüm çıkmaz.

**A8 hâlâ AÇIKTIR** ve iki gerçek insan gerektirir. Yol haritası § 21 H8:
*Faz 4 başlamadan.* İki kişi bulmak zaman alır ve okuma 45 hikâyeyi
kapsayacaktır — bu yüzden karar Faz 4'te değil **şimdi** planlanmalıdır.
