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

## 2. Yazılmış hikâyelerin inceleme kaydı

> **Bu bölüm kapının okuduğu tek yerdir.** `qa_age.py`, `REVIEW` kategorili
> yazılmış bir hikâye için kimliği **yalnızca aşağıdaki işaretli blokta**
> arar. Bekleyen kuyrukta (§ 3) durmak **yetmez**.
>
> Ayrım Faz 3'te kondu ve bir kusuru kapattı: kapı eskiden kimliğin defterde
> **bir yerde** geçmesini arıyordu, kuyruk tablosu da bu şartı sağlıyordu —
> yani hiç incelenmemiş bir hikâye, sırf kuyrukta durduğu için geçebilirdi.
> Faz 2'de tetiklenmedi (yazılan 15 hikâyenin hiçbiri `REVIEW` taşımıyordu);
> Faz 3'ün altısı taşıyor. `selftest.py` iki yönlü sınar: kuyruk kaydı
> **saymamalı**, sonuç kaydı **saymalı**.

<!-- AGE-REVIEW:RECORDED -->

### 2.1 · Faz 1 — ses kalibrasyon pilotu

| # | Hikâye (`id`) | Kültür | Durum | İşaret | Sonuç |
|---:|---|---|---|---|---|
| 21 | `korean-dangun` | Korean | `cleared` | — | `REVIEW` kategorisi taşımıyor. `transformation` **ALLOW** seviyesindedir (§ 2.5) ve dönüşüm hikâyenin kendisidir. Ayının mağaradaki yüz günü **sabırla** anlatılır, bedensel acıyla değil. Kaplanın ayrılışı yargılanmaz. Son paragraf çözümsüz korku taşımaz (§ 2.14). **Bütün metin kapılarından geçti.** |

> Pilot hikâyenin `REVIEW` kategorisi taşımaması **bilinçli bir seçimdir**:
> ses kalibrasyonu, aynı anda en zor yaş kararını da vermek zorunda
> bırakılmamalıydı. Zor kararlar Faz 2'den itibaren, kalibre edilmiş bir
> sesle verilir.

### 2.2 · Faz 2 — ilk on beş hikâye

Hiçbiri `REVIEW` kategorisi taşımıyor; onbeşi de `IMPLY` seviyesindeki
şiddet/yas kategorileriyle yazıldı. Kayıt geriye dönük olarak Faz 3'te
tamamlandı — kapı o sırada bu bölümü henüz aramıyordu, ama **kayıt
tutulmamış olması incelemenin yapılmadığı anlamına gelmez ve tersi de
doğrudur**: ikisini ayırmak için defter artık sonucu yazar.

