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
black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small
```

## Olumsuz kısıtlar — AGE_POLICY § 2.17

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

> Yol haritası R4 (iade oranı): *"'Look Inside' örneğinde **gerçek** bir
> bölüm açılışı ve **gerçek** bir illüstrasyon."* Yani ilk illüstrasyonlar
> ebeveynin gördüğü ilk şeydir.

---

## `story-001` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-001` |
| STORY_ID | `greek-persephone` |
| CULTURE_ID | `greek` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Girl Who Ate Six Seeds”: Persephone admits she ate six seeds below, and six seeds cannot be given back. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from greek material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-002` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-002` |
| STORY_ID | `greek-arachne` |
| CULTURE_ID | `greek` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Weaver Who Would Not Look Down”: The goddess drops her disguise, and Arachne's cloth turns out to be the better one. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from greek material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-003` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-003` |
| STORY_ID | `greek-icarus` |
| CULTURE_ID | `greek` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “Wings Made in a Locked Room”: The boy climbs past the height his father warned him about. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from greek material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-004` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-004` |
| STORY_ID | `norse-thors-hammer` |
| CULTURE_ID | `norse` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Bride Who Ate an Ox”: Thor agrees to wear the bridal veil himself, and the giant asks why the bride eats so much. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from norse material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-005` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-005` |
| STORY_ID | `norse-idun-apples` |
| CULTURE_ID | `norse` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Goddess Who Kept the Apples”: Loki borrows a falcon shape and carries her home as a nut in his claws. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from norse material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-006` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-006` |
| STORY_ID | `norse-fenrir-binding` |
| CULTURE_ID | `norse` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Ribbon That Held a Wolf”: Fenrir will try it only if a god puts a hand in his mouth, and Tyr does. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from norse material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-007` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-007` |
| STORY_ID | `irish-cu-chulainn-name` |
| CULTURE_ID | `irish` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Boy Who Took the Hound’s Place”: The boy kills the hound, and then offers the smith the only fair thing he has. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from irish material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-008` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-008` |
| STORY_ID | `irish-children-of-lir` |
| CULTURE_ID | `irish` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “Nine Hundred Years on the Water”: Fionnuala decides that if they cannot be saved they will at least not be separated. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from irish material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-009` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-009` |
| STORY_ID | `finnish-sampo` |
| CULTURE_ID | `finnish` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Machine Nobody Can Describe”: Ilmarinen stops asking what it is and forges it anyway. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from finnish material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-010` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-010` |
| STORY_ID | `finnish-kantele` |
| CULTURE_ID | `finnish` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Harp Made from a Fish”: Väinämöinen strings it, and the sound stops the forest. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from finnish material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-011` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-011` |
| STORY_ID | `meso-gilgamesh-plant` |
| CULTURE_ID | `mesopotamian` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Plant at the Bottom of the Sea”: He surfaces with it, stops to wash, and a snake takes it from the bank. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from mesopotamian material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-012` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-012` |
| STORY_ID | `meso-etana-eagle` |
| CULTURE_ID | `mesopotamian` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Eagle and the Snake Who Swore an Oath”: A king who wants a child finds the broken eagle in a pit and feeds him anyway. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from mesopotamian material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-013` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-013` |
| STORY_ID | `persian-zal-simorgh` |
| CULTURE_ID | `persian` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Baby Left on the Mountain”: Years later the father climbs back up, and the boy has to choose. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from persian material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-014` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-014` |
| STORY_ID | `persian-kaveh` |
| CULTURE_ID | `persian` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Blacksmith’s Apron”: He tears the paper in front of the court and walks out with his apron on a pole. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from persian material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-015` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-015` |
| STORY_ID | `turkic-boghach-khan` |
| CULTURE_ID | `turkic` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Boy Who Fought the Bull”: A bull is loosed in the assembly ground and the boy takes his fist away from its forehead. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from turkic material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-016` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-016` |
| STORY_ID | `turkic-basat-tepegoz` |
| CULTURE_ID | `turkic` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The One-Eyed Giant of the Oghuz”: Basat, who was raised by a lion and is not afraid of what the others fear, goes up alone. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from turkic material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-017` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-017` |
| STORY_ID | `hindu-hanuman-sun` |
| CULTURE_ID | `hindu` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Baby Who Mistook the Sun for Fruit”: A thunderbolt knocks him out of the sky, and his father the wind stops moving anywhere on earth. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from hindu material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-018` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-018` |
| STORY_ID | `hindu-ganga-descent` |
| CULTURE_ID | `hindu` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The River That Had to Be Slowed Down”: Śiva steps under the fall and lets it land in his hair, where it slows. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from hindu material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-019` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-019` |
| STORY_ID | `chinese-nuwa-sky` |
| CULTURE_ID | `chinese` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Woman Who Patched the Sky”: Nüwa gathers stones of five colours and melts them into a patch. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from chinese material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-020` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-020` |
| STORY_ID | `chinese-houyi-change` |
| CULTURE_ID | `chinese` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Archer and the Woman on the Moon”: Chang'e swallows it — and every teller disagrees about why. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from chinese material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-021` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-021` |
| STORY_ID | `korean-dangun` |
| CULTURE_ID | `korean` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Bear Who Waited in the Dark”: The tiger leaves on the twentieth day; the bear does not. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from korean material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-022` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-022` |
| STORY_ID | `korean-jumong` |
| CULTURE_ID | `korean` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Boy Who Told the Fish to Rise”: He reaches a river with no bridge, says who his father was, and the fish come up. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from korean material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-023` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-023` |
| STORY_ID | `japanese-amaterasu-cave` |
| CULTURE_ID | `japanese` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Door That Was Opened by Laughing”: Uzume dances on an upturned tub until every god is roaring with laughter. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from japanese material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-024` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-024` |
| STORY_ID | `japanese-susanoo-orochi` |
| CULTURE_ID | `japanese` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “Eight Heads and Eight Bowls of Wine”: He builds a fence with eight gates and puts a vat of strong wine behind each one. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from japanese material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-025` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-025` |
| STORY_ID | `vietnamese-lac-long-quan` |
| CULTURE_ID | `vietnamese` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Hundred Children in the Egg Sac”: They divide the children — fifty to the coast, fifty to the highlands — and agree to come when called. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from vietnamese material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-026` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-026` |
| STORY_ID | `vietnamese-son-tinh-thuy-tinh` |
| CULTURE_ID | `vietnamese` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “Why the River Rises Every Year”: The mountain spirit gets there at dawn, and the water spirit gets there just after. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from vietnamese material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-027` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-027` |
| STORY_ID | `egyptian-horus-seth` |
| CULTURE_ID | `egyptian` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “Eighty Years of Arguing”: Isis disguises herself as an old woman and gets Seth to argue himself into a corner. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from egyptian material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-028` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-028` |
| STORY_ID | `egyptian-isis-secret-name` |
| CULTURE_ID | `egyptian` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Name the Sun God Would Not Say”: Isis can cure him, and names her price: the name he has never told anyone. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from egyptian material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-029` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-029` |
| STORY_ID | `egyptian-shipwrecked-sailor` |
| CULTURE_ID | `egyptian` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Island That Was Not There Afterwards”: An enormous serpent picks him up, and instead of eating him, tells him what happened to his own family. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from egyptian material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-030` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-030` |
| STORY_ID | `yoruba-obatala-land` |
| CULTURE_ID | `yoruba` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Chain Let Down from the Sky”: He pours the earth, the hen scratches it wide — and then he stops, and the work is left half done. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from yoruba material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-031` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-031` |
| STORY_ID | `yoruba-osun-seventeenth` |
| CULTURE_ID | `yoruba` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The One They Left Out”: They go back and are told they left someone out, and they have to go and ask. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from yoruba material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-032` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-032` |
| STORY_ID | `akan-ananse-stories` |
| CULTURE_ID | `akan` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “How the Stories Got Their Name”: Ananse brings all three, one at a time, and each one is caught by being asked a question. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from akan material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-033` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-033` |
| STORY_ID | `akan-ananse-wisdom` |
| CULTURE_ID | `akan` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Pot That Would Not Go Up the Tree”: He cannot climb; a small voice behind him suggests putting the pot on his back. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from akan material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-034` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-034` |
| STORY_ID | `zulu-chameleon-message` |
| CULTURE_ID | `zulu` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “Two Messengers and One Road”: A second message is sent by lizard, and the lizard runs. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from zulu material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-035` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-035` |
| STORY_ID | `inuit-sedna` |
| CULTURE_ID | `inuit` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Woman at the Bottom of the Sea”: She goes under, and what happens to her hands becomes every animal in the sea. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from inuit material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-036` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-036` |
| STORY_ID | `inuit-blind-boy-loon` |
| CULTURE_ID | `inuit` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Boy Who Got His Eyes Back”: A loon takes him out into the lake and holds him under until the water clears his eyes. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from inuit material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-037` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-037` |
| STORY_ID | `maya-hero-twins` |
| CULTURE_ID | `maya` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Ball Game Under the Ground”: They work out that the only way to beat the lords is to let themselves be beaten first. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from maya material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-038` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-038` |
| STORY_ID | `maya-maize-people` |
| CULTURE_ID | `maya` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “Made of Mud, Wood, and Finally Maize”: The wooden people are wiped out, and the makers try a third time with ground maize. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from maya material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-039` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-039` |
| STORY_ID | `aztec-fifth-sun` |
| CULTURE_ID | `aztec` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Small God Who Jumped First”: The rich god stands at the fire four times and cannot do it, and the small one runs past him. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from aztec material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-040` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-040` |
| STORY_ID | `aztec-quetzalcoatl-maize` |
| CULTURE_ID | `aztec` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Ant Who Would Not Say Where”: The ant refuses, so he turns himself into a black ant and follows her in. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from aztec material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-041` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-041` |
| STORY_ID | `andean-llama-flood` |
| CULTURE_ID | `andean` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Llama That Would Not Eat”: The sea is coming up in five days, and there is one mountain high enough. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from andean material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-042` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-042` |
| STORY_ID | `maori-maui-fish` |
| CULTURE_ID | `maori` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Fish That Became an Island”: Something enormous comes up, and Māui tells them not to touch it until he gets back. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from maori material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-043` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-043` |
| STORY_ID | `maori-rangi-papa` |
| CULTURE_ID | `maori` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Children Who Pushed Their Parents Apart”: Tāne puts his shoulders on his mother and his feet on his father and straightens his legs. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from maori material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-044` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-044` |
| STORY_ID | `hawaiian-maui-sun` |
| CULTURE_ID | `hawaiian` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Day That Was Made Longer”: He waits at the crater rim with ropes and catches the sun's legs one at a time as they come over. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from hawaiian material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `story-045` — Hikâye açılış çizimi — sayfanın üst yarısı

