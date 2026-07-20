# Module 18 — Mux / decoder / encoder

**Module id:** module18-mux-decoder  
**Lab:** mux-decoder  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — Mux, decoder, encoder

A multiplexer picks one data input under select control—two inputs need one select bit, four inputs need two. A decoder drives one hot outputs from a binary address. An encoder compresses one hot back to a binary code, often with a valid flag and priority on conflicts. This module makes all three directions concrete.

## Slide 2 — Select, one-hot, encode

Two-to-one mux: Y equals D zero when S is zero, D one when S is one. Four-to-one extends the select field. A two-to-four decoder lights exactly one Y line for addr zero zero through one one. Priority encoder: if I one and I three are both set, high-index-first may report three with V equals one. All inputs zero means V equals zero.

## Slide 3 — Browser lab

![Mux decoder starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge panel, the mux or decoder or encoder diagram, and the input toggles. Load the starter—a two-to-one mux with S equals zero, D zero equals one, D one equals zero, so Y equals one. Switch modes to try a four-to-one mux, a two-to-four decoder, or an encoder challenge. Use Check when a challenge looks done.

## Slide 4 — Workbook practice

In the workbook track, write the two-to-one mux truth table by hand. For addr one zero on a two-to-four decoder, say which Y line is high. Encode only I three set and give Y and V. Name one pitfall: confusing mux select width with decoder output count.

## Slide 5 — Pitfalls to watch

Do not tie multiple decoder outputs high at once—that is not one-hot. Encoder priority rules differ by design—know high versus low index first. And remember: the browser lab is literacy. Real buses still need enables, tri-states, and timing on select changes.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, sketch one mux and one decoder example. When you are ready, take the short quiz, then continue to priority and compare.
