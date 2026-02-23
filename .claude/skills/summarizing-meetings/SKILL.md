---
name: summarizing-meetings
description: |
  MUST BE USED when generating meeting summaries after analysis and routing.
  Creates per-brain and overall summaries, updates CLAUDE.md files.
  Works with analyzing-meetings and routing-brains skills.
---

# Summarizing Meetings Skill

## Purpose

Generate actionable meeting summaries after routing:
1. **Per-brain summaries** for each affected brain
2. **Overall meeting summary** with cross-brain context
3. **Update brain CLAUDE.md files** with new content

For product-specific context, see `CLAUDE.local.md`.

---

## Persona

**Role**: Programme Manager / Chief of Staff

**Mindset**:
- Action-oriented - every summary should enable follow-up
- Context-aware - understands organizational dynamics
- Completeness over speed - never summarize partial content

---

## Per-Brain Summary Template

```markdown
## [Brain Name] - Meeting Updates

**Meeting**: [Meeting Name] | **Date**: [Date]

### Items Routed to This Brain

#### Decisions
- **[Decision Topic]** (YYYY-MM-DD)
  - *Decision*: [What was decided]
  - *Rationale*: [Why, if discussed]
  - *Impact*: [What this affects]

#### Action Items
| Action | Owner | Due Date | Context |
|--------|-------|----------|---------|
| [Action] | [Name] | [Date] | [Related discussion] |

#### Discussion Points
- [Key point 1]
- [Key point 2]

#### Blockers/Questions
- **[Blocker/Question]**
  - *Context*: [Why this matters]
  - *Status*: [Pending/Needs Resolution]

### Cross-Brain Dependencies
- [Any items that also affect other brains]
```

---

## Overall Meeting Summary Template

```markdown
# Meeting Summary | [Meeting Name] | [Date]

## Overview
**Attendees**: [List participants]
**Duration**: [Approximate length]
**Purpose**: [Meeting objective]

## Brain Distribution

| Brain | Items Routed | Key Outcome |
|------------|--------------|-------------|
| [Brain 1] | [N] items | [One-line summary] |
| [Brain 2] | [N] items | [One-line summary] |
| Unmatched | [N] items | Pending assignment |

## Cross-Brain Themes
- [Theme across multiple brains]
- [Dependencies identified]

## Consolidated Action Items
| # | Action | Owner | Due | Brain |
|---|--------|-------|-----|------------|
| 1 | [Action] | [Name] | [Date] | [Brain] |

## Unresolved Items
- [Items requiring follow-up]

## Next Steps
- [Overall next steps]
```

---

## Quick Recap Format

For short meetings or highlights only:

```markdown
**Meeting Recap** | [Meeting Name] | [Date]

**Routed to Brains:**
- [Brain 1]: [N] items ([one-line summary])
- [Brain 2]: [N] items ([one-line summary])

**Key Decisions:**
- [Decision 1] → [Brain]

**Action Items:**
- [ ] [Action] - [Owner] - [Due] → [Brain]

**Unmatched Items**: [N] items pending assignment
```

---

## Updating Brain CLAUDE.md Files

### Key Decisions Section
Append new decisions:
```markdown
- **[Decision Topic]** (YYYY-MM-DD)
  - *Decision*: [What was decided]
  - *Rationale*: [Why this choice]
  - *Trade-offs*: [What we're giving up]
  - *Related docs*: Meeting notes [Date]
```

### Current Status Section
Update if meeting changed status:
```markdown
**Last Updated**: YYYY-MM-DD HH:MM
- **Progress**: [Updated based on discussion]
- **Recent Changes**: [What changed]
- **Next Milestone**: [Updated if discussed]
```

### Open Questions Section
- Mark questions as RESOLVED if answered
- Add new questions raised

### Update Prompt
Before updating any CLAUDE.md, ask:
```
Should I update [Brain Name]/CLAUDE.md with:
- [N] decisions
- [N] action items
- [N] status updates
- [N] questions resolved

Proceed? (y/n)
```

---

## LNO Classification for Items

Classify items using Leverage-Neutral-Overhead:

| Classification | Criteria | Handling |
|----------------|----------|----------|
| **Leverage** | Decisions affecting multiple brains, blockers, timeline changes | Highlight prominently |
| **Neutral** | Status updates, routine discussions | Standard placement |
| **Overhead** | Administrative, scheduling, logistics | Capture briefly or omit |

### Prioritization in Summaries
1. **Lead with Leverage items** - Top of each section
2. **Group Neutral items** - Standard sections
3. **Minimize Overhead** - Only if actionable

---

## The "Skeptical Executive" Test

Before finalizing, ensure summary answers:

| Question | Your Summary Must Answer |
|----------|--------------------------|
| "What did we decide?" | Clear decisions with owners |
| "Who's doing what by when?" | Action items with deadlines |
| "What's blocking us?" | Blockers with resolution plans |
| "What changed?" | Status updates with impact |
| "What do I need to do?" | Clear next steps for reader |

If any question can't be answered → there's a gap.

---

## Example Input

```
Routed items:
- frontend-modernization: 2 decisions, 1 action
- api-platform: 1 blocker, 2 discussions
- Unmatched: 0 items
```

## Example Output

```markdown
# Meeting Summary | Weekly Sync | 2026-01-21

## Overview
**Attendees**: Engineering Lead, PM, Designer
**Duration**: 30 minutes
**Purpose**: Weekly status and blockers

## Brain Distribution
| Brain | Items | Key Outcome |
|------------|-------|-------------|
| frontend-modernization | 3 | React migration approved |
| api-platform | 3 | API blocker identified |

## Consolidated Action Items
| # | Action | Owner | Due | Brain |
|---|--------|-------|-----|------------|
| 1 | Create React migration plan | Engineering | Jan 28 | frontend-modernization |
| 2 | Escalate API blocker | PM | Jan 22 | api-platform |

## Next Steps
- React migration kickoff scheduled for next week
- API blocker needs resolution before launch
```

---

## Quality Gates

- [ ] Per-brain summaries generated
- [ ] Overall summary includes all routed items
- [ ] Cross-brain dependencies noted
- [ ] Action items have owners and deadlines
- [ ] Leverage items highlighted
- [ ] CLAUDE.md updates confirmed with user

---

## Anti-Patterns

- ❌ Summarizing before complete read-through
- ❌ Losing context when splitting by brain
- ❌ Forgetting cross-brain dependencies
- ❌ Overwriting existing CLAUDE.md content
- ❌ Adding duplicates
- ✅ Maintain overall context while routing to brains
- ✅ Append only, verify before writing
- ✅ Ask before updating CLAUDE.md files

---

## Success Criteria

1. Per-brain summaries actionable
2. Overall summary provides cross-brain context
3. CLAUDE.md files updated correctly
4. Leverage items highlighted
5. User can take immediate action from summary
