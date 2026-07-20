# learn_digital

[![GitHub](https://img.shields.io/badge/GitHub-learn__digital-181717?logo=github)](https://github.com/universal-verification-methodology/learn_digital)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](LICENSE)
[![Role](https://img.shields.io/badge/role-Git%20submodule-orange)](https://github.com/universal-verification-methodology/learning)
[![Parent](https://img.shields.io/badge/parent-learning%20monorepo-0A9EDC)](https://github.com/universal-verification-methodology/learning)
[![Labs](https://img.shields.io/badge/labs-GitHub%20Pages-222?logo=githubpages)](https://universal-verification-methodology.github.io/learning/tools/)
[![Domain](https://img.shields.io/badge/domain-digital%20logic%20%7C%20FSM%20%7C%20datapath-purple)](https://github.com/universal-verification-methodology/learn_digital)

**learn_digital** is the open learning path for *digital logic foundations without deep HDL syntax*.

Readers and students usually **open a module README** (or the live tools) or clone this public repo. Authors edit content here (or via the parent monorepo checkout), rebuild slides/audio with **module-slides** in the parent, and push; the parent repo only stores a pinned submodule commit.


## Table of contents

- [Contents](#contents)
- [Browse or clone](#browse-or-clone)
- [Consume from the parent](#consume-from-the-parent)
- [Author: publish or update](#author-publish-or-update)
- [Two learning tracks](#two-learning-tracks)
- [Module landings](#module-landings)
- [Browser labs](#browser-labs)
- [License](#license)

## Contents

```text
learn_digital/
├── README.md
├── LICENSE
├── docs/
│   ├── MODULES.md       # full module index (00–50)
│   └── TWO_TRACKS.md    # Track A (workbook) vs Track B (browser)
├── scripts/
│   └── module.sh
├── module00-intro/
├── module01-radix-converter/
│   ├── README.md · CHECKLIST.md · EXAMPLES.md
│   ├── outline.yaml · transcript.md
│   └── (optional) slides / video / assets/
├── …
└── module50-wrap/
```

Videos and decks are optional per module. Generate with the **module-slides** skill in the parent monorepo when ready.

## Browse or clone

- **Browser labs:** [https://universal-verification-methodology.github.io/learning/tools/](https://universal-verification-methodology.github.io/learning/tools/)
- **Syllabus (parent):** [`syllabus.md` § learn_digital](https://github.com/universal-verification-methodology/learning/blob/main/syllabus.md#3-learn_digital)
- **Clone this repo alone:**

```bash
git clone https://github.com/universal-verification-methodology/learn_digital.git
cd learn_digital
chmod +x scripts/*.sh
./scripts/module.sh 01 --check
```

Then open [module00-intro/README.md](module00-intro/README.md).

## Consume from the parent

```bash
git clone --recurse-submodules \
  git@github.com:universal-verification-methodology/learning.git
ls courses/learn_digital
```

## Author: publish or update

```bash
cd courses/learn_digital
# … edit module README / CHECKLIST / EXAMPLES / transcript …
cd ../..
python .cursor/skills/module-slides/scripts/transcript_to_outline.py \
  courses/learn_digital/moduleNN-slug
bash .cursor/skills/module-slides/scripts/narrate_clips.sh \
  courses/learn_digital/moduleNN-slug
```

## Two learning tracks

Every **lab** module documents both tracks. Intro/wrap have no lab. Details: [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md).

| Track | Practice surface | Start here |
|-------|------------------|------------|
| **A — Workbook** | Paper / sketches + `EXAMPLES.md` | [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md) |
| **B — Browser lab** | Platform tools | [local](http://127.0.0.1:8080/tools/) · [live](https://universal-verification-methodology.github.io/learning/tools/) |

Lab status snapshot: **46 shipped** · **3 planned** (see [docs/MODULES.md](docs/MODULES.md)).

## Module landings

Full status table: **[docs/MODULES.md](docs/MODULES.md)**. Clusters: 00 intro · 01–10 numbers · 11–16 Boolean · 17–24 gates · 25–29 clocks · 30–34 FSM · 35–41 datapath · 42–47 memory · 48–49 integration · 50 wrap → Verilog.

| Module | Landing |
|--------|---------|
| 00 — Welcome to digital foundations | [module00-intro](module00-intro/README.md) |
| 01 — Radix & bit width | [module01-radix-converter](module01-radix-converter/README.md) |
| 02 — Two’s complement | [module02-twos-complement](module02-twos-complement/README.md) |
| 03 — Overflow / wrap | [module03-overflow-wrap](module03-overflow-wrap/README.md) |
| 04 — ASCII / hex dump | [module04-ascii-hex](module04-ascii-hex/README.md) |
| 05 — Gray code | [module05-gray-code](module05-gray-code/README.md) |
| 06 — BCD | [module06-bcd-lab](module06-bcd-lab/README.md) |
| 07 — Parity / checksum | [module07-parity-checksum](module07-parity-checksum/README.md) |
| 08 — Fixed-point Qm.n | [module08-fixed-point](module08-fixed-point/README.md) |
| 09 — Bit-fields | [module09-bit-fields](module09-bit-fields/README.md) |
| 10 — Endian packing | [module10-endian-lab](module10-endian-lab/README.md) |
| 11 — Truth tables | [module11-truth-table](module11-truth-table/README.md) |
| 12 — Boolean laws | [module12-boolean-laws](module12-boolean-laws/README.md) |
| 13 — K-maps | [module13-kmap](module13-kmap/README.md) |
| 14 — SOP ↔ POS | [module14-sop-pos](module14-sop-pos/README.md) |
| 15 — Don’t-care minimization | [module15-dont-care-lab](module15-dont-care-lab/README.md) |
| 16 — Logic hazards | [module16-logic-hazards](module16-logic-hazards/README.md) |
| 17 — Gate composer | [module17-gate-composer](module17-gate-composer/README.md) |
| 18 — Mux / decoder / encoder | [module18-mux-decoder](module18-mux-decoder/README.md) |
| 19 — Priority & compare | [module19-priority-compare](module19-priority-compare/README.md) |
| 20 — Half / full adder | [module20-half-full-adder](module20-half-full-adder/README.md) |
| 21 — XOR parity tree | [module21-xor-parity-tree](module21-xor-parity-tree/README.md) |
| 22 — Tri-state / bus | [module22-tri-state-bus](module22-tri-state-bus/README.md) |
| 23 — Barrel shifter | [module23-barrel-shifter](module23-barrel-shifter/README.md) |
| 24 — Seven-segment | [module24-seven-segment](module24-seven-segment/README.md) |
| 25 — Clock-edge stepper | [module25-clock-stepper](module25-clock-stepper/README.md) |
| 26 — Setup / hold | [module26-setup-hold](module26-setup-hold/README.md) |
| 27 — Reset timelines | [module27-reset-timelines](module27-reset-timelines/README.md) |
| 28 — Clock enable vs gated clock | [module28-clock-enable](module28-clock-enable/README.md) |
| 29 — CDC / 2-FF sync | [module29-cdc-sync](module29-cdc-sync/README.md) |
| 30 — FSM designer | [module30-fsm-lab](module30-fsm-lab/README.md) |
| 31 — State encoding | [module31-state-encoding](module31-state-encoding/README.md) |
| 32 — Sequence detector | [module32-seq-detector](module32-seq-detector/README.md) |
| 33 — Ring / Johnson | [module33-ring-johnson](module33-ring-johnson/README.md) |
| 34 — LFSR / PRBS | [module34-lfsr-lab](module34-lfsr-lab/README.md) |
| 35 — Ripple-carry adder | [module35-ripple-carry-adder-animator](module35-ripple-carry-adder-animator/README.md) |
| 36 — Carry-lookahead G/P | [module36-carry-look-ahead-adder-propagate-and-generate](module36-carry-look-ahead-adder-propagate-and-generate/README.md) |
| 37 — Array multiplier | [module37-array-mult](module37-array-mult/README.md) |
| 38 — ALU explorer | [module38-alu-explorer](module38-alu-explorer/README.md) |
| 39 — Carry-select sketch | [module39-carry-select-adder](module39-carry-select-adder/README.md) |
| 40 — Booth encode | [module40-booth-encode](module40-booth-encode/README.md) |
| 41 — Signed arithmetic | [module41-signed-arith](module41-signed-arith/README.md) |
| 42 — RAM / ROM map | [module42-mem-map](module42-mem-map/README.md) |
| 43 — FIFO pointers | [module43-fifo-lab](module43-fifo-lab/README.md) |
| 44 — Cache walk | [module44-cache-walk](module44-cache-walk/README.md) |
| 45 — Dual-port RAM | [module45-dual-port-ram](module45-dual-port-ram/README.md) |
| 46 — Byte-enable memory | [module46-byte-enable-mem](module46-byte-enable-mem/README.md) |
| 47 — Async FIFO (Gray) | [module47-async-fifo](module47-async-fifo/README.md) |
| 48 — Handshake (valid/ready) | [module48-handshake](module48-handshake/README.md) |
| 49 — Block-diagram integrator | [module49-block-diagram](module49-block-diagram/README.md) |
| 50 — Digital complete → Verilog | [module50-wrap](module50-wrap/README.md) |

## Browser labs

Follow modules 01–49 in [docs/MODULES.md](docs/MODULES.md). Primary path: [radix-converter](https://universal-verification-methodology.github.io/learning/tools/radix-converter/) → number systems → Boolean → gates → clocks → FSM → datapath → memory → [handshake](https://universal-verification-methodology.github.io/learning/tools/handshake/) / [block-diagram](https://universal-verification-methodology.github.io/learning/tools/block-diagram/).

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see [`LICENSE`](LICENSE).

Concept path split from [`learn_digital_verilog`](https://github.com/universal-verification-methodology/learn_digital_verilog). Platform tools and the parent monorepo may carry additional notices.
