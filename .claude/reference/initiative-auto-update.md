# Initiative Context Auto-Update Protocol

## Purpose

Automatically maintain living documentation for each initiative by updating initiative-specific CLAUDE.md files based on conversation context, decisions, and work performed.

## Activation Conditions

**This protocol activates when:**
- Current working directory is within `/Initiatives/[initiative-name]/` path
- User is creating documents, making decisions, or discussing initiative-related work
- Significant events occur during the conversation (see triggers below)

## Detection Triggers

Monitor conversations for these significant events:

### High Priority Events (Always Capture)

- **Document Creation**: New PRDs, strategies, GTM plans, analyses, or templates created
- **Explicit Decisions**: User says "we'll go with," "decided to," "let's do," "we should," "our approach is"
- **Status Changes**: "completed," "blocked," "paused," "resumed," "ready to launch," "shipped"
- **Key Milestones**: "launched," "validated," "approved," "signed off"
- **Blockers Identified**: "can't proceed because," "waiting on," "blocked by," "dependency on"

### Medium Priority Events (Capture When Relevant)

- **Framework Application**: Team Topologies, LNO, Jobs-to-be-Done, Wardley Mapping applied to initiative
- **Stakeholder Input**: Feedback, requirements, or decisions from stakeholders mentioned
- **Success Metrics**: New metrics defined, baselines set, or results measured
- **Trade-offs Made**: Explicit choices between alternatives with rationale
- **Questions Raised**: Open questions or uncertainties that need resolution

### Low Priority Events (Optional Capture)

- **Research Findings**: Competitive analysis, user research, market insights
- **Template Usage**: Which templates were applied and why
- **Cross-Initiative Dependencies**: Links or dependencies identified with other initiatives

## Auto-Update Execution Protocol

### Step 1: Detect Initiative Context

```
When working in: /Initiatives/[initiative-name]/
Check for: [initiative-name]/CLAUDE.md
If not exists: Offer to create from standard template
If exists: Read current content before updating
```

### Step 2: Monitor & Accumulate During Conversation

As conversation progresses, track:
- Decisions made and their rationale
- Documents created with their purpose
- Status changes or milestone updates
- New blockers or open questions identified
- Key stakeholder feedback or input received
- Framework applications and insights

### Step 3: Trigger Update Decision

**Automatic trigger when:**
- Conversation includes 2+ high priority events
- Document creation or major edit completes
- User explicitly says "update initiative context"
- End of conversation with significant decisions made

**Proactive notification:**
> "I noticed we [made decisions about X / created Y / identified blocker Z].
> I'll update this initiative's CLAUDE.md to capture this context."

### Step 4: Execute Update

1. **Read** current `Initiatives/[initiative-name]/CLAUDE.md`
2. **Extract** relevant context from this conversation:
   - What decisions were made and why
   - What documents were created and their purpose
   - What changed in status or progress
   - What new questions or blockers emerged
   - What frameworks or insights were applied
3. **Update** appropriate sections:
   - Append to "Key Decisions & Rationale"
   - Refresh "Current Status"
   - Add to "Documents in This Initiative"
   - Update "Open Questions" or mark as resolved
   - Record in "Lessons Learned" if applicable
   - Update "Last Updated" timestamp
4. **Preserve** all existing content - never overwrite, only append/update
5. **Confirm** to user: "✓ Updated [Initiative Name] context in CLAUDE.md"

## Initiative CLAUDE.md Standard Template

When creating a new initiative CLAUDE.md file, use this template:

