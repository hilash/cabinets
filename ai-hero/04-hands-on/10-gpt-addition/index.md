---
title: 4.10 GPT Addition Exercise
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - karpathy
  - exercise
  - gpt
  - transformer
order: 10
icon: 🎯
---

# 🎯 4.10 — Exercise: Train a GPT to do addition

**Time:** 3 hours.
**Type:** The big exercise. You take the GPT you just built and teach it arithmetic.

## The brief (from Karpathy)

> Train a GPT that does addition of two numbers, i.e. `a + b = c`.
>
> You may find it helpful to predict the digits of `c` in **reverse order**, as the typical addition algorithm (that you're hoping it learns) would proceed right to left too.
>
> You may want to modify the data loader to simply serve random problems and skip the generation of `train.bin`/`val.bin`.
>
> You may want to **mask out the loss** at the input positions of `a + b` that just specify the problem, using `y=-1` in the targets (see `CrossEntropyLoss` `ignore_index`).
>
> **Does your Transformer learn to add?**

## What success looks like

A model that, given `12+345=`, produces `357` (or `753` if you went with reversed digits and decoded back).

Expect:

- **Simple regime first**: 2-digit + 2-digit. Should learn perfectly with enough data.
- **Harder regime**: 3-digit, 4-digit. Generalization starts to break down. Interesting.

## Design decisions you have to make

| Decision | Options |
|---|---|
| Vocabulary | Digits 0-9 plus `+`, `=`, padding. Tiny vocab (~13). |
| Data | Generate random problems on the fly. No file-based dataset needed. |
| Digit order of answer | Forward (`345`) vs. reverse (`543`) — try both, report which learns faster |
| Loss masking | Ignore loss on the problem-statement tokens; only penalize wrong digit predictions |
| Context length | Long enough for `a + b = c` in your chosen format. Compute the max. |
| Model size | Small GPT — `n_layer=4`, `n_head=4`, `n_embd=128` is a reasonable starting point |

## Hints (no spoilers — just directions)

<details>
<summary>How to format examples</summary>

A single example is a string like `"12+34=46<pad>"` tokenized char-by-char. During training, the targets at positions inside the answer are the next digit; targets at the problem-statement positions are `-1` (ignored).

</details>

<details>
<summary>The reverse-digit trick</summary>

Addition carries *right to left*. A left-to-right autoregressive model has to "know" the answer before starting to emit it — because digit 1 of the answer can depend on carries from digits further right.

If you train the model to emit digits of the answer in reverse (units first, then tens, etc.), the carry structure becomes natural. You decode by reversing the output at inference.

</details>

<details>
<summary>Debugging a model that's stuck at ~chance</summary>

- Print a batch. Are the targets what you expect? Is the loss mask correct?
- Overfit a batch of 4 examples. If you can't overfit, you have a model bug, not a data bug.
- Check the attention is causal. A non-causal mask lets the model cheat.

</details>

## Start in `notebook.ipynb`

Scaffold with a data generator, a minimal GPT import from section 4.9, and an evaluation harness that samples problems and reports accuracy.

## Checklist

- [ ] Wrote a random-problem data generator for addition
- [ ] Chose a digit order convention (forward or reverse) and stuck with it
- [ ] Masked loss on problem-statement tokens with `ignore_index=-1`
- [ ] Trained the model to convergence
- [ ] Evaluated on held-out problems — reported accuracy
- [ ] Tried generalization: train on 2-digit, test on 3-digit. What happens?

## My results

- Digit order chosen: `forward / reverse`
- 2-digit accuracy: `___%`
- 3-digit accuracy: `___%`
- Generalization from 2-digit train to 3-digit test: `___%`

## Observations

```

```

## My notes

```

```

## Next

**[[../11-gpt-tokenizer/index|4.11 GPT Tokenizer →]]** — the last Karpathy video.
