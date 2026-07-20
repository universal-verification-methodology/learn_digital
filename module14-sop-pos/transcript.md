# Module 14 — SOP ↔ POS

**Module id:** module14-sop-pos  
**Lab:** sop-pos  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — SOP and POS

Sum-of-products ORs minterms where F is one. Product-of-sums ANDs maxterms where F is zero. Same function, two canonical views—dual of each other. Sigma-m lists minterm indices; pi-M lists maxterm indices. This module makes derive, compare, and read both forms concrete.

## Slide 2 — Minterms and maxterms

A minterm is a product true on exactly one row—like A-prime B for m zero on two variables. A maxterm is a sum false on exactly one row—like A plus B for M zero. Canonical SOP lists every one row; canonical POS lists every zero row. That full form is not always minimal—you still simplify with grouping or laws.

## Slide 3 — Browser lab

![SOP POS starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge panel, the F column and derived SOP or POS, and Derive or Explain controls. Load the starter XOR—F is one on rows one and two. Derive SOP and POS and check POS includes M zero and M three. Try preset AND or OR, or switch to three variables. Use Check when a challenge looks done.

## Slide 4 — Workbook practice

In the workbook track, take two-variable XOR. Write canonical SOP from rows one and two, and POS from rows zero and three. For AND, note only m three is one. For all zeros, SOP is zero; for all ones, both forms collapse to one. Name one pitfall: assuming canonical SOP is already minimal.

## Slide 5 — Pitfalls to watch

Do not mix SOP and POS rules—SOP uses F equals one, POS uses F equals zero. Minterm m zero and maxterm M zero are different shapes. And remember: the browser lab is literacy. Real synthesis picks the form that fits your gate library and timing.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, write SOP and POS for one small table. When you are ready, take the short quiz, then continue to don’t-care minimization.
