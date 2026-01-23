# Content Folder

Add your themes, templates, and organizational context here.

## Structure

```
content/
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

### Option 1: Clone a content pack

```bash
git clone https://github.com/[org]/content-[name].git content-pack
cp -r content-pack/* content/
```

### Option 2: Add individual files

```bash
# Add a theme
cp my-brand-theme.md content/themes/pptx/

# Add a template
cp my-prd-template.md content/templates/

# Add org data
cp colleagues.json content/org/
```

## The Contract

- **Put files in the right folders**
- **Shannon reads what's there**
- **Missing files = built-in defaults used**
- **No configuration needed**

See `.claude/reference/content-contract.md` for full documentation.
