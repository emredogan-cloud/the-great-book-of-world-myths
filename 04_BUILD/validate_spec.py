#!/usr/bin/env python3
"""
VERİ BÜTÜNLÜĞÜ KAPISI — culture_index.json + story_index.json
================================================================================
Kapı seviyeleri KÜMÜLATİFTİR (karar K8): phase1'in şartları phase2'de de
aranır. Seviye `.gate`ten okunur, tahmin edilmez.

    python3 04_BUILD/validate_spec.py --gate phase1 --verbose --json <path>

ÖLÜ KURAL AVI (karar K14): her kimlik referansı gerçek bir kayda denk
gelmek zorundadır. Bestiarium'da denk gelmeyen iki kimlik yüzünden en
hassas etik notu taşıyan madde zorunlu kapının DIŞINDA kaldı ve hiçbir
yerde hata görünmedi — "kapının sessizliği, kalitenin kanıtı değildi."
"""

from __future__ import annotations

import argparse
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mythbook as mb


# =============================================================================
# ŞEMA — hafif, bağımlılıksız doğrulayıcı
# =============================================================================
# jsonschema kurmuyoruz (karar K7). Şema dosyaları belge olarak durur;
# burada onların ZORUNLU KILDIĞI şeyler elle ama eksiksiz denetlenir.

SOURCE_TYPES = {"primary", "scholarly", "reference", "index", "retelling"}
INDEPENDENT_TYPES = {"primary", "scholarly", "reference"}
STRONG_TYPES = {"primary", "scholarly"}
VERIFICATIONS = {"fulltext", "toc", "article", "sv", "canon", "catalog", "secondary"}
STRONG_VERIFICATIONS = {"fulltext", "toc", "article", "sv", "canon"}

STORY_STATUSES = {
    "candidate", "researching", "verified", "locked",
    "written", "edited", "age-reviewed", "final", "dropped",
}
WRITTEN_STATUSES = {"written", "edited", "age-reviewed", "final"}

CONTENT_FLAGS = {
    "violence", "death", "grief", "monsters", "transformation", "cannibalism",
    "sacrifice", "sexuality", "abuse", "kidnapping", "war", "revenge",
    "punishment", "supernatural-horror", "religious", "culturally-sensitive",
    "frightening-imagery",
}

# AGE_POLICY § 3 — hangi kategori hangi seviyede.
# IMPLY/OMIT/REVIEW kategorileri ageAdaptationNote'u ZORUNLU kılar
# (SOURCING_STANDARD § 6).
POLICY_LEVEL = {
    "violence": "IMPLY",
    "death": "ALLOW",
    "grief": "ALLOW",
    "monsters": "ALLOW",
    "transformation": "ALLOW",
    "cannibalism": "IMPLY",
    "sacrifice": "REVIEW",
    "sexuality": "OMIT",
    "abuse": "OMIT",
    "kidnapping": "ALLOW",
    "war": "ALLOW",
    "revenge": "ALLOW",
    "punishment": "ALLOW",
    "supernatural-horror": "IMPLY",
    "religious": "REVIEW",
    "culturally-sensitive": "REVIEW",
    "frightening-imagery": "IMPLY",
}
NOTE_REQUIRING = {k for k, v in POLICY_LEVEL.items() if v in ("IMPLY", "OMIT", "REVIEW")}

AGE_REVIEW_STATUSES = {"pending", "cleared", "needs-review", "founder-approved", "parent-approved"}


# =============================================================================
# 1. KÜLTÜR DİZİNİ
# =============================================================================

