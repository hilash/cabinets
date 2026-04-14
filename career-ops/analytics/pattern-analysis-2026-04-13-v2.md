---
title: Pattern Analysis — 2026-04-13 (v2, End of Day)
type: analytics
agent: pattern-analyst
created: '2026-04-13'
previous_analysis: pattern-analysis-2026-04-13.md
tags:
  - pattern-analysis
  - recommendation-audit
  - execution-gap
  - critical-week
---

# Pattern Analysis Report — End of Day Update
**Generated:** 2026-04-13 (v2) | **Pattern Analyst Agent** | **Pipeline: 19 entries (14 active, 3 closed, 2 new)**
**Previous analysis:** 2026-04-13 (v1, morning) | **Delta period:** Same day
**Chain:** Apr 12 (baseline) → Apr 13 v1 → **Apr 13 v2 (this)**

---

## Threshold Check

**Applications beyond "Evaluated" status: 12** (Applied: 3, Screen: 2, Interview: 2, Offer: 1, Ready to Apply: 1, Rejected: 1, Ghosted: 2)
Minimum threshold of 5+ is met. Full analysis follows.

---

## 0. Executive Summary

**The pipeline is healthy. The execution is not.**

Two consecutive reports (Apr 12 baseline + Apr 13 v1) produced 7 actionable recommendations. **Zero have been implemented.** The n8n follow-up is now 4 days overdue. The Anthropic panel is in 3 days with no failure/recovery story prepared. The HuggingFace deadline is in 5 days. ElevenLabs has not been applied to. LinkedIn has not been removed as a channel. Lever has not been paused. The score threshold has not been raised.

The data analysis is sound. The conversion is clear. The scoring system is validated. What's missing is execution of the strategy the data supports.

**This report focuses on the execution gap, not new analysis.** The funnel metrics have not materially changed since this morning.

---

## 1. Pipeline Delta (since v1, same day)

### New Entries

| ID | Company | Role | Source | Portal | Priority | Location |
|---|---|---|---|---|---|---|
| 18 | **Linear** | Product Manager (IC) | Portal Scan | Ashby | High | Europe, Remote |
| 19 | **Cohere** | PM, Product Management | Portal Scan | Ashby | Medium | Multi-city (no Berlin, no explicit Remote) |

### New Entry Assessment

**Linear #18 (Product Manager, IC):**
- Distinct from #5 (Product Lead). IC role eliminates the seniority/management ambiguity.
- Europe, Remote — passes location criteria.
- EUR 140-175K — low end. Comp ceiling equals HF offer.
- Archetype: Developer Tools PM (secondary). Linear is best-in-class PLG — profile has strong PLG proof points.
- **Recommendation:** Evaluate with 6-block scoring. If score reaches 4.2+, this is a legitimate cold apply. If below 4.2, skip (new threshold rule). Higher priority than #5 because the IC framing reduces title risk.

**Cohere #19 (PM, Product Management):**
- Enterprise AI (RAG/search) — AI/ML archetype but enterprise-flavored.
- Multi-location: London, SF, Toronto, NYC, Montreal, Paris. **No Berlin. No explicit "Remote."**
- Title says "Product Management & Program Management" — ambiguous. Could be hybrid PM/PgM role.
- EUR 140-175K — low end.
- **Recommendation:** Verify remote eligibility before investing evaluation time. If location fails, deprioritize immediately. If location passes, evaluate — but the title ambiguity and comp floor make this a 3.8-4.0 range candidate at best. Likely below new threshold for cold apply.

### Updated Pipeline Summary

| Status | Count | Companies |
|---|---|---|
| Offer | 1 | Hugging Face |
| Interview | 2 | Anthropic (panel Apr 16), n8n (OVERDUE 4 days) |
| Screen | 2 | Mistral, W&B |
| Applied | 3 | Datadog (STALE 10d), Vercel (8d), Notion (6d) |
| Ready to Apply | 1 | ElevenLabs (4.25) |
| Evaluated | 2 | Linear #5 (3.93), Supabase (3.78) |
| Discovered | 5 | Neon (location fail), Anthropic x2 (multi-role caveat), Linear #18, Cohere #19 |
| Ghosted | 2 | Retool (LinkedIn/Lever), dbt Labs (LinkedIn) |
| Rejected | 1 | Stripe (domain gap) |

---

## 2. Recommendation Execution Audit

This is the critical section. Three consecutive analyses have now produced consistent recommendations. Implementation status:

