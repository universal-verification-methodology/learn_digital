# Module 44 — Cache walk

**Module id:** module44-cache-walk  
**Lab:** cache-walk  
**Tracks:** A (workbook) · B (browser lab)

## Slide 1 — Cache walk

A direct-mapped cache splits each address into tag, index, and offset. Index selects which set to probe. Tag compares against the stored line tag when valid. Offset picks the byte inside the cache line. A hit needs valid set and matching tag. A miss fetches or installs the line. Two addresses with the same index but different tags map to one set and can conflict. This lab walks probe, hit, miss, and install step by step.

## Slide 2 — Address 0x14 starter

Starter: cold direct-mapped cache, two index bits, two offset bits—four sets, four-byte lines, sixteen-byte capacity. Address hex fourteen decodes to tag one, index one, offset zero. First Access is a miss; install loads the line into set one. Access again is a hit. Address hex fifteen shares tag and index with offset one—still a hit, spatial locality. Address hex twenty-four shares index one but tag two—a conflict miss.

## Slide 3 — Browser lab

![Cache walk starter](assets/lab-starter.png)

In the browser lab, set index and offset bit widths and enter an address. Colored address bits show tag, index, and offset fields. Access walks decode, probe, and hit or miss verdict. The set table shows valid, tag, and line data. On miss, choose Install line to fill the set. Access log records each result.

## Slide 4 — Workbook practice

On paper, split address hex fourteen with two index and two offset bits. Label tag, index, and offset values. Draw four sets with one line each. Trace cold access, install, repeat hit, and one conflict miss. Compute line size as two to the offset bits and capacity as sets times line size. Name one pitfall: assuming same index means same tag.

## Slide 5 — Pitfalls to watch

Do not treat index as the full address—tag distinguishes lines in the same set. Valid zero always means miss. Direct-mapped is simple but thrashes on conflicts; set-associative caches reduce that at higher cost. And remember: this toy memory uses a formula for bytes—real caches fetch from backing store.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, decode zero fourteen, miss once, hit twice, then try zero twenty-four. On paper, fill one row of the set table after install. When you are ready, take the short quiz, then continue to dual-port RAM.
