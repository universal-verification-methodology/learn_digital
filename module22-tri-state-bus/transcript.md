# Module 22 — Tri-state / bus

**Module id:** module22-tri-state-bus  
**Lab:** tri-state-bus  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — Tri-state / bus

A shared bus lets several drivers connect to one wire—but only one should drive at a time. With enable off, the driver is high-Z, disconnected from the net. With enable on, it drives zero or one. No active driver means float Z, unless a pull-up or pull-down resistor defines idle level. Two enabled drivers with different data fight and the bus reads X. This module makes resolution rules concrete.

## Slide 2 — Enable, float, fight

Starter case: driver A enabled with data one, B and C off—the bus is one. Turn all enables off with no pull and the bus is Z. Enable B with zero while A still drives one and you get contention X. Two drivers on the same value may still show that bit, but overlapping enables is unsafe practice. Safe protocol: exactly one enable high—often one-hot output-enable in real designs.

## Slide 3 — Browser lab

![Tri-state bus starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge panel, the driver toggles and bus readout, and the schematic. Load the starter—only A drives one, bus equals one. Try all off for Z, force contention, or set pull-up on a float. Hit Explain resolution to see the verdict trace. Use Check when a challenge looks done.

## Slide 4 — Workbook practice

In the workbook track, fill a small table: all off, one driver on, two drivers agree, two drivers fight. Sketch three tri-state buffers on one bus line with enable pins. With all enables low and pull-up on, what is the bus? Name one pitfall: enabling two drivers at once on an external bus.

## Slide 5 — Pitfalls to watch

Do not treat multi-drive same value as safe—it still violates one-driver discipline. Internal FPGA fabrics often prefer muxes over tri-state. And remember: the browser lab is literacy. Real boards still need OE timing, bus holders, and protocol rules beyond this toy resolver.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, draw one bus with two drivers and label Z and X cases. When you are ready, take the short quiz, then continue to barrel shifter.
