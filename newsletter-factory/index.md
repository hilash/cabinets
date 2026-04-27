---
title: Newsletter Factory
icon: "✉️"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - newsletter
  - email
  - content
  - template
order: 1
---

# ✉️ Newsletter Factory

> A complete newsletter OS in a directory. Fill in three placeholders, run the bootstrap prompt, and your `Editor-in-Chief` agent builds your brand voice, a 12-issue calendar, drafts the launch issue with subject-line and opening-hook variants, and recommends a platform tuned to your cadence and growth model.

---

## ⚡ Bootstrap your Newsletter OS

**Step 1.** Fill in the three placeholders below.

**Step 2.** Open the AI panel on this page. Paste the prompt block. Run.

**Step 3.** Wait. The agent writes `brand/index.md`, fills `issue-calendar.csv` with 12 issues, drafts `issues/001-launch/draft.md`, generates 8 subject lines and 3 opening hooks, and recommends a platform.

```
You are the Editor-in-Chief agent for this Newsletter Factory cabinet. The writer just filled
in the "Onboarding" section of index.md.

Read those answers. Then build out the cabinet in this exact order:

1. Write `brand/index.md`. Lock in: newsletter name, one-line premise, target reader,
   default issue format (curated / essay / deep-dive / digest / listicle / interview /
   lessons), target word count, send cadence (weekly? bi-weekly?), preferred send-day
   and send-time, voice rules (5 do's and 5 don'ts), the standing sections every issue
   has, the voice-defining one-sentence "tagline" that opens every issue, and the
   sign-off that closes every issue.

2. Generate 12 issue ideas in `issue-calendar.csv`. Number them 001–012. Each row gets
   working_title (under 70 chars), premise, format, target_words, target_send_date
   matching cadence, referral_hook (what makes it forward-worthy), status=`idea`. Issue
   001 is the launch / manifesto issue introducing the newsletter to a new subscriber.

3. Draft `issues/001-launch/draft.md` using the right template from
   `generators/issue-generator.md`. Read aloud. Cut anything that sounds written.

4. Append "## Subject-line candidates" (8 variants — mix promise / question / number /
   curiosity-gap) to `issues/001-launch/index.md` using `generators/subject-line-generator.md`.

5. Append "## Opening-line hooks" (3 variants: scene / question / contradiction) to the
   same file using `generators/opening-hook-generator.md`.

6. Append "## Growth-loop hook" to `issues/001-launch/draft.md` using
   `generators/growth-loop-generator.md`. Pick one share/referral lever appropriate to
   the issue's content.

7. Recommend a platform. Read `platform-guide/index.md`. Based on the writer's cadence,
   monetization plans, and tech-comfort level, append a "## Recommended platform" block
   to `brand/index.md` with a 1-line answer + 2–3 lines of reasoning.

8. Append "## ✅ Bootstrap complete — [YYYY-MM-DD]" to this index.md with what was built
   and next steps for the writer.

Rules:
- Use ONLY what the writer provided in Onboarding. Do not invent biographical details.
- If a placeholder is empty or vague, ask the writer to fill it in. Do not guess.
- Do not modify `platform-guide/`, `growth-guide/`, or `generators/` — those are durable
  templates.
```

---

## 🧩 Onboarding — fill these in

### 1. Who are you?

> _Name, what you do, why you're the right person to write THIS newsletter, the one-sentence credibility proof. "I'm a 20-year corporate lawyer who left to teach plain-language contracts — sharp, slightly cynical, allergic to legal jargon" beats "I write about law."_

```
_________
```

### 2. What is the newsletter about?

> _Premise in one sentence. Target reader (specific — "in-house counsel at SMBs who don't have a contracts team" beats "lawyers"). The 3 questions every issue helps them answer. What this newsletter is NOT about (lock the scope)._

```
_________
```

### 3. What style and cadence?

> _Default format (curated / essay / deep-dive / digest / listicle / interview / lessons). Target length (words or read-time). Cadence (weekly Sunday morning? Tuesday lunch?). Tone (warm? sharp? deadpan?). Preferred sign-off ("see you next week"? "stay sharp"? something custom?). Free or paid (or paid tier later)? Three words readers should use to describe you. Three words you must never sound like._

```
_________
```

---

## 📚 What is in this cabinet

| Page | What it is |
|---|---|
| [[brand/index]] | Newsletter brand & voice spec — populated by bootstrap |
| `issue-calendar.csv` | The issue pipeline — interactive table |
| [[issues/index]] | Issue archive + reusable template |
| [[generators/index]] | Prompt packs: issue, subject line, opening hook, growth loop |
| [[platform-guide/index]] | Substack vs Beehiiv vs ConvertKit vs Ghost vs Buttondown decision matrix |
| [[growth-guide/index]] | Growth loops, referral programs, deliverability, send-time optimization |

## 🤖 Your team

- **✉️ Editor-in-Chief** — drafting, voice, subject lines, growth tactics. Refills calendar Mondays. Drafts next issue Wednesdays.

## 🔁 What runs on a schedule

- **Weekly Calendar Fill** — Monday 9am. Top up to ≥6 issues.
- **Weekly Issue Prep** — Wednesday 10am. Draft the next un-drafted issue.

## 🚀 After the bootstrap

1. Read `brand/index.md`. Edit anything that doesn't sound like you.
2. Read the launch issue in `issues/001-launch/draft.md`. Read it aloud.
3. Pick a platform from `platform-guide/index.md`. Set up the account.
4. Send the launch issue. Note open rate, click rate, replies.
5. The Wednesday agent drafts issue 002 for you.
