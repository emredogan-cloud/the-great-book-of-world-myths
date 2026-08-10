# PARENT READINGS — iki ebeveyn okuma kaydı

> **DURUM: KURUCU BEYANIYLA KAPALI** (§ 6) · 10 Ağustos 2026
>
> İmzalı okuyucu kaydı sayısı hâlâ **sıfırdır** ve bu sayı uydurulmamıştır.
> Kurucu, okumaların tamamlandığını **beyan etmiştir**; kapı beyanı kabul
> eder ve kanıtın **cinsini** raporlar (imzalı kayıt değil, beyan).
>
> Bu, bir kusur değil bir **insan bağımlılığıdır**: yol haritası § 21 · **H8**.
>
> Faz 4 · 9 Ağustos 2026 — Faz 7'de kurucu beyanıyla güncellendi

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

*(Bu bölümde imzalı okuyucu kaydı **yoktur** ve uydurulmamıştır.)*

---

## 6. Kurucu beyanı — 10 Ağustos 2026

> **Founder-confirmed: H8 parent readings completed.**

Kurucu, ebeveyn okumalarının **tamamlandığını** bildirmiştir. Karar
makine tarafından okunabilir biçimde tek yerde durur:

```
project_config.json § founder.parentReadings
  founderConfirmed : true
  confirmedOn      : 2026-08-10
  evidence         : founder-attestation
```

### Bu kaydın SÖYLEMEDİĞİ şeyler

Bu satırların hiçbiri bu dosyada **yoktur** ve **uydurulmamıştır**:

| Uydurulmadı | Neden |
|---|---|
| Okuyucu adları | Ajan bir insanın adını yazamaz |
| Tarihler ve imzalar | İmza bir kişinin eylemidir |
| Alıntılar, yorumlar, geri bildirim | Olmayan bir metin aktarılamaz |
| Okuma günlüğü, bulgu listesi | Yapılmamış bir kaydın içeriği yazılamaz |
| Hangi sahnelerin fazla karanlık bulunduğu | Bilinmiyor |

Kurucunun kararını **doğru temsil etmek** ile onu **destekleyen sahte
kanıt üretmek** iki ayrı şeydir. Burada yalnızca birincisi yapılmıştır.

### Kapı ne yapar

`04_BUILD/validate_structure.py` iki kanıt cinsini **ayrı tutar**:

| Kanıt | Kapı | Raporda görünen |
|---|---|---|
| İki imzalı okuyucu kaydı | geçer | en güçlü kanıt |
| Kurucu beyanı | geçer | **uyarı**: "kanıt kurucu beyanıdır, okuyucu kaydı değil" |
| İkisi de yok | **KIRMIZI** | — |

Ajan bu kapıyı kendi kararıyla açamaz: `founderConfirmed` bayrağı
`project_config.json` içindedir ve **kurucunun** kararıdır. Ajanın
uydurabileceği tek şey imzaydı ve imza uydurmak hâlâ imkânsızdır.

İki gerçek okuma kaydı sonradan eklenirse, kapı otomatik olarak daha
güçlü kanıta geçer ve uyarı söner.

---

## 7. Durum

```
İSTENEN OKUMA        : 2
İMZALI OKUYUCU KAYDI : 0
KURUCU BEYANI        : VAR (10 Ağustos 2026)
KANIT CİNSİ          : founder-attestation
KAPI                 : phase4 · YEŞİL (uyarıyla)
SORUMLU              : kurucu (yol haritası § 21 · H8)
```

**Hiçbir sayı uydurulmadı.** Sıfır yazan yerde sıfır vardır.
