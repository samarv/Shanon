# Input Folder

Add your themes, templates, and organizational context here.

## Structure

```
input/
├── themes/
│   ├── pptx/          # Presentation themes (.md files)
│   └── pdf/           # PDF styles (.css files)
├── templates/         # Document templates (.md files)
├── output-styles/     # Writing voice definitions (.md files)
├── org/               # Organization data
│   ├── colleagues.json
│   └── org-context.md
├── best-practices/    # Quality standards (.md files)
└── reference/         # Additional protocols (.md files)
```

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

## The Contract

- **Put files in the right folders**
- **Shannon reads what's there**
- **Missing files = built-in defaults used**
- **No configuration needed**

See `.claude/rules/input-resolution.md` for full resolution order.
