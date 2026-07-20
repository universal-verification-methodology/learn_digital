# Module 06 — BCD

**Module id:** module06-bcd-lab  
**Lab:** bcd-lab  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — BCD

Binary-coded decimal stores each decimal digit in its own four-bit nibble. Displays, money, and some bus formats still speak BCD. Decimal forty-two packs as hex forty-two, not as binary two-A. This module makes that packing—and invalid nibbles—easy to see.

## Slide 2 — Four bits per digit

Each BCD digit uses four bits and runs from zero through nine. Nibbles A through F are invalid. Packed BCD lays digits side by side in one word—two digits need eight bits, four digits need sixteen. Do not confuse BCD with ordinary binary of the same decimal value; encode and decode on purpose.

## Slide 3 — Browser lab

![BCD lab starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge panel, the digit and packed-hex views, and Encode or Decode controls. Load the starter for decimal forty-two as packed zero-x-forty-two. Try encoding ninety-nine, then load an invalid nibble like four-A and watch valid go false. Show an encode trace when you want the digit-by-digit picture. Use Check when a challenge looks done.

## Slide 4 — Workbook practice

In the workbook track, write packed BCD for forty-two, ninety-nine, and zero with two digits. Mark why nibble A is illegal. Encode two thousand twenty-six as four digits and check you get hex two-zero-two-six. Note one pitfall: treating binary zero-x-two-A as if it were BCD for forty-two.

## Slide 5 — Pitfalls to watch

Do not mix binary and BCD encodings of the same number. Invalid nibbles must be rejected, not silently accepted. And remember: the browser lab is literacy. Real displays and decimal datapaths still need correct packing width and digit checks.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, pack a few decimals and one invalid case by hand. When you are ready, take the short quiz, then continue to parity and checksum.
