---
title: 4.3 Trigram Exercise
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - karpathy
  - exercise
  - trigram
order: 3
icon: 🎯
---

# 🎯 4.3 — Exercise: Trigram language model

**Time:** 1 hour.
**Type:** Exercise. You build this yourself.

## The brief

> Train a **trigram** language model — take two characters as input and predict the third. Use a **neural net** architecture (not just counting). Evaluate the loss. Did it improve over the bigram model?

Straight from Karpathy's exercise recommendations at the end of the makemore video.

## What you should end with

- A working PyTorch notebook that:
  1. Loads `names.txt`
  2. Constructs trigram training pairs — `(char_1, char_2) → char_3`
  3. Feeds them through a small neural net (embedding or one-hot of a pair → linear → softmax)
  4. Trains it with cross-entropy loss
  5. Reports the final **training loss** and **validation loss**
- A comparison sentence: "my trigram loss is X; my bigram loss was Y; trigram improved by Z%."

## Hints (if you want them)

<details>
<summary>Hint 1: How to represent a pair of characters?</summary>

You have 27 characters (26 letters + `.`). A pair of characters has 27×27 = 729 possible values.

Two equivalent approaches:
- **One-hot**: concatenate two one-hot vectors of size 27 → input is a 54-dim vector
- **Index**: map each pair `(a, b)` to a single integer `a * 27 + b`, then use a 729-dim one-hot or an embedding lookup

Either works. The embedding approach prepares you for what Karpathy does in the next video.

</details>

<details>
<summary>Hint 2: Train/val split</summary>

Shuffle your trigrams and split 90/10 into train and val. Report both losses. The gap tells you if you're overfitting.

</details>

<details>
<summary>Hint 3: Expected loss</summary>

If you do this right, trigram loss should beat bigram loss. The exact number depends on your architecture, but it should be noticeably lower. If your trigram is *worse*, you have a bug.

</details>

## Work in the notebook

Open `notebook.ipynb` in this directory. The data loader scaffold and an evaluation cell are ready. Fill in the model and training loop.

## Checklist

- [ ] Wrote the data loader for trigrams
- [ ] Defined the neural-net architecture
- [ ] Trained to convergence (loss stopped decreasing)
- [ ] Recorded train + val loss
- [ ] Compared to the bigram result — wrote the one-line comparison
- [ ] Sampled some names from the trigram model (they should sound slightly more name-like than bigram samples)

## My results

- Bigram val loss: `___`
- Trigram val loss: `___`
- Improvement: `___%`
- Sample names:
  ```

  ```

## My notes

```

```

## Next

**[[../04-makemore-mlp/index|4.4 Makemore MLP →]]**
