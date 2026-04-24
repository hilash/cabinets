---
title: AI Hero
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - course
  - ai
  - llm
  - self-paced
order: 1
icon: 🦸
---

# 🦸 AI Hero

> **A complete, interactive course on AI.** Start with a single neuron, end with your own GPT. Math, intuition, theory, and hands-on construction — at your own pace.

You will cover the math, develop intuition for the architecture, and build an LLM from the ground up — starting with a perceptron in pure Python, finishing with your own GPT in PyTorch, and closing with a research paper you can read critically.

## How long will this take?

**~20 hours** of focused work. Plan ahead — do it in small chunks so things sink in. Interactive webapps, embedded videos, and live notebooks make every concept something you can poke at, not just read about.

## The 5 Stages

| # | Stage | Video | Exercise | Total |
|---|---|---|---|---|
| 1 | 🧮 **Math Prerequisites** | 4 h | — | 4 h |
| 2 | 🧠 **Intuition** | 3 h | — | 3 h |
| 3 | 📜 **Academic Theory** | 1 h | 1 h | 2 h |
| 4 | 🏗️ **Hands-On** (Karpathy) | 12 h | 5 h | 17 h |
| 5 | 🔍 **Research Paper** | — | 1 h | 1 h |

> 20 h is the video-at-1x estimate. 2x is often fine. Exercise time is the floor — go deeper if you have it.

## Start here

1. Read **[[00-getting-started/index|How to use this cabinet]]** first — it explains the agents, the notebooks, and the progress system.
2. Open the **Dashboard** (left sidebar) to see your progress at a glance.
3. Work through the stages in order. Each stage links to the next.

## The stages

- 🧮 [[01-math-prerequisites/index|1. Math Prerequisites]] — linear algebra, calculus, probability (4 h)
- 🧠 [[02-intuition/index|2. Intuition]] — 3Blue1Brown's neural network series (3 h)
- 📜 [[03-academic-theory/index|3. Academic Theory]] — survey of modern architectures (2 h)
- 🏗️ [[04-hands-on/index|4. Hands-On]] — Karpathy's Zero to Hero, from micrograd to GPT (17 h)
- 🔍 [[05-research-paper/index|5. Research Paper]] — read one paper critically (1 h)

## 🎛️ Interactive visualizations

Five live webapps, cabinet parchment theme, editorial typography. Play with them while you watch the videos.

- 📊 **[[dashboard/index|Dashboard]]** — your progress across all stages, with per-section bars
- 🗺️ **[[concept-map/index|Concept Map]]** — force-directed graph of 38 concepts, click any node to locate it in the course
- 🧠 **[[neuron-playground/index|Neuron Playground]]** — drag sliders for inputs + weights, watch a single neuron compute live with its activation curve
- 🎢 **[[gradient-descent/index|Gradient Descent]]** — drop a ball on a 2D loss landscape, tune LR and momentum, break it on purpose
- 👁️ **[[attention-viz/index|Attention Visualizer]]** — click tokens in a sentence, see the attention heatmap light up, toggle the causal mask

## Your team

Four agents live in this cabinet — ask any of them anything. They are **not ChatGPT**: do not ask them to do your exercises for you. They are study partners, not spoiler machines.

- **🎓 Mentor** — plans your week, sets pace, flags when you're behind
- **📐 Math Tutor** — explains matrix ops, chain rule, probability intuitions
- **💻 Code Tutor** — reviews your notebook attempts; explains PyTorch + Python patterns
- **📊 Progress Tracker** — owns `progress/progress.csv` and the dashboard

## Ground rules

1. **Do exercises yourself.** Wrong attempts teach more than copying a solution.
2. **Type the code.** Do not copy-paste from Karpathy's videos. Your fingers need the reps.
3. **Write in the notes fields.** Each section has a "My notes" block. Future-you needs them.
4. **If you're stuck > 30 min**, ask the tutors — don't ask ChatGPT (it'll give you spoilers).

## When you finish

You should be able to:

- Write forward + backward pass of a small MLP by hand on paper
- Explain attention as a weighted-sum-over-values in one sentence
- Train a transformer from scratch on a toy problem
- Read an arXiv abstract and tell whether it's worth your time

Good luck. Ship it. 🚀
