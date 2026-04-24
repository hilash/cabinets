---
title: 4. Hands-On (Karpathy)
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - karpathy
  - hands-on
  - stage-4
order: 5
icon: 🏗️
---

# 🏗️ Stage 4 — Hands-On (Karpathy's Zero to Hero)

**Time:** 12 hours of video + 5 hours of exercises = **17 hours**, the biggest stage in the course.
**Source:** Andrej Karpathy's *Neural Networks: Zero to Hero* playlist.

> Karpathy's videos are the LLM version of "NAND to Tetris". You start from nothing — a scalar autograd engine in pure Python — and end up training a small GPT-2 from scratch. By the end, you've built an LLM with your own hands.

## Ground rules for this stage

1. **Type the code yourself.** Do not copy-paste from his GitHub. Type it as he types it.
2. **Even if you've seen it before**, don't skip the early videos. They build on each other and the later videos assume the earlier code.
3. **Pause liberally.** When Karpathy says "try to figure out X yourself," *actually pause the video and try*.
4. **If a notebook exists for this section, use it.** Starter cells are already laid out.

## The path

| # | Section | Type | Time | Page |
|---|---|---|---|---|
| 4.1 | Micrograd — building an autograd engine | Watch | 2.5 h | [[01-micrograd/index\|Micrograd]] |
| 4.2 | Makemore bigram | Watch | 2 h | [[02-makemore-bigram/index\|Makemore 1]] |
| 4.3 | **Trigram exercise** | Do | 1 h | [[03-trigram-exercise/index\|Trigram]] |
| 4.4 | Makemore MLP | Watch | 1 h | [[04-makemore-mlp/index\|Makemore 2]] |
| 4.5 | **MLP tuning exercise** | Do | 0.5 h | [[05-mlp-tuning/index\|Tune MLP]] |
| 4.6 | Activations + BatchNorm | Watch | 2 h | [[06-activations-batchnorm/index\|Makemore 3]] |
| 4.7 | Becoming a Backprop Ninja | Watch + Do | 2.5 h | [[07-backprop-ninja/index\|Makemore 4]] |
| 4.8 | WaveNet | Watch | 1 h | [[08-wavenet/index\|Makemore 5]] |
| 4.9 | Let's build GPT | Watch | 2 h | [[09-build-gpt/index\|Build GPT]] |
| 4.10 | **GPT addition exercise** | Do | 3 h | [[10-gpt-addition/index\|GPT Addition]] |
| 4.11 | Let's build the GPT Tokenizer | Watch | 2 h | [[11-gpt-tokenizer/index\|Tokenizer]] |

**Four exercises are marked bold.** Those are where you produce something. Everything else is watching-while-typing.

## Setup

```bash
pip install torch numpy matplotlib jupyter
```

For the Makemore sections, get the names.txt dataset (Karpathy links it in the video; `wget https://raw.githubusercontent.com/karpathy/makemore/master/names.txt` works too).

For the Build GPT section, Karpathy uses `input.txt` (Tiny Shakespeare).

## What you'll have built by the end

- An autograd engine from scratch (micrograd)
- A bigram language model
- A trigram language model (your exercise)
- An MLP-based character language model
- A GPT-2-like transformer, trained on Shakespeare
- A BPE tokenizer like GPT-2's

## Checklist

- [ ] All 11 section pages fully ticked
- [ ] All 4 bolded exercises completed with working notebooks
- [ ] Can explain in one sentence what `micrograd.Value` does
- [ ] Can draw a transformer block and label every component
- [ ] Can beat Karpathy's val loss of 2.2 on the MLP task

## Next

**[[../05-research-paper/index|Stage 5: Research Paper →]]**
