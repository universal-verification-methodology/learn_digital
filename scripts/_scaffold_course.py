#!/usr/bin/env python3
"""Scaffold courses/learn_digital from syllabus (lab-driven + dual tracks)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # courses/learn_digital
COURSES = ROOT.parent
DST = ROOT

LAB_BASE_LOCAL = "http://127.0.0.1:8080/tools"
LAB_BASE_LIVE = "https://universal-verification-methodology.github.io/learning/tools"

# (num, slug, kind, title, lab_id|None, status S|P|None)
MODULES = [
    (0, "intro", "intro", "Welcome to digital foundations", None, None),
    (1, "radix-converter", "lab", "Radix & bit width", "radix-converter", "S"),
    (2, "twos-complement", "lab", "Two’s complement", "twos-complement", "S"),
    (3, "overflow-wrap", "lab", "Overflow / wrap", "overflow-wrap", "S"),
    (4, "ascii-hex", "lab", "ASCII / hex dump", "ascii-hex", "S"),
    (5, "gray-code", "lab", "Gray code", "gray-code", "S"),
    (6, "bcd-lab", "lab", "BCD", "bcd-lab", "S"),
    (7, "parity-checksum", "lab", "Parity / checksum", "parity-checksum", "S"),
    (8, "fixed-point", "lab", "Fixed-point Qm.n", "fixed-point", "S"),
    (9, "bit-fields", "lab", "Bit-fields", "bit-fields", "S"),
    (10, "endian-lab", "lab", "Endian packing", "endian-lab", "S"),
    (11, "truth-table", "lab", "Truth tables", "truth-table", "S"),
    (12, "boolean-laws", "lab", "Boolean laws", "boolean-laws", "S"),
    (13, "kmap", "lab", "K-maps", "kmap", "S"),
    (14, "sop-pos", "lab", "SOP ↔ POS", "sop-pos", "S"),
    (15, "dont-care-lab", "lab", "Don’t-care minimization", "dont-care-lab", "S"),
    (16, "logic-hazards", "lab", "Logic hazards", "logic-hazards", "S"),
    (17, "gate-composer", "lab", "Gate composer", "gate-composer", "S"),
    (18, "mux-decoder", "lab", "Mux / decoder / encoder", "mux-decoder", "S"),
    (19, "priority-compare", "lab", "Priority & compare", "priority-compare", "S"),
    (20, "half-full-adder", "lab", "Half / full adder", "half-full-adder", "S"),
    (21, "xor-parity-tree", "lab", "XOR parity tree", "xor-parity-tree", "S"),
    (22, "tri-state-bus", "lab", "Tri-state / bus", "tri-state-bus", "S"),
    (23, "barrel-shifter", "lab", "Barrel shifter", "barrel-shifter", "S"),
    (24, "seven-segment", "lab", "Seven-segment", "seven-segment", "S"),
    (25, "clock-stepper", "lab", "Clock-edge stepper", "clock-stepper", "S"),
    (26, "setup-hold", "lab", "Setup / hold", "setup-hold", "S"),
    (27, "reset-timelines", "lab", "Reset timelines", "reset-timelines", "S"),
    (28, "clock-enable", "lab", "Clock enable vs gated clock", "clock-enable", "S"),
    (29, "cdc-sync", "lab", "CDC / 2-FF sync", "cdc-sync", "S"),
    (30, "fsm-lab", "lab", "FSM designer", "fsm-lab", "S"),
    (31, "state-encoding", "lab", "State encoding", "state-encoding", "S"),
    (32, "seq-detector", "lab", "Sequence detector", "seq-detector", "S"),
    (33, "ring-johnson", "lab", "Ring / Johnson", "ring-johnson", "S"),
    (34, "lfsr-lab", "lab", "LFSR / PRBS", "lfsr-lab", "S"),
    (35, "ripple-carry-adder-animator", "lab", "Ripple-carry adder", "ripple-carry-adder-animator", "S"),
    (36, "carry-look-ahead-adder-propagate-and-generate", "lab", "Carry-lookahead G/P",
     "carry-look-ahead-adder-propagate-and-generate", "S"),
    (37, "array-mult", "lab", "Array multiplier", "array-mult", "S"),
    (38, "alu-explorer", "lab", "ALU explorer", "alu-explorer", "S"),
    (39, "carry-select-adder", "lab", "Carry-select sketch", "carry-select-adder", "S"),
    (40, "booth-encode", "lab", "Booth encode", "booth-encode", "S"),
    (41, "signed-arith", "lab", "Signed arithmetic", "signed-arith", "S"),
    (42, "mem-map", "lab", "RAM / ROM map", "mem-map", "S"),
    (43, "fifo-lab", "lab", "FIFO pointers", "fifo-lab", "S"),
    (44, "cache-walk", "lab", "Cache walk", "cache-walk", "S"),
    (45, "dual-port-ram", "lab", "Dual-port RAM", "dual-port-ram", "S"),
    (46, "byte-enable-mem", "lab", "Byte-enable memory", "byte-enable-mem", "S"),
    (47, "async-fifo", "lab", "Async FIFO (Gray)", "async-fifo", "S"),
    (48, "handshake", "lab", "Handshake (valid/ready)", "handshake", "S"),
    (49, "block-diagram", "lab", "Block-diagram integrator", "block-diagram", "S"),
    (50, "wrap", "wrap", "Digital complete → Verilog", None, None),
]


def mod_dir(num: int, slug: str) -> Path:
    return DST / f"module{num:02d}-{slug}"


def lab_urls(lab_id: str) -> tuple[str, str]:
    return (f"{LAB_BASE_LOCAL}/{lab_id}/index.html", f"{LAB_BASE_LIVE}/{lab_id}/")


def write_module_readme(
    num: int, slug: str, kind: str, title: str, lab_id: str | None, status: str | None
) -> None:
    d = mod_dir(num, slug)
    d.mkdir(parents=True, exist_ok=True)
    nn = f"{num:02d}"
    prev = next((m for m in MODULES if m[0] == num - 1), None)
    nxt = next((m for m in MODULES if m[0] == num + 1), None)

    nav = []
    if prev:
        nav.append(f"[← {prev[3]}](../module{prev[0]:02d}-{prev[1]}/README.md)")
    else:
        nav.append("← Start")
    nav.append("[Course README](../README.md)")
    if nxt:
        nav.append(f"[{nxt[3]} →](../module{nxt[0]:02d}-{nxt[1]}/README.md)")
    else:
        nav.append("End →")
    nav_line = " · ".join(nav)

    if kind == "intro":
        body = f"""# Module {nn}: {title}

