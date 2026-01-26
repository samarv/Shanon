---
name: subagent-creator
description: Guide for creating effective custom subagents in Claude Code. Use when users want to create or update specialized AI subagents with custom system prompts, tool restrictions, and specific configurations for task delegation.
---

# Subagent Creator

This skill provides guidance for creating effective custom subagents in Claude Code.

## Using This Skill

**CRITICAL**: When helping users create subagents, always follow these meta-principles learned from effective subagent design:

1. **Announce Your Approach**: Start by identifying what type of subagent they need (read-only analyzer, domain expert, performance optimizer, etc.)
2. **Use the Decision Tree**: Guide them through structured questions to determine the right configuration
3. **Apply Visibility Principles**: Teach them to add framework/methodology announcements in their subagent prompts
4. **Distinguish Primary vs Supporting**: Help them identify ONE main task, with supporting capabilities as needed
5. **Include Complete Examples**: Show working examples, not just abstract templates

## About Subagents

Subagents are specialized AI assistants that handle specific types of tasks. Each subagent runs in its own context window with a custom system prompt, specific tool access, and independent permissions. When Claude encounters a task that matches a subagent's description, it delegates to that subagent, which works independently and returns results.

### Benefits of Subagents

1. **Preserve context** - Keep exploration and implementation out of your main conversation
2. **Enforce constraints** - Limit which tools a subagent can use
3. **Reuse configurations** - Share user-level subagents across all projects
4. **Specialize behavior** - Focus system prompts for specific domains
5. **Control costs** - Route tasks to faster, cheaper models like Haiku

### Meta-Principles from Effective Subagents

Based on analysis of high-performing subagents (growth-experiments, marketing-copywriter):

**The Framework Visibility Pattern:**
When a subagent has multiple preloaded skills (3+), users can't see which methodology is being applied. Solution:
1. List all preloaded frameworks with descriptions
2. Provide decision tree for selection
3. Require announcement at start: `🔧 FRAMEWORK: [name] + REASON`
4. Include example workflow showing proper usage

**The Decision Tree Pattern:**
Complex subagents need structured routing logic, not just lists:
- Bad: "Use framework-a for X, framework-b for Y, framework-c for Z"
- Good: Multi-step decision tree with clear conditionals

**The Primary vs Supporting Pattern:**
Prevent framework dilution by distinguishing:
- **Primary frameworks**: Choose ONE based on scenario
- **Supporting frameworks**: Consult as needed in addition

**The Complete Example Pattern:**
Abstract templates confuse. Show working examples:
- User request → Framework announcement → Execution → Output
- Mark what makes it good with ✅ checklist

Apply these patterns when creating complex, multi-skill subagents.

## Core Principles

### 1. Focused Specialization

Each subagent should excel at one specific task. Narrow focus leads to better performance.

**Good**: A subagent that reviews code for security vulnerabilities  
**Bad**: A subagent that reviews code, writes tests, and deploys applications

### 2. Clear Descriptions with Triggers

Claude uses the `description` field to decide when to delegate. Write clear, specific descriptions that include:
- What the subagent does
- When to use it (specific scenarios)
- What triggers delegation

Include phrases like "use proactively" or "use immediately after" to encourage automatic delegation.

### 3. Minimal Tool Access

Grant only necessary permissions (principle of least privilege):
- Read-only subagents: `tools: Read, Grep, Glob`
- Bash-only subagents: `tools: Bash`
- Full-access subagents: Omit `tools` field to inherit all

Use `disallowedTools` to deny specific tools while inheriting others.

### 4. Skill Visibility (CRITICAL)

**When a subagent preloads skills, teach it to announce which framework it's using.**

If your subagent has multiple preloaded skills (like the growth-experiments or marketing-copywriter patterns):
- Add a "Preloaded Skills" section listing all available frameworks
- Include a decision tree to guide framework selection
- Require the subagent to announce: `🔧 FRAMEWORK: [name]` at the start of responses
- This makes methodology visible to users

Example from effective subagents:
```markdown
## Preloaded Skills

You have 5 specialized frameworks:
- `skill-a` - For scenario X
- `skill-b` - For scenario Y

**CRITICAL**: Always announce which primary framework you're applying.
```

### 5. Progressive Disclosure

Start simple, add complexity only when needed:
1. Begin with basic system prompt
2. Add tool restrictions if needed
3. Configure model selection for performance/cost
4. Add hooks for advanced validation
5. Preload skills for domain knowledge
6. Add framework visibility (if multiple skills)

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

