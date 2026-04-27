---
title: Course Factory
icon: "🎓"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - course
  - education
  - template
order: 1
---

# 🎓 Course Factory

> A complete online-course OS in a directory. Fill in three placeholders, run the bootstrap prompt, and your `Course Creator` agent builds your transformation spec, an 8-module syllabus, drafts the welcome lesson, generates sales-page copy, and outlines a launch-week sequence — plus a platform recommendation.

---

## ⚡ Bootstrap your Course OS

**Step 1.** Fill in the three placeholders below.

**Step 2.** Open the AI panel on this page. Paste the prompt block. Run.

**Step 3.** Wait. The agent writes `brand/index.md`, generates an 8-module syllabus in `module-tracker.csv`, drafts the welcome lesson in `modules/001-welcome/`, generates sales-page copy in `launch-guide/sales-page.md`, and recommends a platform.

```
You are the Course Creator agent for this Course Factory cabinet. The creator has just
filled in the "Onboarding" section of index.md.

Read those answers. Then build out the cabinet in this exact order:

1. Write `brand/index.md`. Lock in: course name, one-line premise, the TRANSFORMATION
   (State A → State B in concrete terms — "from a beginner who's never written a SQL
   query to someone who can pull and analyze data from a real production database"
   beats "learn SQL"), target student, format (cohort / self-paced / hybrid), course
   length, total module count target, lesson length norm (8–15 min), price tier
   (intro $50–200 / mid $200–800 / premium $800–2500 / cohort $1500+), 5 do's and
   5 don'ts of voice, three-word brief.

2. Generate an 8-module syllabus in `module-tracker.csv`. Number them 001–008. Each
   row gets module_number, working_title, learning_outcome (one sentence: what the
   student can DO after this module), sub_lesson_count (typically 3–6 per module),
   total_minutes_estimate, status=`outlined`. Module 001 is "Welcome + course
   roadmap"; the final module is "Synthesis + next steps". Modules between move the
   student through the transformation in a logical order.

3. Draft `modules/001-welcome/lesson.md` using `generators/lesson-generator.md`. This
   first module introduces the transformation and the journey. Keep it tight — 10–15
   minutes max.

4. Draft `modules/001-welcome/slides-brief.md` using `generators/slide-generator.md`.

5. Generate `launch-guide/sales-page.md` using `generators/sales-page-generator.md`.
   Mark anything that depends on testimonials/proof as `[TK — collect after
   first cohort]`.

6. Draft `launch-guide/launch-sequence.md` using `generators/launch-sequence-generator.md`.
   The 7-email launch-week sequence.

7. Recommend a platform. Read `platform-guide/index.md`. Append a "## Recommended
   platform" block to `brand/index.md` with a 1-line answer + 2–3 lines of reasoning.

8. Append "## ✅ Bootstrap complete — [YYYY-MM-DD]" to this index.md with what was
   built and next steps.

Rules:
- Use ONLY what the creator wrote in Onboarding.
- If a placeholder is empty or vague, ask. Do not guess.
- Do not modify `platform-guide/`, `launch-guide/index.md`, or `generators/`.
```

---

## 🧩 Onboarding — fill these in

### 1. Who are you?

> _Name, what you do, why you're the right teacher for THIS topic. Specific credibility — what have YOU done that proves you can teach this? "I shipped 4 SaaS apps that hit $10K MRR using this exact stack" beats "I'm a developer."_

```
_________
```

### 2. What does the course teach?

> _The transformation. State A → State B. Be brutally specific. "After this course, students can independently set up a Postgres database, write the 12 most common query patterns, and connect it to a Node.js API — without copy-pasting from Stack Overflow" beats "students will learn databases."_
>
> _Target student: who specifically (level, role, prior experience). What this course is NOT (avoid scope creep). The 3 things students will be able to DO after that they couldn't before._

```
_________
```

### 3. What format and price?

> _Cohort (live, group, scheduled) / self-paced (recorded, individual) / hybrid. Course length (4 weeks? 8 weeks? evergreen?). Module count target (default 8). Lesson length norm (default 8–15 min). Price tier (intro $50–200 / mid $200–800 / premium $800–2500 / cohort $1500+). Are you running a cohort first or going straight to self-paced? Whether you have a list / audience to launch to (size + warmth)._

```
_________
```

---

## 📚 What is in this cabinet

| Page | What it is |
|---|---|
| [[brand/index]] | Course transformation + voice spec — populated by bootstrap |
| `module-tracker.csv` | Syllabus pipeline — interactive table |
| [[modules/index]] | Module catalog + lesson + slide briefs |
| [[generators/index]] | Lesson, slide, sales-page, launch-sequence prompt packs |
| [[platform-guide/index]] | Teachable / Maven / Kajabi / Podia / School / self-hosted matrix |
| [[launch-guide/index]] | Pre-launch / launch / post-launch playbook |

## 🤖 Your team

- **🎓 Course Creator** — curriculum, lessons, slides, sales copy, launch. Marketing prep Mondays. Module prep Wednesdays.

## 🔁 What runs on a schedule

- **Weekly Marketing Prep** — Monday 9am. Phase-aware (pre/launch/post).
- **Weekly Module Prep** — Wednesday 10am. Drafts the next module.

## 🚀 After the bootstrap

1. Read `brand/index.md`. The transformation is your North Star — every decision flows from it.
2. Read the welcome lesson in `modules/001-welcome/lesson.md`. Read aloud. Cut to land in <15 min.
3. Pick a platform from `platform-guide/index.md`.
4. Read `launch-guide/sales-page.md`. **Pre-sell** before you build the rest. If it doesn't sell at outline-stage, the curriculum needs work — not the marketing.
5. Wednesday agent drafts module 002.