| Alan | Değer |
|---|---|
| ID | `story-045` |
| STORY_ID | `hawaiian-pele-journey` |
| CULTURE_ID | `hawaiian` |
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
| STATUS | `pending` |

**PROMPT**

```
the turning moment of “The Fire That Was Looking for a Home”: She reaches the largest island last and digs where the mountain is highest. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. a standalone horizontal illustration in 3:2 landscape proportions, the whole scene composed inside the frame with a clean margin of white paper on all four sides. visual detail drawn from hawaiian material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-001` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-001` |
| STORY_ID | `—` |
| CULTURE_ID | `akan` |
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
a small emblem for Akan tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from akan material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-002` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-002` |
| STORY_ID | `—` |
| CULTURE_ID | `egyptian` |
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
a small emblem for Ancient Egyptian tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from egyptian material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-003` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-003` |
| STORY_ID | `—` |
| CULTURE_ID | `andean` |
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
a small emblem for Andean tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from andean material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-004` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-004` |
| STORY_ID | `—` |
| CULTURE_ID | `aztec` |
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
a small emblem for Aztec (Mexica) tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from aztec material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-005` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-005` |
| STORY_ID | `—` |
| CULTURE_ID | `chinese` |
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
a small emblem for Chinese tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from chinese material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-006` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-006` |
| STORY_ID | `—` |
| CULTURE_ID | `finnish` |
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
a small emblem for Finnish tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from finnish material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-007` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-007` |
| STORY_ID | `—` |
| CULTURE_ID | `greek` |
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
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Greek tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from greek material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-008` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-008` |
| STORY_ID | `—` |
| CULTURE_ID | `hawaiian` |
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
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Hawaiian tradition: a single outrigger sailing canoe (waʻa kaulua) seen from the side, hull, outrigger float and crab-claw sail, empty of people. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from hawaiian material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-009` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-009` |
| STORY_ID | `—` |
| CULTURE_ID | `hindu` |
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
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Hindu tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from hindu material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-010` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-010` |
| STORY_ID | `—` |
| CULTURE_ID | `inuit` |
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
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Inuit tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from inuit material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-011` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-011` |
| STORY_ID | `—` |
| CULTURE_ID | `irish` |
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
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Irish tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from irish material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-012` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-012` |
| STORY_ID | `—` |
| CULTURE_ID | `japanese` |
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
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Japanese tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from japanese material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-013` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-013` |
| STORY_ID | `—` |
| CULTURE_ID | `korean` |
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
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Korean tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from korean material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-014` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-014` |
| STORY_ID | `—` |
| CULTURE_ID | `maya` |
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
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Maya tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from maya material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-015` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-015` |
| STORY_ID | `—` |
| CULTURE_ID | `mesopotamian` |
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
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Mesopotamian tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from mesopotamian material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-016` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-016` |
| STORY_ID | `—` |
| CULTURE_ID | `maori` |
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
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Māori tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from maori material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-017` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-017` |
| STORY_ID | `—` |
| CULTURE_ID | `norse` |
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
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Norse tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from norse material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-018` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-018` |
| STORY_ID | `—` |
| CULTURE_ID | `persian` |
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
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Persian tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from persian material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-019` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-019` |
| STORY_ID | `—` |
| CULTURE_ID | `turkic` |
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
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Turkic tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from turkic material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-020` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-020` |
| STORY_ID | `—` |
| CULTURE_ID | `vietnamese` |
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
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Vietnamese tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from vietnamese material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-021` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-021` |
| STORY_ID | `—` |
| CULTURE_ID | `yoruba` |
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
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Yoruba tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from yoruba material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
```

