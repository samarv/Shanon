# Shannon Architecture

Technical deep-dive into Shannon's structure and design principles.

---

## System Overview

Shannon is a file-based AI system for product management. It combines:
1. AI assistant (Claude via Cursor)
2. Methodology files (markdown-based skills and protocols)
3. Context layering (personal, organizational, initiative-specific)
4. Zero-configuration discovery (filesystem is the registry)

---

## Directory Structure

### Complete Structure

```
shannon/
├── .claude/                          # Core Shannon system
│   ├── CLAUDE.md                     # System instructions & methodology
│   ├── CLAUDE.local.example.md       # Template for personal context
│   ├── CLAUDE.local.md               # Your context (gitignored)
│   │
│   ├── skills/                       # 350+ PM frameworks
│   │   ├── email-drafter/            # CRAFT method email drafting
│   │   │   ├── SKILL.md              # Skill definition & methodology
│   │   │   └── references/           # Examples and documentation
│   │   ├── pptx/                     # Presentation creation
│   │   ├── prioritizing-todos/       # LNO framework
│   │   ├── eigenquestion-context/    # High-leverage questioning
│   │   ├── first-mile-experience-design/
│   │   ├── comprehension-first-design/
│   │   └── ... 345 more skills
│   │
│   ├── agents/                       # Specialized assistants
│   │   ├── meeting-summarizer.md     # Meeting transcript analysis
│   │   ├── exec-reviewer.md          # Strategic alignment review
│   │   ├── ux-reviewer.md            # User experience feedback
│   │   ├── pdf-builder.md            # Markdown to PDF conversion
│   │   └── ... 5 more agents
│   │
│   ├── reference/                    # Core protocols
│   │   ├── quality-framework.md      # 5 validation gates
│   │   ├── uncertainty-protocol.md   # When to ask questions
│   │   ├── initiative-auto-update.md # Initiative context tracking
│   │   ├── meeting-protocols.md      # Meeting analysis rules
│   │   ├── content-contract.md       # Content system documentation
│   │   └── structure-manifest.md     # System structure documentation
│   │
│   ├── output-styles/                # Writing voice definitions
│   │   └── samarvir.md               # Example output style
│   │
│   └── defaults/                     # Built-in fallbacks
│       ├── themes/
│       │   ├── pptx/                 # Default presentation themes
│       │   │   └── minimal.md
│       │   └── pdf/                  # Default PDF styles
│       │       └── default.css
│       └── templates/                # Default document templates
│           └── meeting-notes.md
│
├── content/                          # Your content layer (optional)
│   ├── themes/                       # Brand themes for outputs
│   │   ├── pptx/                     # Presentation themes (.md)
│   │   └── pdf/                      # PDF styles (.css)
│   ├── templates/                    # Organization templates (.md)
│   ├── org/                          # Colleague data, org context
│   │   ├── colleagues.json           # Name verification data
│   │   └── org-context.md            # Organization structure
│   ├── output-styles/                # Writing voice definitions
│   ├── best-practices/               # Extended quality standards
│   └── reference/                    # Additional protocols
│
├── Initiatives/                      # Your product initiatives
│   └── [initiative-name]/
│       ├── CLAUDE.md                 # Auto-maintained context
│       ├── prd.md                    # PRD document
│       ├── research/                 # Research artifacts
│       └── ... (any work artifacts)
│
├── Templates/                        # Symlink to content/templates/
├── .gitignore                        # Ignores CLAUDE.local.md
└── README.md                         # This file
```

---

## Core Concepts

### 1. Skills: Auto-Activating Methodologies

**What they are:**  
Skills are markdown files containing PM frameworks and methodologies. Each skill has:
- YAML frontmatter with name and description
- Framework explanation
- Step-by-step application protocol
- Examples and anti-patterns

**How they activate:**  
Shannon reads the skill description and auto-activates when user intent matches. No explicit invocation needed.

**Example skill file structure:**

```markdown
---
name: email-drafter
description: Draft strategic emails using CRAFT method (Catch attention, 
  Reasoning, Ask, Follow-up, Timebox). Use when user requests email drafting.
---

# Email Drafting with CRAFT Method

## Framework
[Methodology explanation]

## Application Protocol
[Step-by-step instructions]

## Examples
[Concrete examples]
```

**Lazy loading:**  
Skills are loaded on-demand, not all at once. This keeps context efficient.

### 2. Quality Gates: 5-Step Validation

Every output passes through 5 gates before delivery:

**Gate 0: Skill Utilization**
- Did I check if a skill exists for this task?
- Am I applying the skill's framework vs. generic response?

