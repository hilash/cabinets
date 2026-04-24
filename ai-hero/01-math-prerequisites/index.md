---
title: 1. Math Prerequisites
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - math
  - stage-1
order: 2
icon: 🧮
---

# 🧮 Stage 1 — Math Prerequisites

**Time:** 4 hours of video.
**Goal:** Refresh (or learn for the first time) the math you'll use in every other stage.

Everyone should go over this, at least as a skim. If you haven't taken Calculus I and Linear Algebra I, **do not** skip this — you'll hit a wall in the backprop section.

## Pay extra attention to these three

These are the specific operations you will be doing yourself in code soon:

| Concept | Why it matters later |
|---|---|
| **Matrix multiplication** | Every forward pass in every neural net |
| **Transpose** | Gradient of `Wx` with respect to `x` is `Wᵀ`. No exceptions. |
| **Chain rule** | The entire backprop algorithm is the chain rule, applied repeatedly |

If you can't do a 3×3 matmul on paper without looking anything up, stop here and practice until you can.

## Sub-stages

| # | Topic | Time | Page |
|---|---|---|---|
| 1.1 | Linear Algebra | 2 h | [[linear-algebra/index\|Linear Algebra]] |
| 1.2 | Calculus | 1 h | [[calculus/index\|Calculus]] |
| 1.3 | Probability | 1 h | [[probability/index\|Probability]] |

## Checklist

- [ ] Completed all checkboxes in [[linear-algebra/index|Linear Algebra]]
- [ ] Completed all checkboxes in [[calculus/index|Calculus]]
- [ ] Completed all checkboxes in [[probability/index|Probability]]
- [ ] Can do a 3×3 matrix multiplication on paper, no calculator
- [ ] Can derive the chain rule for `f(g(h(x)))` by hand

## Math gotchas

_The Math Tutor appends notes here as you report confusion points._

## When you finish

Go to **[[../02-intuition/index|Stage 2: Intuition]]**.
