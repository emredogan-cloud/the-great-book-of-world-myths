## Ne değişti

<!-- Tek cümle. Hangi faz, hangi iş. -->

## Kapı durumu

- [ ] `./04_BUILD/qa_all.sh` yerelde **YEŞİL**
- [ ] `.gate` seviyesi doğru
- [ ] Üretilen belgeler taze (`--fix` gerekmedi)
- [ ] Manuscript sızıntısı yok

## Yazım fazıysa

- [ ] Bu partide **en fazla üç hikâye** var
- [ ] Her hikâyenin `ageReviewStatus` alanı `pending` değil
- [ ] Her hikâyenin kültürel notu **bu hikâyeye özgü** (kalıp değil)
- [ ] Sürüklenme ölçüldü ve commit iletisine geçti: `qa_drift → %__`
- [ ] Her yeni özel adın telaffuzu **ve kaynağı** var

## Karar değiştiyse

- [ ] `DECISIONS.md`'ye `K##` yazıldı
- [ ] `CHANGELOG.md` güncellendi
- [ ] İlgili kapı eşiği güncellendi
- [ ] `05_TESTS/selftest.py` kurgusu güncellendi

> Beş adımın hepsi yapılmazsa belge ile kapı ayrışır. **Ayrışan bir kapı
> ölü kuraldır.**
