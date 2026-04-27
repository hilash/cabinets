---
title: Sales-Page Generator
icon: "💸"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - generator
  - sales
order: 4
---

# 💸 Sales-Page Generator

The sales page is where most courses die. Not because the page is bad — because the **transformation isn't sharp enough**. If the sales page is hard to write, the curriculum needs work, not the copy.

## Generator prompt

```
You are the Course Creator. Read brand/index.md (transformation, target student, price,
voice).

Generate a sales page in this exact structure:

# [HERO]

  [Headline — under 12 words, names the transformation]
  Example shape: "Go from [State A] to [State B] in [time]"

  [Sub-headline — under 25 words, adds specificity / urgency / proof]

  [CTA button — 2–4 words, action verb]

# [WHO THIS IS FOR]

  Direct address. 3 bullet points starting with "You're a..." that describe the target
  student in their own words.

  Then: "Skip this course if..." — 2 bullets that filter out wrong-fit students. This is
  not throwaway — it dramatically improves conversion among right-fit buyers.

# [THE TRANSFORMATION]

  Before / After contrast. Two columns:

  | Before this course | After this course |
  |---|---|
  | [Concrete State A statement] | [Concrete State B statement] |
  | [Pain point] | [Resolution] |
  | [Frustration] | [New capability] |

  3–5 rows. Use the language the student uses about themselves, not industry jargon.

# [WHAT YOU'LL LEARN]

  Modules-overview format. For each module:
    - Module N: [Name]
      One sentence: what the student can DO after this module.

  Use the syllabus from `module-tracker.csv`. Each entry: 1 line. No padding.

# [PROOF]

  ## Why me?
  3–4 bullets on the creator's relevant experience. Concrete, not generic. Mark as
  [TK — creator to fill in if not in brand/index.md].

  ## What past students say
  Reserve 3 testimonial slots. If first cohort hasn't run yet, mark [TK — collect after
  first cohort].

  ## Sample lesson
  Embed a 2–4 minute extract from the welcome lesson or a hero module. Marker:
  [SAMPLE LESSON — embed link to preview]

# [OBJECTION DESTROYERS]

  3–5 of the most common objections, in the student's own voice, with a real answer.

  Common ones to consider (pick the most relevant 3–5):
  - "I'm not sure I have time."
  - "I'm a beginner — is this too advanced?"
  - "I'm not a beginner — is this too basic?"
  - "What if it doesn't work for me?"
  - "Why this course over [free YouTube alternative]?"
  - "What if I get stuck?"
  - "Can I do this on my own time?" (for cohort)

  Each objection: 1–2 sentence answer that REFRAMES, not dismisses.

# [PRICE + GUARANTEE]

  Price reveal — be direct. No "investment" language unless the brand voice is corporate.

  If running a cohort: include the cohort dates explicitly.
  If self-paced: state lifetime access vs annual.

  Refund policy: state plainly. Most courses use 14-day or 30-day money-back. Cohort
  courses sometimes offer "complete the first week, decide if it's right".

# [FAQ]

  6–8 questions in the student's voice. Answer plainly. Avoid corporate hedging.

# [FINAL CTA]

  Repeat the hero headline + button. Optionally add: "Doors close [date]" or "Next
  cohort starts [date]" — only if true.

# [P.S. or "ONE LAST THING"]

  3–4 sentences in the creator's voice. Personal. Honest. Address the student who's
  on the fence — what would you say to them at a coffee shop?
```

## Pre-sell rule

Run this sales page BEFORE you build the rest of the course. Even at outline stage. If 5–10 people pre-pay (or join a wait-list with deposits), you have validation. If nobody does, the curriculum doesn't have product-market fit yet — fix that before producing 60 hours of video.

## Iteration

The sales page rewrites itself after the first cohort. Real testimonials replace `[TK]`s. Real before/after stories replace abstract language. By cohort 3, the page is mostly student voice — and that's when conversion really starts to compound.
