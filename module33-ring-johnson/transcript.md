# Module 33 — Ring / Johnson

**Module id:** module33-ring-johnson  
**Lab:** ring-johnson  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — Ring / Johnson

A shift register with feedback becomes a counter without a binary adder. A ring counter feeds the MSB back into the LSB—the one-hot bit walks: zero-zero-zero-one becomes zero-zero-one-zero, and so on. Period N for N bits with one-hot init. A Johnson counter feeds inverted MSB—a twisted ring that visits two-N distinct states from all-zero. Same shift chain, different feedback tap. This module steps both and compares periods.

## Slide 2 — Ring walk starter

Starter: ring mode with one-hot pattern zero-zero-zero-one. Step once and the one moves to zero-zero-one-zero—feedback equals q-three, shift into q-zero. Four steps complete a full ring period back to zero-zero-zero-one. Switch to Johnson: load zero-zero-zero-zero, step eight times for the full two-N cycle. Watch the feedback box—plain q-three for ring, not-q-three for Johnson. Beware all-zero on a ring—it can lock with zero feedback forever.

## Slide 3 — Browser lab

![Ring Johnson starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the feedback chain diagram, the sequence strip, and the RTL snippet for each mode. Load the starter—ring one-hot zero-zero-zero-one. Step, run full ring period, or try Johnson eight states. Use Check when a challenge looks done.

## Slide 4 — Workbook practice

In the workbook track, write the always block for ring versus Johnson feedback. List four ring states starting from zero-zero-zero-one. Count Johnson states for four bits—why two-N? Sketch what happens if a ring starts at all-zero. Name one pitfall: invalid init or illegal states without recovery.

## Slide 5 — Pitfalls to watch

Do not confuse display order—here q-three through q-zero is MSB left. Ring needs valid one-hot init; Johnson needs the right reset. Neither replaces a binary counter when you need full two-to-the-N counting. And remember: the browser lab is literacy. Real designs still need timing, enable, and illegal-state handling.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, draw one ring walk and one Johnson feedback inversion. When you are ready, take the short quiz, then continue to LFSR and PRBS.
