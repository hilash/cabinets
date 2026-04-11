# Cabinet Registry

This is a public registry of Cabinet templates. Each top-level directory is a complete cabinet.

## Conventions

- Cabinet directory names use kebab-case
- Every cabinet must have: `.cabinet`, `.agents/`, `.jobs/`, `index.md`, `.cabinet-state/.gitkeep`
- `.cabinet` files are YAML (no `.yaml` extension)
- Agent personas are markdown with YAML frontmatter at `.agents/<slug>/persona.md`
- Jobs are YAML at `.jobs/<name>.yaml`
- Child cabinets are nested directories that also contain a `.cabinet` file
- `.cabinet-state/` is for runtime state only — keep empty with `.gitkeep`
- Do NOT add website code here — the website lives in the separate `cabinets-web` repo
