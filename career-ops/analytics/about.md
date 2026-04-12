---
title: Analytics
created: '2026-04-12T00:00:00Z'
modified: '2026-04-12T00:00:00Z'
tags:
  - analytics
  - patterns
  - metrics
order: 1
---
# Analytics

Data-driven insights about your search performance. Pattern detection turns failures into strategy adjustments.

## What Gets Tracked

- **Pipeline velocity** — new opportunities in vs closures out per week
- **Conversion rates** — between each pipeline stage
- **Channel ROI** — which sources produce interviews, not just applications
- **Evaluation accuracy** — do high-score roles actually convert?
- **Rejection patterns** — where and why you're getting cut
- **Interview performance** — which question types are your strengths/weaknesses
- **Time in stage** — how long opportunities sit before moving forward

## Weekly Reports

The `weekly-pipeline-health` job produces a report every Monday covering all the above metrics.

## Friday Pattern Analysis

The `rejection-patterns` job runs every Friday to identify systemic issues:
- Are you getting filtered at the resume screen? (CV tailoring problem)
- Are you failing phone screens? (Story delivery problem)
- Are you getting cut at onsites? (Depth or energy problem)
- Are you getting ghosted? (Channel or targeting problem)
