"""
Render a short excerpt of Portal's "Still Alive" as a WAV file.

The script uses only the Python standard library. It writes a stereo WAV next
to the script by default and can optionally play it with a system audio player.
"""

from __future__ import annotations

import argparse
import math
import shutil
import struct
import subprocess
import wave
from pathlib import Path

SAMPLE_RATE = 44_100
BPM = 120
SECONDS_PER_BEAT = 60.0 / BPM
DEFAULT_OUTPUT = "portal_still_alive_excerpt.wav"
RELEASE_SECONDS = 0.09

# Short melodic excerpt reduced to note events so the script stays dependency-free.
SCORE: list[tuple[float, tuple[str, ...], float]] = [
    (0.000, ("G5",), 0.468),
    (0.498, ("F#5",), 0.463),
    (0.991, ("E5",), 0.492),
    (1.484, ("E5",), 0.465),
    (1.983, ("A3", "F#5"), 1.024),
    (2.513, ("D4",), 0.525),
    (3.009, ("F#4",), 0.522),
    (3.502, ("D4",), 0.527),
    (4.000, ("B3",), 0.527),
    (4.498, ("D4",), 0.522),
    (4.991, ("F#4",), 0.522),
    (5.484, ("D4",), 0.524),
    (5.983, ("A3",), 0.559),
    (6.513, ("D4",), 0.525),
    (7.009, ("F#4",), 0.522),
    (7.502, ("D4", "A4"), 0.527),
    (8.000, ("B3", "G5"), 0.527),
    (8.498, ("D4", "F#5"), 0.522),
    (8.991, ("F#4", "E5"), 0.522),
    (9.484, ("D4", "E5"), 0.998),
    (9.983, ("A3",), 0.559),
    (10.513, ("D4", "F#5"), 0.525),
    (11.009, ("F#4",), 0.522),
    (11.502, ("D4",), 0.527),
    (12.000, ("B3", "D5"), 0.990),
    (12.498, ("D4",), 0.522),
    (12.991, ("F#4", "E5"), 0.522),
    (13.484, ("D4", "A4"), 0.524),
    (13.983, ("A3",), 0.559),
    (14.513, ("D4",), 0.525),
    (15.009, ("F#4",), 0.522),
    (15.502, ("D4",), 0.527),
    (16.000, ("B3",), 0.527),
    (16.498, ("D4",), 0.522),
    (16.991, ("F#4",), 0.522),
    (17.484, ("D4", "A4"), 0.524),
    (17.983, ("B3", "E5"), 1.024),
    (18.513, ("E4",), 0.525),
    (19.009, ("G4", "F#5"), 0.522),
    (19.502, ("E4", "G5"), 1.488),
    (20.000, ("B3",), 0.527),
    (20.498, ("E4",), 0.522),
    (20.991, ("G4", "E5"), 0.522),
    (21.484, ("E4", "C#5"), 0.998),
    (21.983, ("A3",), 0.559),
    (22.513, ("E4", "D5"), 1.486),
    (23.009, ("G4",), 0.522),
    (23.502, ("E4",), 0.527),
    (24.000, ("A3", "E5"), 0.990),
    (24.498, ("E4",), 0.522),
    (24.991, ("G4", "A4"), 0.522),
    (25.484, ("E4", "A4"), 1.058),
    (25.983, ("A3",), 0.559),
    (26.513, ("D4", "F#5"), 0.988),
    (27.009, ("F#4",), 0.522),
    (27.502, ("D4",), 0.527),
    (28.000, ("B3",), 0.527),
    (28.498, ("D4",), 0.522),
    (28.991, ("F#4",), 0.522),
    (29.484, ("D4",), 0.524),
    (29.983, ("A3",), 0.559),
    (30.513, ("D4",), 0.525),
    (31.009, ("F#4",), 0.522),
    (31.502, ("D4",), 0.527),
    (32.000, ("B3", "G5"), 0.527),
]

NOTE_TO_MIDI = {
    "C": 0,
    "C#": 1,
    "D": 2,
    "D#": 3,
    "E": 4,
    "F": 5,
    "F#": 6,
    "G": 7,
    "G#": 8,
    "A": 9,
    "A#": 10,
    "B": 11,
}


def note_to_midi(note: str) -> int:
    """Convert a note like F#5 into a MIDI note number."""
    name = note[:-1]
    octave = int(note[-1])
    return 12 * (octave + 1) + NOTE_TO_MIDI[name]


def note_to_frequency(note: str) -> float:
    """Convert a note name into its frequency in Hz."""
    midi = note_to_midi(note)
    return 440.0 * (2.0 ** ((midi - 69) / 12.0))


