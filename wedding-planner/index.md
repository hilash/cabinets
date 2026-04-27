---
title: Wedding Planner
icon: "💍"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - wedding
  - planning
  - template
order: 1
---

# 💍 Wedding Planner

> A complete wedding-planning OS in a directory. Fill in three placeholders, run the bootstrap prompt, and your `Planner` agent builds your vendor matrix, timeline, budget, vow + speech generators, and a day-of runbook — all tuned to your specific wedding.

---

## ⚡ Bootstrap your Wedding OS

**Step 1.** Fill in the three placeholders below. Be specific.

**Step 2.** Open the AI panel on this page. Paste the prompt block. Run.

**Step 3.** Wait. The agent will: write `vision/index.md`, populate `vendors/tracker.csv` with categories scoped to your wedding type, generate the 18-month timeline backwards from your wedding date, populate `budget/tracker.csv` with realistic line items at your total budget, and draft an opening day-of runbook.

```
You are the Planner agent for this Wedding Planner cabinet. The couple has just filled in
the "Onboarding" section of index.md with three answers: who they are, their vision, and
their budget + date.

Read those three answers. Then build out the cabinet in this exact order:

1. Write `vision/index.md` based on the couple's answers. Lock in: couple names, wedding
   date, location/region, total guest count target, vibe/aesthetic, ceremony type
   (religious / civil / secular / blended), reception style (sit-down / cocktail /
   buffet / family-style), MUST-haves (3–5 items), MUST-NOTs (3–5 items), inherited
   constraints (family expectations, faith, cultural elements), three-word brief.

2. Populate `vendors/tracker.csv` with category rows scoped to the couple's wedding type.
   Standard categories: venue, catering, photographer, videographer, florist, music
   (DJ or band), officiant, attire (each side), rings, stationery, transportation,
   hair-and-makeup, cake/dessert, rentals. Add or remove based on the couple's vision
   (e.g. drop videographer if they explicitly said no video; add wine/bar separately
   if BYOB-style venue). For each row, set status=`prospecting`.

3. Generate `timeline/tracker.csv` working BACKWARDS from the wedding date. Use the
   standard 18-month milestones in `timeline/index.md`, scaled to the time the couple
   has remaining. Mark anything already in the past as `overdue` so the couple sees it.

4. Populate `budget/tracker.csv` with line items based on the standard breakdown
   (~50% venue+catering, ~12% photo+video, ~10% attire, ~10% flowers+décor, ~8% music,
   ~10% other), scaled to the couple's total budget. Adjust for known vision elements
   (smaller guest count = less venue spend, etc.).

5. Draft a starter `day-of/runbook.md` using `generators/day-of-timeline-generator.md`.
   It will be incomplete — the couple fills in actual times when vendors are booked,
   but the structure should be ready.

6. Append a "## ✅ Bootstrap complete — [YYYY-MM-DD]" block to this index.md with:
     - 3 specific vendors to contact this week (with template outreach from
       `generators/vendor-outreach-generator.md`)
     - Top 3 timeline milestones in the next 30 days
     - Budget reality check vs estimates

Rules:
- Use ONLY what the couple wrote in Onboarding. Do not invent traditions or preferences.
- If a placeholder is empty or vague, ask the couple to fill it in. Do not guess.
- Do not modify `generators/`, `day-of/runbook.md` once it has user data, or any
  vendor with status `booked`.
```

---

## 🧩 Onboarding — fill these in

### 1. Who are you?

> _Both names, how you met (if it informs the day), pronouns, where you live, where you'll get married. Any cultural / faith / family traditions that need to be honored. "Two non-religious software engineers in Berlin, getting married in Tuscany; bride's family is Italian Catholic, groom's is Jewish — we want both rituals condensed into a 20-minute secular ceremony" beats "we're getting married."_

```
_________
```

### 2. What is the vision?

> _Vibe in three words (e.g. "intimate, candlelit, joyful" / "big, loud, full of dancing" / "outdoors, casual, no formalities"). Guest count range. Ceremony style. Reception style. 3 must-haves. 3 must-NOTs. The thing you'd be most upset if it went wrong. The thing you genuinely don't care about that everyone tells you you should._

```
_________
```

### 3. What is the budget and date?

> _Total budget (be specific — "we have $40K and won't go over $45K" beats "around $40K"). Wedding date or target month. Time the couple can spend per week on planning. Whether one of you is doing more (so the planner pings the right person). Number of months to wedding. Any known constraints — family contributing? Inherited venue? Locked vendors?_

```
_________
```

---

## 📚 What is in this cabinet

| Page | What it is |
|---|---|
| [[vision/index]] | The wedding vision spec — populated by bootstrap |
| [[vendors/index]] | Vendor matrix + tracker |
| [[timeline/index]] | 18-month timeline + tracker |
| [[budget/index]] | Budget breakdown + tracker |
| [[generators/index]] | Vow, speech, vendor outreach, day-of timeline generators |
| [[day-of/index]] | The day-of runbook + emergency kit + family/wedding-party briefs |

## 🤖 Your team

- **💍 Planner** — sourcing, scheduling, budget, day-of. Runs Mondays for the weekly punch list. Runs the 1st of each month for the budget check.

## 🔁 What runs on a schedule

- **Weekly Progress Check** — Monday 9am. Overdue items + next 14 days + blockers.
- **Monthly Budget Check** — 1st of each month. Variance flags + headroom + recommendations.

## 🚀 After the bootstrap

1. Read `vision/index.md`. This is your bible — every decision flows from here.
2. Open `vendors/tracker.csv`. Start outreach to the top 3 vendors the agent flagged.
3. Open `timeline/tracker.csv`. Add owners (one of you) to each milestone.
4. Open `budget/tracker.csv`. Sanity-check the numbers against your reality.
5. The Monday agent runs the punch list. The 1st-of-month agent runs the budget check.