**Kind:** `intro` · Dual-track course welcome

{nav_line}

## What this course is

**learn_digital** teaches digital logic foundations **without deep HDL syntax**, using two modes on every lab module:

| Track | Where you practice | Best for |
|-------|--------------------|----------|
| **A — Workbook** | Paper / notes / mental models | Muscle memory for tables, encodings, timing sketches |
| **B — Browser lab** | Interactive lab on the learning platform | Instant feedback, challenges, visual intuition |

You can do **A only**, **B only**, or **both** (recommended: B for intuition, then A to harden the idea).

HDL coding lands in **learn_verilog** / **learn_systemverilog**. Legacy combined path: [`../learn_digital_verilog/`](../learn_digital_verilog/).

## Setup (Track A)

1. Notebook or tablet for truth tables, timing sketches, and encodings.
2. Optional: skim [`../learn_digital_verilog/`](../learn_digital_verilog/) only as stretch — not required here.

## Setup (Track B)

1. Serve the platform: `python -m http.server 8080 --directory platform` (from monorepo root).
2. Open http://127.0.0.1:8080/tools/index.html
3. Or use the live site: {LAB_BASE_LIVE}/

## How to move through modules

1. Read the module **README** (outcomes).
2. Pick a track (or both).
3. Check off **CHECKLIST.md**.
4. Optional: skim `outline.yaml` / `transcript.md` for upcoming slides & clips.

## Media (planned)

| Artifact | Path |
|----------|------|
| Outline | [outline.yaml](outline.yaml) |
| Transcript stub | [transcript.md](transcript.md) |
| Slides / video | generate later with **module-slides** |

## Next

→ [Module 01: Radix & bit width](../module01-radix-converter/README.md)
"""
    elif kind == "wrap":
        body = f"""# Module {nn}: {title}

**Kind:** `wrap`

{nav_line}

## You can now

