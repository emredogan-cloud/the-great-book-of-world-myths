# 07_ASSETS/raw — ham görseller

Kurucunun GPT Image ile ürettiği **PNG** dosyaları buraya konur.

**Bu dosyaların üzerine asla yazılmaz.** Üretim formatları
`04_BUILD/convert_images.py` ile `07_ASSETS/processed/` altına türetilir:

```
raw/story-001.png  ──convert_images.py──┬──> processed/print/story-001.tif   (600 dpi, gri)
                                        ├──> processed/kindle/story-001.png  (bütçeye optimize)
                                        └──> processed/web/story-001.webp    (A+ ve pazarlama)
```

Dosya adları `07_ASSETS/IMAGE_PROMPT_LIBRARY.md` tarafından belirlenir ve
`04_BUILD/make_prompts.py --check` tarafından denetlenir. Elle ad vermeyin.

Ham dosyalar depoda durmaz (`.gitignore` § ③) — yerelde saklanır ve
yedeklenir. Depoda yalnızca **ölçümleri** durur.
