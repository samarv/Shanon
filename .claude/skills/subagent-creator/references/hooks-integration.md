# Hooks Integration

Guide for using hooks with subagents to add validation, automation, and lifecycle management.

## Overview

Hooks are commands that run at specific points in a subagent's lifecycle. They enable:
- **Validation** - Check inputs before tool execution
- **Automation** - Run linters, tests, or cleanup after actions
- **Lifecycle management** - Setup and teardown operations

## Hook Events

### PreToolUse

Runs **before** a subagent uses a tool. Use for validation and approval.

**When it fires:** Before each tool invocation  
**Matcher:** Tool name (e.g., `Bash`, `Edit`, `Write`)  
**Exit code behavior:**
- `0` - Allow operation
- `1` - Log error, allow operation
- `2` - **Block operation**, return error to subagent

**Configuration:**

```yaml
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-command.sh"
```

**Use cases:**
- Validate SQL queries are read-only
- Check file paths are within allowed directories
- Verify commands don't contain dangerous operations
- Enforce naming conventions before creating files

### PostToolUse

Runs **after** a subagent uses a tool. Use for automation and validation.

**When it fires:** After each tool invocation completes  
**Matcher:** Tool name (e.g., `Edit`, `Write`, `Bash`)  
**Exit code behavior:**
- `0` - Success
- `1` - Log error, continue
- Non-zero - Logged but doesn't block subsequent operations

**Configuration:**

```yaml
hooks:
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: "./scripts/run-linter.sh"
```

**Use cases:**
- Run linters after file edits
- Execute tests after code changes
- Update documentation after API changes
- Generate derived files (e.g., build artifacts)

### Stop

Runs when the subagent finishes execution. Use for cleanup and finalization.

**When it fires:** When subagent completes (success or failure)  
**Matcher:** None (applies to all Stop events)  
**Exit code behavior:**
- Exit codes logged but don't affect subagent result

**Configuration:**

```yaml
hooks:
  Stop:
    - hooks:
        - type: command
          command: "./scripts/cleanup.sh"
```

**Use cases:**
- Clean up temporary files
- Close connections
- Generate summary reports
- Reset environment state

## Hook Input Format

Hooks receive JSON input via stdin with tool parameters and context.

### PreToolUse Input

```json
{
  "event": "PreToolUse",
  "tool": "Bash",
  "tool_input": {
    "command": "SELECT * FROM users WHERE active = true"
  },
  "agent_id": "abc123",
  "agent_name": "db-reader"
}
```

### PostToolUse Input

```json
{
  "event": "PostToolUse",
  "tool": "Edit",
  "tool_input": {
    "file_path": "src/api/users.py",
    "old_string": "...",
    "new_string": "..."
  },
  "tool_output": "File edited successfully",
  "agent_id": "abc123",
  "agent_name": "code-fixer"
}
```

### Stop Input

```json
{
  "event": "Stop",
  "agent_id": "abc123",
  "agent_name": "code-reviewer",
  "final_status": "completed"
}
```

## Complete Examples

### 1. Read-Only Database Validator

Blocks SQL write operations using PreToolUse hook.

**Subagent configuration:**

```yaml
---
name: db-reader
description: Execute read-only database queries. Use for data analysis and reporting.
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

When analyzing data:
1. Identify relevant tables
2. Write efficient SELECT queries
3. Present results with context
```

**Validation script** (`scripts/validate-readonly-query.sh`):

```bash
#!/bin/bash
# Validates that SQL queries are read-only (SELECT only)

# Read JSON input from stdin
INPUT=$(cat)

# Extract the command from tool_input
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# If no command, allow (nothing to validate)
if [ -z "$COMMAND" ]; then
  exit 0
fi

# Check for write operations (case-insensitive)
WRITE_OPS='INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|TRUNCATE|REPLACE|MERGE'
if echo "$COMMAND" | grep -iE "\b($WRITE_OPS)\b" > /dev/null; then
  # Write to stderr (shown to subagent)
  echo "Blocked: Write operations not allowed. Use SELECT queries only." >&2
  # Exit 2 blocks the operation
  exit 2
fi

# Allow the operation
exit 0
```

**Make executable:**

```bash
chmod +x scripts/validate-readonly-query.sh
```

**Testing:**

