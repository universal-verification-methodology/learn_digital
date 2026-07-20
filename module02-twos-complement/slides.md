---
marp: true
title: Two’s complement
paginate: true
---

# Two’s complement

Unsigned numbers only go one way

---

## Sign bit, negate, range
- At a fixed width, the top bit is the sign
- All ones is minus one
- To negate, invert every bit and add one
- The range is not symmetric
- That asymmetric floor is easy to forget when you “just add one more.”

---

## Browser lab
![Two’s complement starter](assets/lab-starter.png)

---

## Workbook practice
- In the workbook track, write width eight on paper
- Start from plus five: bits ending in zero one zero one
- Negate by hand, invert, then add one, and confirm you land on minus five
- Then write the signed meanings of all ones, the minimum pattern with only the sign bit set
- Name one RTL pitfall: treating a signed wire as unsigned, or forgetting the asymmetric min

---

## Pitfalls to watch
- Do not read the most significant bit as “just another magnitude bit” when the type is
- Do not expect plus one hundred twenty-eight to fit in eight-bit two’s complement, it wraps
- And remember: the browser lab is literacy
- Waveforms and RTL still demand the same signed-versus-unsigned discipline

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On paper, negate one value by hand and list min, max, and minus one for one width
- When you are ready, take the short quiz, then continue to overflow and wrap

