#!/usr/bin/env bash
# Mechanical checks on a PR worktree: build, image weight, stray files, external links.
# Usage: run_checks.sh <worktree-dir>
# Output is organized in [BUILD] / [IMAGES] / [STRAY] / [LINKS] sections with
# PASS / WARN / FAIL markers, for interpretation by the reviewer.
set -uo pipefail

WORKTREE="${1:?usage: run_checks.sh <worktree-dir>}"
MAIN_REPO="/home/pbellec/git/school-brainhack.github.io"
THEMES_DIR="${MAIN_REPO}/themes"

# Build with the exact Hugo version CI uses (see .github/workflows/hugo.yml).
# System hugo is too old (0.92) and snap hugo is too new (rejects a duplicate
# YAML key in config.yaml that 0.128 tolerates) — so pin and auto-download.
HUGO_VERSION="0.128.0"
HUGO_BIN_DIR="${HOME}/git/brainhack-pr-review/bin"
HUGO="${HUGO_BIN_DIR}/hugo"
if [ ! -x "$HUGO" ] || ! "$HUGO" version 2>/dev/null | grep -q "v${HUGO_VERSION}"; then
  echo "Downloading hugo_extended ${HUGO_VERSION}..."
  mkdir -p "$HUGO_BIN_DIR"
  curl -sL "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz" \
    | tar -xz -C "$HUGO_BIN_DIR" hugo
fi

cd "$WORKTREE"
CHANGED=$(git diff --name-status "origin/main...HEAD")
ADDED_OR_MODIFIED=$(echo "$CHANGED" | awk '$1 ~ /^(A|M)/ {print $2}')

########################################
echo "=== [BUILD] hugo --minify (hugo v${HUGO_VERSION} extended, same as CI) ==="
BUILD_LOG=$("$HUGO" --minify --themesDir "$THEMES_DIR" -d "${WORKTREE}/public" 2>&1)
if [ $? -eq 0 ]; then
  echo "PASS: site builds"
  echo "$BUILD_LOG" | grep -iE 'warn' && echo "WARN: build warnings above" || true
else
  echo "FAIL: build error"
  echo "$BUILD_LOG" | tail -30
fi

########################################
echo ""
echo "=== [IMAGES] size of images added/modified by the PR (WARN >500KB, FAIL >1.5MB) ==="
IMG_COUNT=0
while IFS= read -r f; do
  case "${f,,}" in
    *.png|*.jpg|*.jpeg|*.gif|*.webp|*.svg|*.bmp|*.tiff)
      IMG_COUNT=$((IMG_COUNT + 1))
      if [ -f "$f" ]; then
        SIZE=$(stat -c%s "$f")
        HUMAN=$(numfmt --to=iec "$SIZE")
        if [ "$SIZE" -gt 1500000 ]; then
          echo "FAIL: $f is ${HUMAN} (>1.5MB) — must be compressed/resized"
        elif [ "$SIZE" -gt 500000 ]; then
          echo "WARN: $f is ${HUMAN} (>500KB) — suggest compressing"
        else
          echo "PASS: $f (${HUMAN})"
        fi
      else
        echo "WARN: $f listed in diff but missing from worktree"
      fi
      ;;
  esac
done <<< "$ADDED_OR_MODIFIED"
[ "$IMG_COUNT" -eq 0 ] && echo "PASS: no images added or modified"

########################################
echo ""
echo "=== [STRAY] unexpected files in the PR ==="
STRAY=0
while IFS= read -r f; do
  [ -z "$f" ] && continue
  case "${f,,}" in
    *.ipynb|*.ds_store|*ipynb_checkpoints*|*__pycache__*|*.pyc|*.csv|*.tsv|*.nii|*.nii.gz|*.mat|*.pkl|*.pickle|*.npy|*.npz|*.zip|*.tar|*.tar.gz|*.h5|*.hdf5|*node_modules*|*.swp|*~|thumbs.db)
      echo "FAIL: stray file: $f"
      STRAY=$((STRAY + 1))
      ;;
  esac
  case "$f" in
    content/en/project/*) : ;;
    *)
      echo "WARN: touches file outside content/en/project/: $f"
      STRAY=$((STRAY + 1))
      ;;
  esac
done <<< "$ADDED_OR_MODIFIED"
# deletions outside project dirs are also suspicious
while IFS= read -r line; do
  f=$(echo "$line" | awk '$1 == "D" {print $2}')
  [ -z "$f" ] && continue
  case "$f" in
    content/en/project/*) echo "WARN: deletes $f" ;;
    *) echo "FAIL: deletes file outside content/en/project/: $f"; STRAY=$((STRAY + 1)) ;;
  esac
done <<< "$CHANGED"
[ "$STRAY" -eq 0 ] && echo "PASS: only expected project content files"

########################################
echo ""
echo "=== [LINKS] external links in added/modified markdown (HTTP status) ==="
URLS=$(echo "$ADDED_OR_MODIFIED" | grep -E '\.md$' | while IFS= read -r f; do
  [ -f "$f" ] && grep -oE 'https?://[^ )>"\\`]+' "$f"
done | sed 's/[.,;:]*$//' | sort -u)
if [ -z "$URLS" ]; then
  echo "PASS: no external links found"
else
  while IFS= read -r url; do
    CODE=$(curl -sIL -o /dev/null -w '%{http_code}' --max-time 15 -A "Mozilla/5.0 (X11; Linux x86_64)" "$url" 2>/dev/null)
    case "$CODE" in
      2*|3*) echo "PASS: $CODE $url" ;;
      403|405|429|999) echo "WARN: $CODE $url (may be bot-blocking; verify manually)" ;;
      000) echo "WARN: no response (timeout/DNS) $url" ;;
      *) echo "FAIL: $CODE $url" ;;
    esac
  done <<< "$URLS"
fi

echo ""
echo "=== checks done ==="