def check_cultures(cultures: dict, gate: str, r: mb.Result) -> None:
    mb.banner("kültür dizini")

    entries = cultures.get("cultures", [])
    macro_ids = {m["id"] for m in cultures.get("macroRegions", [])}

    r.add(bool(macro_ids), f"makro bölge tanımlı ({len(macro_ids)})",
          "macroRegions boş — harita etiketleri üretilemez")

    # --- kimlik benzersizliği ---
    ids = [c.get("id") for c in entries]
    dupes = [i for i, n in collections.Counter(ids).items() if n > 1]
    r.add(not dupes, f"kültür kimlikleri benzersiz ({len(ids)} kayıt)",
          f"yinelenen kimlik: {dupes}")

    # --- slug biçimi ---
    bad_slug = [i for i in ids if not i or not re.fullmatch(r"[a-z0-9-]+", i)]
    r.add(not bad_slug, "kültür kimlikleri slug biçiminde", f"geçersiz: {bad_slug}")

    # --- ÖLÜ KURAL AVI: makro bölge referansları ---
    orphan_macro = sorted({c["macroRegion"] for c in entries
                           if c.get("macroRegion") not in macro_ids})
    r.add(not orphan_macro,
          "her kültürün makro bölgesi tanımlı bir bölgeye denk geliyor",
          f"denk gelmeyen: {orphan_macro} — ÖLÜ REFERANS (karar K14)")

    # --- zorunlu alanlar ---
    missing = []
    for c in entries:
        for field in ("name", "nameTr", "status", "livingTradition",
                      "restrictionAssessment", "rationale"):
            if c.get(field) in (None, ""):
                missing.append(f"{c.get('id')}·{field}")
    r.add(not missing, "kültür kayıtlarında zorunlu alan eksiği yok",
          f"eksik: {missing[:8]}")

    # --- yol haritasının kilitlediği kültürler ---
    required = set(mb._CFG["scope"]["culturesLockedByRoadmap"])
    present = {c["id"] for c in entries}
    missing_locked = sorted(required - present)
    r.add(not missing_locked,
          f"yol haritasının adıyla saydığı {len(required)} kültür dizinde",
          f"EKSİK: {missing_locked} — bunlar kitabın konumlanma iddiasının kanıtıdır")

    locked_ids = {c["id"] for c in entries if c.get("status") == "locked"}
    not_locked = sorted(c["id"] for c in entries
                        if c["id"] in required and c.get("status") != "locked")
    r.add(not not_locked,
          "yol haritasının kültürleri 'locked' durumda",
          f"'locked' değil: {not_locked}")

    # --- ÖLÜ KURAL AVI: yol haritasının ALTI GELENEĞİ hâlâ karşılanıyor mu ---
    # Karar K23 iki geleneği daraltmıştır (Polinezya → Māori + Hawai'i,
    # Batı Afrika → Yoruba + Akan). Daraltma bir kaçış yolu OLAMAZ: her
    # geleneğin en az bir KİLİTLİ kültürle karşılandığı ayrıca denetlenir.
    # Bu denetim olmadan, bir kültürü listeden düşürmek yol haritasının
    # adıyla saydığı bir geleneği SESSİZCE yok edebilirdi.
    traditions = mb._CFG["scope"].get("roadmapTraditions") or {}
    uncovered, dangling = [], []
    for tradition, satisfiers in traditions.items():
        if not any(s in locked_ids for s in satisfiers):
            uncovered.append(tradition)
        dangling += [s for s in satisfiers if s not in present]
    r.add(not uncovered,
          f"yol haritasının {len(traditions)} geleneğinin hepsi kilitli bir kültürle karşılanıyor",
          f"KARŞILANMAYAN gelenek: {uncovered} — yol haritası bunları ADIYLA sayar")
    r.add(not dangling,
          "gelenek eşlemesindeki her kimlik dizinde var",
          f"denk gelmeyen: {sorted(set(dangling))} — ÖLÜ REFERANS (karar K14)")

    # --- sayım ---
    locked = [c for c in entries if c.get("status") == "locked"]
    candidates = [c for c in entries if c.get("status") == "candidate"]

    # --- aday havuzu — HER KAPIDA denetlenir ---
    # ⚠ ÖLÜ KURAL DÜZELTMESİ (Faz 1). Bu denetim eskiden yalnızca `else`
    # dalındaydı, yani kapı phase1'e YÜKSELDİĞİ AN kayboluyordu — tam da
    # yedek payının anlam kazandığı noktada. DoD § 17 ölçüt 7 ise onu
    # `validate_spec`'in denetlediğini söylüyordu. Belge kapıyı anlatıyor,
    # kapı hiçbir şey demiyordu: Bestiarium D28'in aynı sınıfı.
    r.warn(len(entries) >= mb.CULTURE_CANDIDATE_MIN,
           f"kültür aday havuzu yeterli ({len(entries)} ≥ {mb.CULTURE_CANDIDATE_MIN})",
           f"aday havuzu {len(entries)} < {mb.CULTURE_CANDIDATE_MIN} — bir kültür "
           "kısıtlılık taramasında düşerse 22 sayısı tutmaz (SOURCING_STANDARD § 9)")

    if mb.gate_at_least(gate, "phase1"):
        r.add(len(locked) == mb.CULTURE_TARGET,
              f"{mb.CULTURE_TARGET} kültür kilitli ({len(locked)})",
              f"{len(locked)}/{mb.CULTURE_TARGET} kilitli — alt başlık '22 cultures' diyor "
              "ve alıcı (ebeveyn) tam olarak o sayıyı tarıyor")

        pending = [c["id"] for c in locked if c.get("restrictionAssessment") == "pending"]
        r.add(not pending,
              "kilitli her kültürün kısıtlılık değerlendirmesi tamamlandı",
              f"'pending' kalan: {pending} — SOURCING_STANDARD § 7 MUAFİYETSİZ (K20)")

        # Taraması 'restricted' çıkan bir kültür KİLİTLENEMEZ. Tarama bir
        # onay kutusu değilse, olumsuz sonucunun bir sonucu olmak zorundadır.
        restricted = [c["id"] for c in locked
                      if c.get("restrictionAssessment") == "restricted"]
        r.add(not restricted,
              "kilitli hiçbir kültür 'restricted' taramasıyla geçmiyor",
              f"KISITLI ama kilitli: {restricted} — tarama olumsuzsa kültür "
              "kilitlenemez (SOURCING_STANDARD § 7); yerine aday gelir")

        # Kilitli her kültürün kısıtlılık taraması bir CÜMLEYLE kayıtlı olmalı.
        thin = [c["id"] for c in locked
                if len((c.get("restrictionNote") or "").strip()) < 20]
        r.add(not thin,
              "kilitli her kültürün kısıtlılık notu açık bir cümle",
              f"eksik/kısa not: {thin} — 'tarandı' demek tarama değildir")
    else:
        r.ok(f"kültür sayımı: {len(locked)} kilitli · {len(candidates)} aday",
             f"kapı {gate} — 22 kilit şartı phase1'de açılır")

    # --- kasıtlı dışarıda bırakılanlar gerekçeli mi ---
    for ex in cultures.get("excluded", []):
        r.add(len(ex.get("reason", "")) >= 30 and bool(ex.get("disposition")),
              f"dışarıda bırakma gerekçeli: {ex.get('id')}",
              f"{ex.get('id')} — gerekçe veya 'disposition' eksik; "
              "kasıtlı dışarıda bırakma bir KARARDIR ve okura söylenir")

    # --- vinyet kimlikleri benzersiz ---
    vids = [c.get("vignetteId") for c in entries if c.get("vignetteId")]
    vdupes = [i for i, n in collections.Counter(vids).items() if n > 1]
    r.add(not vdupes, "kültür vinyet kimlikleri benzersiz", f"yinelenen: {vdupes}")


