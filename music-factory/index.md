---
title: Music Factory
icon: music
created: 2026-04-25
modified: 2026-04-27
tags: [music, midi, browser-apps, public-domain]
---

# 🎹 Music Factory

> Pick a famous song. Watch it light up note-by-note. Hear it. Download the `.mid`.
>
> No build, no server, no account. Two HTML files, vanilla JS, Web Audio.

## Open the apps

- **[[factory/index|🎛️ Factory — multi-song MIDI player]]** ← *the main one*. A song picker with eight public-domain classics, a piano-roll visualizer, Web Audio playback, and a one-click `.mid` download for every song.
- **[[still-alive/index|🟠 Still Alive — Portal player]]** — the dedicated, hand-authored Portal "Still Alive" experience. Same player engine, GLaDOS-themed.

## Songs in the factory

| Song | Composer / source |
|---|---|
| Ode to Joy | Beethoven, Symphony No. 9 (1824) |
| Für Elise | Beethoven, Bagatelle No. 25 in A minor |
| Twinkle Twinkle Little Star | Trad. / Mozart variations |
| Jingle Bells | James Lord Pierpont, 1857 |
| Happy Birthday to You | Patty & Mildred Hill, 1893 (PD since 2016) |
| Korobeiniki (Tetris Theme A) | Russian folk, 1861 |
| Canon in D | Pachelbel, c. 1680 |
| When the Saints Go Marching In | Traditional spiritual |
| In the Hall of the Mountain King | Grieg, Peer Gynt (1875) |
| Greensleeves | English traditional, 16th c. |
| Frère Jacques | French traditional, c. 1780 |
| Auld Lang Syne | Robert Burns, 1788 |
| Amazing Grace | John Newton, 1779 |
| William Tell Overture (Finale) | Rossini, 1829 |
| Hava Nagila | Jewish traditional |
| Yankee Doodle | American traditional, c. 1750s |

All public-domain. The `.mid` files are generated on the fly from the in-page note data — no audio files or external requests.

## Want a new song?

**Open the Tasks panel and ask:** *"add my favorite MIDI song — <name>"*

That kicks off an agent task that:

1. Looks up or transcribes the melody (and a simple bass line) into the cabinet's note format
2. Verifies the song is public-domain or your original work
3. Appends it to the `SONGS` array in `factory/index.html`
4. Reloads the factory so the new song appears in the picker

If you'd rather hand-author it, the format is dead simple — see the `SONGS` array near the top of `factory/index.html`. Each song is a list of `["pitchName", beats]` tuples for melody (and optionally bass), plus `bpm` and metadata. Beats are quarter-note counts: `1` is a quarter, `0.5` an eighth, `1.5` a dotted quarter, `2` a half. `"rest"` for silence.

## Keyboard shortcuts (in the factory)

- **Space** — play / pause
- **R** — restart current song
- **← →** — previous / next song

## What's under the hood

Single-file `factory/index.html`, ~600 lines:

- **Compiler** — turns `[pitch, beats]` tuples into absolute-time note events
- **Web Audio synth** — sine + triangle (melody) / sine + sawtooth (bass), per-note ADSR
- **Canvas piano roll** — color-coded melody/bass, scrolling playhead window
- **Standard MIDI File writer** — emits format-1 `.mid` binary by hand: header chunk, MTrk chunk, tempo + time-sig + program-change + delta-timed note-on/note-off events. The download is a real, DAW-importable file.

No dependencies. Runs offline. Open `factory/index.html` directly in any modern browser.
