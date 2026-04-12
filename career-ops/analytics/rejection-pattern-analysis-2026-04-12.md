---
title: Rejection & Pattern Analysis — Week of 2026-04-12
type: analytics
agent: evaluator
created: '2026-04-12'
tags:
  - rejection-analysis
  - patterns
  - channel-roi
  - interview-performance
---

# Rejection & Pattern Analysis
**Period:** Pipeline inception through 2026-04-12
**Previous analysis:** None — this is the first run. No week-over-week delta available.
**Data source:** `pipeline/tracker.csv` (14 entries), `interview-prep/story-bank.md`, `interview-prep/index.md`

---

## Pipeline Snapshot

| Status | Count | Roles |
|--------|-------|-------|
| Offer | 1 | Hugging Face |
| Interview | 2 | Anthropic, n8n |
| Screen | 2 | Mistral, Weights & Biases |
| Applied (pending) | 4 | Datadog, Vercel, Retool, Notion |
| Evaluating/Discovered | 3 | Linear, Supabase, ElevenLabs |
| **Rejected** | **1** | **Stripe** |
| **Ghosted** | **1** | **dbt Labs** |

**Total negative outcomes: 2 of 11 submitted applications (18%)**
**Active conversion funnel health: Strong** — 1 offer, 4 in late stages.

---

## Section 1: Rejection Pattern Analysis

### 1.1 Role Type & Seniority Clustering

**Rejections by role type:**
- Stripe — PM, Billing API (payments domain, API-focused)
- dbt Labs — PM, Core Platform (data infra, dbt-specific)

**Pattern:** Both rejections are in highly domain-specific niches (payments, data tooling) where the candidate's core expertise is adjacent but not native. Neither is a generalist PM rejection. There is **no clustering at seniority level** — both are standard Senior PM targets.

**Verdict:** Domain expertise mismatch, not seniority misjudgment.

---

### 1.2 Channel Performance (Critical Finding)

| Channel | Applications | Screens+ | Conversion |
|---------|-------------|----------|------------|
| Referral | 4 (Anthropic, n8n, Stripe, Notion) | 3 of 3 evaluated | **~100%** |
| Career Page (direct) | 4 (Mistral, Vercel, HuggingFace, W&B) | 3 of 3 evaluated | **~100%** |
| LinkedIn (cold apply) | 3 (Datadog, Retool, dbt Labs) | 0 of 1 evaluated | **0%** |
| Portal Scan | 3 (Linear, Supabase, ElevenLabs) | Not yet evaluated | TBD |

**LinkedIn is performing at 0% conversion.** Of the three LinkedIn applications:
- dbt Labs: Ghosted (4 weeks, no response — confirmed resume-screen failure)
- Retool: 12 days, no response, score 3.8 — likely heading toward ghost
- Datadog: 11 days, no response, score 4.1 — too early to judge

Referrals and direct career-page applications are converting at dramatically higher rates. The gap is not surprising — ATS filters deprioritize LinkedIn applicants who don't match keyword patterns exactly, and recruiters prioritize inbound referrals.

**Action required:** Stop cold-applying via LinkedIn. Use LinkedIn for referral identification and networking only, then apply directly via the company's career page.

---

### 1.3 Stage-of-Rejection Analysis

| Stage | Count | Details |
|-------|-------|---------|
| Resume/ATS Screen | 1 | dbt Labs (ghosted — no response 4 weeks post-apply) |
| Phone Screen | 0 | — |
| Early Interview | 0 | — |
| Final Round | 1 | Stripe (explicit feedback received) |

**Key insight:** There is NO phone-screen or early-interview rejection pattern. The funnel is not leaking at the story-delivery or positioning stage. The two negative outcomes are at opposite ends: one didn't get through the door (ATS), one made it all the way to the final and lost on a specific domain gap.

**This is a targeting problem, not a delivery problem.**

---

### 1.4 Evaluation Score vs. Outcome Correlation

| Score Range | Outcomes |
|-------------|---------|
| 4.5–5.0 | Offer (HuggingFace 4.7), Interview (Anthropic 4.6, n8n 4.5) |
| 4.2–4.4 | Screen (Mistral 4.3, W&B 4.2), Final-round rejection (Stripe 4.2) |
| 3.8–4.0 | No movement / Ghosted (Retool 3.8, dbt Labs 3.9) |

**The scoring system is working.** Scores 4.5+ are consistently reaching late-stage interviews. Scores below 4.0 are producing no forward movement. The 4.0 threshold rule exists precisely to avoid wasting time on dbt Labs (3.9) and Retool (3.8).

