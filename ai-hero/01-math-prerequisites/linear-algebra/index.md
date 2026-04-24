---
title: 1.1 Linear Algebra
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - math
  - linear-algebra
order: 1
icon: 🟦
---

# 🟦 Linear Algebra

**Time:** 2 hours.
**Source:** Serrano Academy — Linear Algebra playlist.
**Scope:** Videos 1–9 of the playlist.

## Watch

<iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab" title="Linear Algebra playlist" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Direct link: [Linear Algebra — Serrano Academy (playlist)](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=1)

## What you'll learn

- Vectors and vector spaces — why they're the natural object for representing data
- Linear transformations as **functions** that preserve addition and scaling
- Matrix multiplication as **function composition** — two transformations chained
- Transpose — what it does geometrically, and why it shows up in gradients
- Dot product, norms, projections
- (Maybe) determinants and eigenvectors depending on how far into the 9 videos you get

## Concepts to internalize

**Matrix shape notation.** Always write shapes. `(m, n) @ (n, p) → (m, p)`. Inner dimensions must match; they get eaten. Outer dimensions survive.

**Matmul is not elementwise.** `A * B` in numpy is elementwise. `A @ B` is the real one. Get this wrong once, lose an hour of debugging.

**Transpose swaps axes.** Shape `(m, n)` becomes `(n, m)`. The `i,j` element becomes the `j,i` element. That's it.

## Exercises (do these on paper)

1. Multiply by hand:

   ```
   A = [[1, 2],     B = [[5, 6],
        [3, 4]]          [7, 8]]

   A @ B = ?
   ```

   Then do `B @ A`. Confirm they're different (matmul is not commutative).

2. What's the shape of `A @ B` if `A` is `(4, 7)` and `B` is `(7, 3)`?

3. What's `Aᵀ` if `A = [[1, 2, 3], [4, 5, 6]]`? Write out the full matrix.

4. Prove to yourself that `(A @ B)ᵀ = Bᵀ @ Aᵀ`. Use a 2×2 example.

## Checklist

- [ ] Watched video 1 (vectors)
- [ ] Watched video 2 (linear transformations)
- [ ] Watched video 3 (matrix multiplication)
- [ ] Watched video 4 (dot product / projections)
- [ ] Watched video 5
- [ ] Watched video 6
- [ ] Watched video 7
- [ ] Watched video 8
- [ ] Watched video 9
- [ ] Can do a 2×2 matmul in my head
- [ ] Understand what transpose does geometrically

## My notes

_Jot what confused you and what clicked. The Math Tutor will thank you later._

```

```

## Next

[[../calculus/index|1.2 Calculus]] →