```markdown
# [Initiative Name] - Context & Memory

## Initiative Overview
- **Status**: [Planning/Active/Blocked/Paused/Completed]
- **Timeline**: [Start Date] - [Target End Date]
- **Owner**: [Who's leading this initiative]
- **Last Updated**: [YYYY-MM-DD HH:MM]

## Core Objective
[What are we trying to achieve and why? Focus on customer/business outcome, not features.]

## Key Decisions & Rationale
<!-- Newest first, maintain chronological order -->

- **[Decision Topic]** (YYYY-MM-DD)
  - *Decision*: [What was decided]
  - *Rationale*: [Why this choice]
  - *Trade-offs*: [What we're giving up or accepting]
  - *Related docs*: [Links if applicable]

## Current Status

**Last Updated**: [YYYY-MM-DD HH:MM]

- **Progress**: [Current state in 1-2 sentences]
- **Recent Changes**: [What changed since last update]
- **Next Milestone**: [What's coming next]
- **Confidence Level**: [High/Medium/Low - in hitting timeline/goals]

## Blockers & Open Questions

### Active Blockers
- **[Blocker Title]** (YYYY-MM-DD)
  - *Context*: [Why this is blocking progress]
  - *Impact*: [What's affected]
  - *Resolution Plan*: [How we plan to unblock]

### Open Questions
- **[Question]** (YYYY-MM-DD)
  - *Context*: [Why this matters]
  - *Impact*: [What depends on the answer]
  - *Status*: [Pending/Researching/Resolved]

## Stakeholders & Context

- **Primary Stakeholders**: [Who cares most about this]
- **Key Contributors**: [Who's working on this]
- **External Dependencies**: [What we depend on outside the team]
- **Related Initiatives**: [Cross-references to other initiatives]

## Documents in This Initiative

- [Document Name](./document-name.md) (YYYY-MM-DD)
  - *Purpose*: [Why this document exists]
  - *Status*: [Draft/Review/Final/Archived]
  - *Key Insights*: [Main takeaways]

## Lessons Learned

- **[Lesson Title]** (YYYY-MM-DD)
  - *What Worked*: [Successful patterns to replicate]
  - *What Didn't*: [Mistakes or anti-patterns to avoid]
  - *Application*: [How this applies to future work]

## Success Metrics

- **[Metric Name]**: [Baseline] → [Target] → [Current]
  - *Why it matters*: [Connection to objective]
  - *Measurement method*: [How we track this]

## Frameworks Applied

- **[Framework Name]** (YYYY-MM-DD)
  - *Application*: [How we used it]
  - *Insights*: [What we learned]
  - *Artifacts*: [Links to analysis/documents]
```

## Update Format Standards

### Decision Entry Format

```markdown
- **[Decision Topic]** (YYYY-MM-DD)
  - *Decision*: [Brief, clear statement of what was decided]
  - *Rationale*: [Why this choice - connect to customer/business value]
  - *Trade-offs*: [What we're giving up, what we're accepting]
  - *Related docs*: [filename.md](./filename.md)
```

### Status Update Format

```markdown
**Last Updated**: YYYY-MM-DD HH:MM
- **Progress**: [Current state - be specific about % complete or milestone reached]
- **Recent Changes**: [What changed since last update - focus on outcomes]
- **Next Milestone**: [What's coming next with target date]
- **Confidence Level**: [High/Medium/Low] - [brief reason]
```

### Document Entry Format

```markdown
- [Document Name](./document-name.md) (YYYY-MM-DD)
  - *Purpose*: [Why this document exists - what decision does it enable?]
  - *Status*: [Draft/Review/Final/Archived]
  - *Key Insights*: [1-2 sentence takeaway]
```

### Blocker/Question Resolution Format

```markdown
- **[Original Blocker/Question]** (YYYY-MM-DD) - RESOLVED (YYYY-MM-DD)
  - *Resolution*: [How it was resolved]
  - *Impact*: [What this unblocked or enabled]
```

## Quality Standards for Updates

### Conciseness

- Each entry: 2-3 sentences maximum
- Focus on "what" and "why", not detailed "how"
- Link to documents for implementation details

### Relevance

- Only capture information valuable for future context
- Skip routine/trivial updates
- Prioritize decisions and outcomes over process notes

### Clarity

- Use clear, searchable language
- Avoid ambiguous pronouns ("this", "it", "that")
- Include enough context to understand months later
- Write for someone new joining the initiative

### Chronological Integrity