| # | Hikâye (`id`) | Durum | Uyarlama kararı ve sonucu |
|---:|---|---|---|
| 1 | `greek-persephone` | `cleared` | Kaynak kaçırılma sahnesiyle açar; anlatı **sonrasından** başlar (§ 2.8). Yumuşatma yok: kız alınmıştır, Demeter’in yası çözülmez, kış bedeldir. |
| 2 | `greek-arachne` | `cleared` | Ovidius’un dokumasındaki saldırı kataloğu **sayılmaz**, "tanrılar kötü davranıyordu" denir. Darbe tek cümle, sahne dönüşümdür (§ 2.1, § 2.8). |
| 3 | `greek-icarus` | `cleared` | Çocuk ölür ve babası onu gömer — hiçbiri saklanmaz. Boğulma tek cümle, beden betimlenmez (§ 2.2). |
| 4 | `norse-thors-hammer` | `cleared` | Þrymskviða’nın sonundaki öldürme iki cümlede **sonucuyla** verilir, sahnelenmez (§ 2.1). Şiirin asıl konusu olan kılık değiştirme komedisi bütün kalır. |
| 5 | `norse-idun-apples` | `cleared` | Þjazi’nin yanışı **söylenir**, betimlenmez (§ 2.1). Kaçırma, kapma anından değil Idun’un yokluğundan anlatılır. |
| 6 | `norse-fenrir-binding` | `cleared` | Týr elini kaybeder: tek cümle, yara yok (§ 2.1). Fenrir ölçeğiyle ve herkesin bildiği sonla korkutur, anatomiyle değil (§ 2.4). |
| 7 | `irish-cu-chulainn-name` | `cleared` | **Hayvana yönelen şiddet** — § 2.1 özel inceleme. Ne yaptığı ve neye mal olduğu söylenir; köpeğin yaraları betimlenmez. Çocuğun bedeli **üstlenmesi** hikâyenin dönümüdür. |
| 8 | `irish-children-of-lir` | `cleared` | **Üvey anne zulmü** (§ 2.9). Aoife’nin eylemi tek paragraf, cezası söylenir ve sahnelenmez; hikâye zulüm değil **dayanma** üzerinden taşınır. |
| 9 | `finnish-sampo` | `cleared` | Uyarlama gerekmedi. İşaretli kategori demirci ateşinden yükselen biçimler; siluetle ve etkiyle verilir, envanterlenmez (§ 2.4). |
| 10 | `finnish-kantele` | `cleared` | Uyarlama gerekmedi. Väinämöinen’in çalarken ağlaması kaynağın duygusal merkezidir; korunur ve **çözülmez** (§ 2.3). |
| 11 | `meso-gilgamesh-plant` | `cleared` | Destan avuntuyu reddeder ve anlatı da reddeder: bitki geri gelmez, ölümsüzlük olmaz. Kaynaktaki ceset betimi **yoktur** (§ 2.2). |
| 12 | `meso-etana-eagle` | `cleared` | Kartalın yavruları yemesi ve yılanın tuzağı **söylenir**, ikisi de sahnelenmez; kartalın açlığı tek cümle (§ 2.1, § 2.12). |
| 13 | `persian-zal-simorgh` | `cleared` | **Yenidoğanın terk edilmesi** (§ 2.9 · OMIT seviyesi). Korundu çünkü anlatının **kınadığı** haksızlık budur: iki cümle, zulüm sahnelenmez, Sām’ın utancı dönümdür. Ebeveyn kuştur, baba değil. |
| 14 | `persian-kaveh` | `cleared` | Zahhāk’ın yılanları: **olgu söylenir** — kral onları gençlerle besler — ne besleme ne iştah betimlenir (§ 2.1, § 2.6). Kāveh’in oğulları için yası bütün kalır. |
| 15 | `turkic-boghach-khan` | `cleared` | **Babanın oğlunu yaralaması** (§ 2.9). Korundu çünkü anlatının **çözdüğü** haksızlık budur: tek cümle, annenin arayışı dönümdür. Boğa dövüşü üç cümle ve tek duyu ayrıntısı (§ 2.1). |

### 2.3 · Faz 3 — ikinci on beş hikâye

Altısı `REVIEW` kategorisi taşıyor ve kapı bunları **adıyla** arıyor:
`hindu-hanuman-sun`, `hindu-ganga-descent`, `japanese-amaterasu-cave`,
`japanese-susanoo-orochi`, `yoruba-obatala-land`, `yoruba-osun-seventeenth`.

