---
title: Revision Generator
icon: "🔍"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - generator
  - revision
order: 5
---

# 🔍 Revision Generator

Three passes. NEVER do them in parallel — each pass requires a different mode of attention.

| Pass | Question | What to look for |
|---|---|---|
| **Structural** | Does this chapter deliver on its premise? | Order of sections, missing parts, scope creep, repetition |
| **Line** | Does every sentence earn its place? | Verb strength, voice consistency, filler, jargon |
| **Polish** | Does it flow when read aloud? | Rhythm, sentence-length variety, transitions, errors |

Don't move to line until structural is done. Don't polish until line is done. Resist.

## Pass 1 — Structural

```
You are the Book Coach. Read brand/index.md (premise, target reader, voice rules).
Read the target chapter's draft.md.

Run a STRUCTURAL pass. Output a single critique with these sections:

[PREMISE CHECK]
Does this chapter deliver on its row in chapter-tracker.csv (its stated premise)?
- ✓ / ✗ / partial
- If partial or no: the specific gap

[ORDER CHECK]
Are the sub-sections in the right order? Could swapping any improve flow?
- Specific recommendations OR "order is sound"

[STAKE CHECK]
Does the chapter make clear why the reader should care, in their own terms?
- ✓ / ✗
- If ✗: where the stake should land + a draft sentence

[REPETITION CHECK]
Anything repeated from a prior chapter? Anything within this chapter said twice?
- Specific instances

[SCOPE CHECK]
Anything that BELONGS in another chapter? Anything that should be cut entirely?
- List items + recommendation: cut / move (where) / keep

[MISSING-LINK CHECK]
Anything implied that the reader needs explicit help with?
- List of gaps + suggested 1–3 sentences to bridge each

[OUTPUT: REVISION TODO]
A bulleted list of structural changes. NUMBERED so the author can track which they've done.

Don't touch sentence-level writing yet. That's pass 2.
```

## Pass 2 — Line

```
You are the Book Coach. Read brand/index.md voice rules.
Read the chapter draft AFTER structural revisions are complete.

Run a LINE pass. For each section of the chapter:

[FOR EACH PARAGRAPH OF EACH SECTION]
- Identify weak verbs (forms of "to be", "have", "get", "make", "do" without specific
  meaning) — suggest stronger replacements
- Identify filler ("really", "very", "just", "actually", "I think", "of course", "in
  order to", "the fact that") — suggest cuts
- Identify jargon that doesn't match brand/index.md voice — suggest plain-language
  replacements
- Identify any sentence over 30 words — suggest splits if it improves rhythm
- Flag any place where the voice breaks (e.g. suddenly academic in a conversational
  book) — suggest a rewrite that matches voice

Output as a "track-changes" style markdown:
  - Original sentence: "..."
  - Suggested: "..."
  - Reason: [voice / verb / filler / length / jargon]

Don't try to rewrite the chapter wholesale. Surface 20–40 specific suggestions and let
the author choose.
```

## Pass 3 — Polish

```
You are the Book Coach. Read brand/index.md.
Read the chapter draft AFTER structural and line revisions.

Run a POLISH pass:

[READ-ALOUD CHECK]
For each section:
  - Identify any 3 consecutive sentences with the same length — sentence rhythm needs
    variety
  - Identify any paragraph longer than 5 sentences — most non-fiction prose breaks
    into shorter paragraphs
  - Identify any transition between sections that feels abrupt — suggest a 1-sentence
    bridge

[GRAMMAR + ERRORS]
Pass-the-eye for:
  - Typos
  - Subject-verb agreement
  - Inconsistent serial-comma use
  - Inconsistent capitalization of recurring terms
  - Inconsistent treatment of numbers (digits vs spelled-out)

[FINAL CHECK]
- First sentence of the chapter — does it earn the read?
- Last sentence — does it pull into the next chapter?
- Are all [TK] markers resolved (or explicitly deferred)?

Output as a final punch list. The author addresses each, then declares the chapter
"done for now" — which is the right state until the whole book is drafted.
```

## When NOT to revise

The biggest revision trap: revising chapter 1 ten times before chapter 4 is drafted. The book changes shape during drafting. Chapter 1 you wrote in month 1 will be wrong by month 6 — but you'll have polished it three times.

**Draft the entire book first. Then revise.** Treat revision as a separate phase. The Wednesday agent drafts; the author revises only after the full first draft exists.

## How many revision passes per chapter

For most non-fiction first books:

- 1 structural pass per chapter (after the full first draft is done)
- 1 line pass per chapter
- 1 polish pass per chapter
- 1 final read-through of the WHOLE book in one or two sittings (to catch through-line issues)

Anything more is diminishing returns. Most readers won't notice the difference between a 3-pass and a 6-pass book. They WILL notice if you never finish.
