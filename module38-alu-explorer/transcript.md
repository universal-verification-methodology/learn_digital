# Module 38 — ALU explorer

**Module id:** module38-alu-explorer  
**Lab:** alu-explorer  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — ALU explorer

An arithmetic logic unit takes two operands, an opcode, and produces a result plus condition flags. Opcode selects the function—add, subtract, AND, OR, XOR, shift, compare. The datapath is shared; control wires pick which hardware runs. Flags summarize the outcome: Z when Y is zero, N from the MSB, C for carry or borrow, V for signed overflow on add or sub. This module steps a four-bit ALU and reads flags after each operation.

## Slide 2 — ADD five plus three starter

Starter: four-bit ADD, A equals five, B equals three. Result Y is one-zero-zero-zero binary—eight unsigned, minus eight signed in four bits because the MSB is set. Flags: Z zero, N one, C zero, V zero. Switch opcode to SUB, AND, or SLT and watch Y and flags change. On ADD, C equals one means unsigned carry out. On SUB, C equals one means no borrow. V lights up when signed add or sub overflows the representable range.

## Slide 3 — Browser lab

![ALU explorer starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the opcode grid, the A and B bit rows, and the Y plus Z-N-C-V flag strip. Load the starter—ADD with five and three. Toggle bits, change width, try SLT versus SLT.S for signed compare. Use Check when a challenge looks done.

## Slide 4 — Workbook practice

In the workbook track, compute four-bit ADD five plus three and list Z, N, C, V. Do SUB three minus five and explain C equals zero. AND twelve with three for zero and Z equals one. Explain when unsigned SLT and signed SLT.S disagree on fifteen versus one. Name one pitfall: reading C as signed overflow instead of V.

## Slide 5 — Pitfalls to watch

Do not mix unsigned carry with signed overflow—C and V mean different things. N is MSB of result, not a separate sign register. Compare ops return zero or one in Y, not a full difference. And remember: the browser lab is literacy. Real ALUs still need decode, timing, and ISA-specific flag rules.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, fill one opcode row with Y and flags. When you are ready, take the short quiz, then continue to carry-select adder.
