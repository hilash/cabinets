---
title: 4.1 Micrograd
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T20:22:24.326Z'
tags:
  - karpathy
  - autograd
  - backprop
icon: ⚙️
order: 1
---
# ⚙️ 4.1 — Micrograd

**Time:** 2.5 hours of video, typing along. **Title:** *The spelled-out intro to neural networks and backpropagation: building micrograd.*

> Karpathy's claim: after this video, you understand backpropagation. He is not exaggerating.

## Watch (and type along)

<iframe width="720" height="405" src="https://www.youtube.com/embed/VMj-3S1tku0" title="The spelled-out intro to neural networks and backpropagation: building micrograd" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Direct link: [Building micrograd — YouTube](https://youtu.be/VMj-3S1tku0)

## What you build

A scalar-valued autograd engine — `micrograd.Value` — in **pure Python**, no torch, no numpy. Every operation (`+`, `*`, `tanh`, etc.) builds up a computation graph. `.backward()` walks the graph in topological order and computes gradients via the chain rule.

Then a tiny MLP on top of it, which you train on a toy dataset.

## Key concepts introduced

<table class="border-collapse w-full" style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Concept</p></th><th colspan="1" rowspan="1"><p>First touched in this video</p></th></tr><tr><td colspan="1" rowspan="1"><p>Forward pass</p></td><td colspan="1" rowspan="1"><p>Yes</p></td></tr><tr><td colspan="1" rowspan="1"><p>Backward pass (backprop)</p></td><td colspan="1" rowspan="1"><p>Yes — the core of the video</p></td></tr><tr><td colspan="1" rowspan="1"><p>Topological sort of the graph</p></td><td colspan="1" rowspan="1"><p>Yes</p></td></tr><tr><td colspan="1" rowspan="1"><p>Gradient accumulation (<code>+=</code> not <code>=</code>)</p></td><td colspan="1" rowspan="1"><p>Yes — and the bug that arises if you forget</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>zero_grad()</code> before each training step</p></td><td colspan="1" rowspan="1"><p>Yes</p></td></tr><tr><td colspan="1" rowspan="1"><p>Chain rule applied to code</p></td><td colspan="1" rowspan="1"><p>Constantly</p></td></tr></tbody></table>

## Pay extra attention at these moments

-   When he implements `__add__` and `__mul__` — the `_backward` lambda captures locals; that's how the graph tracks parents
    
-   The derivation of the derivative of `tanh`
    
-   The topological sort (he writes it from scratch)
    
-   The step where `zero_grad` is added after the fact — pause and ask yourself *why the loss went up before he added it*
    

## Work with the reference notebook

Open `notebook.ipynb` in this directory. It contains a **complete reference implementation** with:

- The full `Value` class with `+`, `*`, `**`, `tanh`, `exp`, `relu`
- A `draw_graph()` function that renders your computation graph (graphviz or matplotlib fallback)
- `Neuron`, `Layer`, `MLP` built on top
- A real training loop on a 4-example toy dataset with a loss curve plot

Do not just run the cells. Type along with Karpathy's video — your fingers need the reps. Use the reference to check yourself after each section.

## 🎛️ Related visualization

See the loss landscape your autograd engine navigates: **[[../../gradient-descent/index|Gradient Descent simulator]]**. Drop a ball on 2D loss surfaces (bowl, valley, saddle, wavy), play with learning rate and momentum.

## Checklist

-   Watched the entire video, typing along
    
-   My `Value` class passes: `((Value(2) + Value(3)) * Value(4)).backward()` gives sensible grads
    
-   I implemented `__add__`, `__mul__`, `__pow__`, `tanh`, `exp`
    
-   I implemented `.backward()` with topological sort
    
-   I understand why we **accumulate** `grad` instead of **overwrite** it
    
-   I can explain, in one sentence, what backprop is doing
    
-   I trained the tiny MLP and watched the loss decrease
    

## My notes

## Next

[[../02-makemore-bigram/index|4.2 Makemore: bigram →]]
