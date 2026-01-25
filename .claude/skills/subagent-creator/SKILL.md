---
name: subagent-creator
description: Guide for creating effective custom subagents in Claude Code. Use when users want to create or update specialized AI subagents with custom system prompts, tool restrictions, and specific configurations for task delegation.
---

# Subagent Creator

This skill provides guidance for creating effective custom subagents in Claude Code.

## About Subagents

Subagents are specialized AI assistants that handle specific types of tasks. Each subagent runs in its own context window with a custom system prompt, specific tool access, and independent permissions. When Claude encounters a task that matches a subagent's description, it delegates to that subagent, which works independently and returns results.

### Benefits of Subagents

1. **Preserve context** - Keep exploration and implementation out of your main conversation
2. **Enforce constraints** - Limit which tools a subagent can use
3. **Reuse configurations** - Share user-level subagents across all projects
4. **Specialize behavior** - Focus system prompts for specific domains
5. **Control costs** - Route tasks to faster, cheaper models like Haiku

## Core Principles

### Focused Specialization

Each subagent should excel at one specific task. Narrow focus leads to better performance.

**Good**: A subagent that reviews code for security vulnerabilities  
**Bad**: A subagent that reviews code, writes tests, and deploys applications

### Clear Descriptions

Claude uses the `description` field to decide when to delegate. Write clear, specific descriptions that include:
- What the subagent does
- When to use it (specific scenarios)
- What triggers delegation

Include phrases like "use proactively" or "use immediately after" to encourage automatic delegation.

### Minimal Tool Access

Grant only necessary permissions (principle of least privilege):
- Read-only subagents: `tools: Read, Grep, Glob`
- Bash-only subagents: `tools: Bash`
- Full-access subagents: Omit `tools` field to inherit all

Use `disallowedTools` to deny specific tools while inheriting others.

### Progressive Disclosure

Start simple, add complexity only when needed:
1. Begin with basic system prompt
2. Add tool restrictions if needed
3. Configure model selection for performance/cost
4. Add hooks for advanced validation
5. Preload skills for domain knowledge

## Anatomy of a Subagent

Subagents are Markdown files with YAML frontmatter:

```markdown
---
name: code-reviewer
description: Expert code review specialist. Use proactively after code changes.
tools: Read, Grep, Glob, Bash
model: sonnet
---

You are a senior code reviewer ensuring high standards.

When invoked:
1. Run git diff to see recent changes
2. Review modified files
3. Provide specific feedback
```

### Required Fields

- **name**: Unique identifier (lowercase, hyphens, max 40 chars)
- **description**: When Claude should delegate (critical for triggering)

### Optional Fields

- **tools**: Tools this subagent can use (inherits all if omitted)
- **disallowedTools**: Tools to deny from inherited set
- **model**: `sonnet`, `opus`, `haiku`, or `inherit` (default)
- **permissionMode**: `default`, `acceptEdits`, `dontAsk`, `bypassPermissions`, or `plan`
- **skills**: Skills to preload into subagent's context
- **hooks**: Lifecycle hooks (`PreToolUse`, `PostToolUse`, `Stop`)

See [Configuration Reference](references/configuration-reference.md) for complete details.

## Subagent Scope

Store subagents in different locations based on scope:

| Location | Scope | Priority |
|----------|-------|----------|
| `--agents` CLI flag | Current session | 1 (highest) |
| `.claude/agents/` | Current project | 2 |
| `~/.claude/agents/` | All your projects | 3 |
| Plugin's `agents/` | Where enabled | 4 (lowest) |

**Project subagents** (`.claude/agents/`) - Share with your team via version control  
**User subagents** (`~/.claude/agents/`) - Personal subagents for all projects

## Subagent Creation Process

Follow these steps to create effective subagents:

1. Understand the use case with concrete examples
2. Plan the subagent configuration
3. Initialize the subagent file
4. Edit the configuration and system prompt
5. Test with real tasks
6. Iterate based on performance

