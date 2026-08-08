# CHANGELOG — The Great Book of World Myths

Bu dosya [Keep a Changelog](https://keepachangelog.com/tr/1.1.0/) biçimini
izler ve [Semantic Versioning](https://semver.org/lang/tr/) kullanır.

Her faz **ancak etiketlenerek kapanır** ve her etiketin burada bir bloğu
olmak zorundadır — `release.yml` bunu denetler.

---

## [Yayımlanmamış]

### Sıradaki

- **Faz 1 · Temel** (kapsam kilidi · 45 araştırma kaydı · ses kalibrasyon
  pilotu) — **kurucu onayı bekliyor**

Onay istenen belge: [`PHASE_1_APPROVAL_REQUEST.md`](PHASE_1_APPROVAL_REQUEST.md)

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
