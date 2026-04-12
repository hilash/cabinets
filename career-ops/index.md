---
title: Career Ops
created: '2026-04-12T00:00:00Z'
modified: '2026-04-12T00:00:00Z'
tags:
  - job-search
  - career
  - ai-powered
  - cabinet
order: 1
---
# Career Ops

> "Companies use AI to filter candidates. I gave candidates AI to choose companies."
> — Santiago Fernandez ([@santifer](https://github.com/santifer))

Career Ops is an AI-powered job search command center adapted from the [career-ops](https://github.com/santifer/career-ops) open source project (MIT license) by Santiago Fernandez de Valderrama. The original system evaluated 740+ job offers, generated 100+ tailored CVs, and helped Santiago land a Head of Applied AI role.

This cabinet adapts that methodology into a structured, visual, agent-driven system.

## Philosophy

- **Filter, don't spray.** This is not a mass-apply tool. It helps you find the few offers genuinely worth your time.
- **Human-in-the-loop.** AI evaluates and recommends. You decide and submit. Never auto-apply.
- **Quality over quantity.** Don't apply to anything scoring below 4.0/5.
- **Data-driven.** Every decision backed by evaluation scores, pipeline metrics, and pattern analysis.

## How It Works

1. **Configure your profile** in [[profile]] — your CV, proof points, skills matrix, and search criteria
2. **Scan portals** using [[portals]] — 45+ companies across Greenhouse, Ashby, Lever, Wellfound
3. **Evaluate offers** with the 6-block system in [[evaluations]] — each job gets blocks A through F
4. **Generate tailored CVs** in [[cv-lab]] — ATS-optimized, keyword-injected, one per application
5. **Track your pipeline** on the [[pipeline]] board — from discovered to offer with full status history
6. **Prep for interviews** using [[interview-prep]] — STAR+R stories, negotiation scripts, company research
7. **Analyze patterns** in [[analytics]] — rejection patterns, channel ROI, pipeline velocity

## Your Team — 10 Agents

Adapted from the 16 modes in the original career-ops system, organized into 10 specialized agents:

### Core Pipeline
- **Pipeline Conductor** — orchestrates the full auto-pipeline: URL → evaluation → CV → application → tracker. Also handles batch processing and pipeline integrity.
- **Evaluator** — runs the 6-block A-F+G evaluation on every job offer, multi-offer comparison, and scoring
- **CV Tailor** — generates ATS-optimized, keyword-injected CVs per application with proof point selection
- **Scanner** — discovers new roles across 30+ company portals using 3-level scanning (Playwright, API, WebSearch)

### Interview & Negotiation
- **Interview Strategist** — builds STAR+R stories, company-specific prep packets, negotiation playbooks
- **Application Assistant** — helps fill application forms with personalized answers, cover letters, and tone calibration

### Intelligence & Networking
- **Researcher** — deep company research across 6 axes: strategy, movements, culture, challenges, competitors, candidate angle
- **Outreach Specialist** — LinkedIn outreach (4 contact-type frameworks) and follow-up cadence management

### Strategy & Growth
- **Pattern Analyst** — rejection pattern detection, funnel analysis, channel ROI, archetype performance, strategic recommendations
- **Career Advisor** — evaluates courses/certifications and portfolio projects against career goals and skill gaps

## The 6-Block Evaluation System

Every job offer is evaluated across six blocks:

| Block | Name | What It Covers |
| --- | --- | --- |
| **A** | Role Summary | Title, level, team, scope, growth potential |
| **B** | CV Match Analysis | Skills overlap, gap identification, keyword alignment |
| **C** | Level Strategy | Seniority fit, over/under-leveling risk, career trajectory |
| **D** | Compensation Research | Market benchmarks, equity analysis, total comp modeling |
| **E** | Personalization Tips | Company culture signals, application angle, differentiators |
| **F** | Interview Prep | Likely questions, STAR+R stories to load, company-specific intel |

## Attribution

This cabinet is adapted from [santifer/career-ops](https://github.com/santifer/career-ops) by Santiago Fernandez de Valderrama, licensed under MIT. The original project provides Claude Code skills, a Go terminal dashboard, PDF generation via Playwright, and portal scanning — this cabinet adapts the methodology and evaluation framework into the cabinet format.
