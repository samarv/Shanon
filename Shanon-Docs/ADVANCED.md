# Advanced Shannon Usage

Power user features, content pack management, and customization.

---

## Content Packs

### What Are Content Packs?

Content packs add organization-specific overlays to Shannon:
- Brand themes (presentation colors, PDF styling)
- Document templates (PRD format, pitch structure)
- Organization data (colleague names, org structure)
- Output styles (writing voice, tone preferences)
- Extended quality standards

Shannon works fully without them. Content packs add 10% polish when you need it.

---

## Installing Content Packs

### Method 1: Clone Existing Pack

```bash
# Clone from your organization
git clone https://github.com/my-org/shannon-content.git input-pack

# Copy to input folder
cp -r input-pack/* input/

# Verify installation
ls input/themes/pptx/    # Should show .md theme files
ls input/templates/      # Should show template files
```

### Method 2: Create Custom Pack

```bash
# Create folders
mkdir -p input/themes/{pptx,pdf}
mkdir -p input/templates
mkdir -p input/org
mkdir -p input/output-styles

# Add your files
cp my-company-theme.md input/themes/pptx/
cp my-prd-template.md input/templates/
cp colleagues.json input/org/
```

---

## Creating Brand Themes

### Presentation Themes (PPTX)

Create `input/themes/pptx/my-brand.md`:

```markdown
---
name: My Company Brand
primary_color: "#0066CC"
secondary_color: "#FF6B35"
accent_color: "#FFB84D"
---

# My Company Presentation Theme

## Brand Guidelines
- Primary: Blue (#0066CC) - titles, key messages
- Secondary: Orange (#FF6B35) - callouts, emphasis
- Accent: Yellow (#FFB84D) - highlights, data points

## Typography
- Headings: Montserrat Bold
- Body: Open Sans Regular
- Code: Fira Mono

## Layout Preferences
- Title slide: Full-bleed image, white text overlay
- Content slides: 60/40 split (content left, visual right)
- Data slides: Large chart, minimal text

## Voice
- Professional but approachable
- Data-driven, evidence-backed
- Action-oriented conclusions
```

Shannon applies these preferences when creating presentations.

### PDF Styles

Create `input/themes/pdf/my-brand.css`:

```css
/* My Company PDF Theme */

:root {
  --primary-color: #0066CC;
  --secondary-color: #FF6B35;
  --text-color: #333333;
  --heading-font: 'Montserrat', sans-serif;
  --body-font: 'Open Sans', sans-serif;
}

h1, h2, h3 {
  color: var(--primary-color);
  font-family: var(--heading-font);
}

body {
  color: var(--text-color);
  font-family: var(--body-font);
}

/* More styles... */
```

---

## Document Templates

### Creating Templates

Templates live in `input/templates/`. Use markdown with placeholder markers.

**Example: PRD Template**

Create `input/templates/prd.md`:

```markdown
# [PRODUCT NAME] - Product Requirements Document

**Owner:** [PM NAME]  
**Status:** [Draft | Review | Approved]  
**Last Updated:** [DATE]

---

## Problem Statement

**Who**: [Target user persona]  
**What**: [The problem they face]  
**Why it matters**: [Business/user impact]

### Success Metrics
- [Metric 1]: [Baseline] → [Target]
- [Metric 2]: [Baseline] → [Target]

---

## Proposed Solution

[High-level solution description]

### Key Features
1. **[Feature 1]**: [Description]
   - User benefit: [Benefit]
   - Success criteria: [Criteria]

2. **[Feature 2]**: [Description]
   - User benefit: [Benefit]
   - Success criteria: [Criteria]

---

## Trade-offs

| Option | Pros | Cons | Recommendation |
|--------|------|------|----------------|
| [Option 1] | [Pros] | [Cons] | [Yes/No + why] |
| [Option 2] | [Pros] | [Cons] | [Yes/No + why] |

**Chosen approach:** [Decision + rationale]

---

## Open Questions

1. [Question 1]?
   - **Owner:** [Name]
   - **Deadline:** [Date]

2. [Question 2]?
   - **Owner:** [Name]
   - **Deadline:** [Date]

---

## Rollout Plan

### Phase 1: [Name] (Week of [Date])
- [Milestone 1]
- [Milestone 2]

### Phase 2: [Name] (Week of [Date])
- [Milestone 3]
- [Milestone 4]
```

