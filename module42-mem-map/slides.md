---
marp: true
title: RAM / ROM map
paginate: true
---

# RAM / ROM map

Memory maps connect an address bus to stored words

---

## DE AD BE EF starter
- Starter: sixteen-by-eight RAM loaded from a readmemh-style dump
- At address zero: hex DE, then AD, BE, EF
- Read address zero gives data DE
- Read address three gives EF
- The grid shows every cell with at-sign and hex value
- Switch to ROM and try a write, the status reports blocked

---

## Browser lab
![Memory map starter](assets/lab-starter.png)

---

## Workbook practice
- On paper, draw a sixteen-word memory map with addresses zero through F
- Label starter bytes DE AD BE EF at zero through three
- Explain what at-sign zero A means in a readmemh file
- Tabulate RAM versus ROM: read allowed, write allowed, init method
- Name one pitfall: confusing byte address order with big-endian multi-byte layout elsewhere

---

## Pitfalls to watch
- Do not assume ROM never changes, init load still programs the image in this lab
- At-sign sets address; following bytes fill upward sequentially
- Address bits are log two of depth, sixteen words need four bits, not eight
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, read addr zero and three, then try a ROM-blocked write
- On paper, sketch one readmemh dump with at-sign and four data bytes
- When you are ready, take the short quiz, then continue to FIFO pointers

