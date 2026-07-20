---
marp: true
title: FIFO pointers
paginate: true
---

# FIFO pointers

A FIFO buffer decouples producer and consumer with first-in first-out order, the oldest entry is read next

---

## Push A5 starter
- Starter: depth-four empty FIFO
- Push hex A5
- Count becomes one, empty clears, write pointer advances to one, read pointer stays at zero
- Data A5 sits in slot zero
- Pop once returns A5, count returns to zero, read pointer advances to one
- Fill with four pushes to set full; a fifth push logs blocked FULL

---

## Browser lab
![FIFO lab starter](assets/lab-starter.png)

---

## Workbook practice
- On paper, draw a depth-four FIFO with wr and rd pointers
- Trace push A5, then pop A5, listing count and pointers after each step
- Show what happens when wr wraps after four pushes
- Tabulate empty versus full conditions
- Name one pitfall: popping when empty or pushing when full

---

## Pitfalls to watch
- Do not confuse wr equals rd with empty
- Some pointer-only FIFOs leave one slot spare to detect full
- Async clock domains need Gray-coded pointers and synchronizers, beyond this sync lab
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, push A5, pop it back, then fill and drain once
- On paper, trace FIFO order for two pushes and one pop
- When you are ready, take the short quiz, then continue to cache walk

