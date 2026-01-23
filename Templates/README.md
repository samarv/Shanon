# Templates

Templates are loaded from `content/templates/` if available.
Fallback templates are in `.claude/defaults/templates/`.

## Using Templates

Shannon automatically uses templates when creating documents.

```
"Create a PRD for feature X"
→ Shannon uses content/templates/prd.md if exists
→ Falls back to asking for format preferences
```

## Adding Templates

Add template files to `content/templates/`:

```bash
cp my-prd-template.md content/templates/prd.md
```

## Template Guidelines

- Use clear placeholder markers: `[PLACEHOLDER]`
- Include structure comments
- Keep templates focused on structure, not content
- Add guidance comments for each section
