#!/bin/bash
# Logs minimal session activity for system-evolution pattern detection.
# Runs async on Stop -- non-blocking, append-only.

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-.}"
LOG_FILE="$PROJECT_DIR/.claude/session-log.jsonl"

BRAINS_TOUCHED=""
if [ -d "$PROJECT_DIR/Brains" ]; then
  BRAINS_TOUCHED=$(find "$PROJECT_DIR/Brains" -name "*.md" -newer "$LOG_FILE" 2>/dev/null | head -10 | tr '\n' ',' | sed 's/,$//')
fi

OUTPUT_FILES=""
if [ -d "$PROJECT_DIR/output" ]; then
  OUTPUT_FILES=$(find "$PROJECT_DIR/output" -type f -newer "$LOG_FILE" 2>/dev/null | head -10 | tr '\n' ',' | sed 's/,$//')
fi

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

echo "{\"ts\":\"$TIMESTAMP\",\"brains_touched\":\"$BRAINS_TOUCHED\",\"output_files\":\"$OUTPUT_FILES\"}" >> "$LOG_FILE"

exit 0
