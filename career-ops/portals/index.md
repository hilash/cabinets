---
title: Portal Scanner
created: '2026-04-12T00:00:00Z'
modified: '2026-04-12T00:00:00Z'
tags:
  - portals
  - scanning
  - sourcing
order: 1
---
# Portal Scanner

The Scanner agent scans 30+ company career portals daily using 19 search queries, discovering new roles before they appear on aggregators.

## How It Works

1. Scanner reads portal configs from `portals.yaml`
2. For each active portal, runs all search queries against the board API
3. Filters results against your profile criteria
4. Deduplicates against existing pipeline entries
5. Adds qualifying matches to `/pipeline/tracker.csv` as "Discovered"

## Portal Types

| Type | API Pattern | Example |
| --- | --- | --- |
| **Greenhouse** | `boards.greenhouse.io/[slug]/jobs` | Anthropic, Notion, Vercel |
| **Ashby** | `jobs.ashbyhq.com/[slug]` | Linear, Supabase, ElevenLabs |
| **Lever** | `jobs.lever.co/[slug]` | Figma, Retool |
| **Wellfound** | `wellfound.com/company/[slug]/jobs` | Startup aggregator |
| **Career Page** | Custom URL per company | Stripe, n8n |

## Coverage

- **30 companies** configured across 5 portal types
- **19 search queries** covering PM, leadership, and adjacent roles
- **3 priority tiers:** active (daily scan), watch (weekly), paused
- **4 target domains:** AI/ML, developer tools, data, fintech

## Customization

Edit `portals.yaml` to:
- Add new companies and their board URLs
- Change scan frequency (active/watch/paused)
- Add or remove search queries
- Adjust priority levels
