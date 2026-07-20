# Module 21 — XOR parity tree

**Module id:** module21-xor-parity-tree  
**Lab:** xor-parity-tree  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — XOR parity tree

Parity counts whether the number of ones is even or odd. Reduce XOR folds every bit with xor: odd count of ones gives one, even gives zero. You can fold left to right in a chain or pair bits in a balanced tree—XOR is associative, so both give the same answer. A tree needs about log N stages; a chain needs N minus one. Hardware parity generators prefer trees for timing. This module makes reduce XOR and tree depth concrete.

## Slide 2 — Fold, depth, even and odd

Four-bit one-zero-one-zero has two ones, so reduce XOR equals zero. Level one pairs one xor zero and one xor zero to get one-one; level two xors those to root zero. Tree depth for four bits is two; chain depth is three. Even parity bit equals reduce XOR; odd parity is the inverse. Flip any single bit and parity toggles. An odd leftover at a tree level promotes unchanged to the next row.

## Slide 3 — Browser lab

![XOR parity tree starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge panel, the bit row and XOR tree diagram, and the parity readouts. Load the starter—four bits one-zero-one-zero, reduce XOR equals zero, tree depth two versus chain depth three. Step tree levels or reveal the full tree, then compare depths. Use Check when a challenge looks done.

## Slide 4 — Workbook practice

In the workbook track, reduce-xor the bits one-one-zero-one by hand. Draw a balanced tree for eight bits and state tree depth versus chain depth. For reduce XOR equals one, give even and odd parity bits. Name one pitfall: building a long XOR chain when a tree would meet timing.

## Slide 5 — Pitfalls to watch

Do not confuse even parity with odd parity—one is the complement of the other. Tree and chain must agree on the final bit, but not on delay. And remember: the browser lab is literacy. Real links still need generator polynomials, multi-bit ECC, and on-wire framing beyond a single parity bit.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On paper, sketch one four-bit tree and label each level. When you are ready, take the short quiz, then continue to tri-state and bus.
