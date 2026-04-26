---
title: Survival Tracker
icon: timer
created: 2026-04-26
tags: [dashboard, app, newborn]
---

# Survival Tracker

> Full-screen Cabinet app via the `.app` marker. Built for one-handed reading at 3am.

## What it shows

- **"Day X of the marathon"** counter — pulled from baby's DOB
- **Witching-hour banner** — auto-appears 5pm–10pm with one rotating tactic per hour
- **Three big counters** — last feed, last sleep, last diaper, with "X min ago" stamps that auto-refresh every 30 seconds
- **Sleep state block** — full-width when a nap is in progress (dark blue), big "Wake up" button. Tracks duration live.
- **Wake-window timer** — age-calibrated target (45–60 / 60–75 / 75–90 min by week), color shifts gold past target-min, pink past target-max
- **Tap-to-log buttons** — large, finger-friendly. Feed-breast / feed-bottle / wet diaper / dirty diaper.
- **Cluster feed counter** — feeds in the last 3 hours. Hits 3+ → message changes to "that's cluster feeding, normal, especially 4–8pm."
- **Today vs yesterday** — feeds, sleep, diapers with up/down deltas

## Persistence

Data lives in browser localStorage. Survives page reload, doesn't sync between devices on its own. To write entries back to `../mom-command/logs/*.csv` (so other devices and Martha's morning brief see them), ask Martha: "log my last entries from the survival tracker."

## Key thresholds (color logic)

- **Last feed > 2h** → counter goes gold (warn)
- **Last feed > 3h** → counter goes pink (alert — newborns under 6 weeks shouldn't go longer)
- **No diaper logged after noon** → diaper counter goes pink
- **Awake past target-min** → wake-window bar goes gold; past target-max → pink
- **Witching hour (5pm–10pm)** → banner appears with a tactic
- **3+ feeds in 3 hours** → cluster-feed message changes tone

## Design notes

- Vanilla JS + CSS, no framework, no npm. Single file.
- Fraunces serif headings + JetBrains Mono labels match the parchment aesthetic of `mom-command`.
- Every interactive element is at least 48px tall (Apple HIG minimum) — built for one tired thumb.
- `user-scalable=no` on the viewport — pinch-zoom would interfere with the tap targets.
