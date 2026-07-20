# Module 28 — Clock enable vs gated clock

**Module id:** module28-clock-enable  
**Lab:** clock-enable  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — Clock enable vs gated clock

To save power or skip cycles you can stop updating a register—but how you stop matters. Clock enable keeps clk free-running and loads only when ce is high: if ce, q gets d. AND-gating the clock feeds clk and ce into an AND—if ce changes while clk is high, a glitch can fake an extra edge. Integrated clock gates latch enable when clk is low, then AND—safer when you truly must gate. This module compares all three styles.

## Slide 2 — Load, hold, glitch

Starter: clock-enable mode with ce equals one—each posedge loads d into q. Set ce to zero and q holds even if d changes—that is recycle without touching the clock tree. Switch to AND-gated mode and arm an enable glitch while clk is high—the warning lights up. ICG sketch shows latched enable for cleaner gating. Preferred RTL default: clock enable on the data path, not raw AND on clk.

## Slide 3 — Browser lab

![Clock enable starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge panel, the clk-ce-q wave strip and diagram, and the RTL snippet for each style. Load the starter—clock enable with free-running clk. Run the demo load-then-hold, try gated glitch, or switch to ICG. Use Check when a challenge looks done.

## Slide 4 — Workbook practice

In the workbook track, write the always block for clock enable versus AND-gated clock. Sketch clk, ce, and q for CE equals one then CE equals zero with d changing. Explain why ce toggling during clk high is risky for gated mode. Name one pitfall: using AND-gated clocks without an ICG cell in real silicon.

## Slide 5 — Pitfalls to watch

Do not confuse holding q with stopping the clock—CE holds data; gating stops edges. Glitches on gated clocks can cause extra captures or timing nightmares. And remember: the browser lab is literacy. Real designs still need clock-tree constraints, ICG rules, and STA on enable paths.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, draw one CE hold wave and one gated-glitch caution. When you are ready, take the short quiz, then continue to CDC and two-FF sync.
