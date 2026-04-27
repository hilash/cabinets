---
title: Day-Of Timeline Generator
icon: "⏱️"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - generator
  - day-of
order: 5
---

# ⏱️ Day-Of Timeline Generator

The single most useful document you produce. Every vendor, every wedding-party member, every parent needs the same shared timeline. The day works because everyone has a copy.

## Generator prompt

```
You are the Planner. You are generating the day-of timeline.

Read `vision/index.md` for the ceremony time, location, and reception style.
Read `vendors/tracker.csv` to identify booked vendors.

Ask the user for any specifics not in those files:
  - Ceremony start time (this anchors everything)
  - Ceremony location → reception location (same place? travel time?)
  - First-look photos: yes / no
  - Cocktail hour: how long?
  - Sit-down meal duration (typically 90 min)
  - Cake cut + first dance + parent dances + open dance floor sequence
  - Send-off: yes / no, and what kind (sparklers / car / etc.)

Generate the timeline backwards from ceremony start. Output as a table:

| Time | Event | Who is involved | Location | Notes |
|---|---|---|---|---|

Standard structure (adjust to user's specifics):

  T-5h: Hair + makeup begin (bride + bridal party)
  T-4h: Photographer arrives — getting-ready coverage
  T-3h: Groom + groomsmen arrive at venue, get dressed
  T-2.5h: Vendors arrive (florist setup, DJ load-in)
  T-2h: First-look photos (if doing them) + bridal party portraits
  T-1h: Family portraits (use the family-photos shotlist from `day-of/family-shots.md`)
  T-30min: Guests start arriving (greeted by ushers)
  T-15min: Officiant briefs key family on ceremony order
  T-5min: Couple in position
  T-0: Ceremony begins
  +30min: Ceremony ends — receiving line OR straight to cocktail hour
  +30 to +90min: Cocktail hour + couple does private moment + remaining portraits
  +90min: Guests seated for reception
  +95min: Couple's grand entrance
  +100min: Welcome toast (host or couple)
  +105min: First course served
  +30 to +60min into meal: Speeches (rotate with courses, not all at once)
  Mid-meal: First dance + parent dances
  After meal: Open dance floor
  ~3h into reception: Cake cut
  4–5h into reception: Last dance + send-off
  END: Vendor strike begins per their contracts

Output the timeline as a table. Then output four extracts:

  ### Photographer brief — when to be where
  ### DJ / band brief — set list windows + anchor moments
  ### Wedding-party brief — when each person needs to be where
  ### Family brief — for parents + key family on ceremony + photos

Each extract is a focused subset of the master timeline for that audience.

Then output:

  ### Buffer zones
  Mark every place a 15-minute buffer was added. Explain why. (Hair always runs late.
  Cocktail hour gives portraits + setup margin. Speeches always overrun.)

  ### Single points of failure
  List 3–5 things that, if delayed, push the whole timeline. With contingency.
```

## Distribution

The day-of timeline goes to:

| Recipient | Version |
|---|---|
| Each vendor | Their extract — what they need to know about their part |
| Wedding party | Wedding-party brief — when they need to be where |
| Parents / hosts | Family brief — ceremony order, photos, speeches |
| MC / officiant | Master timeline — they coordinate the day |
| The couple | Master timeline — read once, then trust the team |

Send these out the **week before** the wedding. Not the day before. Not the day-of.

## Buffer everywhere

Every transition gets a 15-minute buffer:
- Hair / makeup → photos
- Photos → ceremony
- Ceremony → cocktail
- Cocktail → seating
- Speeches → next course

The day always runs long. Buffers absorb the slack so you're not behind by 8pm.

## What goes wrong (and how to handle it)

| Failure | Backup |
|---|---|
| Hair / makeup runs late | First-look photos slide; family portraits compress |
| Officiant / vendor stuck in traffic | Designated person ready to call them at T-30min if not on-site |
| Weather (outdoor venue) | Indoor backup confirmed at venue, decision called by T-3h |
| MC microphone fails | Second mic on standby with DJ; officiant has their own |
| Cake delivery late | Cake cut shifts later in reception; cake setup can happen during dinner |
| Speech runs long | MC has authority to gently cut at the agreed-on max |

The timeline is a living document. The agent updates it when vendor times change. The couple does NOT manage it on the day — the planner / MC / day-of coordinator does.
