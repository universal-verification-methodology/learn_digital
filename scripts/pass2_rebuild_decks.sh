#!/usr/bin/env bash
# Re-sync slides and rebuild PDF/video (reuse existing TTS audio).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
SCRIPTS="$ROOT/.cursor/skills/module-slides/scripts"
cd "$ROOT"

n=0
for d in courses/learn_digital/module*; do
  [[ -f "$d/transcript.md" ]] || continue
  n=$((n + 1))
  echo
  echo "======== $(basename "$d") ($n) ========"
  python3 "$SCRIPTS/transcript_to_outline.py" "$d"
  python3 "$SCRIPTS/build_pptx.py" "$d"
  python3 "$SCRIPTS/verify_transcript_consistency.py" "$d"
  python3 "$SCRIPTS/verify_clip.py" "$d"
  bash "$SCRIPTS/build_video.sh" --target-dir "$d"
done

echo
echo "Done: rebuilt $n module deck(s)."
