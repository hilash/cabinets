---
title: Keto HQ
created: '2026-04-23T00:00:00Z'
modified: '2026-04-23T00:00:00Z'
tags:
  - keto
  - nutrition
  - protocol
  - specialty
order: 1
---
# Keto HQ

A specialty cabinet for running a ketogenic protocol. Installs standalone or alongside Personal OS — if `personal-os/health/` exists, Keto HQ reads labs, weight, and workouts from it and stays in lane on diet.

**Not a doctor.** Informational layer for adults without contraindications. See [[sources/keto/contraindications]].

## What lives here

- `profile.md` — goal (therapeutic / metabolic health / body comp), starting metrics, medical context.
- `targets.md` — your macro targets and electrolyte plan.
- `logs/` — daily intake + ketone readings (CSV or markdown).
- `meals/` — go-to meals, rotations, pantry staples.
- `stalls/` — diagnostic notes from any plateau.
- `sources/keto/` — the evidence layer for this protocol.
- `briefs/` — weekly keto review + ad-hoc diagnostics.

## Team

- **Keto Coach** — weekly brief, adherence review, stall diagnostics, adjustments, electrolyte floor (sodium / potassium / magnesium).
- **Meal Architect** — meal rotation, macro-hit planning, pantry staples, grocery lists.

## Plugs into Personal OS

When `personal-os/health/` is present:

- Reads labs (fasting glucose, A1c, triglycerides, HDL, LDL, ApoB, uric acid, electrolytes) for interpretation.
- Reads `wearables/` for weight, HRV, workouts.
- Defers protocol-independent advice to Personal OS agents (Longevity Physician reads labs, Strength Coach programs training). Keto HQ only adds keto-specific lenses.
- Writes its weekly brief both locally and as a cross-posted summary to `personal-os/health/briefs/keto-week-YYYY-WW.md` so the Care Coordinator can see it.

Standalone mode: just use the local `logs/` and let Keto HQ drive its own briefs.

## Goals the protocol can serve

1. **Metabolic health** — improve glucose control, triglycerides, HDL. Less strict; cyclical variants acceptable.
2. **Body composition** — fat loss in a satiating framework. Macros + resistance training + protein-forward.
3. **Therapeutic** — epilepsy, specific neurological indications, under physician direction. Different macro ratios and stricter.

State your goal in `profile.md` — agents calibrate recommendations accordingly.

## Weekly rhythm

- **Sunday 9am** — Keto Coach writes the weekly brief.
- **Sunday 9:30am** — Keto Coach reviews last week's electrolyte intake + symptoms.
- **Monday 10am** — Meal Architect publishes the week's meal rotation + grocery list.

## First-use checklist

1. Fill `profile.md` (goal, age, sex, weight, conditions, meds).
2. Check [[sources/keto/contraindications]] — proceed only if none apply.
3. Set targets via Keto Coach (first-run prompt).
4. Start logging in `logs/YYYY-MM.csv`.
5. Let the first weekly brief run after 7 days of logging.
