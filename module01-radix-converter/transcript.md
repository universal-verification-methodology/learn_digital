# Module 01 — Radix & bit width

**Module id:** module01-radix-converter  
**Lab:** radix-converter  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — Radix & bit width

Hardware does not store “thirteen.” It stores a fixed-width bit pattern that you may read as binary, hex, unsigned decimal, or two’s-complement signed. This module trains that conversion skill—in the browser lab for speed, then on paper so you can still do it without the UI.

## Slide 2 — Same bits, many readings

A width is a hard budget: eight bits is not the same box as four bits. Inside one width, the pattern is shared. Binary, hex, and unsigned decimal are different spellings of those bits. Signed two’s complement is another reading of the same pattern—so all ones at width eight is unsigned two hundred fifty-five, but signed minus one. Change the width, and the meaning can change even if you type the same digits.

## Slide 3 — Browser lab

![Radix converter starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge panel, the width control, and the linked views for binary, hex, and decimal. Load the starter, set a width, enter a value in one base, and watch the others update. Try Check when you think a challenge is done. You do not need a full tour—the lab walks the rest. Explore a few challenges, then come back for the workbook track.

## Slide 4 — Workbook practice

In the workbook track, pick one concrete conversion and do it by hand. For example, take unsigned decimal thirteen at width eight. Write the eight-bit binary, then the hex, and say the unsigned decimal out loud so the three spellings feel like one pattern. Then flip to signed thinking: what signed value is the all-ones pattern at that width? Write one pitfall you will watch for in later RTL—wrong width, or mixing signed and unsigned readings.

## Slide 5 — Pitfalls to watch

Do not treat hex digits as if the width were infinite—overflow wraps or truncates inside the chosen width. Do not confuse “the number I typed” with “the bits the hardware keeps.” And remember: the browser lab is for literacy. When you write RTL later, the same bit-pattern discipline still applies on paper and in waveforms.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, finish at least one worked conversion and name one pitfall. When you are ready, take the short quiz, then continue to two’s complement.
