# ARAŞTIRMA KAYDI ŞABLONU

> Her hikâyenin `01_RESEARCH/research/<story-id>.md` altında bir kaydı
> vardır. Kayıtlar `04_BUILD/research_gen.py` tarafından
> `story_index.json`'dan **üretilir** — elle düzenlenmez, bir sonraki
> üretimde kaybolur.
>
> Elle yazılan şey `story_index.json`'ın kendisidir; bu dosya onun
> **okunabilir yüzüdür** ve kaynak doğrulamasının denetlenebilmesi için
> vardır.
>
> Ölçüt: [`SOURCING_STANDARD.md`](../SOURCING_STANDARD.md)

---

## Üretilen kaydın yapısı

```markdown
# <Başlık> — araştırma kaydı

<!-- OTOMATİK ÜRETİLDİ — 04_BUILD/research_gen.py
     Kaynak: 01_RESEARCH/story_index.json
     ELLE DÜZENLEMEYİN — bir sonraki üretimde kaybolur. -->

| Alan | Değer |
|---|---|
| **id** | `<slug>` |
| **Başlık (EN)** | … |
| **Kültür** | … (makro bölge) |
| **Bölge** | … |
| **Bölüm** | … |
| **Durum** | `verified` |
| **Görsel** | `story-007` |
| **Kelime hedefi** | 950 |

## 1. Kaynaklar
### Kaynak 1 · `primary` · doğrulama `canon`
- **Künye:** …
- **Yer:** …
### Kaynak 2 · `scholarly` · doğrulama `article`
…

**Kapı durumu:** ≥2 bağımsız ✅ · ≥1 primary/scholarly ✅ · ≥1 güçlü doğrulama ✅

## 2. Kanonik anlatım
- **Seçilen:** …
- **Gerekçe:** …
- **Bilinen varyantlar:** …
- **Okura söylenecek (kültürel not):** …

## 3. Kısıtlılık taraması        ← MUAFİYETSİZ
- **Tarandı:** ✅
- **Sonuç:** <açık bir cümle — ne arandı, ne bulundu, ne yapıldı>

## 4. Yaş uyarlaması             ← AGE_POLICY
- **İçerik işaretleri:** violence, death, sacrifice
- **Politika seviyeleri:** IMPLY, ALLOW, IMPLY+REVIEW
- **Uyarlama notu:** <kaynakta olan, kitapta olmayan/örtülen ne>
- **İnceleme durumu:** `cleared`

## 5. Kişiler                    ← "kim kimdir" sözlüğünü besler
| Ad | Rol | Sözlükte |
|---|---|---|

## 6. Telaffuz                   ← telaffuz rehberini besler
| Ad | Telaffuz | IPA | Kaynak |
|---|---|---|---|

## 7. Olay örgüsü — dört hareket
- **① Kapı:** …
- **② Baskı:** …
- **③ Dönüm:** …
- **④ Sonuç:** …

## 8. Olgusal iddialar ve kaynakları
| İddia | Kaynak |
|---|---|

## 9. Temalar ve motifler
- Temalar: …
- Motif kodu (bilgi — kapı değil): …
```

---

## Zorunlu alanlar — kapıya bağlı

`04_BUILD/validate_research.py` şunları arar ve **boş bırakılamaz**:

| Alan | Kural |
|---|---|
| `sources` | ≥2 bağımsız (`index`/`retelling` sayılmaz), ≥1 `primary`/`scholarly`, ≥1 güçlü doğrulama |
| `canonicalVersion` | Hangi anlatım seçildi |
| `canonicalRationale` | **Neden.** "Daha yumuşak olduğu için" tek başına geçersiz |
| `restrictionScreened` | `true` — muafiyet yok |
| `restrictionNote` | ≥20 karakter, açık cümle |
| `ageReviewStatus` | `pending` dışında bir değer (Faz 1'de `pending` kabul, yazımdan sonra değil) |
| `contentFlags` | AGE_POLICY'nin 17 kategorisinden hangileri |
| `ageAdaptationNote` | `contentFlags` bir `IMPLY`/`OMIT`/`REVIEW` kategorisi içeriyorsa **zorunlu** |
| `characters` | ≥1, sözlüğü besler |
| `pronunciationEntries` | Hikâyedeki **her** özel ad, `pronunciationSource` ile |
| `factualClaims[].sourceRef` | `sources[].ref` değerlerinden birine denk gelmeli |

---

## Yasaklar — hatırlatma

- Görmediğin sayfa numarasını yazma
- Başka bir **yeniden anlatımı** kaynak sayma
- İki ansiklopediyi iki bağımsız kaynak sayma
- Telaffuz uydurma
- **Mitin boşluğunu anlatı akıcılığı için doldurma**

> *"Never invent mythology. Never invent historical claims. Never
> fabricate references."* — ve bir ekle: **hikâye uydurulmaz.**