### Step 1: Understanding the Use Case

**Start by identifying the subagent type using this decision tree:**

#### Subagent Type Decision Tree

**What's the primary purpose?**

**Analysis/Research (Read-Only)**
- Code quality analysis → `code-analyzer` pattern
- Codebase exploration → `explorer` pattern  
- Documentation review → `doc-reviewer` pattern
- Security audit → `security-auditor` pattern

**Transformation/Building (Read-Write)**
- Feature implementation → `feature-builder` pattern
- Refactoring → `refactorer` pattern
- Test generation → `test-generator` pattern
- Documentation generation → `doc-generator` pattern

**Domain Expertise (Multi-Framework)**
- Growth experimentation → See growth-experiments example
- Marketing copywriting → See marketing-copywriter example
- Data analysis → `data-analyst` pattern
- API development → `api-developer` pattern

**Constrained Operations (Tool-Restricted)**
- Read-only database queries → `db-reader` pattern
- Safe file operations → `safe-operator` pattern
- Validated commands → Pattern with hooks

#### Clarifying Questions

After identifying the type, gather specifics:

- **Task scope**: What exactly will it do? Give concrete examples.
- **Tool needs**: Should it only read, or also modify files?
- **Domain knowledge**: Does it need preloaded skills/frameworks?
- **Output format**: What should the results look like?
- **Triggers**: When should Claude automatically delegate to it?

**Example for a domain expert subagent:**
- "Will it use multiple methodologies or just one approach?"
- "Should it announce which framework it's applying?"
- "How many skills will be preloaded? (If >3, add framework visibility)"

Conclude when you have a clear sense of type, scope, and configuration needs.

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

The body after frontmatter becomes the system prompt. Structure depends on complexity:

**For Simple Subagents (Single Task):**

1. **Role definition**: "You are a [role] specializing in [domain]"
2. **Workflow**: Step-by-step process when invoked
3. **Key practices**: Guidelines and best practices
4. **Output format**: How to present results

**Example:**
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

Provide feedback by priority:
- Critical issues (must fix)
- Warnings (should fix)  
- Suggestions (consider improving)
```

**For Complex Subagents (Multiple Skills/Frameworks):**

Apply the visibility pattern from growth-experiments and marketing-copywriter:

1. **Role definition** with specializations
2. **Preloaded Skills section** listing all frameworks
3. **Decision tree** for framework selection
4. **Framework announcement requirement** with format
5. **Workflow steps** that include announcing choice
6. **Example workflow** showing proper usage

**Example structure:**
```markdown
You are a [domain] specialist with deep expertise in [areas].

## Preloaded Skills

You have N specialized frameworks preloaded:
- `framework-a` - For scenario X
- `framework-b` - For scenario Y
- `framework-c` - For scenario Z

**CRITICAL**: Always announce which primary framework you're applying 
at the start of your response so the user knows which methodology 
is guiding the work.

## When Invoked

Follow this workflow:

### 1. Understand the Context
Gather key details:
- [Question 1]
- [Question 2]

If information is missing, ask clarifying questions.

### 2. Select Primary Framework

Use this decision tree:

**STEP 1: Identify scenario type**
- Condition A? → Use `framework-a`
- Condition B? → Use `framework-b`
- Condition C? → Use `framework-c`

**IMPORTANT**: Select ONE primary framework. Don't apply all simultaneously.

### 3. Announce Your Framework Choice

**ALWAYS start your response with:**

```
🔧 FRAMEWORK: [framework-name]
REASON: [One sentence why this framework fits]
```

### 4. Execute
Apply the selected framework's methodology...

## Example Workflow

Here's how you should respond:

**User Request**: "[example request]"

**Your Response**:
```
🔧 FRAMEWORK: framework-a
REASON: [Reasoning for selection]

[Rest of response applying framework principles]
```

**What Makes This Good:**
✅ Framework announced with reasoning
✅ Applied framework methodology
✅ User knows which approach is being used
```

**Key Differences:**
- Simple subagents: Direct workflow
- Complex subagents: Add framework visibility layer
- Add decision tree when 3+ skills are preloaded
- Always include example workflow for complex patterns

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

Inject domain knowledge via skills. **For 3+ skills, add framework visibility:**

```yaml
---
name: growth-strategist
description: |
  Growth strategy expert with multiple frameworks. Use proactively for 
  growth planning, experimentation, or optimization work.
skills:
  - growth-model-construction
  - experimentation-framework
  - retention-optimization
  - acquisition-strategy
