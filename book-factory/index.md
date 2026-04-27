---
title: Book Factory
icon: "📖"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - book
  - writing
  - template
order: 1
---

# 📖 Book Factory

> A complete book-writing OS in a directory. Fill in three placeholders, run the bootstrap prompt, and your `Book Coach` agent builds your premise sheet, a 12-chapter outline, drafts chapter 1, generates cover-art prompts and a back-cover blurb, and recommends a publishing path tuned to your goals.
>
> Designed for non-fiction. Adaptable to memoir.

---

## ⚡ Bootstrap your Book OS

**Step 1.** Fill in the three placeholders below.

**Step 2.** Open the AI panel on this page. Paste the prompt block. Run.

**Step 3.** Wait. The agent writes `brand/index.md`, generates a 12-chapter outline in `chapter-tracker.csv`, drafts `chapters/001-introduction/draft.md`, generates a cover-art brief, drafts the back-cover blurb, and recommends a publishing path.

```
You are the Book Coach agent for this Book Factory cabinet. The author has just filled in
the "Onboarding" section of index.md.

Read those answers. Then build out the cabinet in this exact order:

1. Write `brand/index.md`. Lock in: book working title, one-line premise (ONE problem
   for ONE reader that this book uniquely solves), target reader (specific), book
   archetype (argument / framework / narrative / how-to / reference), target word
   count (typically 50,000–80,000 for non-fiction), target chapter count (typically
   10–14), chapter length norm (~5,000 words), tone, voice rules (5 do's and 5
   don'ts), the "one thing" the reader will be able to do or believe after, the
   competing books that already exist (and how this one is different), three-word
   brief.

2. Generate a 12-chapter outline in `chapter-tracker.csv`. Number them 001–012. Each
   row gets chapter_number, working_title, premise (one sentence: what the chapter
   delivers to the reader), archetype_within (story-led / argument-led / how-to /
   case-study / synthesis), target_words (~5,000), status=`outlined`. Chapter 001 is
   the introduction (sets the premise + earns trust). The final chapter is the
   synthesis + "what now". Chapters between move the reader through the argument or
   journey.

3. Draft `chapters/001-introduction/draft.md` using `generators/chapter-generator.md`.
   The introduction earns the reader's commitment to the rest of the book. Mark all
   personal anecdotes as `[TK — author's story]`.

4. Draft `chapters/001-introduction/notes.md` with a "## Structural questions" section
   for the author to address (e.g. "Where in your life is the moment that proves the
   premise?").

5. Generate `cover-art/brief.md` using `generators/cover-art-generator.md`. Both the
   thumbnail-readable brief AND the full-cover brief.

6. Generate `cover-art/blurb.md` using `generators/blurb-generator.md`. The 150-word
   back-cover blurb + the 25-word elevator pitch.

7. Recommend a publishing path. Read `publishing-guide/index.md`. Append a
   "## Recommended publishing path" block to `brand/index.md` with a 1-line answer +
   2–3 lines of reasoning.

8. Append "## ✅ Bootstrap complete — [YYYY-MM-DD]" to this index.md with what was
   built and the author's next steps.

Rules:
- Use ONLY what the author wrote in Onboarding. Do not invent biography, anecdotes,
  or expertise.
- If a placeholder is empty or vague, ask the author. Do not guess the premise.
- Do not modify `publishing-guide/`, `writing-guide/`, or `generators/`.
```

---

## 🧩 Onboarding — fill these in

### 1. Who are you?

> _Name. What you do. Why YOU specifically can write THIS book — your specific experience, credential, or perspective that nobody else has. "I spent 12 years as a cardiac ICU nurse and have seen 200+ deaths up close — I'm writing about how to talk to dying people because most resources for that are written by people who haven't" beats "I'm a healthcare worker who wants to write."_

```
_________
```

### 2. What is the book about?

> _The premise: ONE problem for ONE specific reader that this book uniquely solves. The target reader (specific — "early-career engineering managers in their first 6 months of the role" beats "managers"). The ONE thing the reader will be able to do or believe after they finish. The book archetype (argument / framework / narrative / how-to / reference). What this book is NOT (lock the scope). Two competing books that already exist + how this one is different._

```
_________
```

### 3. What format and audience?

> _Target word count (50,000 / 65,000 / 80,000 are typical). Target chapter count (10–14 standard). Tone (academic / journalistic / conversational / personal-essay / hybrid). Publishing path you're considering (KDP self-pub / hybrid press / agent + traditional / unsure). Time you can spend writing per week (be realistic). Your platform / audience size (newsletter, social following, etc. — affects publishing-path recommendation). Three words readers should use to describe this book. Three words it must never sound like._

```
_________
```

---

## 📚 What is in this cabinet

| Page | What it is |
|---|---|
| [[brand/index]] | Premise sheet + voice spec — populated by bootstrap |
| `chapter-tracker.csv` | The chapter pipeline — interactive table |
| [[chapters/index]] | Chapter catalog + reusable template |
| [[generators/index]] | Chapter, cover-art, blurb, revision generators |
| [[writing-guide/index]] | Daily practice, beating writer's block, the messy middle |
| [[publishing-guide/index]] | KDP / IngramSpark / Draft2Digital / hybrid / traditional |

## 🤖 Your team

- **📖 Book Coach** — premise discipline, chapter drafting, voice consistency, publishing recs. Runs Mondays for the progress check. Runs Wednesdays to draft the next chapter.

## 🔁 What runs on a schedule

- **Weekly Progress Check** — Monday 9am. Drift flags + the ONE chapter to focus on.
- **Weekly Chapter Prep** — Wednesday 10am. Drafts the next un-drafted chapter.

## 🚀 After the bootstrap

1. Read `brand/index.md`. The premise is your North Star — every chapter answers to it.
2. Read chapter 1 in `chapters/001-introduction/draft.md`. Read aloud. Mark every `[TK — author's story]` and replace with your real anecdote.
3. Read `cover-art/blurb.md`. If the blurb sounds boring, the premise needs sharpening — fix the premise first.
4. Look at the recommended publishing path in `brand/index.md`. Read the corresponding deep-dive in [[publishing-guide/index]].
5. Wednesday agent drafts chapter 2. You revise chapter 1 in parallel.
