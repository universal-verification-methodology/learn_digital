# Module 11 — Truth tables

**Module id:** module11-truth-table  
**Lab:** truth-table  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — Truth tables

A truth table lists every input combination and the output F. Two inputs give four rows; three inputs give eight. It is the ground truth for gates, muxes, and adder bits before you write HDL. This module makes fill, check, and read a table concrete.

## Slide 2 — Every row, one function

Each row is one minterm index from all zeros through all ones. AND is one only when every input is one. OR is one when any input is one. XOR is one when inputs differ. Challenges in the lab ask you to match a described function—majority, parity, mux select, full-adder sum. Edit F in the table or the expression; both can stay in sync.

## Slide 3 — Browser lab

![Truth table starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge panel, the input and F columns, and expression or fill controls. Load the starter for F equals A and B on two variables. Step through the four rows and confirm F is one only on the one-one row. Pick a challenge, fill the table or edit the expression, then Check. Export SOP or POS when you want the sum-of-products picture. Explore a few; no full tour needed.

## Slide 4 — Workbook practice

In the workbook track, build a two-input AND and XOR table by hand. Add a three-input majority row set. Say how many rows you need for four variables. Name one pitfall: stopping at three rows when you have three inputs—that misses half the table.

## Slide 5 — Pitfalls to watch

Do not skip rows or duplicate an index. X in a cell means don’t-care, not “pick any answer.” And remember: the browser lab is literacy. Real verification still needs exhaustive or constrained cases beyond one hand table.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, write one full table and circle the minterms where F is one. When you are ready, take the short quiz, then continue to Boolean laws.
