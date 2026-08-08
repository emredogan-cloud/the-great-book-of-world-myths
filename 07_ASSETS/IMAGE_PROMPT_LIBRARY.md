# IMAGE PROMPT LIBRARY — The Great Book of World Myths

<!-- OTOMATİK ÜRETİLDİ — 04_BUILD/make_prompts.py · ELLE DÜZENLEMEYİN -->

**68 görsel** · 45 hikâye açılışı · 22 kültür vinyeti · 1 harita

> Çalışma arayüzü: [`IMAGE_PROMPT_LIBRARY.html`](IMAGE_PROMPT_LIBRARY.html)
> — kopyalama düğmeleriyle. Bu dosya kayıt nüshasıdır.

## Akış

```
IMAGE_PROMPT_LIBRARY.html
      ↓  kurucu · GPT Image
07_ASSETS/raw/<id>.png                    ← HAM · ÜZERİNE ASLA YAZILMAZ
      ↓  04_BUILD/convert_images.py
07_ASSETS/processed/print/<id>.tif        ← 600 dpi gri TIFF
07_ASSETS/processed/kindle/<id>.png       ← dosya bütçesine optimize
07_ASSETS/processed/web/<id>.webp         ← A+ ve pazarlama
      ↓  04_BUILD/images.py --measure
06_REPORTS/tracked/image-consistency.json ← ölçüm depoda durur (K18)
```

**Kurucudan KDP'ye hazır dosya istenmez.** Ham çıktı PNG'dir; üretim
formatlarını hat türetir (karar K5).

## Üslup gövdesi — 68 promptta AYNI

```
black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches
```

## Olumsuz kısıtlar — AGE_POLICY § 2.17

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

> Yol haritası R4 (iade oranı): *"'Look Inside' örneğinde **gerçek** bir
> bölüm açılışı ve **gerçek** bir illüstrasyon."* Yani ilk illüstrasyonlar
> ebeveynin gördüğü ilk şeydir.

---

## `story-001` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-001` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-001.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-001.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-001.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-001.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-001.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-002` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-002` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-002.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-002.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-002.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-002.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-002.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-003` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-003` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-003.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-003.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-003.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-003.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-003.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-004` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-004` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-004.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-004.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-004.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-004.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-004.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-005` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-005` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-005.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-005.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-005.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-005.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-005.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-006` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-006` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-006.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-006.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-006.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-006.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-006.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-007` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-007` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-007.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-007.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-007.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-007.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-007.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-008` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-008` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-008.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-008.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-008.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-008.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-008.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-009` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-009` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-009.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-009.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-009.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-009.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-009.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-010` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-010` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-010.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-010.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-010.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-010.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-010.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-011` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-011` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-011.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-011.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-011.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-011.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-011.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-012` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-012` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-012.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-012.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-012.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-012.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-012.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-013` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-013` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-013.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-013.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-013.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-013.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-013.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-014` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-014` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-014.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-014.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-014.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-014.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-014.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-015` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-015` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-015.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-015.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-015.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-015.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-015.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-016` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-016` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-016.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-016.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-016.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-016.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-016.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-017` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-017` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-017.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-017.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-017.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-017.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-017.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-018` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-018` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-018.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-018.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-018.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-018.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-018.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-019` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-019` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-019.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-019.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-019.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-019.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-019.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-020` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-020` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-020.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-020.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-020.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-020.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-020.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-021` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-021` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-021.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-021.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-021.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-021.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-021.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-022` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-022` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-022.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-022.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-022.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-022.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-022.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-023` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-023` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-023.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-023.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-023.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-023.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-023.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-024` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-024` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-024.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-024.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-024.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-024.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-024.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-025` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-025` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-025.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-025.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-025.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-025.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-025.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-026` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-026` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-026.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-026.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-026.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-026.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-026.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-027` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-027` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-027.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-027.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-027.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-027.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-027.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-028` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-028` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-028.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-028.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-028.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-028.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-028.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-029` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-029` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-029.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-029.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-029.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-029.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-029.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-030` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-030` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-030.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-030.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-030.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-030.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-030.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-031` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-031` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-031.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-031.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-031.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-031.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-031.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-032` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-032` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-032.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-032.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-032.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-032.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-032.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-033` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-033` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-033.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-033.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-033.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-033.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-033.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-034` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-034` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-034.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-034.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-034.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-034.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-034.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-035` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-035` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-035.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-035.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-035.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-035.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-035.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-036` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-036` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-036.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-036.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-036.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-036.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-036.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-037` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-037` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-037.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-037.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-037.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-037.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-037.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-038` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-038` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-038.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-038.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-038.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-038.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-038.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-039` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-039` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-039.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-039.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-039.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-039.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-039.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-040` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-040` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-040.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-040.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-040.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-040.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-040.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-041` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-041` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-041.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-041.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-041.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-041.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-041.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-042` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-042` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-042.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-042.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-042.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-042.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-042.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-043` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-043` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-043.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-043.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-043.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-043.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-043.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-044` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-044` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-044.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-044.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-044.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-044.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-044.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `story-045` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-045` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Hikâye açılış çizimi — sayfanın üst yarısı |
| OUTPUT_FILENAME | `story-045.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/story-045.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/story-045.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/story-045.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/story-045.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 2400 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 3:2 (yatay) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Hikâyenin ilk sayfasının üst yarısı |
| STATUS | `blocked-on-inventory` |
| NOTES | Hikâye envanteri kilitlenmeden konu yazılamaz (DECISIONS § A3). |

**PROMPT**

```
PENDING — story inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. upper half of a 6x9 inch page. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-001` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-001` |
| STORY_ID | `—` |
| CULTURE_ID | `inuit` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-001.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-001.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-001.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-001.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-001.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Inuit tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. visual detail drawn from inuit material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-002` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-002` |
| STORY_ID | `—` |
| CULTURE_ID | `korean` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-002.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-002.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-002.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-002.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-002.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Korean tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. visual detail drawn from korean material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-003` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-003` |
| STORY_ID | `—` |
| CULTURE_ID | `persian` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-003.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-003.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-003.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-003.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-003.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Persian tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. visual detail drawn from persian material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-004` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-004` |
| STORY_ID | `—` |
| CULTURE_ID | `polynesian` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-004.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-004.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-004.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-004.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-004.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Polynesian tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. visual detail drawn from polynesian material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-005` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-005` |
| STORY_ID | `—` |
| CULTURE_ID | `turkic` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-005.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-005.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-005.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-005.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-005.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Turkic tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. visual detail drawn from turkic material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-006` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-006` |
| STORY_ID | `—` |
| CULTURE_ID | `west-african` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-006.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-006.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-006.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-006.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-006.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `pending` |