- Move fluently across number systems, Boolean minimization, and gate blocks
- Reason about clocks, resets, CDC, and FSM encodings
- Sketch adders, ALUs, memory maps, FIFOs, and handshakes at the concept level

## Dual-track recap

If you mainly used **browser labs**, redo a few Track A sketches for modules 11–13, 25–27, and 30–32 so tables and timing feel natural on paper.  
If you mainly used **workbook**, open any skipped browser labs for interactive challenges.

## Next course

→ **learn_verilog** (syllabus: [../../syllabus.md](../../syllabus.md#4-learn_verilog))  
Legacy combined path: [`../learn_digital_verilog/`](../learn_digital_verilog/).

## Checklist

- [ ] I completed Track A and/or Track B for the lab modules I care about
- [ ] I can explain radix, two’s complement, and a simple FSM encoding without looking it up
- [ ] I am ready to map these concepts into Verilog modules
"""
    else:
        assert lab_id and status
        local, live = lab_urls(lab_id)
        status_note = (
            "Shipped"
            if status == "S"
            else "Planned (Coming soon on tools index — use Track A until it ships)"
        )
        body = f"""# Module {nn}: {title}

**Kind:** `lab` · Primary lab: `{lab_id}` · **{status_note}**

{nav_line}

## Outcomes

After this module you can explain and practice the ideas taught by **`{lab_id}`**, in the browser and/or on paper.

## Two tracks (pick one or both)

### Track A — Workbook (hands-on)

1. Open [EXAMPLES.md](EXAMPLES.md) and work the paper / sketch prompts.
2. Complete [CHECKLIST.md](CHECKLIST.md) without relying only on the UI.
3. Optional self-check: `./scripts/module.sh {nn} --check` (from course root).

### Track B — Browser lab (online)

1. Local: [{local}]({local})
2. Live: [{live}]({live})
3. Load the **starter example**, then work challenges.
4. Check off the Track B items in [CHECKLIST.md](CHECKLIST.md).

> Concept labs are literacy tools — they prepare you for RTL courses; they do not replace writing synthesizable HDL.

## Media (planned)

| Artifact | Path |
|----------|------|
| Outline | [outline.yaml](outline.yaml) |
| Transcript stub | [transcript.md](transcript.md) |
| Slides / video | generate later with **module-slides** |

## Files

```
module{nn}-{slug}/
├── README.md
├── CHECKLIST.md
├── EXAMPLES.md
├── outline.yaml
├── transcript.md
└── (optional) examples/   # stretch notes only
```
"""
    (d / "README.md").write_text(body, encoding="utf-8")


def write_checklist(num: int, slug: str, kind: str, title: str, lab_id: str | None) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    if kind == "intro":
        text = f"""# Module {nn} checklist — {title}

## Setup

- [ ] Notebook / tablet ready for Track A sketches
- [ ] Opened this repo at `courses/learn_digital`
- [ ] Opened the [tools index]({LAB_BASE_LOCAL}/index.html) once (or live site)

## Mindset

- [ ] I understand Track A = workbook, Track B = browser lab
- [ ] I know HDL coding is deferred to **learn_verilog**
"""
    elif kind == "wrap":
        text = f"""# Module {nn} checklist — {title}

- [ ] Reviewed outcomes in [README.md](README.md)
- [ ] Ready to start **learn_verilog** (or revisit weak modules)
"""
    else:
        text = f"""# Module {nn} checklist — {title}

## Track A — Workbook

- [ ] Worked through at least one prompt in [EXAMPLES.md](EXAMPLES.md)
- [ ] Can explain the outcome in my own words (no UI crutches)

## Track B — Browser lab (`{lab_id}`)

- [ ] Opened the lab (local or live)
- [ ] Loaded the starter example
- [ ] Completed a few challenges (or noted the lab is still Coming soon)

## Done when

- [ ] I can do the task on paper **or** I finished the browser challenges (preferably both)
"""
    (d / "CHECKLIST.md").write_text(text, encoding="utf-8")


def write_examples_md(num: int, slug: str, kind: str, title: str) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    if kind != "lab":
        (d / "EXAMPLES.md").write_text(
            f"# Module {nn} — no workbook trees\n\nThis is an `{kind}` module. See [README.md](README.md).\n",
            encoding="utf-8",
        )
        return
    text = f"""# Module {nn} examples — {title}

Track A (workbook). No mandatory HDL trees — stay concept-first.

## Paper prompts

1. Restate the core idea of this module in one sentence.
2. Draw or tabulate one worked example (truth table, encoding, timing, pointer diagram, …).
3. Name one pitfall you would watch for in later RTL courses.

## Stretch (optional)

Peek at [`../learn_digital_verilog/`](../learn_digital_verilog/) only if you want a Verilog preview — not required for **learn_digital**.
"""
    (d / "EXAMPLES.md").write_text(text, encoding="utf-8")


def write_outline_transcript(num: int, slug: str, kind: str, title: str, lab_id: str | None) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    (d / "outline.yaml").write_text(
        f"""# Module {nn} outline
title: "{title}"
kind: {kind}
lab: {lab_id or "null"}
slides:
  - Course context / why this matters for digital design
  - Core idea (1 concept)
  - Track B: show lab starter (if lab module)
  - Track A: one paper / sketch demo
  - Common pitfalls
  - Your turn + quiz prompt
duration_minutes: 8
""",
        encoding="utf-8",
    )
    show_b = (
        f"Open the browser lab, `{lab_id}`. Load the starter. Point at the UI."
        if lab_id
        else "Point at the course map / tools index."
    )
    (d / "transcript.md").write_text(
        f"""# Module {nn} transcript — {title}

> Stub for voiceover / clip. Expand when recording (module-slides).

## Hook

In digital design you will live in bits, gates, and timing. This module: **{title}**.

## Teach

(3–5 sentences on the concept.)

## Show Track B

{show_b}

## Show Track A

On paper or a whiteboard, demonstrate one sketch from EXAMPLES.md.

## Your turn

Complete the checklist for at least one track. Then take the short quiz.
""",
        encoding="utf-8",
    )


def write_docs_index() -> None:
    docs = DST / "docs"
    docs.mkdir(exist_ok=True)
    rows = []
    for num, slug, kind, title, lab_id, status in MODULES:
        lab = f"`{lab_id}`" if lab_id else "—"
        st = status or "—"
        rows.append(
            f"| {num:02d} | `{kind}` | [{title}](../module{num:02d}-{slug}/README.md) | {lab} | {st} |"
        )
    (docs / "MODULES.md").write_text(
        f"""# learn_digital — module index

Lab-driven syllabus (pass 3). Full product syllabus: [../../syllabus.md](../../syllabus.md#3-learn_digital).

| # | Kind | Module | Lab | Status |
|---|------|--------|-----|--------|
{chr(10).join(rows)}

## Dual tracks

See [TWO_TRACKS.md](TWO_TRACKS.md).
""",
        encoding="utf-8",
    )
    (docs / "TWO_TRACKS.md").write_text(
        f"""# Two learning tracks

## Track A — Workbook

Practice with paper, notes, and mental models (no install).

- Prompts live under each `moduleNN-*/EXAMPLES.md`
- Self-check: `./scripts/module.sh NN --check`

Use this track when you need **fidelity of thought**: tables, encodings, timing sketches you can redo without a UI.

## Track B — Browser lab

Practice in the learning platform concept labs.

- Local tools: {LAB_BASE_LOCAL}/
- Live: {LAB_BASE_LIVE}/
- Each lab module README links its primary lab id

Use this track for **intuition** and quick challenges. Planned labs show “Coming soon”; use Track A until they ship.

## Recommended path

1. **Track B** starter + a few challenges (5–10 min)
2. **Track A** paper sketch + checklist (5–15 min)
3. Optional quiz / transcript review

Doing only one track is OK for self-study; **learn_verilog** expects comfort with the concepts from both.
""",
        encoding="utf-8",
    )


def write_course_readme() -> None:
    landing = [
        f"| {num:02d} — {title} | [module{num:02d}-{slug}](module{num:02d}-{slug}/README.md) |"
        for num, slug, _k, title, *_ in MODULES
    ]
    shipped = sum(1 for m in MODULES if m[5] == "S")
    planned = sum(1 for m in MODULES if m[5] == "P")
    (DST / "README.md").write_text(
        "\n".join(
            [
                "# learn_digital",
                "",
                "[![GitHub](https://img.shields.io/badge/GitHub-learn__digital-181717?logo=github)](https://github.com/universal-verification-methodology/learn_digital)",
                "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](LICENSE)",
                "[![Role](https://img.shields.io/badge/role-Git%20submodule-orange)](https://github.com/universal-verification-methodology/learning)",
                "[![Parent](https://img.shields.io/badge/parent-learning%20monorepo-0A9EDC)](https://github.com/universal-verification-methodology/learning)",
                "[![Labs](https://img.shields.io/badge/labs-GitHub%20Pages-222?logo=githubpages)](https://universal-verification-methodology.github.io/learning/tools/)",
                "[![Domain](https://img.shields.io/badge/domain-digital%20logic%20%7C%20FSM%20%7C%20datapath-purple)](https://github.com/universal-verification-methodology/learn_digital)",
                "",
                "**learn_digital** is the open learning path for *digital logic foundations without deep HDL syntax*.",
                "",
                "Readers and students usually **open a module README** (or the live tools) or clone this public repo. Authors edit content here (or via the parent monorepo checkout), rebuild slides/audio with **module-slides** in the parent, and push; the parent repo only stores a pinned submodule commit.",
                "",
                "",
                "## Table of contents",
                "",
                "- [Contents](#contents)",
                "- [Browse or clone](#browse-or-clone)",
                "- [Consume from the parent](#consume-from-the-parent)",
                "- [Author: publish or update](#author-publish-or-update)",
                "- [Two learning tracks](#two-learning-tracks)",
                "- [Module landings](#module-landings)",
                "- [Browser labs](#browser-labs)",
                "- [License](#license)",
                "",
                "## Contents",
                "",
                "```text",
                "learn_digital/",
                "├── README.md",
                "├── LICENSE",
                "├── docs/",
                "│   ├── MODULES.md       # full module index (00–50)",
                "│   └── TWO_TRACKS.md    # Track A (workbook) vs Track B (browser)",
                "├── scripts/",
                "│   └── module.sh",
                "├── module00-intro/",
                "├── module01-radix-converter/",
                "│   ├── README.md · CHECKLIST.md · EXAMPLES.md",
                "│   ├── outline.yaml · transcript.md",
                "│   └── (optional) slides / video / assets/",
                "├── …",
                "└── module50-wrap/",
                "```",
                "",
                "Videos and decks are optional per module. Generate with the **module-slides** skill in the parent monorepo when ready.",
                "",
                "## Browse or clone",
                "",
                "- **Browser labs:** [https://universal-verification-methodology.github.io/learning/tools/](https://universal-verification-methodology.github.io/learning/tools/)",
                "- **Syllabus (parent):** [`syllabus.md` § learn_digital](https://github.com/universal-verification-methodology/learning/blob/main/syllabus.md#3-learn_digital)",
                "- **Clone this repo alone:**",
                "",
                "```bash",
                "git clone https://github.com/universal-verification-methodology/learn_digital.git",
                "cd learn_digital",
                "chmod +x scripts/*.sh",
                "./scripts/module.sh 01 --check",
                "```",
                "",
                "Then open [module00-intro/README.md](module00-intro/README.md).",
                "",
                "## Consume from the parent",
                "",
                "```bash",
                "git clone --recurse-submodules \\",
                "  git@github.com:universal-verification-methodology/learning.git",
                "ls courses/learn_digital",
                "```",
                "",
                "## Author: publish or update",
                "",
                "```bash",
                "cd courses/learn_digital",
                "# … edit module README / CHECKLIST / EXAMPLES / transcript …",
                "cd ../..",
                "python .cursor/skills/module-slides/scripts/transcript_to_outline.py \\",
                "  courses/learn_digital/moduleNN-slug",
                "bash .cursor/skills/module-slides/scripts/narrate_clips.sh \\",
                "  courses/learn_digital/moduleNN-slug",
                "```",
                "",
                "## Two learning tracks",
                "",
                "Every **lab** module documents both tracks. Intro/wrap have no lab. Details: [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md).",
                "",
                "| Track | Practice surface | Start here |",
                "|-------|------------------|------------|",
                "| **A — Workbook** | Paper / sketches + `EXAMPLES.md` | [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md) |",
                f"| **B — Browser lab** | Platform tools | [local]({LAB_BASE_LOCAL}/) · [live]({LAB_BASE_LIVE}/) |",
                "",
                f"Lab status snapshot: **{shipped} shipped** · **{planned} planned** (see [docs/MODULES.md](docs/MODULES.md)).",
                "",
                "## Module landings",
                "",
                "Full status table: **[docs/MODULES.md](docs/MODULES.md)**. Clusters: 00 intro · 01–10 numbers · 11–16 Boolean · 17–24 gates · 25–29 clocks · 30–34 FSM · 35–41 datapath · 42–47 memory · 48–49 integration · 50 wrap → Verilog.",
                "",
                "| Module | Landing |",
                "|--------|---------|",
                *landing,
                "",
                "## Browser labs",
                "",
                "Follow modules 01–49 in [docs/MODULES.md](docs/MODULES.md). Primary path: [radix-converter](https://universal-verification-methodology.github.io/learning/tools/radix-converter/) → number systems → Boolean → gates → clocks → FSM → datapath → memory → [handshake](https://universal-verification-methodology.github.io/learning/tools/handshake/) / [block-diagram](https://universal-verification-methodology.github.io/learning/tools/block-diagram/).",
                "",
                "## License",
                "",
                "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see [`LICENSE`](LICENSE).",
                "",
                "Concept path split from [`learn_digital_verilog`](https://github.com/universal-verification-methodology/learn_digital_verilog). Platform tools and the parent monorepo may carry additional notices.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_scripts() -> None:
    scripts = DST / "scripts"
    scripts.mkdir(exist_ok=True)
    (scripts / "module.sh").write_text(
        r"""#!/usr/bin/env bash
# Generic module helper: ./scripts/module.sh NN [--check|--demo|--help]
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
NN="${1:-}"
shift || true
if [[ -z "$NN" || "$NN" == "--help" ]]; then
  echo "Usage: $0 NN [--check|--demo|--help]"
  exit 0
fi
NN="$(printf '%02d' "$((10#$NN))")"
MOD_DIR="$(find "$ROOT" -maxdepth 1 -type d -name "module${NN}-*" | head -1)"
if [[ -z "$MOD_DIR" ]]; then
  echo "No module directory for $NN"
  exit 1
fi
ACTION="${1:---check}"
case "$ACTION" in
  --check)
    echo "Module $NN self-check (Track A environment)"
    echo "Module dir: $MOD_DIR"
    command -v bash >/dev/null && echo "[OK] bash"
    [[ -f "$MOD_DIR/EXAMPLES.md" ]] && echo "[OK] EXAMPLES.md" || echo "[INFO] no EXAMPLES.md"
    [[ -f "$MOD_DIR/CHECKLIST.md" ]] && echo "[OK] CHECKLIST.md"
    echo "[INFO] Track B lab link is in README.md"
    ;;
  --demo)
    echo "Demo: open $MOD_DIR/EXAMPLES.md and README.md"
    ;;
  *)
    echo "Unknown option: $ACTION"
    exit 1
    ;;
esac
""",
        encoding="utf-8",
    )
    (scripts / "README.md").write_text(
        """# Scripts

| Script | Purpose |
|--------|---------|
| `module.sh NN` | `--check` / `--demo` for module number `NN` |
| `_scaffold_course.py` | Regenerate course stubs from syllabus (authors) |

```bash
chmod +x scripts/*.sh
./scripts/module.sh 01 --check
```
""",
        encoding="utf-8",
    )


def write_license() -> None:
    src = COURSES / "learn_unix" / "LICENSE"
    dst = DST / "LICENSE"
    if src.exists():
        dst.write_text(src.read_text(encoding="utf-8").replace("learn_unix", "learn_digital"), encoding="utf-8")
    else:
        dst.write_text(
            "Creative Commons Attribution 4.0 International (CC BY 4.0)\n\n"
            "Copyright (c) The learn_digital contributors.\n\n"
            "https://creativecommons.org/licenses/by/4.0/\n",
            encoding="utf-8",
        )


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    write_license()
    write_course_readme()
    write_docs_index()
    write_scripts()
    for num, slug, kind, title, lab_id, status in MODULES:
        print(f"module{num:02d}-{slug} …")
        write_module_readme(num, slug, kind, title, lab_id, status)
        write_checklist(num, slug, kind, title, lab_id)
        write_examples_md(num, slug, kind, title)
        write_outline_transcript(num, slug, kind, title, lab_id)
    print("Done:", DST)


if __name__ == "__main__":
    main()
