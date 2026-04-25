---
title: Module 1 — Motion
created: 2026-04-25
tags: [curriculum, physics, motion, kinematics]
icon: move
order: 1
---

# Module 1 — Motion

## Hook

Drop a tennis ball from your hand. It hits the floor in about half a second. In that half second, it covered roughly a meter — but it didn't cover the meter at a steady pace. It started slow and finished fast.

That single observation contains the three ideas that run this entire module:

- **Position** — where the ball is.
- **Velocity** — how fast its position is changing.
- **Acceleration** — how fast its velocity is changing.

If you can tell those three apart, you can describe the motion of anything: a falling ball, a sprinter, a car merging onto a highway, a satellite. This module gives you the vocabulary, the equations (algebra only), and the graphs that make all of it visual.

## Core Concepts

### Position (x)

Position is *where something is*, measured from a chosen origin. Units: meters (m).

Position is a number with a sign. If you pick "right" as positive, then `x = +3 m` means three meters to the right of the origin. `x = -2 m` means two meters to the left. The origin is your choice — pick whatever makes the problem easy.

### Displacement (Δx)

Displacement is the *change* in position: `Δx = x_final − x_initial`.

Displacement is not the same as distance traveled. If you walk 3 m east and then 3 m back west, your distance traveled is 6 m but your displacement is 0 m. Physics cares about displacement.

### Velocity (v)

Velocity is *how fast position changes, and in what direction*. Units: meters per second (m/s).

Average velocity over a time interval:

```
v_avg = Δx / Δt = (x_final − x_initial) / (t_final − t_initial)
```

Velocity has a sign. `+5 m/s` is moving in the positive direction at 5 m/s. `-5 m/s` is moving in the negative direction at the same speed. **Speed** is just the size of velocity with the sign stripped off.

### Acceleration (a)

Acceleration is *how fast velocity changes*. Units: meters per second per second (m/s²).

```
a_avg = Δv / Δt = (v_final − v_initial) / (t_final − t_initial)
```

Three things to internalize:

1. Acceleration is *not* the same as "going fast." A car cruising at 100 km/h on the highway has zero acceleration.
2. Acceleration with the *same* sign as velocity means speeding up. Acceleration with the *opposite* sign means slowing down (sometimes called "deceleration," but that's just a word — physics only has acceleration).
3. On Earth, free-falling objects have a downward acceleration of about `g = 9.8 m/s²`, regardless of mass.

### The Algebra-Only Kinematic Equations

For motion in a straight line with **constant acceleration**, four equations cover almost everything:

```
1.  v = v₀ + a·t                       (velocity at time t)
2.  x = x₀ + v₀·t + ½·a·t²             (position at time t)
3.  v² = v₀² + 2·a·(x − x₀)            (velocity vs. position, no t)
4.  x = x₀ + ½·(v₀ + v)·t              (uses average velocity)
```

`v₀` is initial velocity, `x₀` is initial position. Pick the equation whose unknowns match what you have and what you want.

### Graphs of Motion

Three graphs, read in order, tell the whole story:

| Graph | What the slope means | What the area means |
|-------|----------------------|---------------------|
| Position vs. time (x-t) | velocity | — |
| Velocity vs. time (v-t) | acceleration | displacement |
| Acceleration vs. time (a-t) | "jerk" (ignore for now) | change in velocity |

Two patterns to memorize:

- A **straight, sloped line on x-t** = constant velocity.
- A **straight, sloped line on v-t** = constant acceleration (which makes x-t a parabola).

## Interactive Element — The Velocity-Time Slider Thought Experiment

You don't need a simulator open to do this. Picture a velocity-vs-time graph with two sliders:

- **Slider A** sets the *starting velocity* `v₀` (the height of the line at t = 0).
- **Slider B** sets the *acceleration* `a` (the slope of the line).

Now run these four scenarios in your head and predict the shape of the position-vs-time graph for each, *before* reading the answer:

**Scenario 1.** `v₀ = +5 m/s`, `a = 0`. → A horizontal line on v-t at +5.
**Scenario 2.** `v₀ = 0`, `a = +2 m/s²`. → A line through the origin sloping upward.
**Scenario 3.** `v₀ = +10 m/s`, `a = -2 m/s²`. → A line starting at +10 sloping downward, crossing zero at t = 5 s.
**Scenario 4.** `v₀ = -5 m/s`, `a = +1 m/s²`. → A line starting at -5 sloping upward, crossing zero at t = 5 s.

Now the predictions:

| Scenario | Position-vs-time shape | What's happening physically |
|----------|------------------------|------------------------------|
| 1 | Straight line, slope +5 | Cruising at constant speed |
| 2 | Upward-curving parabola from origin | Speeding up from rest |
| 3 | Parabola that rises, peaks at t = 5 s, then falls | Thrown up, comes back down |
| 4 | Parabola that falls, bottoms out at t = 5 s, then rises | Moving backward, slowing, then forward |

If you got Scenario 3 or 4 correct, you have the central insight of kinematics: **velocity tells you the slope of position, and acceleration tells you the slope of velocity.** The shapes follow.

**Want to play with real sliders?** PhET's free *Moving Man* simulation lets you drag any of the three quantities and watch the others respond in real time: <https://phet.colorado.edu/en/simulations/moving-man>

## Worked Example — The Stoplight Sprint

> A car is stopped at a red light. The light turns green and the car accelerates at a constant `2.5 m/s²` for `8 seconds`, then continues at that velocity. How far has the car traveled at the moment it stops accelerating, and how fast is it going?

**Step 1 — Write down what we know.**

```
v₀ = 0 m/s        (starts from rest)
a  = 2.5 m/s²
t  = 8 s
x₀ = 0 m          (call the stoplight the origin)
```

**Step 2 — Pick equations.**

For final velocity, use equation 1:
```
v = v₀ + a·t
v = 0 + (2.5)(8)
v = 20 m/s
```

For position, use equation 2:
```
x = x₀ + v₀·t + ½·a·t²
x = 0 + 0 + ½·(2.5)·(8)²
x = ½·(2.5)·(64)
x = 80 m
```

**Step 3 — Sanity-check.**

Average velocity over the 8 s should be `(0 + 20)/2 = 10 m/s`. Multiplied by 8 s gives 80 m. ✓ Matches.

**Answer:** The car has traveled **80 meters** and is moving at **20 m/s** (about 72 km/h, or 45 mph) when it stops accelerating.

## Practice Questions

Try each one with paper before peeking at the answer.

**1.** A jogger runs 200 m east in 50 s, pauses for 10 s, then walks 50 m east in 25 s. What is her average velocity over the entire trip?

**2.** A skateboarder is rolling at +4 m/s when she starts pushing, accelerating at +0.5 m/s² for 6 s. What is her velocity at the end of the 6 s?

**3.** A ball is dropped from rest off a bridge and falls for 3 s before hitting the water. Using `g = 9.8 m/s²`, how fast is it moving when it hits the water, and how far did it fall?

**4.** A cyclist traveling at +12 m/s brakes uniformly and comes to a stop in 4 s. What is the acceleration (include sign), and how far does the bike travel during braking?

**5.** Looking at a velocity-vs-time graph, you see a straight horizontal line at v = -3 m/s from t = 0 to t = 6 s. Describe the motion in words, and find the displacement over those 6 s.

---

### Answers

**1.** Total displacement = 200 + 0 + 50 = 250 m east. Total time = 50 + 10 + 25 = 85 s. `v_avg = 250/85 ≈ 2.94 m/s east`.

**2.** `v = v₀ + a·t = 4 + (0.5)(6) = 4 + 3 = 7 m/s`.

**3.** `v = v₀ + g·t = 0 + (9.8)(3) = 29.4 m/s downward`. Distance fallen: `x = ½·g·t² = ½·(9.8)·(9) = 44.1 m`.

**4.** `a = (v − v₀)/t = (0 − 12)/4 = -3 m/s²` (negative because she's slowing down). Distance: average velocity is `(12 + 0)/2 = 6 m/s`, times 4 s = `24 m`.

**5.** The object is moving in the negative direction at a constant 3 m/s — no acceleration, just steady backward motion. Displacement is the area under the v-t graph: `(-3 m/s)(6 s) = -18 m` (i.e., 18 meters in the negative direction).

## What's Next — Bridge to Module 2 (Forces)

You can now describe *how* things move. You cannot yet explain *why*.

Why does the dropped tennis ball accelerate at exactly 9.8 m/s² and not some other number? Why does the car in the worked example need to push against the road to accelerate? Why does a hockey puck on ice glide nearly forever, while one on concrete stops quickly?

Acceleration is the bridge. Every acceleration you computed in this module had a *cause* — gravity, an engine, friction, a brake — and that cause has a name: **force**. Module 2 introduces Newton's three laws and the equation that ties everything you just learned to the physical world:

```
F = m·a
```

The kinematics from this module describe the motion. The forces in the next module *create* it. Once you have both, you can solve almost any everyday mechanics problem from scratch.

→ [Module 2 — Forces](../module-2-forces/)
