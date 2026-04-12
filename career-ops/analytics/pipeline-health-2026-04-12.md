---
title: Pipeline Health Report — 2026-04-12
generated: '2026-04-12'
agent: evaluator
job: weekly-pipeline-health
---

# Pipeline Health Report
**Generated:** 2026-04-12 | **Evaluator Agent** | **Total Opportunities: 14**

---

## Pipeline Metrics

### Stage Distribution

| Status | Count | % of Total |
|---|---|---|
| Discovered | 1 | 7% |
| Evaluating | 2 | 14% |
| Applied | 4 | 29% |
| Screen | 2 | 14% |
| Interview | 2 | 14% |
| Offer | 1 | 7% |
| Rejected | 1 | 7% |
| Ghosted | 1 | 7% |
| Withdrawn | 0 | 0% |

**Active opportunities:** 12 | **Closed/Dead:** 2 (1 Rejected, 1 Ghosted)

### Conversion Rates

| Funnel Stage | Passed | Total | Rate |
|---|---|---|---|
| Discovery → Application | 11 | 14 | 78.6% |
| Applied → Screen+ (decided) | 6 | 7 | **85.7%** |
| Screen → Interview | 4 | 6 | **66.7%** |
| Interview → Offer (concluded) | 1 | 2 | **50.0%** |

> Applied → Screen rate is strong. 4 applications are still pending (Datadog, Vercel, Retool, Notion) and not included in the denominator.
> Stripe reached final round before rejection — counted in Interview → Offer concluded pool.

### Time in Stage (Active Opportunities)

| Company | Status | Applied | Days Waiting | Flag |
|---|---|---|---|---|
| Datadog | Applied | 2026-04-03 | 9 days | ⚠️ Stale tomorrow |
| Vercel | Applied | 2026-04-05 | 7 days | — |
| Retool | Applied | 2026-04-02 | **10 days** | 🔴 STALE |
| Notion | Applied | 2026-04-07 | 5 days | — |
| Mistral | Screen | 2026-03-28 | 15 days in process | — |
| W&B | Screen | 2026-04-01 | 11 days in process | — |
| Anthropic | Interview | 2026-03-22 | Next round Apr 16 | — |
| n8n | Interview | 2026-03-20 | Onsite done Apr 9 | 🔴 FOLLOW-UP OVERDUE |

### Pipeline Velocity

| Week | New Discovered | Closures | Net |
|---|---|---|---|
| Mar 10–16 | 3 (dbt Labs, HuggingFace, Stripe) | 0 | +3 |
| Mar 17–23 | 2 (n8n, Anthropic) | 0 | +2 |
| Mar 24–30 | 3 (Mistral, W&B, Retool) | 0 | +3 |
| Mar 31–Apr 6 | 3 (Datadog, Vercel, Notion) | 0 | +3 |
| Apr 7–12 | 3 (Linear, Supabase, ElevenLabs) | 0 | +3 |

**Average discovery rate:** 2.8/week
**Average closure rate:** 0.4/week (Stripe rejected Apr 5; dbt Labs ghosted ~Mar 26)
**Pipeline is growing.** At current velocity, active count will hit 16+ without closures by Apr 19.

---

## Quality Metrics

### Evaluation Score Analysis

**Scored applications:** 11 (of 14 total — 3 unscored: ElevenLabs, Linear, Supabase)

| Metric | Value | Target | Status |
|---|---|---|---|
| Average score (all applied) | **4.25** | — | Strong |
| % scoring 4.0+ | **81.8%** (9/11) | >80% | ✅ Passing |
| % scoring 3.5–3.9 | **18.2%** (2/11) | — | Acceptable |
| % scoring below 3.0 | **0%** | 0% | ✅ Clean |

**Below-threshold applications:**
- Retool (3.8) — applied despite note: "interesting domain." Now stale at 10 days.
- dbt Labs (3.9) — ghosted after 4 weeks. Predictable outcome.

### Referral vs. Cold Apply

| Channel | Applications | Interview+ | Rate |
|---|---|---|---|
| Referral | 4 (Anthropic, n8n, Stripe, Notion) | 3 (Anthropic, n8n, Stripe) | **75%** |
| Cold (Career Page, LinkedIn, Portal Scan) | 7 | 2 (Mistral→Screen, W&B→Screen, HuggingFace→Offer*) | ~42% |

> *HuggingFace came from Career Page (cold), reached Offer — exceptional outlier.
> Referral conversion to Interview is nearly 2× cold. This is signal.

### Channel Performance

| Source | Applications | Best Outcome | Verdict |
|---|---|---|---|
| Referral | 4 | 2× Interview, 1× Offer (pipeline) | **Best channel** |
| Career Page | 4 | 1× Offer (HuggingFace), 1× Interview (n8n via referral) | **Strong** |
| Portal Scan | 3 | Evaluating (no conversions yet) | Discovery only |
| LinkedIn | 3 | 0 beyond Applied (1 ghosted) | **Weak — reduce** |

| Portal Type | Applications | Best Outcome | Verdict |
|---|---|---|---|
| Greenhouse | 7 | 1× Offer (HuggingFace) | Reliable volume |
| Career Page (direct) | 2 | 1× Interview, 1× Rejected-final | High quality |
| Ashby | 3+ | 1× Interview (Anthropic) | Best for AI companies |
| Lever | 1 | Stale (Retool) | Avoid |

