---
title: Title & Hook Generator
icon: "🎯"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - generator
  - title
  - hook
order: 4
---

# 🎯 Title & Hook Generator

Episode titles are the *only* thing 90% of potential listeners ever see. Cold opens are the only thing 90% of *clickers* ever hear. Get both right and your episode has a chance.

---

## Prompt — 8 working titles + 3 cold-open hooks

> Paste into the AI panel of any episode page (or the calendar). Replace `{premise}` with the episode's premise, or just say "for episode NNN".

```
You are the Producer. Read brand/index.md and the target episode's row in
content-calendar.csv (premise, format, target_minutes).

Output two blocks:

[8 WORKING TITLES]
- Each title under 60 characters. Apple/Spotify truncate after that.
- Mix four "shapes":
    1. Question titles — "Why do dogs eat grass?"
    2. Number titles — "3 mistakes new dog owners make in week one"
    3. Statement titles — "Crate training is not cruel"
    4. Curiosity-gap titles — "The thing every vet wishes you'd stop doing"
- No clickbait we can't deliver on. If the episode doesn't deliver "the secret",
  don't promise "the secret".
- No colons unless the show's brand voice uses them.

[3 COLD-OPEN HOOKS — 30 seconds each, word-for-word]
- Hook A: open on a SCENE — concrete, sensory, dropping the listener mid-action.
- Hook B: open on a QUESTION — one the listener has had but never said aloud.
- Hook C: open on a CONTRADICTION — "everybody thinks X. X is wrong because…"

Each hook ends with a sentence that sets up the rest of the episode without
spoiling the payoff. Read each one aloud silently — if it sounds like a press
release, rewrite.
```

---

## How to choose

- Pick the title that **promises a specific thing the episode actually delivers**. Vague wins on impressions, specific wins on play-through and retention. Retention is the metric Spotify and Apple use to recommend you.
- Pick the hook that opens **the loudest** without being false. The listener's finger is hovering over skip — give them no reason to use it in the first ten seconds.

## Once you have a winning hook

Open `episodes/NNN-slug/script.md` and replace the `[COLD OPEN — 30 seconds]` block with the chosen hook word-for-word. Keep the other two in a `## Alternatives` section at the bottom — useful for re-cuts and promo clips.
