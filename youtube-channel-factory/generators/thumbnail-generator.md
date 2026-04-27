---
title: Thumbnail Generator
icon: "🖼️"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - generator
  - thumbnail
order: 3
---

# 🖼️ Thumbnail Generator

The thumbnail-and-title combo IS the video. CTR lives or dies here. Treat thumbnails as products, not afterthoughts.

## Three rules of YouTube thumbnails

1. **One focal point.** A face showing emotion if possible. The eye must lock onto one thing in under 0.5s.
2. **Contrast at 320×180px.** Browse on YouTube on a phone. Thumbnails compete at thumb size. If you can't read the on-thumbnail text and identify the focal point in 1 second on a phone, it's broken.
3. **The thumbnail completes the title** — they're a couplet. Title says the *what*, thumbnail shows the *visceral why-care*. Don't repeat the title text on the thumbnail.

## Generator prompt

```
You are the Creative Director. Read brand/index.md (visual identity) and the target video's
row in content-calendar.csv (premise, format, thumbnail_concept).

Output a thumbnail brief for video {NNN} in this exact structure:

  ## Central concept
  One sentence describing the single focal element. Must be drawable on a napkin.

  ## On-thumbnail text
  Maximum 4 words. All caps. Massively contrasting against the background. State this
  text on its own line in backticks.

  ## Image-gen prompt
  A single ready-to-paste prompt for Midjourney v6+ (also portable to Flux, DALL·E,
  Gemini Image). Requirements:
    - 16:9 aspect ratio. End with "--ar 16:9 --v 6"
    - One central element. Heavy contrast. Bold.
    - Style descriptors must match brand/index.md visual identity.
    - The thumbnail text is added in post (Photoshop, Canva, Photopea) — DO NOT ask the
      image generator to render the text. AI text rendering is unreliable at thumbnail size.
      Generate the background + focal subject only.
    - Reserve the bottom-left or top-right third of the frame as a "text safe zone"
      (lower visual density there).

  ## Two alternative concepts
  Briefly describe two completely different visual angles for this video. The creator
  picks the strongest after seeing all three rendered.

  ## On-thumbnail text — three variants
  Three 4-word-max alternatives. Different emotional pulls (curiosity, urgency, payoff).
```

## Tools

| Tool | Best for |
|---|---|
| Midjourney v6+ | Painterly / cinematic / striking. Best aesthetic. |
| Flux | Photorealistic + accurate text (if you do render text via AI) |
| Gemini Image / Imagen 3 | Clean compositions, brand-safe |
| Ideogram | Best-in-class for in-image text (if you need it) |
| **Photoshop / Photopea / Canva** | **For adding the on-thumbnail text — always do this in post, never via AI** |

## Workflow

1. Generate the background/subject from the prompt above.
2. Pull into Photoshop / Photopea (free) / Canva.
3. Add the on-thumbnail text in your channel's brand typography (locked in `brand/index.md`).
4. Export 1280×720px JPG (under 2MB — YouTube's limit).
5. Test at 320×180px. If it doesn't read in 1 second, redo.

## A/B testing

After 100k impressions, YouTube's experimental feature lets you A/B test up to 3 thumbnails for the same video. Always upload all three alternates so you can switch later.