### Step 1: Understanding the Use Case

Clarify what the subagent should do with concrete examples:

- What task will it perform?
- When should Claude delegate to it?
- What tools does it need?
- Should it modify files or only read?
- What should the output look like?

**Example questions for an image-processor subagent:**
- "Should it only analyze images or also edit them?"
- "What image operations: resize, crop, format conversion?"
- "Can you give examples of how you'd use it?"

Conclude when you have a clear sense of functionality.

### Step 2: Planning the Configuration

Based on the use case, determine:

1. **Name**: Short, descriptive (e.g., `code-reviewer`, `db-reader`)
2. **Tools**: What capabilities are needed?
   - Read-only: `Read, Grep, Glob`
   - With shell access: Add `Bash`
   - Can modify: Add `Write, Edit`
3. **Model**: Balance capability and cost
   - `haiku` - Fast, cheap (simple tasks)
   - `sonnet` - Balanced (most use cases)
   - `opus` - Powerful (complex reasoning)
   - `inherit` - Match main conversation
4. **Scope**: Project or user-level?
5. **Constraints**: Any tool restrictions or hooks needed?

### Step 3: Initialize the Subagent

Use the initialization script for quick setup:

```bash
scripts/init_subagent.py <subagent-name> --scope <project|user>
```

Examples:
```bash
# Project-level subagent (shared with team)
scripts/init_subagent.py code-reviewer --scope project

# User-level subagent (personal, all projects)
scripts/init_subagent.py data-analyzer --scope user
```

The script creates a template file with TODO placeholders at the appropriate location.

Alternatively, use the `/agents` command in Claude Code for interactive creation.

### Step 4: Edit the Subagent

#### Complete the Frontmatter

1. **Description**: Write a clear, comprehensive description
   - What the subagent does
   - When to use it (specific triggers)
   - Include "use proactively" if appropriate

   Example:
   ```yaml
   description: Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code.
   ```

2. **Tools**: Configure tool access
   - Specify allowed tools: `tools: Read, Grep, Glob`
   - Or deny specific tools: `disallowedTools: Write, Edit`
   - Or inherit all tools: (omit field)

3. **Model**: Choose appropriate model (optional)
   ```yaml
   model: haiku  # Fast and cheap
   model: sonnet # Balanced
   model: opus   # Most capable
   model: inherit # Match parent (default)
   ```

#### Write the System Prompt

The body after frontmatter becomes the system prompt. Include:

1. **Role definition**: "You are a [role] specializing in [domain]"
2. **Workflow**: Step-by-step process when invoked
3. **Key practices**: Guidelines and best practices
4. **Output format**: How to present results

**Example structure:**
```markdown
You are a senior code reviewer ensuring high standards.

When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Begin review immediately

Review checklist:
- Code clarity and readability
- Proper error handling
- Security considerations
- Performance implications

Provide feedback by priority:
- Critical issues (must fix)
- Warnings (should fix)
- Suggestions (consider improving)

Include specific examples of how to fix issues.
```

Keep prompts focused on the specific task. See [Patterns and Examples](references/patterns-and-examples.md) for more templates.

### Step 5: Test the Subagent

Test with real tasks to validate behavior:

1. **Explicit delegation**: "Use the code-reviewer subagent to review my recent changes"
2. **Automatic delegation**: Make code changes and see if Claude delegates automatically
3. **Edge cases**: Test with unusual inputs or scenarios

Check:
- Does it trigger at the right time?
- Does it have the right tools?
- Is the output useful?
- Are any permissions missing?

Validate the configuration:
```bash
scripts/validate_subagent.py .claude/agents/code-reviewer.md
```

### Step 6: Iterate

Based on testing, refine:
- **Description**: Make triggers clearer if delegation is inconsistent
- **System prompt**: Add missing guidance or clarify instructions
- **Tools**: Adjust if it needs more or fewer capabilities
- **Model**: Change if performance or cost is an issue

