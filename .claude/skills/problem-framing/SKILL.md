---
name: problem-framing
description: Guide the upstream work of negotiating from feature requests to specific user struggles. Use when stakeholders request features ("build a calendar"), when scope seems unbounded, when you need to define the real problem before solutioning, or when asked to "frame this problem", "what's the real ask", "negotiate scope", or "move upstream". This skill transforms vague requests into bounded problem statements.
---

# Problem Framing

Transform feature requests into specific, bounded problem statements by moving upstream from solutions to struggles.

## Core Principle

Never accept a feature request at face value. The request "build a calendar" is a solution. The problem might be "users can't find available time slots for appointments." Framing reveals the actual struggle so the solution can be shaped appropriately.

## The Framing Workflow

1. **Receive the request** - Note it's likely in solution-space
2. **Ask "Why?"** - Uncover the underlying struggle
3. **Identify the struggling moment** - When/where does the pain occur?
4. **Bound the problem** - What's in scope, what's explicitly out?
5. **Validate** - Does the framed problem match real user behavior?

## Framing Questions

### Moving from Solution to Problem

| Request Type | Framing Question |
|--------------|------------------|
| "Build X feature" | "What struggle does X solve? When does that pain occur?" |
| "Add Y capability" | "What can't users do today? What workaround do they use?" |
| "Improve Z" | "What specifically is broken? Who experiences it?" |

### The Five Whys (Adapted)

Don't literally ask "why" five times. Instead:

1. "What prompted this request?"
2. "What happens if we don't build this?"
3. "What workaround exists today?"
4. "When exactly does the user feel this pain?"
5. "What would 'solved' look like for the user?"

### Bounding Questions

- "If we could only solve ONE aspect, which matters most?"
- "What's the minimum viable outcome?"
- "What should explicitly NOT be solved in this cycle?"

## From Request to Framed Problem

**Bad (Solution-space)**:
> "Build a newsletter builder"

**Better (Problem-space, but vague)**:
> "Users need to communicate with their audience"

**Good (Framed Problem)**:
> "Project managers need to send monthly status updates to stakeholders. Currently they copy-paste into email, losing formatting and spending 2+ hours per update. They need to select from past content and send consistent, branded updates in under 15 minutes."

## Output: Framed Problem Statement

Generate a Framed Problem Statement with these elements:

```markdown
## Framed Problem Statement

**Who**: [Specific user role/persona]

**Struggle**: [The specific moment of friction or pain]

**Current Workaround**: [How they cope today, and what it costs them]

**Desired Outcome**: [What "solved" looks like, in user terms]

**Boundaries**:
- In scope: [What this problem includes]
- Out of scope: [What this problem explicitly excludes]

**Validation**: [Evidence this is a real problem - user quotes, data, observed behavior]
```

## Anti-Patterns

| Anti-Pattern | Why It Fails | Instead |
|--------------|--------------|---------|
| Accepting requests verbatim | Commits to a solution before understanding the problem | Ask "what struggle does this solve?" |
| Framing too broadly | "Users need better communication" gives no direction | Specify who, when, what pain |
| Skipping validation | Assumes the stated problem is the real problem | Ask "have you observed this?" |
| Solution leakage | "Users need a calendar..." still contains solution | Remove all nouns that are features |

## Success Criteria

A well-framed problem:

- [ ] Contains no feature nouns (calendar, dashboard, widget)
- [ ] Specifies a user role, not "users" generically
- [ ] Describes a moment of struggle, not a capability gap
- [ ] Has explicit boundaries (in/out of scope)
- [ ] Can be validated against real user behavior
- [ ] Allows multiple possible solutions

## Handoff to Shaping

Once the problem is framed, use the `shape-up-pitch` skill to shape a bounded solution and create a pitch for the betting table.
