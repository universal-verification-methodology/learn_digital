---
marp: true
title: Logic hazards
paginate: true
---

# Logic hazards

Combinational logic can glitch when inputs change

---

## One input moves, paths differ
- Hazard analysis usually changes one input at a time
- Different path delays let one SOP term drop before another picks up
- A consensus term that bridges adjacent cubes, like B C here, can cover the gap
- Equal delays can hide the glitch in simulation but not in silicon

---

## Browser lab
![Logic hazards starter](assets/lab-starter.png)

---

## Workbook practice
- In the workbook track
- Write the consensus term B C by hand
- Name static-one versus static-zero from the dip or spike direction
- Note one pitfall: assuming equal gate delays means no hazard in real hardware

---

## Pitfalls to watch
- Do not confuse a hazard with wrong logic
- Cover terms must actually bridge the risky transition
- And remember: the browser lab is literacy
- Real designs still need timing analysis

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On paper, identify one static hazard and one consensus fix
- When you are ready, take the short quiz, then continue to gate composer

