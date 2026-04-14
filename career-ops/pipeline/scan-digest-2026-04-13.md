---
title: Daily Scan Digest — 2026-04-13
agent: scanner
type: digest
date: '2026-04-13'
portals_scanned: 22
new_discoveries: 2
stale_flags: 1
location_verified: 1
portal_corrections: 2
---

# Scanner Daily Digest — Sunday 13 April 2026

## Summary

Second full portal scan. 22 portal endpoints checked across Greenhouse API, Ashby, Lever, and career pages.
**2 new roles added to pipeline** (IDs 18–19). **1 location verification** completed (ID 15 — fails criteria).
**2 portal type corrections** applied to portals.yaml (Mistral → Lever, Cohere → Ashby).

---

## New Discoveries

| ID | Company | Role | Priority | Location | Notes |
|----|---------|------|----------|----------|-------|
| 18 | **Linear** | Product Manager | **HIGH** | Europe, Remote | IC PM at best-in-class PLG dev tools company. Distinct from Product Lead (ID 5). Lower seniority risk. |
| 19 | **Cohere** | PM, Product Management | Medium | London + 5 offices | Enterprise AI (RAG/search). Verify exact title/level — listing bundles PM & Program Management. |

---

## Verification Updates

| ID | Company | Role | Update |
|----|---------|------|--------|
| 15 | Neon | Lead PM, Developer Experience | **LOCATION CONFIRMED: SF/NYC on-site only.** Fails location criteria. Deprioritized. |
| 10 | ElevenLabs | PM, API Platform | **Still unverified.** Second consecutive scan shows no PM titles on Ashby board (JS rendering issue). Stale flag persists. |

---

## Pipeline Snapshot (active + in-flight)

| ID | Company | Role | Status | Score | Urgency |
|----|---------|------|--------|-------|---------|
| 11 | Hugging Face | Senior PM, Hub | **Offer** | 4.7 | Decision deadline **Apr 18** (5 days) |
| 1 | Anthropic | PM, Claude API | **Interview** | 4.6 | Panel **Apr 16** (3 days) |
| 7 | n8n | Head of Product | **Interview** | 4.5 | Follow-up **OVERDUE** (4 days since onsite) |
| 2 | Mistral | Senior PM, Platform | Screen | 4.3 | Awaiting next round |
| 13 | W&B | PM, ML Ops | Screen | 4.2 | Awaiting onsite schedule |
| 4 | Vercel | Senior PM, DX | Applied | 4.4 | No response (8 days) |
| 10 | ElevenLabs | PM, API Platform | Ready to Apply | 4.25 | Verify listing, then apply |
| 3 | Datadog | PM, Observability | Applied | 4.1 | No response (10 days) |
| 14 | Notion | PM, API Platform | Applied | 4.0 | Referral in, waiting (6 days) |
| 5 | Linear | Product Lead | Evaluated | 3.93 | Apply if pipeline thins |
| 6 | Supabase | PM, Developer Tools | Evaluated | 3.78 | Backup only |
| 18 | **Linear** | **Product Manager** | **Discovered** | — | **NEW — needs evaluation** |
| 19 | **Cohere** | **PM, Product Mgmt** | **Discovered** | — | **NEW — needs evaluation** |
| 16 | Anthropic | PM, Claude Code | Discovered | — | Pending multi-role policy |
| 17 | Anthropic | PM, API Growth | Discovered | — | Pending multi-role policy |

**Pipeline total:** 19 entries (15 active, 2 Ghosted, 1 Rejected, 1 location-failed)

---

## Portal Coverage & Findings

