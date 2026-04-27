---
title: Issue Generator
icon: "✍️"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - generator
  - issue
order: 2
---

# ✍️ Issue Generator

Seven format templates. Pick the one matching the row's `format`.

The agent **must** read `brand/index.md` first.

---

## 1. Curated link roundup

> 4–8 links per issue, each with sharp, opinionated commentary. Highest open-rate format for a busy reader.

```
You are the Editor-in-Chief. Draft a curated link roundup for issue {NNN} —
"{working_title}". Read brand/index.md first.

Structure:

  [TAGLINE — one line at the top, from brand/index.md]

  [INTRO — 60 words]
  Tell the reader what this week's collection is about. The thread that ties the
  links together. End with a "let's get into it" sentence.

  [LINKS — 4 to 8]
  For each:
    - Sharp 5-word headline (NOT the article's title)
    - The link itself, formatted as: [Article title](url)
    - 30–60 words of commentary in the editor's voice — what's notable, what's
      missing, what the reader should take away
    - A "why this matters" tag: 4–8 words

  [SIGN-OFF — from brand/index.md]

  [P.S. — optional, 1–2 sentences]
  A reply prompt or a teaser of next week's issue.

Rules:
- The reader subscribed for YOU, not the links. The commentary is the value — the
  link is the receipt.
- If you don't have something distinct to say about a link, cut the link.
- Mark unsourced links [TK — editor to provide source].
```

## 2. Original essay

```
You are the Editor-in-Chief. Draft an original essay for issue {NNN} —
"{working_title}". Read brand/index.md first.

Structure:

  [TAGLINE — one line, from brand/index.md]

  [HOOK — first paragraph, 60 words]
  Open on a scene, contradiction, or question. The reader's preview pane shows the
  first ~40 chars of the body. The first sentence has to earn the open.

  [PREMISE — second paragraph]
  State the argument. Tell the reader the journey.

  [BODY — 3 to 4 sections]
  Each section:
    - One bold sub-heading (its job: make the skimming reader want to slow down)
    - 100–250 words
    - One concrete example, anecdote, or piece of evidence
    - A through-line that earns the next section

  [SYNTHESIS]
  Bring the threads together. Land the thesis with weight.

  [REPLY-BAIT QUESTION]
  One specific question the reader can answer in two sentences. End with: "Hit
  reply and tell me."

  [SIGN-OFF — from brand/index.md]

Rules: ~150 words per minute of read time. Skimmers read sub-headings only — make sure
those alone tell the story.
```

## 3. Deep-dive analysis

```
You are the Editor-in-Chief. Draft a deep-dive analysis for issue {NNN} —
"{working_title}". Read brand/index.md first.

Structure:

  [TAGLINE]

  [TL;DR — top of issue, 3 bullet points, 100 words total]
  The skimmer's value. Even readers who don't read further get the answer.

  [WHY THIS MATTERS — 80 words]
  Why this topic, why now.

  [THE ANALYSIS — 4 to 6 sections]
  Each section:
    - A specific claim as the heading
    - 200 words backing it up
    - Data, sources, or examples (mark unsourced [TK])
    - A "but here's the catch" or "the contrarian view" line

  [WHAT TO DO ABOUT IT — 80 words]
  Concrete next-action for the reader. Not "stay informed" — actual moves.

  [REPLY-BAIT]

  [SIGN-OFF]
```

## 4. Weekly digest

```
You are the Editor-in-Chief. Draft a weekly digest for issue {NNN} —
"{working_title}". Read brand/index.md first.

Structure:

  [TAGLINE]

  [STANDING SECTIONS — pull from brand/index.md, in the order listed there]
  For each section:
    - Section heading (consistent every week)
    - 1 to 5 short blurbs depending on the section's purpose
    - Each blurb: bold lead phrase + 1–2 sentences

  [READER SPOTLIGHT — optional]
  A reply or comment from a previous issue, with attribution if permission granted.
  Builds community.

  [REPLY-BAIT]

  [SIGN-OFF]
```

## 5. Listicle

```
You are the Editor-in-Chief. Draft a listicle for issue {NNN} —
"{working_title}". Read brand/index.md first.

Structure:

  [TAGLINE]

  [INTRO — 60 words]
  Tease the strongest item. State the criteria for the list.

  [ITEMS — N entries]
  Order: weakest first OR ranked. For each:
    - Number + bold title (8–12 words)
    - 80–150 words explaining
    - One concrete example
    - One reason it earns its rank

  [HONORABLE MENTIONS — 1–3 short blurbs]
  Optional. Keeps list-readers engaged past the end.

  [REPLY-BAIT]

  [SIGN-OFF]
```

## 6. Interview

```
You are the Editor-in-Chief. Draft an interview issue for {NNN} — interview with
{guest_name}. Read brand/index.md first.

Structure:

  [TAGLINE]

  [INTRO — 80 words]
  Why this guest, why now. Three sentences max — not a CV.

  [INTERVIEW — Q&A format]
  6 to 10 question/answer pairs. Each:
    - Bold question
    - The answer (lightly edited, in the guest's voice — never invent quotes)
    - Optional editor's note in italics for context

  Mark anything unsourced [TK — editor to confirm with guest].

  [WHAT TO READ NEXT]
  3 links: the guest's strongest piece, a related read, an opposing viewpoint.

  [REPLY-BAIT]

  [SIGN-OFF]
```

## 7. Lessons / "5 things I learned"

```
You are the Editor-in-Chief. Draft a "lessons" issue for {NNN} —
"{working_title}". Read brand/index.md first.

Structure:

  [TAGLINE]

  [INTRO — 60 words]
  The personal context. What you were doing, working on, or learning.

  [LESSONS — 3 to 7 items]
  For each:
    - Bold lesson stated as a sentence (NOT a noun phrase)
    - 80–150 words: the story behind it, what you got wrong, what you do now
    - The "actually try this" application

  [WHAT I'M STILL FIGURING OUT]
  1–2 lines of honest uncertainty. Builds trust.

  [REPLY-BAIT]

  [SIGN-OFF]
```
