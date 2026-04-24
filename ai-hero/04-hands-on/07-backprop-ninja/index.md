---
title: 4.7 Backprop Ninja
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - karpathy
  - backprop
  - chain-rule
  - exercise
order: 7
icon: 🥷
---

# 🥷 4.7 — Becoming a Backprop Ninja

**Time:** 2 hours video + ~30 min active pause-and-try.
**Title:** *Building makemore Part 4: Becoming a Backprop Ninja.*

This video earns its reputation. Karpathy takes the full MLP + BatchNorm model and asks you to compute **every gradient by hand**, from scratch — no `.backward()`.

## Watch (but pause *before* every step)

<iframe width="720" height="405" src="https://www.youtube.com/embed/q8SA3rM6ckI" title="Building makemore Part 4: Becoming a Backprop Ninja" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Direct link: [Backprop Ninja — YouTube](https://youtu.be/q8SA3rM6ckI)

## The exercise (critical)

> Before each step Andrej does, **pause the video and try to do the backprop yourself.**

This is the whole point. Watching him derive `dlogits` and then nodding along teaches you nothing. Writing `dlogits` in your notebook, getting a shape error, fixing it, then watching his answer — that teaches you.

The key exercise cells are already staged in `notebook.ipynb`.

## What you'll backprop by hand

Working backward from the loss, through:

- Cross-entropy loss → logits
- Logits → pre-activation of the output layer
- Pre-activation → BatchNorm params (γ, β), running stats, and pre-BN
- Pre-BN → Linear
- Linear → tanh
- Tanh → pre-tanh Linear
- Pre-tanh Linear → embedding indices
- Embeddings → embedding table gradient

Every single one. With shapes.

## What this gives you

- Shape-level intuition for backprop that you'll lose if you only ever call `.backward()`
- The ability to *read* PyTorch's C++ gradient kernels when you need to
- A mental model of why certain gradient shapes are the transpose of something else (spoiler: chain rule)

## Checklist

- [ ] Watched every segment and **paused before each backprop step to try myself**
- [ ] My manual gradients match PyTorch's `.backward()` to numerical precision
- [ ] I correctly derived the BatchNorm backward pass (this is the hardest one)
- [ ] I can explain why the embedding table gradient is an `.index_add_` operation
- [ ] I understand the role of `torch.allclose` for sanity-checking gradients

## Common gotchas

- **Scatter vs. gather**: embedding gradients need you to scatter gradient *back* to the table rows that were indexed
- **BatchNorm math** has three chained derivatives: γ, β, and the normalization itself. Most people bomb on the normalization term because the denominator depends on all samples in the batch
- **Summing vs. not summing** over the batch dim — when does a gradient get summed vs. reshaped?

## My notes

```

```

## Next

**[[../08-wavenet/index|4.8 WaveNet →]]**
