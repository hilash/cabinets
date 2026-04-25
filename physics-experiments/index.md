---
title: Physics Experiments
icon: flask
created: 2026-04-23
tags: [physics, experiments, simulations]
---

# Physics Experiments

Interactive, self-contained simulations of classic physics experiments. Each folder is an embedded web app — open it from the sidebar to launch.

## Experiments

- **Double-Slit** (`double-slit/`) — Wave-particle duality. Watch an interference pattern emerge photon by photon.
- **Pendulum Wave** (`pendulum-wave/`) — 15 pendulums tuned to different periods produce a mesmerizing standing-wave illusion.
- **Projectile Motion** (`projectile-motion/`) — Classical ballistics. Tune angle, velocity, and gravity; trace the parabola.
- **Wave Interference** (`wave-interference/`) — Two coherent point sources on a ripple tank. Adjust separation and wavelength to reshape the pattern.
- **Brachistochrone** (`brachistochrone/`) — Race three balls down straight, circular, and cycloid paths. The cycloid wins — every time.

All apps run entirely in the browser. No network, no dependencies.

## Implementation notes

Each experiment is a directory with an `index.html` file (plus a `.app` marker for full-screen rendering in Cabinet). Built with vanilla JS + Canvas 2D — zero build step, zero external libs. Open the HTML file directly in any browser if you want to hack on it.