| # | Hikâye (`id`) | Durum | Uyarlama kararı ve sonucu |
|---:|---|---|---|
| 16 | `turkic-basat-tepegoz` | `cleared` | **Yamyamlık olaydır, sahne değildir** (§ 2.6 · IMPLY). Devin ne yediği söylenir — "giden atlılar dönmedi", "her aile oğullarını iki kez saydı" — ve yeme hiçbir yerde sahnelenmez. Kör etme **tek cümle** ve sonrası betimlenmez (§ 2.1). Anlatı Odysseia'ya tabi kılınmadı: çerçeve Oghuz çerçevesidir, benzerlik yalnızca kültürel notta ve **açık soru** olarak durur. Son paragraf yasla değil, gençlerin tartışmasıyla biter (§ 2.14). |
| 17 | `hindu-hanuman-sun` | `cleared` | **Yaşayan din** (§ 2.15). Metinde "myth" sözcüğü geçmiyor ve geçmiş zaman tuzağı yok; kültürel not şimdiki zamanda. Vajra darbesi **tek cümle** ve yara betimlenmiyor: "thunderbolt" atılır, çocuk düşer ve kalkmaz. Tanrıların armağanları bir **pazarlık** olarak veriliyor, mucize gösterisi olarak değil. İnancın doğruluğu hakkında hiçbir iddia yok. |
| 18 | `hindu-ganga-descent` | `cleared` | **Yaşayan din** (§ 2.15). Uyarlama gerekmedi; çerçeveleme gerekti. Altmış bin atanın külü **olgu olarak** söyleniyor, ölüm sahnelenmiyor. Ritüel talimatı, banyo prosedürü ve mantra **yok**. Kapanış nehri bugünkü hâliyle — şimdiki zamanda, insanlarıyla ve tartışmalarıyla — bırakıyor; bu § 2.15'in geçmiş zaman tuzağına verilen doğrudan cevaptır. |
| 19 | `chinese-nuwa-sky` | `cleared` | **Korkutucu imge** (§ 2.17 · ALLOW, ölçüyle). Kırık gökten geçen ateş ve su **etkiyle** anlatılıyor: sönmeyen ateş, çekilmeyen su, tepeye çıkan insanlar ve hayvanlar. Kaynağın felaket kataloğu envanterlenmiyor. Kaplumbağanın bacakları anlatının merkezindedir ve **yumuşatılmadı** — kaynakta ne varsa o söylendi, betimlenmedi. Kapanış bir tamir ve bir alet üzerinedir, dehşet üzerinde değil (§ 2.14). |
| 20 | `chinese-houyi-change` | `cleared` | **Ölüm ve yas** (§ 2.3). Dokuz güneşin düşürülmesi **söylenir**, sahnelenmez. Asıl yaş kararı ayrılıktır: Chang’e ile Hou Yi bir daha buluşmaz ve anlatı bunu **zorla mutlu sona çevirmez** — § 2.3 örtmeceyi ve zorla mutlu sonu ikisini birden yasaklar. Chang’e'nin gerekçesi **açık bırakıldı**, çünkü en eski metin de açık bırakıyor; varyantlar kültürel notta. Kapanış bir aile sofrasında, şimdiki zamanda. |
| 22 | `korean-jumong` | `cleared` | **Şiddet ve takip** (§ 2.1 · IMPLY). Kardeşlerin niyeti söylenir, kovalamaca sahnedir, **hiçbir öldürme ve hiçbir yara betimlenmez**. Nehir kenarında kimse ok atmaz: çözüm şiddetle değil **geçişle** gelir ve anlatının dönümü budur. Yuhwa'nın oğlunu göndermesi bir terk ediş olarak değil, bir **koruma** olarak kuruldu (§ 2.9). |
| 23 | `japanese-amaterasu-cave` | `cleared` | **Yaşayan din + doğaüstü korku** (§ 2.15, § 2.4). Susanoo'nun tahribatı **özetlenir**: pirinç tarlaları ve kanallar adıyla anılır, dokuma salonundaki şiddet tek cümlede "şiddetli bir şey yaptı ve bir kadın öldü" olarak verilir — atın derisinin yüzülmesi ve kadının ölümü **betimlenmez** (§ 2.1, § 2.2). Karanlık, ürkütücü değil **pratik** sonuçlarıyla anlatılır: pirinç olgunlaşmaz, böcekler çoğalır. Şinto yaşıyor: Ise şimdiki zamanda ve **ritüel içeriği olmadan** anılır; norito, kannushi uygulaması ve regalia geleneği **kullanılmadı**. |
| 24 | `japanese-susanoo-orochi` | `cleared` | **KURBAN — bu partinin en zor kararı** (§ 2.7 · IMPLY + inceleme). Yedi kızın alınmış olması **olaydır, sahne değildir**: okur bunu ağlayan iki ebeveynden öğrenir, hiçbir alınma anlatılmaz. Sekizinci kız hikâyede bir kurban değil bir **kişidir** — konuşulur, bakar, adı vardır. Yılan siluet ve ölçekle çizilir, envanterle değil (§ 2.4). Öldürme tek paragraf ve **sonucuyla** verilir; "nehir kızıl aktı" kaynağın kendi cümlesidir ve betim değil sonuçtur. Kılıç için § 2.16 uygulandı: kapalı olduğu **söylenir**, uydurulmaz — *"That is not a secret this book can open, and it is not going to guess."* |
| 25 | `vietnamese-lac-long-quan` | `cleared` | **Yas** (§ 2.3). Ayrılık kalıcıdır ve **onarılmadı**: § 2.3 hem örtmeceyi hem zorla mutlu sonu yasaklar, ve kaynak da onarmıyor. Çocukların ikiye ayrılması bir kayıp olarak değil, **açıkça anlatılmış bir karar** olarak kuruldu — kimse kandırılmaz, kimse kaçırılmaz, çocuklara sebebi söylenir ve üzülmelerine izin verilir. Son paragraf ayrılığı bugünkü bir bayrama bağlar; çözümsüz korku yok (§ 2.14). |
| 26 | `vietnamese-son-tinh-thuy-tinh` | `cleared` | **Savaş ve intikam** (§ 2.11 ALLOW, § 2.12). Dövüş **manzarayla** anlatılır: su yükselir, tepe yükselir. Hiçbir ölü, hiçbir yaralı, hiçbir ordu yok — *"Nobody was thrown at anybody and no army was involved."* İntikam yıllıktır ve **çözülmez**; kaynak da çözmüyor. Kapanış bir dağı gösteriyor: somut, bugün, işaret edilebilir. |
| 27 | `egyptian-horus-seth` | `cleared` | **Cinsellik — § 2.8 OMIT, İSTİSNASIZ.** Chester Beatty I'deki açık cinsel bölümler ve sakatlama **tamamen dışarıda**; anlatı mahkeme, kayık yarışı ve Isis'in kılık değiştirmesi üzerinden taşınıyor ve kaynak bunu bütünüyle destekliyor. Göz yaralanması **tek cümle**, sahne ise **iyileşmesi**: wedjat'ın kırılıp bütünlenen şey olarak okunması buradan geliyor. Seth kötü adam olarak düzleştirilmedi (§ 0.3) — ağlayan yabancıya iyi davranması ve mahkemeye kendi aleyhine rapor vermesi korundu. |
| 28 | `egyptian-isis-secret-name` | `cleared` | **Şiddet ve doğaüstü korku** (§ 2.1, § 2.4). Ra'nın acısı **tek paragrafta** ve anatomisiz: yanıyor, üşüyor, çenesi tutmuyor. Asıl karar § 2.16 ve SOURCING_STANDARD § 10: **gizli ad hiçbir nüshada yazmıyor ve kitap onu uydurmuyor.** Boşluk kapatılmadı, okura **gösterildi** — *"This book is not going to fill it in either."* Kapanış metnin neden hayatta kaldığını söylüyor: güzel olduğu için değil, işe yaradığı düşünüldüğü için. |
| 29 | `egyptian-shipwrecked-sailor` | `cleared` | **Yas ve ölüm** (§ 2.3, § 2.2). Yılanın yetmiş beş akrabasını kaybetmesi **tek kısa konuşmada** verilir ve **avutulmaz**: kaynağın kendi noktası, yılanın hâlâ orada olmasıdır. Anlatı bir teselli vaadiyle değil, **kırık bir çerçeveyle** biter — memurun cevabı ("ölmek üzere olan kuşa kim su verir?") kaynakta vardır ve silinmedi. Papirüsün sonunun kayıp olduğu okura **söylenir**; uydurulmuş bir kapanış eklenmedi (SOURCING_STANDARD § 10). |
| 30 | `yoruba-obatala-land` | `cleared` | **Yaşayan din + kültürel hassasiyet** (§ 2.15, § 2.16). **ENGELLİLİK AİTİYOLOJİSİ KULLANILMADI.** Birkaç anlatımda Ọbàtálá'nın yarım bıraktığı iş, engelli doğan insanların açıklaması olarak verilir; o açıklama kitapta **yoktur**, çünkü engelli okuru bir hata olarak çerçeveler. Yarım kalan iş **korundu** — kaynağın anlatısı budur; ona iliştirilen açıklama düşürüldü ve bu karar araştırma kaydında ve burada **yazılı**, çünkü okur ona başka yerde rastlayabilir. Ifá divinasyonu, odù içeriği ve ẹbọ talimatı **kullanılmadı**. Anlatım çokluğu gizlenmedi: iki şehrin farklı anlattığı okura söylendi. |
| 31 | `yoruba-osun-seventeenth` | `cleared` | **Yaşayan din + kültürel hassasiyet** (§ 2.15, § 2.16). Uyarlama gerekmedi; sınır gerekti. Ọ̀ṣun-Òṣogbo festivali **şimdiki zamanda** ve **dışarıdan görülebilen kadarıyla** anlatıldı: alay, kalabaş, davullar, kalabalık. İnisiyasyon içeriği, divinasyon prosedürü ve ẹbọ **yok**, ve metin bunu okura açıkça söylüyor — *"The part that is public is public. The rest belongs to the people who keep it."* İnancın doğruluğu hakkında hiçbir iddia yok. |

