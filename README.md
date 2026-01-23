# Shannon

A modular PM system for AI-assisted product management.

## Overview

Shannon provides:
- **Skills**: Capabilities like presentation creation, email drafting, meeting summarization
- **Agents**: Specialized assistants for specific tasks
- **Methodology**: Shreyas Doshi PM philosophy, quality gates, analytical reasoning
- **Content System**: Optional themes, templates, and org context overlays

Shannon works standalone. Content packs enhance it with organization-specific context.

## Quick Start

### 1. Clone Shannon

```bash
git clone https://github.com/[you]/shannon.git my-workspace
cd my-workspace
```

### 2. Create Your Personal Context

```bash
cp .claude/CLAUDE.local.example.md .claude/CLAUDE.local.md
# Edit with your info
```

Or let Shannon guide you through setup on first conversation.

### 3. (Optional) Add Content Pack

```bash
# Clone a content pack
git clone https://github.com/[org]/content-[name].git content-pack
cp -r content-pack/* content/
```

### 4. Start Using

Open in Cursor or your Claude-enabled IDE. Shannon is ready.

## Structure

```
shannon/
├── .claude/
│   ├── CLAUDE.md                 # Core methodology
│   ├── CLAUDE.local.example.md   # Personal context template
│   ├── skills/                   # All capabilities
│   ├── agents/                   # Specialized assistants
│   ├── reference/                # Core protocols
│   ├── output-styles/            # Default voice
│   └── defaults/                 # Fallback content
├── content/                      # Your content (themes, templates, org data)
├── Initiatives/                  # Your initiatives
└── Templates/                    # Points to content/templates/
```

## How It Works

### Methodology (Always Active)

Shannon includes complete PM methodology:
- Shreyas Doshi philosophy (first principles, trade-offs, outcomes)
- Quality gates (5 core checks before any output)
- Analytical reasoning framework
- Eigenquestion context gathering
- Initiative auto-update protocol

### Content (Optional Enhancement)

Content packs provide organization-specific context:
- **Themes**: Brand colors for presentations and PDFs
- **Templates**: Document formats (PRDs, pitches, meeting notes)
- **Org Data**: Colleague names, org structure, navigation
- **Best Practices**: Quality standards that extend core gates
- **Output Styles**: Writing voice definitions

If content is missing, Shannon uses built-in defaults and informs you.

### Personal Layer (Your Context)

`CLAUDE.local.md` contains your personal context:
- Name, role, team, manager
- Product focus and key dates
- Communication preferences
- Stakeholder quick reference

This file is gitignored for privacy.

## Content System

### Resolution Order

1. `CLAUDE.local.md` (always wins)
2. `content/[type]/` (your content pack)
3. `.claude/defaults/[type]/` (built-in)
4. Ask user / skip feature

### Adding Content

```bash
# Add a presentation theme
cp my-theme.md content/themes/pptx/

# Add a PDF style
cp my-style.css content/themes/pdf/

# Add a template
cp my-template.md content/templates/

# Add org data
cp colleagues.json content/org/
```

See `.claude/reference/content-contract.md` for full documentation.

## Skills

Shannon includes skills for:
- Presentation creation and editing (pptx)
- Document generation (docx, pdf)
- Email drafting (CRAFT method)
- Meeting summarization
- Strategic analysis
- Pitch creation (Shape Up)
- TODO prioritization (LNO framework)
- And more...

Skills auto-activate when your request matches their description.

## Agents

Specialized assistants for specific tasks:
- `meeting-summarizer`: Transcript processing
- `exec-reviewer`: Strategic alignment review
- `ux-reviewer`: User experience feedback
- `pdf-builder`: Markdown to PDF conversion
- And more...

## Creating Content Packs

A content pack is just folders with files:

```
my-content-pack/
├── themes/
│   ├── pptx/
│   │   └── my-brand.md
│   └── pdf/
│       └── my-brand.css
├── templates/
│   └── prd.md
├── output-styles/
│   └── my-voice.md
└── org/
    └── colleagues.json
```

No manifest required. No configuration. Just files in folders.

## License

[Your license here]
