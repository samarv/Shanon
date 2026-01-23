# Output Location Protocol

## Purpose

Ensure all generated artifacts are saved to the appropriate location in the project structure, not left in temporary directories.

## Output Directory Structure

```
Operations/
├── adhoc/                    # One-off work, organized by topic
│   ├── [topic-name]/         # e.g., aecGoals/
│   │   ├── [artifact].md
│   │   └── [artifact].html
├── recurring/                # Regular deliverables
│   ├── leadership-reviews/   # Executive presentations
│   │   └── assets/           # Images, charts
│   ├── manager-meetings/     # Manager sync materials
│   ├── squad-strategy/       # Strategy documents
│   └── landingPage/          # Landing page assets
```

## Output Location Rules

| Artifact Type | Location | Naming Convention |
|---------------|----------|-------------------|
| **Leadership Materials** | `Operations/recurring/leadership-reviews/` | `[month][year].[ext]` |
| **Ad-hoc Analysis** | `Operations/adhoc/[topic]/` | Descriptive name |
| **Strategy Documents** | `Operations/recurring/squad-strategy/` | `[month][year].md` |
| **Initiative Artifacts** | `Initiatives/[name]/` | Keep with initiative |
| **Temporary/Test Files** | `Output/` | Prefix with `test_` |
| **PDFs** | Same as source document | `[source-name].pdf` |

## Determining Output Location

When generating any artifact:

1. **Ask**: "What is this artifact for?"
   - Leadership review → `Operations/recurring/leadership-reviews/`
   - Customer-facing → `Operations/adhoc/[product]/`
   - Initiative work → `Initiatives/[name]/`
   - Testing → `Output/` (temporary)

2. **Create folder** if it doesn't exist

3. **Use descriptive names** that indicate purpose and date

## Clean Up Protocol

- **Output/** folder is for temporary files only
- Move finalized artifacts to appropriate Operations folder
- Delete test files when no longer needed
- Keep `Output/` folder clean
