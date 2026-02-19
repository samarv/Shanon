# Input Resolution

Shannon uses an input overlay system. Input packs provide themes, templates, org data, and best practices.

**Core principle**: Input is OPTIONAL. Shannon works without any input pack.

## Resolution Order (first found wins)

1. `CLAUDE.local.md` preferences (always highest priority)
2. `input/[type]/` (user's input pack)
3. `.claude/defaults/[type]/` (Shannon's built-in)
4. Ask user / skip feature

## Input Types

| Type | Path | Fallback |
|------|------|----------|
| PPTX themes | `input/themes/pptx/*.md` | `.claude/defaults/themes/pptx/minimal.md` |
| PDF styles | `input/themes/pdf/*.css` | `.claude/defaults/themes/pdf/default.css` |
| Templates | `input/templates/*.md` | `.claude/defaults/templates/` or ask user |
| Output styles | `input/output-styles/*.md` | Professional PM default |
| Org data | `input/org/` | Skip feature |
| Best practices | `input/best-practices/*.md` | Core quality gates only |

## When Input Is Missing

Inform user clearly, never block:
- "Using minimal theme since no brand theme is installed."
- "Name verification disabled -- no input/org/colleagues.json found."

## Adding New Input Types

Input is extensible. Create a folder in `input/` (e.g., `input/personas/`), reference it from a skill or rule, and Shannon discovers it automatically. The filesystem IS the registry.
