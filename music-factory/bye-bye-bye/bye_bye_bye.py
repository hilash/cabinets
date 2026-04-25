#!/usr/bin/env python3
"""Generates and plays the 'Bye Bye Bye' (NSYNC) chorus hook as a MIDI file.

Writes `bye_bye_bye.mid` next to this script, then tries to play it using
whichever MIDI player is available on the system (timidity, fluidsynth, or
macOS's built-in `afplay` via a soundfont-less fallback).

No third-party dependencies — MIDI bytes are written by hand.
"""

from __future__ import annotations

import os
import shutil
import struct
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# MIDI primitives
# ---------------------------------------------------------------------------

TICKS_PER_QUARTER = 480
BPM = 108  # Bye Bye Bye sits around 172 BPM in half-time feel; 108 reads musically for the hook
MICROSECONDS_PER_MINUTE = 60_000_000


def variable_length(value: int) -> bytes:
    """Encode an integer as a MIDI variable-length quantity."""
    buffer = value & 0x7F
    out = bytearray()
    value >>= 7
    while value:
        buffer <<= 8
        buffer |= 0x80 | (value & 0x7F)
        value >>= 7
    while True:
        out.append(buffer & 0xFF)
        if buffer & 0x80:
            buffer >>= 8
        else:
            break
    return bytes(out)


NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def note_number(name: str) -> int:
    """'C4' -> 60, 'Eb5' -> 75, etc."""
    name = name.replace("b", "#")  # normalize flats; 'Eb' -> 'E#' is wrong, handle below
    # proper flat handling
    return _note_number(name)


def _note_number(name: str) -> int:
    # Accept both 'Eb4' and 'D#4' by normalizing flats down a semitone from the natural
    if "b" in name:
        natural, octave = name.replace("b", "")[:-1], int(name[-1])
        return 12 * (octave + 1) + NOTE_NAMES.index(natural) - 1
    if "#" in name:
        natural_sharp = name[:-1]
        octave = int(name[-1])
        return 12 * (octave + 1) + NOTE_NAMES.index(natural_sharp)
    natural = name[:-1]
    octave = int(name[-1])
    return 12 * (octave + 1) + NOTE_NAMES.index(natural)


def n(name: str) -> int:
    # small helper that handles flats correctly
    if name == "R":
        return -1
    if "b" in name:
        natural = name[0]
        octave = int(name[-1])
        return 12 * (octave + 1) + NOTE_NAMES.index(natural) - 1
    return _note_number(name)


# ---------------------------------------------------------------------------
# Melody — the iconic "Bye Bye Bye" chorus hook in C minor
# ---------------------------------------------------------------------------
# Each entry: (note_name_or_"R", beats)
# Structure:
#   Bar 1-2: "I'm doin' this tonight / you're probably gonna start a fight"
#   Bar 3-4: "I know this can't be right / hey baby come on"
#   Bar 5-6: "I loved you endlessly / when you weren't there for me"
#   Bar 7-8: "So now it's time to leave and make it alone"
#   Bar 9+:  "Bye bye bye" — the hook
MELODY: list[tuple[str, float]] = [
    # Verse-lead-in: "I'm doin' this tonight"
    ("G4",  0.5), ("G4",  0.5), ("G4",  0.5), ("Ab4", 0.5),
    ("G4",  0.5), ("F4",  0.5), ("Eb4", 1.0),
    ("R",   0.5),

    # "You're probably gonna start a fight"
    ("G4",  0.5), ("G4",  0.5), ("G4",  0.5), ("Ab4", 0.5),
    ("G4",  0.5), ("F4",  0.5), ("Eb4", 1.0),
    ("R",   0.5),

    # Build-up to the chorus — rising tension
    ("Eb4", 0.5), ("F4",  0.5), ("G4",  0.5), ("Ab4", 0.5),
    ("Bb4", 1.0), ("G4",  0.5), ("Ab4", 0.5),
    ("R",   0.5),

    # "Bye" — the hook (bars 1-2 of chorus)
    ("G4",  1.0), ("F4",  1.0), ("Eb4", 2.0),
    ("R",   0.5),

    # "Bye bye" — repeat, descending further
    ("G4",  0.5), ("G4",  0.5), ("F4",  1.0), ("Eb4", 1.0),
    ("D4",  1.0), ("Eb4", 1.0),
    ("R",   0.5),

    # Answer phrase — "ain't no lie, baby bye bye bye"
    ("G4",  0.5), ("G4",  0.5), ("F4",  0.5), ("Eb4", 0.5),
    ("D4",  0.5), ("Eb4", 0.5), ("F4",  0.5), ("G4",  0.5),
    ("G4",  1.0), ("F4",  1.0), ("Eb4", 2.0),
    ("R",   1.0),
]

