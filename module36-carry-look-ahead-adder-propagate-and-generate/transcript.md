# Module 36 — Carry-lookahead G/P

**Module id:** module36-carry-look-ahead-adder-propagate-and-generate  
**Lab:** carry-look-ahead-adder-propagate-and-generate  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — Carry-lookahead G/P

Ripple-carry waits for each Cout before the next Cin. Carry-lookahead computes generate and propagate per bit first. Generate G equals A and B—this bit forces a carry out. Propagate P equals A XOR B—the bit passes Cin through when G is zero. Recursive rule: C out equals G plus P times C in. Sum is P XOR C in. Expand C two, C three, and so on from G, P, and C zero—all carries in parallel, not one long ripple. This module reads the G/P table and steps through expanded equations.

## Slide 2 — Five plus three starter

Starter: four-bit A equals five, B equals three, C zero zero. Bit zero: both inputs one, so G zero is one and P zero is zero—G forces C one to one even with C zero zero. Step to reveal C one, C two, and the expanded forms—C two includes G one plus P one dot G zero. Full reveal: sum eight, Cout zero. If G is one, carry out is one regardless of Cin. If G is zero and P is one, carry passes. If both are zero, carry is killed.

## Slide 3 — Browser lab

![Carry-lookahead starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the G and P table per bit, the expanded carry equations, and the sum strip. Load the starter—four-bit five plus three. Reveal carries one at a time or Show all. Compare with ripple: more lookahead logic, shorter carry delay. Use Check when a challenge looks done.

## Slide 4 — Workbook practice

In the workbook track, write G, P, and C one for bit zero of five plus three. Expand C two symbolically from G one, P one, G zero, and C zero. Explain generate versus propagate in one sentence each. Sketch why CLA trades area for speed versus ripple. Name one pitfall: confusing G with P or forgetting sum uses P XOR C.

## Slide 5 — Pitfalls to watch

Do not treat expanded equations as magic—each term is a real AND-OR path. G equals one always wins; P equals zero kills carry regardless of Cin. Wide adders use prefix trees, not one giant flat expansion. And remember: the browser lab is literacy. Real RTL still needs sensible grouping and timing on carry paths.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, write one recursive C equation and one expanded C two. When you are ready, take the short quiz, then continue to the array multiplier.
