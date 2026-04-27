---
title: Image Generator
icon: "🖼️"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - generator
  - image
  - cover-art
order: 3
---

# 🖼️ Image Generator

The Producer agent does not generate images. It generates **prompts** that you paste into Midjourney, Flux, Gemini Image, DALL·E, or your tool of choice.

Two artifacts:

1. **Show cover art** — one-time, lives at the top of [[../brand/index]]. Square 3000×3000px. Apple Podcasts, Spotify, and YouTube all require this.
2. **Episode art** — one per episode, lives in `episodes/NNN-slug/index.md`. Same square format.

---

## Style discipline

The hardest thing about podcast art is **consistency across episodes**. New podcasters generate every episode's art from scratch and end up with twelve unrelated images. That kills brand recognition.

Lock the show's visual style first (colors, typography, illustration vs. photo, mood, repeating motifs). Every episode reuses 80% of that style — only one or two elements change per episode.

The prompt below has two halves. The **style block** stays identical across episodes. The **subject block** changes per episode.

---

## Prompt for SHOW cover art

> Run once at bootstrap. Paste the result at the bottom of `brand/index.md` under `## Cover art prompt`.

```
You are the Producer. Read brand/index.md to understand the show's premise, target listener,
and the three "describe us in three words" adjectives.

Then write a single image-generation prompt for the show's main cover art. Format the
prompt for Midjourney v6+ but keep it portable to Flux, Gemini Image, and DALL·E (avoid
tool-specific tokens unless they're widely supported).

Requirements the prompt must enforce:
  - Aspect ratio: 1:1 (square). End the Midjourney prompt with "--ar 1:1 --v 6".
  - Resolution-friendly composition: nothing important within 200px of the edge — Apple
    Podcasts crops corners on some surfaces.
  - The show name (from brand/index.md) must be in the image as text. Specify a
    typography style — serif / sans / hand-drawn / etc. — that matches the tone.
  - One central visual element. Not a collage.
  - Limited color palette: 2–4 colors total, one accent.
  - Style descriptors should match the show's three durable adjectives.
  - Output must scale legibly to 55×55 pixels (the size it appears on a phone lock screen).

Output ONLY the prompt itself, ready to paste — no preamble, no explanation.
```

---

## Prompt for EPISODE art

> Run for each episode. The Wednesday `weekly-episode-prep` job auto-generates this when it drafts a script.

```
You are the Producer. Read brand/index.md first to recall the locked-in show visual style.
Then read episodes/{NNN-slug}/index.md and script.md for the episode's specific subject.

Write a single image-generation prompt for this episode's art that:

  1. Inherits the show's locked style block — same palette, same typography, same
     illustration-vs-photo choice, same mood. Do not redesign the show.
  2. Changes only the central subject to match THIS episode's premise.
  3. Includes the episode number prominently (e.g. "EP 003" or "#03") in the show's
     established typography.
  4. Optionally includes a one- or two-word subtitle pulled from the episode title — never
     the full episode title, it won't fit at 55×55px.

Aspect ratio 1:1. End with "--ar 1:1 --v 6" for Midjourney compatibility. Output ONLY the
prompt itself, ready to paste.
```

---

## Tool quick-reference

| Tool | Best for | Notes |
|---|---|---|
| Midjourney v6+ | Stylized, painterly, distinctive looks | Best aesthetic out of the box. Use `--style raw` if it over-stylizes. |
| Flux (Pro / Dev) | Realistic photography, accurate text-in-image | Strongest for typography. Free tier via Replicate / fal.ai. |
| Gemini Image (Imagen 3+) | Mixed photo + text + clean compositions | Good guardrails. Easy with kid-friendly shows. |
| DALL·E 3 | Conceptual / illustrated, integrated with ChatGPT | Tends toward soft, illustrated style. Will reword your prompt — be explicit. |
| Ideogram | Anything with text — best-in-class typography | Underrated for podcast art. |

## Once the image is generated

1. Save as PNG or high-quality JPG at 3000×3000px.
2. Drop it into `episodes/NNN-slug/cover.png` (or `brand/cover.png` for show art) — Cabinet renders it inline in the sidebar.
3. Upload the same file to your podcast host (Buzzsprout / Transistor / Captivate / Spotify for Podcasters). They re-encode for each platform.
