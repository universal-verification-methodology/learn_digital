# Module 08 — Fixed-point Qm.n

**Module id:** module08-fixed-point  
**Lab:** fixed-point  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — Fixed-point Qm.n

Hardware often needs fractions without a full floating-point unit. Fixed-point Qm.n keeps a binary point: m bits for the integer side including sign, n bits for the fraction. Decode divides the signed raw integer by two to the n. This module makes scale, step, and saturation concrete.

## Slide 2 — Scale, step, and width

In this lab, total width W equals m plus n. The smallest positive step is two to the minus n. Encoding a real multiplies by two to the n and rounds into the bit field; values past the range saturate. Changing n with the same raw bits moves the binary point and changes the real value. m includes the sign bit here.

## Slide 3 — Browser lab

![Fixed-point starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge panel, the Qm.n bit view with the binary point, and Encode or Decode controls. Load the starter for Q four-dot-four raw hex one-eight, which decodes to one-point-five. Encode zero-point-five and a negative like minus one-point-two-five. Try a huge encode to see saturation, or change n and watch the real value shift. Use Check when a challenge looks done.

## Slide 4 — Workbook practice

In the workbook track, take Q four-dot-four. Show why raw twenty-four is one-point-five, and why raw eight is zero-point-five. Compute the step size as one sixteenth. Note the approximate min near minus eight. Name one pitfall: treating raw bits as a float without dividing by two to the n.

## Slide 5 — Pitfalls to watch

Do not forget the scale when you mix formats. Saturation is not the same as wrap. And remember: the browser lab is literacy. Real DSP still needs agreed Q formats, rounding modes, and overflow policy across blocks.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, encode and decode one Q four-dot-four value by hand. When you are ready, take the short quiz, then continue to bit-fields.
