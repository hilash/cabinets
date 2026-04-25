---
title: Music Factory
icon: music
created: 2026-04-25
tags: [music, midi, python, browser-apps]
---

# 🎹 Music Factory

> **Compose songs in Python. Render them as MIDI. Play them in the browser with a live visualizer.**

This cabinet shows three things you can do with ~50 lines of pure-Python MIDI code: render a recognizable song, ship it as a self-contained web player, and document the process so the next song takes 20 minutes instead of an afternoon.

## What's inside

- **[[still-alive/index|🟠 Still Alive — Portal MIDI Player]]** — full-screen Cabinet app. The GLaDOS song from *Portal*, with a piano-roll visualizer that lights up note-by-note as it plays. Click the page in the sidebar — Cabinet renders it edge-to-edge thanks to the `.app` marker.
- **[[bye-bye-bye/bye_bye_bye|🎤 Bye Bye Bye — NSync as Python]]** — a single self-contained Python script that builds the song's melody, bass, and chord track, then writes `bye_bye_bye.mid`. Run it: `python bye_bye_bye.py`.
- **[[composing-in-python/index|📝 Composing in Python — How-to]]** — a step-by-step guide for writing your own song with `mido` + `pygame`. Note helpers, beat→tick conversion, melody/bass tracks, and a runnable example.

## Why this is fun

MIDI is the quietest superpower in programming. ~120 lines of code can produce something a stranger immediately recognizes. There's no audio engine to wrestle with, no audio files to license — just integers (note number, velocity, ticks) flowing into a `.mid` file that any browser, DAW, or speaker can play.

This cabinet exists to lower the activation energy. Steal the Portal player as a template, swap the `SCORE` for your own notes, and you've shipped a song.

## Quickstart

```bash
# 1. Try the browser player
open still-alive/index.html       # plays in any modern browser

# 2. Generate a fresh MIDI from Python
cd bye-bye-bye/
pip install mido
python bye_bye_bye.py             # writes bye_bye_bye.mid in this folder

# 3. Read the guide
open composing-in-python/index.md
```

## What this cabinet does NOT include

- A DAW. Use Logic, Ableton, GarageBand, or [signal](https://signal.vercel.app/) (browser) to open the `.mid` files for editing.
- Audio rendering. The Python scripts produce `.mid` (note data only). To turn that into a `.wav` or `.mp3`, route through a soft-synth like FluidSynth.
- Copyright clearance. The melodies of "Still Alive" and "Bye Bye Bye" belong to their composers. These files are educational reproductions — keep them that way.

## Implementation notes

- The Still Alive player is vanilla JS + Canvas + the Web Audio API — zero dependencies, runs offline.
- The Python scripts depend only on `mido` (and `pygame` if you want to play in-process). No external services.
- The `.app` marker on `still-alive/` tells Cabinet to render that page full-screen with the sidebar collapsed.
