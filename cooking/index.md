---
title: Cooking
icon: utensils
created: 2026-04-27
tags: [cooking, recipes, meal-planning, pantry]
---

# 🍳 Cooking

> **What's for dinner?** A cabinet for cooking at home — pantry tracking, recipes ranked by what's about to expire, weekly meal plans that generate their own shopping lists.

## Open the Studio first

- 🍳 [[recipe-tonight/index|Recipe Tonight]] — full-screen Liquid Glass dashboard. Tonight's pick (auto-suggested from what's about to expire), use-it-or-lose-it pantry list, 7-day meal plan, this week's shopping list. The "what should I make" tax — solved.

## What's inside

- `recipes.csv` — your saved recipes with rating, last-cooked date, source link, prep time, tags
- `pantry.csv` — what's in the fridge/freezer/pantry, with purchase + expiry dates
- `meal-plan.csv` — 7-day plan, regenerated weekly
- `shopping-list.md` — auto-built from the meal plan minus what's already in pantry

## Your team — 1 agent

- 🍳 **Chef** — your kitchen brain. Reads the pantry, ranks tonight's options by what's expiring, scales recipes for serving size, suggests substitutions, builds the weekly meal plan. Doesn't pretend to be a Michelin sommelier — just makes tonight easier.

## Daily rhythm

- **5:30 pm daily** — Chef scans pantry, picks tonight's dinner from your saved recipes, surfaces 2 alternatives.
- **Sunday 7 pm** — Chef writes next week's `meal-plan.csv` and `shopping-list.md`, balanced across cuisines + protein sources.

## Pair with

- **`personal-os`** — if installed, Chef cross-references with `family/` for who's eating, with `health/` for any allergies/preferences, with `money/` for grocery budget.
- **`keto-hq`** or other diet cabinets — Chef respects their macro constraints when picking from your saved recipes.
