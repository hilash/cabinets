---
title: Episodes
icon: "🎧"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - episodes
order: 1
---

# 🎧 Episodes

The episode catalog. Each episode lives in its own folder under `episodes/<NNN-slug>/` with three files:

| File | What it is |
|---|---|
| `index.md` | Episode overview, status, links, cover-art prompt |
| `script.md` | The actual script (or interview question ladder) |
| `shownotes.md` | Show notes for distribution platforms |

## Folder convention

```
episodes/
  001-pilot/
    index.md
    script.md
    shownotes.md
  002-<slug>/
    ...
```

The episode number is zero-padded to 3 digits. The slug is the kebab-cased working title.

## Templates

- [[episode-template|📄 Episode index template]] — copy this into a new episode folder as `index.md`
- See [[../generators/script-generator|✍️ Script generator]] for script templates per format
- See [[../generators/shownotes-generator|📝 Shownotes generator]] for shownote templates

## How to start a new episode

1. Add a row to [[../content-calendar|content-calendar.csv]] with `status=idea`.
2. Wait for the Wednesday `weekly-episode-prep` job to draft it — *or*, if you want it now:
3. Open the AI panel on the calendar page and ask: *"Producer, draft episode NNN now."*

## Catalog

- [[001-pilot/index|001 — Pilot]]
