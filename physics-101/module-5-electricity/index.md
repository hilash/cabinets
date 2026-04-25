---
title: Module 5 — Electricity
created: 2026-04-25
tags: [curriculum, physics, education, electricity]
icon: zap
order: 5
---

# Module 5 — Electricity

> Charge, current, voltage, resistance, and how they all fit together in a circuit.

## Hook — The 9V Battery Test

Pick up a 9-volt battery (the rectangular kind with both terminals on top) and touch it to your tongue. You feel a sharp, metallic tingle. Touch the same battery to your fingertip — nothing.

Same battery. Same 9 volts. Why does your tongue feel it but your skin doesn't?

The answer is hiding in this module. By the end, you'll be able to explain it in one sentence using three numbers: **voltage**, **resistance**, and **current**.

---

## Core Concepts

### 1. Charge (Q)

Matter is made of atoms, and atoms contain protons (+) and electrons (−). When an object has more electrons than protons, it carries a **negative charge**. Fewer electrons → positive charge. Equal → neutral.

- **Symbol:** Q
- **Unit:** coulomb (C)
- **One coulomb** ≈ 6.24 × 10¹⁸ electrons. Big number. A single electron carries almost nothing on its own.
- **Rule:** Like charges repel. Opposite charges attract.

### 2. Current (I)

When charges *move* through a wire, you have a **current**. Current is the *rate* of charge flow — how many coulombs pass a point per second.

- **Symbol:** I
- **Unit:** ampere (A) = 1 coulomb per second
- **Direction (convention):** from + to −, even though electrons actually drift the other way. Blame Benjamin Franklin — he guessed wrong, and we've never bothered to flip the convention.

Think of current like the *flow rate* of water in a pipe. Liters per second of water → coulombs per second of charge.

### 3. Voltage (V)

Voltage is the **electrical pressure** that pushes charges through a wire. More precisely, it's the energy per unit of charge — joules per coulomb.

- **Symbol:** V
- **Unit:** volt (V) = 1 joule per coulomb
- A 9V battery puts 9 joules of energy into every coulomb that flows out of its + terminal.

Water analogy: voltage is the height difference between a tank and a tap. Bigger drop → harder push → faster flow.

### 4. Resistance (R)

Every wire, lightbulb, and component fights the flow of charge a little. That opposition is **resistance**.

- **Symbol:** R
- **Unit:** ohm (Ω)
- A short, thick copper wire: tiny resistance.
- A long, thin tungsten filament: big resistance — that's why it heats up and glows.

Water analogy: a narrow, kinked pipe. Same pressure, less flow.

### 5. Ohm's Law

These three quantities are bound together by the most-used equation in electronics:

> **V = I × R**

Voltage equals current times resistance. Rearranged:

- I = V / R (current grows with voltage, shrinks with resistance)
- R = V / I (resistance is just the ratio of how much you push to how much flows)

That's it. Most of intro circuit analysis is bookkeeping around this one equation.

### 6. Series vs Parallel

Two ways to connect components:

**Series** — components on a single loop, end-to-end. Same current flows through every component. Resistances add:

> R_total = R₁ + R₂ + R₃ + ...

**Parallel** — components on separate branches between the same two points. Same voltage across each branch. Currents add. Total resistance is *less* than the smallest individual resistance:

> 1 / R_total = 1/R₁ + 1/R₂ + 1/R₃ + ...

A useful intuition: parallel paths give the current more room to flow, like opening extra lanes on a highway.

---

## Interactive Element — Circuit Reasoning Exercise

For each scenario below, reason out what happens *before* you peek at the answer. Cover the answer with your hand if you have to.

### Scenario A — The Doubled Battery

You have a circuit: one 1.5V battery, one 10Ω resistor. You measure the current.

Now you swap the battery for a 3V one (same resistor). What happens to the current?

<details>
<summary>Show answer</summary>

**Current doubles.** From Ohm's law, I = V / R. R is unchanged, V doubled, so I doubles. New current = 3 / 10 = 0.3 A. Old current = 1.5 / 10 = 0.15 A.

</details>

### Scenario B — Two Bulbs in Series

Two identical bulbs are wired in **series** to a battery. Both glow dimly. You unscrew one bulb. What happens to the other?

<details>
<summary>Show answer</summary>

**It goes out.** In a series loop, the same current must flow through every component. Removing one bulb breaks the loop — current can't flow at all, so the other bulb has nothing to light it.

</details>

### Scenario C — Two Bulbs in Parallel

