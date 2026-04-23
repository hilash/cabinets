---
title: Health
created: '2026-04-23T00:00:00Z'
modified: '2026-04-23T00:00:00Z'
tags:
  - health
  - labs
  - supplements
  - longevity
order: 5
---
# Health

Six specialists. One patient. Every recommendation cites a source.

This cabinet is **not a doctor**. It's a private operating layer that keeps your data organized, interprets trends, and drafts questions/protocols that you verify with your physician. Nothing here is medical advice.

## What lives here

- `profile.md` — age, sex, height, weight, conditions, medications, allergies, family history.
- `labs/` — blood panels. PDF + parsed CSV + interpretation notes.
- `wearables/` — exports (Apple Health, Garmin, Oura). Monthly rollups.
- `food/` — optional daily log or weekly snapshot.
- `workouts/` — program + sessions + PRs.
- `medications.md` — active meds with doses, timing, prescriber.
- `supplements.md` — current stack with rationale and source refs.
- `appointments/` — visit notes, questions for next visit.
- `sources/` — **the trust layer.** Every claim an agent makes points here.
- `briefs/` — weekly holistic brief + ad-hoc briefs.

## Team

| Agent | What they own |
|-------|---------------|
| **Care Coordinator** | Synthesizes the other five. Writes the weekly brief. Preps appointment questions. |
| **Protocol Scientist** | Sleep, light, temperature, timing, nervous-system protocols. |
| **Longevity Physician** | Labs interpretation, biomarker trends, age-adjusted reference ranges. |
| **Metabolic Dietitian** | Food, fasting, glucose, weight, macros. |
| **Strength Coach** | Programming, progressions, recovery, movement quality. |
| **Pharmacist** | Interactions, dosing, timing, supplement stack construction. |

## The trust rule

Every recommendation in every brief ends with a **Sources** block linking to files in `health/sources/`. If an agent wants to recommend something and can't find a source file for it, they must either **write the source file first** (with links to primary evidence) or **refuse the recommendation**.

See [[sources/index|Sources]].

## Weekly rhythm

- **Sunday 10am** — Care Coordinator runs the weekly holistic brief.
- **On new labs upload** — Longevity Physician produces an interpretation; Pharmacist + Dietitian review the supplement stack against new numbers.
- **Quarterly** — full supplement review.

## First-use checklist

1. Fill out `profile.md`.
2. Drop your most recent labs PDF into `labs/YYYY-MM/`.
3. List current meds in `medications.md` (prescriber, dose, timing, reason).
4. List current supplements in `supplements.md` (with why you started each).
5. Let the first weekly brief run. It will tell you what's missing.
