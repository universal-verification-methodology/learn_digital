---
marp: true
title: Endian packing
paginate: true
---

# Endian packing

The same integer can sit in memory two ways

---

## Unpack, pack, swap
- Unpack splits a word into bytes in address order for the chosen mode
- Pack builds the word from bytes at plus zero through plus three
- Byte-swap reverses the four bytes in the word
- Compare LE versus BE when you want the side-by-side picture
- BE puts one-two first

---

## Browser lab
![Endian lab starter](assets/lab-starter.png)

---

## Workbook practice
- In the workbook track, take word one-two-three-four-five-six-seven-eight
- Write LE and BE byte order at addresses plus zero through plus three
- Pack LE bytes A-A B-B C-C D-D and check you get D-D C-C B-B A-A
- Note one pitfall: assuming host endian always matches the wire or the spec

---

## Pitfalls to watch
- Do not confuse byte order with bit order inside a byte
- Mixing LE and BE across a bus without conversion corrupts multi-byte fields
- And remember: the browser lab is literacy
- Real SoCs still need explicit endian policy on DMA, registers, and network frames

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On paper, unpack one word both ways and pack one byte sequence
- When you are ready, take the short quiz, then continue to truth tables

