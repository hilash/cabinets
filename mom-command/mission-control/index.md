---
title: Mission Control
icon: layout-dashboard
created: 2026-04-26
tags: [dashboard, app]
---

# Mission Control

> Full-screen dashboard. Last feed, last sleep, last diaper, baby's age, growth percentile, milestones, vaccinations, next appointment — all on one page. Pulls from `../baby-profile.md`, `../logs/*.csv`, and `../pediatrician.md`.

The page renders as a full-screen Cabinet app via the `.app` marker — open it from the sidebar.

## What it shows

- **Top vitals row** — last feed/sleep/diaper with "X min ago" stamps, today's totals, next appointment
- **Quick log buttons** — tap to log a feed/sleep/diaper. Persists to browser storage between visits; ask Martha to "log my last entries" to write back to CSV
- **Today's stream** — every entry from feeds + sleeps + diapers, today only, time-stamped
- **Growth chart** — weight curve with WHO-style percentile band, latest reading + percentile
- **Milestones — next up** — windows from milestone-log.csv, color-coded (gold = due, pink = overdue, green = done)
- **Vaccines** — upcoming + completed, against the CDC schedule

## Data sources

| Card | Reads |
|---|---|
| Vitals (top row) | `../logs/feed-log.csv`, `sleep-log.csv`, `diaper-log.csv`, `../pediatrician.md` |
| Quick log | Writes to browser localStorage; Martha syncs to CSV on request |
| Stream | `../logs/feed-log.csv`, `sleep-log.csv`, `diaper-log.csv` |
| Growth chart | `../logs/growth-chart.csv` |
| Milestones | `../logs/milestone-log.csv` |
| Vaccines | `../logs/vaccination-schedule.csv` |
