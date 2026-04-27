---
title: Fitness
icon: dumbbell
created: 2026-04-27
tags: [fitness, strength, training, log]
---

# 🏋️ Fitness

> **Train like you mean it.** Strength logs, weekly volume, PRs, recovery — and a coach that plans the week so you don't have to.

## Open the Console first

- 🏋️ [[strength-console/index|Strength Console]] — full-screen Liquid Glass dashboard. Big stats (this week's volume, PRs hit, recovery score, days trained). Movement library with last 3 sets per lift + 1RM. Volume heatmap by week × movement. Recent workouts. Quick-log a new set with one tap.

## What's inside

- `workouts.csv` — every set: date, exercise, weight, reps, RPE, notes
- `exercises.csv` — your movement library (compound + accessory + mobility)
- `cycles.md` — current program, target reps, deload weeks
- `prs.csv` — auto-tracked best sets per movement
- `recovery.csv` — daily HRV, sleep, soreness self-report

## Your team — 1 agent

- 🏋️ **Coach** — programs your week, watches volume + recovery, calls deloads when they're needed (not when the program says). Reads your last 4 weeks before suggesting tomorrow's session. Doesn't flatter — tells you when you're overreaching.

## Daily rhythm

- **6 am daily** — Coach drops tomorrow's session at the top of `index.md` based on your cycle, last session, and recovery score.
- **Sunday 8 pm** — Coach writes the weekly volume review: % of target volume hit per movement, PRs in the last 7 days, anything trending the wrong way.

## Pair with

- **`personal-os/health`** — if installed, Coach reads HRV + sleep + RHR daily to calibrate session intensity.
- **`keto-hq`** or other diet cabinets — Coach respects fueling state (e.g. lower volume in deep ketosis-adaptation phase).
