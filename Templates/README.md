# Templates

Templates are loaded from `input/templates/` if available.
Fallback templates are in `.claude/defaults/templates/`.

## Using Templates

Shannon automatically uses templates when creating documents.

```
"Create a PRD for feature X"
→ Shannon uses input/templates/prd.md if exists
→ Falls back to asking for format preferences
```

## Adding Templates

Add template files to `input/templates/`:

```bash
cp my-prd-template.md input/templates/prd.md
```

## Template Guidelines

- Use clear placeholder markers: `[PLACEHOLDER]`
- Include structure comments
- Keep templates focused on structure, not content
- Add guidance comments for each section
