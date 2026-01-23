# Meeting Analysis Protocols

Shared protocols used by analyzing-meetings, routing-initiatives, and summarizing-meetings skills.

---

## Ambiguity Detection Protocol

### Core Principle

**When uncertain, STOP and ask. Never assume or infer when ambiguity exists.**

Ambiguity detection happens BEFORE routing, not after.

### Ambiguity Types

| Ambiguity Type | Trigger Phrases | Question to Ask |
|----------------|-----------------|-----------------|
| **Decision vs Discussion** | "Maybe", "we could", "thinking about", "might" | "Was this a firm decision or still under discussion?" |
| **Owner Unclear** | Action without "I'll", "[Name] will" | "Who owns this action item?" |
| **Timeline Ambiguous** | "Soon", "later", "eventually" | "Is there a target date for this?" |
| **Scope Unclear** | Feature mentioned without definition | "What specifically does '[X]' include?" |
| **Conflicting Statements** | Multiple positions without resolution | "Which approach was chosen?" |
| **Conditional Decision** | "If", "depends on", "assuming" | "Is the condition met? What's the fallback?" |

### Ambiguity Scoring

| Score Range | Classification | Action |
|-------------|----------------|--------|
| 0.0 - 0.3 | **Clear** | Proceed with routing |
| 0.3 - 0.5 | **Minor** | Route but flag with [Verify] tag |
| 0.5 - 0.7 | **Significant** | MUST ask user before routing |
| 0.7 - 1.0 | **Critical** | STOP immediately, ask user |

### Mandatory Question Protocol

When ambiguity score > 0.5:

**Step 1**: Present the ambiguous item
```
I found something unclear:
**Item**: "[Quote or paraphrase]"
**Context**: [Where this appeared]
**Ambiguity type**: [Type]
```

**Step 2**: Ask ONE specific question

**Step 3**: Wait for response before continuing

**Step 4**: Acknowledge and continue
```
Got it - [acknowledge]. Continuing with analysis...
```

### Anti-Patterns

- ❌ Assuming "we could" means "we decided"
- ❌ Inferring owners from context without confirmation
- ❌ Treating vague timelines as commitments
- ❌ Batching multiple ambiguous items into one question
- ✅ Asking one question at a time
- ✅ Waiting for explicit confirmation

---

## Pending Document Detection Protocol

### Purpose

When action items involve creating documents, pre-register them in initiative CLAUDE.md files.

### Detection Triggers

| Trigger Phrase | Example | Action |
|----------------|---------|--------|
| "write a doc/document" | "I'll write a doc laying out the tradeoffs" | Register as pending |
| "create a [type]" | "Create a PRD for this feature" | Register as pending |
| "put together a" | "Put together a summary for leadership" | Register as pending |
| "draft a" | "Draft a proposal for the new approach" | Register as pending |
| "document the" | "Document the decision rationale" | Register as pending |
| "write up" | "Write up the requirements" | Register as pending |

### Document Registration Format

```markdown
- [Document Name] (YYYY-MM-DD - PENDING)
  - *Purpose*: [Why this document is being created]
  - *Status*: To be written by [Owner] by [Due date if known]
  - *Cross-reference*: [Other initiatives if applicable]
```

### Cross-Initiative Documents

When a document affects multiple initiatives:
1. Add entry to ALL relevant initiative CLAUDE.md files
2. Include cross-reference in each entry
3. Note in routing summary which initiatives share this document

### Integration with Action Items

Document-creating actions should appear in TWO places:
1. **Action Items table**: With owner, due date, initiative
2. **Documents section**: As PENDING entry with purpose

### Anti-Patterns

- ❌ Capturing document actions ONLY in Action Items
- ❌ Missing cross-initiative documents
- ❌ Not marking documents as PENDING
- ✅ Register in BOTH Action Items AND Documents sections
- ✅ Add cross-references when document affects multiple initiatives

---

## Quality Gates Summary

### Before Processing
- [ ] Complete content read (beginning to end)
- [ ] Input type correctly classified
- [ ] Speaker label presence assessed
- [ ] All initiatives discovered dynamically

### Ambiguity Resolution
- [ ] All items scanned for ambiguity triggers
- [ ] Items with score > 0.5 flagged
- [ ] User prompted for ALL high-ambiguity items
- [ ] Clarifications recorded and incorporated

### Document Capture
- [ ] Action items scanned for document-creation language
- [ ] Document-creating actions registered in Documents section
- [ ] Cross-initiative documents added to ALL relevant files
- [ ] PENDING status clearly marked

### Final Validation
- [ ] All ambiguous items clarified
- [ ] All critical attributions confirmed
- [ ] Summary enables immediate action
- [ ] Cross-initiative dependencies noted