```bash
# Should block
echo '{"tool_input":{"command":"DELETE FROM users"}}' | ./scripts/validate-readonly-query.sh

# Should allow
echo '{"tool_input":{"command":"SELECT * FROM users"}}' | ./scripts/validate-readonly-query.sh
```

### 2. Auto-Linting Code Editor

Runs linter after each file edit using PostToolUse hook.

**Subagent configuration:**

```yaml
---
name: code-fixer
description: Fix code issues with automatic linting. Use when making code improvements or bug fixes.
tools: Read, Edit, Grep, Glob, Bash
model: sonnet
hooks:
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: "./scripts/run-linter.sh"
---

You fix code issues efficiently.

When invoked:
1. Understand the issue
2. Implement the fix
3. Wait for linter results (runs automatically)
4. Address any linter errors

The linter runs after each edit. If it reports issues, fix them immediately.
```

**Linter script** (`scripts/run-linter.sh`):

```bash
#!/bin/bash
# Runs appropriate linter based on file type

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

if [ -z "$FILE_PATH" ]; then
  exit 0
fi

# Determine file type and run linter
case "$FILE_PATH" in
  *.py)
    echo "Running pylint on $FILE_PATH..."
    python3 -m pylint "$FILE_PATH" 2>&1
    ;;
  *.js|*.ts|*.jsx|*.tsx)
    echo "Running eslint on $FILE_PATH..."
    npx eslint "$FILE_PATH" 2>&1
    ;;
  *.go)
    echo "Running golint on $FILE_PATH..."
    golint "$FILE_PATH" 2>&1
    ;;
  *)
    echo "No linter configured for $FILE_PATH"
    ;;
esac

# Exit 0 even if linter finds issues (non-blocking)
exit 0
```

### 3. Test Runner with Cleanup

Runs tests after changes and cleans up on completion.

**Subagent configuration:**

```yaml
---
name: feature-developer
description: Develop features with automatic testing and cleanup. Use for feature implementation.
tools: Read, Write, Edit, Bash, Grep, Glob
model: sonnet
hooks:
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: "./scripts/run-tests.sh"
  Stop:
    - hooks:
        - type: command
          command: "./scripts/cleanup-temp.sh"
---

You develop features with automatic validation.

When invoked:
1. Implement the feature
2. Tests run automatically after changes
3. Fix any test failures
4. Cleanup happens automatically on completion
```

**Test runner** (`scripts/run-tests.sh`):

```bash
#!/bin/bash
INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Run tests related to changed file
if [[ "$FILE_PATH" == *.py ]]; then
  TEST_FILE="${FILE_PATH/src/tests}"
  TEST_FILE="${TEST_FILE/.py/_test.py}"
  
  if [ -f "$TEST_FILE" ]; then
    echo "Running tests for $FILE_PATH..."
    python3 -m pytest "$TEST_FILE" -v
  fi
fi

exit 0
```

**Cleanup script** (`scripts/cleanup-temp.sh`):

```bash
#!/bin/bash
# Clean up temporary files created during development

echo "Cleaning up temporary files..."

# Remove common temp patterns
find . -type f -name "*.tmp" -delete
find . -type f -name "*.pyc" -delete
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null

echo "Cleanup complete"
exit 0
```

### 4. Path Validator

Ensures file operations stay within allowed directories.

**Subagent configuration:**

```yaml
---
name: safe-editor
description: Edit files with path validation. Use for controlled file modifications.
tools: Read, Edit, Write
hooks:
  PreToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: "./scripts/validate-path.sh"
---

You edit files safely within allowed directories.

All file operations are validated. If a path is denied, choose an alternate approach.
```

**Path validator** (`scripts/validate-path.sh`):

```bash
#!/bin/bash
INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Allowed directories
ALLOWED_DIRS=("src/" "tests/" "docs/")

# Check if path starts with allowed directory
ALLOWED=false
for dir in "${ALLOWED_DIRS[@]}"; do
  if [[ "$FILE_PATH" == "$dir"* ]]; then
    ALLOWED=true
    break
  fi
done

if [ "$ALLOWED" = false ]; then
  echo "Blocked: File path '$FILE_PATH' outside allowed directories: ${ALLOWED_DIRS[*]}" >&2
  exit 2
fi

exit 0
```

## Hook Script Best Practices

### 1. Parse JSON Safely

Always use `jq` for JSON parsing:

```bash
#!/bin/bash
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# Check if jq failed
if [ $? -ne 0 ]; then
  echo "Error parsing JSON input" >&2
  exit 1
fi
```

