#!/usr/bin/env bash
# Re-capture Track B lab UI snapshots for learn_digital pass 2.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
SCRIPTS="$ROOT/.cursor/skills/module-slides/scripts"
BASE="${LAB_BASE:-http://127.0.0.1:8080/tools}"

capture() {
  local mod="$1" lab="$2"
  shift 2
  echo "=== $mod ($lab) ==="
  python3 "$SCRIPTS/capture_lab_snapshot.py" "courses/learn_digital/$mod" --lab "$lab" --base "$BASE" "$@"
}

capture module00-intro index --name tools-index.png
capture module01-radix-converter radix-converter
capture module02-twos-complement twos-complement
capture module03-overflow-wrap overflow-wrap
capture module04-ascii-hex ascii-hex
capture module05-gray-code gray-code
capture module06-bcd-lab bcd-lab
capture module07-parity-checksum parity-checksum
capture module08-fixed-point fixed-point
capture module09-bit-fields bit-fields
capture module10-endian-lab endian-lab
capture module11-truth-table truth-table
capture module12-boolean-laws boolean-laws
capture module13-kmap kmap
capture module14-sop-pos sop-pos
capture module15-dont-care-lab dont-care-lab
capture module16-logic-hazards logic-hazards
capture module17-gate-composer gate-composer
capture module18-mux-decoder mux-decoder
capture module19-priority-compare priority-compare
capture module20-half-full-adder half-full-adder
capture module21-xor-parity-tree xor-parity-tree
capture module22-tri-state-bus tri-state-bus
capture module23-barrel-shifter barrel-shifter
capture module24-seven-segment seven-segment
capture module25-clock-stepper clock-stepper
capture module26-setup-hold setup-hold
capture module27-reset-timelines reset-timelines
capture module28-clock-enable clock-enable
capture module29-cdc-sync cdc-sync
capture module30-fsm-lab fsm-lab
capture module31-state-encoding state-encoding
capture module32-seq-detector seq-detector
capture module33-ring-johnson ring-johnson
capture module34-lfsr-lab lfsr-lab
capture module35-ripple-carry-adder-animator ripple-carry-adder-animator
capture module36-carry-look-ahead-adder-propagate-and-generate carry-look-ahead-adder-propagate-and-generate
capture module37-array-mult array-mult
capture module38-alu-explorer alu-explorer
capture module39-carry-select-adder carry-select-adder
capture module40-booth-encode booth-encode
capture module41-signed-arith signed-arith
capture module42-mem-map mem-map
capture module43-fifo-lab fifo-lab
capture module44-cache-walk cache-walk
capture module45-dual-port-ram dual-port-ram
capture module46-byte-enable-mem byte-enable-mem
capture module47-async-fifo async-fifo
capture module48-handshake handshake
capture module49-block-diagram block-diagram
capture module50-wrap index --name tools-index.png

echo "Done: lab snapshots captured."
