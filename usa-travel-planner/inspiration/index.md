---
title: Inspiration Feed
created: '2026-04-25T00:00:00.000Z'
modified: '2026-04-25T00:00:00.000Z'
tags:
  - inspiration
  - events
  - news
  - x
order: 6
icon: 📡
---

# 📡 Inspiration Feed

> What's actually cool happening across America right now.

Every Monday at 9 AM, the **Event Hunter** agent scans X / news / Reddit / Eventbrite for upcoming events worth traveling for, and appends curated finds below. The feed grows append-only — each week is a new section, older weeks stay so you can track what was trending.

**Categories:** music · food · sports · arts · quirky · natural

---

## Week of 2026-04-21 *(seed entries — first weekly scan runs Monday)*

### Cherry Blossom Peak Bloom — Washington, DC — through April 28
**Why it's cool:** This year's peak hit four days later than the average, so the Tidal Basin window is unusually fresh into late April. Walk the basin at dawn before the tour buses.
**Source:** [National Park Service Cherry Blossom Watch](https://www.nps.gov/subjects/cherryblossom/bloom-watch.htm)
**Tags:** natural

### Hatch Green Chile Pre-Season — Hatch, NM — late August teaser, but worth flagging now
**Why it's cool:** The Hatch Chile Festival is Labor Day weekend, but accommodations in Hatch and nearby Las Cruces book up by July. This is the single most concentrated chile-roasting weekend in America — every restaurant in town turns into a chile-roasting tent.
**Source:** [Hatch Chamber of Commerce](https://www.hatchchamberofcommerce.com)
**Tags:** food, quirky

### Salt River Mass Tubing Reopening — Mesa, AZ — opens late April
**Why it's cool:** America's most chaotic, gorgeous, fully-American river-tubing experience reopens for the season. Bring sunscreen. Don't bring valuables. Wild horses sometimes show up.
**Source:** Salt River Tubing — saltrivertubing.com
**Tags:** quirky, natural

---

## How this works

The Event Hunter is set to run weekly via the `weekly-event-scan` job in `/data/usa-travel-planner/.jobs/`. Each scan:

1. Pulls fresh signal from X (search operators), regional news, Reddit, and Eventbrite
2. Filters down to "would I drive cross-country for this?" quality
3. Appends a new `## Week of YYYY-MM-DD` block above the previous one (most recent at top after seed entries)
4. Never modifies past weeks

If you want a manual scan for a specific region or category, just ask the Event Hunter:
> *"Scan for art-week events in October across the West Coast."*
> *"Anything cool in Chicago in the next 6 weeks?"*
> *"Find me weird Americana for a Texas road trip in June."*
