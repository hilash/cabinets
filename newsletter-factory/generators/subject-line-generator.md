---
title: Subject-Line Generator
icon: "📬"
created: '2026-04-27T00:00:00.000Z'
modified: '2026-04-27T00:00:00.000Z'
tags:
  - generator
  - subject-line
order: 3
---

# 📬 Subject-Line Generator

Subject line + sender name = ~50% of your open rate. Write 8 variants per issue. Pick the strongest. Save the rest for next time you cover a similar topic.

## Generator prompt

```
You are the Editor-in-Chief. Read brand/index.md and the target issue's draft.md.
Output 8 subject-line candidates in this structure:

[8 SUBJECT LINES — under 50 chars each, mobile-first]

Mix all four shapes:

  1. PROMISE — "How I shipped a SaaS in 9 days"
  2. QUESTION — "Why does every contract have a 'best efforts' clause?"
  3. NUMBER / LIST — "5 signs your retention strategy is fake"
  4. CURIOSITY-GAP — "The thing every founder gets wrong about pricing"

Write 2 of each shape (8 total). Constraints:

  - Under 50 chars (mobile inboxes truncate around 35–45 chars)
  - Front-load the hook keyword
  - No emojis unless brand/index.md explicitly approves them
  - No ALL CAPS
  - No "Re:" or "Fwd:" tricks
  - Don't promise what the issue doesn't deliver

For each candidate, on the next line, also write the PREVIEW TEXT — the ~40 chars
of body that show after the subject line. This is real estate. Use it.

[FORMAT — write each candidate exactly like this]

  1. [Subject line]
     Preview: [first 40 chars of body that complete the hook]

[TOP PICK]
End with one line: "Recommended: #N because [one-sentence reason]."
```

## What makes a strong subject line

- **Specific.** "How I refunded 18 customers and still grew 12%" beats "Lessons in customer service."
- **Intriguing without baiting.** Promise something the body actually delivers.
- **Personal where appropriate.** "What I learned firing my first hire" outperforms generic versions of the same content.
- **Tested over time.** Track open rates per subject-line shape across issues. Your audience tells you what works.

## A/B testing

Most platforms support split-testing the subject line. Send variant A to 10% of the list, variant B to 10%, and the winner (by open rate after 1–4 hours) to the remaining 80%. Beehiiv, Substack, ConvertKit, and Ghost all support this natively.

## What to avoid

- Spam-trigger words: "free", "act now", "limited time", "you won't believe" — kills deliverability
- Excessive punctuation (`!!!`, `???`) — kills deliverability
- Generic newsletter-y subjects: "[Newsletter name] #42" — generic, low open rate
- Long subjects that get truncated mid-word
