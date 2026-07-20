#!/usr/bin/env python3
"""Re-capture Track B lab UI snapshots for learn_digital pass 2."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / ".cursor/skills/module-slides/scripts"
BASE = "http://127.0.0.1:8080/tools"

CAPTURES: list[tuple[str, str, list[str]]] = [
    ("module00-intro", "index", ["--name", "tools-index.png"]),
    ("module01-radix-converter", "radix-converter", []),
    ("module02-twos-complement", "twos-complement", []),
    ("module03-overflow-wrap", "overflow-wrap", []),
    ("module04-ascii-hex", "ascii-hex", []),
    ("module05-gray-code", "gray-code", []),
    ("module06-bcd-lab", "bcd-lab", []),
    ("module07-parity-checksum", "parity-checksum", []),
    ("module08-fixed-point", "fixed-point", []),
    ("module09-bit-fields", "bit-fields", []),
    ("module10-endian-lab", "endian-lab", []),
    ("module11-truth-table", "truth-table", []),
    ("module12-boolean-laws", "boolean-laws", []),
    ("module13-kmap", "kmap", []),
    ("module14-sop-pos", "sop-pos", []),
    ("module15-dont-care-lab", "dont-care-lab", []),
    ("module16-logic-hazards", "logic-hazards", []),
    ("module17-gate-composer", "gate-composer", []),
    ("module18-mux-decoder", "mux-decoder", []),
    ("module19-priority-compare", "priority-compare", []),
    ("module20-half-full-adder", "half-full-adder", []),
    ("module21-xor-parity-tree", "xor-parity-tree", []),
    ("module22-tri-state-bus", "tri-state-bus", []),
    ("module23-barrel-shifter", "barrel-shifter", []),
    ("module24-seven-segment", "seven-segment", []),
    ("module25-clock-stepper", "clock-stepper", []),
    ("module26-setup-hold", "setup-hold", []),
    ("module27-reset-timelines", "reset-timelines", []),
    ("module28-clock-enable", "clock-enable", []),
    ("module29-cdc-sync", "cdc-sync", []),
    ("module30-fsm-lab", "fsm-lab", []),
    ("module31-state-encoding", "state-encoding", []),
    ("module32-seq-detector", "seq-detector", []),
    ("module33-ring-johnson", "ring-johnson", []),
    ("module34-lfsr-lab", "lfsr-lab", []),
    ("module35-ripple-carry-adder-animator", "ripple-carry-adder-animator", []),
    ("module36-carry-look-ahead-adder-propagate-and-generate", "carry-look-ahead-adder-propagate-and-generate", []),
    ("module37-array-mult", "array-mult", []),
    ("module38-alu-explorer", "alu-explorer", []),
    ("module39-carry-select-adder", "carry-select-adder", []),
    ("module40-booth-encode", "booth-encode", []),
    ("module41-signed-arith", "signed-arith", []),
    ("module42-mem-map", "mem-map", []),
    ("module43-fifo-lab", "fifo-lab", []),
    ("module44-cache-walk", "cache-walk", []),
    ("module45-dual-port-ram", "dual-port-ram", []),
    ("module46-byte-enable-mem", "byte-enable-mem", []),
    ("module47-async-fifo", "async-fifo", []),
    ("module48-handshake", "handshake", []),
    ("module49-block-diagram", "block-diagram", []),
    ("module50-wrap", "index", ["--name", "tools-index.png"]),
]


def main() -> int:
    failed: list[str] = []
    for mod, lab, extra in CAPTURES:
        print(f"=== {mod} ({lab}) ===", flush=True)
        cmd = [
            sys.executable,
            str(SCRIPTS / "capture_lab_snapshot.py"),
            f"courses/learn_digital/{mod}",
            "--lab",
            lab,
            "--base",
            BASE,
            *extra,
        ]
        r = subprocess.run(cmd, cwd=ROOT)
        if r.returncode != 0:
            failed.append(mod)
    if failed:
        print(f"FAILED ({len(failed)}): {', '.join(failed)}", flush=True)
        return 1
    print("Done: lab snapshots captured.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
