---
title: Music Factory
icon: music
created: 2026-04-25
modified: 2026-04-26
tags: [music, midi, python, browser-apps, generator]
---

# 🎹 Music Factory

> **What MIDI would you like to generate today?**
>
> Type a vibe → live piano-roll → one-tap playback → download a real `.mid` file.

## Open the Studio first

- **[[studio/index|🎛️ Studio — the MIDI generator]]** ← *new* · full-screen Cabinet app. Describe a song in plain English (*"a melancholy lofi beat in C minor"*), watch the piano roll fill, hit play (Web Audio synthesizes it live), download as a standard `.mid` file. Ten genres, seven moods, twelve keys, four instruments. No build, no API, no account — runs entirely in your browser.

## Reference players & how-tos

- **[[still-alive/index|🟠 Still Alive — Portal MIDI Player]]** — full-screen Cabinet app. The GLaDOS song from *Portal*, hand-authored, with a piano-roll visualizer that lights up note-by-note as it plays.
- **[[bye-bye-bye/bye_bye_bye|🎤 Bye Bye Bye — NSync as Python]]** — a self-contained Python script that builds melody + bass + chord tracks and writes `bye_bye_bye.mid`. Run: `python bye_bye_bye.py`.
- **[[composing-in-python/index|📝 Composing in Python — How-to]]** — step-by-step guide using `mido` + `pygame`. Note helpers, beat→tick conversion, melody/bass tracks, runnable example.

## Why this exists

MIDI is the quietest superpower in programming. ~120 lines of code can produce something a stranger immediately recognizes. There's no audio engine to wrestle with, no audio files to license — just integers (note number, velocity, ticks) flowing into a `.mid` file that any browser, DAW, or speaker can play.

The Studio takes that one step further: you don't even need to write code. Pick a vibe, hit generate, get a real `.mid`. Then open it in Logic / Ableton / GarageBand / [signal](https://signal.vercel.app/) and edit to taste — or open the source of `studio/index.html` to see exactly how it was built.

## Quickstart

```bash
# 1. Generate a song from a prompt (THE Studio)
open studio/index.html

# 2. Try the hand-authored Portal player
open still-alive/index.html

# 3. Generate a song from Python
cd bye-bye-bye/
pip install mido
python bye_bye_bye.py             # writes bye_bye_bye.mid

# 4. Read the guide
open composing-in-python/index.md
```

## What's under the Studio's hood

All vanilla JS + Web Audio + Canvas in a single ~1500-line `index.html`:

- **Music theory primitives** — scales (major, minor, dorian, pentatonic, blues), chord library (maj/min/maj7/min7/sus4/dim/dom7), Roman-numeral progression builder
- **10 genre presets** with chord progressions, melody styles, bass styles, drum patterns, default instruments — lofi, pop, lullaby, cinematic, Bach invention, chiptune, jazz, rock, ambient, folk
- **Prompt parser** — extracts genre/mood/key/BPM from natural language
- **Procedural generator** — turns params into a track structure (bass + melody + pad + drums) with seeded randomness
- **Piano-roll renderer** — Canvas, color-coded per track, live playhead
- **Web Audio playback engine** — per-instrument oscillator + ADSR, drums via noise + filter, sample-accurate scheduling
- **Standard MIDI File exporter** — writes format-1 `.mid` binary by hand (no library), with tempo, time signature, program changes, and per-track event chunks. The download is a real, DAW-importable file.

## What this cabinet does NOT include

- A DAW. Use Logic, Ableton, GarageBand, or [signal](https://signal.vercel.app/) (browser) to open the `.mid` files for editing.
- High-quality audio rendering. The Studio's playback uses simple oscillator synthesis. For realistic sound, route the downloaded `.mid` through a soft-synth like FluidSynth or any DAW with sampled instruments.
- Copyright clearance. "Still Alive" and "Bye Bye Bye" are educational reproductions — keep them that way. The Studio generates original music from algorithmic templates.

## Implementation notes

- All apps are vanilla JS + Canvas + Web Audio. Zero dependencies, runs offline.
- The Python scripts depend only on `mido` (and `pygame` if you want to play in-process).
- The `.app` marker on `studio/`, `still-alive/` tells Cabinet to render those pages full-screen with the sidebar collapsed.
