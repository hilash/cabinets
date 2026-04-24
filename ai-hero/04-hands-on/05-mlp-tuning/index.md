---
title: 4.5 MLP Tuning Exercise
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - karpathy
  - exercise
  - tuning
  - hyperparameters
order: 5
icon: 🎯
---

# 🎯 4.5 — Exercise: Beat Karpathy's 2.2

**Time:** 30 minutes.
**Type:** Exercise. Hyperparameter tuning, nothing more.

## The brief

> Tune the hyperparameters of the MLP training to **beat Karpathy's best validation loss of 2.2**.

That's it. Same architecture, same data, same loss function. Just make it work better.

## Levers you can pull

| Lever | Safe range to explore |
|---|---|
| Block size (context chars) | 3 → 5 → 8 |
| Embedding dimension | 10 → 20 → 50 |
| Hidden layer size | 200 → 300 → 500 |
| Number of hidden layers | 1 → 2 |
| Batch size | 32 → 64 → 128 |
| Learning rate | Use the LR finder; typically `0.1` early, `0.01` late |
| Training steps | 50k → 200k |
| Weight initialization | He/Xavier |

## Rules

1. **Track every experiment.** One row per run in the table below.
2. **Don't touch the val set mid-experiment.** Decide on a val set, stick with it.
3. **Don't train on the val set, obviously.**
4. **Report the seed.** Reproducibility is table stakes in ML.

## Experiment log

Fill this in as you run experiments. Keep the winner highlighted.

| Run | Block | Emb | Hidden | LR | Steps | Val loss | Notes |
|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  | baseline |
| 2 |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |  |

## Stop conditions

- Beat 2.2 → ✅ done
- Plateau above 2.2 for 5+ experiments → you have a bug or a bad design choice. Ask the Code Tutor.
- Wasted 30+ minutes → move on. This isn't Kaggle.

## Checklist

- [ ] Reproduced Karpathy's baseline and confirmed my val loss is close to his 2.2
- [ ] Ran at least 3 tuning experiments
- [ ] Beat 2.2 on the val set
- [ ] Recorded the winning configuration below
- [ ] Did NOT touch the test set

## Winning config

```
block_size   = ___
emb_dim      = ___
hidden       = ___
lr_schedule  = ___
steps        = ___
val_loss     = ___
```

## My notes

```

```

## Next

**[[../06-activations-batchnorm/index|4.6 Activations + BatchNorm →]]**
