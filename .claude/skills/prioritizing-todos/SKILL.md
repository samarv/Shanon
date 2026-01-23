---
name: prioritizing-todos
description: |
  PROACTIVELY used when user needs daily priorities or LNO classification.
  Generates and maintains TODO.md with Leverage/Neutral/Overhead priorities.
  Scans active initiatives and extracts actionable items dynamically.
---

# Prioritizing TODOs Skill

## Purpose

Generate and maintain a daily TODO.md file that:
1. **Scans active initiatives** dynamically from Initiatives/ folder
2. **Extracts actionable items** (blockers, questions, milestones)
3. **Classifies using LNO framework** (Leverage, Neutral, Overhead)
4. **Creates dated sections** preserving history

Goal: Look at TODO.md and immediately know what high-leverage work to prioritize.

For product-specific context, see `CLAUDE.local.md`.

---

## Persona

**Role**: Executive Assistant / Chief of Staff with ruthless prioritization focus

**Mindset**:
- Leverage-first - always ask "what unblocks the most?"
- Initiative-aware - understands which workstream each item belongs to
- Action-oriented - every item should be doable TODAY
- Honest about overhead - clearly marks admin work as low-priority

---

## LNO Framework

| Category | Definition | Time | Action |
|----------|------------|------|--------|
| **Leverage** | Work that creates disproportionate value; unblocks others | 80% | Do first |
| **Neutral** | Important but predictable; scheduled tasks | 15% | Schedule, batch |
| **Overhead** | Necessary but low-value; admin; documentation | 5% | Minimize, delegate |

### Classification Decision Matrix

**Leverage Indicators**:
- Active Blockers with cross-initiative impact
- Decisions that block downstream tasks
- Questions where the answer changes the plan
- Items affecting major deadlines

**Neutral Indicators**:
- Next Milestones without blocking dependencies
- Routine follow-ups on existing threads
- Scheduled tasks already committed
- Items with future dates

**Overhead Indicators**:
- Documentation updates
- Process compliance (reviews, approvals)
- Administrative tasks (calendar, scheduling)
- Cleanup tasks

### Classification Prompt

For each item, ask:
1. "Does this unblock other work?" → Leverage
2. "Can this be scheduled for a specific time?" → Neutral
3. "Necessary but doesn't advance the initiative?" → Overhead

When uncertain, default to **Neutral**.

---

## Initiative Discovery

**CRITICAL: Never hardcode initiative names. Always discover dynamically.**

```
1. List all subdirectories in /Initiatives/
2. For each subdirectory:
   a. Check if CLAUDE.md exists
   b. Extract Status from "Initiative Overview" section
   c. Only process initiatives with Status: Active
3. Build registry with name, objective, status
```

### Extract Actionable Items

From each active initiative's CLAUDE.md:

| Section | What to Extract | Default LNO |
|---------|-----------------|-------------|
| **Active Blockers** | All items | Leverage |
| **Open Questions** | Status: Pending only | Leverage/Neutral |
| **Next Milestone** | Upcoming milestone | Neutral |

---

## TODO.md Generation

### File Location
`TODO.md` in project root

### Update Behavior
- Add new dated section at TOP
- Preserve all previous sections
- Never overwrite existing content

### Output Template

```markdown
# Daily Priorities

## [DATE] ([DAY_OF_WEEK])

*Generated from [N] active initiatives at [TIMESTAMP]*

### L - Leverage (Do First)
*High-impact work that unblocks others.*

**[initiative-name]**
- [ ] [Task title] - [Brief context]

### N - Neutral (Schedule)
*Important but predictable. Timebox these.*

**[initiative-name]**
- [ ] [Task title] - [Brief context]

### O - Overhead (Minimize)
*Necessary but low-value. Delegate if possible.*

**[initiative-name]**
- [ ] [Task title] - [Brief context]

---
```

### Task Title Guidelines
- Start with action verb: "Clarify", "Follow up", "Decide", "Review"
- Be specific: Include what, who, or which
- Keep under 10 words
- Include deadline references if relevant

---

## Execution Protocol

1. **Check existing TODO.md** - If today's section exists, ask user to regenerate or append
2. **Discover initiatives** - Scan Initiatives/, filter for Active status
3. **Extract items** - From Active Blockers, Pending Questions, Next Milestone
4. **Classify items** - Apply LNO decision matrix
5. **Generate output** - Group by LNO, then by initiative
6. **Write and confirm** - "✓ Updated TODO.md with [N] items across [M] initiatives"

---

## Quality Gates

### Before Generation
- [ ] Initiatives folder scanned dynamically
- [ ] Only Active initiatives processed
- [ ] Each CLAUDE.md read completely

### During Classification
- [ ] Each item assigned exactly one LNO category
- [ ] Leverage items are truly high-impact (not just urgent)
- [ ] Blockers with cross-initiative impact identified

### Before Writing
- [ ] Date format correct: `YYYY-MM-DD (Day)`
- [ ] Task titles start with action verbs
- [ ] Context is concise (one phrase)
- [ ] Previous content preserved

### Anti-Patterns
- ❌ Hardcoding initiative names
- ❌ Processing paused/completed initiatives
- ❌ Marking everything as Leverage
- ❌ Vague task titles ("Do the thing")
- ❌ Overwriting previous days' content
- ✅ Scan Initiatives/ folder fresh each time
- ✅ Apply decision matrix consistently
- ✅ Action-oriented, specific tasks

---

## Example

**Input**: "What should I work on today?"

**Output**:
```markdown
## 2026-01-21 (Tuesday)

*Generated from 3 active initiatives at 14:30*

### L - Leverage (Do First)
**docs-integration**
- [ ] Clarify regionalization requirement - blocks launch decision
- [ ] Follow up on consultant priority - capacity blocker

### N - Neutral (Schedule)
**docs-integration**
- [ ] Align squad on scope reduction - next milestone

### O - Overhead (Minimize)
**ai-renderings**
- [ ] Update help article draft - documentation
```

"✓ Updated TODO.md with 4 items across 2 initiatives (2L, 1N, 1O)"

---

## Success Criteria

1. User can immediately identify highest-leverage work
2. All active initiatives represented
3. Blockers correctly identified as Leverage
4. Historical sections preserved
5. Items are actionable with clear context
6. No stale or resolved items
7. Cross-initiative dependencies visible
