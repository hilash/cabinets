---
title: Setup Guide
created: '2026-04-12T00:00:00Z'
modified: '2026-04-12T00:00:00Z'
tags:
  - docs
  - setup
order: 2
---
# Setup Guide

Get Career Ops running in 5 steps. Takes about 30-60 minutes.

## Step 1: Your CV

Fill in `/profile/cv-master.md` with your complete career history. Be exhaustive — the CV Tailor will cut it down per application. Include:
- Every role with quantified achievements
- Education and certifications
- Languages spoken
- Side projects if relevant

## Step 2: Your Profile

Update `/profile/index.md` and `/profile/profile.yaml` with:
- Career narrative (who you are, what you're good at)
- Search criteria (titles, seniority, industries, comp range)
- Non-negotiables and anti-targets
- Languages and location preferences

## Step 3: Proof Points and Skills

- Fill `/profile/proof-points.md` with your quantified achievements, tagged by skill area
- Complete `/profile/skills-matrix.csv` with honest proficiency levels
- These are what the CV Tailor selects from per application

## Step 4: Configure Portals

Edit `/portals/portals.yaml`:
- Add or remove companies based on your target list
- Set status to active (daily scan), watch (weekly), or paused
- Customize search queries to match your target roles
- Add portal URLs for companies you're interested in

## Step 5: Initialize Pipeline

- Add 5-10 opportunities to `/pipeline/tracker.csv` to seed the pipeline
- Include a mix: some discovered, some already applied
- The Scanner will add new discoveries daily going forward

## After Setup

- Agents will start running their jobs on schedule
- The Scanner discovers new roles daily
- The Evaluator scores them in batches
- You decide which ones are worth applying to
- The CV Tailor generates tailored CVs for applications scoring 4.0+

## Customization

- **Target market:** Edit profile.yaml to change search queries and criteria
- **Language:** Career Ops supports EN, DE, FR, JA, PT, RU, KO, ES
- **Portal list:** Add any company with a Greenhouse, Ashby, Lever, or Wellfound board
- **Evaluation weights:** Adjust block weights in the Evaluator persona if your priorities differ
