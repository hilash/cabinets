---
title: Slide Generator
icon: "🎨"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - generator
  - slides
order: 3
---

# 🎨 Slide Generator

Slides exist to anchor the spoken explanation, not replace it. The student listens; the slides reinforce. **One idea per slide. Big text. Visuals that clarify.**

## Generator prompt

```
You are the Course Creator. Read the target module's lesson.md.

For EACH sub-lesson in the lesson, output the slide-by-slide brief in this format:

### Sub-lesson N.X slides

| Slide # | Type | Content | Image / Diagram | Notes |
|---|---|---|---|---|
| 1 | TITLE | Sub-lesson title (8 words max) | None | Plain title slide. Brand colors. |
| 2 | HOOK | The opening question/contradiction in 6 words max | Optional supporting visual | This slide is on screen during the verbal hook |
| 3 | OUTCOME | "By the end: [outcome]" — verbatim | Icon | One slide, one big line |
| 4..N | CONTENT | One concept per slide | Diagrams, screenshots, code | See content rules below |
| Final-1 | PRACTICE | The exercise prompt | Optional reference image | One slide with the practice instructions |
| Final | BRIDGE | "Next: [next sub-lesson]" | None | Plain end slide |

Content slides MUST follow these rules:
  - Maximum 12 words on screen at any time. If you need more, split the slide.
  - One sentence per slide if it's a "stated idea". One image + ≤6 words if it's a visual.
  - Worked-example slides: SHOW the example as code / diagram / screenshot. Don't paraphrase.
  - Demo / screen-share slides: a single "DEMO →" slide that signals to the student you're
    switching to screen-record. Don't try to recreate live demos as static slides.

For each slide, also output the IMAGE / DIAGRAM PROMPT if one is needed:

  [IMAGE-GEN PROMPT for slide N]
  Single ready-to-paste prompt for Midjourney / Flux / Gemini Image / DALL·E. End with
  "--ar 16:9 --v 6". Match brand/index.md visual identity.

For diagram slides, output a Mermaid diagram block instead — most slide tools support
Mermaid imports, or you can render to SVG.

For code slides, output the actual code (or pseudo-code if not yet implementation-specific).
Include syntax highlighting language tag.
```

## Slide tools

| Tool | Pick this if |
|---|---|
| **Keynote** | Mac, want the smoothest animation transitions and best presenter mode |
| **Figma Slides** | Designer-leaning, want flexibility, work in browser |
| **Pitch** | Modern, web-based, great templates, collaboration-friendly |
| **Google Slides** | Free, collaborative, "good enough" for most courses |
| **PowerPoint** | If you must — Windows shops, corporate audiences |
| **Slidev / Reveal.js** | Developer-focused, write slides in markdown, version-controlled |

## The single rule that separates pro from amateur

**No slide should require a slide.** If the explanation makes no sense without the slide, the explanation is broken — fix the script. Slides are anchors, not crutches.

The student should be able to listen to the audio alone and still get most of the lesson. If they couldn't, the lesson lives or dies by the video player loading correctly. Don't bet the course on that.