# =============================================================================
# 2. HİKÂYE DİZİNİ
# =============================================================================

def check_stories(stories: dict, cultures: dict, gate: str, r: mb.Result) -> None:
    mb.banner("hikâye dizini")

    entries = stories.get("stories", [])
    culture_ids = {c["id"] for c in cultures.get("cultures", [])}
    part_ids = {p["id"] for p in stories.get("parts", [])}

    active = [s for s in entries if s.get("status") != "dropped"]
    locked = [s for s in active if s.get("status") in
              ({"locked", "verified"} | WRITTEN_STATUSES)]

    # --- kimlik benzersizliği ---
    ids = [s.get("id") for s in entries]
    dupes = [i for i, n in collections.Counter(ids).items() if n > 1]
    r.add(not dupes, f"hikâye kimlikleri benzersiz ({len(ids)} kayıt)",
          f"yinelenen kimlik: {dupes}")

    # --- sıra numarası benzersizliği ---
    numbers = [s.get("number") for s in active if s.get("number") is not None]
    ndupes = [i for i, n in collections.Counter(numbers).items() if n > 1]
    r.add(not ndupes, "hikâye sıra numaraları benzersiz", f"yinelenen sıra: {ndupes}")

    # --- ÖLÜ KURAL AVI: kültür referansları ---
    orphan_culture = sorted({s.get("cultureId") for s in entries
                             if s.get("cultureId") not in culture_ids})
    r.add(not orphan_culture,
          "her hikâyenin kültürü dizinde tanımlı",
          f"denk gelmeyen kültür: {orphan_culture} — ÖLÜ REFERANS (karar K14)")

    # --- ÖLÜ KURAL AVI: bölüm referansları ---
    orphan_part = sorted({s.get("partId") for s in entries
                          if s.get("partId") and s["partId"] not in part_ids})
    r.add(not orphan_part, "hikâye bölüm referansları tanımlı",
          f"denk gelmeyen bölüm: {orphan_part}")

    # --- durum değerleri ---
    bad_status = sorted({s.get("status") for s in entries
                         if s.get("status") not in STORY_STATUSES})
    r.add(not bad_status, "hikâye durumları geçerli", f"geçersiz durum: {bad_status}")

    # --- düşürülen hikâyeler gerekçeli mi ---
    undocumented = [s["id"] for s in entries
                    if s.get("status") == "dropped" and not s.get("dropReason")]
    r.add(not undocumented, "düşürülen hikâyeler gerekçeli",
          f"gerekçesiz düşürme: {undocumented}")

    # --- içerik işaretleri ---
    bad_flags = set()
    for s in entries:
        bad_flags |= {f for f in (s.get("contentFlags") or []) if f not in CONTENT_FLAGS}
    r.add(not bad_flags, "içerik işaretleri AGE_POLICY kategorilerine denk geliyor",
          f"tanınmayan işaret: {sorted(bad_flags)} — ÖLÜ REFERANS")

    bad_review = sorted({s.get("ageReviewStatus") for s in entries
                         if s.get("ageReviewStatus") not in AGE_REVIEW_STATUSES
                         and s.get("status") != "dropped"})
    r.add(not bad_review, "yaş inceleme durumları geçerli", f"geçersiz: {bad_review}")

    # --- kaynak yapısı ---
    bad_src_type, bad_src_ver = set(), set()
    for s in entries:
        for src in (s.get("sources") or []):
            if src.get("type") not in SOURCE_TYPES:
                bad_src_type.add(f"{s['id']}:{src.get('type')}")
            if src.get("verification") not in VERIFICATIONS:
                bad_src_ver.add(f"{s['id']}:{src.get('verification')}")
    r.add(not bad_src_type, "kaynak katmanları geçerli", f"geçersiz: {sorted(bad_src_type)[:8]}")
    r.add(not bad_src_ver, "kaynak doğrulama seviyeleri geçerli", f"geçersiz: {sorted(bad_src_ver)[:8]}")

    # --- görsel kimlikleri ---
    image_ids = [s.get("imageId") for s in active if s.get("imageId")]
    idupes = [i for i, n in collections.Counter(image_ids).items() if n > 1]
    r.add(not idupes, "hikâye görsel kimlikleri benzersiz", f"yinelenen: {idupes}")
    bad_img = [i for i in image_ids if not re.fullmatch(r"story-\d{3}", i)]
    r.add(not bad_img, "görsel kimlikleri story-NNN biçiminde", f"geçersiz: {bad_img}")

    # --- KAPI: phase0 ---
    if not mb.gate_at_least(gate, "phase1"):
        r.ok(f"hikâye sayımı: {len(locked)} kilitli · {len(active)} aday",
             f"kapı {gate} — 45 kilit şartı phase1'de açılır")
        return

    # --- KAPI: phase1 ve üstü ---
    r.add(len(locked) == mb.STORY_TARGET,
          f"{mb.STORY_TARGET} hikâye kilitli ({len(locked)})",
          f"{len(locked)}/{mb.STORY_TARGET} kilitli — alt başlık '45 Stories' diyor "
          "ve düşen bir hikâyenin yerine BAŞKASI gelmek zorundadır (SOURCING_STANDARD § 9)")

    r.warn(len(entries) >= mb.STORY_CANDIDATE_MIN,
           f"aday havuzu yeterli ({len(entries)} ≥ {mb.STORY_CANDIDATE_MIN})",
           f"aday havuzu {len(entries)} < {mb.STORY_CANDIDATE_MIN} — yedeksiz kapsam")

    # --- her kilitli kültürün en az bir hikâyesi var mı ---
    locked_cultures = {c["id"] for c in cultures.get("cultures", [])
                       if c.get("status") == "locked"}
    per_culture = collections.Counter(s["cultureId"] for s in locked)
    empty = sorted(locked_cultures - set(per_culture))
    r.add(not empty, "her kilitli kültürün en az bir hikâyesi var",
          f"hikâyesiz kültür: {empty} — '22 cultures' iddiası boş bir kültürle çöker")

    # --- aşırı temsil ---
    # K24 (kurucu, Faz 1): bu iki kısıt artık UYARI DEĞİL HATADIR.
    # Gerekçe: kural kitabın editoryal tezinin ta kendisidir. Raf %80 Yunan
    # olduğu için bu kitap var; tezi uyarı seviyesinde tutmak onu unutulabilir
    # kılar. `distributionCapsAreErrors` yanlışa çekilirse kural uyarıya döner
    # ve o değişiklik project_config'de GÖRÜNÜR olur.
    hard = mb._CFG["scope"].get("distributionCapsAreErrors", False)
    check = r.add if hard else r.warn
    level = "kapı" if hard else "uyarı"

    cap = mb._CFG["scope"]["maxStoriesPerCulture"]
    over = {c: n for c, n in per_culture.items() if n > cap}
    check(not over, f"hiçbir kültür {cap} hikâyeyi aşmıyor ({level})",
          f"aşan: {over} — kitap gizlice '5 kültür + ekler' kitabına dönebilir "
          "(DECISIONS § A3 → K24)")

    greek_cap = mb._CFG["scope"]["maxStoriesGreek"]
    greek = per_culture.get("greek", 0)
    check(greek <= greek_cap, f"Yunan payı sınırda ({greek} ≤ {greek_cap}) ({level})",
          f"Yunan payı {greek} > {greek_cap} — kitabın varlık sebebi rafın %80 Yunan olması")

    # --- kelime hedefi toplamı ---
    total = sum(s.get("wordTarget", mb.WORD_TARGET) for s in locked)
    target = mb.MANUSCRIPT_WORD_TARGET
    drift = abs(total - target) / target * 100 if target else 0
    r.warn(drift <= 10,
           f"kelime bütçesi hedefte ({total:,} · hedef {target:,} · sapma %{drift:.1f})",
           f"kelime bütçesi {total:,}, hedef {target:,} — sapma %{drift:.1f} > %10")


