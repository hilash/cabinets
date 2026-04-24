---
title: 4.11 GPT Tokenizer
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - karpathy
  - tokenizer
  - bpe
order: 11
icon: 🔡
---

# 🔡 4.11 — Let's build the GPT Tokenizer

**Time:** 2 hours of video.
**Title:** *Let's build the GPT Tokenizer.*

Everything you've built so far has used character-level tokenization: one token = one character. Real LLMs don't do that — they use **byte-pair encoding (BPE)**. This video builds GPT-2's tokenizer from scratch.

## Watch

<iframe width="720" height="405" src="https://www.youtube.com/embed/zduSFxRajkE" title="Let's build the GPT Tokenizer" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Direct link: [Let's build the GPT Tokenizer — YouTube](https://youtu.be/zduSFxRajkE)

## Why this matters

Most of the weirdness people blame on LLMs is tokenizer weirdness:

- Why LLMs can't spell certain words
- Why they can't reliably count characters in a word
- Why arithmetic gets worse for certain number ranges
- Why code LLMs handle tabs vs. spaces so differently

Understanding the tokenizer is understanding these failure modes.

## Key concepts introduced

- **Byte-pair encoding (BPE)** — start from bytes, iteratively merge the most common adjacent pair, repeat
- The **merges table** and the **vocab** — two ways of looking at the same training process
- **Regex pre-tokenization** — GPT-2 splits text on a specific regex before BPE to keep word boundaries clean
- Special tokens: `<|endoftext|>`, `<|im_start|>`, etc.
- Encoding vs. decoding — and why decoding after a partial stream can fail at the boundary
- **Unicode, UTF-8, and the footguns** therein — emojis, combining characters, script mixing

## Pay extra attention at these moments

- The live training demo on a short string — watch the merges grow step by step
- The discussion of sentencepiece, tiktoken, and the mess of tokenizer libraries in the wild
- The "glitches" section — trick prompts that exploit tokenizer edge cases (`SolidGoldMagikarp`, trailing spaces, etc.)

## Checklist

- [ ] Watched the full video, typing along
- [ ] Implemented a basic BPE trainer from scratch on a small corpus
- [ ] Implemented `encode` and `decode` for my BPE tokenizer
- [ ] Understand GPT-2's regex pre-tokenization pattern
- [ ] Can explain why LLMs struggle with character-level questions
- [ ] Tested: tokenize a simple English sentence with my BPE, then with `tiktoken`, and compare

## My notes

```

```

## 🎉 Stage 4 complete

If all 11 sections are fully ticked, you have built, from absolute scratch:

- A scalar autograd engine (micrograd)
- A character-level bigram, trigram, MLP, and WaveNet language model
- A small GPT-2 transformer trained on Shakespeare
- A GPT that does arithmetic
- A BPE tokenizer

That is not a small thing. Take five minutes, reflect, and then go to the final stage.

## Next

**[[../../05-research-paper/index|Stage 5: Research Paper →]]**
