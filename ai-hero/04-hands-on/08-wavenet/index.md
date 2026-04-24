---
title: 4.8 WaveNet
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - karpathy
  - wavenet
  - convolutions
  - hierarchical
order: 8
icon: 🌊
---

# 🌊 4.8 — Makemore Part 5: WaveNet

**Time:** 1 hour of video.
**Title:** *Building makemore Part 5: Building a WaveNet.*

You've been smashing character embeddings into one big flat vector before feeding them to the MLP. That's wasteful. **WaveNet** (originally DeepMind's audio model) suggests a hierarchical approach: fuse pairs of characters into a single representation, then fuse pairs of pair-representations, and so on — a tree of features.

## Watch

<iframe width="720" height="405" src="https://www.youtube.com/embed/t3YJ5hKiMQ0" title="Building makemore Part 5: Building a WaveNet" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Direct link: [Makemore Part 5: WaveNet — YouTube](https://youtu.be/t3YJ5hKiMQ0)

## Key concepts introduced

- **Hierarchical fusion** of tokens — the intuition behind convolutional/dilated models for sequences
- A first taste of **1D convolutions** applied to text
- Building reusable PyTorch `nn.Module`s: `Linear`, `BatchNorm1d`, `Tanh`, `Embedding`, `FlattenConsecutive`, `Sequential`
- Why thinking about your model as a **stack of blocks** scales much better than one giant MLP
- Keeping train and eval modes straight across a modular architecture

## Pay extra attention at these moments

- The refactoring pass where he turns his MLP code into proper `nn.Module`s. This is the "now I'm writing real PyTorch" moment — and sets up the GPT video cleanly.
- The `FlattenConsecutive` module. It's five lines but captures the WaveNet hierarchy idea.
- The debate about BatchNorm in a model with varying batch-dim shapes.

## What you should leave with

- Comfort writing custom `nn.Module`s
- Intuition for *why* architecture (hierarchy, inductive bias) matters — the WaveNet beats the flat MLP on the same data
- A vocabulary for discussing "blocks" and "layers" that will help when you hit transformers next

## Checklist

- [ ] Watched the full video, typing along
- [ ] Refactored my MLP code into reusable `nn.Module` blocks
- [ ] Built the hierarchical WaveNet-style model
- [ ] Trained it and compared val loss vs. the flat MLP — WaveNet should win on the same params
- [ ] Understand what `FlattenConsecutive` does to tensor shapes

## My notes

```

```

## Next

**[[../09-build-gpt/index|4.9 Let's build GPT →]]** — the main event.
