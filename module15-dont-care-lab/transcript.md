# Module 15 — Don’t-care minimization

**Module id:** module15-dont-care-lab  
**Lab:** dont-care-lab  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — Don’t-care minimization

Some input combinations never happen—or the output does not matter when they do. Mark them X in the table. Minimize over ones you must cover; treat X as zero or one if it helps. That can drop literals and terms compared to ignoring X. This module makes with-X versus without-X covers concrete.

## Slide 2 — ON, OFF, and optional

Every product term must cover all ON minterms. Cubes must never include an OFF row. Don’t-care rows are optional—you choose zero or one to enlarge groups. Sigma-m with d lists minterms and don’t-cares. Compare covers side by side to see the shrink.

## Slide 3 — Browser lab

![Don’t-care lab starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge panel, the F column with blue X cells, and Minimize or Compare controls. Load the starter—ON at zero, two, five, and seven, X at one and three. Minimize with X and check you get A-prime plus C. Compare with and without X to see A-prime C-prime plus AC shrink to two terms. Use Check when a challenge looks done.

## Slide 4 — Workbook practice

In the workbook track, take the starter pattern by hand. Write the ignore-X SOP, then regroup using X at one and three. Confirm the with-X form has fewer terms. Try a two-variable preset with one ON and one X. Name one pitfall: treating X as OFF by default and missing a smaller cover.

## Slide 5 — Pitfalls to watch

Do not let a group cover an OFF row. X is not “don’t optimize”—it is “pick whichever helps.” And remember: the browser lab is literacy. Real designs still need a spec for what is truly unreachable versus merely unused.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, minimize one small table with at least one X. When you are ready, take the short quiz, then continue to logic hazards.
