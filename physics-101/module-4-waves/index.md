---
title: Module 4 — Waves
created: 2026-04-25
tags: [curriculum, physics, education, waves]
icon: waves
order: 4
---

# Module 4 — Waves

## Hook

Pluck a guitar string. Drop a pebble in a pond. Yell across a canyon. Wave at a friend (literally).

In every case, **something is moving** — but it's not the same kind of motion you've seen so far. The string doesn't fly off the guitar. The pond water doesn't travel to shore. The air between you and your friend doesn't whoosh forward. So what *is* moving?

**Energy is moving. The medium isn't.**

That single idea — energy travelling through stuff without the stuff going anywhere — is the whole game of waves. Once you see it, you start spotting waves everywhere: sound, light, earthquakes, ripples, even the wiggle in a slinky.

This module gives you the vocabulary to describe any wave, and the math to predict how fast it moves and what happens when two waves meet.

---

## Core Concepts

### What a wave actually is

A **wave** is a disturbance that travels through a medium (or through space), carrying energy without permanently moving the medium itself.

Picture a row of dominoes. Each domino barely moves — it just falls into its neighbor. But the *falling* travels all the way down the line. That's a wave.

### The four numbers that describe any wave

Every wave can be pinned down with four measurements:

| Quantity | Symbol | What it measures | Units |
|---|---|---|---|
| **Wavelength** | λ (lambda) | Distance from one peak to the next peak | meters (m) |
| **Frequency** | f | How many full waves pass a point each second | hertz (Hz) |
| **Period** | T | Time for one full wave to pass | seconds (s) |
| **Amplitude** | A | Max height of a peak from the resting line | meters (m) — or whatever the medium is measured in |

Two of these are tied together by definition:

$$
T = \frac{1}{f} \quad\quad f = \frac{1}{T}
$$

If 5 waves pass per second (f = 5 Hz), each one takes 1/5 of a second (T = 0.2 s). That's it — they're the same fact, written two ways.

**Amplitude tells you how loud, bright, or strong** the wave is. Frequency tells you what *kind* of wave it is — high pitch vs low pitch, red light vs blue light. These two are independent: you can crank up the volume (amplitude) without changing the note (frequency).

### Wave speed

How fast does a wave move? Multiply how long each wave is by how many pass per second:

$$
v = f \cdot \lambda
$$

That's the most important equation in this module. Memorize it.

- v = wave speed (m/s)
- f = frequency (Hz)
- λ = wavelength (m)

A short, fast-flickering wave and a long, slow wave can move at exactly the same speed. The medium sets the speed; frequency and wavelength just trade off against each other.

### Transverse vs longitudinal

Waves come in two flavors based on which way the medium wiggles:

- **Transverse:** the medium moves *perpendicular* to the wave's direction.
  Picture a rope you flick up and down — the rope wiggles vertically while the wave travels horizontally.
  *Examples:* light, water surface waves, guitar strings, stadium "the wave."

- **Longitudinal:** the medium moves *parallel* to the wave's direction — squeezing and stretching.
  Picture a slinky you push and pull along its length. Compressions travel down the slinky in the same direction your hand pushed.
  *Examples:* sound in air, P-waves in earthquakes, pressure pulses in pipes.

Quick test: if the medium is moving the same way the wave is traveling, it's longitudinal. If it's moving sideways to the wave, it's transverse.

### Interference: what happens when waves meet

Two waves passing through the same spot at the same time *add together*. This is called the **superposition principle** and it's bizarrely simple — you literally just add the heights at each point.

Two outcomes worth naming:

- **Constructive interference** — peaks line up with peaks. The waves combine into a bigger wave. Louder, brighter, taller.
- **Destructive interference** — peaks line up with troughs. They cancel. Silence, darkness, or flatness.

Noise-cancelling headphones are pure destructive interference: the headphones listen to incoming sound, generate the inverted wave, and the two cancel inside your ear.

After the meeting, both waves keep going as if nothing happened. They pass through each other — they don't bounce off.

---

## Interactive Element — Frequency & Amplitude Slider

Imagine a control panel with two knobs and a live waveform on screen:

```
┌─────────────────────────────────────────────┐
│                                             │
│        ╱╲      ╱╲      ╱╲      ╱╲          │
│       ╱  ╲    ╱  ╲    ╱  ╲    ╱  ╲         │
│  ────╱────╲──╱────╲──╱────╲──╱────╲───     │
│           ╲╱      ╲╱      ╲╱               │
│                                             │
└─────────────────────────────────────────────┘

 Frequency:  [────●────────]   2 Hz
 Amplitude:  [─────────●───]   0.8 m
```

