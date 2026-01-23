---
name: shape-up-pitch
description: Create shaped project pitches that give teams "the whole idea" - de-risked, bounded, and ready to build. Use when you need to shape a project, create a pitch for the betting table, write a shaped proposal, create breadboards or fat marker sketches, or prepare work for a team. Requires a framed problem as input (use problem-framing skill first if needed).
---

# Shape Up Pitch

Create shaped pitches that fix time (appetite) and adjust scope to fit, rather than estimating how long a fixed scope will take.

## Core Principle: Appetite Over Estimates

**Wrong question**: "How long will this take?"
**Right question**: "How much time do we want to spend on this?"

Appetite is typically 2 or 6 weeks - long enough to build something meaningful, short enough to see the end from the beginning.

## Shaping Workflow

1. **Set the appetite** - How much time is this worth?
2. **Gather shapers** - PM + Designer + Senior Engineer (knows where the bodies are buried)
3. **Define the approach** - High-level solution at the right abstraction
4. **Identify rabbit holes** - Technical risks that could blow up the timeline
5. **De-risk** - Resolve open questions BEFORE handing off
6. **Create artifacts** - Breadboards, fat marker sketches, rough architecture
7. **Write the pitch** - Package for the betting table

## The Shaping Session

### Who Must Be Present

| Role | Responsibility |
|------|----------------|
| **PM** | Owns the framed problem, negotiates scope |
| **Designer** | Creates breadboards showing flow and logic |
| **Senior Engineer** | Validates feasibility ("is there electricity in the wall?") |

The engineer is NOT there to code. They're there to identify if the proposed UI implies backend work that doesn't exist or would exceed the appetite.

### Shaping Dynamics

- **Try to break ideas** - If an approach is too complex, don't extend time; change the approach
- **Trade actively** - "We could do A or B within appetite, not both. Which matters more?"
- **Name the rabbit holes** - "If we build that onboarding step, it actually branches into three bank integrations"

## Artifacts

### Breadboards

Show flow and logic WITHOUT visual design. A breadboard contains:

- **Places** (screens, dialogs, menus)
- **Affordances** (buttons, fields, links)
- **Connection lines** (what leads where)

```
[Appointments Screen]
    |
    ├── [2-month dot grid] → shows availability at a glance
    |       └── tap day → [Day Detail]
    |
    └── [Agenda list] → scrollable list of booked slots
            └── tap slot → [Appointment Detail]
```

### Fat Marker Sketches

Rough UI sketches drawn as if using a fat marker - impossible to add detail. Shows:

- Key screen layout
- Primary action placement
- Information hierarchy

NOT wireframes. NOT Figma files. The lack of fidelity is intentional.

### Rough Architecture

High-level view of components:

```
Components:
- 2-month dot grid view (client-side render)
- Sliding agenda view (lazy-load past 7 days)
- Creation button (triggers existing booking flow)

Data:
- Reads from existing appointments API
- No new endpoints needed

Dependencies:
- Existing booking service (confirmed available)
```

## Pitch Structure

```markdown
# [Project Name]

## Problem
[Paste the Framed Problem Statement from problem-framing]

## Appetite
[2 weeks / 6 weeks] - [Brief justification for why this budget]

## Solution
[2-3 paragraphs describing the approach at high level]

## Breadboards
[Include breadboard diagrams showing flow]

## Fat Marker Sketches
[Include rough sketches if helpful]

## Rabbit Holes
[List technical risks identified and how they're addressed]

| Rabbit Hole | Risk | Mitigation |
|-------------|------|------------|
| [Risk 1] | [What could blow up] | [How we've de-risked it] |

## No-Gos
[What's explicitly OUT of scope - prevents scope creep]

## Nice-to-Haves
[Things that could be cut if time runs short - the "dials" the team can turn]
```

## The Handoff

Give the team "the whole idea," NOT a backlog of tickets.

The team is responsible for:
- Breaking down into tasks (often using "Nine Boxes" - roughly 9 implementation chunks)
- Deciding implementation order
- Making tactical decisions within the shaped boundaries

## Circuit Breaker

If the project isn't finished at the end of the appetite:
- **Do NOT extend the timeline**
- Cancel it OR pull it back to the shaping table
- This prevents the sunk cost fallacy

## Quality Checklist

Before pitching:

- [ ] Appetite is explicit (not "as long as it takes")
- [ ] Senior engineer validated feasibility
- [ ] Rabbit holes identified and addressed
- [ ] Artifacts show logic, not just UI
- [ ] No-gos explicitly stated
- [ ] Team can understand "the whole idea" from the pitch alone

## Anti-Patterns

For detailed failure modes and how to avoid them, see [references/anti-patterns.md](references/anti-patterns.md).

## Examples

For breadboard and pitch examples, see [references/pitch-examples.md](references/pitch-examples.md).
