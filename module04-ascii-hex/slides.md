---
marp: true
title: ASCII / hex dump
paginate: true
---

# ASCII / hex dump

Logs, ROMs, and memory dumps are often rows of hex with a printable side view

---

## Bytes, glyphs, and controls
- Printable ASCII typically starts at hex twenty, the space
- Newline is line feed, hex zero A
- A C-style string ends with NUL, hex zero zero
- When a dump cannot show a glyph, it prints a dot so the columns still line up
- Hex on the left and glyphs on the right are two views of the same bytes

---

## Browser lab
![ASCII hex dump starter](assets/lab-starter.png)

---

## Workbook practice
- In the workbook track, write a tiny dump by hand
- Encode the letters H and i, then a line feed, then O and K, then NUL
- Mark which offsets are printable and which would show as dots
- Name one RTL or bring-up pitfall

---

## Pitfalls to watch
- Do not assume every byte is a letter, controls and high bytes break that story
- Do not confuse hex “zero A” with the digit characters for one and zero
- And remember: the browser lab is literacy
- Real dumps from simulators and flash still use the same byte-to-glyph rules

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On paper, dump a short string with one control and one NUL
- When you are ready, take the short quiz, then continue to Gray code

