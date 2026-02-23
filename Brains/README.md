# Brains

Each Brain is a self-contained knowledge context that actively accumulates and connects information.

## Structure

```
Brains/
├── my-brain/
│   ├── CLAUDE.md           # Living knowledge context (auto-maintained)
│   ├── prd.md              # PRD document
│   ├── research/           # Research artifacts
│   └── ...
└── another-brain/
    └── CLAUDE.md
```

## Creating a New Brain

1. Create folder: `mkdir Brains/my-brain`
2. Shannon will offer to create `CLAUDE.md` from template
3. Or create manually using the template in `.claude/reference/brain-auto-update.md`

## Brain CLAUDE.md

Each Brain's `CLAUDE.md` contains:
- Status and timeline
- Core objective
- Key decisions with rationale
- Current blockers and open questions
- Documents created
- Connected Brains (cross-references)
- Knowledge graph (accumulated patterns)
- Evolution log (deepening understanding)
- Success metrics

Shannon automatically updates this file. The `brain-tracker` agent maintains persistent memory across sessions.

## Working with Brains

When you're in a Brain folder, Shannon:
1. Reads the Brain's `CLAUDE.md` for full context
2. Tracks decisions and documents you create
3. Updates the context file with significant events
4. Scans for connections to other Brains
