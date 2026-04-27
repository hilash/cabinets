---
title: Recording Guide
icon: "🎚️"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - recording
  - platforms
order: 1
---

# 🎚️ Recording Guide

The single most expensive mistake a new podcaster makes is using the wrong recording platform. Bad audio is the #1 reason listeners drop off — worse than bad content, worse than a boring guest, worse than a long episode.

This page is a **decision matrix**. Read it once. Pick one platform. Stick with it for at least 5 episodes before switching.

---

## The decision matrix

| Your situation | Use this | Why |
|---|---|---|
| Solo, no guests, just you and a mic | **Local recording** (GarageBand / Audacity / Logic / Reaper) | Highest quality, zero latency, no platform fees, no internet flakiness |
| Solo or guests, video required, want to live-stream | **[[streamyard|StreamYard]]** | Built for live multistreaming. Records as a backup. |
| Remote guests, video + audio, separate tracks | **[[riverside|Riverside]]** | Records each participant locally at studio quality, then uploads. Best audio of any remote tool. |
| Remote guests, audio-only, simple setup | **[[zencastr|Zencastr]]** | Same local-recording approach as Riverside but audio-focused and cheaper |
| Remote guests, audio-only, free | **[[audio-only|Cleanfeed or Zoom + local rec]]** | Both have a $0 path. Cleanfeed has better audio. |
| In-person guests, in the same room | **Local + multi-track interface** | Two mics into a Focusrite Scarlett 2i2 (or similar) → DAW |

## Two questions to answer first

The matrix above just compresses these two:

1. **Are you alone, or with guests?** And if guests — remote or in-person?
2. **Do you need video?** (For YouTube, for live-stream, or to repurpose into Reels / Shorts / TikTok.)

That's it. Everything else is downstream of those two answers.

## What "studio quality" actually means

Most "online podcast platforms" record over the live network connection. If a guest's wifi blips, you lose audio. If their bandwidth is constrained, you get compressed, washy audio. Re-recording a 90-minute episode because the guest had wifi issues happens **a lot**.

The platforms worth paying for (Riverside, Zencastr, SquadCast) solve this with **local recording**: each participant's microphone is recorded *locally* on their machine in uncompressed quality, then the file is uploaded after the call ends. The live call is just a video chat for everyone to see and talk — the actual recording is local.

If your platform doesn't do local recording, you are gambling with every episode.

## Backup is non-optional

Every episode, on every platform, run a **local backup recording** in parallel. On Mac: QuickTime → New Audio Recording. On Windows: OBS or even Audacity. If the platform fails (it will, eventually), you have the audio.

The hosts who don't back up are the hosts who eventually post: *"Sorry, this week's episode is delayed — we lost the recording."* Don't be them.

## Microphone matters more than the platform

A $50 Samson Q2U into a free DAW beats an $800 Shure SM7B used badly on Riverside. If you have to choose, spend money on the mic, not the platform.

A working starter setup:
- **Mic**: Samson Q2U or Audio-Technica ATR2100x (USB + XLR, ~$70). Plug-and-play.
- **Headphones**: anything closed-back (no leak into the mic).
- **Quiet room**: a closet with clothes in it works. Treat the room before you upgrade the mic.

---

## Platform deep-dives

- [[riverside|🎬 Riverside]] — best-in-class for remote guests with video
- [[streamyard|📡 StreamYard]] — best for live-streaming and multistreaming
- [[zencastr|🎙️ Zencastr]] — solid audio-first remote alternative to Riverside
- [[audio-only|🎧 Audio-only options]] — Cleanfeed, Zoom + local rec, SquadCast, local recording

## Once you've chosen

Set the chosen platform as the default in [[../brand/index]] under `Recommended recording setup`. Change it per-episode in `content-calendar.csv` only if a specific episode needs something different (e.g., one episode goes live so it needs StreamYard).
