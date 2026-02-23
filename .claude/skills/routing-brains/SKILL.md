---
name: routing-brains
description: |
  PROACTIVELY used for routing meeting items to Brain CLAUDE.md files.
  Discovers Brains dynamically, matches items by confidence, handles unmatched content.
  Works with analyzing-meetings and summarizing-meetings skills.
---

# Routing Brains Skill

## Purpose

Route meeting items to appropriate Brain CLAUDE.md files:
1. **Discover Brains** dynamically from Brains/ folder
2. **Match items** using keyword and semantic scoring
3. **Handle unmatched** content with user prompts (one at a time)

For product-specific context, see `CLAUDE.local.md`.

---

## Brain Discovery Protocol

### Step 1: Scan Brains Folder

**CRITICAL: Never hardcode Brain names. Always discover dynamically.**

```
1. List all subdirectories in /Brains/
2. For each subdirectory:
   a. Check if CLAUDE.md exists
   b. If yes, read and parse the file
   c. Extract keywords and context for matching
3. Build Brain registry with:
   - Brain name (folder name)
   - Core objective (from CLAUDE.md)
   - Key terms (extracted from all sections)
   - Status (Active/Paused/Completed)
```

### Step 2: Extract Keywords

From each Brain's CLAUDE.md, extract:

| Section | What to Extract |
|---------|-----------------|
| **Core Objective** | Main nouns, verbs, product names |
| **Key Decisions** | Decision topics, technical terms |
| **Documents** | Document names, feature names |
| **Stakeholders** | Team names, product areas |
| **Open Questions** | Problem domains, blockers |

### Step 3: Build Matching Index

```
Brain: "[Brain-name]"
Keywords: [relevant terms extracted]
Core Theme: "[one-line description]"
Status: Active
```

---

## Matching Framework

### Confidence Levels

| Level | Threshold | Action |
|-------|-----------|--------|
| **High** | >= 0.8 | Auto-route to Brain |
| **Medium** | 0.6 - 0.8 | Route with [Review] flag |
| **Low** | 0.4 - 0.6 | Flag as potential, ask user |
| **None** | < 0.4 | Mark as unmatched |

### Matching Algorithm

For each meeting item:

1. **Keyword Match Score** (0-0.5):
   - Count keyword overlaps with Brain keywords
   - Weight Core Objective keywords 2x
   - Normalize by total keywords

2. **Semantic Match Score** (0-0.5):
   - Compare item theme to Brain Core Objective
   - Consider context (what problem is being solved?)
   - Factor in stakeholder mentions

3. **Combined Score**: Keyword + Semantic

### Multi-Brain Matching

Items CAN match multiple Brains if:
- Score >= threshold for multiple Brains
- Item explicitly mentions multiple workstreams
- Action item affects multiple teams

---

## Item Segmentation

Extract discrete items from meeting content:

| Item Type | How to Identify |
|-----------|-----------------|
| **Decision** | "We decided...", "Let's go with...", "The approach is..." |
| **Action Item** | "I'll...", "Can you...", "[Name] will...", "TODO:" |
| **Discussion Point** | Topic shifts, extended back-and-forth |
| **Blocker** | "We can't proceed...", "Waiting on...", "Blocked by..." |
| **Open Question** | "We need to figure out...", "TBD:", "?" |
| **Status Update** | "Update on...", "Progress:", metrics discussion |

---

## Routing Protocol

### Step 1: Match Each Item

```
For each item:
  1. Run matching algorithm
  2. If High confidence (>= 0.8) → Route to Brain
  3. If Medium confidence (0.6-0.8) → Route with [Review] flag
  4. If Low confidence (0.4-0.6) → Add to potential matches
  5. If No match (< 0.4) → Add to unmatched list
```

### Step 2: Handle Multi-Brain Items

If item matches multiple Brains:
1. Route to ALL matching Brains
2. Note cross-Brain dependency
3. Flag in both Brain summaries

---

## Unmatched Content Handling

### Sequential Questioning Protocol

**CRITICAL: Ask ONE question at a time. Do not overwhelm the user.**

**Step 1: Announce count**
```
I found [N] items that don't clearly match any existing Brain.
Let me walk through each one with you.
```

**Step 2: Present FIRST item only**
```
**Item 1 of [N]**: [Brief summary]

**Type**: [Decision/Action/Discussion/Blocker/Question]
**Content**: [Full item - 1-2 sentences]
**Context**: [Why this came up]
**Potential match**: [Brain] (low confidence) OR "No matching Brain"

What would you like to do?
a) Assign to [Brain 1]
b) Assign to [Brain 2]
c) Create a new Brain
d) Leave in temp folder
e) Discard (not relevant)
```

**Step 3: Wait for response before continuing**

**Step 4: Proceed to next item**
```
Got it - [acknowledge choice].
**Item 2 of [N]**: [Next summary]...
```

### New Brain Creation (Guided)

If user chooses to create new Brain:

**Step 1**: "What should this Brain be called? (Suggested: '[name]')"
→ Wait for response

**Step 2**: "In one sentence, what's the core objective?"
→ Wait for response

**Step 3**: Create folder, generate CLAUDE.md, route item, confirm

---

## Example Input

```
Items to route:
1. Decision: "Use React for dashboard migration"
2. Action: "Update API documentation before launch"
3. Discussion: "Potential partnership with external vendor"
```

## Example Output

```markdown
## Routing Results

### High Confidence Routes
- **Decision: React migration** → frontend-modernization (0.92)

### Medium Confidence Routes  
- **Action: API documentation** → api-platform (0.71) [Review]

### Unmatched Items
1 item requires user input:

**Item 1 of 1**: Partnership discussion
**Type**: Discussion Point
**Content**: Potential collaboration with external vendor
**Potential match**: No matching Brain

What would you like to do?
a) Assign to frontend-modernization
b) Assign to api-platform
c) Create a new Brain
d) Leave in temp folder
e) Discard
```

---

## Quality Gates

- [ ] Brains discovered dynamically (not hardcoded)
- [ ] Each item categorized by type
- [ ] Matching algorithm applied consistently
- [ ] Multi-Brain items flagged
- [ ] Confidence levels logged
- [ ] Unmatched items presented one at a time

---

## Anti-Patterns

- ❌ Hardcoding Brain names
- ❌ Force-matching items to Brains
- ❌ Auto-routing low-confidence matches
- ❌ Presenting all unmatched items at once
- ❌ Proceeding before user responds
- ✅ Always scan Brains/ folder fresh
- ✅ Ask ONE question at a time
- ✅ Wait for explicit confirmation

---

## Success Criteria

1. All Brains discovered dynamically
2. Items routed with appropriate confidence
3. Multi-Brain dependencies flagged
4. Unmatched items handled with user input
5. Ready for summarizing-meetings skill
