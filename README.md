# The Great Book of World Myths

**45 Stories of Gods, Heroes, and Monsters from 22 Cultures — Retold for
Young Readers (Ages 8–12)**

[![validate](https://github.com/emredogan-cloud/the-great-book-of-world-myths/actions/workflows/validate.yml/badge.svg)](https://github.com/emredogan-cloud/the-great-book-of-world-myths/actions/workflows/validate.yml)
[![images](https://github.com/emredogan-cloud/the-great-book-of-world-myths/actions/workflows/images.yml/badge.svg)](https://github.com/emredogan-cloud/the-great-book-of-world-myths/actions/workflows/images.yml)

---

## Bu depo nedir

Bu depo bir **kitap üretim sistemidir**, kitabın kendisi değil.

Çocuk mitoloji rafının yaklaşık %80'i Yunan'dır. Bir çocuk Yunan mitlerini
bitirdiğinde önüne konan şey genellikle başka bir Yunan kitabı olur. Bu
kitap 22 kültürden 45 hikâyeyi aynı ciltte, aynı kalitede, 8–12 yaş için
yeniden anlatır.

Depoda duran şey: **araştırma künyeleri, doğrulama kapıları, CI/CD, dizgi
ve KDP üretim hattı, görsel işleme hattı, ölçüm raporları ve belgeler.**

Depoda **durmayan** şey: **kitabın prozası.** Yayımlanmamış manuscript
depo dışında yaşar — `.gitignore` § ① ve
[`DECISIONS.md` § A1](DECISIONS.md). Bir yol kalıbı yeni bir ada konan
dosyayı yakalamaz, bu yüzden ikinci bir hat vardır: CI takip edilen
dosyaların **içeriğine** bakar ve hikâye metni görürse kırmızı yanar.

---

## Durum

| | |
|---|---|
| Faz | **0 · Bootstrap** |
| Kapı (`.gate`) | `phase0` |
| Yazılmış hikâye | 0 / 45 |
| Kilitlenmiş kültür | 0 / 22 |
| Görsel | 0 / 68 |
| Sonraki adım | **Faz 1 — kurucu onayı bekliyor** |

Ölçülmüş güncel durum: [`BOOK_STATS.md`](BOOK_STATS.md) ·
[`ROADMAP_PROGRESS.md`](ROADMAP_PROGRESS.md)

---

## Hızlı başlangıç

```bash
git clone https://github.com/emredogan-cloud/the-great-book-of-world-myths.git
cd the-great-book-of-world-myths

# Bütün kalite kapıları — CI'ın koştuğu komutun birebir aynısı.
# Hiçbiri venv gerektirmez; hepsi Python standart kütüphanesiyle koşar.
./04_BUILD/qa_all.sh

# Ağır işler (görsel ölçümü, dizgi) için:
python3 -m venv 04_BUILD/.venv
04_BUILD/.venv/bin/pip install -r 04_BUILD/requirements.txt
```

Yeşilse CI de yeşil olur. Kırmızıysa ilerleme yoktur.

---

## Dizin yapısı

```
00_CONTEXT/     proje bağlamı, üslup, editoryal mimari, Bestiarium dersleri
01_RESEARCH/    kültür ve hikâye dizinleri, araştırma kayıtları, künyeler
02_MANUSCRIPT/  kitabın prozası — DEPO DIŞINDA (.gitignore § ①)
03_EDITORIAL/   yaş incelemesi, ebeveyn okumaları, düzeltme kayıtları
04_BUILD/       bütün üretim ve doğrulama araçları
05_TESTS/       kapıların KENDİ testi — kasıtlı kusurlu kurgu kitap
06_REPORTS/     ölçüm raporları (tracked/ altındakiler depoda durur)
07_ASSETS/      görseller: raw/ (ham PNG) → processed/ (üretim formatları)
08_OUTPUT/      nihai KDP dosyaları — üretilir, depoda durmaz
09_ARCHIVE/     düşürülen malzeme ve gerekçeleri
```

---

## Kalite kapıları

| Kapı | Ne ölçer |
|---|---|
| `validate_spec.py` | şema, kimlik bütünlüğü, kültür/hikâye sayısı, ölü kural avı |
| `validate_structure.py` | depo bütünlüğü, belge bağları, **manuscript sızıntısı** |
| `validate_research.py` | kaynak tamlığı, künye bütünlüğü, kısıtlılık taraması |
| `qa_age.py` | **yaş politikası** — grafik betimleme, yetişkin sözcük dağarcığı |
| `qa_readability.py` | 8–12 yaş okuma seviyesi, cümle uzunluğu, zor sözcük oranı |
| `qa_length.py` | hikâye kelime bandı |
| `qa_voice.py` | ses, yasak kalıp, noktalama |
| `qa_drift.py` | üslup sürüklenmesi |
| `qa_echo.py` | hikâyeler arası birebir tekrar |
| `qa_diacritics.py` | diakritik ve adlandırma tutarlılığı |
| `qa_crossref.py` | telaffuz · sözlük · kültürel not kapsamı |
| `page_budget.py` | deterministik sayfa modeli |
| `05_TESTS/selftest.py` | **kapıların gerçekten ısırdığının kanıtı** |

Son satır en önemlisidir. Metin yokken yeşil kalan bir hat, kusur
geldiğinde de yeşil kalabilir. `selftest.py` kasıtlı kusurlu bir kurgu
kitap çalıştırır ve her kapının o kusuru **yakaladığını** kanıtlar.

---

## Faz yapısı

| Faz | Başlık | Hikâye | Kümülatif | Etiket |
|---:|---|---:|---:|---|
| 1 | Temel · Kapsam, Araştırma Mimarisi, Ses Kalibrasyonu | 1 | 1/45 | `v0.1.0` |
| 2 | Çekirdek Yazım · İlk On Beş | 15 | 16/45 | `v0.2.0` |
| 3 | Genişleme · İkinci On Beş | 15 | 31/45 | `v0.3.0` |
| 4 | Tamamlama · Son On Dört + Editoryal İnceleme | 14 | **45/45** | `v0.4.0` |
| 5 | Üretim · Dizgi, KDP Dosyaları, Lansman | — | 45/45 | `v1.0.0` |

Tam plan: [`THE_GREAT_BOOK_OF_WORLD_MYTHS_MASTER_ROADMAP.md`](THE_GREAT_BOOK_OF_WORLD_MYTHS_MASTER_ROADMAP.md)

---

## Bu proje neden farklı yazılıyor

Bu, yetişkin bir mitoloji cildinin basitleştirilmiş hâli **değildir**.
Master yayıncılık yol haritası bunu açıkça söyler:

> *"Şiddet ve trajedi saklanmaz ama sahnelenmez: sonuç anlatılır, dehşet
> betimlenmez. Bu yetişkin cildinin bilinçli tersidir ve **ayrı bir yazım
> işidir — çeviri değil**."*

Ve projenin tanımlayıcı riskini de adıyla koyar:

> *"Mitler acımasızdır. Yanlış tonlanmış bir sahne, ebeveyn yorumunda
> 'çocuğum için fazla karanlık' olarak geri döner — ve **bu yorum
> silinemez**."*

Bu yüzden [`AGE_POLICY.md`](AGE_POLICY.md) bu projede bir ek belge değil,
**CI kapısı olan birinci sınıf bir sistemdir**. Amaç kültürel sterilizasyon
değildir; amaç **yaşa uygun yeniden anlatımdır**.

---

## Lisans

Kod ve üretim araçları: **MIT** ([`LICENSE`](LICENSE)).

Kitabın metni, illüstrasyonları ve tasarımı lisansın **kapsamı dışındadır**
ve tüm hakları saklıdır.

---

## İlgili projeler

- **Codex Mythologica** — yetişkin cildi (Cilt I)
- **Codex Bestiarium** — yetişkin bestiyer (Cilt II) · bu projenin
  **referans uygulamasıdır**, dersler
  [`00_CONTEXT/LESSONS_FROM_CODEX_BESTIARIUM.md`](00_CONTEXT/LESSONS_FROM_CODEX_BESTIARIUM.md)'de.
  Bu depo ondan **tamamen bağımsızdır** ve onsuz da çalışır.
