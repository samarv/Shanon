# Input Folder

Add your themes, templates, and organizational context here. Everything is optional — Shannon works without any input files by falling back to built-in defaults.

## Structure

```
input/
├── themes/
│   ├── pptx/          # Presentation themes (.md with YAML frontmatter)
│   └── pdf/           # PDF styles (.css with CSS variables)
├── templates/         # Document templates (.md with [PLACEHOLDER] markers)
├── output-styles/     # Writing voice definitions (.md with YAML frontmatter)
├── org/               # Organization data
│   ├── colleagues.json    # Name verification and lookup
│   └── org-context.md     # Org structure and context
├── best-practices/    # Quality standards (.md files)
└── reference/         # Additional protocols (.md files)
```

## Resolution Order

Shannon resolves content using the first match found:

1. `CLAUDE.local.md` preferences (highest priority)
2. `input/[type]/` (your files here)
3. `.claude/defaults/[type]/` (built-in fallbacks)
4. Ask user or skip the feature

| Type | Path | Built-in Fallback |
|------|------|-------------------|
| PPTX themes | `input/themes/pptx/*.md` | `.claude/defaults/themes/pptx/minimal.md` |
| PDF styles | `input/themes/pdf/*.css` | `.claude/defaults/themes/pdf/default.css` |
| Templates | `input/templates/*.md` | `.claude/defaults/templates/` or ask user |
| Output styles | `input/output-styles/*.md` | Professional PM default |
| Org data | `input/org/` | Feature skipped |
| Best practices | `input/best-practices/*.md` | Core quality gates only |

## Quick Start

### Option 1: Clone an input pack

```bash
git clone https://github.com/[org]/input-[name].git input-pack
cp -r input-pack/* input/
```

### Option 2: Add individual files

```bash
cp my-brand-theme.md input/themes/pptx/
cp my-prd-template.md input/templates/
cp colleagues.json input/org/
```

## File Format Reference

### `colleagues.json`

```json
{
  "colleagues": [
    {
      "name": "Sarah Chen",
      "role": "CEO",
      "team": "Executive",
      "aliases": ["Sarah", "SC"],
      "email": "sarah@company.com"
    }
  ]
}
```

### PPTX Theme (`.md`)

Markdown file with YAML frontmatter defining `name`, colors, and typography. See `.claude/defaults/themes/pptx/minimal.md` for the schema.

### Output Style (`.md`)

Markdown file with YAML frontmatter containing `name` and `applies_to` fields that define the writing voice.

## Extensibility

Input is extensible. Create a new folder (e.g. `input/personas/`), reference it from a skill or rule, and Shannon discovers it automatically. The filesystem is the registry.

## The Contract

- **Put files in the right folders** — Shannon reads what's there
- **Missing files = built-in defaults** — nothing breaks
- **No configuration needed** — drop files in, they're picked up

See `.claude/rules/input-resolution.md` for the full resolution spec.
