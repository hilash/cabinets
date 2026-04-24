---
title: Getting Started
created: '2026-04-24T00:00:00.000Z'
modified: '2026-04-24T00:00:00.000Z'
tags:
  - onboarding
  - howto
order: 1
icon: 🚦
---

# 🚦 How to use this cabinet

> Read this once before you start. It'll save you hours.

## The structure

Everything is organized into 5 numbered stages you work through in order:

```
ai-hero/
├── 01-math-prerequisites/    ← videos + reading checklists
├── 02-intuition/             ← 3Blue1Brown series
├── 03-academic-theory/       ← survey video + paper preview
├── 04-hands-on/              ← Karpathy videos + exercise notebooks
└── 05-research-paper/        ← read one paper critically
```

Plus three support areas:

- **`dashboard/`** — visual progress tracker. Open it from the sidebar.
- **`concept-map/`** — interactive map of every concept in the course. Good for orientation.
- **`progress/`** — the raw CSV and daily log that the Progress Tracker agent maintains.

## The checklist system

Every stage page has a `## Checklist` block with unchecked boxes:

```markdown
- [ ] Watched video 1
- [ ] Watched video 2
- [ ] Can explain concept X to a rubber duck
```

**Your job:** tick them as you go. `- [ ]` → `- [x]`. The Progress Tracker agent reads these every evening and updates the dashboard.

Do not tick a box you didn't actually do. The point of the course is the work, not the dashboard.

## The notebooks

Inside `04-hands-on/`, sections with a `notebook.ipynb` are where you do the real work. Open them in Jupyter, VS Code, or Cursor.

**The rule:** type the code yourself while watching Karpathy's video. Do not copy-paste from his GitHub. Your fingers need the reps — backprop intuition lives in your hands, not your head.

Recommended setup:

```bash
# In a fresh conda or venv
pip install torch numpy matplotlib jupyter
cd 04-hands-on/01-micrograd
jupyter lab notebook.ipynb
```

If you have an M-series Mac, `torch` installs with MPS support — you don't need CUDA for this course. Everything fits on CPU or small GPU.

## The agents

Four agents live in this cabinet. Summon any of them from the AI panel:

| Agent | Ask them when |
|---|---|
| 🎓 **Mentor** | you need a next step, or are wondering if you're falling behind |
| 📐 **Math Tutor** | a symbol, shape, or derivative doesn't click |
| 💻 **Code Tutor** | a notebook cell is broken, or you need a PyTorch idiom explained |
| 📊 **Progress Tracker** | you want a status report without doing the math yourself |

### What NOT to ask them

- "What's the answer to exercise 3?" — they won't tell you
- "Write my trigram model" — they'll refuse and ask what you've tried
- "Summarize the video for me" — watch the video, that's the assignment

### What TO ask them

- "I keep getting a shape mismatch on line 40 of my notebook — here's the error"
- "Explain the chain rule with a numerical example"
- "Why is Karpathy using `F.cross_entropy` instead of a manual softmax?"

## Suggested pacing

| Plan | Sessions | Daily commitment | Finish in |
|---|---|---|---|
| Relaxed | 20 sessions | 1 h/day, 5 days/week | 4 weeks |
| Standard | 10 sessions | 2 h/day, 5 days/week | 2 weeks |
| Crunch | 5 sessions | 4 h/day, 5 days/week | 1 week |

**Pick the plan that fits your week** and put the time on your calendar before something else takes it.

## Checklist

- [ ] Read this whole page
- [ ] Opened the [[dashboard/index|Dashboard]] and confirmed it renders
- [ ] Installed: `torch`, `numpy`, `matplotlib`, `jupyter`
- [ ] Decided on a pacing plan (relaxed / standard / crunch) and blocked the time on your calendar
- [ ] Skimmed the [[../index|main index]] and know what each stage contains

Once these are all ticked, jump to **[[../01-math-prerequisites/index|Stage 1: Math Prerequisites]]**.
