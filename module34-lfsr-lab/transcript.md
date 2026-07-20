# Module 34 — LFSR / PRBS

**Module id:** module34-lfsr-lab  
**Lab:** lfsr-lab  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — LFSR / PRBS

A linear feedback shift register is a shift chain with XOR taps feeding the next MSB. Each clock, feedback XORs selected bits, shifts in at the top, and the LSB falls out—that bit stream is PRBS, pseudo-random binary sequence. Pick a maximal polynomial and a nonzero seed and you visit every nonzero state before repeating. Period is two-to-the-n minus one. LFSRs show up in scramblers, built-in self-test, and link training. This module steps a Fibonacci LFSR and measures period.

## Slide 2 — Maximal starter

Starter: four-bit maximal polynomial x-four plus x plus one, seed zero-zero-zero-one. Step and watch feedback XOR the taps, the register shift, and PRBS bits accumulate. Measure period—you should see fifteen before the seed returns. Try the short polynomial x-four plus x-squared plus one for contrast—period under fifteen. Load all-zero and see the lock warning: feedback stays zero forever. Never seed all-zero on a real LFSR.

## Slide 3 — Browser lab

![LFSR lab starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the XOR feedback chain with tap highlights, the state sequence strip, and the PRBS stream readout. Load the starter—maximal four-bit, seed zero-zero-zero-one. Step, measure period, or compare short versus maximal polynomials. Use Check when a challenge looks done.

## Slide 4 — Workbook practice

In the workbook track, write the Fibonacci update for a four-bit LFSR with taps at MSB and LSB. Compute period for n equals four with a maximal poly. Sketch why all-zero is forbidden. Explain one use case: PRBS for a serial link or BIST pattern. Name one pitfall: non-maximal polynomial or bad seed choice.

## Slide 5 — Pitfalls to watch

Do not confuse PRBS with true random—it repeats after the period. Maximal taps matter; a wrong polynomial shortens the cycle. All-zero locks the register. And remember: the browser lab is literacy. Real designs still need tap polynomials from tables, seed logic, and synchronization on receive.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, draw one LFSR step with XOR feedback. When you are ready, take the short quiz, then continue to the ripple-carry adder animator.
