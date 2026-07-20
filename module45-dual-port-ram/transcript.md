# Module 45 — Dual-port RAM

**Module id:** module45-dual-port-ram  
**Lab:** dual-port-ram  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — Dual-port RAM

Dual-port RAM gives two independent access ports—address, write enable, and data in—sharing one memory array. Both ports can read or write on the same clock edge. Different addresses behave independently. Same address with a write is a collision; the policy decides what each port reads and what data is stored. Common policies are write-first, read-first, and don't-care. Vendor block RAM documents vary—never assume.

## Slide 2 — Independent ports starter

Starter: eight-by-eight RAM with write-first policy. Port A at address zero, port B at address one—no collision. Step clock to read both ports independently. Then preset W slash W collision: both ports write the same address—port A data wins on store. Or preset W slash R: port A writes while port B reads. Under write-first, B sees new data; under read-first, B sees old data; under don't-care, the read may show X.

## Slide 3 — Browser lab

![Dual-port RAM starter](assets/lab-starter.png)

In the browser lab, set collision policy and configure port A and B. The memory grid highlights A in blue, B in violet, both in amber. Step clk applies both ports together. Status shows cycle, collision kind, and policy. Try Preset independent R, W slash W, and W slash R, then switch policies and step again.

## Slide 4 — Workbook practice

On paper, draw an eight-word RAM with two ports. Trace independent reads at addr zero and three. Tabulate collision cases: W slash W, W slash R, R slash R same address. For W slash R with write-first, note whether the read port sees old or new data. Name one pitfall: assuming all BRAMs behave the same on collision.

## Slide 5 — Pitfalls to watch

Do not ignore same-address writes—W slash W may leave undefined priority without a documented policy. Read-first versus write-first changes W slash R behavior on the read port. R slash R at the same address is fine—both see the same cell. And remember: true dual-port versus simple dual-port differs in hardware; this lab is behavioral literacy.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, step independent ports, then collide with two policies. On paper, sketch one W slash R timing with read-first. When you are ready, take the short quiz, then continue to byte-enable memory.
