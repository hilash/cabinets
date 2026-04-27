---
title: Vendors
icon: "📇"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - vendors
order: 1
---

# 📇 Vendors

The vendor matrix. Each row is one vendor under consideration. The Planner adds prospects, you decide. Once `status` is `booked`, the Planner doesn't touch the row.

## Status flow

```
prospecting → contacted → quoted → shortlisted → booked → paid → done
```

| Status | Meaning |
|---|---|
| `prospecting` | On the list, not yet reached out |
| `contacted` | First message sent, awaiting reply |
| `quoted` | They've sent a quote — review, compare |
| `shortlisted` | One of the top contenders — schedule a call/visit |
| `booked` | Contract signed, deposit paid |
| `paid` | Final payment made |
| `done` | Service delivered, post-wedding |
| `passed` | Decided not to use them — keep the row for reference |

## Booking order (the long poles)

The vendors that book up earliest. Lock these first:

1. **Venue** — drives every other decision. Book 12+ months out for popular venues.
2. **Photographer** — best ones go fast, often 12+ months ahead.
3. **Officiant** — especially if religious or in-demand.
4. **Caterer** — often tied to venue, but verify.
5. **Florist** — popular ones book 6–12 months ahead.
6. **DJ / band** — 6–12 months for top picks.

The rest can usually be locked 3–6 months out.

## Vendor categories — what to ask each one

| Category | Critical questions |
|---|---|
| Venue | Capacity, what's included (tables, chairs, linens), corkage / catering rules, accessibility, weather backup, end time, parking |
| Caterer | Per-head pricing, dietary accommodations, tasting included?, minimums, service staff included? |
| Photographer | Hours covered, second shooter, deliverables (RAW or edited only?), turnaround time, sample full gallery from a real wedding |
| Videographer | Coverage hours, drone permitted at venue?, deliverable format + length, music licensing handled |
| Florist | Per-arrangement pricing, sample inspirations, breakdown of ceremony vs reception, setup + breakdown included? |
| DJ / band | Set length, breaks, MC duties?, equipment included, request handling, backup plan if member ill |
| Officiant | Includes ceremony writing?, rehearsal attendance, license filing, any restrictions on vows or readings |
| Hair + makeup | Trial included?, on-site or studio, time per person, touch-ups during day |
| Cake / dessert | Per-slice pricing, dietary options, tasting?, delivery + setup |
| Stationery | Save-the-dates + invites + day-of (programs, menus, escort cards)?, design rounds included |

## Outreach

Use the prompt in [[../generators/vendor-outreach-generator]] to draft a first message. The Planner will personalize it per vendor before sending.

## Tracker

The interactive table is at [[tracker.csv]] — sort by status to see the current pipeline.
