---
title: 1.3 Probability
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - math
  - probability
order: 3
icon: 🟪
---

# 🟪 Probability

**Time:** 1 hour.
**Source:** Krista King — Probability playlist, videos 1–4.
**Scope:** Basic probability intuition — events, distributions, expectation.

## Watch

<iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLiAulSm0XXgvCGe63mrAkda9UQ9478YQv" title="Probability playlist" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Direct link: [Probability — Krista King (playlist)](https://www.youtube.com/watch?v=HZGCoVF3YvM&list=PLiAulSm0XXgvCGe63mrAkda9UQ9478YQv&index=1)

## Why probability at all?

Language modeling **is** probability. A language model outputs `P(next_token | previous_tokens)`. Training is maximum likelihood — you nudge the weights so the correct next token gets higher probability.

The three ideas you must leave with:

| Idea | Where it shows up |
|---|---|
| **Probability distribution** (sums to 1) | Softmax output of an LLM |
| **Expectation** `E[X]` | Loss functions (cross-entropy is an expected negative log-prob) |
| **Independence** vs. **conditional probability** | The entire modeling choice — is this token independent of the previous one, or conditioned on it? |

## Softmax — a first taste

You'll meet this constantly. Given a vector of logits `z`, softmax turns them into a probability distribution:

```
softmax(z)_i = exp(z_i) / Σ_j exp(z_j)
```

Every element is now in `[0, 1]`. All elements sum to `1`. It's a distribution. That's the whole trick.

## Exercises

1. If `z = [1, 2, 3]`, what is `softmax(z)`? (Do it by hand — calculator allowed for `exp`.)
2. A language model says the distribution over the next token is `[cat: 0.6, dog: 0.3, fish: 0.1]`. What is `-log P(dog)`? (This is the loss if the ground truth was "dog".)
3. If I flip a fair coin twice independently, what is `P(both heads)`? What is `P(at least one heads)`?

## Checklist

- [ ] Watched Probability video 1
- [ ] Watched Probability video 2
- [ ] Watched Probability video 3
- [ ] Watched Probability video 4
- [ ] Can compute softmax of a length-3 vector by hand
- [ ] Can explain "cross-entropy" as "average negative log-probability of the correct class"

## My notes

```

```

## Next

[[../index|← Back to Math overview]] or **[[../../02-intuition/index|Stage 2: Intuition →]]**
