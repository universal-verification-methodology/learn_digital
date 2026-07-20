# Module 17 — Gate composer

**Module id:** module17-gate-composer  
**Lab:** gate-composer  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — Gate composer

Boolean functions become gate networks—AND, OR, NOT, and friends wired together. The composer evaluates your net against a truth table row by row. Start simple: one AND for F equals A and B. Then build XOR, majority, mux, or full-adder bits from the same palette. This module makes compose and verify concrete.

## Slide 2 — Wire, probe, check

Place gates, connect inputs A through D, and read output F on every row. NAND is NOT of AND; XOR is one when inputs differ. A two-to-one mux selects B or C under A. Full-adder sum is A xor B xor Cin; carry-out is majority. The truth table is the judge—if every row matches, the net is correct.

## Slide 3 — Browser lab

![Gate composer starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge panel, the gate canvas and net list, and the truth-table probe. Load the starter—a single AND for F equals A and B. Confirm row one-one is the only F equals one. Pick a challenge like XOR or majority and add gates until all rows pass. Use Check when the table looks done.

## Slide 4 — Workbook practice

In the workbook track, sketch a two-input XOR from AND, OR, and NOT—or from NAND only if you know the pattern. Draw a three-input majority gate net. Write the half-adder sum and carry as gate names. Name one pitfall: a net that works on three rows but fails on the fourth.

## Slide 5 — Pitfalls to watch

Do not leave inputs floating—every gate input must be tied. Reusing the wrong polarity breaks active-high logic. And remember: the browser lab is literacy. Real RTL still needs synthesis, timing, and test vectors beyond one truth table.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, draw one small gate net and label wires. When you are ready, take the short quiz, then continue to mux and decoder.