model: sonnet
---

You are a growth strategist with deep expertise in user acquisition, 
retention, and experimentation.

## Preloaded Skills

You have 4 specialized frameworks preloaded:
- `growth-model-construction` - Building growth models and forecasts
- `experimentation-framework` - A/B testing and experiment design
- `retention-optimization` - Improving user retention and engagement
- `acquisition-strategy` - User acquisition channel strategy

**CRITICAL**: Always announce which primary framework you're applying 
at the start of your response.

## When Invoked

### 1. Understand the Context
- What's the growth challenge?
- Current metrics and goals?
- Stage of company (early, growth, scale)?

### 2. Select Primary Framework

**STEP 1: Identify the request type**
- Building forecasts or models? → Use `growth-model-construction`
- Designing experiments? → Use `experimentation-framework`
- Improving retention? → Use `retention-optimization`
- Scaling acquisition? → Use `acquisition-strategy`

### 3. Announce Your Choice

**ALWAYS start with:**
```
📈 FRAMEWORK: [framework-name]
FOCUS: [What aspect of growth]
```

### 4. Apply Framework
Execute using the selected framework's methodology.

## Example

**User**: "Help me design an experiment to test a new onboarding flow"

**Response**:
```
📈 FRAMEWORK: experimentation-framework
FOCUS: Onboarding conversion optimization

## Context Questions
- Current onboarding completion rate?
- Weekly signup volume?
...
```
```

**Why This Works:**
- Lists available frameworks upfront
- Decision tree guides selection
- Required announcement makes methodology visible
- Example shows proper usage
- User always knows which approach is being applied

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

### General Principles

1. **One responsibility per subagent** - Narrow focus works better
2. **Clear, specific descriptions** - Claude uses these for delegation
3. **Minimal tool access** - Grant only what's needed
4. **Test thoroughly** - Try edge cases and unusual inputs
5. **Version control project subagents** - Share with your team
6. **Document complex hooks** - Make validation scripts clear
7. **Iterate based on usage** - Refine after real-world use

### Framework Visibility (When Using Multiple Skills)

**When to add framework visibility:**
- Subagent has 3+ preloaded skills
- Multiple methodologies or approaches are available
- Different scenarios require different frameworks

**How to implement:**
1. Add "Preloaded Skills" section listing all frameworks
2. Create decision tree for framework selection
3. Require announcement format (🔧/📈/✍️ FRAMEWORK: [name])
4. Add "Announce Your Choice" step to workflow
5. Include complete example showing proper usage

**Benefits:**
- User knows which methodology is being applied
- Prevents framework dilution (trying to use all at once)
- Makes subagent reasoning transparent
- Easier to debug and improve

**Real examples to study:**
- `.claude/agents/growth-experiments.md` - 9 skills with decision tree
- `.claude/agents/marketing-copywriter.md` - 11 skills with copy-type routing

### Anti-Patterns to Avoid

**Configuration Errors:**
- ❌ Too broad scope (subagent tries to do everything)
- ❌ Missing triggers in description (Claude won't delegate)
- ❌ Excessive tool access (violates least privilege)
- ❌ No example workflow (unclear how to use)

**Prompt Design Errors:**
- ❌ Generic instructions (not specific to the domain)
- ❌ No workflow structure (subagent doesn't know steps)
- ❌ Missing output format guidance
- ❌ Preloading many skills without framework visibility

**Multi-Skill Errors:**
- ❌ 5+ skills with no decision tree (overwhelming)
- ❌ No framework announcement requirement (user blind to methodology)
- ❌ Trying to apply all frameworks simultaneously
- ❌ No example showing framework selection in action

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

## Complete Example: Creating a Multi-Framework Subagent

Let's walk through creating a "product-strategist" subagent with multiple frameworks:

### User Request
"I want a subagent that helps with product strategy - market analysis, roadmap planning, and competitive positioning."

### Step 1: Identify Type (Using Decision Tree)
- **Purpose**: Domain expertise (multiple methodologies)
- **Pattern**: Domain Expert with Preloaded Skills
- **Skills needed**: 4+ frameworks → Need framework visibility

### Step 2: Clarifying Questions
**You ask:**
- "Which specific frameworks: opportunity-solution-tree, five-step-positioning, competitive-analysis, now-next-later-roadmapping?"
- "Should it work on existing strategy docs or create new ones?"
- "Any tool restrictions or should it inherit all?"

**User answers:**
- "Yes to those 4 frameworks"
- "Both - analyze and create"
- "Needs write access"

### Step 3: Plan Configuration
```yaml
name: product-strategist
scope: project (team uses it)
tools: All (inherits - needs write)
model: sonnet (balanced for strategy work)
skills: 4 frameworks
visibility: YES (4 skills = add framework announcement)
```

### Step 4: Create the Subagent

**Frontmatter:**
```yaml
---
name: product-strategist
description: |
  Product strategy expert specializing in market analysis, positioning, 
  roadmapping, and opportunity identification. Use proactively for 
  strategy planning, competitive analysis, or roadmap work.
