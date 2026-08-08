# ROADMAP PROGRESS — The Great Book of World Myths

<!-- OTOMATİK ÜRETİLDİ — 04_BUILD/update_docs.py · ELLE DÜZENLEMEYİN -->

> Kapı: `phase1` · etiketler için GitHub Releases'e bakın

Kaynak: [`THE_GREAT_BOOK_OF_WORLD_MYTHS_MASTER_ROADMAP.md`](THE_GREAT_BOOK_OF_WORLD_MYTHS_MASTER_ROADMAP.md)

## Faz durumu

| Faz | Başlık | Yazım ilerlemesi | Kilometre taşı | Etiket |
|---:|---|---|---|---|
| **1** | Temel · Kapsam, Araştırma Mimarisi ve Ses Kalibrasyonu | `████████████████` 1/1 (%100) | 1 hikâye · 0 görsel | `v0.1.0` |
| **2** | Çekirdek Yazım · İlk On Beş Hikâye | `█████████████░░░` 13/16 (%81) | 15 hikâye · 16 görsel | `v0.2.0` |
| **3** | Genişleme · İkinci On Beş Hikâye | `███████░░░░░░░░░` 13/31 (%41) | 15 hikâye · 40 görsel | `v0.3.0` |
| **4** | Tamamlama · Son On Dört Hikâye ve Editoryal İnceleme | `█████░░░░░░░░░░░` 13/45 (%28) | 14 hikâye · 68 görsel | `v0.4.0` |
| **5** | Üretim · Dizgi, KDP Dosyaları ve Lansman | `█████░░░░░░░░░░░` 13/45 (%28) | 0 hikâye · 68 görsel | `v1.0.0` |

## Kapı durumu

Aktif kapı: **`phase1`** · sıra 2/7

| Kapı | Komut | Ne zaman açılır |
|---|---|---|
| Yapılandırma ve veri | `validate_spec.py` | her push |
| Depo ve belge | `validate_structure.py` | her push |
| Manuscript sızıntısı | `validate_structure.py` | her push |
| Kapıların kendi testi | `05_TESTS/selftest.py` | her push |
| Araştırma | `validate_research.py` | Faz 1'den itibaren |
| Kelime bandı | `qa_length.py` | metin geldiğinde |
| **Yaş politikası** | `qa_age.py` | metin geldiğinde |
| **Okunabilirlik** | `qa_readability.py` | metin geldiğinde |
| Ses ve yasak kalıp | `qa_voice.py` | metin geldiğinde |
| Tekrar | `qa_echo.py` | metin geldiğinde |
| Diakritik | `qa_diacritics.py` | her zaman |
| Çapraz referans | `qa_crossref.py` | her zaman |
| Sürüklenme | `qa_drift.py` | her 5 hikâyede |
| Sayfa bütçesi | `page_budget.py` | her zaman · Faz 4'ten itibaren HATA |
| Görsel | `images.py --measure` | görsel geldiğinde |

## Envanter

| | Ölçülen | Hedef |
|---|---:|---:|
| Kilitli kültür | 22 | 22 |
| Kilitli hikâye | 45 | 45 |
| Yazılmış hikâye | 13 | 45 |

## Sonraki eylem

**Faz 1 yürürlükte.** 13/45 hikâye yazıldı.

Tek seferde en fazla üç hikâye — daha fazlası üslup sürüklenmesi üretir.

---

*Bu dosya `04_BUILD/update_docs.py` tarafından üretilir.*
