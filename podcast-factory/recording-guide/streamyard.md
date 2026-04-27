---
title: StreamYard
icon: "📡"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - recording
  - streamyard
  - live
order: 3
---

# 📡 StreamYard

> Built for **live streaming** to YouTube, LinkedIn, Facebook, X, Twitch — simultaneously. Recording is the byproduct, not the main feature. Pick this if "going live" is part of your show concept.

## Pick this if

- You want to live-stream the recording to YouTube, LinkedIn, etc. — at the same time
- Your audience interacts in real-time (you read their comments on air)
- You want to multistream to several platforms at once
- The audio quality you can get from a network call is *good enough* (it is, for most non-NPR-style podcasts)

## Don't pick this if

- You want studio-grade audio and never go live — use Riverside or Zencastr instead
- You need separate audio tracks per participant for surgical post-edit (StreamYard records a single mixed track)

## How a StreamYard session works

1. Create a broadcast in the dashboard. Connect destinations (YouTube channel, LinkedIn page, etc.).
2. Send the studio link to your co-host or guest. They join in-browser. No install.
3. You hit "Go Live" — and at the same time, "Start Recording".
4. The recording is the live stream output: one combined video + audio file, plus a separate audio-only file.
5. After the broadcast, the file is available to download from the dashboard.

## Setup checklist before going live

- [ ] All destinations connected and re-authenticated (tokens expire — check 24h ahead)
- [ ] Pre-show banner / overlay set up
- [ ] Co-host or guest joined and tested 10 min before going live
- [ ] Mic and camera levels checked
- [ ] Comment moderator assigned (you can't host AND read every comment)
- [ ] Run a 1-min "private" stream first to confirm everything is wired up

## What you get out

- **MP4** — the live broadcast as one file (combined video + mixed audio)
- **MP3** — audio-only mixed track
- **Comments / chat log** — exportable, useful for shownotes timestamps

## StreamYard-specific gotchas

- **Single mixed audio track.** No per-participant tracks. If your guest's audio sucks, you cannot fix it in post.
- **Browser-based.** Chrome only, really. Other browsers have flaky support.
- **Bandwidth-sensitive.** A 5 Mbps upload is the minimum for HD with two participants. Wired ethernet over wifi.
- **No local recording fallback.** Always run a parallel local audio backup (QuickTime / OBS).

## StreamYard vs. Riverside for "live + recorded"

| | StreamYard | Riverside |
|---|---|---|
| Live to YouTube/LinkedIn/etc. | ✅ Multistream native | ⚠️ One destination, less mature |
| Audio quality (recorded) | Good (network) | Excellent (local recording) |
| Per-participant tracks | ❌ | ✅ |
| Best for | Live shows | Studio-quality interviews |

If your show is "we go live every Tuesday with comments from listeners", use StreamYard. If your show is "long-form interviews that publish polished a week later", use Riverside.
