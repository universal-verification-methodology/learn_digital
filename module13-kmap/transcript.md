# Module 13 — K-maps

**Module id:** module13-kmap  
**Lab:** kmap  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — K-maps

A Karnaugh map lays truth-table ones on a grid so adjacent cells differ by one bit. Group the ones into pairs, quads, or octets—edges wrap. The result is a minimal sum-of-products without listing every row. This module makes fill, group, and read SOP concrete.

## Slide 2 — Adjacent ones, bigger groups

Two-variable maps use Gray order on both axes. Three and four variables add more cells but the same rule: circle the largest legal groups. A group of four drops two literals. Don’t-care X cells can join a group when they help. Pick the minimal SOP when the challenge asks—one term per group.

## Slide 3 — Browser lab

![K-map starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge panel, the Karnaugh map grid, and variable or fill controls. Load the starter—a two-variable XOR pattern. Toggle cells to match a prompt, or load a challenge map directly. Try a three-variable majority or a wrap quad on four variables. Use Check when the map or SOP pick looks done.

## Slide 4 — Workbook practice

In the workbook track, sketch a two-input XOR map by hand and write its SOP. On three variables, group ones for at least two of A, B, or C. Mark why top and bottom rows are neighbors on a four-var map. Name one pitfall: grouping only in a straight line and missing a wrap-around quad.

## Slide 5 — Pitfalls to watch

Do not treat diagonal cells as adjacent—they are not. A group must be a power-of-two size. And remember: the browser lab is literacy. Real logic minimization still needs consistent variable order and don’t-care specs from the design.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, draw one map and circle the groups. When you are ready, take the short quiz, then continue to SOP and POS.