# =============================================================================
# 3. ARAŞTIRMA KAPISI — phase1'den itibaren
# =============================================================================

def check_research_gates(stories: dict, cultures: dict, gate: str, r: mb.Result) -> None:
    if not mb.gate_at_least(gate, "phase1"):
        return

    mb.banner("araştırma kapıları (SOURCING_STANDARD)")

    entries = [s for s in stories.get("stories", [])
               if s.get("status") in ({"locked", "verified"} | WRITTEN_STATUSES)]

    two_independent, one_strong, one_strong_ver = [], [], []
    retelling_cited, unverified_locus = [], []
    canonical_missing, rationale_missing = [], []
    restriction_missing, age_note_missing = [], []
    pronunciation_missing, pron_source_missing = [], []
    claim_orphan = []

    for s in entries:
        sid = s["id"]
        srcs = s.get("sources") or []

        independent = [x for x in srcs if x.get("type") in INDEPENDENT_TYPES]
        if len(independent) < 2:
            two_independent.append(sid)
        if not any(x.get("type") in STRONG_TYPES for x in independent):
            one_strong.append(sid)
        if not any(x.get("verification") in STRONG_VERIFICATIONS for x in independent):
            one_strong_ver.append(sid)

        # yeniden anlatım ASLA kaynak sayılmaz — sayılmışsa listede olmamalı
        if any(x.get("type") == "retelling" for x in srcs):
            retelling_cited.append(sid)

        # sayfa numarası kuralı: 'catalog'/'secondary' doğrulamada sayfa yazılamaz
        for x in srcs:
            locus = (x.get("locus") or "").strip()
            if locus and x.get("verification") in ("catalog", "secondary"):
                if re.search(r"\b(?:p{1,2}\.?\s*)?\d+(?:\s*[–-]\s*\d+)?$", locus):
                    unverified_locus.append(f"{sid}:{locus}")

        if not (s.get("canonicalVersion") or "").strip():
            canonical_missing.append(sid)
        if len((s.get("canonicalRationale") or "").strip()) < 10:
            rationale_missing.append(sid)

        if s.get("restrictionScreened") is not True or \
           len((s.get("restrictionNote") or "").strip()) < 20:
            restriction_missing.append(sid)

        flags = set(s.get("contentFlags") or [])
        if flags & NOTE_REQUIRING and not (s.get("ageAdaptationNote") or "").strip():
            age_note_missing.append(sid)

        pron = s.get("pronunciationEntries") or []
        if not pron:
            pronunciation_missing.append(sid)
        for p in pron:
            if len((p.get("pronunciationSource") or "").strip()) < 5:
                pron_source_missing.append(f"{sid}:{p.get('name')}")

        refs = {x.get("ref") for x in srcs}
        for claim in (s.get("factualClaims") or []):
            if claim.get("sourceRef") not in refs:
                claim_orphan.append(f"{sid}:{claim.get('sourceRef')}")

    r.add(not two_independent, "her hikâyede ≥2 bağımsız kaynak",
          f"eksik: {two_independent[:8]}")
    r.add(not one_strong, "her hikâyede ≥1 primary/scholarly kaynak",
          f"eksik: {one_strong[:8]} — iki ansiklopedi iki bağımsız kaynak DEĞİLDİR")
    r.add(not one_strong_ver, "her hikâyede ≥1 güçlü doğrulama",
          f"eksik: {one_strong_ver[:8]} — fulltext/toc/canon/article/sv")
    r.add(not retelling_cited, "hiçbir hikâye yeniden anlatımı kaynak saymıyor",
          f"künyelemiş: {retelling_cited[:8]} — SOURCING_STANDARD § 2")
    r.add(not unverified_locus, "doğrulanmamış sayfa numarası yok",
          f"şüpheli: {unverified_locus[:8]} — 'catalog'/'secondary' doğrulamada sayfa yazılamaz")
    r.add(not canonical_missing, "her hikâyenin kanonik anlatımı seçilmiş",
          f"eksik: {canonical_missing[:8]}")
    r.add(not rationale_missing, "her kanonik seçim gerekçeli",
          f"eksik: {rationale_missing[:8]} — 'daha yumuşak' TEK BAŞINA geçersiz")
    r.add(not restriction_missing, "kısıtlılık taraması muafiyetsiz tamam",
          f"eksik: {restriction_missing[:8]} — karar K20")
    r.add(not age_note_missing, "IMPLY/OMIT/REVIEW kategorili hikâyelerde uyarlama notu var",
          f"eksik: {age_note_missing[:8]} — SOURCING_STANDARD § 6")
    r.add(not pronunciation_missing, "her hikâyenin telaffuz kaydı var",
          f"eksik: {pronunciation_missing[:8]}")
    r.add(not pron_source_missing, "her telaffuzun kaynağı var",
          f"kaynaksız: {pron_source_missing[:8]} — telaffuz UYDURULMAZ")
    r.add(not claim_orphan, "her olgusal iddia bir kaynağa bağlı",
          f"bağsız: {claim_orphan[:8]}")


