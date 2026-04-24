---
title: 4.6 Activations & BatchNorm
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - karpathy
  - batchnorm
  - activations
  - initialization
order: 6
icon: 📈
---

# 📈 4.6 — Makemore Part 3: Activations, Gradients, BatchNorm

**Time:** 2 hours of video.
**Title:** *Building makemore Part 3: Activations & Gradients, BatchNorm.*

This is the "why does my deep network refuse to learn" video. Initialization, activation distributions, saturating tanh, and finally **batch normalization** as the hack that makes deep nets trainable.

## Watch

<iframe width="720" height="405" src="https://www.youtube.com/embed/P6sfmUTpUmc" title="Building makemore Part 3: Activations & Gradients, BatchNorm" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Direct link: [Makemore Part 3 — YouTube](https://youtu.be/P6sfmUTpUmc)

## Key concepts introduced

- **Initialization**: He/Kaiming init, Xavier/Glorot init, and why random Normal(0, 1) is often wrong
- **Saturation** of tanh/sigmoid — what "dead neurons" look like in a histogram
- **The chicken-and-egg of deep nets**: bad init → bad gradients → doesn't learn
- **Batch normalization**: normalize activations layer-by-layer to keep their distribution stable
- The running statistics for BN at eval time (`running_mean`, `running_var`)
- The bias parameter that BN makes redundant (you can drop the preceding linear's bias)

## Pay extra attention at these moments

- The **histograms of activations and gradients per layer** — Karpathy renders them. Pause and stare. A healthy deep net has similar distributions at every layer; a sick one has distributions that collapse or explode with depth.
- The moment he adds BatchNorm and the loss curve suddenly looks sane
- His manual implementation of BatchNorm — every line matters. Typing this one gives you the intuition for why BN works.

## A concept you'll return to

**Internal covariate shift** is the term for what BN is "fixing." It's a somewhat debated explanation (see the *Understanding BN* follow-up paper by Santurkar et al.), but for now: take the video's framing and internalize that the *distribution* of activations changing mid-training is bad.

## Checklist

- [ ] Watched the full video, typing along
- [ ] Implemented BatchNorm from scratch
- [ ] Plotted per-layer histograms of activations and gradients
- [ ] Confirmed that He init + BN makes my deep MLP train cleanly
- [ ] Can explain why we drop the bias on the linear layer immediately before BN
- [ ] Understand the difference between train mode and eval mode for BN

## My notes

```

```

## Next

**[[../07-backprop-ninja/index|4.7 Becoming a Backprop Ninja →]]** — no more `.backward()` for a while.