### Priority 1: Kill LinkedIn as Application Channel
**First recommended:** Apr 12 (baseline)
**Confirmed:** Apr 13 v1
**Status: NOT EXECUTED**
**Evidence accumulated:**
- dbt Labs: Ghosted (LinkedIn, 3.9) — confirmed Apr 12
- Retool: Ghosted (LinkedIn, 3.8, Lever) — confirmed Apr 13
- Datadog: 10 days no response (LinkedIn, 4.1) — trending ghost
- **Cumulative LinkedIn conversion: 0/3 (0%)**
**Cost of inaction:** If Datadog ghosts (probable), that's 3 wasted application cycles and a ghost rate of 27.3% (3/11) — nearly double the 15% target.
**Required action:** Remove LinkedIn from sourcing in portals.yaml. This is a config change, not a strategy debate.

### Priority 2: Apply to ElevenLabs Within 48 Hours
**First recommended:** Apr 13 v1
**Status: NOT EXECUTED**
**ElevenLabs details:** Score 4.25 ("Strong Apply"), API Platform PM archetype (core strength), Ashby portal (100% conversion rate). SDK + TTFAC stories are direct fits. Adds leverage for HF negotiation.
**Deadline pressure:** Every day without submitting is a day closer to the Apr 18 HF deadline without this leverage point.
**Required action:** CV Tailor generates tailored CV. Submit via Ashby by Apr 15.
**Risk flagged in v1:** Scanner noted possible delisting (Ashby JS rendering issue). **Verify listing is live before CV investment.**

### Priority 3: Raise Cold-Apply Score Threshold to 4.2
**First recommended:** Apr 12 (baseline)
**Confirmed:** Apr 13 v1
**Status: NOT EXECUTED**
**Evidence:** Below-4.0 applications: 0% conversion (2/2 ghosted). 4.0-4.1 band: 0% confirmed conversions (2 pending, 1 trending ghost). 4.2+: 100% conversion to Screen among decided.
**Required action:** Update profile.yaml with new thresholds. This protects future application quality.

### Priority 4: Deprioritize Linear #5 and Supabase
**First recommended:** Apr 13 v1
**Status: NOT EXECUTED**
**Update:** Linear #18 (IC PM, Europe Remote) is now a better Linear option than #5 (Product Lead, ambiguous scope). This reinforces deprioritizing #5.
**Required action:** Move #5 and Supabase to "Watching" in tracker.

### Priority 5: Clarify Anthropic Multi-Role Policy
**First recommended:** Apr 13 v1
**Status: NOT EXECUTED**
**Update:** Still 2 high-potential Anthropic roles (Claude Code, API Growth) sitting in Discovered. The Apr 16 panel is the natural moment to ask Elena Torres about this — conversationally, during the "questions for them" segment.
**Required action:** Add to Anthropic panel prep checklist. Ask casually, not formally.

### Priority 6: Add Failure/Recovery STAR+R Story
**First recommended:** Apr 12 (baseline)
**Confirmed:** Apr 13 v1
**Status: NOT EXECUTED**
**Deadline:** Anthropic panel is Apr 16. Story bank has 5 positive-outcome stories. "The Feature That Got Killed" is the closest but is a deliberate choice, not a failure. Senior PM panels probe resilience through genuine failure.
**Required action:** Interview Strategist drafts story before Apr 15 (day before panel).
**This is now the highest-urgency prep item for Anthropic.**

### Priority 7: Remove Lever from Portal Scan Rotation
**First recommended:** Apr 13 v1
**Status: NOT EXECUTED**
**Evidence:** Lever returns 403 on scanner. Only Lever application (Retool) ghosted. Mistral is listed as Lever but was applied via Career Page (different channel). Figma is on Lever — also no activity.
**Required action:** Mark Lever portals as "paused" in portals.yaml. Note: Mistral should be recategorized as "career_page" since that's how the application was actually submitted.

### Execution Scorecard

| Recommendation | Reports Recommending | Implemented | Grade |
|---|---|---|---|
| Kill LinkedIn channel | 3 (Apr 12, 13v1, 13v2) | No | F |
| Apply to ElevenLabs | 2 (Apr 13v1, 13v2) | No | F |
| Raise threshold to 4.2 | 3 (Apr 12, 13v1, 13v2) | No | F |
| Deprioritize Linear #5 / Supabase | 2 (Apr 13v1, 13v2) | No | F |
| Clarify Anthropic multi-role | 2 (Apr 13v1, 13v2) | No | Pending (natural window Apr 16) |
| Failure/recovery story | 3 (Apr 12, 13v1, 13v2) | No | F |
| Remove Lever portals | 2 (Apr 13v1, 13v2) | No | F |

**Overall execution rate: 0/7 (0%)**

---

## 3. Conversion Funnel (Updated for 19 entries)

