---
title: Self-hosted (Notion + Stripe)
icon: "🛠️"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - platform
  - self-hosted
order: 6
---

# 🛠️ Self-hosted

> The "no platform" option. Notion (or your CMS) for content. Stripe for payments. Loom / YouTube unlisted for video. Slack / Discord for community. Zero platform fees. Maximum setup.

## Pick this if

- You're a developer or technical creator
- You hate platform fees
- You want maximum brand consistency
- Your audience is comfortable with non-standard course experiences
- You're charging premium prices and want every dollar to land

## Don't pick this if

- This is your first course — the friction will distract you from teaching
- You want students to be impressed by the platform polish
- You don't want to debug payment links on launch night

## The DIY stack

| Need | Tool |
|---|---|
| Course content | Notion (with Super.so or Potion as front-end) / your blog / Bear Blog |
| Video hosting | YouTube unlisted, Vimeo, or Wistia (paid, more pro) |
| Payments | Stripe Checkout / Stripe Payment Links |
| Email | ConvertKit / Beehiiv (whatever you'd use anyway) |
| Community | Discord / Slack / Circle (paid) |
| Login / access control | Outseta / Memberstack / custom |
| Sales page | Carrd / Framer / your own site |

Total monthly: ~$30 (Stripe is per-transaction; Notion is free-ish; ConvertKit you'd have anyway).

## Setup

### Minimum viable

1. **Sales page** on Carrd or Framer ($9–25/mo).
2. **Stripe Payment Link** — single product, students pay, get an email with...
3. **Notion page** with the entire course laid out — text + embedded YouTube unlisted videos. Set page to "anyone with link can view" but don't share publicly.
4. **Email automation** — ConvertKit form on the sales page captures buyer email; ConvertKit auto-emails the Notion link after Stripe purchase succeeds.

That's it. You can ship in a day. ~$50 total cost over a month.

### Adding production polish

When the first cohort buys, add:
- A Slack or Discord for community
- Loom recordings of any live sessions
- A simple progress tracker (Airtable / a Notion database where students mark off lessons)
- A weekly Q&A live call (Zoom + recording)

### When to stop self-hosting

You'll know you've outgrown the DIY stack when:
- You're spending more time fixing the stack than teaching
- Students complain about the experience (login, video buffering, "where do I find...")
- You want native analytics on student progress
- You're ready to invest in production polish

At that point, migrate to Teachable / Kajabi / Maven.

## The 95% rule

A self-hosted setup at 95% polish on a $300 course beats a Kajabi setup at 100% polish — IF the content is great. Students forgive a slightly clunky platform; they don't forgive thin content.

The biggest mistake self-hosters make: spending the first 4 weeks building the platform, the next 4 weeks building the course content, then running out of energy before launch. Build the content first. Use the simplest possible delivery. Launch. Then improve.
