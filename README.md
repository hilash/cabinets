# Cabinets

A public registry of [Cabinet](https://runcabinet.com) templates — portable, file-system native operating units for business functions.

## What is a Cabinet?

A cabinet is a directory on disk that contains everything an AI-powered business unit needs to operate: agents, scheduled jobs, a knowledge base, and optional child cabinets. A company is modeled as a tree of cabinets.

```
my-company/
  .cabinet            # identity and metadata
  .agents/            # persistent AI team members
  .jobs/              # scheduled automations
  index.md            # entry point
  marketing/
    reddit/           # child cabinet
    tiktok/           # child cabinet
  app-development/    # child cabinet
```

## Browse the Registry

Each top-level directory in this repo is a complete cabinet template you can install and customize.

| Cabinet | Description |
|---------|-------------|
| [text-your-mom](./text-your-mom) | B2C mobile app company with marketing and engineering teams |
| [saas-startup](./saas-startup) | B2B SaaS startup with product-led growth |
| [ecommerce](./ecommerce) | Direct-to-consumer e-commerce brand |
| [agency](./agency) | Digital agency managing multiple clients |
| [content-creator](./content-creator) | Solo content creator operation |
| [real-estate](./real-estate) | Real estate brokerage with listings and marketing |

## Install a Cabinet

Copy any cabinet directory into your project:

```bash
# Clone and copy
git clone https://github.com/user/cabinets.git /tmp/cabinets
cp -r /tmp/cabinets/text-your-mom ./my-company

# Or use sparse checkout for a single cabinet
git clone --filter=blob:none --sparse https://github.com/user/cabinets.git
cd cabinets
git sparse-checkout set text-your-mom
```

## Contributing

To add a cabinet to the registry:

1. Fork this repo
2. Create a new directory with your cabinet name (kebab-case)
3. Include at minimum: `.cabinet`, `.agents/`, `.jobs/`, `index.md`
4. Submit a pull request

See any existing cabinet for the expected file structure.

## Cabinet File Structure

### `.cabinet` (YAML)

```yaml
schemaVersion: 1
id: my-cabinet
name: My Cabinet
kind: root          # or "child" for nested cabinets
version: 0.1.0
description: What this cabinet does.
entry: index.md
```

### `.agents/<slug>/persona.md` (Markdown with YAML frontmatter)

Defines an AI agent: name, emoji, role, type (lead/specialist), heartbeat schedule, budget, focus areas.

### `.jobs/<name>.yaml` (YAML)

Defines a scheduled job: name, owner agent, cron schedule, prompt.

### `index.md` (Markdown with YAML frontmatter)

Entry point with title, tags, and a description of the cabinet's purpose.