---

## Stale Detection

### 🔴 Applied — Stale (10+ Days, No Response)

| ID | Company | Applied | Days Stale | Action Required |
|---|---|---|---|---|
| 8 | **Retool** | 2026-04-02 | **10 days** | Send follow-up or withdraw. Below threshold anyway. |

### ⚠️ Applied — Approaching Stale (7–9 Days)

| ID | Company | Applied | Days | Action Required |
|---|---|---|---|---|
| 3 | **Datadog** | 2026-04-03 | 9 days | Send follow-up email today. Goes stale tomorrow. |

### Evaluating — Unscored (7+ Days)
No violations. Linear (4 days) and Supabase (3 days) are within window. ElevenLabs entered Discovered 2 days ago.

### 🔴 Interview — Follow-Up Overdue (24h+ After Onsite)

| ID | Company | Onsite Date | Days Overdue | Action Required |
|---|---|---|---|---|
| 7 | **n8n** | 2026-04-09 | **3 days** | Send thank-you / follow-up to Max Weber (CTO) immediately. |

---

## Urgent Action Items

### 🚨 Time-Critical (This Week)

1. **Anthropic panel prep — 4 days** (Apr 16). 2nd round panel. Dream role. This gets maximum prep time. Pull story-bank, run mock questions, research panelists.
2. **n8n follow-up — NOW** (3 days overdue). Onsite went well + CTO contact (Max Weber). A gracious follow-up is expected. Silence reads as disinterest.
3. **Hugging Face offer decision — 6 days** (deadline Apr 18). EUR 175K + equity. Evaluate against pipeline before accepting or negotiating.
4. **Datadog follow-up — TODAY** (goes stale tomorrow, Apr 13). Brief, professional nudge.

### High Priority (This Week)

5. **Evaluate ElevenLabs** (ID 10). High-priority AI company. Discovered 2 days ago. Score it before it ages past 7 days.
6. **Score Linear** (ID 5). Product Lead role. Discovered 4 days ago. Run 6-block eval this week.
7. **Score Supabase** (ID 6). Open source angle noted. Discovered 3 days ago.

### Consider Deprioritizing

8. **Retool** (ID 8). 10-day stale, below threshold (3.8), LinkedIn source (weakest channel). Consider withdrawing and freeing mental bandwidth.

---

## Strategy Recommendation

### What to Focus on This Week

**Your pipeline is in a strong position but has a critical crunch point.**

You have 1 offer (HuggingFace, EUR 175K) and 2 live interviews (Anthropic — dream role; n8n — cultural fit confirmed). The next 7 days determine whether you convert one or both.

**Priority order:**

1. **Anthropic prep is #1** — Panel in 4 days, referral-sourced, highest score in pipeline (4.6). Do not let analytics admin eat panel prep time.
2. **Fix the n8n follow-up** — Every day without contact after an onsite is a small signal of disinterest. Send it now.
3. **HuggingFace offer framing** — Don't accept on first contact. Use Anthropic and n8n timelines to request until Apr 18. Understand equity terms before deciding.
4. **Score the 3 unscored roles** — ElevenLabs, Linear, Supabase. One of these could be the hedge that improves your negotiation position.

### Are You Applying to Too Many Low-Score Roles?

No — but borderline. 81.8% above 4.0 is just over the threshold. The two below-threshold applications (Retool, dbt Labs) both performed as expected: one stale, one ghosted. Stop making exceptions to the score floor. The notes in both cases acknowledged the rule-break at time of application. Trust the score.

### Is the Pipeline Thin or Dense Enough?

Pipeline density is appropriate for your stage (2 active interviews, 1 offer). If Anthropic and n8n both close without an offer, you have 6 active prospects behind them (4 Applied, 2 Screen) — adequate. If HuggingFace is your only offer, you have leverage pressure. Ensure Vercel and Notion get traction before Apr 18.

### Which Stage Is the Bottleneck?

**Applied → Screen** is not the bottleneck — 85.7% conversion of decided applications is excellent. The screen-to-interview transition (66.7%) and interview-to-offer (50%) are normal for senior roles. The actual bottleneck is **discovery source diversity**: LinkedIn produces 0% conversion past Applied. Redirect that effort to referrals and direct Career Page applications.

---

## Pipeline Scorecard

| Metric | Value | Status |
|---|---|---|
| Total pipeline | 14 | Healthy |
| Active opportunities | 12 | Good |
| Offers in hand | 1 | 🟢 |
| Live interviews | 2 | 🟢 |
| Average application score | 4.25 | 🟢 |
| % above 4.0 threshold | 81.8% | 🟡 (just over) |
| Referral rate | 36.4% | 🟡 (target: 40%+) |
| Stale applications | 1 | 🟡 |
| Overdue interview follow-ups | 1 | 🔴 |
| Unscored roles pending | 3 | 🟡 |

**Overall pipeline health: 🟢 Strong** — one critical action item (n8n follow-up) and one imminent deadline (Anthropic panel Apr 16).
