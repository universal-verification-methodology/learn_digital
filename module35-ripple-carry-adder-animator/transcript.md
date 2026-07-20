# Module 35 — Ripple-carry adder

**Module id:** module35-ripple-carry-adder-animator  
**Lab:** ripple-carry-adder-animator  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — Ripple-carry adder

Adding multi-bit numbers means chaining full adders: each stage takes A, B, and carry in, and produces sum and carry out. Sum is A XOR B XOR Cin. Cout is one when at least two inputs are one. In a ripple-carry adder, Cout of bit i minus one feeds Cin of bit i—carry ripples from LSB toward MSB. Simple to build, but worst-case delay grows with bit width. This module steps a four-bit ripple and watches carry propagate.

## Slide 2 — Five plus three starter

Starter: four-bit A equals five, B equals three, Cin zero. Step carry from bit zero: LSBs are both one, so S0 is zero and Cout is one into bit one. Keep stepping until all four stages reveal—sum eight, Cout zero. Try fifteen plus one to see unsigned wrap: sum zero, Cout one. The delay note reminds you: critical path is about N full-adder carry delays. Wide adders use lookahead instead.

## Slide 3 — Browser lab

![Ripple-carry adder starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the FA chain with carry arrows, the step counter, and the sum and Cout strip. Load the starter—four-bit five plus three. Press Step carry to ripple LSB first, or Show all to reveal the full add. Toggle Cin for subtract-style plus-one. Use Check when a challenge looks done.

## Slide 4 — Workbook practice

In the workbook track, draw one full adder with sum and Cout equations. Ripple four bits for five plus three by hand. Explain why bit one waits on bit zero’s Cout. Sketch fifteen plus one in four bits. Name one pitfall: treating Cout as signed overflow instead of unsigned wrap.

## Slide 5 — Pitfalls to watch

Do not assume ripple is fast at sixty-four bits—carry must walk the chain. Half adders have no Cin; full adders do. Cin equals one is common for two’s-complement subtract. And remember: the browser lab is literacy. Real RTL still needs timing analysis and often carry-lookahead or prefix adders.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, draw one ripple step with Cout feeding the next Cin. When you are ready, take the short quiz, then continue to carry-lookahead generate and propagate.
