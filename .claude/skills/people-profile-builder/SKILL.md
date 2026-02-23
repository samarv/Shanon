---
name: people-profile-builder
description: Create and maintain individual colleague communication profiles in Markdown. Use when the user wants to document a person's communication style, tone preferences, decision style, sensitivities, channels, response cadence, or examples of good vs bad communication, and store it as a per-person profile under input/org/profiles/.
---

# People Profile Builder

## Overview

Create or update a per-person profile to help tailor communication and collaboration. Profiles are stored as Markdown files in `input/org/profiles/` using a consistent template.

## Workflow

### 1) Identify the person

- Use `input/org/colleagues.json` to confirm the canonical name and any aliases.
- If the name is ambiguous or missing, ask one question at a time until clear.
- Do not invent details; only use user-provided information.

### 2) Determine the file path

Store each profile at:

`input/org/profiles/<slug>.md`

Slug rules:

- Lowercase
- Spaces to hyphens
- Remove diacritics (for ascii-only filenames)
- Example: `Hans Magnus Inderberg` -> `hans-magnus-inderberg.md`

### 3) Create or update the profile

- If the file does not exist, create it using the template below.
- If it exists, update only the relevant sections and preserve existing content.
- If a section has no information yet, leave a `- TBD` placeholder.

### 4) Evolve patterns toward principles

**As you gather more evidence:**

1. **Flag "why" moments**: When someone explains their reasoning, tag with `[WHY STATED]`
2. **Look for consistency**: Do they state similar reasoning in different contexts?
3. **Promote to principle**: After 3+ confirming instances, create entry in "Stated Operating Principles"
4. **Track predictions**: Note when principles correctly/incorrectly predict behavior
5. **Maintain honesty**: Only claim "principle" status when you have their explicit reasoning, not your inference

**Quality gates for promoting to principle**:
- [ ] Do I have their words explaining "why"? (Not just my inference)
- [ ] Does this appear in 3+ different contexts?
- [ ] Can I use this to predict future behavior?
- [ ] Would *they* recognize this if I showed them?

If all YES → It's a principle worth documenting

## Profile Template

```markdown
# <Full Name>

## Overview
- Role:
- Team:
- Relationship:

## Communication Style
-

## Tone Preferences
-

## Decision Style
-

## Motivations
-

## Sensitivities / Watch-outs
-

## Preferred Channels
-

## Response Cadence
-

## Working With Them
-

## Stated Operating Principles

*Principles the person has explicitly articulated. Only add when you have 3+ instances confirming consistency.*

### [Principle Name]

**Statement**: [One-sentence principle in their words or close paraphrase]

**Evidence**:
- Quote: "[Direct quote]" (Source, Date)
- Quote: "[Another instance]" (Source, Date)
- Context: [Related background]

**How this shows up**:
- [Behavioral manifestation 1]
- [Behavioral manifestation 2]
- [Behavioral manifestation 3]

**Predictive value**:
- [What this principle helps you anticipate]
- [Situations where this principle will drive their behavior]

**Verified predictions**:
- ✓ [Prediction that came true] (Date)
- ✗ [Prediction that failed] (Date) - *[What this taught you]*

**Confidence**: High/Medium/Low

## Principle Tensions

*Optional: Add only when you've observed 2+ principles that conflict*

### [Tension Name]: [Principle A] vs [Principle B]

**Principle A**: "[Statement]"
- Evidence: [Quote/behavior]

**Principle B**: "[Statement]"
- Evidence: [Quote/behavior]

**When they conflict**:
- [Describe the situations where both principles apply]

**Resolution pattern**: [How they typically resolve this tension]
- Example: [Specific instance]

## Good Communication Examples
-

## Bad Communication Examples
-

## Notes / Examples

*Tag special entries to track principle evolution:*
- `[WHY STATED]` - Person explicitly explains reasoning
- `[PRINCIPLE CONFIRMED]` - Existing principle appears again
- `[PRINCIPLE CONFLICT]` - Behavior contradicts stated principle
- `[OPEN QUESTION]` - Unexplained behavior worth investigating

```

---

## Profile Evolution Over Time

### Monthly Review Process

Profiles should evolve from behavioral patterns to predictive mental models over time.

1. **Search for principle evidence**:
   ```bash
   grep -r "\[WHY STATED\]" content/org/profiles/
   ```

2. **Cluster by theme**: Group related "why" statements across different interactions

3. **Promote when ready**: Create "Stated Operating Principles" entry when:
   - 3+ instances confirming consistency
   - Applies across multiple contexts
   - Enables behavioral prediction

4. **Validate predictions**: Track when principle-based predictions succeed/fail

### Confidence Calibration

- **High**: Person explicitly stated this, appears in 3+ contexts, predictions validated
- **Medium**: Person stated this once or twice, pattern consistent, predictions untested
- **Low**: Inferred from behavior, not explicitly stated, needs verification

### When You Don't Know the "Why"

**For unexplained behaviors, add to Notes**:

```markdown
- [OPEN QUESTION] Why does [Person] [behavior]?
  - *Possible reasons*: [Hypothesis 1], [Hypothesis 2]
  - *How it affects working with them*: [Observable impact]
  - *How to test*: [Question to ask or situation to observe]
```

This maintains intellectual honesty: you acknowledge what you don't know rather than fabricating explanations.

### Example: Pattern → Principle Evolution

**Month 1: Behavioral Pattern**
```markdown
## Communication Style
- Values early sharing of drafts for feedback before polish
```

**Month 2: "Why" Captured**
```markdown
## Notes / Examples
- [WHY STATED] "Would love your opinions when reading through it so I can make it do a better pass, with all our input" (Feb 6 2026)
```

**Month 3: Multiple Instances**
```markdown
## Notes / Examples
- [WHY STATED] "Would love your opinions..." (Feb 6 2026)
- [PRINCIPLE CONFIRMED] Shared Scenario vision before reading it himself (Feb 6 2026)
- [PRINCIPLE CONFIRMED] Iterated quickly based on Carl's feedback (Feb 7 2026)
```

**Month 4: Promoted to Principle**
```markdown
## Stated Operating Principles

### Collaborative Refinement

**Statement**: "Better outcomes come from collective input on early drafts"

**Evidence**:
- Quote: "Would love your opinions when reading through it so I can make it do a better pass, with all our input" (Slack, Feb 6 2026)
- Shares documents in draft form, not polished final (Scenario vision doc, Feb 2026)
- Iterates quickly based on feedback: "Doing another iteration now" (Feb 7 2026)

**How this shows up**:
- Shares work-in-progress openly
- Explicitly invites critique before polish
- Commits to fast iteration cycles

**Predictive value**:
- Will share documents in draft form, not polished final
- Expects collaborative iteration, not one-way review
- Values speed of feedback over perfect first draft

**Verified predictions**:
- ✓ Shared Scenario doc before self-review (Feb 2026)
- ✓ Iterated same day based on Carl's feedback (Feb 2026)

**Confidence**: High
```
