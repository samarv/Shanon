---
paths:
  - "Brains/**"
---

# Working with Brains

Brains are self-contained knowledge contexts that actively accumulate and connect information. Each Brain has a `CLAUDE.md` that serves as living documentation.

## When Working in a Brain

1. **Read** the Brain's `CLAUDE.md` first for full context
2. **Track** decisions, documents, and status changes during the session
3. **Update** the Brain's CLAUDE.md with significant events before the session ends
4. **Connect** -- scan for topic overlap with other Brains and note cross-references

## What to Capture

**Always capture**: decisions with rationale, document creation, status changes, blockers, key milestones.
**Sometimes capture**: framework applications, stakeholder feedback, success metrics, trade-offs.
**Skip**: routine process notes, trivial updates.

## Cross-Brain Connections

When updating a Brain, use `Brains/INDEX.md` to find connections:
- Read `Brains/INDEX.md` for the topic map of all Brains
- Match current Brain's topics against other entries
- Update "Connected Brains" section in both CLAUDE.md files
- Update INDEX.md with any new connections

## Brain CLAUDE.md Updates

Use the brain-auto-update protocol: @.claude/reference/brain-auto-update.md

## Quality Standards

- Each entry: 2-3 sentences max
- Focus on "what" and "why", not "how"
- Include enough context for someone new to understand months later
- Maintain reverse chronological order (newest first)
- Never delete entries, only append or mark as resolved