**PROMPT**

```
a small emblem for West African tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. visual detail drawn from west-african material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-007` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-007` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-007.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-007.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-007.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-007.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-007.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `blocked-on-inventory` |
| NOTES | 22 kültür kilitlenmeden vinyet konusu yazılamaz (DECISIONS § A2). |

**PROMPT**

```
PENDING — culture inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-008` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-008` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-008.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-008.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-008.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-008.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-008.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `blocked-on-inventory` |
| NOTES | 22 kültür kilitlenmeden vinyet konusu yazılamaz (DECISIONS § A2). |

**PROMPT**

```
PENDING — culture inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-009` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-009` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-009.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-009.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-009.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-009.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-009.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `blocked-on-inventory` |
| NOTES | 22 kültür kilitlenmeden vinyet konusu yazılamaz (DECISIONS § A2). |

**PROMPT**

```
PENDING — culture inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-010` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-010` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-010.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-010.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-010.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-010.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-010.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `blocked-on-inventory` |
| NOTES | 22 kültür kilitlenmeden vinyet konusu yazılamaz (DECISIONS § A2). |

**PROMPT**

```
PENDING — culture inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-011` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-011` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-011.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-011.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-011.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-011.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-011.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `blocked-on-inventory` |
| NOTES | 22 kültür kilitlenmeden vinyet konusu yazılamaz (DECISIONS § A2). |

**PROMPT**

```
PENDING — culture inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-012` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-012` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-012.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-012.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-012.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-012.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-012.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `blocked-on-inventory` |
| NOTES | 22 kültür kilitlenmeden vinyet konusu yazılamaz (DECISIONS § A2). |

**PROMPT**

```
PENDING — culture inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-013` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-013` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-013.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-013.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-013.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-013.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-013.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `blocked-on-inventory` |
| NOTES | 22 kültür kilitlenmeden vinyet konusu yazılamaz (DECISIONS § A2). |

**PROMPT**

```
PENDING — culture inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-014` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-014` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-014.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-014.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-014.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-014.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-014.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `blocked-on-inventory` |
| NOTES | 22 kültür kilitlenmeden vinyet konusu yazılamaz (DECISIONS § A2). |

