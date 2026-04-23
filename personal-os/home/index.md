---
title: Home
created: '2026-04-23T00:00:00Z'
modified: '2026-04-23T00:00:00Z'
tags:
  - home
  - bills
  - maintenance
order: 3
---
# Home

The **building** side of the household. Bills, utilities, maintenance, warranties, groceries.

People and their schedules live in `family/`. Money goes in `money/`. This cabinet is about the physical dwelling and the stuff that flows through it.

## What lives here

- `bills.md` — every recurring bill. Provider, amount, due date, auto-pay status.
- `utilities.md` — gas, electric, water, internet. Account numbers, meter reads, historical usage.
- `maintenance/` — what was serviced when. Next-service dates.
- `warranties.md` — appliances, roof, HVAC. Purchase date, warranty end, receipts.
- `groceries/` — recurring list, pantry log, delivery preferences.
- `vendors.md` — plumber, electrician, HVAC, cleaner. Phone, last used, rating.
- `briefs/` — weekly home brief.

## Team

- **Home Ops** — maintenance calendar, vendor coordination, "when was the HVAC serviced," "why is the gutter sagging."
- **Bills Clerk** — every bill accounted for. Due dates. Auto-pay status. Anomaly flags.

## Weekly rhythm

- **Monday morning** — Bills Clerk runs the week's due-list and flags anything that jumped >15% vs last month.
- **First Monday of the month** — Home Ops runs the maintenance calendar. "You're due for: [X]."
- **As needed** — anomaly alerts (water bill spike? possible leak).

## Bills template

```
| Provider | Service | Amount | Due | Auto-pay | Last paid | Notes |
|----------|---------|--------|-----|----------|-----------|-------|
| ...      | ...     | ...    | ... | yes/no   | YYYY-MM-DD | ... |
```

## Maintenance schedule seed

- HVAC filter — every 90 days
- HVAC service — spring + fall
- Gutters — spring + late fall
- Smoke/CO detectors — battery annually, unit every 10y
- Water heater — flush annually
- Dryer vent — annually
- Dishwasher filter — quarterly