- Maintain reverse chronological order (newest first) within sections
- Always include timestamps
- Preserve historical entries - never delete, only append or mark as resolved

## Integration with Core Frameworks

### Shreyas Doshi PM Principles

Ensure updates reflect:
- **Customer value focus**: Not just features, but customer outcomes
- **Explicit trade-offs**: Make all trade-offs visible
- **Outcome-based thinking**: Measure success by results, not output
- **First principles reasoning**: Connect decisions to fundamental truths

### LNO Prioritization Framework

Categorize updates by strategic value:
- **Leverage**: High-impact decisions, breakthrough insights, successful patterns
- **Neutral**: Standard updates, routine progress, maintenance items
- **Overhead**: Process notes, administrative updates

Prioritize capturing Leverage items in detail.

### Planner-Execution Loop Integration

**During UNDERSTAND phase:**
- Read initiative's CLAUDE.md for existing context
- Reference previous decisions and current status
- Identify gaps in knowledge or documentation

**During PLAN phase:**
- Apply patterns from "Lessons Learned"
- Consider "Open Questions" and "Blockers"
- Reference related documents and stakeholder context

**During EXECUTE phase:**
- Note significant events as they occur
- Track decisions and rationale in real-time
- Document framework applications and insights

**During VALIDATE phase:**
- Trigger update if significant events occurred
- Verify context captured accurately
- Update status and next milestones

## Manual Control Options

User can control updates with these commands:

- **"Update initiative context"** - Immediate manual trigger
- **"Don't update context"** - Skip auto-update for this session
- **"Show me what you'd update"** - Preview changes before committing
- **"Create initiative CLAUDE.md"** - Generate new file from template
- **"Summarize session for CLAUDE.md"** - Generate summary first, ask before updating

## Edge Cases & Handling

### No CLAUDE.md Exists

```
Prompt: "This initiative doesn't have a CLAUDE.md context file yet.
Should I create one using the standard template?
[Shows template preview]"
```

### Multiple Initiatives Referenced

- Update only the initiative folder where primary work occurred
- If ambiguous, ask: "Which initiative should I update: [list options]?"
- Can update multiple if clearly working across initiatives

### Sensitive Information Detection

- **Never** auto-capture: credentials, API keys, PII, internal code names, unannounced features
- Warn user if detected: "I'll skip recording sensitive information mentioned in this conversation"

### Conflicting Information

If new information contradicts existing entries:
```markdown
- **[Original Topic]** (YYYY-MM-DD) - UPDATED (YYYY-MM-DD)
  - *Original*: [Previous information]
  - *Update*: [New information]
  - *Reason for change*: [Why the change]
```

### Initiative Completion

When initiative reaches "Completed" status:
- Add final summary to "Core Objective" section
- Mark all open questions as closed or transferred
- Document final metrics vs targets
- Capture key lessons learned
- Update status to "Completed" with completion date

## Performance Optimization

### Efficiency

- Accumulate updates during conversation (don't write after every message)
- Write once at end of conversation or when explicitly triggered
- Batch multiple updates into single file write operation
- Cache initiative name and path to avoid repeated directory checks

### Smart Detection

- Use keyword pattern matching for high-priority event detection
- Learn from user feedback about what to capture
- Adjust verbosity based on initiative phase (more detail in planning, less in maintenance)

## Success Criteria

**This protocol succeeds when:**
1. Initiative context is always current without manual effort
2. User never has to re-explain previous decisions
3. AI can quickly get up to speed on any initiative by reading CLAUDE.md
4. Historical context enables better recommendations and decision-making
5. Zero information loss between sessions
6. Context files are valuable reference documents even without AI

## Activation Summary

**This protocol automatically activates for every conversation where:**
- Working directory path contains `/Initiatives/[initiative-name]/`
- User creates/edits files within initiative folder
- Significant events detected (decisions, documents, status changes)

**Result**: Every initiative maintains living documentation that automatically captures context, decisions, and progress with minimal user intervention while maintaining high quality standards.