Shannon uses this template automatically when you request a PRD.

---

## Organization Data

### Colleague Name Verification

Create `input/org/colleagues.json`:

```json
{
  "colleagues": [
    {
      "name": "Sarah Chen",
      "role": "CEO",
      "team": "Executive",
      "aliases": ["Sarah", "SC"],
      "email": "sarah@company.com"
    },
    {
      "name": "Mike Johnson",
      "role": "CTO",
      "team": "Engineering",
      "aliases": ["Mike", "MJ"],
      "email": "mike@company.com"
    }
  ]
}
```

Shannon uses this for:
- Name verification (catches typos)
- Auto-completing titles/roles
- Understanding org relationships

### Organization Context

Create `input/org/org-context.md`:

```markdown
# Organization Context

## Company Structure
- **CEO:** Sarah Chen
- **CTO:** Mike Johnson (Engineering)
- **CPO:** You report here (Product)
- **CMO:** Lisa Park (Marketing)

## Product Teams
- **Growth Platform** (your team): 2 PMs, 8 engineers, 2 designers
- **Core Platform**: 3 PMs, 12 engineers, 3 designers
- **Enterprise**: 2 PMs, 6 engineers, 1 designer

## Key Initiatives
- **Q1 Focus:** PLG funnel optimization
- **Q2 Target:** Enterprise feature parity
- **Annual Goal:** 100% YoY revenue growth
```

---

## Writing Voice Customization

### Output Styles

Create `input/output-styles/my-voice.md`:

```markdown
---
name: My Professional Voice
applies_to: [emails, documents, presentations]
---

# My Writing Voice

## Principles
- **Direct**: Get to the point quickly
- **Data-driven**: Back claims with evidence
- **Action-oriented**: Always include clear next steps
- **Collaborative**: Frame as "we" not "I"

## Email Style
- Subject lines: [Action] Topic (max 6 words)
- Opening: State purpose in first sentence
- Body: Use bullets, not paragraphs
- Close: Single clear ask + deadline

## Document Style
- Start with TL;DR or Executive Summary
- Use framework-driven structure
- Callout boxes for key decisions
- Always include "What's next" section

## Avoid
- Jargon without definition
- Passive voice
- Burying the ask
- Walls of text
```

Shannon applies this voice automatically to outputs.

---

## Extended Quality Standards

### Custom Quality Gates

Create `input/best-practices/quality-standards.md`:

```markdown
# Company Quality Standards

These extend Shannon's core quality gates.

## Additional Gates

### Gate 5: Legal Review
- [ ] Does this expose company strategy publicly?
- [ ] Are competitor names mentioned appropriately?
- [ ] Is customer data properly anonymized?

### Gate 6: Brand Alignment
- [ ] Does tone match company voice?
- [ ] Are visual elements on-brand?
- [ ] Is messaging consistent with positioning?

## Specific Standards

### PRDs Must Include
- Accessibility considerations
- Security implications
- Privacy impact assessment
- API design if applicable

### Emails Must Include
- Response deadline if action required
- Meeting link if scheduling
- Brief context for forwarded recipients
```

Shannon applies these ON TOP OF the core 5 gates.

---

## Custom Skills

### Creating a Custom Skill

1. Create folder:
```bash
mkdir -p .claude/skills/my-custom-skill
```

2. Create `SKILL.md`:

```markdown
---
name: my-custom-skill
description: Activate when user requests [specific task]. This skill helps with [purpose].
---

# My Custom Skill

Brief description of what this skill does and when to use it.

## Framework

[Explain the methodology or framework]

### Core Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]

## Application Protocol

### Step 1: [Step Name]
[What to do]

### Step 2: [Step Name]
[What to do]

### Step 3: [Step Name]
[What to do]

## Examples

### Example 1: [Scenario]
**Context:** [Situation]
**Input:** [What user provided]
**Application:** [How skill was applied]
**Output:** [Result]

## Anti-Patterns

| Anti-Pattern | Why It Fails | Instead |
|--------------|--------------|---------|
| [Pattern 1] | [Reason] | [Better approach] |

## Quality Check

Before delivering output, verify:
- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]
```

3. Shannon discovers it automatically on next use.

See `.claude/reference/structure-manifest.md` for full specification.

---

## Brain Management

### Creating Brains

```bash
# Create Brain folder
mkdir -p Brains/my-feature

# Shannon will offer to create CLAUDE.md
# Or create manually from template
```