### 2. Handle Missing Fields

Provide defaults for missing fields:

```bash
# Use // empty for safe default
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Check if field is present
if [ -z "$FILE_PATH" ]; then
  # Nothing to validate, allow
  exit 0
fi
```

### 3. Write Clear Error Messages

Error messages go to stderr and are shown to the subagent:

```bash
if [ "$INVALID" = true ]; then
  echo "Blocked: Invalid operation - $REASON" >&2
  exit 2
fi
```

### 4. Use Exit Codes Correctly

```bash
# 0 - Allow/Success
exit 0

# 1 - Log error but continue
echo "Warning: Something wrong" >&2
exit 1

# 2 - Block operation (PreToolUse only)
echo "Blocked: Operation not allowed" >&2
exit 2
```

### 5. Make Scripts Executable

```bash
chmod +x scripts/validate-*.sh
chmod +x scripts/run-*.sh
chmod +x scripts/cleanup-*.sh
```

### 6. Test Scripts Independently

```bash
# Test with sample input
echo '{"tool_input":{"command":"test"}}' | ./scripts/validate.sh

# Test with various edge cases
echo '{}' | ./scripts/validate.sh
echo '{"tool_input":{}}' | ./scripts/validate.sh
```

## Matchers

Matchers determine which tool invocations trigger the hook.

### Single Tool

```yaml
matcher: "Bash"  # Matches Bash only
```

### Multiple Tools (OR)

```yaml
matcher: "Edit|Write"  # Matches Edit OR Write
```

### All Tools

```yaml
matcher: ".*"  # Matches any tool (regex)
```

## Advanced Patterns

### Conditional Validation

Different validation based on file type:

```bash
#!/bin/bash
INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

case "$FILE_PATH" in
  *.py)
    # Python-specific validation
    ;;
  *.js)
    # JavaScript-specific validation
    ;;
  *)
    # Default: allow
    exit 0
    ;;
esac
```

### Logging and Metrics

```bash
#!/bin/bash
INPUT=$(cat)
TOOL=$(echo "$INPUT" | jq -r '.tool // empty')

# Log tool usage
echo "$(date): $TOOL used by subagent" >> /tmp/subagent-usage.log

# Continue (non-blocking)
exit 0
```

### Chaining Multiple Hooks

```yaml
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-sql.sh"
        - type: command
          command: "./scripts/log-query.sh"
```

Hooks run in order. If any exits with code 2, the operation is blocked.

## Debugging Hooks

### 1. Check Hook Execution

Add logging to your hooks:

```bash
#!/bin/bash
echo "Hook started: $(date)" >> /tmp/hook-debug.log
INPUT=$(cat)
echo "Input: $INPUT" >> /tmp/hook-debug.log
# ... rest of script
echo "Hook completed" >> /tmp/hook-debug.log
```

### 2. Test Hook Scripts Directly

```bash
# Simulate hook input
cat > test-input.json <<EOF
{
  "event": "PreToolUse",
  "tool": "Bash",
  "tool_input": {
    "command": "SELECT * FROM users"
  }
}
EOF

cat test-input.json | ./scripts/validate-readonly-query.sh
echo "Exit code: $?"
```

### 3. Validate Hook Configuration

Use the validation script:

```bash
scripts/validate_subagent.py .claude/agents/my-agent.md
```

## Troubleshooting

### Hook Not Running

- Check file path in hook configuration is correct
- Ensure script is executable (`chmod +x`)
- Verify matcher matches the tool name exactly
- Check subagent YAML syntax

### Hook Blocking Valid Operations

- Check exit codes (use 0 for allow, 2 for block)
- Verify validation logic with test cases
- Add logging to debug validation decisions

### JSON Parsing Errors

- Install `jq` if not available: `brew install jq` or `apt install jq`
- Test JSON parsing separately
- Handle missing fields with defaults

## Integration with /agents Command

The `/agents` command provides an interactive way to:
- Add hooks to existing subagents
- Edit hook configurations
- Test hook scripts
- View hook execution logs

This skill focuses on manual hook configuration. Use `/agents` for interactive workflows.

## Next Steps

1. Start with simple validation hooks
2. Test thoroughly with edge cases
3. Add automation hooks (linting, testing)
4. Implement cleanup hooks for stateful operations
5. Monitor hook performance and adjust as needed
