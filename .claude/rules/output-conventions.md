# Output Conventions

All generated artifacts go to `output/` by default. Shannon auto-organizes by topic.

## Default Locations

| Artifact | Location |
|----------|----------|
| All generated files | `output/` |
| Brain-specific artifacts | `Brains/[name]/` |
| Temporary/test files | `output/` (prefix with `test_`) |
| PDFs | Same directory as source document |

## When Saving Files

1. If working within a Brain, save to `Brains/[name]/`
2. Otherwise, save to `output/`
3. Create topic subfolders in `output/` when it improves organization
4. Use descriptive names that indicate purpose and date

## Clean Up

- `output/` auto-organizes: Shannon creates subfolders as patterns emerge
- Move finalized artifacts to the relevant Brain if they belong to one
- Delete test files when no longer needed
