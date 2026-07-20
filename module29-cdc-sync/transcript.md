# Module 29 — CDC / 2-FF sync

**Module id:** module29-cdc-sync  
**Lab:** cdc-sync  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — CDC / 2-FF sync

When a signal crosses from one clock domain to another, timing is not guaranteed—the source can change while the destination flop is sampling. That is clock-domain crossing, or CDC. The first flop in the destination domain may go metastable, stuck between zero and one. A two-flop synchronizer gives one extra cycle to settle: q1 samples async_in, q2 samples q1, and dst logic uses q2—not q1. This module shows why that chain matters.

## Slide 2 — Safe, unsafe, multi-bit

Starter: two-FF mode with async_in toggling and clk_dst stepping. After a near-edge sample, q1 may show M for metastable; step again and q2 settles to a clean zero or one. One-FF mode is unsafe—sync_out comes straight from q1. Multi-bit misuse warns you: a bus cannot ride a classic two-FF chain; use Gray code, handshake, or an async FIFO instead. Never fan q1 into combinational logic in the dst domain.

## Slide 3 — Browser lab

![CDC sync starter](assets/lab-starter.png)

In the browser lab, look at the synchronizer chain diagram, the async-q1-q2 wave strip, and the RTL for each style. Load the starter—two-FF single-bit sync. Try arm near-edge sample then step, or run the demo toggle-risk-two-steps. Switch to one-FF or multi-bit misuse to see the warnings. Use Check when a challenge looks done.

## Slide 4 — Workbook practice

In the workbook track, draw async_in, q1, q2, and sync_out across two dst clock edges. Write the always block for a two-FF synchronizer. Explain why q2 is the safe output. Sketch what goes wrong with one flop or with an eight-bit bus through two flops. Name one pitfall: using q1 before it has settled.

## Slide 5 — Pitfalls to watch

Do not treat CDC as a timing exception you can ignore—metastability is probabilistic, not impossible. Two flops improve MTBF but do not make multi-bit buses safe. And remember: the browser lab is literacy. Real designs still need CDC constraints, synchronizer cells, and proper protocols for data paths.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, draw one two-FF settle wave and one multi-bit caution. When you are ready, take the short quiz, then continue to the FSM designer lab.
