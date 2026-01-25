# Configuration Reference

Complete reference for all subagent frontmatter fields with examples and best practices.

## Required Fields

### name

Unique identifier for the subagent.

**Format**: Lowercase letters, digits, and hyphens only  
**Length**: Max 40 characters  
**Rules**: Cannot start/end with hyphen, no consecutive hyphens

**Examples:**
```yaml
name: code-reviewer
name: data-analyzer
name: api-tester
```

**Invalid:**
```yaml
name: Code-Reviewer  # No uppercase
name: code_reviewer  # No underscores
name: -code-reviewer # Cannot start with hyphen
```

### description

Explains what the subagent does and when Claude should delegate to it. This is the **primary triggering mechanism** for subagent delegation.

**Best practices:**
- Include what the subagent does
- Specify when to use it (scenarios, triggers)
- Use action words ("Use when...", "Use immediately after...")
- Include "use proactively" to encourage automatic delegation
- Be specific about task types or file types

**Examples:**

```yaml
# Good: Specific with clear triggers
description: Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code.

# Good: Domain-specific with scenarios
description: Execute read-only database queries. Use when analyzing data, generating reports, or investigating database contents. Only SELECT queries allowed.

# Good: Task-specific with context
description: Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues or when tests fail.

# Bad: Too vague
description: Helps with code

# Bad: No triggers
description: A code reviewer that looks at code quality
```

## Optional Fields

### tools

Specifies which tools the subagent can use. If omitted, inherits all tools from parent conversation.

**Format**: Comma-separated string or list

**Available tools:**
- `Read` - Read files
- `Write` - Create/overwrite files
- `Edit` - Modify existing files
- `Grep` - Search file contents
- `Glob` - Find files by pattern
- `Bash` - Execute shell commands
- `Task` - Delegate to other subagents
- `AskUserQuestion` - Ask clarifying questions
- `ListDir` - List directory contents
- `FileSearch` - Search for files
- `CodebaseSearch` - Semantic code search

**Examples:**

```yaml
# Read-only subagent
tools: Read, Grep, Glob

# Can analyze and execute
tools: Read, Grep, Glob, Bash

# Can modify files
tools: Read, Write, Edit, Grep, Glob

# Inherit all tools (omit field)
# (no tools field)
```

**Common patterns:**

```yaml
# Code reviewer (read-only)
tools: Read, Grep, Glob, Bash

# Debugger (can modify)
tools: Read, Edit, Bash, Grep, Glob

# Database reader (bash only for queries)
tools: Bash

# Research agent (read and search)
tools: Read, Grep, Glob, CodebaseSearch, ListDir
```

### disallowedTools

Denies specific tools from the inherited set. Use when you want most tools but need to block specific ones.

**Format**: Comma-separated string or list

**Examples:**

```yaml
# Inherit all except write operations
disallowedTools: Write, Edit

# Inherit all except dangerous operations
disallowedTools: Bash, Write

# Block delegation and write
disallowedTools: Task, Write
```

**When to use:**
- Use `tools` when you want to allow specific tools (allowlist)
- Use `disallowedTools` when you want to block specific tools (denylist)
- Don't use both together (confusing)

### model

Specifies which AI model the subagent uses.

**Options:**
- `haiku` - Fast, cheap, good for simple tasks
- `sonnet` - Balanced capability and speed (default choice)
- `opus` - Most capable, slower, expensive
- `inherit` - Use same model as parent conversation (default if omitted)

**Examples:**

```yaml
# Fast research agent
model: haiku

# Balanced code reviewer
model: sonnet

# Complex reasoning
model: opus

# Match parent (default)
model: inherit
```

**Choosing a model:**
- **haiku**: Simple file searches, basic analysis, quick operations
- **sonnet**: Code review, debugging, moderate complexity
- **opus**: Complex architectural decisions, tricky bugs
- **inherit**: When subagent complexity matches main conversation

### permissionMode

Controls how the subagent handles permission prompts.

**Options:**
- `default` - Standard permission checking with prompts
- `acceptEdits` - Auto-accept file edits
- `dontAsk` - Auto-deny permission prompts (allowed tools still work)
- `bypassPermissions` - Skip all permission checks (use with caution!)
- `plan` - Plan mode (read-only exploration)

**Examples:**

```yaml
# Standard prompts
permissionMode: default

# Auto-accept edits (trusted subagent)
permissionMode: acceptEdits

# Deny everything not explicitly allowed
permissionMode: dontAsk

# Skip all checks (dangerous!)
permissionMode: bypassPermissions
```

**Warning:** `bypassPermissions` skips all permission checks. Use only for fully trusted operations.

### skills

Preloads skill content into the subagent's context at startup. The full skill content is injected, giving the subagent domain knowledge without requiring discovery.

**Format**: List of skill names

**Examples:**

```yaml
# API developer with conventions
skills:
  - api-conventions
  - error-handling-patterns

# Data analyst with domain knowledge
skills:
  - database-schema
  - query-patterns

# Frontend builder with design system
skills:
  - component-library
  - design-tokens
```

**Notes:**
- Subagents don't inherit skills from parent conversation
- Skills must be explicitly listed here
- Full skill content is loaded (uses context)
- Use for domain-specific knowledge the subagent needs

### hooks

Defines lifecycle hooks that run during subagent execution.

**Available events:**
- `PreToolUse` - Before using a tool
- `PostToolUse` - After using a tool
- `Stop` - When subagent finishes

**Format:**

```yaml
hooks:
  PreToolUse:
    - matcher: "ToolName"
      hooks:
        - type: command
          command: "./scripts/validate.sh"
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: "./scripts/run-linter.sh"
  Stop:
    - hooks:
        - type: command
          command: "./scripts/cleanup.sh"
```

**Examples:**

```yaml
# Validate database queries before execution
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-readonly-query.sh"

# Run linter after file edits
hooks:
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: "./scripts/lint-files.sh"

# Cleanup on completion
hooks:
  Stop:
    - hooks:
        - type: command
          command: "./scripts/cleanup-temp-files.sh"
```

See [Hooks Integration](hooks-integration.md) for detailed hook documentation.

## Complete Examples

### Minimal Configuration

```yaml
---
name: quick-reviewer
description: Quick code review. Use after small changes.
---

Review code changes quickly. Focus on critical issues only.
```

### Read-Only Analyzer

```yaml
---
name: code-analyzer
description: Analyze code quality and architecture. Use when investigating codebases.
tools: Read, Grep, Glob, CodebaseSearch
model: sonnet
---

You are a code quality analyst...
```

### Full-Featured Subagent

```yaml
---
name: api-developer
description: Implement API endpoints following team conventions. Use for API development.
tools: Read, Write, Edit, Grep, Glob, Bash
model: sonnet
permissionMode: acceptEdits
skills:
  - api-conventions
  - error-handling-patterns
hooks:
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: "./scripts/run-api-tests.sh"
---

You implement API endpoints following preloaded conventions...
```

### Constrained Bash Subagent

```yaml
---
name: db-reader
description: Execute read-only database queries for data analysis.
tools: Bash
model: haiku
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-readonly-query.sh"
---

You are a database analyst with read-only access...
```

## Field Validation

The `validate_subagent.py` script checks:

- **name**: Format, length, character restrictions
- **description**: Presence, minimum length, TODO placeholders
- **tools**: Valid tool names
- **model**: Valid model names
- **permissionMode**: Valid mode names
- **skills**: List format
- **hooks**: Valid event names and structure

Run validation:
```bash
scripts/validate_subagent.py <path-to-subagent.md>
```