skills:
  - opportunity-solution-tree-mapping
  - five-step-product-positioning
  - competitive-analysis-framework
  - now-next-later-roadmapping
model: sonnet
---
```

**System Prompt (applying framework visibility pattern):**
```markdown
You are a senior product strategist with deep expertise in market 
analysis, positioning, and strategic planning.

## Preloaded Skills

You have 4 specialized frameworks preloaded:
- `opportunity-solution-tree-mapping` - Connecting outcomes to solutions
- `five-step-product-positioning` - Market positioning strategy
- `competitive-analysis-framework` - Analyzing competitive landscape
- `now-next-later-roadmapping` - Strategic roadmap planning

**CRITICAL**: Always announce which primary framework you're applying 
at the start of your response so the user knows which methodology 
is guiding the strategy work.

## When Invoked

### 1. Understand the Context

Gather these details:
- **What stage?**: Analysis, planning, or execution?
- **What's the focus?**: Market, competition, roadmap, positioning?
- **What deliverable?**: Document, framework application, analysis?

**If key information is missing, ask clarifying questions.**

### 2. Select Primary Framework

Use this decision tree:

**STEP 1: Identify the strategic need**
- **Connecting problems to solutions?** → Use `opportunity-solution-tree-mapping`
- **Defining market position?** → Use `five-step-product-positioning`
- **Analyzing competitors?** → Use `competitive-analysis-framework`
- **Planning roadmap?** → Use `now-next-later-roadmapping`

**IMPORTANT**: Select ONE primary framework. Don't apply all simultaneously.

### 3. Announce Your Framework Choice

**ALWAYS start your response with:**

```
🎯 FRAMEWORK: [framework-name]
FOCUS: [Strategic area]
DELIVERABLE: [What you'll produce]
```

**Example:**
```
🎯 FRAMEWORK: five-step-product-positioning
FOCUS: Market positioning for new AI feature
DELIVERABLE: Positioning statement and messaging
```

### 4. Execute Strategy Work

Apply the selected framework's methodology:
- Gather necessary context
- Apply framework principles
- Produce structured output
- Provide strategic recommendations

## Example Workflow

**User Request**: "Help me position our new AI assistant feature"

**Your Response**:

```
🎯 FRAMEWORK: five-step-product-positioning
FOCUS: AI assistant feature positioning
DELIVERABLE: Complete positioning statement

## Context Questions
Before positioning, I need:
- Who's the target customer segment?
- What's the alternative they use today?
- What's unique about your approach?

[Assuming answers provided...]

## Positioning Analysis

### 1. Target Segment
[Framework step 1 application]

### 2. Market Category
[Framework step 2 application]

[etc.]
```

**What Makes This Good:**
✅ Framework announced with focus area
✅ Asked clarifying questions
✅ Applied framework methodology systematically
✅ User knows which approach guides the strategy
```

### Step 5: Test & Validate

**Test scenarios:**
1. "Analyze our competitive landscape" → Should trigger competitive-analysis-framework
2. "Build a roadmap for Q2" → Should trigger now-next-later-roadmapping
3. "How should we position against competitor X?" → Should trigger five-step-product-positioning

**Validation:**
```bash
scripts/validate_subagent.py .claude/agents/product-strategist.md
```

### Step 6: Results

**What we built:**
- ✅ Clear delegation triggers in description
- ✅ 4 frameworks with visibility pattern
- ✅ Decision tree for framework selection
- ✅ Required framework announcement (🎯 FRAMEWORK)
- ✅ Complete example showing usage
- ✅ Proper workflow structure

**Why it works:**
- User always knows which strategy methodology is being applied
- Prevents trying to use all 4 frameworks at once
- Clear routing logic based on strategic need
- Can be tested, debugged, and improved systematically

---

This example demonstrates applying the meta-principles to create effective multi-framework subagents. Use this pattern for any domain expert subagent with 3+ preloaded skills.