Same two bulbs, now wired in **parallel** to the same battery. You unscrew one. What happens to the other?

<details>
<summary>Show answer</summary>

**It keeps glowing — and a touch brighter, in real circuits.** Each bulb is on its own branch with the full battery voltage across it, so removing one branch doesn't break the other. (This is why house wiring is parallel: turning off the kitchen light shouldn't kill the bedroom.)

</details>

### Scenario D — Back to the Hook

A 9V battery on your tongue: ~5,000 Ω of resistance. A 9V battery on dry fingertip skin: ~100,000 Ω.

Estimate the current in each case. Which one can you feel?

<details>
<summary>Show answer</summary>

- Tongue: I = 9 / 5,000 = **0.0018 A = 1.8 mA**. You feel that.
- Fingertip: I = 9 / 100,000 = **0.00009 A = 0.09 mA**. Below the threshold of sensation.

Same voltage, same battery — different resistance, different current, different sensation. That's the whole story.

</details>

---

## Worked Example — Series Circuit With Two Resistors

**Problem.** A 12V battery is connected in series with a 4Ω resistor and an 8Ω resistor. Find:

1. The total resistance.
2. The current flowing in the loop.
3. The voltage across each resistor.

**Step 1 — Total resistance.**

Series resistors add:

R_total = R₁ + R₂ = 4 + 8 = **12 Ω**

**Step 2 — Current.**

The whole loop sees the battery's 12V across the total 12Ω. Apply Ohm's law:

I = V / R_total = 12 / 12 = **1 A**

In a series circuit, this same 1 A flows through *every* component. That's the defining property of series.

**Step 3 — Voltage across each resistor.**

Apply Ohm's law to each resistor individually (same current, different R):

- V₁ = I × R₁ = 1 × 4 = **4 V**
- V₂ = I × R₂ = 1 × 8 = **8 V**

**Sanity check.** The two voltages should add up to the battery voltage: 4 + 8 = 12 V. ✓

This is **Kirchhoff's voltage law** in disguise: every joule of energy a coulomb gains from the battery has to be spent somewhere in the loop.

---

## Practice Questions

Try each one before reading the answer.

**Q1.** A circuit has a 6V battery and a 2Ω resistor. What is the current?

<details>
<summary>Answer</summary>

I = V / R = 6 / 2 = **3 A**.

</details>

**Q2.** A current of 0.5 A flows through a resistor when 10V is applied across it. What is its resistance?

<details>
<summary>Answer</summary>

R = V / I = 10 / 0.5 = **20 Ω**.

</details>

**Q3.** Three resistors — 2Ω, 3Ω, and 5Ω — are connected in **series**. What is the total resistance?

<details>
<summary>Answer</summary>

R_total = 2 + 3 + 5 = **10 Ω**. Series resistances simply add.

</details>

**Q4.** Two 6Ω resistors are connected in **parallel**. What is the total resistance?

<details>
<summary>Answer</summary>

1 / R_total = 1/6 + 1/6 = 2/6 = 1/3, so R_total = **3 Ω**.

Shortcut for two equal resistors in parallel: just halve the value. Makes sense — two equal lanes carry twice the current of one.

</details>

**Q5.** A toaster on a 120V outlet draws 10 A. What is the resistance of its heating element, and how much charge flows through it in one minute?

<details>
<summary>Answer</summary>

- Resistance: R = V / I = 120 / 10 = **12 Ω**.
- Charge in one minute: 10 A means 10 coulombs per second. In 60 seconds: Q = I × t = 10 × 60 = **600 C**.

That's about 3.7 × 10²¹ electrons through the element every minute. Toast is hard work.

</details>

---

## What's Next — Bridge to Module 6 (Light)

You just learned that moving charges = current. Here's the punchline that connects this whole module to the next:

> **Whenever charges accelerate, they radiate electromagnetic waves.**

The current wiggling back and forth in a radio antenna *is* what produces radio waves. The electrons jumping between energy levels in a lightbulb filament *are* what produces visible light. Electricity and light are not two separate phenomena — they're the same field, vibrating at different frequencies.

In **Module 6 — Light**, we'll pick up exactly there: how oscillating charges create electromagnetic waves, why those waves come in a spectrum from radio to gamma rays, and what happens when they hit a mirror, a lens, or your eye.

The water-in-a-pipe analogy gets you through circuits. It can't get you through light. For that, you need waves — which you already met in Module 4. Bring both with you.

→ [Module 6 — Light](../module-6-light/)
