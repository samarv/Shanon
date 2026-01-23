---
name: eigenquestion-context
description: |
  Gather context through high-leverage eigenquestions when information is missing or ambiguous.
  ACTIVATE THIS SKILL when: (1) context is missing or unclear, (2) user asks something requiring unstated assumptions,
  (3) working within an initiative without recent context, (4) starting new work or strategic decisions,
  (5) multiple valid approaches exist without clear direction, (6) user says "clarify", "help me think through",
  or "what should I consider". This skill asks ONE discriminating question at a time to unlock maximum downstream clarity.
---

# Eigenquestion Context Gathering

Gather missing context through high-leverage questions that maximize information gain. One question at a time.

## Core Concept

An **Eigenquestion** is the single question that, when answered, also answers the largest number of subsequent questions.

Instead of asking many clarifying questions, identify the ONE question with the most **discriminating power**—the question that establishes a fundamental principle and eliminates the need to debate every downstream decision.

## When to Activate

**Use this skill when:**
- Context is missing or ambiguous
- User request requires assumptions you shouldn't make
- Starting work on an initiative without recent context
- Making strategic decisions with multiple valid paths
- You're tempted to ask 3+ clarifying questions (find the eigenquestion instead)

**Do NOT use when:**
- Context is already sufficient in initiative CLAUDE.md
- Question is operational, not strategic
- User has explicitly provided the needed context

## The Eigenquestion Protocol

### Step 1: Identify the Uncertainty Space

Before asking, map what you don't know:

```
What decisions depend on this context?
- Decision A: [what it affects]
- Decision B: [what it affects]
- Decision C: [what it affects]

Which single piece of information would resolve the most decisions?
```

### Step 2: Formulate the Eigenquestion

**Good eigenquestions are:**
- **Binary or categorical** (not open-ended): "Is this more about X or Y?"
- **Discriminating**: The answer changes the entire approach
- **Future-oriented**: Often about market direction, user behavior, or strategic bets
- **Testable**: You can imagine concrete implications of each answer

**Bad questions (avoid):**
- "Can you tell me more about...?" (too vague)
- "What do you want?" (puts burden on user)
- "What are the requirements?" (information-gathering, not discriminating)

### Step 3: Ask ONE Question

Format:

> To [achieve goal / create output], I need to understand one thing:
>
> **[Eigenquestion]?**
>
> This will determine [what it unlocks].

Wait for answer. Do not ask multiple questions.

### Step 4: Persist the Answer

After receiving the answer:

1. **If working in an initiative**: Update `Initiatives/[name]/CLAUDE.md`
   - Add to "Key Decisions & Rationale" if strategic
   - Mark resolved in "Open Questions" if applicable

2. **If cross-initiative context**: Update `CLAUDE.local.md` under "Preferences Discovered"

3. **Confirm persistence**: "✓ Captured: [brief summary of decision]"

### Step 5: Iterate or Proceed

If more context needed, return to Step 1. Identify the NEXT eigenquestion.

If context is now sufficient, proceed with the task.

## Eigenquestion Patterns

| Uncertainty Domain | Eigenquestion Pattern | What It Unlocks |
|-------------------|----------------------|-----------------|
| **Scope** | "Is this more about [solving X] or [enabling Y]?" | Feature prioritization, success metrics |
| **User priority** | "If we could only serve one user perfectly, [persona A] or [persona B]?" | Design decisions, messaging, trade-offs |
| **Timeline vs quality** | "Is shipping by [date] more important than [quality attribute]?" | Scope cuts, resource allocation |
| **Market bet** | "In 2 years, is this market more likely to value [consistency] or [comprehensiveness]?" | Platform strategy, partnership decisions |
| **Core identity** | "Are we fundamentally a [X] or a [Y]?" | Product direction, what to say no to |
| **Resource allocation** | "If we had to cut half the scope, what's the non-negotiable core?" | MVP definition, phasing |
| **Integration** | "Should this [stand alone] or [integrate deeply with X]?" | Architecture, dependencies, timeline |

## Examples

### Example 1: Vague Feature Request

**User**: "We need to add collaboration features to Board."

**Uncertainty space**:
- Real-time or async collaboration?
- Internal team or external stakeholders?
- Light commenting or deep co-authoring?

**Eigenquestion**:
> To shape the right collaboration features, I need to understand one thing:
>
> **Is Board collaboration primarily about teams working together in real-time (like Figma), or about asynchronous review and feedback (like Google Docs comments)?**
>
> This determines the entire technical architecture and UX model.

### Example 2: Strategic Direction

**User**: "Help me write a pitch for the betting table."

**Uncertainty space**:
- What problem are we solving?
- Which customer segment?
- What's the appetite (small/medium/large batch)?

**Eigenquestion**:
> To write a compelling pitch, I need to understand one thing:
>
> **Is this pitch addressing a known pain point we've validated, or exploring a new opportunity we believe in but haven't proven?**
>
> This determines whether we lead with user evidence or strategic vision.

### Example 3: Prioritization Decision

**User**: "We're behind on the Global Launch timeline. What should we cut?"

**Uncertainty space**:
- What's the must-have for launch?
- What defines "launch" vs "post-launch"?
- Which stakeholders care about which features?

**Eigenquestion**:
> To recommend scope cuts, I need to understand one thing:
>
> **Is the Global Launch deadline immovable (we ship whatever's ready), or is it the feature set that's immovable (we slip if needed)?**
>
> This determines whether we're cutting features or negotiating timeline.

## Anti-Patterns

| Anti-Pattern | Why It Fails | Instead |
|--------------|--------------|---------|
| Asking 5 questions at once | Overwhelms user, loses discriminating power | Find the ONE eigenquestion |
| "Tell me more about..." | Puts burden on user, vague | Offer binary/categorical choice |
| Asking about details before strategy | Wastes effort if direction changes | Start with strategic eigenquestion |
| Not persisting answers | Loses context, re-asks later | Always update CLAUDE.md |
| Asking questions you can answer yourself | Wastes user time | Check existing context first |

## Quality Check

Before asking, verify:
- [ ] I checked initiative CLAUDE.md for existing context
- [ ] This question has discriminating power (answer changes approach)
- [ ] It's binary or categorical, not open-ended
- [ ] I'm asking ONE question, not bundling multiple
- [ ] I know where I'll persist the answer

## References

For detailed examples and case studies, see [references/examples.md](references/examples.md).
