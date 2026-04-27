---
title: Videos
icon: "🎥"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - videos
order: 1
---

# 🎥 Videos

The video catalog. Each video lives in its own folder under `videos/<NNN-slug>/`:

| File | What it is |
|---|---|
| `index.md` | Video overview, status, title candidates, hook candidates, end-screen |
| `script.md` | The script (or beat sheet) |
| `thumbnail-brief.md` | Concept, on-thumbnail text, image-gen prompt, alternates |

## Folder convention

```
videos/
  001-pilot/
    index.md
    script.md
    thumbnail-brief.md
  002-<slug>/
    ...
```

## Templates

- [[video-template|📄 Video index template]] — copy as `index.md` for a new video
- See [[../generators/script-generator|✍️ Script generator]] for per-format templates

## Catalog

- [[001-pilot/index|001 — Pilot]]
