# Contributing to Shannon

Help improve Shannon by contributing skills, protocols, or documentation.

---

## Ways to Contribute

1. **Create new skills** - Add PM frameworks and methodologies
2. **Improve existing skills** - Enhance documentation, add examples
3. **Report issues** - Found a bug or have a suggestion?
4. **Share content packs** - Create and share organization-specific overlays
5. **Improve documentation** - Fix typos, clarify concepts, add examples

---

## Creating Skills

### Skill Structure

Every skill follows this structure:

```
.claude/skills/my-skill-name/
├── SKILL.md              # Main skill file (required)
├── references/           # Optional supporting docs
│   ├── examples.md       # Extended examples
│   ├── research.md       # Framework sources
│   └── case-studies.md   # Real-world applications
└── assets/               # Optional images, diagrams
```

### SKILL.md Template

```markdown
---
name: my-skill-name
description: |
  One sentence explaining when this skill activates and what it does.
  Be specific about trigger conditions. Shannon uses this for auto-activation.
---

# Skill Title

Brief introduction (2-3 sentences) explaining what this skill does and 
when to use it.

## Core Concept

Explain the fundamental principle or framework. What's the "big idea"?

### Key Principles

1. **Principle 1:** [Explanation]
2. **Principle 2:** [Explanation]
3. **Principle 3:** [Explanation]

## When to Use This Skill

**Use when:**
- [Situation 1]
- [Situation 2]
- [Situation 3]

**Don't use when:**
- [Situation A]
- [Situation B]

## Framework Application

### Step 1: [Step Name]

[What to do in this step]

**Example:**
- [Example showing this step]

### Step 2: [Step Name]

[What to do in this step]

**Example:**
- [Example showing this step]

### Step 3: [Step Name]

[What to do in this step]

**Example:**
- [Example showing this step]

## Examples

### Example 1: [Scenario Name]

**Context:** [Describe the situation]

**Input:** [What the user provided]

**Application:** [How the framework was applied step-by-step]

**Output:** [The result]

**Why it worked:** [Explanation]

### Example 2: [Scenario Name]

[Same structure as Example 1]

## Anti-Patterns

Common mistakes when applying this framework:

| Anti-Pattern | Why It Fails | Instead |
|--------------|--------------|---------|
| [Pattern 1] | [Reason] | [Better approach] |
| [Pattern 2] | [Reason] | [Better approach] |

## Quality Check

Before delivering output, verify:

- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]

## References

- **Source:** [Original framework creator]
- **Further reading:** [Links to resources]
- **Related skills:** [Other Shannon skills to consider]
```

### Writing Good Skill Descriptions

The description in YAML frontmatter determines when skills activate.

**Good descriptions:**

```yaml
description: |
  Draft strategic emails using CRAFT method. Activate when user 
  requests email drafting, stakeholder communication, or executive updates.
```

**Why it works:**
- Specific trigger words: "email drafting", "stakeholder communication"
- Framework named: "CRAFT method"
- Clear purpose: "strategic emails"

**Bad descriptions:**

```yaml
description: Help with emails
```

**Why it fails:**
- Too vague
- No framework mentioned
- Unclear when to activate

### Skill Naming Conventions

- Use kebab-case: `my-skill-name`
- Be descriptive: `first-mile-experience-design` not `fmed`
- Match folder name to skill name
- Include framework origin if applicable: `craft-email-method`

---

## Submitting Skills

### 1. Fork the Repository

```bash
git clone https://github.com/[you]/shannon.git
cd shannon
git checkout -b add-my-skill-name
```

### 2. Create Your Skill

```bash
mkdir -p .claude/skills/my-skill-name/references
touch .claude/skills/my-skill-name/SKILL.md
```

Fill in the SKILL.md template above.

### 3. Test Your Skill

```bash
# Open Shannon in Cursor
cursor .

# Test skill activation
# Make a request that should trigger your skill
# Verify it activates and produces good output
```

### 4. Submit Pull Request

```bash
git add .claude/skills/my-skill-name/
git commit -m "Add [Framework Name] skill for [use case]"
git push origin add-my-skill-name
```

Create PR with:
- **Title:** "Add [Skill Name] skill"
- **Description:** 
  - What framework does this implement?
  - Who created the original framework?
  - When should this skill activate?
  - Example use case

---

## Improving Existing Skills

