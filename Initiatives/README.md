# Initiatives

Each initiative gets its own folder with a `CLAUDE.md` context file.

## Structure

```
Initiatives/
├── my-initiative/
│   ├── CLAUDE.md           # Initiative context (auto-maintained)
│   ├── prd.md              # PRD document
│   ├── research/           # Research artifacts
│   └── ...
└── another-initiative/
    └── CLAUDE.md
```

## Creating a New Initiative

1. Create folder: `mkdir Initiatives/my-initiative`
2. Create context file: Shannon will offer to create `CLAUDE.md` from template
3. Or create manually using the template in `.claude/reference/initiative-auto-update.md`

## Initiative CLAUDE.md

Each initiative's `CLAUDE.md` contains:
- Status and timeline
- Core objective
- Key decisions with rationale
- Current blockers and open questions
- Documents created
- Success metrics

Shannon automatically updates this file based on `.claude/reference/initiative-auto-update.md`.

## Working in Initiatives

When you're in an initiative folder, Shannon:
1. Reads the initiative's `CLAUDE.md` for context
2. Tracks decisions and documents you create
3. Updates the context file with significant events
