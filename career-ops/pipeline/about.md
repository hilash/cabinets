---
title: Pipeline
created: '2026-04-12T00:00:00Z'
modified: '2026-04-12T00:00:00Z'
tags:
  - pipeline
  - tracking
order: 1
---
# Pipeline

Your job search funnel, tracked with precision. Every opportunity flows through a canonical status sequence.

## Status Flow

```
Discovered → Evaluating → Ready to Apply → Applied → Screen → Interview → Offer → Accepted
                ↓              ↓              ↓          ↓         ↓          ↓
              Skip          Withdrawn      Rejected   Rejected  Rejected  Declined
                                            Ghosted   Ghosted   Ghosted
```

## Status Definitions

| Status | Meaning |
| --- | --- |
| **Discovered** | Found by scanner or manually. Not yet evaluated. |
| **Evaluating** | 6-block evaluation in progress or pending. |
| **Ready to Apply** | Scored 4.0+. CV tailoring needed before applying. |
| **Applied** | Application submitted. Clock starts on follow-up. |
| **Screen** | Phone screen or recruiter call in progress. |
| **Interview** | In the interview loop (technical, onsite, panel). |
| **Offer** | Received an offer. Negotiation phase. |
| **Accepted** | Signed. Done. |
| **Rejected** | They said no at any stage. |
| **Ghosted** | No response after 3+ weeks. |
| **Withdrawn** | You decided not to pursue (scored too low, lost interest). |
| **Skip** | Evaluator recommended skip (score below 3.0). |

## Health Rules

- Evaluate within 3 days of discovery — stale Discovered entries mean the scanner is outrunning you
- Don't apply to roles scoring below 3.5 without a warm referral
- Follow up on Applied after 7 days — silence is data
- Ghosted is not rejection — one follow-up can resurrect 15% of ghosted applications
- If more than 30% of applied roles are Ghosted, your channel strategy needs work

## Data

Pipeline data lives in `tracker.csv`. The visual board reads from this file.
