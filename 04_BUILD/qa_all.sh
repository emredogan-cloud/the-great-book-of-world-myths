#!/usr/bin/env bash
# =============================================================================
# THE GREAT BOOK OF WORLD MYTHS — BÜTÜN KALİTE KAPILARI
# =============================================================================
# CI'ın çalıştırdığı komutların birebir aynısı. Push etmeden önce yerelde
# koşturun; yeşilse CI de yeşil olur.
#
#   ./04_BUILD/qa_all.sh                mevcut kapı seviyesiyle (.gate)
#   ./04_BUILD/qa_all.sh phase1         kapıyı yükselterek dene
#   ./04_BUILD/qa_all.sh --fix          üretilen belgeleri tazeleyerek
#
# Hafif kapıların hiçbiri venv gerektirmez; hepsi standart kütüphaneyle
# koşar (karar K7). Görsel işleri Pillow ister ve yoksa ATLANIR.
# =============================================================================
set -uo pipefail

BUILD="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(dirname "$BUILD")"
TESTS="$ROOT/05_TESTS"
cd "$ROOT"

GATE=""
FIX=0
for arg in "$@"; do
  case "$arg" in
    --fix) FIX=1 ;;
    phase0|phase1|phase2|phase3|phase4|phase5|release) GATE="$arg" ;;
    *) echo "bilinmeyen argüman: $arg" >&2; exit 2 ;;
  esac
done

# Kapı seviyesi `.gate` dosyasındadır; yalnızca AÇIKÇA verilirse o kazanır.
# (Bestiarium'da `--fix` kapıyı draft'a düşürüyordu — yani belgeleri
# tazeleyen koşu açılmış kapıları HİÇ denetlemiyordu.)
if [ -z "$GATE" ]; then
  GATE="$( [ -f .gate ] && tr -d '[:space:]' < .gate || echo phase0 )"
fi

PY="${PYTHON:-python3}"
VENV_PY="$PY"
[ -x "$BUILD/.venv/bin/python" ] && VENV_PY="$BUILD/.venv/bin/python"

FAILED=()
SKIPPED=()

run () {
  local name="$1"; shift
  echo
  echo "──────────────────────────────────────────────────────────────────────"
  echo "▸ $name"
  echo "──────────────────────────────────────────────────────────────────────"
  if "$@"; then return 0; else FAILED+=("$name"); return 1; fi
}

# Pillow isteyen işler: çıkış 2 = ATLANDI, gerçek bir kalite düşüşü değil.
run_optional () {
  local name="$1"; shift
  echo
  echo "──────────────────────────────────────────────────────────────────────"
  echo "▸ $name"
  echo "──────────────────────────────────────────────────────────────────────"
  "$@"
  case $? in
    0) ;;
    2) echo "ATLANDI: bağımlılık yok — pip install -r 04_BUILD/requirements.txt"
       SKIPPED+=("$name") ;;
    *) FAILED+=("$name") ;;
  esac
}

echo "════════════════════════════════════════════════════════════════════════"
echo "  THE GREAT BOOK OF WORLD MYTHS · KALİTE KAPILARI · kapı: $GATE"
echo "════════════════════════════════════════════════════════════════════════"

# SIRA ÖNEMLİ: research_gen dizinden kayıtları üretir, make_index arka
# maddeyi üretir, update_docs ikisini de ölçer.
if [ "$FIX" = "1" ]; then
  echo "▸ üretilen belgeler tazeleniyor…"
  $PY 04_BUILD/research_gen.py  >/dev/null
  $PY 04_BUILD/make_prompts.py  >/dev/null
  $PY 04_BUILD/make_index.py    >/dev/null
  $PY 04_BUILD/update_docs.py   >/dev/null
fi

# ── YAPILANDIRMA VE VERİ ────────────────────────────────────────────────────
run "veri bütünlüğü"            $PY 04_BUILD/validate_spec.py --gate "$GATE" \
                                   --json 06_REPORTS/spec-validation.json
run "depo ve belge bütünlüğü"   $PY 04_BUILD/validate_structure.py \
                                   --json 06_REPORTS/structure.json
run "araştırma kayıtları"       $PY 04_BUILD/validate_research.py \
                                   --json 06_REPORTS/research.json

# ── KAPILARIN KENDİ TESTİ — en önemlisi ────────────────────────────────────
run "KAPILARIN KENDİ TESTİ"     $PY 05_TESTS/selftest.py

# ── METİN KAPILARI ─────────────────────────────────────────────────────────
run "kelime bandı"              $PY 04_BUILD/qa_length.py --json 06_REPORTS/qa-length.json
run "YAŞ POLİTİKASI"            $PY 04_BUILD/qa_age.py --json 06_REPORTS/qa-age.json
run "okunabilirlik (8–12 yaş)"  $PY 04_BUILD/qa_readability.py --json 06_REPORTS/qa-readability.json
run "ses ve yasak kalıp"        $PY 04_BUILD/qa_voice.py --json 06_REPORTS/qa-voice.json
run "tekrar taraması"           $PY 04_BUILD/qa_echo.py --json 06_REPORTS/qa-echo.json
run "diakritik ve adlandırma"   $PY 04_BUILD/qa_diacritics.py --json 06_REPORTS/qa-diacritics.json
run "çapraz referans ve kapsam" $PY 04_BUILD/qa_crossref.py --json 06_REPORTS/qa-crossref.json
run "üslup sürüklenmesi"        $PY 04_BUILD/qa_drift.py --json 06_REPORTS/qa-drift.json