def soft_clip(value: float) -> float:
    """Keep the mixed waveform from clipping harshly."""
    return math.tanh(value * 1.1)


def voice_gain(note: str) -> float:
    """Bring the melody forward while keeping bass notes supportive."""
    midi = note_to_midi(note)
    if midi >= 76:
        return 0.23
    if midi >= 69:
        return 0.19
    if midi >= 60:
        return 0.14
    return 0.11


def stereo_pan(note: str) -> tuple[float, float]:
    """Pan low notes slightly left and high notes slightly right."""
    midi = note_to_midi(note)
    pan = max(-0.65, min(0.65, (midi - 64) / 24.0))
    angle = (pan + 1.0) * math.pi / 4.0
    return math.cos(angle), math.sin(angle)


def synth_sample(frequency: float, t: float) -> float:
    """Blend a few simple waves for a bright, game-like timbre."""
    sine = math.sin(2.0 * math.pi * frequency * t)
    triangle = 2.0 * abs(2.0 * ((frequency * t) % 1.0) - 1.0) - 1.0
    detuned = math.sin(2.0 * math.pi * (frequency * 1.003) * t)
    return (0.50 * sine) + (0.28 * triangle) + (0.22 * detuned)


def envelope(frame: int, sustain_frames: int, release_frames: int) -> float:
    """Simple attack/decay/release curve to avoid pops."""
    attack_frames = max(1, int(0.008 * SAMPLE_RATE))
    if frame < attack_frames:
        return frame / attack_frames
    if frame < sustain_frames:
        progress = frame / max(1, sustain_frames)
        return 1.0 - (0.14 * progress)

    release_frame = frame - sustain_frames
    if release_frame >= release_frames:
        return 0.0
    release_progress = release_frame / max(1, release_frames)
    return 0.86 * ((1.0 - release_progress) ** 2)


def render_excerpt() -> bytes:
    """Render the score into 16-bit stereo PCM bytes."""
    release_frames = int(RELEASE_SECONDS * SAMPLE_RATE)
    last_beat = max(start + duration for start, _, duration in SCORE) + 1.5
    total_frames = int(last_beat * SECONDS_PER_BEAT * SAMPLE_RATE)
    left = [0.0] * total_frames
    right = [0.0] * total_frames

    for start_beat, notes, duration_beats in SCORE:
        start_frame = int(start_beat * SECONDS_PER_BEAT * SAMPLE_RATE)
        sustain_frames = int(duration_beats * SECONDS_PER_BEAT * SAMPLE_RATE)
        total_note_frames = sustain_frames + release_frames

        for note in notes:
            frequency = note_to_frequency(note)
            left_gain, right_gain = stereo_pan(note)
            gain = voice_gain(note) / max(1, len(notes))

            for frame in range(total_note_frames):
                target = start_frame + frame
                if target >= total_frames:
                    break
                sample = synth_sample(frequency, frame / SAMPLE_RATE)
                sample *= envelope(frame, sustain_frames, release_frames) * gain
                left[target] += sample * left_gain
                right[target] += sample * right_gain

    peak = max(
        1.0,
        max(abs(sample) for sample in left),
        max(abs(sample) for sample in right),
    )
    normalization = 0.94 / peak
    frames = bytearray()

    for left_sample, right_sample in zip(left, right):
        left_int = int(32767 * soft_clip(left_sample * normalization))
        right_int = int(32767 * soft_clip(right_sample * normalization))
        frames.extend(struct.pack("<hh", left_int, right_int))

    return bytes(frames)


def write_wav(output_path: Path, pcm_frames: bytes) -> None:
    """Write PCM bytes to a stereo WAV file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(output_path), "wb") as handle:
        handle.setnchannels(2)
        handle.setsampwidth(2)
        handle.setframerate(SAMPLE_RATE)
        handle.writeframes(pcm_frames)


def play_audio(path: Path) -> bool:
    """Play the file if a compatible local player is installed."""
    candidates = [
        ["afplay", str(path)],
        ["ffplay", "-nodisp", "-autoexit", "-loglevel", "error", str(path)],
        ["aplay", str(path)],
    ]
    for command in candidates:
        if shutil.which(command[0]):
            subprocess.run(command, check=False)
            return True
    return False


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render a short excerpt of Portal's 'Still Alive' to WAV.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path(__file__).with_name(DEFAULT_OUTPUT),
        help="Where to write the WAV file.",
    )
    parser.add_argument(
        "--play",
        action="store_true",
        help="Play the rendered WAV after writing it.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pcm_frames = render_excerpt()
    write_wav(args.output, pcm_frames)
    print(f"Wrote {args.output}")

    if args.play and not play_audio(args.output):
        print("No compatible audio player found for automatic playback.")


if __name__ == "__main__":
    main()
