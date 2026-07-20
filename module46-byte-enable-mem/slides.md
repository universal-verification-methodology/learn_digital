---
marp: true
title: Byte-enable memory
paginate: true
---

# Byte-enable memory

A thirty-two-bit word RAM can update one byte at a time using byte-enable bits

---

## be equals 0001 starter
- Starter: four words by thirty-two bits
- Word zero is hex DDCCBBAA, bytes AA, BB, CC, DD little-endian
- Set addr zero
- Step clock: only byte zero changes from AA to fifty-five
- Word zero becomes DDCCBB55; BB, CC, DD unchanged
- Try be equals one-one-one-one for a full word, or zero-zero-one-one for a low halfword

---

## Browser lab
![Byte-enable memory starter](assets/lab-starter.png)

---

## Workbook practice
- On paper, draw word zero with four byte lanes
- Mark be equals zero-zero-zero-one and din byte zero equals fifty-five
- Show the word before and after partial write
- Tabulate be patterns
- Name one pitfall: confusing be bit order with big-endian byte numbering

---

## Pitfalls to watch
- Do not assume we equals one always writes the full word, check be
- Disabled lanes are not zeroed; they retain old values
- Little-endian means be zero is the least significant byte
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, run the starter step and confirm only byte zero patches
- On paper, sketch one partial write with be equals zero-zero-one-one
- When you are ready, take the short quiz, then continue to async FIFO Gray pointers