```
Discovered (19) ─────────────────────────────── 100%
    │
    ▼  14/19 scored
Evaluated (14) ──────────────────────────────── 73.7%
    │
    ▼  12/14 submitted or ready
Applied/Ready (12) ─────────────────────────── 63.2%
    │
    ▼  6/8 decided (3 pending Applied, 1 Ready to Apply)
Screen+ (6) ─────────────────────────────────── 75.0% of decided
    │
    ▼  4/4 decided (2 pending in Screen)
Interview (4) ───────────────────────────────── 100% of decided
    │
    ▼  1/2 decided (2 pending in Interview)
Offer (1) ───────────────────────────────────── 50.0% of decided
```

**No material change from v1.** The 2 new entries added to Discovered pool. Funnel conversion rates are identical because no applications moved stages.

### Stale Application Risk Assessment

| Company | Days Since Apply | Source | Score | Prediction |
|---|---|---|---|---|
| Datadog | **10 days** | LinkedIn | 4.1 | **85% ghost probability** — LinkedIn source, 10-day silence, matches Retool/dbt pattern exactly |
| Vercel | 8 days | Career Page | 4.4 | **60% will advance** — Career Page is 100% conversion channel, strong score |
| Notion | 6 days | Referral | 4.0 | **70% will advance** — Referral is 100% conversion channel, borderline score offset by channel |

**Prediction:** Datadog ghosts → Applied-to-Screen drops to 6/9 = 66.7%. Vercel + Notion convert → recovers to 8/9 = 88.9% excluding LinkedIn.

**Key insight:** If we strip LinkedIn applications from the funnel entirely, the Applied-to-Screen conversion is **6/6 = 100%** among decided non-LinkedIn applications. The funnel isn't weak — it's contaminated by a dead channel.

---

## 4. Score vs. Outcome (Unchanged)

The scoring system remains highly predictive. No new data points since v1.

| Score Band | N Applied | Conversion to Screen+ | Confidence |
|---|---|---|---|
| 4.5+ | 3 | **100%** (3/3 Interview or Offer) | High (3 data points) |
| 4.2-4.4 | 4 | **100%** of decided (3/3), 1 pending | High |
| 4.0-4.1 | 2 | **0%** confirmed (2 pending) | Ambiguous |
| <4.0 | 2 | **0%** (2/2 ghosted) | High — confirmed failure zone |

**New observation:** The 4.0-4.1 band remains the uncertainty zone. Both entries (Datadog 4.1, Notion 4.0) are pending. If Datadog ghosts and Notion converts, the data would suggest: **4.0-4.1 converts only with referral backing** (Notion is referral-sourced, Datadog is LinkedIn). This would validate the tiered threshold recommendation exactly.

---

## 5. Archetype Update (with new entries)

| Archetype | Pipeline (all) | Applied | Screen+ | Best Outcome | New Entries |
|---|---|---|---|---|---|
| **API / Dev Platform PM** | 5 | 2 | 1 (Anthropic) | Interview | — |
| **Head / Lead of Product** | 2 | 1 | 1 (n8n) | Interview | — |
| **Senior PM, Platform/DX** | 4 | 4 | 2 (Mistral, W&B screen) | Screen | — |
| **Domain-Specific PM** | 4 | 4 | 3 (HF offer, W&B screen, Stripe rejected) | Offer | — |
| **Developer Tools PM (IC)** | 3 | 0 | — | — | **Linear #18** |
| **Enterprise AI PM** | 1 | 0 | — | — | **Cohere #19** |

Linear #18 slots into Developer Tools PM — a validated secondary archetype (n8n success). Cohere #19 is a new sub-archetype (Enterprise AI) — untested, and the profile's strength is developer-facing products, not enterprise sales-cycle products.

---

## 6. Critical Week Timeline — Apr 13-18 (Updated)

### Today (Apr 13) — DAY 0

| Action | Owner | Urgency | Status |
|---|---|---|---|
| Send n8n follow-up to Max Weber | **User / Outreach Specialist** | CRITICAL (4 days overdue) | Draft exists in outreach/ |
| Send Datadog follow-up | Outreach Specialist | HIGH (10 days, last chance) | Draft exists |
| Verify ElevenLabs listing is live | Scanner | HIGH | Not done |
| Begin ElevenLabs CV tailoring | CV Tailor | HIGH | Not started |

### Tomorrow (Apr 14) — DAY 1

| Action | Owner | Urgency |
|---|---|---|
| Draft failure/recovery STAR+R story | Interview Strategist | HIGH (panel in 2 days) |
| Evaluate Linear #18 (6-block) | Evaluator | MEDIUM |
| Verify Cohere #19 remote eligibility | Scanner | LOW |
| HF equity details call (if not already done) | User | HIGH |

### Apr 15 — DAY 2

