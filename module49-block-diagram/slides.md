---
marp: true
title: System integration
paginate: true
---

# System integration

A chip is more than gates, it is blocks wired together

---

## Starter mini CPU
- Starter preset: CPU, ALU, RegFile, and Memory on the canvas
- Cpu rf_ctrl enables the register write
- Four links are still missing
- Click an output port, then a matching input, until validation turns green

---

## Browser lab
![Block diagram starter](assets/lab-starter.png)

---

## Workbook practice
- On paper, sketch four blocks, CPU, ALU, RegFile, and Memory, and label their ports
- Draw the five datapath wires from the starter
- Add the four CPU-to-memory links and name each signal
- Explain why addr cannot wire to a data port in this teaching model
- Optionally sketch how a bus sits between CPU and memory instead of a direct link

---

## Pitfalls to watch
- Do not wire output to output or input to input, direction matters
- Types must match; the lab rejects addr-to-data mistakes
- One input accepts only one driver; a new wire replaces the old one
- This is a conceptual integration sketch, not a full SoC generator or place-and-route tool
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish the starter until integration passes, then load the bus preset
- On paper, list the nine required edges for the complete mini system
- When you are ready

