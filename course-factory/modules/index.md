---
title: Modules
icon: "📚"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - modules
order: 1
---

# 📚 Modules

The curriculum. Each module lives in its own folder under `modules/<NNN-slug>/`:

| File | What it is |
|---|---|
| `lesson.md` | The lesson script(s) for the module |
| `slides-brief.md` | Slide-by-slide brief — content + design intent |
| `practice.md` | Practice exercises with expected outputs |
| `index.md` | Module overview + status + assets |

## Folder convention

```
modules/
  001-welcome/
    index.md
    lesson.md
    slides-brief.md
    practice.md
  002-<slug>/
    ...
```

## The lesson loop

Each lesson follows the same structure:

```
HOOK → outcome → explanation → worked example → practice → bridge
```

- **HOOK** — open on a question, problem, or contradiction. NEVER on "Welcome to module 3".
- **OUTCOME** — state what they'll be able to do at the end of THIS lesson.
- **EXPLANATION** — the minimum vocabulary + concept. Cut everything not needed for the practice.
- **WORKED EXAMPLE** — solve one real instance, narrating decisions.
- **PRACTICE** — student does it. Most of the learning happens here.
- **BRIDGE** — one sentence to the next lesson.

## Catalog

- [[001-welcome/index|001 — Welcome + course roadmap]]
