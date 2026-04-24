---
title: 4.2 Makemore — Bigram
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - karpathy
  - makemore
  - language-model
  - bigram
order: 2
icon: 🔤
---

# 🔤 4.2 — Makemore: bigram language model

**Time:** 2 hours of video.
**Title:** *The spelled-out intro to language modeling: building makemore.*

You trained a neural net in the last video. Now you'll use one to model a *probability distribution* — specifically, a bigram language model over names.

## Watch

<iframe width="720" height="405" src="https://www.youtube.com/embed/PaCmpygFfXo" title="The spelled-out intro to language modeling: building makemore" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Direct link: [Building makemore — YouTube](https://youtu.be/PaCmpygFfXo)

## What you build

Two versions of a bigram character language model on `names.txt`:

1. **Counting-based**: just tally how often each character follows each other character. Normalize into a distribution per row. No neural net.
2. **Neural-net-based**: same outputs, but learned via gradient descent on a one-hidden-layer neural net.

Then compare: do they agree? (They should, roughly.)

## Key concepts introduced

- Character-level tokenization with a special `.` start/end token
- **One-hot encoding** of discrete inputs
- **Softmax** on the output layer to get a distribution over next characters
- **Cross-entropy loss** (equivalent to negative log-likelihood)
- Why the counting model and the NN converge to similar answers
- **Model smoothing** (add-one / add-epsilon) and what it prevents

## Get the data

```bash
wget https://raw.githubusercontent.com/karpathy/makemore/master/names.txt
```

32,000+ first names. You'll use this dataset for sections 4.2 through 4.8.

## Work with the starter notebook

Open `notebook.ipynb` — it has the data loader scaffolding and checkpoints for counting vs. neural versions.

## Checklist

- [ ] Watched the full video, typing along
- [ ] Built and sampled from the counting bigram model
- [ ] Built and trained the neural-net bigram model
- [ ] Confirmed both models produce similar-quality name samples
- [ ] Can explain why cross-entropy = -log(P[correct]) averaged over the batch
- [ ] Understand the role of `.` as start/end token

## My notes

```

```

## Next

**[[../03-trigram-exercise/index|4.3 Trigram exercise →]]** — time to ship your first model.
