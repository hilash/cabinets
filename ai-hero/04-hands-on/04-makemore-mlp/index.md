---
title: 4.4 Makemore MLP
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - karpathy
  - makemore
  - mlp
  - embedding
order: 4
icon: 🧮
---

# 🧮 4.4 — Makemore Part 2: MLP

**Time:** 1 hour of video.
**Title:** *Building makemore Part 2: MLP.*

Follows the 2003 Bengio *et al.* neural language model paper. This is the first time you see a **character embedding** and a proper **multi-layer** network.

## Watch

<iframe width="720" height="405" src="https://www.youtube.com/embed/TCH_1BHY58I" title="Building makemore Part 2: MLP" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Direct link: [Makemore Part 2: MLP — YouTube](https://youtu.be/TCH_1BHY58I)

## What you build

A character-level MLP:

```
input:  block_size=3 previous characters  →  embedding lookup (vocab=27, d=10)
                                           →  concat → (3*10,) vector
                                           →  Linear → tanh
                                           →  Linear → logits (27,)
                                           →  cross-entropy loss
```

You'll train it on names, tune hyperparameters, and see the model generate plausible names.

## Key concepts introduced

- **Embedding table**: learned vectors for discrete tokens. `C[idx]` replaces one-hot encoding.
- **Block size / context window**: how many previous characters the model sees
- **Mini-batch SGD**: train on a random subset at each step
- **Learning rate finder**: sweep LR and see where loss decreases fastest
- **Train / val / test splits** — and why
- **Overfitting** — what it looks like on the loss curves

## Pay extra attention at these moments

- When he visualizes the 2D embedding after training. Vowels cluster. Why?
- The discussion of "what's the max sensible size of this model before it overfits?"
- The notebook-style exploration of different hyperparameters — mirror this in your own notebook

## Watch out for

- He uses `.view(-1, 30)` to flatten embeddings — the `-1` means "figure out the batch dim from the other dim." Understand this before moving on.
- `F.cross_entropy(logits, targets)` — this includes softmax internally. Do NOT also softmax the logits yourself before passing them in.

## Checklist

- [ ] Watched the full video, typing along
- [ ] Built the MLP with embedding, hidden, and output layers
- [ ] Split data into train/val/test (80/10/10 is typical)
- [ ] Ran the learning rate finder — know what LR zone my model likes
- [ ] Trained long enough to see val loss plateau
- [ ] Recorded my best val loss: `___`
- [ ] Sampled names — they should be noticeably better than trigram

## My notes

```

```

## Next

**[[../05-mlp-tuning/index|4.5 MLP tuning exercise →]]** — beat Karpathy's 2.2.
