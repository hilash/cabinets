# Cabinet Registry

This is a public registry of Cabinet templates. Each top-level directory is a complete cabinet.

## Repos & packages

| What | Where |
|---|---|
| Registry (this repo) | https://github.com/hilash/cabinets (currently private) |
| CLI tool source | https://github.com/hilash/cabinets-tool (private) |
| CLI tool on npm | https://www.npmjs.com/package/cabinets (`cabinets@0.1.1`) |
| Scaffolder on npm | https://www.npmjs.com/package/create-cabinet |
| Website | Separate `cabinets-web` repo |

### CLI tools

- `npx create-cabinet` — scaffold a blank cabinet from scratch
- `npx cabinets add <name>` — install a template from this registry (or any GitHub repo)
- `npx cabinets browse` — browse available templates in the registry
- `npx cabinets list` — list cabinets in current directory
- `npx cabinets info <name>` — inspect a cabinet without installing

Single-name sources (e.g. `npx cabinets add agency`) resolve to `hilash/cabinets/<name>`.

## Conventions

- Cabinet directory names use kebab-case
- Every cabinet must have: `.cabinet`, `.agents/`, `.jobs/`, `index.md`, `.cabinet-state/.gitkeep`
- `.cabinet` files are YAML (no `.yaml` extension)
- Agent personas are markdown with YAML frontmatter at `.agents/<slug>/persona.md`
- Jobs are YAML at `.jobs/<name>.yaml`
- Child cabinets are nested directories that also contain a `.cabinet` file
- `.cabinet-state/` is for runtime state only — keep empty with `.gitkeep`
- Do NOT add website code here — the website lives in the separate `cabinets-web` repo
- Do NOT add the CLI tool code here — it lives in the separate `cabinets-tool` repo

## .cabinet file schema

```yaml
schemaVersion: 1
id: agency-root
name: Digital Agency
kind: root           # root or child
version: 0.1.0
description: Digital agency managing multiple client engagements.
entry: index.md
```

Child cabinets add `parent.shared_context` and `access.mode` fields.

## Comparable projects

- [paperclipai/companies](https://github.com/paperclipai/companies) — agent company registry for the Paperclip platform. Uses `COMPANY.md` + `AGENTS.md` + `SKILL.md` format. Installed via `npx companies.sh add`. Key difference: companies are agent-team definitions with org charts; cabinets are structured workspaces that hold both agents and working data/content.

## Security

- All profile/CV data in templates uses placeholders (`you@example.com`, `linkedin.com/in/yourname`, `+49 XXX XXXXXXXX`)
- No real secrets, credentials, or PII in the repo
- The GitHub workflow uses `${{ secrets.CABINETS_WEB_PAT }}` properly (not hardcoded)