**PROMPT**

```
PENDING — culture inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-015` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-015` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-015.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-015.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-015.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-015.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-015.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `blocked-on-inventory` |
| NOTES | 22 kültür kilitlenmeden vinyet konusu yazılamaz (DECISIONS § A2). |

**PROMPT**

```
PENDING — culture inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-016` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-016` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-016.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-016.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-016.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-016.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-016.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `blocked-on-inventory` |
| NOTES | 22 kültür kilitlenmeden vinyet konusu yazılamaz (DECISIONS § A2). |

**PROMPT**

```
PENDING — culture inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-017` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-017` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-017.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-017.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-017.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-017.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-017.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `blocked-on-inventory` |
| NOTES | 22 kültür kilitlenmeden vinyet konusu yazılamaz (DECISIONS § A2). |

**PROMPT**

```
PENDING — culture inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-018` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-018` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-018.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-018.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-018.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-018.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-018.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `blocked-on-inventory` |
| NOTES | 22 kültür kilitlenmeden vinyet konusu yazılamaz (DECISIONS § A2). |

**PROMPT**

```
PENDING — culture inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-019` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-019` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-019.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-019.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-019.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-019.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-019.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `blocked-on-inventory` |
| NOTES | 22 kültür kilitlenmeden vinyet konusu yazılamaz (DECISIONS § A2). |

**PROMPT**

```
PENDING — culture inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-020` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-020` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-020.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-020.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-020.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-020.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-020.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `blocked-on-inventory` |
| NOTES | 22 kültür kilitlenmeden vinyet konusu yazılamaz (DECISIONS § A2). |

**PROMPT**

```
PENDING — culture inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-021` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-021` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-021.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-021.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-021.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-021.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-021.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `blocked-on-inventory` |
| NOTES | 22 kültür kilitlenmeden vinyet konusu yazılamaz (DECISIONS § A2). |

**PROMPT**

```
PENDING — culture inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `culture-022` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-022` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Kültür vinyeti — kültür kartında |
| OUTPUT_FILENAME | `culture-022.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/culture-022.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/culture-022.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/culture-022.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/culture-022.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 1600 px |
| EXPECTED_HEIGHT | 1600 px |
| ASPECT | 1:1 (kare) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Kültür kartı (DECISIONS § A4) |
| STATUS | `blocked-on-inventory` |
| NOTES | 22 kültür kilitlenmeden vinyet konusu yazılamaz (DECISIONS § A2). |

**PROMPT**

```
PENDING — culture inventory is Phase 1's first task. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. small spot illustration, no frame. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features
```

## `map-001` — Dünya haritası — 22 kültürün konumu

| Alan | Değer |
|---|---|
| ID | `map-001` |
| STORY_ID | `—` |
| CULTURE_ID | `—` |
| PURPOSE | Dünya haritası — 22 kültürün konumu |
| OUTPUT_FILENAME | `map-001.png` |
| RAW_OUTPUT_PATH | `07_ASSETS/raw/map-001.png` |
| PROCESSED_PRINT | `07_ASSETS/processed/print/map-001.tif` |
| PROCESSED_KINDLE | `07_ASSETS/processed/kindle/map-001.png` |
| PROCESSED_WEB | `07_ASSETS/processed/web/map-001.webp` |
| FORMAT | PNG |
| EXPECTED_WIDTH | 4800 px |
| EXPECTED_HEIGHT | 2400 px |
| ASPECT | 2:1 (açık sayfa) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Ön veya arka iç kapak (açık sayfa) |
| STATUS | `pending` |
| NOTES | Yer adları DİZGİDE eklenir, çizimde değil — böylece 5 dil sürümünde harita yeniden üretilmez. |

**PROMPT**

```
a hand-drawn world map marking the homelands of the 22 cultures in this book, in the manner of an old chart but honest about coastlines. black and white pen-and-ink illustration for a children's book, confident varied line weight, open uncluttered composition, generous white space, warm and inviting rather than frightening, no cross-hatching denser than the eye can read at 6x9 inches. double-page spread map. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no place labels (typeset separately)
```

---

*Bu dosya `04_BUILD/make_prompts.py` tarafından üretilir.*