**Gate 1: Purpose Validation**
- Why does this matter?
- Who is the audience?
- What are success criteria?

**Gate 2: Content Validation**
- Is customer value articulated?
- Are trade-offs explicit?
- Are assumptions identified?

**Gate 3: Quality Validation**
- Is a systematic framework applied?
- Are claims evidence-based?
- Can stakeholders act on this?

**Gate 4: Shreyas Standard**
- Would Shreyas Doshi approve this thinking?
- Does this demonstrate Principal PM judgment?
- Is this worthy of executive attention?

See `.claude/reference/quality-framework.md` for full details.

### 3. Content Resolution: Layered Override System

Shannon resolves content in priority order:

```
1. CLAUDE.local.md          (highest priority - your preferences)
2. content/[type]/           (content pack overlays)
3. .claude/defaults/[type]/  (built-in fallbacks)
4. Ask user / skip feature   (graceful degradation)
```

**Example: Presentation theme resolution**

User requests: "Create a presentation about Q1 roadmap"

1. Check `CLAUDE.local.md` → any theme preference specified? Use it.
2. Check `content/themes/pptx/` → any .md theme files? Use first match.
3. Check `.claude/defaults/themes/pptx/minimal.md` → use built-in.
4. If nothing exists → ask user or use plaintext.

**No configuration files needed.** The filesystem IS the registry.

### 4. Initiative Context: Auto-Tracking

When working in `Initiatives/[name]/`:

1. Shannon reads `Initiatives/[name]/CLAUDE.md` for context
2. Tracks decisions, documents, status changes during work
3. Updates the `CLAUDE.md` file with significant events
4. Maintains living documentation automatically

**What gets tracked:**
- Key decisions and rationale
- Documents created with links
- Status changes and blockers
- Open questions and resolutions

See `.claude/reference/initiative-auto-update.md` for protocol.

### 5. Agents: Specialized Sub-Assistants

Agents are isolated contexts with specific permissions:

| Agent | Purpose | Permissions | Trigger |
|-------|---------|-------------|---------|
| `meeting-summarizer` | Transcript analysis | Read-only | Meeting content detected |
| `updating-todos` | LNO prioritization | Read + write | User asks about priorities |
| `initiative-tracker` | Context updates | Read + write | Proactive in initiatives |
| `exec-reviewer` | Strategic feedback | Read-only | Request for exec perspective |
| `ux-reviewer` | UX feedback | Read-only | Request for UX perspective |
| `pdf-builder` | PDF generation | Read + write + terminal | PDF creation request |

Agents auto-activate based on trigger phrases in their YAML description.

---

## Design Principles

### 1. Zero Configuration

**Principle:** No manifest files, no config.yaml, no setup scripts.

**Implementation:**
- Skills discovered via filesystem scan
- Content resolved via priority hierarchy
- Templates loaded from conventional paths
- No "registration" step needed

**Trade-off:** Requires consistent file structure conventions.

### 2. Graceful Degradation

**Principle:** System works without optional components.

**Implementation:**
- Missing content pack → use defaults
- Missing templates → ask user or use built-in
- Missing org data → skip features that need it
- Always inform user what's missing, never block

**Example:**  
"Using minimal theme since no brand theme installed. Add to `content/themes/pptx/` to customize."

### 3. Privacy-First

**Principle:** Personal context stays local.

**Implementation:**
- `CLAUDE.local.md` is gitignored
- No telemetry or cloud sync
- All processing happens locally in IDE
- Content packs can be private repos

**Trade-off:** Context doesn't sync across machines (by design).

### 4. Filesystem as Registry

**Principle:** Discovery via conventions, not configuration.

**Implementation:**
- Skills in `.claude/skills/[name]/SKILL.md`
- Templates in `content/templates/[name].md`
- Themes in `content/themes/[type]/[name].[ext]`
- No need to "register" new content

**Benefit:** Add files → Shannon discovers them automatically.

### 5. Lazy Loading

**Principle:** Load only what's needed for current request.

**Implementation:**
- Skills load on-demand via description matching
- Protocols load when specific context triggers them
- Initiative context loads when working in initiative folder
- Never load "just in case"

**Benefit:** Efficient context usage, faster responses.

---

## Technical Details

### Skill Activation Mechanism

1. **User makes request**  
   Example: "Draft an email to my VP about Q1 roadmap"

2. **Shannon scans skill descriptions**  
   Reads YAML frontmatter descriptions of skills in `.claude/skills/`

