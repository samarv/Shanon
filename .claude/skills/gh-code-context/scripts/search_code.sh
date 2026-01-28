#!/usr/bin/env bash
#
# search_code.sh - Search for code across GitHub Enterprise organizations using API
#
# Usage:
#   search_code.sh <query> [--host <hostname>] [--org <org>] [--language <lang>] [--limit <n>]
#
# Examples:
#   search_code.sh "function handleAuth" --host github.mycompany.com --org my-org
#   search_code.sh "class UserService" --language typescript --limit 20
#   search_code.sh "import React" --org my-org --language tsx

set -euo pipefail

# Defaults
HOST=""
ORG=""
LANGUAGE=""
LIMIT=10
QUERY=""

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
        --language)
            LANGUAGE="$2"
            shift 2
            ;;
        --limit)
            LIMIT="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage: search_code.sh <query> [--host <hostname>] [--org <org>] [--language <lang>] [--limit <n>]"
            echo ""
            echo "Options:"
            echo "  --host      GitHub hostname (e.g., github.mycompany.com). Defaults to github.com"
            echo "  --org       Organization to search within"
            echo "  --language  Filter by programming language"
            echo "  --limit     Maximum results to return (default: 10)"
            exit 0
            ;;
        *)
            if [[ -z "$QUERY" ]]; then
                QUERY="$1"
            else
                QUERY="$QUERY $1"
            fi
            shift
            ;;
    esac
done

if [[ -z "$QUERY" ]]; then
    echo "Error: Search query required" >&2
    echo "Usage: search_code.sh <query> [--host <hostname>] [--org <org>] [--language <lang>]" >&2
    exit 1
fi

# Build search query with qualifiers
SEARCH_QUERY="$QUERY"

if [[ -n "$ORG" ]]; then
    SEARCH_QUERY="$SEARCH_QUERY org:$ORG"
fi

if [[ -n "$LANGUAGE" ]]; then
    SEARCH_QUERY="$SEARCH_QUERY language:$LANGUAGE"
fi

# URL encode the query
ENCODED_QUERY=$(printf '%s' "$SEARCH_QUERY" | jq -sRr @uri)

# Build gh API args
GH_ARGS=("api")
if [[ -n "$HOST" ]]; then
    GH_ARGS+=("--hostname" "$HOST")
fi
GH_ARGS+=("/search/code?q=${ENCODED_QUERY}&per_page=${LIMIT}")

echo "# Searching: $QUERY"
echo "# Host: ${HOST:-github.com}"
[[ -n "$ORG" ]] && echo "# Organization: $ORG"
[[ -n "$LANGUAGE" ]] && echo "# Language: $LANGUAGE"
echo ""

# Execute search and format results
RESULT=$(gh "${GH_ARGS[@]}" 2>&1) || {
    echo "Error executing search: $RESULT" >&2
    exit 1
}

# Check if we got results
TOTAL=$(echo "$RESULT" | jq -r '.total_count // 0')
echo "# Found: $TOTAL matches (showing up to $LIMIT)"
echo ""

# Format output
echo "$RESULT" | jq -r '
  .items[]? | 
  "## " + .repository.full_name + "/" + .path + "\n" +
  "Repository: " + .repository.full_name + "\n" +
  "File: " + .path + "\n" +
  "URL: " + .html_url + "\n" +
  "Score: " + (.score | tostring) + "\n"
'
