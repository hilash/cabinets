---
title: Lesson Generator
icon: "✍️"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - generator
  - lesson
order: 2
---

# ✍️ Lesson Generator

Every lesson follows the same loop. Don't deviate without reason — students rely on the structure being predictable.

## Generator prompt

```
You are the Course Creator. Read brand/index.md (transformation, voice, lesson length norm)
and the target module's row in module-tracker.csv (working_title, learning_outcome,
sub_lesson_count).

Output the FULL lesson for this module. The module breaks down into N sub-lessons (where N
matches sub_lesson_count). For EACH sub-lesson, produce:

[SUB-LESSON N.X — title]

  Target length: ~[brand/index.md lesson length norm] minutes

  ## HOOK (15–30 seconds)
  Open on a question, problem, or contradiction. NEVER on "Welcome to lesson 3" or
  "In this lesson we'll be covering". The hook earns the first 30 seconds — without it,
  drop-off begins immediately.

  ## OUTCOME (15 seconds)
  One sentence: "By the end of this lesson, you'll be able to [verb + observable thing]."

  ## EXPLANATION (3–5 minutes)
  The minimum vocabulary and concept needed for this lesson's outcome. Cut everything else.
  Mark every claim/example. Use these markers:
    [TEXT: "key term"]    — show on-screen
    [DIAGRAM: description] — visual aid needed
    [DEMO: what to show]   — screen-share / live action
    [TK — citation]        — claim that needs source

  ## WORKED EXAMPLE (3–5 minutes)
  Solve ONE concrete instance. Narrate the decisions — "I'd usually try X first, but
  here's why X breaks…" — that's the gold. Don't just present the solution; show the
  thinking that produces it.

  ## PRACTICE (1–2 minutes of instruction → student does the exercise on their own time)
  State the exercise. State the expected output. State the success criteria.
  Practice prompts go in `practice.md` separately, but in the lesson you set them up.

  ## BRIDGE (15 seconds)
  ONE sentence into the next sub-lesson. Earn the click.

[END SUB-LESSON]

Repeat for all sub-lessons in the module.

After all sub-lessons, output:

[MODULE WRAP — 1 minute, only at the end of the FINAL sub-lesson in this module]
- Quick recap: what the student can now do
- One concrete win: a specific thing they should be able to point to as evidence
- Bridge to the next module

Rules:
- Read every line aloud silently. If it sounds like a textbook, rewrite for spoken delivery.
- ~150 words per minute target.
- Mark anything you don't have source for as [TK — creator to verify].
```

## Length discipline

Course lessons that run long lose students. Lesson length norms:
- Welcome / introductions: 8–15 min
- Concept lessons: 8–12 min each
- Worked-example lessons: 10–15 min
- Skill-application lessons: 12–20 min
- Synthesis / capstone: 15–25 min

If a sub-lesson can't fit its scope in the target time, **split it**. Two 10-minute lessons beat one 20-minute lesson on completion rate.

## Re-record vs edit

You'll record an imperfect take and want to re-record. Don't — unless:
- The audio is unusable
- A factual error is in the script
- The energy is dead

A B-grade take of a great lesson beats an A-grade take of a perfectly polished filler. Ship.
