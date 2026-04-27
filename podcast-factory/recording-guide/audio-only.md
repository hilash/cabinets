---
title: Audio-only options
icon: "🎧"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - recording
  - audio-only
  - free
order: 5
---

# 🎧 Audio-only options

You don't have to pay for Riverside or Zencastr to make a great-sounding podcast. There are three good audio-only routes — including a $0 path.

---

## Option 1 — Local recording (solo, $0)

If you record alone, **just record locally**. No platform. No upload. No internet flakiness.

| OS | Tool |
|---|---|
| Mac | GarageBand (free), Logic Pro (paid), Reaper (paid, cheap) |
| Windows | Audacity (free), Reaper, Cakewalk (free) |
| Linux | Audacity, Ardour |

**Why it's the best option for solo:** zero latency, lossless audio, full control, no vendor lock-in. You will get better audio than 95% of paid platforms can give you for a remote call.

**Setup:**
1. Plug in your USB mic (Samson Q2U, ATR2100x, etc.) or XLR mic + interface.
2. Open the DAW. New project. Set sample rate to 48kHz, bit depth to 24-bit.
3. Arm the track. Hit record. Talk.
4. Export WAV when done. Edit. Done.

---

## Option 2 — Cleanfeed ($0 with paid tier)

[cleanfeed.net](https://cleanfeed.net) — browser-based, audio-only, with a free tier that records.

**Pick this if:**
- You record remote guests
- You want studio-grade audio
- You can't pay for Zencastr or Riverside

**How it works:** Network call, but uses Opus codec at high bitrates over a peer-to-peer connection. Quality is excellent for a network call — better than Zoom, much better than a phone call. Not as good as local recording (Riverside / Zencastr) but the gap is small for most ears.

**Setup:**
1. You sign up for free, send a link to your guest.
2. Guest joins in browser. No account needed.
3. You hit record on your side. The recording is made on *your* machine of the combined call audio (or separated tracks on the paid tier).
4. Stop, download, edit.

**Watch out:**
- Free tier records combined audio only. Paid (~$15/month) gets you separated tracks.
- Quality depends on both participants' connections. Ethernet beats wifi.
- Always run a local backup just in case.

---

## Option 3 — Zoom + local recording ($0)

The "everyone already has Zoom" option. It works. It is not pretty.

**Pick this if:**
- The guest refuses to install or sign up for anything
- The guest is very non-technical
- You're fine with audio that sounds like a Zoom call (because it will sound like a Zoom call)

**The trick:** Don't rely on Zoom's recording. Run a **local audio recording** on each participant's end:
- You: QuickTime (Mac) or Audacity (Windows) recording your own mic.
- Guest: ask them to record themselves on Voice Memos (iPhone) or the Windows Voice Recorder.
- After the call, the guest sends you their local file via Dropbox / Google Drive / WeTransfer.
- You sync the two files in your DAW using the clap method (everyone claps at the start).

**This is called a "double-ender"** in podcasting. It's how interview podcasts were made for a decade before Riverside existed. Free, reliable, and the audio is genuinely studio-grade — because each side recorded locally.

The only downside: you depend on the guest to (a) remember to record, (b) actually send you the file. Brief them clearly and politely follow up.

---

## Option 4 — SquadCast (acquired by Descript)

If you edit in Descript, SquadCast (now part of Descript Studios) is the most integrated option. Same local-recording model as Riverside / Zencastr. Worth considering as a fourth option if Descript is already your editor.

---

## Quick chooser

| Situation | Pick |
|---|---|
| Solo, no guests | Local DAW (GarageBand / Audacity) |
| Remote guest, $0 budget, semi-technical guest | Cleanfeed |
| Remote guest, $0 budget, non-technical guest | Zoom + double-ender |
| Remote guest, ~$20/month budget | Zencastr or Riverside |
| Remote guest, edits in Descript | SquadCast |

Whichever you pick: **always run a local backup recording on your end.** Every time.
