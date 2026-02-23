# Output Folder

Default destination for all artifacts Shannon generates.

## What Goes Here

Shannon writes generated files to this directory unless you specify a different path (e.g. `Brains/my-project/`).

| Artifact Type | Format | Examples |
|---------------|--------|----------|
| Documents | `.md` | PRDs, meeting notes, emails, strategy docs |
| Presentations | `.pptx` | Slide decks via the `pptx` skill |
| PDFs | `.pdf` | Formatted documents via the `md-to-pdf` skill |
| Reports | `.md`, `.pdf` | Analysis outputs, competitive reviews |

## How It Works

1. Shannon generates the artifact during your session
2. The file is written here (or to a path you specify)
3. You review — **Keep** saves it, **Undo** discards it

## Notes

- Files are named per request; there is no enforced naming convention
- This folder is safe to clean out at any time
- Large or project-specific artifacts may live in `Brains/[name]/` instead
- Generated files reference the themes, templates, and styles resolved from `input/` (or built-in defaults)