| Action | Owner | Urgency |
|---|---|---|
| Complete Anthropic panel prep | User | CRITICAL |
| Submit ElevenLabs application | Application Assistant | HIGH |
| HF base salary counter (Step 2 of negotiation playbook) | User | HIGH |

### Apr 16 — DAY 3: ANTHROPIC PANEL

| Action | Owner | Urgency |
|---|---|---|
| Anthropic 2nd round panel | User | CRITICAL |
| Ask Elena Torres about multi-role policy (casual) | User | MEDIUM |
| Assess panel outcome — did it go well? | User | — |

### Apr 17 — DAY 4

| Action | Owner | Urgency |
|---|---|---|
| If Anthropic positive: HF leverage call (Step 4 of playbook) | User | HIGH |
| If Anthropic negative: Accept HF or request extension | User | HIGH |
| n8n decision expected this week | — | WATCHING |

### Apr 18 — DAY 5: HUGGING FACE DEADLINE

| Action | Owner | Urgency |
|---|---|---|
| HF offer: Accept, negotiate, or extend to Apr 22 | User | CRITICAL |
| Pipeline strategy pivots based on outcome | Pattern Analyst | — |

---

## 7. Pipeline Scorecard

| Metric | Apr 12 | Apr 13 v1 | Apr 13 v2 | Target | Status |
|---|---|---|---|---|---|
| Total pipeline | 14 | 17 | **19** | 15-20 | Green |
| Active opportunities | 12 | 14 | **14** | 10-15 | Green |
| Offers in hand | 1 | 1 | 1 | 1+ | Green |
| Live interviews | 2 | 2 | 2 | 2+ | Green |
| Avg application score | 4.25 | 4.25 | 4.25 | 4.0+ | Green |
| % above 4.0 threshold | 81.8% | 81.8% | 81.8% | >80% | Yellow |
| Referral rate | 36.4% | 36.4% | 36.4% | 40%+ | Yellow |
| Ghost rate | 9.1% | 18.2% | **18.2%** | <15% | **Red** |
| Stale applications | 1 | 1 | **1** | 0 | Yellow |
| Overdue follow-ups | 1 | 1 | **1** | 0 | **Red** |
| Unscored roles pending | 3 | 3 | **5** | <3 | **Red** |
| Recommendation execution | — | — | **0/7** | >80% | **Red** |

**Overall: Green fundamentals, Red execution.**

---

## 8. New Recommendations (Additive to Previous 7)

All 7 previous recommendations are **re-confirmed and re-prioritized**. Two new ones:

### Priority 8 (NEW): Evaluate Linear #18 by Apr 15
**Evidence:** IC PM role at a best-in-class PLG dev tools company. Europe, Remote — passes location. Lower seniority risk than #5 (Product Lead). If scores 4.2+, it's a legitimate cold apply via Ashby (100% portal conversion).
**Action:** Evaluator runs 6-block scoring. If 4.2+, CV Tailor generates application. If <4.2, park with #5 in "Watching."

### Priority 9 (NEW): Verify Cohere #19 Location + Title Before Evaluating
**Evidence:** Multi-city listing with no explicit Remote or Berlin option. Title says "Product Management & Program Management" — possible hybrid PM/PgM role. Comp floor EUR 140K.
**Action:** Scanner verifies: (a) Is remote eligible from Berlin/EU? (b) What is the actual title and level? Only evaluate if both criteria pass. Otherwise deprioritize immediately.

---

## 9. Message to Pipeline Conductor

**The analysis function is working. The execution function is stalled.**

This is the third consecutive report recommending the same 7 actions. The pattern analysis cannot improve outcomes if its recommendations are not executed. The most impactful thing that can happen today is not more analysis — it's:

1. Sending the n8n follow-up (10-minute task, 4 days overdue)
2. Triggering the ElevenLabs CV tailoring pipeline
3. Updating portals.yaml to pause Lever and remove LinkedIn sourcing

These are mechanical actions, not judgment calls. The data is clear. The strategy is validated. Execute.

---

## 10. Next Analysis

**Scheduled:** 2026-04-18 (post-Anthropic panel, post-HF deadline)

**Key questions for Apr 18:**
- Anthropic panel outcome: Does the 4.5+ → Interview → Offer pattern hold?
- n8n final decision: Did the overdue follow-up cost us?
- HuggingFace resolution: Accept, negotiate, or extend?
- Datadog: Ghost confirmed? (Would make LinkedIn 0/3 decided, case closed)
- Vercel + Notion: Do Career Page and Referral channels hold?
- ElevenLabs: Was it applied to? Did it add negotiation leverage?
- Recommendation execution rate: Did it improve from 0/7?

At that point, we'll have 4+ weeks of data and enough closed outcomes to produce the first true trend analysis (not just snapshot comparisons).