## `culture-022` — Kültür vinyeti — kültür kartında

| Alan | Değer |
|---|---|
| ID | `culture-022` |
| STORY_ID | `—` |
| CULTURE_ID | `zulu` |
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
| STATUS | `pending` |

**PROMPT**

```
a small emblem for Zulu tradition — one object or creature that a reader of that tradition would recognise at once. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. small spot illustration, no frame. visual detail drawn from zulu material culture, researched not invented; no pastiche and no borrowed motifs from other traditions. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture
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
| EXPECTED_WIDTH | 3600 px |
| EXPECTED_HEIGHT | 2400 px |
| ASPECT | 3:2 (açık sayfa) |
| DPI | 600 |
| COLOR_MODE | grayscale (1-bit line art on white) |
| PLACEMENT | Ön veya arka iç kapak (açık sayfa) |
| STATUS | `pending` |
| NOTES | Yer adları DİZGİDE eklenir, çizimde değil — böylece 5 dil sürümünde harita yeniden üretilmez. |

**PROMPT**

```
a clean hand-drawn world map with no labels of any kind, in the manner of an old chart but honest about coastlines: continents, major islands and a simple compass rose only. Leave the oceans open and uncluttered — location markers and place names are typeset afterwards and must not be drawn. black and white pen-and-ink line drawing for a children's book on a flat pure white background, clean confident outlines of varied weight, the white of the paper is the only background there is, open uncluttered composition, warm and inviting rather than frightening, shadows suggested by a few short separated strokes, never by filling an area, so the drawing stays crisp when printed small. double-page spread map. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

**NEGATIVE_PROMPT**

