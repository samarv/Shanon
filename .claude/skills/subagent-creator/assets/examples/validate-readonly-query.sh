#!/bin/bash
# Validates that SQL queries are read-only (SELECT only)
# 
# This script is referenced by the db-reader subagent example.
# It demonstrates how to use PreToolUse hooks to validate operations.
#
# Usage: Hook automatically passes JSON via stdin
# Exit codes:
#   0 - Allow operation
#   1 - Log error but allow
#   2 - Block operation

# Read JSON input from stdin
INPUT=$(cat)

# Extract the command field from tool_input using jq
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# If no command, allow (nothing to validate)
if [ -z "$COMMAND" ]; then
  exit 0
fi

# Check for write operations (case-insensitive)
WRITE_OPS='INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|TRUNCATE|REPLACE|MERGE'
if echo "$COMMAND" | grep -iE "\b($WRITE_OPS)\b" > /dev/null; then
  # Write error message to stderr (shown to subagent)
  echo "Blocked: Write operations not allowed. Use SELECT queries only." >&2
  # Exit code 2 blocks the operation
  exit 2
fi

# Allow the operation
exit 0