### 2.4 · Faz 4 — son on dört hikâye

Beşi `REVIEW` kategorisi taşıyor ve kapı bunları **adıyla** arıyor:
`aztec-fifth-sun`, `hawaiian-pele-journey`, ve `culturally-sensitive`
taşıyanlar. Kalanlar `IMPLY`/`ALLOW` seviyesinde uyarlandı.

| # | Hikâye (`id`) | Durum | Uyarlama kararı ve sonucu |
|---:|---|---|---|
| 32 | `akan-ananse-stories` | `cleared` | Uyarlama gerekmedi. İşaretli kategori `monsters` (§ 2.4 · ALLOW): eşekarısı, piton ve leopar **yakalanır, öldürülmez** ve hiçbiri betimlenmez — üçü de bir **soruyla** alt edilir. Anansesem'in kendisi çocukların önünde, akşamları anlatılan **açık** bir türdür; Rattray'in başka ciltlerdeki **kapalı** malzemesi (Altın Tabure töreni, adae, klan bilgisi) kullanılmadı. |
| 33 | `akan-ananse-wisdom` | `cleared` | **Hiçbir kategori taşımıyor** ve bu bilinçli bir seçimdir: yalnızca uyarlanmış hikâyelerden kurulu bir kitap, iyi seçmemiş bir kitaptır. Ananse kaybeder ve kaybı bir **çocuk** gösterir; ders veren kapanış yok, sonuç var (§ 2.2 · CHILDREN_WRITING_STYLE § 2.2). |
| 34 | `zulu-chameleon-message` | `cleared` | **ÖLÜM — § 2.2 ALLOW ve ÖRTMECE YASAK.** Anlatı insanların neden öldüğünü açıklıyor ve **yumuşatmıyor**: sözcük kullanılıyor, mesaj düz, son **onarılmıyor**. Unkulunkulu inip düzeltmiyor, bukalemun ikinci şans almıyor, kertenkele cezalandırılmıyor. Fikrini neden değiştirdiği **söylenmiyor** — bu bir boşluk değil, anlatıcıların bilerek koruduğu bir sessizliktir ve kitap onu doldurmadı. Son paragraf çözümsüz korku değil, bir **kayıt** taşıyor (§ 2.14). isangoma inisiyasyonu, muthi ve amadlozi pratiği **kullanılmadı**. |

<!-- /AGE-REVIEW:RECORDED -->

---

## 3. Bekleyen inceleme kuyruğu

Aşağıdaki hikâyeler yazılmadan önce ikinci bir göz gerektirir.
**Bu bölüm kapıyı BESLEMEZ** (§ 2'nin başındaki nota bakın).

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