**Try this in your head (or sketch it):**

1. **Drag frequency up.** Waves get *narrower* — more peaks fit in the same space. Wavelength shrinks. If the medium's speed is fixed, λ = v / f, so doubling frequency halves wavelength.

2. **Drag amplitude up.** Waves get *taller* — but the spacing stays the same. The note doesn't change; it just gets louder.

3. **Drag frequency to zero.** The wave flattens into a straight line. No oscillation, no wave.

4. **Drag amplitude to zero.** Same straight line — but now it's because there's no disturbance, not because there's no oscillation pattern.

**Mental model:** frequency = the wave's identity. Amplitude = the wave's loudness. They're orthogonal — change one, the other doesn't care.

**Bonus thought experiment:** add a second waveform on top, identical but shifted half a wavelength. Watch them cancel. Now shift it a *full* wavelength — they double. That's interference, live.

---

## Worked Example

**Problem:** A tuning fork vibrates at 440 Hz (concert A). The sound wave it produces travels through air at 343 m/s. What is the wavelength of the sound?

**Step 1 — write down what you know.**

- Frequency: f = 440 Hz
- Wave speed: v = 343 m/s
- Find: wavelength λ

**Step 2 — pick the equation.**

The wave speed equation links all three:

$$
v = f \cdot \lambda
$$

We want λ, so rearrange:

$$
\lambda = \frac{v}{f}
$$

**Step 3 — plug in.**

$$
\lambda = \frac{343 \text{ m/s}}{440 \text{ Hz}} = 0.78 \text{ m}
$$

**Step 4 — sanity check.**

About 78 cm — roughly the length of your arm. That's reasonable for an audible sound wave (audible wavelengths range from a couple centimeters up to about 17 meters). Higher pitch → shorter wavelength, lower pitch → longer. 440 Hz is mid-range, so a sub-meter wavelength fits.

**Answer:** λ ≈ 0.78 m

---

## Practice

Try each one before peeking at the answer.

### 1.

A wave on a rope has a wavelength of 2 m and a frequency of 5 Hz. How fast is the wave traveling?

<details>
<summary>Answer</summary>

v = f · λ = 5 Hz × 2 m = **10 m/s**
</details>

### 2.

A radio station broadcasts at 100 MHz (100,000,000 Hz). Radio waves travel at the speed of light, 3 × 10⁸ m/s. What is the wavelength?

<details>
<summary>Answer</summary>

λ = v / f = (3 × 10⁸ m/s) / (10⁸ Hz) = **3 m**

That's why FM radio antennas are about a meter long — they're tuned to a fraction of the wavelength.
</details>

### 3.

You double the amplitude of a sound wave but leave the frequency alone. What changes — the pitch, the loudness, both, or neither?

<details>
<summary>Answer</summary>

**Loudness only.** Amplitude controls intensity (how loud); frequency controls pitch. They're independent.
</details>

### 4.

A pendulum completes one full swing every 0.5 seconds. What's its frequency?

<details>
<summary>Answer</summary>

f = 1 / T = 1 / 0.5 s = **2 Hz**
</details>

### 5.

Two identical waves meet. Wave A's peak lines up exactly with Wave B's trough. What does the combined wave look like at that instant — and what is this called?

<details>
<summary>Answer</summary>

The waves cancel completely — the medium is flat at the meeting point. This is **destructive interference**. (If the waves keep traveling, they emerge unchanged on the other side.)
</details>

---

## What's Next — Bridge to Module 5 (Electricity)

You just learned that waves carry energy through a medium without the medium going anywhere. Hold onto that idea — it's about to come back in disguise.

In **Module 5 — Electricity**, you'll meet *current*: the flow of electrons through a wire. At first it looks like the opposite of a wave — actual particles moving down the wire, like water through a hose.

But here's the twist: when you flip a light switch, the bulb lights up almost instantly, even if the wire is a kilometer long. The electrons themselves drift through the wire incredibly slowly (millimeters per second). So how does the energy get there fast?

**The energy travels as a wave** — an electromagnetic disturbance racing down the wire near the speed of light, while the electrons themselves barely move. Same trick you just learned: the medium stays put; the energy moves.

Module 5 will give you charge, voltage, current, and resistance — the bookkeeping of electrical energy. Then in Module 6, waves and electricity collide head-on as light reveals itself to be an electromagnetic wave, and everything you learned here turns out to apply to the photons hitting your eyes right now.

→ [Module 5 — Electricity](../module-5-electricity/)
