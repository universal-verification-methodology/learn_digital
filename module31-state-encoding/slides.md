---
marp: true
title: State encoding
paginate: true
---

# State encoding

An FSM has abstract states S0, S1, S2, but silicon stores bit patterns in flip-flops

---

## Hamming distance and flips
- Starter: four states in binary, two flip-flops
- Click S1 to S2 and Hamming distance is two, both bits flip
- That matters because combinational decode can briefly see illegal intermediate codes
- Switch to one-hot
- Switch to Gray: ring steps often have Hamming one
- Yellow rows in the arc table flag multi-bit transitions

---

## Browser lab
![State encoding starter](assets/lab-starter.png)

---

## Workbook practice
- In the workbook track
- Sketch one-hot for three states
- Explain why five states in three binary bits leaves unused codes
- Name one pitfall: multi-bit flips glitching state decode

---

## Pitfalls to watch
- Do not assume binary is always best, compact codes can hazard decode
- One-hot costs more FFs but simplifies “are we in S2?” checks
- Unused binary codes need a default next-state, not hope
- And remember: the browser lab is literacy
- Real RTL still needs synthesis encoding hints and safe illegal-state recovery

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On paper, draw one binary multi-flip arc and one Gray single-flip step
- When you are ready, take the short quiz, then continue to the sequence detector