# Simple bass line in C minor following the chord progression
# Cm - Ab - Eb - Bb (repeat)
BASS: list[tuple[str, float]] = [
    ("C3",  2.0), ("Ab2", 2.0),
    ("Eb3", 2.0), ("Bb2", 2.0),
    ("C3",  2.0), ("Ab2", 2.0),
    ("Eb3", 2.0), ("Bb2", 2.0),
    ("C3",  2.0), ("Ab2", 2.0),
    ("Eb3", 2.0), ("Bb2", 2.0),
    ("C3",  2.0), ("Ab2", 2.0),
    ("Eb3", 2.0), ("Bb2", 2.0),
    ("C3",  4.0), ("Ab2", 4.0),
]


# ---------------------------------------------------------------------------
# MIDI track assembly
# ---------------------------------------------------------------------------

def build_track(notes: list[tuple[str, float]], channel: int, program: int, velocity: int) -> bytes:
    """Build a single MIDI track body (without the MTrk header) from a note list."""
    events = bytearray()

    # Program change — pick the instrument
    events += variable_length(0)
    events += bytes([0xC0 | channel, program])

    for name, beats in notes:
        duration_ticks = int(beats * TICKS_PER_QUARTER)
        if name == "R":
            # Rest: advance the clock by emitting a zero-velocity note-on/note-off pair
            # on a muted note, OR simply bake the delay into the next event.
            # We take the simpler path — accumulate delay into the next event.
            events += _accumulated_delay(duration_ticks)
            continue
        pitch = n(name)
        # Note on immediately (delta already 0 unless carried over)
        events += _accumulated_delay(0)
        events += bytes([0x90 | channel, pitch, velocity])
        # Note off after duration
        events += variable_length(duration_ticks)
        events += bytes([0x80 | channel, pitch, 0])

    # End of track meta
    events += variable_length(0)
    events += bytes([0xFF, 0x2F, 0x00])
    return bytes(events)


# Module-level pending delay used by `_accumulated_delay` to fold rests into the next event.
_pending_delay: int = 0


def _accumulated_delay(extra_ticks: int) -> bytes:
    global _pending_delay
    _pending_delay += extra_ticks
    out = variable_length(_pending_delay)
    _pending_delay = 0
    return out


def build_tempo_track() -> bytes:
    """Track 0 in a type-1 MIDI file carries tempo/meta events."""
    events = bytearray()
    microseconds_per_quarter = MICROSECONDS_PER_MINUTE // BPM
    events += variable_length(0)
    events += bytes([0xFF, 0x51, 0x03])
    events += microseconds_per_quarter.to_bytes(3, "big")
    # End of track
    events += variable_length(0)
    events += bytes([0xFF, 0x2F, 0x00])
    return bytes(events)


def wrap_track(body: bytes) -> bytes:
    return b"MTrk" + struct.pack(">I", len(body)) + body


def build_midi_file() -> bytes:
    global _pending_delay

    _pending_delay = 0
    melody_body = build_track(MELODY, channel=0, program=81, velocity=100)  # 81 = Lead 2 (sawtooth)

    _pending_delay = 0
    bass_body = build_track(BASS, channel=1, program=38, velocity=85)  # 38 = Synth Bass 1

    tempo_body = build_tempo_track()

    header = b"MThd" + struct.pack(">IHHH", 6, 1, 3, TICKS_PER_QUARTER)
    return header + wrap_track(tempo_body) + wrap_track(melody_body) + wrap_track(bass_body)


# ---------------------------------------------------------------------------
# Playback
# ---------------------------------------------------------------------------

def try_play(path: Path) -> None:
    """Try to play the MIDI file with whatever is available; fall through quietly."""
    for cmd in (["timidity", str(path)], ["fluidsynth", "-i", str(path)]):
        if shutil.which(cmd[0]):
            print(f"Playing with {cmd[0]}...")
            subprocess.run(cmd, check=False)
            return
    # macOS fallback — render to AIFF with system tools if `fluidsynth` isn't installed
    if sys.platform == "darwin" and shutil.which("afplay"):
        print("No MIDI synth found. On macOS, install one with:")
        print("  brew install fluid-synth fluid-soundfont")
        print(f"MIDI file written to: {path}")
        print("Open it in GarageBand / QuickTime to hear it.")
        return
    print(f"MIDI file written to: {path}")
    print("No MIDI player detected. Install `timidity` or `fluidsynth` to hear it.")


def main() -> None:
    out_path = Path(__file__).with_name("bye_bye_bye.mid")
    out_path.write_bytes(build_midi_file())
    print(f"Wrote {out_path} ({out_path.stat().st_size} bytes)")
    try_play(out_path)


if __name__ == "__main__":
    main()
