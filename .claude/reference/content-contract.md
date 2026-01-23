# Content Contract

## Overview

Shannon uses a content overlay system. Content packs provide themes, templates, org data, and best practices that customize Shannon for specific organizations or users.

**Core principle**: Content is OPTIONAL. Shannon works without any content pack.

---

## The Contract

Content goes in `content/`. The filesystem IS the registry.

```
content/
├── themes/
│   ├── pptx/          # Presentation themes (.md files)
│   └── pdf/           # PDF styles (.css files)
├── templates/         # Document templates (.md files)
├── output-styles/     # Writing voice definitions (.md files)
├── org/               # Organization data
│   ├── colleagues.json
│   ├── org-context.md
│   └── name-verification.md
├── best-practices/    # Quality standards that extend core
│   └── quality-standards.md
└── reference/         # Org-specific protocols
    └── output-locations.md
```

**Put files in the right folders. Shannon reads what's there.**

---

## Resolution Order

When Shannon needs content, it checks in order:

1. **CLAUDE.local.md** - Personal preferences (always wins)
2. **content/[type]/** - User's content pack
3. **.claude/defaults/[type]/** - Shannon's built-in fallbacks
4. **Ask user / skip feature** - When nothing found

---

## Content Types

### themes/pptx/ - Presentation Themes

Files: `*.md`

Each theme file should define:
- Color palette (hex values)
- Typography (font stack)
- Design principles
- Slide patterns
- CSS variables (for html2pptx)
- PptxGenJS color values

Example: `content/themes/pptx/autodesk.md`

### themes/pdf/ - PDF Styles

Files: `*.css`

CSS for markdown-to-PDF conversion. Should include:
- Typography (font family, sizes, line height)
- Colors (text, background, accent)
- Code block styling
- Table styling
- Print-specific rules

Example: `content/themes/pdf/autodesk.css`

### templates/ - Document Templates

Files: `*.md`

Markdown templates for common documents:
- PRDs
- Meeting notes
- Pitches
- Decision documents
- Leadership reviews

Templates should have clear placeholders and structure.

Example: `content/templates/prd.md`

### output-styles/ - Writing Voice

Files: `*.md`

Define writing voice and communication style:
- Tone (direct, friendly, formal)
- Structure preferences
- Anti-patterns to avoid
- Example phrases

Example: `content/output-styles/samarvir.md`

### org/ - Organization Data

Files: `colleagues.json`, `org-context.md`, `name-verification.md`

Organization-specific data:
- **colleagues.json**: Org structure for name lookup
- **org-context.md**: How to navigate the org
- **name-verification.md**: Protocol for matching names

### best-practices/ - Quality Extensions

Files: `*.md`

Company-specific standards that EXTEND (not replace) Shannon's core quality framework:
- Additional quality gates
- Naming conventions
- Communication standards
- Review processes

### reference/ - Org-Specific Protocols

Files: `*.md`

Additional protocols for specific organizations:
- Output locations
- Approval workflows
- Documentation standards

---

## When Content Is Missing

Shannon handles missing content gracefully:

| Missing | Behavior |
|---------|----------|
| Brand theme | Use minimal theme, inform user |
| PDF style | Use default.css |
| Templates | Ask user for format preferences |
| Output style | Use professional-pm.md (neutral tone) |
| Org data | Disable name verification, skip org context |
| Best practices | Use core quality gates only |

**Never block. Always inform. Always proceed.**

---

## Adding New Content Types

Content is extensible. To add a new type:

1. Create folder in your content pack (e.g., `content/personas/`)
2. Add files following a consistent format
3. Reference from a skill or CLAUDE.md
4. Shannon discovers automatically

No changes to Shannon core required.

---

## Creating a Content Pack

A content pack is just a folder structure. No manifest required.

```bash
# Create structure
mkdir -p my-content/{themes/pptx,themes/pdf,templates,output-styles,org,best-practices,reference}

# Add your files
cp my-theme.md my-content/themes/pptx/
cp my-style.css my-content/themes/pdf/
cp my-template.md my-content/templates/
# etc.

# Use with Shannon
cp -r my-content/* /path/to/shannon/content/
# Or symlink
ln -s /path/to/my-content /path/to/shannon/content
```

---

## Content Pack Examples

### Generic (for external PMs)

```
content-generic/
├── themes/
│   ├── pptx/
│   │   ├── professional-dark.md
│   │   └── professional-light.md
│   └── pdf/
│       └── professional.css
├── templates/
│   ├── prd.md
│   ├── meeting-notes.md
│   └── pitch.md
└── output-styles/
    └── professional-pm.md
```

### Company-Specific

```
content-acme/
├── themes/
│   ├── pptx/
│   │   └── acme.md
│   └── pdf/
│       └── acme.css
├── templates/
│   └── acme-prd.md
├── output-styles/
│   └── acme-voice.md
├── org/
│   ├── colleagues.json
│   ├── org-context.md
│   └── name-verification.md
└── best-practices/
    └── quality-standards.md
```
