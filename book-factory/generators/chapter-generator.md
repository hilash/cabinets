---
title: Chapter Generator
icon: "✍️"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - generator
  - chapter
order: 2
---

# ✍️ Chapter Generator

Five archetypes. Pick the one matching the chapter's `archetype_within` column.

## Generator prompt

```
You are the Book Coach. Read brand/index.md (premise, voice, archetype, target reader)
and the target chapter's row in chapter-tracker.csv (working_title, premise,
archetype_within, target_words).

Write a full first draft for the chapter. Use the matching template below. Aim for ~target_words.

Throughout the draft:
  - Mark every personal anecdote slot as [TK — author's story]
  - Mark every unsourced claim as [TK — verify]
  - Mark every place a real example would land as [TK — example]
  - Match the voice rules in brand/index.md
  - DO NOT invent biographical details, quotes, or specific numbers about real people

[STORY-LED CHAPTER]

  HOOK (300–500 words)
  Open on a SCENE. Concrete, sensory, in time. The author or someone they know in
  a specific moment. End the hook on a question or contradiction that requires the
  rest of the chapter.

  STAKE (200–300 words)
  Why does this scene matter? What's at stake for the reader of THIS book?

  THE BODY (target_words minus other sections)
  3–5 sub-sections. Each sub-section:
    - Sub-heading (states a sub-claim)
    - 600–1200 words developing it
    - At least one concrete example or anecdote per sub-section
    - One transition that earns the next sub-section

  APPLICATION (200–400 words)
  What can the reader DO with this? Concrete next-action.

  BRIDGE (1 paragraph)
  Land on a question or claim that pulls into the next chapter.

[ARGUMENT-LED CHAPTER]

  HOOK (200–400 words)
  Open on a counter-intuitive claim, a question the reader has had, or a contradiction
  in conventional wisdom.

  THE THESIS (100–200 words)
  State the chapter's argument in one paragraph. The thesis should be specific enough
  that someone could disagree with it.

  THE CASE (target_words minus other sections)
  3–5 sub-sections, each defending part of the thesis:
    - Sub-claim as heading
    - 600–1200 words of argument
    - Evidence: stories, citations, examples (mark unsourced)
    - Counter-argument addressed (briefly — not all of it, but acknowledge tension)

  WHAT THIS MEANS (200–400 words)
  The implication. What follows from the thesis being true?

  BRIDGE (1 paragraph)

[HOW-TO CHAPTER]

  HOOK (200–300 words)
  The reader's pain point in their own words. The frustration that brought them here.

  STAKE (100–200 words)
  What does this skill unlock? What's the cost of not having it?

  THE PROCESS (target_words minus other sections)
  Step-by-step. Each step:
    - Step name (active verb)
    - 400–800 words explaining
    - Worked example
    - Common mistakes flagged
    - "How to know you've done it right" check

  PRACTICE (200–400 words)
  An exercise the reader can do today. Concrete prompt + expected output.

  BRIDGE (1 paragraph)

[CASE-STUDY CHAPTER]

  HOOK (200–400 words)
  Open INSIDE the case — a moment in the case-study story.

  CONTEXT (200–300 words)
  Who, when, what setting. Briefly.

  THE STORY (target_words minus other sections)
  Tell the case in chronological order. 3–5 acts. Each act:
    - What happened
    - The decision point
    - The choice made + the result
    - The lesson (one paragraph)

  THE GENERALIZABLE LESSON (300–500 words)
  Pull back. What does this case teach that applies beyond this case?

  BRIDGE (1 paragraph)

[SYNTHESIS / FINAL-CHAPTER]

  HOOK (200–300 words)
  Open with a moment that captures the book's premise.

  RECAP (300–500 words)
  Walk back through the spine of the book. NOT a summary of every chapter — the
  through-line. The single argument or journey the book made.

  THE INTEGRATED VIEW (target_words minus other sections)
  How does it all fit together? The thing that's true once you've read everything.

  WHAT NOW (300–500 words)
  Concrete moves the reader can make this week, this month, this year. From short
  to long horizon.

  CLOSE
  One last image, story, or line that gives the book a memorable ending. Earn the
  back-cover.

[Output the full draft using the matching template. End with a [WORD COUNT: ~X] line
and a [VOICE CHECK] section flagging any places you're uncertain whether the voice
matches brand/index.md.]
```

## Drafting beats research

The single biggest trap of first-time authors: spending a week researching when one hour of drafting would surface what they actually need to research. **Draft first. Mark `[TK]`. Research only what the draft proves you need.**

If you research before drafting, you'll find 10x more than you can use, plus you won't know which 10% of it actually matters until you've written the chapter around it.
