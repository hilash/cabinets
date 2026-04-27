---
title: Generators
icon: "⚙️"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - generators
  - prompts
order: 1
---

# ⚙️ Generators

Copy-paste prompt packs. Each one is a self-contained prompt you can paste into the AI panel of any episode page (or hand to the `Producer` agent) to generate one specific artifact.

These prompts assume the agent has already read [[../brand/index]]. Tone, length, and format always come from there — never from inside these prompts.

| Generator | What it produces |
|---|---|
| [[script-generator|✍️ Script generator]] | A full script for solo, conversation, interview, narrative, or mailbag formats |
| [[image-generator|🖼️ Image generator]] | Cover-art and per-episode art prompts for Midjourney / Flux / Gemini Image / DALL·E |
| [[title-and-hook-generator\|🎯 Title & hook generator]] | 8 working titles + 3 cold-open hooks per episode |
| [[shownotes-generator|📝 Shownotes generator]] | One-line hook, 60-word summary, timestamps scaffold, SEO keywords |

## How they fit together

```
brand/index.md         ← source of truth (tone, length, format)
        │
        ▼
content-calendar.csv   ← episode pipeline
        │
        ▼
generators/*.md        ← prompt packs the Producer (or you) runs
        │
        ▼
episodes/NNN-slug/     ← script.md + shownotes.md + index.md (with image prompt)
```

Don't edit the generators per-episode — keep them stable. If a generator needs to evolve, evolve it once here and every future episode benefits.
