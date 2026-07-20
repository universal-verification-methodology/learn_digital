# Module 23 — Barrel shifter

**Module id:** module23-barrel-shifter  
**Lab:** barrel-shifter  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — Barrel shifter

A barrel shifter moves every bit in one operation—logical left, logical right, arithmetic right, or rotate. For eight bits you need three mux stages, not seven serial shifts. Each amount bit enables a power-of-two stage: one, two, or four positions. Amount three fires stages one and two together—that is one plus two, not three times one. This module makes stage selection and modes concrete.

## Slide 2 — Stages, modes, result

Starter: hex D two is one-one-zero-one-zero-zero-one-zero. Logical left by three enables amount bits one and two. After stage one you get one-zero-one-zero-zero-one-zero-zero; after stage two the result is one-zero-zero-one-zero-zero-zero-zero—hex nine zero. Logical right fills with zeros from the left. Arithmetic right replicates the sign bit. Rotate wraps bits with no fill loss. Critical path is about three mux delays, not the shift distance.

## Slide 3 — Browser lab

![Barrel shifter starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge panel, the input bits and stage diagram, and the hex result readouts. Load the starter—hex D two shifted left by three toward hex nine zero. Step stages or show all, then try SRA or rotate presets. Use Check when a challenge looks done.

## Slide 4 — Workbook practice

In the workbook track, SLL hex eight zero right by one and give the result. For amount five, list which power-of-two stages fire. Sketch three mux layers for an eight-bit barrel. Contrast SRL and SRA on a negative pattern. Name one pitfall: confusing barrel stages with counting single-bit shifts one at a time.

## Slide 5 — Pitfalls to watch

Do not assume amount N means N serial one-bit layers—decode the amount into power-of-two enables. SRA and SRL differ only in the fill bit. And remember: the browser lab is literacy. Real ALUs still need variable-width rules, flags, and synthesis constraints beyond this eight-bit toy.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, trace one starter stage by stage. When you are ready, take the short quiz, then continue to seven segment.