# =============================================================================
# 4. YAZIM KAPISI — phase2'den itibaren
# =============================================================================

def check_writing_gate(stories: dict, gate: str, r: mb.Result) -> None:
    if not mb.gate_at_least(gate, "phase2"):
        return

    mb.banner("yazım kapısı")

    entries = [s for s in stories.get("stories", []) if s.get("status") != "dropped"]
    written = [s for s in entries if s.get("status") in WRITTEN_STATUSES]

    phases = {p["id"]: p for p in mb._CFG["phases"]}
    expected = phases.get(gate, {}).get("storiesCumulative")

    if expected is not None:
        r.add(len(written) >= expected,
              f"{gate} için yazım hedefi tuttu ({len(written)} ≥ {expected})",
              f"{len(written)} yazıldı, {gate} {expected} bekliyor")

    # kültürel not yazılmış hikâyelerde zorunlu
    missing_note = [s["id"] for s in written if not (s.get("culturalNote") or "").strip()]
    r.add(not missing_note, "yazılmış her hikâyenin kültürel notu var",
          f"eksik: {missing_note[:8]} — yol haritası: 'her hikâye sonunda 2 satırlık kültürel not'")

    # yaş incelemesi 'pending' kalamaz
    pending = [s["id"] for s in written if s.get("ageReviewStatus") == "pending"]
    r.add(not pending, "yazılmış hikâyelerde yaş incelemesi başlamış",
          f"'pending' kalan: {pending[:8]} — AGE_POLICY § 4")

    # dört hareket
    no_plot = [s["id"] for s in written
               if not (s.get("plot") or {}).get("turn")]
    r.warn(not no_plot, "yazılmış hikâyelerde dönüm anı kayıtlı",
           f"eksik: {no_plot[:8]} — CHILDREN_WRITING_STYLE § 3")


