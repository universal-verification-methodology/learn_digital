---
marp: true
title: Reset timelines
paginate: true
---

# Reset timelines

Reset puts a flip-flop into a known state, usually zero when rst_n is low

---

## Mid-cycle, edge, release
- Starter scenario: drive D to one, take a posedge so both q_sync and q_async become one
- Assert rst_n low mid-cycle, the async flop clears immediately
- At a posedge with rst_n still low, both clear
- Release rst_n high, then capture new data on a later edge
- A short mid-cycle pulse may be ignored by sync reset if it ends before the sampling edge

---

## Browser lab
![Reset timelines starter](assets/lab-starter.png)

---

## Workbook practice
- In the workbook track, sketch clk, rst_n
- Write the always block for each style
- For rst_n low at posedge, do both FFs end at zero?
- Name one pitfall: releasing async reset too close to a clock edge without recovery time

---

## Pitfalls to watch
- Do not assume sync and async behave the same off the edge
- Rst_n naming implies active low, not “never reset.” And remember
- Real SoCs still need reset trees, CDC

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On paper, draw one mid-cycle reset wave
- When you are ready, take the short quiz, then continue to clock enable versus gated clock

