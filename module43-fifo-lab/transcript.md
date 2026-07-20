# Module 43 — FIFO pointers

**Module id:** module43-fifo-lab  
**Lab:** fifo-lab  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — FIFO pointers

A FIFO buffer decouples producer and consumer with first-in first-out order—the oldest entry is read next. A write pointer selects the next push slot; a read pointer selects the next pop slot. Both wrap modulo depth. Empty means count equals zero; full means count equals depth. Push while full is blocked; pop while empty is blocked. This lab uses a count-based synchronous model in one clock domain.

## Slide 2 — Push A5 starter

Starter: depth-four empty FIFO. Push hex A5. Count becomes one, empty clears, write pointer advances to one, read pointer stays at zero. Data A5 sits in slot zero. Pop once returns A5, count returns to zero, read pointer advances to one. Fill with four pushes to set full; a fifth push logs blocked FULL. Push eleven then twenty-two—pop must return eleven first.

## Slide 3 — Browser lab

![FIFO lab starter](assets/lab-starter.png)

In the browser lab, set depth four or eight and enter push data in hex. Push and Pop update the slot row with WR and RD markers. Flags show empty, full, count, almost full, and almost empty. The event log records each operation or block. Try fill, blocked push, and drain to empty.

## Slide 4 — Workbook practice

On paper, draw a depth-four FIFO with wr and rd pointers. Trace push A5, then pop A5, listing count and pointers after each step. Show what happens when wr wraps after four pushes. Tabulate empty versus full conditions. Name one pitfall: popping when empty or pushing when full.

## Slide 5 — Pitfalls to watch

Do not confuse wr equals rd with empty—in count-based designs, count is the source of truth. Some pointer-only FIFOs leave one slot spare to detect full. Async clock domains need Gray-coded pointers and synchronizers—beyond this sync lab. And remember: real FIFOs add clock enables, reset, and almost-full thresholds for flow control.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, push A5, pop it back, then fill and drain once. On paper, trace FIFO order for two pushes and one pop. When you are ready, take the short quiz, then continue to cache walk.
