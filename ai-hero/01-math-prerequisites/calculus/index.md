---
title: 1.2 Calculus
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - math
  - calculus
  - chain-rule
order: 2
icon: 🟩
---

# 🟩 Calculus

**Time:** 1 hour.
**Source:** Serrano Academy — Calculus playlist (videos 1–4) + one bonus video on the chain rule.
**Scope:** Derivatives, gradients, the chain rule.

## Watch 1 — Calculus basics (videos 1–4)

<iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr" title="Calculus playlist" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Direct link: [Calculus — Serrano Academy (playlist)](https://www.youtube.com/watch?v=WUvTyaaNkzM&list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr&index=1)

## Watch 2 — Chain rule (the most important idea in deep learning)

<iframe width="720" height="405" src="https://www.youtube.com/embed/AXqhWeUEtQU" title="Chain rule explained" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Direct link: [The chain rule](https://www.youtube.com/watch?v=AXqhWeUEtQU)

## What you'll learn

- Derivative as **slope of a function at a point** — and as the *rate of change*
- Partial derivatives — take the slope *in one direction only*, freezing the others
- Gradient — the vector of all partial derivatives. It points uphill.
- **The chain rule** — how to differentiate nested functions. This *is* backpropagation.

## Why the chain rule is everything

A neural network is a chain of functions:

```
loss = L(f_N( f_{N-1}( ... f_1(x) ... )))
```

To train it, you want `∂loss/∂(weights)` for every layer. The only way to get there is the chain rule. Every single deep learning framework is, at its heart, a highly-optimized chain rule calculator.

> If you only remember one formula from this stage, remember:
> `df/dx = df/dg · dg/dx`

## Exercises (do these on paper)

1. Let `f(x) = (3x + 2)²`. Use the chain rule to compute `df/dx`.
2. Let `f(x, y) = x²y + y³`. Compute `∂f/∂x` and `∂f/∂y`.
3. Let `L = (y - ŷ)²` and `ŷ = w·x + b`. Compute `∂L/∂w` and `∂L/∂b` using the chain rule. **This is one training step of linear regression.**

## Checklist

- [ ] Watched Calculus video 1 (derivative basics)
- [ ] Watched Calculus video 2
- [ ] Watched Calculus video 3
- [ ] Watched Calculus video 4
- [ ] Watched the standalone chain-rule video
- [ ] Did all 3 exercises above on paper

## My notes

```

```

## Next

[[../probability/index|1.3 Probability]] →
