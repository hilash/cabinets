---
title: Script Generator
icon: "✍️"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - generator
  - script
order: 2
---

# ✍️ Script Generator

Five templates — one per format. Pick the one that matches the episode's `format` column in `content-calendar.csv` (which inherits from the default in `brand/index.md`).

**How to use a template:**

1. Open the AI panel on the target episode's `script.md`.
2. Copy the relevant prompt block below.
3. Paste, then fill in the bracketed `{episode_number}` and `{working_title}` (or just say "draft script for episode 003" — the Producer agent can find the row in the calendar).
4. Run.

The agent is required to first read [[../brand/index]] for tone, length, and segment structure. Don't restate those in the prompt — the brand page wins.

---

## 1. Solo monologue

> One host, one mic. Highest density per word. The script is mostly word-for-word.

```
You are the Producer. Write a full word-for-word solo script for episode {episode_number} —
"{working_title}".

Read brand/index.md first. Match the show's segment structure, length, and tone exactly.

Structure the script as:

  [COLD OPEN — 30 seconds]
  Open on a question, a scene, or a contradiction. Never on "Hi everyone".

  [HOOK — 1 minute]
  State the premise of the episode. Tell the listener exactly what they will get
  if they stay. Reference the show's three durable questions only if relevant.

  [BODY — segments per brand/index.md]
  Use the segment structure from brand/index.md. For each segment:
    - one signposting sentence ("ok, three things on this — first…")
    - the content, in spoken sentences
    - one transition sentence into the next segment

  [CALLBACK — 30 seconds]
  Tie back to the cold open. The listener should feel a loop closing.

  [CTA — 15 seconds]
  One ask. Subscribe, share, reply, or visit a link. Pick ONE.

Rules:
- Short sentences. Contractions. No list-of-six bullets in the script body.
- Read every sentence aloud in your head — if you wouldn't say it, cut it.
- Mark stage directions in [BRACKETS]: [PAUSE], [LAUGH], [SOUND CUE: x].
- Word count target: ~150 words per minute of target length.
```

---

## 2. Two-host conversation

> Two regulars. The script is a topic spine, not a transcript. You want chemistry, not recitation.

```
You are the Producer. Draft a conversation spine for episode {episode_number} —
"{working_title}". Two hosts — names per brand/index.md.

Read brand/index.md first.

Output:

  [COLD OPEN — 30 seconds]
  Word-for-word. One host opens with a scene, question, or hot take. The other reacts.

  [PREMISE — 1 minute]
  Word-for-word from one host. Sets up the episode.

  [TOPIC SPINE]
  3–5 topics, each with:
    - the topic question (1 line)
    - 3–5 bullet talking points (the host should not read these — they're prompts)
    - one "landmine" — something one host believes the other will disagree with
    - one "callback opportunity" — a memory, in-joke, or running thread to bring back

  [WRAP — word-for-word]
  Callback to the cold open. CTA — one ask only.

Do not write dialogue line by line for the body. Trust the hosts to talk. Your job is to
guarantee they don't run out of things to say or wander off-topic.
```

---

## 3. Interview (host + guest)

> Pre-interview prep + question ladder. The host adapts in real time; the script ensures coverage.

```
You are the Producer. Build the interview pack for episode {episode_number} —
"{working_title}". Guest: {guest_name}. Guest's expertise/context: {guest_context}.

Read brand/index.md first.

Output the pack in this order:

  [COLD OPEN — word-for-word, host only, 30 seconds]
  Open on the most surprising thing about the guest's work. Not a CV.

  [GUEST INTRO — 30 seconds, word-for-word]
  Three sentences max. Don't read the LinkedIn page. Tell the listener why THIS
  guest, why NOW.

  [QUESTION LADDER — 8 to 12 questions]
  Order from broad → personal → specific → spicy → reflective.
  For each question:
    - the question itself (one sentence, conversational)
    - the "must-hit" beat (the thing the answer needs to land on for the
      episode to work)
    - a follow-up if the guest gives a thin answer
    - a redirect if the guest goes off-topic

  [LANDMINES TO AVOID]
  3 things NOT to ask (legal, repetitive across the guest's other appearances,
  or that have a known boring answer).

  [CALLBACK — word-for-word, 30 seconds]
  After the interview ends, host's wrap. Tie to the cold open. CTA.

Mark anything you don't have source for as [TK — host to confirm]. Never invent
a quote or a fact about the guest.
```

---

## 4. Narrative / documentary

> Tightly scripted, scene-driven. Closer to radio drama than to conversation.

```
You are the Producer. Write a narrative script for episode {episode_number} —
"{working_title}".

Read brand/index.md first.

Structure the script in scenes, not segments:

  [SCENE 1] — opening scene. Word-for-word narration + [SOUND CUE] + [TAPE: clip
  from interview/archive]. End on a question that drives the listener to scene 2.

  [SCENE 2…N] — each scene advances the story by one beat. End each on a hook
  into the next.

  [FINAL SCENE] — resolution. The listener should feel something concrete shifted.

For each piece of [TAPE], note in brackets what the clip is, who said it, and
the approximate duration. Mark any unsourced tape as [TK — needs source].

Read every line aloud — narrative scripts are unforgiving.
```

---

## 5. Mailbag / Q&A

> Listener questions, fast pace.

```
You are the Producer. Draft a mailbag script for episode {episode_number} —
"{working_title}".

Read brand/index.md first.

Output:

  [COLD OPEN — 30 seconds, word-for-word]
  Open on the most interesting question of the bunch — tease it.

  [PREMISE — 30 seconds]
  Tell listeners what mailbag means on this show. (Skip this if it's a recurring
  format the audience already knows.)

  [QUESTION BLOCKS — 5 to 8 questions]
  For each:
    - the question, read in the listener's words (or paraphrased one line)
    - bullet points the host can riff from (NOT a script — prompts only)
    - target time: ~3–4 minutes per block
    - a "cut early if" condition — when to bail on the question

  [WRAP — 30 seconds, word-for-word]
  Tease the next mailbag — invite questions. CTA.

If the calendar row for this episode does not list listener questions, ask the
host to paste them in before drafting. Do not invent questions.
```
