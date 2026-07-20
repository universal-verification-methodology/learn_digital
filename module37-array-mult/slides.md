---
marp: true
title: Array multiplier
paginate: true
---

# Array multiplier

Unsigned multiply builds partial products from every bit pair

---

## Five times three starter
- Starter: four-bit unsigned A equals five, B equals three
- Five is zero-one-zero-one, three is zero-zero-one-one
- Partial row for B-zero is five; row for B-one shifted left is ten
- Four AND cells are one in the grid
- Add the partials and the product is fifteen, binary zero-zero-one-one-one-one
- Product bit zero is A-zero AND B-zero only

---

## Browser lab
![Array multiplier starter](assets/lab-starter.png)

---

## Workbook practice
- In the workbook track, draw the AND grid for three-bit two times three
- Write partial row zero and row one with shifts
- Compute product bit zero by hand
- Explain why N-bit times N-bit needs two-N bits
- Name one pitfall: forgetting the left shift on each B-j row

---

## Pitfalls to watch
- Do not confuse the AND grid with the final sum, adders still reduce the rows
- Signed multiply needs Booth or similar, not this unsigned array alone
- Area and delay scale with width; real chips use Wallace trees or Booth
- And remember: the browser lab is literacy
- Real RTL still needs pipelining and signed/unsigned rules

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On paper, sketch one partial row and one shifted row
- When you are ready, take the short quiz, then continue to the ALU explorer

