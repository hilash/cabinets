---
title: 3. Academic Theory
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - theory
  - architectures
  - stage-3
order: 4
icon: 📜
---

# 📜 Stage 3 — Academic Theory

**Time:** 1 hour of video + 1 hour of exercise.
**Source:** A one-hour survey of major deep learning architectures.
**Why:** Before you read papers, you need to know what the words *mean*.

> **Note:** If you're more hands-on than academic, you may prefer to do this stage **after** the Hands-On stage, as a summary. That's fine.

## Watch

<iframe width="720" height="405" src="https://www.youtube.com/embed/Q9bdjoVx_m4" title="Deep learning architectures survey" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Direct link: [Major deep learning architectures — survey talk](https://www.youtube.com/watch?v=Q9bdjoVx_m4)

## What's covered

Without peeking at the video, the talk covers (roughly):

- **MLPs** (multilayer perceptrons) — the baseline architecture
- **CNNs** (convolutional networks) — spatial inductive bias for images
- **RNNs / LSTMs** — sequential data before transformers ate the world
- **Transformers** — attention-based, the architecture of LLMs
- Training tricks: regularization, normalization, residual connections
- Loss landscapes, optimizers, learning rate schedules

## Exercise — architecture cheat sheet (1 hour)

Fill out the table below *from memory* after watching. No peeking at the video or web.

Use three columns per architecture:

- **What's the inductive bias?** (What prior assumption does this architecture encode?)
- **Where does it shine?**
- **Where does it fail?**

### My cheat sheet

| Architecture | Inductive bias | Shines at | Fails at |
|---|---|---|---|
| MLP |  |  |  |
| CNN |  |  |  |
| RNN / LSTM |  |  |  |
| Transformer |  |  |  |

After you fill it in, check back against the video and correct mistakes in a different color (or append a "corrections" block below).

### Corrections

```

```

## Glossary to pick up along the way

Terms you should be able to define in one sentence after this stage — helpful for the [[../05-research-paper/index|research paper]] stage later:

- Residual connection
- Layer normalization
- Batch normalization
- Dropout
- Softmax temperature
- Cross-entropy loss
- Learning rate schedule
- Gradient clipping

## Checklist

- [ ] Watched the full architectures survey
- [ ] Filled out the cheat sheet from memory
- [ ] Checked my answers against the video and wrote corrections
- [ ] Can define every term in the glossary
- [ ] Can draw a transformer block on paper (attention + FFN + residuals + layernorm)

## My notes

```

```

## Next

**[[../04-hands-on/index|Stage 4: Hands-On →]]** (the main event)
