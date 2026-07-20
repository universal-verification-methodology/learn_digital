---
marp: true
title: Valid/ready handshake
paginate: true
---

# Valid/ready handshake

A streaming beat moves when source and sink agree in the same cycle

---

## Starter beat
- Starter preset: both assert on cycle zero
- Valid and ready are one, data is hex A5, and fire is one, one beat transfers immediately
- The wave table shows eight cycles; click valid or ready cells to toggle
- Step through cycles to see when fire lights up
- Try source-stall preset, valid rises late while ready waits
- Try sink-stall, valid held high until ready finally rises

---

## Browser lab
![Handshake starter](assets/lab-starter.png)

---

## Workbook practice
- On paper, draw valid and ready waveforms for one successful beat and one sink stall
- Write the fire equation in words
- Tabulate four cycles showing valid, ready, and whether a transfer happens
- Explain what the source should do while valid is high and ready is still low
- Name one place you might see this handshake style on chip

---

## Pitfalls to watch
- Do not assume valid alone moves data, both sides must agree
- Do not toggle data while waiting for ready; stability matters for real RTL
- Avoid combinational loops where ready depends on valid in a way that creates a cycle
- This lab is conceptual timing literacy, not a full protocol checker or VIP
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, run together, source-stall, and sink-stall presets and count transfers
- On paper, sketch a two-beat back-to-back burst
- When you are ready, take the short quiz, then continue to the block-diagram integrator

