---
title: Publishing Guide
icon: "🚀"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - publishing
  - distribution
order: 1
---

# 🚀 Publishing Guide

Recording is half the work. Publishing is the other half — and almost no one talks about it.

---

## The 30-second model of how podcast distribution actually works

Most platforms (Apple Podcasts, Overcast, Pocket Casts, Castro, Podcast Addict, etc.) **do not host your audio**. They read an **RSS feed** that points to your audio files. Your podcast host generates that RSS feed.

```
Your podcast host (Buzzsprout/Transistor/etc)
        │
        ▼
RSS feed (an XML URL)
        │
        ├──→ Apple Podcasts (reads the feed)
        ├──→ Overcast        (reads the feed)
        ├──→ Pocket Casts    (reads the feed)
        ├──→ Castro          (reads the feed)
        └──→ Podcast Addict  (reads the feed)

Spotify, YouTube — different. See below.
```

This is why you only need to upload to **one place** to be on most podcast apps.

---

## Step 1 — Pick a podcast host

Your podcast host stores the audio files and generates the RSS feed.

| Host | Price | Notes |
|---|---|---|
| **Buzzsprout** | Free tier (90-day expiry) → ~$12/mo | Easiest UX, best documentation. Recommended for beginners. |
| **Transistor** | ~$19/mo | Multi-podcast hosting (good if you plan more than one show) |
| **Captivate** | ~$19/mo | Strong analytics, marketing tools built-in |
| **Spotify for Podcasters** | Free | Was Anchor. Free forever. Sub-par RSS for non-Spotify platforms. |
| **Substack** | Free | Bundle with newsletter. RSS works but is limited. |

**If you don't know which to pick, pick Buzzsprout.** You can move later — your RSS feed can be redirected.

## Step 2 — Submit your RSS feed to the platforms

Once your host gives you an RSS URL, submit it to each platform **once**. After that, every new episode auto-distributes.

| Platform | Where to submit |
|---|---|
| **Apple Podcasts** | [podcasters.apple.com/connect](https://podcasters.apple.com/connect) |
| **Spotify** | [podcasters.spotify.com](https://podcasters.spotify.com) — submit your RSS feed (most hosts have a 1-click button) |
| **YouTube Music / YouTube** | YouTube auto-pulls eligible RSS feeds. Or upload audio-as-video manually. |
| **Amazon Music / Audible** | [podcasters.amazon.com](https://podcasters.amazon.com) |
| **iHeartRadio** | [iheart.com/content/submit-your-podcast](https://iheart.com/content/submit-your-podcast) |
| **Pocket Casts / Overcast / Castro / etc.** | No submission needed — they index Apple's database |

Apple approves new shows in 1–7 days. Spotify usually within 24 hours. Once approved, every new episode appears automatically when you publish on your host.

## Step 3 — YouTube is its own thing

YouTube doesn't read RSS the same way. You have three options:

1. **YouTube Music auto-import** (free) — works for some hosts, audio-only listing.
2. **Upload audio + static image as video** — biggest reach, takes 5 extra minutes per episode. Tools like Headliner make this easy.
3. **Upload the actual video** (if you recorded with Riverside / StreamYard) — best for growth, requires a YouTube channel and at least minimal video editing.

For most podcasts, option 2 is the sweet spot until you have proof of demand.

## Step 4 — Promo clips for social

3 short vertical clips per episode. 30s, 60s, 90s. Post:

- TikTok
- Instagram Reels
- YouTube Shorts
- LinkedIn (for biz/professional shows)
- X / Threads (for tech / commentary shows)

Tools: Opus Clip (AI-generated clips, paid), Descript (manual + AI), Headliner (free, simple).

The Wednesday `weekly-episode-prep` job already drafts clip suggestions in `episodes/NNN-slug/shownotes.md` under `## Promo clip suggestions`.

## Step 5 — Per-episode publish checklist

Add this to each episode's `index.md`:

- [ ] Master audio uploaded to host
- [ ] Episode metadata: title, description (60-word summary), timestamps, episode art
- [ ] Published — RSS feed updated
- [ ] Verified live: Apple ✓ Spotify ✓ YouTube ✓
- [ ] 1–3 promo clips cut and scheduled
- [ ] Newsletter / blog post drafted (if applicable)
- [ ] Calendar row → `status=published`

---

## What NOT to worry about (yet)

New podcasters waste weeks on these. Don't:

- **A custom domain for your podcast website.** Your host gives you one. Use it.
- **Multiple hosting accounts.** One host. One feed. Don't fragment.
- **Paid promotion before episode 10.** Get to 10 episodes first. Most podcasts die before they even reach 10.
- **Sponsorship pitches before 1,000 downloads/episode.** Sponsors want audience. Build it first.
- **Perfecting your trailer.** Episode 001 IS your trailer. The "podcast trailer" format is overrated for new shows.

What to focus on instead:

1. Publish 10 episodes. Consistent cadence beats production quality at this stage.
2. Get 5 friends to listen and give honest feedback. Iterate on segment structure based on what bored them.
3. After 10 episodes, look at retention curves in your host's analytics. Cut whatever segment loses listeners.
