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

Seven format templates. Pick the one matching the video's `format` column.

The agent **must** read `brand/index.md` first. Don't restate brand rules inside the prompts.

---

## 1. Tutorial / How-to

```
You are the Creative Director. Write a word-for-word tutorial script for video {NNN} —
"{working_title}". Read brand/index.md first.

Structure:

  [HOOK — 0:00–0:08]
  Show the END RESULT first. State the payoff promise in one sentence: "By the end of
  this video, you'll [outcome]." Never open on intro music or "hey guys".

  [SETUP — 0:08–0:30]
  One sentence on what they need (tools, prerequisites). One sentence on why most
  tutorials get this wrong. Then: "Here's the version that actually works."

  [STEPS — body]
  Numbered steps. For each:
    - Step name (one bold line)
    - The actual instructions (spoken, short sentences)
    - The single "watch out" or pitfall in this step
    - On-screen text suggestion: [TEXT: "step name"]
    - B-roll cue: [B-ROLL: what to show]

  [PAYOFF — before midpoint]
  Show the result working. Acknowledge what was hard.

  [BONUS / OVER-DELIVER — after midpoint]
  One thing you didn't promise. The viewer who stayed gets rewarded.

  [CTA — last 15s]
  One ask only. Pull from generators/end-screen-generator.md.

Rules: ~150 words per minute. Mark on-screen text and B-roll. Mark unsourced claims
[TK — creator to confirm].
```

## 2. Vlog

```
You are the Creative Director. Write a beat sheet (NOT a verbatim script) for vlog
video {NNN} — "{working_title}". Read brand/index.md first.

Output:

  [COLD OPEN — 0:00–0:08, word-for-word]
  Drop the viewer mid-action. A scene from later in the video. End on a question or
  contradiction that earns the next 60 seconds.

  [PREMISE — 0:08–0:30, word-for-word]
  Why this vlog. What the viewer will see by the end.

  [BEATS — body]
  6–10 beats. Each:
    - Beat name (one line)
    - 2–3 talking points (NOT a script — prompts only)
    - Emotional turn (what shifts)
    - B-roll/cutaway list

  [CALLBACK — last 30s, word-for-word]
  Tie back to the cold open. One ask CTA.

Vlogs live or die on personality. Don't over-script.
```

## 3. Video essay

```
You are the Creative Director. Write a fully scripted video essay for {NNN} —
"{working_title}". Read brand/index.md first.

Structure:

  [HOOK — 0:00–0:15, word-for-word]
  Open on a counterintuitive claim or unresolved question. Make the viewer NEED the
  answer.

  [THESIS — 0:15–1:00]
  State the argument in one sentence. Tell the viewer the journey.

  [ACTS — body, 3 acts]
  Each act:
    - Sub-claim (the act's job)
    - Evidence (sources, examples — mark unsourced [TK])
    - B-roll plan: archival, supers, cutaways, motion graphics
    - Transition that earns the next act

  [SYNTHESIS]
  Bring the threads together. Land the thesis with weight.

  [CTA — final 30s]
  One ask. Tie to a related video on the channel.

Essays demand B-roll. Every claim needs a visual.
```

## 4. Listicle / Top N

```
You are the Creative Director. Write a listicle script for {NNN} — "{working_title}". Read brand/index.md first.

Structure:

  [HOOK — 0:00–0:08]
  Tease the #1 (or #N) entry without revealing it. Promise the list payoff.

  [PREMISE — 0:08–0:25]
  Why this list. What criteria. Tell the viewer where the ranking is going.

  [ENTRIES — body]
  Order: lowest first, highest last. For each entry:
    - Number + name (on-screen text)
    - 30–60 seconds of content
    - One specific reason it earns this rank
    - One pattern interrupt (B-roll, super, zoom)

  [BONUS / HONORABLE MENTIONS — optional]
  1–2 entries that didn't quite make the cut. Keeps listcrowders watching past the end.

  [CTA — final 15s]
  One ask only.

Don't pad. Cut entries that don't earn the time.
```

## 5. Reaction

```
You are the Creative Director. Build a reaction-video pack for {NNN} — "{working_title}".
Read brand/index.md first.

Output:

  [SUBJECT BRIEF]
  What's being reacted to. URL or source. Why this and why now.

  [TIMESTAMP MAP]
  List of 5–10 timestamps in the source material that need to be reacted to. For each:
    - Source timestamp
    - The "must-have" reaction beat
    - One thing to point out the casual viewer would miss
    - Optional follow-up tangent (pre-prepared)

  [OPENING — word-for-word, 0:00–0:15]
  Why this reaction. Why this creator.

  [CLOSING — word-for-word, last 30s]
  Synthesis: the through-line of the whole reaction. CTA.

Don't write reactions verbatim — that's lying to the viewer. Prompts only.
```

## 6. Mini-documentary

```
You are the Creative Director. Write a mini-doc script for {NNN} — "{working_title}".
Read brand/index.md first.

Structure as scenes, not segments:

  [SCENE 1 — opening, word-for-word VO + [B-ROLL] + [INTERVIEW: who, soundbite]]
  Open in motion. End on a question.

  [SCENE 2…N — narrative beats]
  Each scene advances the story. End each on a hook into the next.

  [FINAL SCENE]
  Resolution + emotional payoff + CTA.

Mark every interview clip [TK — needs source] if not yet recorded.
```

## 7. YouTube Short / vertical

```
You are the Creative Director. Write a 30–60 second Shorts script for {NNN} —
"{working_title}". Read brand/index.md first.

Structure:

  [HOOK — 0:00–0:03]
  ONE bold claim or question. Visual must support it.

  [BODY — 0:03–0:50]
  Three beats max. Each: one sentence + one cut. Pace is everything.

  [PAYOFF — 0:50–end]
  Resolve the hook. CTA — usually "watch the full video [link]" or "follow for more".

Vertical 9:16. ~3 words per second. No intro music.
```
