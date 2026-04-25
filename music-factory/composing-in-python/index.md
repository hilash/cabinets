# MIDI Song Player

Python script that programmatically builds a MIDI song and plays it.

## Dependencies

```bash
pip install mido pygame
```

On macOS you may also need:
```bash
brew install fluid-synth
```

## Code

```python
#!/usr/bin/env python3
"""
midi_player.py — Build and play a MIDI song in Python.

Dependencies: mido, pygame
    pip install mido pygame
"""

import tempfile
import os
import mido
from mido import MidiFile, MidiTrack, Message

# ── Note helpers ──────────────────────────────────────────────────────────────

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def note_to_midi(name: str, octave: int) -> int:
    """Convert note name + octave to MIDI number (e.g. 'C', 4 → 60)."""
    return NOTE_NAMES.index(name) + (octave + 1) * 12

def beats_to_ticks(beats: float, ticks_per_beat: int) -> int:
    return int(beats * ticks_per_beat)

# ── Song definition ───────────────────────────────────────────────────────────

# Each entry: (note_name, octave, duration_in_beats)
# None = rest
MELODY = [
    ("E", 5, 0.5), ("E", 5, 0.5), ("E", 5, 1.0),
    ("E", 5, 0.5), ("E", 5, 0.5), ("E", 5, 1.0),
    ("E", 5, 0.5), ("G", 5, 0.5), ("C", 5, 0.5), ("D", 5, 0.5),
    ("E", 5, 2.0),
    ("F", 5, 0.5), ("F", 5, 0.5), ("F", 5, 0.5), ("F", 5, 0.5),
    ("F", 5, 0.5), ("E", 5, 0.5), ("E", 5, 0.5), ("E", 5, 0.25), ("E", 5, 0.25),
    ("E", 5, 0.5), ("D", 5, 0.5), ("D", 5, 0.5), ("E", 5, 0.5),
    ("D", 5, 1.0), ("G", 5, 1.0),
]

BASS = [
    ("C", 3, 1.0), ("G", 3, 1.0), ("A", 3, 1.0), ("E", 3, 1.0),
    ("F", 3, 1.0), ("C", 3, 1.0), ("D", 3, 1.0), ("G", 3, 1.0),
]

TEMPO_BPM = 120
VELOCITY = 80
TICKS_PER_BEAT = 480

# ── Build MIDI ────────────────────────────────────────────────────────────────

def build_midi() -> MidiFile:
    mid = MidiFile(ticks_per_beat=TICKS_PER_BEAT)
    tempo = mido.bpm2tempo(TEMPO_BPM)

    def make_track(notes, channel=0, program=0) -> MidiTrack:
        track = MidiTrack()
        track.append(mido.MetaMessage("set_tempo", tempo=tempo, time=0))
        track.append(Message("program_change", channel=channel, program=program, time=0))
        for entry in notes:
            if entry is None:
                continue
            name, octave, dur = entry
            pitch = note_to_midi(name, octave)
            ticks = beats_to_ticks(dur, TICKS_PER_BEAT)
            track.append(Message("note_on",  channel=channel, note=pitch, velocity=VELOCITY, time=0))
            track.append(Message("note_off", channel=channel, note=pitch, velocity=0,        time=ticks))
        return track

    # Melody: piano (program 0), Bass: acoustic bass (program 32)
    mid.tracks.append(make_track(MELODY, channel=0, program=0))
    mid.tracks.append(make_track(BASS * 2, channel=1, program=32))
    return mid

# ── Play ──────────────────────────────────────────────────────────────────────

def play_midi(mid: MidiFile, path: str):
    """Write MIDI to a temp file and play via pygame."""
    try:
        import pygame
    except ImportError:
        raise SystemExit("Install pygame:  pip install pygame")

    mid.save(path)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    print(f"Playing {path}  ({TEMPO_BPM} BPM) — press Ctrl+C to stop")
    pygame.mixer.music.play()
    try:
        while pygame.mixer.music.get_busy():
            pygame.time.wait(200)
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
    finally:
        pygame.quit()

# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Build and play a MIDI song")
    parser.add_argument("--save", metavar="FILE", help="Save MIDI to this path instead of a temp file")
    parser.add_argument("--no-play", action="store_true", help="Build the MIDI file but don't play it")
    args = parser.parse_args()

    mid = build_midi()

    if args.save:
        out = args.save
    else:
        tmp = tempfile.NamedTemporaryFile(suffix=".mid", delete=False)
        out = tmp.name
        tmp.close()

    if args.no_play:
        mid.save(out)
        print(f"Saved to {out}")
    else:
        play_midi(mid, out)
        if not args.save:
            os.unlink(out)
```

## Running it

```bash
# Play immediately (uses a temp file):
python midi_player.py

# Save the .mid and play it:
python midi_player.py --save my_song.mid

# Just save, don't play:
python midi_player.py --save my_song.mid --no-play
```

## How it works

| Layer | Library | Role |
|-------|---------|------|
| MIDI construction | `mido` | Builds note-on/note-off messages into tracks |
| Playback | `pygame.mixer.music` | Loads the `.mid` file and streams it through the OS MIDI synth |

The melody is Jingle Bells (first phrase) encoded as `(note, octave, duration_beats)` tuples.
The bass track loops a simple I–V–vi–III–IV–I–ii–V progression.

## Extending

- **Change the song** — edit `MELODY` / `BASS` tuples.
- **Change the instrument** — adjust `program=` (General MIDI patch numbers 0–127).
- **Add chords** — append multiple `note_on` messages at `time=0` in the same track.
- **Load an existing `.mid`** — skip `build_midi()` and call `play_midi(mido.MidiFile("your.mid"), "your.mid")`.
