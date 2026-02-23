# Organizational Context & Name Lookup

## Colleagues Database

**File**: `content/org/colleagues.json`

This file contains organizational chart data. Use it to:
- Identify correct spelling of colleague names
- Understand reporting relationships and team structures
- Find who reports to whom
- Determine which division/team someone belongs to
- Resolve name ambiguities (e.g., "Michael" → which Michael?)

## User Context

For user-specific organizational context (name, team, manager, reporting chain), see `CLAUDE.local.md`.

## When to Reference

Automatically consult `content/org/colleagues.json` when:
- Writing emails to/about colleagues (verify name spelling)
- Discussing organizational context or team structures
- Mentioning stakeholders in documents
- Clarifying reporting chains or escalation paths
- User mentions a partial name or nickname

## Name Correction Protocol

Before finalizing any document mentioning colleagues:
1. Check `content/org/colleagues.json` for correct spelling
2. Verify organizational context is accurate
3. Use full names on first reference, then can use first names

For detailed name verification protocol, see `.claude/reference/name-verification.md`.
