# PARENT READINGS — iki ebeveyn okuma kaydı

> **BU DOSYA HENÜZ GEÇERLİ DEĞİLDİR.**
>
> Aşağıda **sıfır** imzalı okuma vardır ve `04_BUILD/validate_structure.py`
> `phase4` kapısında **iki** arar. Kapı şu anda **kırmızıdır ve öyle
> kalmalıdır**.
>
> Bu, bir kusur değil bir **insan bağımlılığıdır**: yol haritası § 21 · **H8**.
>
> Faz 4 · 9 Ağustos 2026

---

## 1. Bu dosya neden var

Master yol haritası R2'yi (yaş uygunluğu) projenin **tanımlayıcı riski**
sayar ve azaltmasını iki parçalı yazar:

> *"Mitler acımasızdır. Yanlış tonlanmış bir sahne, ebeveyn yorumunda
> 'çocuğum için fazla karanlık' olarak geri döner — ve **bu yorum
> silinemez**. Azaltma: **yazım öncesi AGE_POLICY.md**; yayından önce
> **en az iki ebeveyn okuması**."*

Birinci parça bootstrap'ta yapıldı ve `qa_age.py` olarak koda geçti.

**İkinci parça makineyle üretilemez.** İki gerçek insanın 45 hikâyeyi
okuması gerekir. Bu ajan onları uyduramaz, imzalarını yazamaz ve yerlerine
karar veremez.

---

## 2. Faz 4'te bulunan kusur

Bu dosyanın kapısı **üç faz boyunca ÖLÜYDÜ**.

| Ne diyordu | Nerede | Gerçek |
|---|---|---|
| *"`phase4` + PARENT_READINGS.md iki imzalı kayıt"* | yol haritası § 16 | kod bunu aramıyordu |
| *"`validate_structure.py` **Faz 5** kapısında arar"* | `DECISIONS.md` § A8 | kod bunu da aramıyordu |

Yani R2'nin insan yarısı **hiçbir mekanizmaya bağlı değildi**. İki belge
birbiriyle de çelişiyordu. Yol haritası kazandı (§ 1): kapı **phase4**'tedir.

Kapı Faz 4'te yazıldı, `selftest` ile sınandı ve **kasıtlı olarak kırmızı
bırakıldı**.

---

## 3. Okuyucudan istenen

Her okuyucu **45 hikâyenin tamamını** okur. Örnekleme yeterli değildir:
tonu kıran şey tek bir sahnedir ve hangisi olduğu önceden bilinemez.

Okuma sırasında not alınacak dört şey:

| # | Soru |
|---|---|
| 1 | Hangi sahne **fazla karanlık** geldi? Hikâye adı ve paragraf. |
| 2 | Hangi sahne **fazla yumuşatılmış** geldi? (Aşırı saklama da kusurdur — `AGE_POLICY.md` § 0.) |
| 3 | Çocuğunuz **hangi yaşta** bunu okuyabilir? Alt başlık 8–12 diyor. |
| 4 | Bir kültür hakkında **rahatsız edici** ya da yanlış gelen bir şey var mı? |

Olumsuz geri bildirim **saklanmaz**. Bulunan her şey bu dosyaya yazılır ve
sonucunda ne yapıldığı da yazılır — düzeltildiyse nasıl, düzeltilmediyse
neden.

---

## 4. Kayıt biçimi

Her okuma bir bölüm alır ve **imza satırı zorunludur**. Kapı yalnızca bu
çıpayı sayar:

```
<!-- PARENT-READING:SIGNED okuyucunun adı -->
```

Şablon:

```markdown
### Okuma 1 — <ad>

- **Tarih:**
- **Okunan:** 45/45 hikâye
- **İlişki:** (kaç yaşında bir çocuğun ebeveyni)
- **Fazla karanlık bulunan sahneler:**
- **Fazla yumuşak bulunan sahneler:**
- **Önerilen yaş aralığı:**
- **Kültürel kaygılar:**
- **Sonuç:** `onaylandı` / `düzeltmeyle onaylandı` / `onaylanmadı`
- **Yapılan düzeltmeler:**

<!-- PARENT-READING:SIGNED <ad> -->
```

---

## 5. Kayıtlar

*(Henüz yok. Kurucu iki okuyucu bulduğunda buraya eklenir.)*

---

## 6. Durum

```
İSTENEN OKUMA   : 2
KAYITLI OKUMA   : 0
KAPI            : phase4 · KIRMIZI
BLOKLADIĞI      : v0.4.0 sürümü ve Faz 5'e geçiş
SORUMLU         : kurucu (yol haritası § 21 · H8)
```

**Bu sayı uydurulamaz.** Sıfır yazıyorsa sıfırdır.
