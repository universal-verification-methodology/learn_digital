# Module 25 — Clock-edge stepper

**Module id:** module25-clock-stepper  
**Lab:** clock-stepper  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — Clock-edge stepper

Sequential logic does not change on every input wiggle—it samples on a clock edge. A D flip-flop copies D into Q on each rising edge of clk. Poke the input first, then step the clock—same rhythm as the HDL simulator toolbar. Registers, counters, and shift chains are all edge-triggered blocks built from this idea. This module makes posedge stepping concrete.

## Slide 2 — Poke, edge, capture

Starter lab: D flip-flop with a toggling clock. Set D to one, apply poke, then advance to posedge clk—Q becomes one. Set D to zero and take another posedge—Q returns to zero. Enable registers only capture when EN is high. Counters increment on edge after reset clears. A pipeline needs two edges before the second stage sees your bit. The truth table records each poke and each edge in time order.

## Slide 3 — Browser lab

![Clock stepper starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge panel, the signal readout and truth table, and the poke fields with posedge button. Load the starter—D flip-flop, poke D equals one, then posedge clk. Switch presets for enable, counter, or shift register. Use Check when a challenge looks done.

## Slide 4 — Workbook practice

In the workbook track, sketch a D flip-flop timing diagram: D changes, then posedge, then Q updates. For an enable register with EN equals zero, say whether Q changes on posedge. Draw two pipeline stages and label the one-cycle delay. Name one pitfall: changing D and expecting Q to move before the clock edge.

## Slide 5 — Pitfalls to watch

Do not confuse level-sensitive latches with edge-triggered flops—this lab is edge-triggered. Reset and enable matter on the same edge as data. And remember: the browser lab is literacy. Real designs still need setup, hold, and clock-domain crossing rules beyond manual stepping.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, draw one posedge capture wave. When you are ready, take the short quiz, then continue to setup and hold.
