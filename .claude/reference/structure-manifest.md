# Folder Structure Manifest

## Purpose

Defines the expected `.claude/` folder structure so skills and agents can validate their environment and ask questions when something is missing. This enables self-healing behavior.

---

## Expected Structure

```
.claude/
├── CLAUDE.md                    (required) - Project-level conventions
├── CLAUDE.local.md              (optional) - User-specific preferences (gitignored)
├── agents/                      (required) - Sub-agent definitions
│   └── *.md                     - YAML frontmatter + instructions
├── skills/                      (required) - Capability methodologies
│   └── [skill-name]/            - Skill folder (gerund naming)
│       └── SKILL.md             - Skill definition (< 500 lines)
├── reference/                   (required) - Protocol documentation
│   └── *.md                     - Shared protocols and guidelines
```

---

## Validation Protocol

### On Skill/Agent Startup

1. **Check required paths exist**:
   - `.claude/CLAUDE.md`
   - `.claude/agents/`
   - `.claude/skills/`
   - `.claude/reference/`

2. **If missing required item**: Ask ONE question
   ```
   "I notice [path] is missing. Should I create it or skip this check?"
   ```

3. **If missing optional item** (e.g., CLAUDE.local.md): Log and continue
   ```
   Note: CLAUDE.local.md not found. Using default context.
   ```

4. **Don't block on optional items** - proceed with available context

---

## Naming Conventions

### Skills
- **Folder name**: lowercase, hyphens, gerund-form
- **Examples**: `analyzing-meetings`, `routing-initiatives`, `prioritizing-todos`
- **Max length**: 64 characters

### Agents
- **File name**: lowercase, hyphens, gerund-form
- **Examples**: `updating-todos.md`, `summarizing-meetings.md`
- **Max length**: 64 characters

### YAML Frontmatter Requirements

```yaml
---
name: skill-or-agent-name        # Required, ≤64 chars, lowercase-hyphen
description: |                   # Required, ≤1024 chars
  Clear description of what this does.
  Include trigger phrase: "MUST BE USED when..." or "PROACTIVELY used for..."
tools:                           # Optional, list only what's needed
  - read_file
  - write
---
```

---

## Skill File Requirements

Each `SKILL.md` must include:

| Section | Required | Purpose |
|---------|----------|---------|
| Purpose | Yes | What this skill does |
| Persona | Yes | Role and expertise |
| Trigger Phrase | Yes | When to auto-activate |
| Example Input | Yes | Sample input for testing |
| Example Output | Yes | Expected output format |
| Success Criteria | Yes | Checklist of what "done" looks like |
| Quality Gates | Yes | Validation before delivery |

### Size Limit
- **Maximum**: 500 lines per SKILL.md
- **If larger**: Split into supporting files in same folder or move protocols to `reference/`

---

## Self-Healing Questions

When validating structure, ask questions ONE AT A TIME:

### Missing Required Folder
```
"The [folder] folder doesn't exist. Should I create it now?"
Options: Yes / No, skip for now
```

### Missing CLAUDE.local.md
```
"No CLAUDE.local.md found. Would you like me to create one with default preferences?"
Options: Yes / No, use defaults
```

### Skill Missing Required Section
```
"The [skill-name] skill is missing [section]. Should I add a template for it?"
Options: Yes / No, skip validation
```

---

## Integration

Skills and agents should call validation at startup:

```markdown
## Startup Validation

Before processing, verify:
1. Required folders exist (see structure-manifest.md)
2. User context available (CLAUDE.local.md or defaults)
3. Any skill-specific dependencies present

If validation fails, ask user before proceeding.
```
