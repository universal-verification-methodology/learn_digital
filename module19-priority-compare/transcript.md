# Module 19 — Priority & compare

**Module id:** module19-priority-compare  
**Lab:** priority-compare  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — Priority & compare

When several requests arrive at once, a priority encoder picks one winner and reports its index. Enable-in and enable-out let you cascade blocks. A comparator answers equal, greater-than, and less-than—but unsigned magnitude and signed two’s-complement order can disagree on the same bit pattern. This module makes both ideas concrete.

## Slide 2 — Winner, flags, cascade

High-index-first: if I zero and I two are both set, the winner is two. Low-index-first would pick zero instead—priority is a design choice. With all inputs zero and enable-in high, valid is zero and enable-out asserts for the next encoder in a chain. Compare four-bit A and B: unsigned treats every bit as magnitude; signed treats the MSB as sign. Same bits can yield A greater unsigned but A less signed.

## Slide 3 — Browser lab

![Priority compare starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge panel, the encoder or comparator diagram, and the input toggles. Load the starter—a four-input priority encoder, high-index-first, with I zero and I two set, so winner I two and Y equals two. Switch to compare mode and try a signed versus unsigned disagree case. Use Check when a challenge looks done.

## Slide 4 — Workbook practice

In the workbook track, for I one and I three both set, give the winner high-index-first and low-index-first. With enable-in high and no inputs active, state V and enable-out. For four-bit A equals fifteen and B equals one, say unsigned and signed relational results. Name one pitfall: assuming comparator flags match without checking signed mode.

## Slide 5 — Pitfalls to watch

Do not mix up priority direction—high versus low index first changes the answer. Enable-out is not “any input high”; it means no local winner while enable-in is on. And remember: the browser lab is literacy. Real buses still need timing, width agreement, and test vectors on both unsigned and signed views.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, sketch one priority case and one compare disagree case. When you are ready, take the short quiz, then continue to half and full adder.
