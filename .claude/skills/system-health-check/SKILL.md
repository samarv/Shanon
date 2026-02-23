---
name: system-health-check
description: |
  Diagnose Shannon system integrity. Use when something seems broken, on first run,
  or when user asks "check system health", "diagnose Shannon", "what's broken",
  "is Shannon set up correctly", or "run health check".
context: fork
allowed-tools: Read, Glob, Grep, Bash
---

# System Health Check

You are Shannon's self-diagnostic system. Scan the project for structural issues, broken references, and configuration problems. Report findings clearly and propose fixes.

## Diagnostic Checklist

Run these checks in order:

### 1. Folder Structure

Verify these directories exist:
- `Brains/`
- `input/`
- `output/`
- `.claude/rules/`
- `.claude/hooks/`
- `.claude/reference/`
- `.claude/agents/`
- `.claude/skills/`
- `.claude/defaults/`

### 2. Core Rules Files

Verify `.claude/rules/` contains:
- `pm-philosophy.md`
- `quality-gates.md`
- `output-conventions.md`
- `input-resolution.md`
- `brain-context.md`
- `analytical-reasoning.md`

### 3. Hook Scripts

Verify `.claude/hooks/` contains executable scripts:
- `check-onboarding.sh` (SessionStart: detects missing CLAUDE.local.md)
- `log-session.sh` (Stop: logs session activity for pattern detection)

Verify `.claude/settings.json` exists and contains `SessionStart` and `Stop` hooks.

### 4. Brain Integrity

Check `Brains/INDEX.md` exists and is not empty (beyond template).

For each subdirectory in `Brains/`:
- Check if `CLAUDE.md` exists
- If it exists, verify it has required sections: Brain Overview, Core Objective, Key Decisions, Current Status
- Check the Brain has an entry in `Brains/INDEX.md`
- Flag Brains missing CLAUDE.md or missing from INDEX

### 5. Reference Protocols

Verify `.claude/reference/` contains:
- `brain-auto-update.md`
- `uncertainty-protocol.md`
- `meeting-protocols.md`

### 6. Agent Configuration

For each `.claude/agents/*.md`:
- Verify YAML frontmatter has `name` and `description`
- Check for references to old paths (`Initiatives/`, `content/`, `Operations/`, `Output/`)

### 7. User Context

Check if `CLAUDE.local.md` exists:
- If missing: flag as "Onboarding not complete"
- If exists: check for key sections (name, role, preferences)

## Output Format

```
# Shannon Health Check Report

## Status: [GREEN | YELLOW | RED]

### Checks Passed
- [x] Folder structure complete
- [x] Core rules present
- ...

### Issues Found
1. **[Issue]** -- [Description]
   - Fix: [What to do]
   - Auto-fixable: [Yes/No]

### Recommended Actions
1. [Most important fix first]
2. ...
```

## Fix Proposals

For each issue found:
1. Explain what's wrong in plain language
2. Propose a specific fix
3. Ask "Should I fix this?" before making any changes
4. Apply fixes one at a time, confirming each

Never silently fix issues. Transparency is a core Shannon principle.

## Success Criteria

- All folders exist
- All rule files present and well-formed
- All hook scripts present and executable
- All Brains have valid CLAUDE.md
- No broken path references
- CLAUDE.local.md exists with user context
