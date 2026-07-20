# Module 03 — Overflow / wrap

**Module id:** module03-overflow-wrap  
**Lab:** overflow-wrap  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — Overflow / wrap

Fixed-width math does not grow a bigger box when the answer is too big. The bits wrap, or—in signed math—you get overflow that is not the same as a carry flag. This module trains that distinction: what stores in the register versus what a flag is trying to tell you.

## Slide 2 — Wrap versus signed overflow

Unsigned wrap is modular arithmetic: results live modulo two to the width. Add fourteen and three in four bits and you store one, not seventeen. Signed overflow is different: the bit pattern may look “fine” as unsigned while the signed meaning is wrong—for example seven plus one at width four becomes minus eight. Carry and signed overflow are not the same question.

## Slide 3 — Browser lab

![Overflow wrap starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge panel, the operands A and B, and the width plus signed-versus-unsigned mode. Load the starter—four-bit unsigned, try fourteen plus three—and watch the wrap. Run a signed demo when the lab offers one. Use Check when a challenge looks done. Explore a few; no full UI tour needed here.

## Slide 4 — Workbook practice

In the workbook track, pick width four. On paper, add fourteen plus three unsigned and show why the stored result is one. Then try signed seven plus one and explain why that is overflow, not “just another wrap story.” Write one sentence on why free-running counters often rely on wrap on purpose, and one pitfall: treating carry as if it meant signed overflow.

## Slide 5 — Pitfalls to watch

Do not assume saturation—clamping to min or max—is the same as wrap; most simple RTL adders wrap unless you build saturation. Do not ignore width when you “check the answer in your head” with unlimited decimal. And remember: the browser lab is literacy. Waveforms still show the wrapped bits, not the mathematical ideal.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, work one unsigned wrap and one signed overflow example. When you are ready, take the short quiz, then continue to ASCII and hex dump literacy.
