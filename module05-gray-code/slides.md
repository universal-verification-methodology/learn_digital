---
marp: true
title: Gray code
paginate: true
---

# Gray code

Binary counts flip many bits at once, seven to eight is a noisy edge

---

## One-bit neighbors, convert carefully
- To encode binary to Gray, exclusive-or the value with itself shifted right by one
- Adjacent Gray codes differ by exactly one bit
- Do not do ordinary add or compare on Gray bits as if they were binary
- Async FIFOs prefer Gray pointers so only one bit is in flight across a synchronizer

---

## Browser lab
![Gray code starter](assets/lab-starter.png)

---

## Workbook practice
- In the workbook track, take width four
- Write binary zero through a few counts and the Gray code beside each
- Confirm each step flips one Gray bit
- Encode binary seven by hand with exclusive-or of the value and its right shift
- Note one pitfall: adding in Gray without decoding

---

## Pitfalls to watch
- Do not treat Gray as “just another binary.” Multi-bit binary transitions are exactly what
- And remember: the browser lab is literacy
- Real CDC and FIFO designs still depend on that single-bit property across clock domains

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On paper, build a short Gray table and one encode by hand
- When you are ready, take the short quiz, then continue to BCD