| Company | Type | Scanned? | PM Roles Found | Notes |
|---------|------|----------|----------------|-------|
| Anthropic | Greenhouse | ✅ | Dev Community Lead EMEA (London) — not PM | No new PM roles vs yesterday. Existing IDs 1, 16, 17. |
| Vercel | Greenhouse | ✅ | 0 PM roles | Solutions Architect (Remote UK/DE) and FDE (Berlin) noted — not PM. |
| Datadog | Greenhouse | ✅ | 6 Director-level PM (all NY) | Too senior + wrong location. Skip. |
| Cloudflare | Greenhouse | ✅ | Director PM Data Security (multi); Dev GTM Munich | Director too senior. Dev GTM = not PM. |
| Linear | Ashby | ✅ | **Product Manager (Europe, Remote)** | **NEW → ID 18.** Also confirmed Product Lead (ID 5) still listed. |
| Cohere | Ashby | ✅ | **PM & Program Management (London+)** | **NEW → ID 19.** Also: CSM Berlin, FDE UK/EU noted. |
| Supabase | Ashby | ✅ | PM Pricing & Billing (Remote) | Different from ID 6. Pricing/billing = off-profile. Skipped. |
| Neon | Ashby | ✅ | Lead PM DevEx (SF/NYC only) | Confirmed on-site. ID 15 updated — fails location. |
| ElevenLabs | Ashby | ⚠️ Partial | 0 PM titles visible | Stale flag on ID 10 persists. B2B Marketing + Deployment roles only. |
| n8n | Career Page | ❌ JS limit | — | CSS-only response. ID 7 already in Interview. |
| Stripe | Career Page | ⚠️ Partial | APAC Product Lead (Singapore) | Wrong location. No EU/remote PM roles. |
| Mistral | Lever | ❌ 403 | — | Lever blocking. ID 2 already in Screen. |
| W&B | Ashby | ❌ JS limit | — | ID 13 already in Screen. |
| Grafana | Ashby | ❌ JS limit | — | No data. |
| Notion | Greenhouse | ❌ 404 | — | Slug not found. ID 14 already Applied via referral. |
| HuggingFace | Greenhouse | ❌ 404 | — | Slug not found. ID 11 has Offer. |
| dbt Labs | Greenhouse | ❌ 404 | — | Slug not found. ID 12 already Ghosted. |
| Wise | Greenhouse | ❌ 404 | — | Slug not found. Not in pipeline. |
| Planetscale | Greenhouse | ❌ 404 | — | Slug not found. Not in pipeline. |
| Figma | Lever | ❌ 403 | — | Lever blocking. Not in pipeline. |
| Retool | Lever | ❌ 403 | — | ID 8 already Ghosted. |
| Wellfound | Wellfound | — | Not scanned | Aggregator — deprioritized vs direct portals. |

---

## Portal Config Corrections Applied

1. **Mistral**: Changed type `greenhouse` → `lever`, URL → `jobs.lever.co/mistral` (careers page confirmed Lever)
2. **Cohere**: Changed type `greenhouse` → `ashby`, URL → `jobs.ashbyhq.com/cohere` (careers page confirmed Ashby)

---

## Technical Observations

- **Greenhouse API 404 pattern**: 8 out of 14 Greenhouse slugs returned 404. The `boards-api.greenhouse.io/v1/boards/<slug>` endpoint only works for companies that haven't migrated away. Confirmed working: Anthropic, Vercel, Datadog, Cloudflare. Failed: Mistral, HuggingFace, Notion, Cohere, Wise, dbt Labs, Planetscale.
- **Ashby improvement**: Successfully scraped Linear, Cohere, Supabase, Neon, and partial ElevenLabs today (vs only Linear partial yesterday). Grafana and W&B still JS-blocked.
- **Lever**: Still 403 across the board. No workaround available.

---

## Recommended Actions

### For Evaluator
1. **Evaluate ID 18** (Linear PM, Europe Remote) — high priority, strong location + company fit
2. **Evaluate ID 19** (Cohere PM, London) — medium priority, verify title and level first
3. **Re-evaluate ID 16** (Anthropic PM Claude Code) — still pending multi-role policy

### For Pipeline Conductor
1. **ID 7 n8n follow-up is now 4 days overdue** — escalate immediately
2. **ID 4 Vercel** — 8 days no response, approaching ghost threshold
3. **ID 3 Datadog** — 10 days no response, approaching ghost threshold
4. **ID 10 ElevenLabs** — manually verify listing before applying (2 scans couldn't confirm)

### For User
1. **Apr 16 (3 days)**: Anthropic panel — ensure prep is locked
2. **Apr 18 (5 days)**: HF offer deadline — decision point. Pipeline alternatives are building but none at offer stage yet