# ── ÜRETİM MODELİ ──────────────────────────────────────────────────────────
run "sürüm ve telif modeli"     $PY 04_BUILD/editions.py --json 06_REPORTS/editions.json
run "sayfa bütçesi"             $PY 04_BUILD/page_budget.py --json 06_REPORTS/page-budget.json

# ── GÖRSEL HATTI (Pillow ister) ────────────────────────────────────────────
run_optional "görsel ölçümünün kalibrasyonu" \
                                $VENV_PY 05_TESTS/image_selftest.py \
                                --json 06_REPORTS/tracked/image-calibration.json
# Envanter ÖNCE koşar: 68 dosya gerçekten var mı, bozuk mu, doğru kültüre mi
# bağlı. Kalite ölçümü bu soruyu sormaz ve yanlış kültüre bağlanmış kusursuz
# bir vinyet bütün kalite kapılarından geçer.
run_optional "ham varlık envanteri"          \
                                $VENV_PY 04_BUILD/asset_inventory.py --check
run_optional "görsel format bütçeleri"       \
                                $VENV_PY 04_BUILD/convert_images.py --check
run_optional "görsel tutarlılığı"            \
                                $VENV_PY 04_BUILD/images.py

# ── FAZ 5 ÜRETİMİ (reportlab + Pillow ister) ───────────────────────────────
# Bu üç kapı Faz 5'te doğdu ve üretim yüzeyini denetler: gerçek PDF, gerçek
# EPUB, gerçek metadata. Manuscript yoksa "uygulanamaz" derler — DEVRE DIŞI
# değil (K18: denetlenecek rapor DEPODA durur).
run_optional "üretim iç bloğu güncel"        \
                                $VENV_PY 04_BUILD/interior.py --check
run_optional "Kindle EPUB güncel"            \
                                $VENV_PY 04_BUILD/epub.py --check
run "KDP metadata paketi"       $PY 04_BUILD/metadata.py --check

# ── FAZ 6 · KDP PAKETİ (reportlab + Pillow + poppler ister) ────────────────
# Kapak sayfa sayısına bağlıdır: sayfa sayısı değişirse sırt kayar ve eski
# kapak GEÇERSİZ olur. Bu yüzden kapak kapısı iç blok kapısından SONRA koşar.
run_optional "PAKET KAPILARININ KENDİ TESTİ" \
                                $VENV_PY 05_TESTS/package_selftest.py
run_optional "kapak üretimi güncel"          \
                                $VENV_PY 04_BUILD/covers.py --check
run_optional "A+ modülleri güncel"           \
                                $VENV_PY 04_BUILD/aplus.py --check
run_optional "KDP teslim belgeleri güncel"   \
                                $VENV_PY 04_BUILD/handoff.py --check

# ── ÜRETİLEN BELGELER BAYAT MI ─────────────────────────────────────────────
run "prompt kütüphanesi güncel" $PY 04_BUILD/make_prompts.py --check
# Sayfa kalibrasyonu reportlab ister; manuscript yoksa da atlanır. Bir
# kapının varlığı yetmez, KOŞMASI gerekir — bu satır olmadan
# calibrate_pages.py ölü bir betik olurdu (karar K18'in aynı dersi).
run_optional "sayfa kalibrasyonu güncel" \
                                $VENV_PY 04_BUILD/calibrate_pages.py --check
# Ara prova: yapısal regresyon avı (taşma, sıra, başlık, görsel eşlemesi).
# reportlab ister ve manuscript yoksa "uygulanamaz" der — kapı DEVRE DIŞI değil.
run_optional "ara prova dizgisi güncel" \
                                $VENV_PY 04_BUILD/proof_interior.py --check
run "araştırma kayıtları güncel" $PY 04_BUILD/research_gen.py --check
run "arka madde önizlemesi güncel" $PY 04_BUILD/make_index.py --check
run "üretilen belgeler güncel"  $PY 04_BUILD/update_docs.py --check

# ── ÖZET ───────────────────────────────────────────────────────────────────
echo
echo "════════════════════════════════════════════════════════════════════════"
if [ ${#SKIPPED[@]} -gt 0 ]; then
  echo "  ⊘ ${#SKIPPED[@]} kapı atlandı (bağımlılık yok):"
  for s in "${SKIPPED[@]}"; do echo "     · $s"; done
fi
if [ ${#FAILED[@]} -eq 0 ]; then
  echo "  ✅ BÜTÜN KAPILAR YEŞİL · kapı seviyesi: $GATE"
  echo "════════════════════════════════════════════════════════════════════════"
  exit 0
fi
echo "  ⛔ ${#FAILED[@]} KAPI KIRMIZI"
for f in "${FAILED[@]}"; do echo "     · $f"; done
echo "════════════════════════════════════════════════════════════════════════"
echo
echo "  Kalite düştü. Düzeltilmeden ilerleme yok."
echo "  Üretilen belge bayatsa:  ./04_BUILD/qa_all.sh --fix"
exit 1
