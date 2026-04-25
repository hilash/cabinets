---
title: Biology Experiments
icon: dna
created: 2026-04-25
tags: [biology, experiments, simulations, history-of-science]
---

# Biology Experiments

Interactive simulations of the five experiments that built modern molecular biology. Each folder is a self-contained web app — open it from the sidebar to launch.

## Experiments

- **Griffith Transformation** (`griffith-transformation/`) — 1928. Heat-killed virulent pneumococci can transform live harmless strains into killers. The first hint that *something* carries heredity between cells.
- **Hershey-Chase** (`hershey-chase/`) — 1952. Radioactively label phage protein (³⁵S) and DNA (³²P), blend, spin, and watch only the DNA enter the bacterium. DNA, not protein, is the genetic material.
- **Mendel's Peas** (`mendel-peas/`) — 1865. A Punnett square simulator. Cross any two parental genotypes and watch the F1 and F2 ratios emerge generation by generation.
- **Meselson-Stahl** (`meselson-stahl/`) — 1958. Grow E. coli in heavy nitrogen (¹⁵N), shift to light (¹⁴N), and watch DNA bands settle in a density gradient. The proof that replication is semiconservative.
- **Miller-Urey** (`miller-urey/`) — 1953. Spark a flask of methane, ammonia, hydrogen, and water vapor for a week and watch amino acids accumulate. Life's building blocks from a primordial soup.

All apps run entirely in the browser. No network, no dependencies.

## Implementation notes

Each experiment is a directory with an `index.html` file. Built with vanilla JS + Canvas — zero build step, zero external libs. Open the HTML directly in any browser if you want to hack on it.

## Why these five

These are the experiments that turned biology from a descriptive science into a molecular one. Read together they answer four questions in order:
1. Is heredity carried by *something* physical? (Griffith)
2. Which molecule? (Hershey-Chase)
3. How does it copy itself? (Meselson-Stahl)
4. Where did it come from? (Miller-Urey)

Mendel sits at the front because the math of inheritance — dominant/recessive ratios — is what made the rest interpretable.
