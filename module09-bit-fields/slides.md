---
marp: true
title: Bit-fields
paginate: true
---

# Bit-fields

Control and status registers pack flags and counters into one word

---

## Extract, insert, mask
- Field width is hi minus lo plus one
- Bit zero is the LSB in this lab
- Before you OR an insert
- An unmasked insert value can spill into other fields
- Show the mask formula when you want the bit picture

---

## Browser lab
![Bit-fields starter](assets/lab-starter.png)

---

## Workbook practice
- In the workbook track, take word A-five-two-D
- Extract COUNT at seven to three by hand and confirm five
- Clear that field with insert zero and check TAG is unchanged
- Write width of MODE at two to one as two
- Name one pitfall: inserting without masking so bits spill

---

## Pitfalls to watch
- Do not assume bit zero is MSB, this lab uses LSB numbering
- Overlapping fields or wrong hi and lo break packs
- And remember: the browser lab is literacy
- Real CSRs still need a spec for reset values, access types, and side effects

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On paper, extract and insert one field by hand
- When you are ready, take the short quiz, then continue to endian packing

