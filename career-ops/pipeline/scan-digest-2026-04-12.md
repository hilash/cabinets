---
title: Daily Scan Digest — 2026-04-12
agent: scanner
type: digest
date: '2026-04-12'
portals_scanned: 18
new_discoveries: 3
stale_flags: 1
---

# Scanner Daily Digest — Sunday 12 April 2026

## Summary

Completed first full portal scan. 18 portals checked across Greenhouse, Ashby, Lever, and career pages.
**3 new roles added to pipeline** (IDs 15–17). **1 stale flag raised** (ID 10 ElevenLabs).

---

## New Discoveries

| ID | Company | Role | Priority | Notes |
|----|---------|------|----------|-------|
| 15 | **Neon** | Lead PM, Developer Experience | Medium | Developer infra + DX = strong domain fit. Verify remote availability (listed SF/NYC). |
| 16 | **Anthropic** | PM, Claude Code | **HIGH** | Dev tools PM in Claude ecosystem. Confirm multi-role application policy (ID 1 already in interview). |
| 17 | **Anthropic** | PM, API Growth | High | API platform + growth angle. Same-company caveat as ID 16. Evaluate after ID 16 policy confirmed. |

---

## Pipeline Snapshot (active + in-flight)

| ID | Company | Role | Status | Score | Urgency |
|----|---------|------|--------|-------|---------|
| 11 | Hugging Face | Senior PM, Hub | **Offer** | 4.7 | ⚠️ Decision deadline Apr 18 |
| 1 | Anthropic | PM, Claude API | **Interview** | 4.6 | ⚠️ Panel Apr 16 |
| 7 | n8n | Head of Product | **Interview** | 4.5 | Berlin onsite done, awaiting decision |
| 13 | W&B | PM, ML Ops | Screen | 4.2 | Onsite TBD |
| 2 | Mistral | Senior PM, Platform | Screen | 4.3 | Awaiting next round |
| 4 | Vercel | Senior PM, DX | Applied | 4.4 | No response yet |
| 10 | ElevenLabs | PM, API Platform | Evaluating | 4.21 | ⚠️ See stale flag below |
| 5 | Linear | Product Lead | Evaluating | 3.87 | Scored, pending apply decision |
| 6 | Supabase | PM, Developer Tools | Evaluating | 3.68 | Scored, clarify seniority first |
| 16 | Anthropic | PM, Claude Code | Discovered | — | Needs evaluation + policy check |
| 17 | Anthropic | PM, API Growth | Discovered | — | Needs evaluation after ID 16 |
| 15 | Neon | Lead PM, DevEx | Discovered | — | Needs evaluation + location verify |

---

## Stale Flag

**ID 10 — ElevenLabs, PM API Platform (Discovered 2026-04-10)**

April 12 scan of ElevenLabs job board found zero PM-titled roles. Current openings are
predominantly Sales, Marketing, and Engineering. However, Ashby requires JavaScript to render
listings, so this may be a false negative from the static-fetch limitation rather than the role
being filled.

**Action:** Manually verify at `elevenlabs.io/careers` before discarding or proceeding with
application (Evaluator scored it 4.21 — strong apply recommendation).

---

## Portal Coverage & Findings

| Company | Type | Status | PM Roles Found | Notes |
|---------|------|--------|----------------|-------|
| Anthropic | Greenhouse | ✅ Scanned | 6 PM roles (page 4 of 9) | New: Claude Code, API Growth |
| Linear | Ashby | ✅ Partial | PM (NA + Europe) | JS-rendered; existing ID 5 may match |
| Supabase | Ashby | ✅ Partial | PM Pricing & Billing | Already in tracker as ID 6 |
| ElevenLabs | Ashby | ⚠️ JS limit | 0 PM roles visible | Stale flag raised |
| Neon | Ashby | ✅ Partial | Lead PM Dev Experience | **NEW → ID 15** |
| Vercel | Greenhouse | ✅ Scanned | 0 PM roles (Solutions Architect only) | ID 4 already applied |
| Datadog | Greenhouse | ✅ Scanned | Director PM roles (NY-only) | ID 3 already applied; Director roles not a fit |
| Cloudflare | Greenhouse | ✅ Scanned | Director PM Data Security | Multi-site (no Berlin); skip |
| Notion | Career Page | ✅ Scanned | PM Enterprise, PM Ops Mgr | ID 14 already applied; Enterprise → SF/NYC, skip |
| Grafana Labs | Greenhouse | ✅ Scanned | 0 PM roles | No PM openings currently |
| PlanetScale | Greenhouse | ✅ Scanned | 0 PM roles (5 total openings) | Very thin hiring |
| n8n | Career Page | ⚠️ JS limit | — | ID 7 already in Interview |
| Cohere | Ashby | ❌ JS only | — | Could not scrape; Ashby JS-rendered |
| W&B | Ashby | ❌ JS only | — | Could not scrape; ID 13 already in Screen |
| Replicate | Ashby | ❌ JS only | — | Could not scrape |
| Figma | Lever | ❌ 403 | — | Lever blocking scraper |
| Retool | Lever | ❌ 403 | — | Lever blocking scraper |
| Stripe | Career Page | ⚠️ Paginated | 0 PM roles visible | Pagination issue; manual check recommended |
| Wise | Greenhouse | — | — | Not reached in this scan cycle |
| Mistral | Greenhouse | — | — | 404 on boards-api; try job-boards domain |

---

## Technical Learnings

- **Greenhouse migration**: `boards.greenhouse.io` → `job-boards.greenhouse.io` (301 redirect).
  JSON API at `boards-api.greenhouse.io/v1/boards/<slug>` still responds for most companies.
- **Ashby boards**: Fully JavaScript-rendered. Static fetch returns only loading shell — no job data.
  Only `jobs.ashbyhq.com/linear` returned partial content in this scan.
- **Lever boards**: Returning 403 for `jobs.lever.co` direct access. Use company career pages instead.
- **Greenhouse JSON API**: Paginated; defaults to first N jobs. For large boards (Anthropic: 429 jobs),
  must paginate through pages on the web UI (page 4 had the PM department).

---

## Recommended Actions for Evaluator

1. **Evaluate ID 16** (Anthropic PM Claude Code) — highest priority discovery; strong profile fit
2. **Evaluate ID 17** (Anthropic PM API Growth) — after ID 16 multi-role policy resolved
3. **Evaluate ID 15** (Neon Lead PM Dev Experience) — verify remote first, then score
4. **Verify ID 10** (ElevenLabs) — manual check at elevenlabs.io/careers before applying

## Recommended Actions for Pipeline Conductor

1. **ID 11** (HF Offer) — decision by Apr 18. Only 6 days. Escalate if other strong outcomes pending.
2. **ID 1** (Anthropic panel) — Apr 16. 4 days away. Ensure interview prep is complete.
3. Ask user about Anthropic's multi-role application policy (affects IDs 16 & 17).
