#!/usr/bin/env bash
#
# find_usages.sh - Find where a symbol (function, class, variable) is used across repos
#
# Usage:
#   find_usages.sh <symbol> [--host <hostname>] [--org <org>] [--exclude-def] [--limit <n>]
#
# Examples:
#   find_usages.sh "UserAuthService" --host github.mycompany.com --org my-org
#   find_usages.sh "handleSubmit" --exclude-def --limit 30
#   find_usages.sh "import { Button }" --org my-org

set -euo pipefail

# Defaults
HOST=""
ORG=""
EXCLUDE_DEF=false
LIMIT=15
SYMBOL=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --host)
            HOST="$2"
            shift 2
            ;;
        --org)
            ORG="$2"
            shift 2
            ;;
        --exclude-def)
            EXCLUDE_DEF=true
            shift
            ;;
        --limit)
            LIMIT="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage: find_usages.sh <symbol> [--host <hostname>] [--org <org>] [--exclude-def] [--limit <n>]"
            echo ""
            echo "Options:"
            echo "  --host        GitHub hostname (e.g., github.mycompany.com)"
            echo "  --org         Organization to search within"
            echo "  --exclude-def Exclude likely definition files (files matching symbol name)"
            echo "  --limit       Maximum results (default: 15)"
            exit 0
            ;;
        *)
            if [[ -z "$SYMBOL" ]]; then
                SYMBOL="$1"
            else
                SYMBOL="$SYMBOL $1"
            fi
            shift
            ;;
    esac
done

if [[ -z "$SYMBOL" ]]; then
    echo "Error: Symbol to search for is required" >&2
    exit 1
fi

# Build search query
SEARCH_QUERY="$SYMBOL"

if [[ -n "$ORG" ]]; then
    SEARCH_QUERY="$SEARCH_QUERY org:$ORG"
fi

# URL encode the query
ENCODED_QUERY=$(printf '%s' "$SEARCH_QUERY" | jq -sRr @uri)

# Build gh API args
GH_ARGS=("api")
if [[ -n "$HOST" ]]; then
    GH_ARGS+=("--hostname" "$HOST")
fi
GH_ARGS+=("/search/code?q=${ENCODED_QUERY}&per_page=${LIMIT}")

echo "# Finding usages of: $SYMBOL"
echo "# Host: ${HOST:-github.com}"
[[ -n "$ORG" ]] && echo "# Scope: $ORG"
echo ""

# Execute search
RESULT=$(gh "${GH_ARGS[@]}" 2>&1) || {
    echo "Error executing search: $RESULT" >&2
    exit 1
}

TOTAL=$(echo "$RESULT" | jq -r '.total_count // 0')
echo "# Total matches: $TOTAL"
echo ""

if [[ "$EXCLUDE_DEF" == "true" ]]; then
    # Filter out files that likely contain the definition
    SYMBOL_LOWER=$(echo "$SYMBOL" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]//g')
    echo "$RESULT" | jq -r --arg sym "$SYMBOL_LOWER" '
      .items[]? | 
      select((.path | ascii_downcase | gsub("[^a-z0-9]"; "")) | contains($sym) | not) |
      "## " + .repository.full_name + "/" + .path + "\n" +
      "URL: " + .html_url + "\n"
    '
else
    echo "$RESULT" | jq -r '
      .items[]? | 
      "## " + .repository.full_name + "/" + .path + "\n" +
      "URL: " + .html_url + "\n"
    '
fi

echo ""
echo "# Summary"
echo "$RESULT" | jq -r '
  "Repositories found: " + ([.items[]? | .repository.full_name] | unique | join(", "))
'