## Common Patterns

### Read-Only Analyzer

For analysis without modification:

```yaml
---
name: code-analyzer
description: Analyze code quality and architecture. Use when investigating codebases.
tools: Read, Grep, Glob, Bash
model: sonnet
---

You are a code quality analyst.

When invoked:
1. Understand the analysis request
2. Search relevant code sections
3. Identify patterns and issues
4. Provide structured findings

Focus on: architecture, patterns, quality, maintainability.
```

### Bash-Restricted with Validation

Allow Bash but validate commands with hooks:

```yaml
---
name: db-reader
description: Execute read-only database queries. Use for data analysis.
tools: Bash
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-readonly-query.sh"
---

You are a database analyst with read-only access.

Execute SELECT queries only. If asked to modify data, explain you have read-only access.
```

Create the validation script separately. See [Hooks Integration](references/hooks-integration.md).

### Full-Access Developer

For tasks requiring modification:

```yaml
---
name: feature-builder
description: Implement new features end-to-end. Use when building complete features.
tools: Read, Write, Edit, Grep, Glob, Bash
model: sonnet
---

You are a full-stack developer implementing features.

When invoked:
1. Understand requirements
2. Plan implementation
3. Write code with proper structure
4. Test thoroughly
5. Document changes

Focus on: clean code, proper testing, clear documentation.
```

### Domain Expert with Preloaded Skills

Inject domain knowledge via skills:

```yaml
---
name: api-developer
description: Implement API endpoints following team conventions. Use for API work.
skills:
  - api-conventions
  - error-handling-patterns
model: sonnet
---

You implement API endpoints following preloaded conventions.

Apply patterns from loaded skills. Maintain consistency with existing APIs.
```

See [Patterns and Examples](references/patterns-and-examples.md) for more detailed examples.

## When to Create Subagents vs Skills

**Use Subagents when:**
- You want isolated context (keep verbose output separate)
- You need tool restrictions (enforce read-only, bash-only, etc.)
- You want to route to different models (Haiku for speed/cost)
- The task is self-contained with clear delegation triggers

**Use Skills when:**
- You want to extend knowledge in the main conversation
- You need bundled resources (scripts, references, assets)
- The workflow should run in current context
- You want to teach Claude new procedures or formats

**Use Both when:**
- A subagent needs domain knowledge (use `skills` field in subagent)
- A skill should run in isolation (use `context: fork` in skill)

## Using the /agents Command

Claude Code provides the `/agents` command for interactive management:

- View all available subagents
- Create new subagents with guided setup
- Edit existing subagent configuration
- Delete custom subagents
- See which subagents are active when duplicates exist

This skill focuses on programmatic creation and understanding subagent design. Use `/agents` for interactive workflows.

## Validation and Quality

Always validate subagents before deployment:

```bash
scripts/validate_subagent.py <path-to-subagent.md>
```

The validator checks:
- YAML frontmatter format
- Required fields present
- Valid tool names
- Valid model and permission mode values
- System prompt completeness

Fix all errors before using the subagent.

## Best Practices

1. **One responsibility per subagent** - Narrow focus works better
2. **Clear, specific descriptions** - Claude uses these for delegation
3. **Minimal tool access** - Grant only what's needed
4. **Test thoroughly** - Try edge cases and unusual inputs
5. **Version control project subagents** - Share with your team
6. **Document complex hooks** - Make validation scripts clear
7. **Iterate based on usage** - Refine after real-world use

## Resources

### scripts/

- **init_subagent.py** - Generate new subagent templates
- **validate_subagent.py** - Validate subagent configuration

### references/

- **configuration-reference.md** - Complete field reference with examples
- **patterns-and-examples.md** - Detailed subagent patterns and templates
- **hooks-integration.md** - Using hooks for conditional validation

### assets/

- **template-subagent.md** - Clean template for manual creation
- **examples/** - Working examples (code-reviewer, db-reader)