```
no blood, no gore, no wounds, no corpses, no severed limbs, no visible entrails, no torture, no nudity, no sexualised figures, no terrified faces in close-up, no photorealism, no colour, no grey wash, no digital gradients, no text, no lettering, no watermark, no signature, no modern objects, no cultural pastiche, no generic fantasy armour, no stereotyped features, no engraving texture, no place labels (typeset separately)
```


---

# FAZ 5 — KAPAK PROMPTLARI

**7 prompt.** Bunlar **68 iç görsele DÂHİL DEĞİLDİR** (talimat § 29): ayrı bir ticari varlık ailesidir.

> **Kapak, markanın bilinçli esnetildiği tek yerdir.** Yol haritası § 18: iç bloğun *koyu kodeks* dili kapakta İŞLEMEZ. Kapak renkli, sıcak ve karakterlidir.

> **Tipografi üretilmez.** Kesin başlık, alt başlık, yaş aralığı ve sırt yazısı CLI ile SONRADAN basılır (§ 44–45). Prompt yalnızca **yer ayırır**.

## `cover-paperback-front`

| Alan | Değer |
|---|---|
| HEDEF | KDP paperback · front cover |
| ORAN | 6.0:9.0 (portrait) |
| ÖLÇÜ (inç) | 6.0 × 9.0 |
| ÜRETİM (px) | 1800 × 2700 |
| TİPOGRAFİ | SONRADAN BASILIR |
| TESTLER | 160px, thumbnail-silhouette, age-badge-corner |

**Amaç.** Ana satış görseli. 160 piksel testini bu geçmek zorunda.

**Metin-güvenli alanlar.**
- top third — title (post-processed)
- under title — subtitle (post-processed)
- lower right corner — 'Ages 8–12' badge (post-processed)

```
front cover only, portrait 6.0×9.0 inches. Composition: one hero scene that says 'stories from the whole world' without naming a single culture — a child-scaled figure looking out over a horizon where several distinct landscapes meet (northern ice, desert river, forest, island sea), with a few unmistakable mythic silhouettes at readable scale in the middle distance: a feathered serpent, a thunder-hammer, a great fish, a firebird. Keep the upper third visually calm — that band carries the title. Keep the lower right corner calm — that corner carries the age range. full-colour children's book cover illustration, ages 8 to 12, warm and inviting, bright saturated palette with a clear focal point, characterful stylised figures with friendly readable faces, storybook poster composition rather than a busy collage, strong silhouette that still reads when the image is one inch wide. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

NEGATIVE_PROMPT

```
no blood, no gore, no wounds, no corpses, no weapons pointed at the viewer, no nudity, no sexualised figures, no terrified faces, no horror imagery, no dark gothic codex styling, no muted desaturated palette, no photorealism, no 3D render, no anime pastiche, no text, no lettering, no title, no logo, no watermark, no signature, no cultural pastiche, no stereotyped features, no sacred or restricted ceremonial imagery, no religious iconography presented as decoration, no busy edge-to-edge detail that collapses at thumbnail size
```

## `cover-paperback-wrap`

| Alan | Değer |
|---|---|
| HEDEF | KDP paperback · full wrap (bleed dahil 12.84×9.25 in) |
| ORAN | 12.84:9.25 (landscape wrap) |
| ÖLÇÜ (inç) | 12.84 × 9.25 |
| ÜRETİM (px) | 3852 × 2775 |
| TİPOGRAFİ | SONRADAN BASILIR |
| TESTLER | spine-safe, barcode-clear-zone, no-detail-in-fold |

**Amaç.** Arka kapak + sırt + ön kapak tek dosyada.

**Metin-güvenli alanlar.**
- spine (0.59" wide) — title + author, post-processed
- back cover left two thirds — blurb, post-processed
- back cover lower right — ISBN/barcode clear zone, 2×1.2 in, must stay empty of detail

```
a single continuous wrap-around cover illustration, landscape 12.84×9.25 inches. The same world-horizon scene continues across the back: on the back cover the landscape opens into calm sky and empty ground so a paragraph of text can sit on it. Keep a vertical band 0.59 inches wide dead centre almost empty — that is the spine and any detail there will be lost in the fold. Keep the bottom right of the back cover flat and light for the barcode. Do not mirror the front composition on the back. full-colour children's book cover illustration, ages 8 to 12, warm and inviting, bright saturated palette with a clear focal point, characterful stylised figures with friendly readable faces, storybook poster composition rather than a busy collage, strong silhouette that still reads when the image is one inch wide. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

NEGATIVE_PROMPT

```
no blood, no gore, no wounds, no corpses, no weapons pointed at the viewer, no nudity, no sexualised figures, no terrified faces, no horror imagery, no dark gothic codex styling, no muted desaturated palette, no photorealism, no 3D render, no anime pastiche, no text, no lettering, no title, no logo, no watermark, no signature, no cultural pastiche, no stereotyped features, no sacred or restricted ceremonial imagery, no religious iconography presented as decoration, no busy edge-to-edge detail that collapses at thumbnail size
```

## `cover-hardcover-wrap`

| Alan | Değer |
|---|---|
| HEDEF | KDP hardcover · case laminate wrap (14.65×10.25 in) |
| ORAN | 14.65:10.25 (landscape wrap) |
| ÖLÇÜ (inç) | 14.65 × 10.25 |
| ÜRETİM (px) | 4116 × 3075 |
| TİPOGRAFİ | SONRADAN BASILIR |
| TESTLER | wrap-safe, hinge-safe, spine-safe |

**Amaç.** Ciltli sarım. Ciltsizden AYRI dosyadır — sarım ve menteşe payları ciltsizde yoktur.

