---
marp: true
title: FSM designer
paginate: true
---

# FSM designer

A finite-state machine has a finite set of states, inputs, outputs, and rules for what happens next

---

## Moore toggle starter
- Starter: Moore toggle with two states, S0 outputs zero, S1 outputs one
- When x equals one, the state flips; when x equals zero, it holds
- Step the stream one-zero-one-one and watch Z follow the state
- The transition table lists next state for every state-and-input pair
- Try the Mealy pulse preset too, Z pulses only on the transition when x equals one

---

## Browser lab
![FSM lab starter](assets/lab-starter.png)

---

## Workbook practice
- In the workbook track, draw a two-state Moore toggle and fill in its transition table
- Write one sentence on how Moore output differs from Mealy
- Sketch a three-state ring that advances on x equals one
- Name one pitfall: forgetting a default transition or leaving a state unreachable

---

## Pitfalls to watch
- Do not mix Moore and Mealy rules in the same table, output columns mean different things
- One input bit per step is like one clock cycle; the stream is not arbitrary analog time
- And remember: the browser lab is literacy
- Real RTL still needs encoding, reset state, and synthesis-friendly state registers

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On paper, draw one Moore table and one Mealy arc with Z on it
- When you are ready, take the short quiz, then continue to state encoding