# =============================================================================
# 5. YAPILANDIRMA TUTARLILIĞI
# =============================================================================

def check_config(gate: str, r: mb.Result) -> None:
    mb.banner("yapılandırma tutarlılığı")

    cfg = mb._CFG

    declared = cfg["gates"]["current"]
    r.add(declared == gate,
          f"project_config.gates.current ↔ .gate ({gate})",
          f"project_config '{declared}' diyor, .gate '{gate}' diyor — "
          "iki doğruluk kaynağı, ikisi de yanlış olabilir")

    r.add(cfg["gates"]["levels"] == mb.GATE_LEVELS,
          "kapı seviyeleri mythbook ile aynı",
          "project_config.gates.levels ile mythbook.GATE_LEVELS ayrışmış")

    # faz kümülatifleri gerçekten toplanıyor mu
    running = 0
    bad = []
    for p in cfg["phases"]:
        running += p["storiesWritten"]
        if p["storiesCumulative"] != running:
            bad.append(f"{p['id']}: {p['storiesCumulative']} ≠ {running}")
    r.add(not bad, "faz kümülatif hikâye sayıları toplanıyor", f"tutmuyor: {bad}")
    r.add(running == mb.STORY_TARGET,
          f"fazların toplamı {mb.STORY_TARGET} hikâye",
          f"fazların toplamı {running}, hedef {mb.STORY_TARGET} — "
          "son yazım fazı 45/45'e ulaşmak ZORUNDA")

    # son yazım fazı, üretim fazından önce bitmeli
    writing_phases = [p for p in cfg["phases"] if p["storiesWritten"] > 0]
    last_writing = writing_phases[-1]["number"] if writing_phases else 0
    r.add(last_writing < len(cfg["phases"]),
          "yazım son fazdan ÖNCE bitiyor",
          "yazım son faza taşmış — üretim fazı yazımla aynı fazda olamaz")

    # görsel toplamı
    ill = cfg["illustration"]
    total = ill["storyOpenings"] + ill["cultureVignettes"] + ill["maps"]
    r.add(total == ill["total"],
          f"görsel toplamı tutuyor ({total})",
          f"{ill['storyOpenings']}+{ill['cultureVignettes']}+{ill['maps']} = {total} ≠ {ill['total']}")
    r.add(ill["storyOpenings"] == mb.STORY_TARGET,
          "hikâye açılış görseli sayısı hikâye sayısına eşit",
          f"{ill['storyOpenings']} görsel ≠ {mb.STORY_TARGET} hikâye")
    r.add(ill["cultureVignettes"] == mb.CULTURE_TARGET,
          "kültür vinyeti sayısı kültür sayısına eşit",
          f"{ill['cultureVignettes']} vinyet ≠ {mb.CULTURE_TARGET} kültür")

    # lansman formatları
    launch = [k for k, v in cfg["editions"].items() if v.get("enabled") and v.get("launch")]
    r.add("hardcover" in launch,
          "ciltli lansmanla birlikte açılıyor",
          "yol haritası: 'Bu kitapta ciltli LANSMANLA BİRLİKTE açılmalı — "
          "okul/kütüphane ve hediye alımı ciltliye gider'")


# =============================================================================
# GİRİŞ NOKTASI
# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description="Veri bütünlüğü kapısı")
    ap.add_argument("--gate", default=None, help="kapı seviyesi (varsayılan: .gate)")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    gate = args.gate or mb.read_gate()
    mb.gate_rank(gate)

    print("═" * 72)
    print(f"  VERİ BÜTÜNLÜĞÜ · kapı: {gate}")
    print("═" * 72)

    r = mb.Result(f"validate_spec[{gate}]", verbose=args.verbose)

    cultures = mb.load_cultures()
    stories = mb.load_stories()

    check_config(gate, r)
    check_cultures(cultures, gate, r)
    check_stories(stories, cultures, gate, r)
    check_research_gates(stories, cultures, gate, r)
    check_writing_gate(stories, gate, r)

    return r.finish(args.json)


if __name__ == "__main__":
    sys.exit(main())
