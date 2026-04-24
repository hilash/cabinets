---
title: 2. Intuition
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - intuition
  - neural-networks
  - 3blue1brown
  - stage-2
order: 3
icon: 🧠
---

# 🧠 Stage 2 — Intuition

**Time:** 3 hours of video.
**Source:** 3Blue1Brown — Neural Networks series.
**Scope:** The entire playlist.

You just did the math. Now put it to work by *seeing* neural networks — gradient descent, backprop, the whole thing — rendered the way only Grant Sanderson can render them.

## If you're already an NN veteran

You can technically skip to video 4, but we recommend at least the extra 15 minutes on 2x as a reminder. Concepts in 3B1B's framing will come back when Karpathy builds them in code. Matching the two framings in your head is the win.

## Watch

<iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi" title="3Blue1Brown — Neural Networks" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Direct link: [3Blue1Brown — Neural Networks playlist](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)

## 🎛️ Play with the ideas

Two interactive webapps live alongside this stage. Open them in the sidebar as you watch:

- **[[../neuron-playground/index|Neuron Playground]]** — drag sliders for inputs, weights, and bias. Watch the dot product + bias + activation fn compute live, with the activation curve highlighted at your current point. Swap between tanh, sigmoid, ReLU, identity.
- **[[../gradient-descent/index|Gradient Descent simulator]]** — drop a ball on a 2D loss landscape. Adjust learning rate and momentum. Break it on purpose — see what a too-large LR does. Try the "valley" landscape with momentum off, then on.

These make the geometric pictures in the 3Blue1Brown videos concrete. A minute on each saves ten minutes of confusion later.

## What you'll leave with

- A **geometric** picture of what a neuron does: dot product + bias + nonlinearity = "am I excited about this input?"
- A mental movie of **gradient descent** — marble rolling downhill in a high-dimensional loss landscape
- The four equations of **backpropagation** — not by symbol, but by the *idea* of credit assignment from output back to input
- What attention does (if the playlist covers it) — and why it became the backbone of modern LLMs

## Prompts to test yourself

If you can't answer these in a sentence, rewatch the relevant segment:

1. In plain English: what does a single neuron compute?
2. Why do we need a nonlinearity between layers? What happens without one?
3. What is a loss function *measuring*?
4. During backprop, the gradient "flows backward." What specifically is flowing?
5. If the gradient is small at a layer, what happens to training of layers upstream of it?

## Checklist

- [ ] Watched video 1 (What is a neural network?)
- [ ] Watched video 2 (Gradient descent)
- [ ] Watched video 3 (Backpropagation)
- [ ] Watched video 4 (Backprop calculus)
- [ ] Watched remaining videos in the playlist (attention, transformers, etc.)

## My notes

```

```

## Next

**[[../03-academic-theory/index|Stage 3: Academic Theory →]]**