Found a typo? Want to add examples? Have a better explanation?

### Small Fixes (typos, formatting)

1. Edit the file directly
2. Submit PR with descriptive commit message
3. No issue needed for minor fixes

### Substantial Changes (framework modifications)

1. Open issue first describing the change
2. Discuss with maintainers
3. Submit PR after consensus
4. Include rationale in PR description

---

## Content Pack Guidelines

Sharing organization-specific content? Follow these practices:

### Content Pack Structure

```
my-org-content-pack/
├── README.md             # Installation instructions
├── themes/
│   ├── pptx/
│   │   └── company-brand.md
│   └── pdf/
│       └── company-style.css
├── templates/
│   ├── prd.md
│   ├── pitch.md
│   └── meeting-notes.md
├── org/
│   └── .gitkeep          # Don't commit PII
├── output-styles/
│   └── company-voice.md
└── best-practices/
    └── quality-standards.md
```

### Content Pack README Template

```markdown
# [Company Name] Shannon Content Pack

Official content pack for [Company Name].

## Installation

\```bash
git clone [this-repo] shannon-content
cp -r shannon-content/* [your-shannon]/input/
\```

## What's Included

- **Presentation theme:** [Company] brand colors and layouts
- **Templates:** PRD, pitch deck, meeting notes in [Company] format
- **Writing voice:** [Company] tone and style guidelines
- **Quality standards:** [Company]-specific quality gates

## Maintenance

Contact: [Team/Person responsible]
Last updated: [Date]
```

### Privacy in Content Packs

**DO commit:**
- Theme files (colors, layouts)
- Template structures
- Writing voice guidelines
- Quality standards

**DON'T commit:**
- `org/colleagues.json` (contains PII)
- Actual customer names
- Internal metrics/data
- Confidential information

Use `.gitignore`:

```
org/colleagues.json
org/*-internal.md
```

---

## Documentation Improvements

### README, ARCHITECTURE, EXAMPLES

To improve main documentation:

1. Identify what's unclear or missing
2. Submit issue with:
   - What you were trying to understand
   - What was confusing
   - What would have helped
3. Or submit PR directly with improvements

### Skill Documentation

Each skill can have extended documentation in `references/`:

```
.claude/skills/my-skill/
├── SKILL.md
└── references/
    ├── examples.md       # Extended examples
    ├── research.md       # Framework origins
    └── case-studies.md   # Real-world usage
```

---

## Reporting Issues

### Bug Reports

Use this template:

```markdown
**Description:**
[What's wrong?]

**Expected behavior:**
[What should happen?]

**Actual behavior:**
[What actually happens?]

**Reproduction steps:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Context:**
- Shannon version: [commit hash or date]
- IDE: [Cursor / other]
- Skill involved: [if applicable]

**Screenshots:**
[If helpful]
```

### Feature Requests

Use this template:

```markdown
**Feature:**
[What do you want?]

**Use case:**
[When would you use this?]

**Current workaround:**
[How do you do this today?]

**Proposed solution:**
[Your idea for how it could work]

**Related frameworks:**
[Any PM methodologies this relates to?]
```

---

## Code of Conduct

### Be Respectful

- Respect different PM perspectives and methodologies
- No framework wars ("My framework is better than yours")
- Constructive feedback only
- Remember: we're all trying to improve PM practice

### Be Collaborative

- Help others understand frameworks
- Share your learnings
- Give credit to original framework creators
- Build on each other's work

### Be Practical

- Focus on what works, not what's "pure"
- Real-world examples over theoretical perfection
- Admit when frameworks don't apply
- Iterate based on feedback

---

## Recognition

Contributors are recognized in:
- Skill credit: "Contributed by [Name]"
- CHANGELOG entries
- Release notes
- Community showcase

Top contributors may be invited to:
- Maintain specific skill areas
- Review skill submissions
- Shape Shannon's direction

---

## Questions?

- **Skill design questions:** Open a discussion issue
- **Technical questions:** See ARCHITECTURE.md
- **Usage questions:** See EXAMPLES.md
- **General questions:** Open an issue with "Question" label

---

## License

By contributing to Shannon, you agree that your contributions will be 
licensed under the same MIT License as the project.

All skills should credit original framework creators and link to 
source materials where applicable.

---
Test
**Thank you for helping elevate PM practice for everyone!**
