#!/bin/bash
# Deterministic onboarding detection.
# If CLAUDE.local.md is missing, inject a strong signal into context.

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-.}"

if [ ! -f "$PROJECT_DIR/CLAUDE.local.md" ] && [ ! -f "$PROJECT_DIR/.claude/CLAUDE.local.md" ]; then
  cat <<'EOF'
ONBOARDING_NEEDED: No CLAUDE.local.md found.
Shannon works best with your personal context. Start the onboarding flow:
1. Ask the user their name and role
2. Ask what they're working on right now
3. Ask how they like their outputs (concise/detailed, formal/casual)
4. Create CLAUDE.local.md from answers
5. Create their first Brain from answer #2
EOF
else
  echo "Shannon ready."
fi

exit 0