**Metin-güvenli alanlar.**
- spine (0.65" wide) — title + author, post-processed
- back cover — blurb, post-processed
- outer 0.625" on every edge — WRAP, folds around the board and is not seen; no subject may sit there
- 0.375" either side of the spine — HINGE, creases in binding

```
the same wrap-around world-horizon scene, landscape 14.65×10.25 inches, but composed with a wider safety margin: every important element must sit at least 1.0 inches inside the outer edge, because the outer band folds around the board and the band beside the spine creases into the hinge. Extend background colour and sky all the way to the edge so the fold shows no white. full-colour children's book cover illustration, ages 8 to 12, warm and inviting, bright saturated palette with a clear focal point, characterful stylised figures with friendly readable faces, storybook poster composition rather than a busy collage, strong silhouette that still reads when the image is one inch wide. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

NEGATIVE_PROMPT

```
no blood, no gore, no wounds, no corpses, no weapons pointed at the viewer, no nudity, no sexualised figures, no terrified faces, no horror imagery, no dark gothic codex styling, no muted desaturated palette, no photorealism, no 3D render, no anime pastiche, no text, no lettering, no title, no logo, no watermark, no signature, no cultural pastiche, no stereotyped features, no sacred or restricted ceremonial imagery, no religious iconography presented as decoration, no busy edge-to-edge detail that collapses at thumbnail size
```

## `cover-front-variant-figures`

| Alan | Değer |
|---|---|
| HEDEF | KDP paperback · front cover — variant A |
| ORAN | 6.0:9.0 (portrait) |
| ÖLÇÜ (inç) | 6.0 × 9.0 |
| ÜRETİM (px) | 1800 × 2700 |
| TİPOGRAFİ | SONRADAN BASILIR |
| TESTLER | 160px, no-culture-outranks-another, age-badge-corner |

**Amaç.** Karakter ağırlıklı alternatif. Rakip rafta figürlü kapaklar daha iyi çalışıyor; ölçülecek.

**Metin-güvenli alanlar.**
- top third — title
- lower right — age badge

```
front cover only, portrait. Composition: a loose ring of six to eight mythic figures from clearly different traditions, drawn at the same scale and with the same warmth so no tradition outranks another — a trickster spider, a sun-catcher with a rope, a thunder god with a hammer, a feathered serpent, a woman rising from dark water, a boy with wax wings. They face outward around a calm centre. Leave the top third quiet for the title. full-colour children's book cover illustration, ages 8 to 12, warm and inviting, bright saturated palette with a clear focal point, characterful stylised figures with friendly readable faces, storybook poster composition rather than a busy collage, strong silhouette that still reads when the image is one inch wide. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

NEGATIVE_PROMPT

```
no blood, no gore, no wounds, no corpses, no weapons pointed at the viewer, no nudity, no sexualised figures, no terrified faces, no horror imagery, no dark gothic codex styling, no muted desaturated palette, no photorealism, no 3D render, no anime pastiche, no text, no lettering, no title, no logo, no watermark, no signature, no cultural pastiche, no stereotyped features, no sacred or restricted ceremonial imagery, no religious iconography presented as decoration, no busy edge-to-edge detail that collapses at thumbnail size
```

## `cover-front-variant-object`

| Alan | Değer |
|---|---|
| HEDEF | KDP paperback · front cover — variant B |
| ORAN | 6.0:9.0 (portrait) |
| ÖLÇÜ (inç) | 6.0 × 9.0 |
| ÜRETİM (px) | 1800 × 2700 |
| TİPOGRAFİ | SONRADAN BASILIR |
| TESTLER | 160px, single-silhouette, age-badge-corner |

**Amaç.** Tek-nesne alternatifi: küçük resimde en güçlü siluet.

**Metin-güvenli alanlar.**
- upper third — title
- lower right — age badge

```
front cover only, portrait. Composition: one enormous open book lying open, and out of its pages a whole world rises — mountains, an ocean with a great fish, a stepped pyramid, a longship, a torii gate, a baobab — small enough to read as one shape at thumbnail size. A child sits on the lower edge of the book looking up into it. The silhouette of book-plus-rising-world must be legible as a single mark at one inch tall. full-colour children's book cover illustration, ages 8 to 12, warm and inviting, bright saturated palette with a clear focal point, characterful stylised figures with friendly readable faces, storybook poster composition rather than a busy collage, strong silhouette that still reads when the image is one inch wide. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

NEGATIVE_PROMPT

```
no blood, no gore, no wounds, no corpses, no weapons pointed at the viewer, no nudity, no sexualised figures, no terrified faces, no horror imagery, no dark gothic codex styling, no muted desaturated palette, no photorealism, no 3D render, no anime pastiche, no text, no lettering, no title, no logo, no watermark, no signature, no cultural pastiche, no stereotyped features, no sacred or restricted ceremonial imagery, no religious iconography presented as decoration, no busy edge-to-edge detail that collapses at thumbnail size
```

## `cover-back-panel`

| Alan | Değer |
|---|---|
| HEDEF | KDP · back cover panel (wrap içinde) |
| ORAN | 6.0:9.0 (portrait) |
| ÖLÇÜ (inç) | 6.0 × 9.0 |
| ÜRETİM (px) | 1800 × 2700 |
| TİPOGRAFİ | SONRADAN BASILIR |
| TESTLER | blurb-legibility, barcode-clear-zone |

**Amaç.** Sarım kullanılmazsa ayrı arka kapak paneli.

**Metin-güvenli alanlar.**
- upper two thirds — blurb + '45 stories · 22 cultures' line
- lower right 2×1.2 in — barcode clear zone, keep flat

```
back cover panel, portrait. Composition: mostly calm sky and open ground in the cover's palette, with a thin band of small mythic silhouettes along the very bottom like a horizon frieze. The upper two thirds must be quiet enough that a paragraph of text sits on it and stays readable. Bottom right must be flat and pale for the barcode. full-colour children's book cover illustration, ages 8 to 12, warm and inviting, bright saturated palette with a clear focal point, characterful stylised figures with friendly readable faces, storybook poster composition rather than a busy collage, strong silhouette that still reads when the image is one inch wide. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

NEGATIVE_PROMPT

```
no blood, no gore, no wounds, no corpses, no weapons pointed at the viewer, no nudity, no sexualised figures, no terrified faces, no horror imagery, no dark gothic codex styling, no muted desaturated palette, no photorealism, no 3D render, no anime pastiche, no text, no lettering, no title, no logo, no watermark, no signature, no cultural pastiche, no stereotyped features, no sacred or restricted ceremonial imagery, no religious iconography presented as decoration, no busy edge-to-edge detail that collapses at thumbnail size
```

## `cover-thumbnail-test`

| Alan | Değer |
|---|---|
| HEDEF | İç test — 160 piksel okunabilirlik |
| ORAN | 6.0:9.0 (portrait) |
| ÖLÇÜ (inç) | 6.0 × 9.0 |
| ÜRETİM (px) | 160 × 240 |
| TİPOGRAFİ | SONRADAN BASILIR |
| TESTLER | 160px, world-readable, 22-cultures-readable |

**Amaç.** ÜRETİM VARLIĞI DEĞİL, TESTTİR. Yol haritası § 18 kapağın 160 pikselde okunmasını şart koşar: 'World' ve '22 Cultures' küçük resimde okunabilmeli. Bu kayıt, seçilen kapağın küçültülüp sınanacağı adımı görünür tutar.

**Metin-güvenli alanlar.**
- title band
- age badge

```
NOT A GENERATION PROMPT. Take the chosen front cover with post-processed typography applied, downscale it to 160 pixels wide, and check by eye: is the word 'World' readable? is '22 Cultures' readable? is the age badge readable? does the hero shape still read as one thing? If any answer is no, the cover fails and is reworked. full-colour children's book cover illustration, ages 8 to 12, warm and inviting, bright saturated palette with a clear focal point, characterful stylised figures with friendly readable faces, storybook poster composition rather than a busy collage, strong silhouette that still reads when the image is one inch wide. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

NEGATIVE_PROMPT

```
no blood, no gore, no wounds, no corpses, no weapons pointed at the viewer, no nudity, no sexualised figures, no terrified faces, no horror imagery, no dark gothic codex styling, no muted desaturated palette, no photorealism, no 3D render, no anime pastiche, no text, no lettering, no title, no logo, no watermark, no signature, no cultural pastiche, no stereotyped features, no sacred or restricted ceremonial imagery, no religious iconography presented as decoration, no busy edge-to-edge detail that collapses at thumbnail size
```


---

# FAZ 5 — AMAZON A+ İÇERİK PROMPTLARI

**10 prompt.** Bunlar **68 iç görsele DÂHİL DEĞİLDİR** (talimat § 29): ayrı bir ticari varlık ailesidir.


> **Tipografi üretilmez.** Kesin başlık, alt başlık, yaş aralığı ve sırt yazısı CLI ile SONRADAN basılır (§ 44–45). Prompt yalnızca **yer ayırır**.

## `aplus-001-hero`

| Alan | Değer |
|---|---|
| HEDEF | Amazon A+ · Standard Image Header with Text |
| AMAZON MODÜLÜ | Standard Image Header with Text |
| ORAN | 970:600 |
| ÜRETİM (px) | 970 × 600 |
| TİPOGRAFİ | SONRADAN BASILIR |
| TESTLER | text-safe-left, no-generated-text |

**Amaç.** Ürün tanıtımı — modülün ilk ekranı.

**Metin-güvenli alanlar.**
- left 40% — headline and subhead, post-processed

```
a wide banner illustration: the same world-horizon idea as the cover, stretched into a panorama — northern ice on the far left running through desert river, forest and island sea to the far right, with small mythic silhouettes spaced along it. The left 40 percent must stay very calm and light: a headline sits there. Nothing important in the outer 30 pixels. clean marketing illustration for a children's book product page, generous flat background, one clear subject, colour palette drawn from the book cover, calm uncluttered composition with deliberate empty space for text. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

NEGATIVE_PROMPT

```
no text, no lettering, no logos, no watermark, no signature, no user interface elements, no fake screenshots, no star ratings, no price tags, no Amazon branding, no busy collage, no photorealism, no stereotyped features, no cultural pastiche
```

## `aplus-002-cultures`

| Alan | Değer |
|---|---|
| HEDEF | Amazon A+ · Standard Image & Light Text Overlay |
| AMAZON MODÜLÜ | Standard Image & Light Text Overlay |
| ORAN | 970:300 |
| ÜRETİM (px) | 970 × 300 |
| TİPOGRAFİ | SONRADAN BASILIR |
| TESTLER | equal-weight-cultures, text-safe-overlay |

**Amaç.** 22 kültüre genel bakış — 'kapsam' vaadini tek görselde kurar.

**Metin-güvenli alanlar.**
- full width — light text overlay, post-processed

```
a long horizontal frieze of twenty-two small emblems in one consistent flat-colour style, evenly spaced on a plain warm background: sankofa bird, eye of horus, sun disc, feathered serpent, dragon, kantele, greek helmet, outrigger canoe, conch, kayak, triquetra, torii, hourglass drum, maya glyph, lamassu, fish hook, hammer, winged lion, wolf head, long dragon, bell, shield and spear. Equal visual weight for every emblem — none larger or more central than another. Plenty of clear space above and below the row for a text overlay. clean marketing illustration for a children's book product page, generous flat background, one clear subject, colour palette drawn from the book cover, calm uncluttered composition with deliberate empty space for text. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

NEGATIVE_PROMPT

```
no text, no lettering, no logos, no watermark, no signature, no user interface elements, no fake screenshots, no star ratings, no price tags, no Amazon branding, no busy collage, no photorealism, no stereotyped features, no cultural pastiche
```

## `aplus-003-map`

| Alan | Değer |
|---|---|
| HEDEF | Amazon A+ · Standard Single Image & Sidebar |
| AMAZON MODÜLÜ | Standard Single Image & Sidebar |
| ORAN | 300:400 |
| ÜRETİM (px) | 300 × 400 |
| TİPOGRAFİ | SONRADAN BASILIR |
| TESTLER | no-generated-text, no-labels, matches-locked-culture-list |

**Amaç.** Dünya haritası kavramı — ebeveynin 'eğitici' algısı.

**Metin-güvenli alanlar.**
- none in image — caption sits in the module's sidebar

```
a simplified, friendly world map in the cover palette with twenty-two small glowing dots marking homelands, no country borders, no place names. Portrait crop centred on the Atlantic so the Americas, Africa and Europe all read. Warm paper background. clean marketing illustration for a children's book product page, generous flat background, one clear subject, colour palette drawn from the book cover, calm uncluttered composition with deliberate empty space for text. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

NEGATIVE_PROMPT

```
no text, no lettering, no logos, no watermark, no signature, no user interface elements, no fake screenshots, no star ratings, no price tags, no Amazon branding, no busy collage, no photorealism, no stereotyped features, no cultural pastiche
```

## `aplus-004-value`

| Alan | Değer |
|---|---|
| HEDEF | Amazon A+ · Standard Four Image & Text |
| AMAZON MODÜLÜ | Standard Four Image & Text |
| ORAN | 220:220 |
| ÜRETİM (px) | 220 × 220 |
| TİPOGRAFİ | SONRADAN BASILIR |
| TESTLER | 220px-legible, no-generated-numerals |

**Amaç.** '45 hikâye / 22 kültür' eğitsel değeri — dört kareden biri.

**Metin-güvenli alanlar.**
- caption below image, post-processed — the numbers 45 and 22 are TEXT, never generated

```
a small square icon-illustration: a stack of open books with a large friendly numeral shape suggested by the composition (not drawn as a character), on a flat warm background with wide margins. Simple enough to read at 220 pixels. clean marketing illustration for a children's book product page, generous flat background, one clear subject, colour palette drawn from the book cover, calm uncluttered composition with deliberate empty space for text. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

NEGATIVE_PROMPT

```
no text, no lettering, no logos, no watermark, no signature, no user interface elements, no fake screenshots, no star ratings, no price tags, no Amazon branding, no busy collage, no photorealism, no stereotyped features, no cultural pastiche
```

## `aplus-005-linework`

| Alan | Değer |
|---|---|
| HEDEF | Amazon A+ · Standard Four Image & Text |
| AMAZON MODÜLÜ | Standard Four Image & Text |
| ORAN | 220:220 |
| ÜRETİM (px) | 220 × 220 |
| TİPOGRAFİ | SONRADAN BASILIR |
| TESTLER | matches-interior-style, 220px-legible |

**Amaç.** Siyah-beyaz illüstrasyon sistemi — iç bloğun dürüst tanıtımı.

**Metin-güvenli alanlar.**
- caption below image, post-processed

```
a small square showing a single black-and-white pen-and-ink vignette in the book's actual interior style, floating on a flat warm background with wide margins — this one square deliberately uses the interior line language so the buyer sees what is really inside the book. clean marketing illustration for a children's book product page, generous flat background, one clear subject, colour palette drawn from the book cover, calm uncluttered composition with deliberate empty space for text. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

NEGATIVE_PROMPT

```
no text, no lettering, no logos, no watermark, no signature, no user interface elements, no fake screenshots, no star ratings, no price tags, no Amazon branding, no busy collage, no photorealism, no stereotyped features, no cultural pastiche
```

## `aplus-006-reader`

| Alan | Değer |
|---|---|
| HEDEF | Amazon A+ · Standard Four Image & Text |
| AMAZON MODÜLÜ | Standard Four Image & Text |
| ORAN | 220:220 |
| ÜRETİM (px) | 220 × 220 |
| TİPOGRAFİ | SONRADAN BASILIR |
| TESTLER | age-positioning, inclusive-figure |

**Amaç.** Genç okur konumlandırması — 8–12 yaş.

**Metin-güvenli alanlar.**
- caption below image, post-processed

```
a small square: a child of about ten reading, absorbed, sitting with knees up, one small mythic silhouette drifting out of the book above their head. Warm flat background, wide margins. Ambiguous enough in dress and features that any reader can be the child in it. clean marketing illustration for a children's book product page, generous flat background, one clear subject, colour palette drawn from the book cover, calm uncluttered composition with deliberate empty space for text. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

NEGATIVE_PROMPT

```
no text, no lettering, no logos, no watermark, no signature, no user interface elements, no fake screenshots, no star ratings, no price tags, no Amazon branding, no busy collage, no photorealism, no stereotyped features, no cultural pastiche
```

## `aplus-007-backmatter`

| Alan | Değer |
|---|---|
| HEDEF | Amazon A+ · Standard Four Image & Text |
| AMAZON MODÜLÜ | Standard Four Image & Text |
| ORAN | 220:220 |
| ÜRETİM (px) | 220 × 220 |
| TİPOGRAFİ | SONRADAN BASILIR |
| TESTLER | no-generated-text, reads-as-reference-page |

**Amaç.** Telaffuz · sözlük · kültürel not — öğretmen/ebeveyn gerekçesi.

**Metin-güvenli alanlar.**
- caption below image, post-processed

```
a small square: an open book showing two facing pages laid out as a reference spread — a column of short entries on the left and a small emblem on the right — rendered as shape and rhythm only, with NO readable words. Flat warm background, wide margins. clean marketing illustration for a children's book product page, generous flat background, one clear subject, colour palette drawn from the book cover, calm uncluttered composition with deliberate empty space for text. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

NEGATIVE_PROMPT

```
no text, no lettering, no logos, no watermark, no signature, no user interface elements, no fake screenshots, no star ratings, no price tags, no Amazon branding, no busy collage, no photorealism, no stereotyped features, no cultural pastiche
```

## `aplus-008-interior`

| Alan | Değer |
|---|---|
| HEDEF | Amazon A+ · Standard Three Images & Text |
| AMAZON MODÜLÜ | Standard Three Images & Text |
| ORAN | 300:300 |
| ÜRETİM (px) | 300 × 300 |
| TİPOGRAFİ | SONRADAN BASILIR |
| TESTLER | honest-interior-representation, no-generated-text |

**Amaç.** Kitap içi önizleme — 'Look Inside' beklentisini dürüst kurar.

**Metin-güvenli alanlar.**
- caption below image, post-processed

```
a three-quarter view of the physical paperback lying open, showing a story opening: illustration across the upper half of the page and text below it. The page content is suggested, not readable. Soft shadow, plain warm background, generous margin. clean marketing illustration for a children's book product page, generous flat background, one clear subject, colour palette drawn from the book cover, calm uncluttered composition with deliberate empty space for text. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

NEGATIVE_PROMPT

```
no text, no lettering, no logos, no watermark, no signature, no user interface elements, no fake screenshots, no star ratings, no price tags, no Amazon branding, no busy collage, no photorealism, no stereotyped features, no cultural pastiche
```

## `aplus-009-parent`

| Alan | Değer |
|---|---|
| HEDEF | Amazon A+ · Standard Single Left Image |
| AMAZON MODÜLÜ | Standard Single Left Image |
| ORAN | 300:300 |
| ÜRETİM (px) | 300 × 300 |
| TİPOGRAFİ | SONRADAN BASILIR |
| TESTLER | buyer-trust, text-safe-right |

**Amaç.** Ebeveyn/öğretmen değer önerisi — güven tarafı.

**Metin-güvenli alanlar.**
- right side — value proposition text, post-processed

```
a warm domestic scene reduced to essentials: an adult and a child sharing the open book, seen from the side, both looking at the same page. No faces in detail. Flat background in the cover palette, wide clear margin on the right for text. clean marketing illustration for a children's book product page, generous flat background, one clear subject, colour palette drawn from the book cover, calm uncluttered composition with deliberate empty space for text. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

NEGATIVE_PROMPT

```
no text, no lettering, no logos, no watermark, no signature, no user interface elements, no fake screenshots, no star ratings, no price tags, no Amazon branding, no busy collage, no photorealism, no stereotyped features, no cultural pastiche
```

## `aplus-010-series`

| Alan | Değer |
|---|---|
| HEDEF | Amazon A+ · Standard Company Logo |
| AMAZON MODÜLÜ | Standard Company Logo |
| ORAN | 600:180 |
| ÜRETİM (px) | 600 × 180 |
| TİPOGRAFİ | SONRADAN BASILIR |
| TESTLER | no-generated-text, logo-safe |

**Amaç.** Seri kimliği — 'The Great Book of…' rafı.

**Metin-güvenli alanlar.**
- right band — series wordmark, post-processed

```
a horizontal series lockup ILLUSTRATION ONLY: a simple emblem — an open book with a small globe rising from it — centred on a flat background, with a wide empty band to its right. The series name is TEXT and is added afterwards; do not draw any letterforms. clean marketing illustration for a children's book product page, generous flat background, one clear subject, colour palette drawn from the book cover, calm uncluttered composition with deliberate empty space for text. Suitable for readers aged 8 to 12: the image may be dramatic, it may not be frightening.
```

NEGATIVE_PROMPT

```
no text, no lettering, no logos, no watermark, no signature, no user interface elements, no fake screenshots, no star ratings, no price tags, no Amazon branding, no busy collage, no photorealism, no stereotyped features, no cultural pastiche
```

---

*Bu dosya `04_BUILD/make_prompts.py` tarafından üretilir.*
