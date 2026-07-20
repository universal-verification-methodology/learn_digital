#!/usr/bin/env python3
"""Re-sync slides and rebuild PDF/video (reuse existing TTS audio)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / ".cursor/skills/module-slides/scripts"


def run(cmd: list[str]) -> None:
    r = subprocess.run(cmd, cwd=ROOT)
    if r.returncode != 0:
        raise SystemExit(r.returncode)


def to_wsl(path: Path) -> str:
    s = str(path.resolve())
    if len(s) >= 2 and s[1] == ":":
        return f"/mnt/{s[0].lower()}{s[2:].replace(chr(92), '/')}"
    return s.replace(chr(92), "/")


def main() -> None:
    modules = sorted((ROOT / "courses/learn_digital").glob("module*"))
    n = 0
    build_video = SCRIPTS / "build_video.sh"
    for mod in modules:
        if not (mod / "transcript.md").is_file():
            continue
        n += 1
        print(f"\n======== {mod.name} ({n}) ========", flush=True)
        run([sys.executable, str(SCRIPTS / "transcript_to_outline.py"), str(mod)])
        run([sys.executable, str(SCRIPTS / "build_pptx.py"), str(mod)])
        run([sys.executable, str(SCRIPTS / "verify_transcript_consistency.py"), str(mod)])
        run([sys.executable, str(SCRIPTS / "verify_clip.py"), str(mod)])
        run(["bash", to_wsl(build_video), "--target-dir", to_wsl(mod)])
    print(f"\nDone: rebuilt {n} module deck(s).", flush=True)


if __name__ == "__main__":
    main()
