---
title: Shownotes Generator
icon: "📝"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - generator
  - shownotes
order: 5
---

# 📝 Shownotes Generator

Two passes:

1. **Pre-record draft** — written from the script. Has the structure but uses `[TK]` for anything that depends on the actual recording (timestamps, exact quotes, audio-only moments).
2. **Post-record finalization** — after editing, replace `[TK]`s with real timestamps, real quotes, and any links mentioned during the recording.

---

## Pass 1 — Pre-record draft (run automatically by Wednesday job)

```
You are the Producer. Read brand/index.md (for tone), and read episodes/{NNN-slug}/script.md
for content. Then write a pre-record draft of episodes/{NNN-slug}/shownotes.md with this exact
structure:

## One-line hook
A single sentence — under 100 characters — that describes what the listener gets out of the
episode. This appears in podcast app listings and on YouTube descriptions. No clickbait.

## 60-word summary
~60 words. Three jobs: (1) tell the listener what the episode is about, (2) tell them why
they should care, (3) tell them what they'll know or be able to do after they finish. Read
aloud — must work as natural prose, not as marketing copy.

## Timestamps
List every segment from the script with a `[TK]` placeholder for the time:
  - `[TK]` — Cold open
  - `[TK]` — [Segment 1 name]
  - `[TK]` — [Segment 2 name]
  - …

## Links mentioned
List anything the script references that has a URL — books, products, articles, other
episodes. If the script mentions something without a URL, mark `[TK — link]`.

## Subscribe & follow
Boilerplate block — copy the show's standard subscription links from brand/index.md.

## SEO keywords (3–5)
3–5 phrases the listener might actually search for. NOT keyword-stuffed — these get used
sparingly inside the summary if natural.
```

---

## Pass 2 — Post-record finalization

```
You are the Producer. The host has finished recording episode {episode_number}. Read the
existing episodes/{NNN-slug}/shownotes.md (the pre-record draft) and update it:

1. Replace every `[TK]` in Timestamps with a real time. The host will paste a rough
   timestamp list — match each item to the corresponding segment heading. If a moment
   shifted (e.g., the cold open ran long), update.
2. Replace every `[TK — link]` with the actual URL the host pasted. If a link is still
   missing, leave the `[TK]` in place and flag it back to the host.
3. Re-read the 60-word summary. If the recording diverged from the script (it usually
   did), rewrite the summary to match what actually got said — not what was planned.
4. Update the one-line hook only if the recording produced a stronger hook than the script.
5. Append a "## Promo clip suggestions" section with 3 candidate clips: a 30-second
   moment, a 60-second moment, and a 90-second moment. Each: timestamp range,
   one-sentence reason this clip is shareable.

Keep the structure. Don't add new sections.
```

---

## Where shownotes are used

| Surface | What part is shown |
|---|---|
| Apple Podcasts | Hook + 60-word summary + timestamps + links |
| Spotify | Hook + 60-word summary + timestamps + links (chapter markers if your host supports them) |
| YouTube description | Hook + 60-word summary + timestamps (works as YouTube chapters if formatted `0:00 Title`) |
| Newsletter / blog post | All of the above + promo clip embeds |
| Social posts | The one-line hook + a promo clip |

Keep the pre-record draft and post-record version in the same file — track changes with git, not by duplicating files.