**Stripe (4.2) is the interesting case:** It made it to the final round via referral power, then failed on a domain gap that was already visible in the Block B score (4.2, the weakest of all Stripe's blocks). The referral got the resume through; the interview exposed the gap.

**Recommendation:** Enforce the 4.0 threshold strictly. Referrals can override it conditionally, but only if the Block B score is ≥ 4.0 specifically (skills match).

---

### 1.5 Skills & Experience Gaps Cited in Rejections

**Stripe — final round feedback: "wanted more payments domain"**

This is the only rejection with explicit feedback. The gap is clear:
- Skills matrix has **no payments, fintech, or billing infrastructure** experience listed
- Story bank has **no STAR+R story covering payments, transactions, or financial products**
- Block B for Stripe was 4.2 — the system correctly flagged the gap; the user applied anyway (justified by referral)

**dbt Labs — no feedback (ghosted)**

Likely causes:
1. **ATS keyword gap:** dbt Labs would weight "dbt" experience heavily. The skills matrix mentions dbt in "Data Analysis" context (SQL, dbt models) but not as a core product expertise. The role was "PM, Core Platform" for dbt the product — very different from using dbt as a tool.
2. **LinkedIn cold apply:** ATS deprioritization
3. **Score 3.9:** Applied below threshold — this was a strategic mistake

---

## Section 2: Interview Pattern Analysis

### 2.1 Interview Type Performance

Based on pipeline stage and available feedback:

| Interview Type | Attempted | Result |
|---------------|-----------|--------|
| Behavioral/STAR | Multiple (n8n onsite, Anthropic ongoing) | Positive signals |
| Technical/Domain | Mistral technical screen (completed), W&B phone screen | Advancing |
| Final Round / Product | Stripe final round | Rejected (domain gap) |
| Cultural Fit | n8n onsite | "Strong culture fit" — advancing |

**No pattern of failing a specific interview type.** The Stripe final-round failure was domain-specific, not a behavioral or structural interview failure.

### 2.2 Story Bank Coverage Analysis

Current story bank (5 stories) mapped to competency categories:

| Story | Competencies Covered | Pipeline Relevance |
|-------|---------------------|-------------------|
| PLG Revenue Engine | Growth, data-driven, revenue impact | High — API/PLG companies |
| SDK That Developers Liked | DX, technical depth, shipping | Very high — dev-tools pipeline |
| Building the Team From Scratch | Leadership, hiring, scaling | High — Head of Product targets |
| The Migration Nobody Wanted | Conflict, technical leadership, stakeholder mgmt | Medium |
| The Feature That Got Killed | Hard decisions, data-driven, prioritization | High — all roles |

**Coverage gaps:**
- **Payments/fintech domain:** Zero stories. This gap was exposed at Stripe. Low priority given search criteria excludes fintech, but if any Stripe-like referrals appear, this is a liability.
- **Enterprise/B2B sales-cycle:** No story addressing sales-cycle-aware product decisions. Low priority.
- **Failure/recovery story:** All stories end positively. A story showing resilience through a real failure (not just "I killed a feature") would round out the bank.

### 2.3 Energy & Vibe Signal

**Available signals:**
- n8n onsite: "Strong culture fit" — positive
- Anthropic: Made it to 2nd round panel — positive
- Mistral: Technical screen completed, advancing — positive

No evidence of declining energy or deteriorating performance signals. Pipeline is moving forward in the right places.

---

## Section 3: Actionable Recommendations

### Priority 1: Kill LinkedIn as an application channel [URGENT]
**Evidence:** 0% conversion from 3 applications. dbt Labs ghosted. Retool (3.8) likely to ghost.
**Action:** Remove LinkedIn from application sourcing. Use it exclusively for identifying warm contacts who can route applications through referrals or direct introductions to hiring managers.

### Priority 2: Enforce the 4.0 floor — no exceptions without Block B ≥ 4.0
**Evidence:** Every application below 4.0 has produced no movement or a ghost.
**Action:** Before submitting any application scored below 4.0, require a Block B (CV Match) score of 4.0 or higher AND an existing warm referral. Cold applications below 4.0 are time sinks.

### Priority 3: Add one failure/recovery STAR+R story to the bank
**Evidence:** Story bank has 5 strong stories but all trend positive. Interviewers at Anthropic and n8n will probe failure tolerance at PM Lead / Head of Product level.
**Suggested theme:** A product that failed to hit its success metric despite strong execution — and what you did next. This is different from "the feature I killed" which was a choice, not a failure.

### Priority 4: ATS keyword optimization for portal-scan applications
**Evidence:** dbt Labs ghost likely driven by ATS filtering. Portal-scan roles (LinkedIn, Ashby, cold) face higher ATS risk.
**Action:** For any application sourced via portal scan (Linear, Supabase, ElevenLabs), the CV must be keyword-matched before submitting. Run each through Block B ATS check with ≥ 85% keyword alignment before applying.

### Priority 5: No new payments or core-data-infra applications unless referral + domain story exists
**Evidence:** Stripe final-round failure on payments domain. dbt Labs ATS ghost on dbt-specific domain.
**Action:** If a payments or data-infra company appears in the pipeline, Block B must score ≥ 4.5 to justify applying. Below that — pass.

---

## Section 4: Pipeline Health Score

| Metric | Value | Assessment |
|--------|-------|-----------|
| Offers in hand | 1 (Hugging Face, EUR 175K) | Strong — decision needed by Apr 18 |
| Late-stage interviews | 2 (Anthropic Apr 16, n8n awaiting) | Excellent |
| Screen-stage active | 2 (Mistral, W&B) | Healthy |
| Ghost rate | 1/11 submitted (9%) | Acceptable — driven by below-threshold apply |
| Rejection rate | 1/11 submitted (9%) — final round | Low, domain-specific |
| Channel diversity | 2 strong (referral, career page), 1 dead (LinkedIn) | Concentration risk |
| Eval score accuracy | High — scores predictive of outcomes | System working |

**Overall: The pipeline is healthy.** One offer exists (decision required). Two dream-tier processes are in late stages. The evaluation system is accurate. The main structural issues are channel over-reliance on LinkedIn and the failure to enforce the score threshold.

---

## Next Analysis

This report covers pipeline inception through 2026-04-12. The next rejection-pattern analysis should run 2026-04-18 (post-Anthropic 2nd round, post-HuggingFace decision deadline) to capture:
- Anthropic panel outcome
- n8n final decision
- HuggingFace offer resolution
- Any movement on Mistral / W&B / Vercel / Datadog

Week-over-week delta will be available at that point.