3. **Intent matching**  
   Matches user intent to skill description semantically

4. **Skill loads**  
   Reads full `SKILL.md` file into context

5. **Framework applied**  
   Follows skill's protocol to generate output

6. **Quality gates validate**  
   Output passes through 5 validation gates

7. **Result delivered**  
   User receives output with framework attribution

### Content Pack Structure

A content pack is a repository with conventional folders:

```
my-company-content-pack/
├── themes/
│   ├── pptx/
│   │   └── company-brand.md       # Presentation theme
│   └── pdf/
│       └── company-style.css      # PDF styling
├── templates/
│   ├── prd.md                     # PRD template
│   ├── pitch.md                   # Pitch template
│   └── meeting-notes.md           # Meeting notes template
├── output-styles/
│   └── company-voice.md           # Writing voice
├── org/
│   ├── colleagues.json            # Name verification
│   └── org-context.md             # Org structure
├── best-practices/
│   └── quality-standards.md       # Extended quality gates
└── README.md                      # Content pack documentation
```

**Installation:**

```bash
git clone https://github.com/my-org/content-pack.git
cp -r content-pack/* content/
```

**No manifest required.** Shannon discovers files via conventions.

### Personal Context Structure

`CLAUDE.local.md` example:

```markdown
# Personal Context

## Profile
- **Name:** Jane Smith
- **Role:** Senior Product Manager
- **Team:** Growth Platform
- **Manager:** John Doe (VP Product)

## Product Context
- **Product:** Acme Analytics Platform
- **Key Terms:** activation, retention, PLG funnel
- **Key Dates:** Q1 planning (Jan 15), board meeting (Feb 1)

## Communication Preferences
- **Stakeholder updates:** Use CRAFT method, concentric circles
- **Technical discussions:** Direct and data-driven
- **Team communication:** Collaborative, ask for input

## Stakeholder Quick Reference
- **Sarah Chen (CEO):** Cares about revenue impact, board narrative
- **Mike Johnson (CTO):** Needs technical feasibility, resourcing
- **Lisa Park (Design):** Values user research, wants early involvement
```

This context gets used in every Shannon response automatically.

---

## Extension Points

### Adding Custom Skills

1. Create folder: `.claude/skills/my-custom-skill/`
2. Create `SKILL.md` with YAML frontmatter:

```markdown
---
name: my-custom-skill
description: When to activate this skill and what it does.
---

# My Custom Skill

[Your methodology here]
```

3. Shannon discovers it automatically
4. Activates when description matches user intent

See `.claude/reference/structure-manifest.md` for detailed spec.

### Adding Custom Content Types

Content is extensible beyond built-in types:

1. Create folder: `content/my-custom-type/`
2. Add files: `content/my-custom-type/my-file.md`
3. Reference from skill or protocol
4. Shannon discovers it automatically

**Example:**  
Add `content/personas/` for user persona definitions. Reference from skills that need persona context.

---

## Performance Characteristics

**Skill activation:** < 1 second (description scan + load)  
**Context resolution:** Instant (filesystem lookup)  
**Quality gates:** Negligible (framework application)  
**Initiative updates:** < 2 seconds (file write)

**Context efficiency:**  
- Lazy loading keeps token usage minimal
- Only active skill loaded, not all 350
- Protocol loading on-demand
- Personal context always loaded (small file)

---

## Security & Privacy

**Local-first:**
- All processing in local IDE
- No cloud services required
- No telemetry or tracking

**Gitignore configuration:**
- `CLAUDE.local.md` never committed
- `content/org/` typically gitignored (contains PII)
- Initiative folders can be private repos

**Content pack security:**
- Content packs are just files
- Review before installing (like any git repo)
- Can use private repos for sensitive content

---

## Troubleshooting

**"Skill not activating"**
- Check skill description matches your intent
- Try more specific request language
- Explicitly mention framework: "Use CRAFT method to draft email"

**"Content not found"**
- Check file is in correct path (e.g., `content/themes/pptx/`)
- Check filename extension matches convention
- Shannon will inform you what's missing

**"Quality gates failing"**
- Review `.claude/reference/quality-framework.md`
- Check if output answers "Why does this matter?"
- Verify trade-offs are explicit
- Ensure success metrics are quantified

---

## Further Reading

- `.claude/CLAUDE.md` - Full system instructions
- `.claude/reference/content-contract.md` - Content system details
- `.claude/reference/structure-manifest.md` - Skill structure spec
- `.claude/reference/quality-framework.md` - Quality gates explained
- `CONTRIBUTING.md` - How to create skills and contribute