### Brain Context Template

Create `Brains/my-feature/CLAUDE.md`:

```markdown
# [Feature Name] Brain

**Status:** [Discovery | Planning | Building | Launched]  
**Owner:** [Your name]  
**Timeline:** [Start] - [Target completion]

---

## Objective

[One-sentence goal]

**Success Metrics:**
- [Metric 1]: [Target]
- [Metric 2]: [Target]

---

## Key Decisions & Rationale

### [Date]: [Decision Title]
**Decision:** [What was decided]  
**Rationale:** [Why this decision]  
**Trade-offs:** [What we're giving up]  
**Impact:** [What changes]

---

## Documents Created

- [Date]: [prd.md](prd.md) - Product requirements
- [Date]: [pitch.md](pitch.md) - Leadership pitch

---

## Current Blockers

1. [Blocker 1]
   - **Impact:** [What's blocked]
   - **Owner:** [Who's resolving]
   - **Deadline:** [When]

---

## Open Questions

1. [Question 1]?
   - **Status:** [Open | Resolved]
   - **Owner:** [Name]
```

Shannon auto-updates this as you work in the Brain.

---

## Advanced Workflows

### Multi-Brain Projects

For complex work spanning multiple Brains:

```bash
Brains/
├── parent-project/
│   ├── CLAUDE.md              # Overview context
│   ├── sub-brain-1/           # Nested Brain
│   │   └── CLAUDE.md
│   └── sub-brain-2/
│       └── CLAUDE.md
```

Shannon tracks context hierarchically.

### Team Collaboration

**Setup for team use:**

1. Create shared content pack:
```bash
# In separate repo: shannon-content
git init shannon-content
cd shannon-content
mkdir -p themes/{pptx,pdf} templates org
# Add team content
git commit -m "Initial content pack"
```

2. Team members install:
```bash
# In their Shannon workspace
git clone [team-content-repo] input-pack
cp -r input-pack/* input/
```

3. Each member has own `CLAUDE.local.md` (gitignored)

4. Brains can be shared or private

### Content Pack Versioning

```bash
# In content pack repo
git tag v1.0.0
git push --tags

# Team members update
cd input-pack
git pull
git checkout v1.0.0
cp -r * ../input/
```

---

## Troubleshooting

### "Content not being used"

Check resolution order:
1. Is content in correct path?
2. Check file naming matches convention
3. Verify CLAUDE.local.md doesn't override
4. Check for typos in filenames

### "Skill not activating"

- Make skill description more specific
- Use keywords from description in request
- Check SKILL.md has valid YAML frontmatter
- Explicitly mention skill: "Use [skill name] to..."

### "Templates not applying"

- Verify template in `input/templates/`
- Check filename matches document type
- Ensure markdown formatting is valid
- Shannon will inform if template missing

---

## Performance Optimization

### Large Content Packs

For organizations with many templates/themes:

```bash
input/
├── themes/
│   ├── pptx/
│   │   ├── default.md          # Primary theme
│   │   ├── executive.md        # For exec audiences
│   │   └── technical.md        # For engineering
│   └── pdf/
│       └── default.css         # Single style
```

Shannon loads only what's needed for current request.

### Brain Cleanup

Archive completed Brains:

```bash
mkdir -p Brains/archive
mv Brains/completed-feature Brains/archive/
```

Shannon won't scan archived Brains unless you work in them.

---

## Security Best Practices

### Sensitive Data

**DO:**
- Use `.gitignore` for PII-containing files
- Keep `input/org/` private
- Use environment-specific content packs
- Review content pack before installing

**DON'T:**
- Commit `CLAUDE.local.md`
- Include actual customer data in examples
- Share API keys in templates
- Commit production credentials

### Content Pack Review

Before installing team content pack:

```bash
# Clone to temp location first
git clone [input-pack] /tmp/review-content
cd /tmp/review-content

# Review files
ls -R
cat templates/prd.md
cat org/colleagues.json

# Install if safe
cp -r * ~/shannon-workspace/input/
```

---

## Further Resources

- [ARCHITECTURE.md](ARCHITECTURE.md) - Technical deep-dive
- [CONTRIBUTING.md](CONTRIBUTING.md) - Create and contribute skills
- [EXAMPLES.md](EXAMPLES.md) - Extended use cases
- `.claude/reference/content-contract.md` - Content system details
