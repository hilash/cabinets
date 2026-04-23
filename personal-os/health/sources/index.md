---
title: Sources
created: '2026-04-23T00:00:00Z'
modified: '2026-04-23T00:00:00Z'
tags:
  - health
  - sources
  - evidence
order: 1
---
# Sources

This is the trust layer. Every recommendation in every health brief points back to a file here. No file → no recommendation.

## Structure

```
sources/
  supplements/     ← one file per supplement: mechanism, dose, UL, evidence
  protocols/       ← one file per behavioral protocol: light, cold, sleep, etc.
  labs/            ← reference ranges and interpretation guides
  biomarkers/      ← markers & what they mean at different life stages
  interactions/    ← supplement-drug and supplement-supplement interactions
  training/        ← programming principles, recovery research
  diet/            ← macronutrient, fasting, pattern evidence
```

## Source file format

Every source file follows this structure:

```markdown
---
title: [Topic]
last_reviewed: YYYY-MM-DD
evidence_tier: strong | emerging | anecdotal
---

# [Topic]

## Claim
[The specific recommendation this file backs.]

## Mechanism
[Brief, plain-language explanation.]

## Evidence
- [Guideline body name — year — key numbers — link]
- [Meta-analysis / systematic review — year — summary — link]
- [RCT(s) — year — design, N, effect size — link]

## Parameters
- Dose / duration / timing / population
- Upper limits / contraindications

## Who this does NOT apply to
[Conditions, medications, life stages that make this advice wrong.]

## Notes from [user's] labs / context
[Populated over time as agents reference this file.]
```

## Evidence tiers

- **Strong** — multiple RCTs, meta-analyses, or established clinical guidelines.
- **Emerging** — small trials, consistent observational data, or strong mechanistic rationale.
- **Anecdotal** — case reports, n=1 self-experiments, expert opinion.

Agents must label every claim by tier when citing.

## Seed entries

Start with these. Add more as agents reference new claims.

### Supplements
- [[supplements/vitamin-d]]
- [[supplements/omega-3]]
- [[supplements/magnesium-glycinate]]

### Protocols
- [[protocols/morning-light]]

### Labs
- [[labs/ferritin-ranges]]

## When an agent cites something not in `sources/`

The rule: **write the source file first, then make the recommendation.** If that's too much for a one-off suggestion, the agent flags the suggestion as `[unsourced — needs source file]` so it can't be acted on until verified.
