#!/usr/bin/env bash
#
# get_file_context.sh - Get comprehensive context for a file in a repository
#
# Usage:
#   get_file_context.sh <owner/repo> <file_path> [--host <hostname>]
#
# Examples:
#   get_file_context.sh my-org/my-app src/utils/auth.ts --host github.mycompany.com
#   get_file_context.sh my-org/my-repo lib/service.py

set -euo pipefail

# Defaults
HOST=""
REPO=""
FILE_PATH=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --host)
            HOST="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage: get_file_context.sh <owner/repo> <file_path> [--host <hostname>]"
            echo ""
            echo "Options:"
            echo "  --host   GitHub hostname (e.g., github.mycompany.com)"
            exit 0
            ;;
        *)
            if [[ -z "$REPO" ]]; then
                REPO="$1"
            elif [[ -z "$FILE_PATH" ]]; then
                FILE_PATH="$1"
            fi
            shift
            ;;
    esac
done

if [[ -z "$REPO" ]] || [[ -z "$FILE_PATH" ]]; then
    echo "Error: Repository and file path required" >&2
    exit 1
fi

# Build base gh args
GH_ARGS=("api")
if [[ -n "$HOST" ]]; then
    GH_ARGS+=("--hostname" "$HOST")
fi

DIR_PATH=$(dirname "$FILE_PATH")
if [[ "$DIR_PATH" == "." ]]; then
    DIR_PATH=""
fi

echo "# File Context: $REPO/$FILE_PATH"
echo "# Host: ${HOST:-github.com}"
echo ""

# 1. Get file content
echo "## File Content"
echo '```'
CONTENT=$(gh "${GH_ARGS[@]}" "repos/$REPO/contents/$FILE_PATH" 2>/dev/null) || {
    echo "(Unable to fetch file content)"
    CONTENT=""
}
if [[ -n "$CONTENT" ]]; then
    echo "$CONTENT" | jq -r '.content // empty' | base64 -d 2>/dev/null || echo "(Could not decode content)"
fi
echo '```'
echo ""

# 2. Get directory structure (siblings)
echo "## Directory Structure"
if [[ -n "$DIR_PATH" ]]; then
    echo "Path: $DIR_PATH/"
    gh "${GH_ARGS[@]}" "repos/$REPO/contents/$DIR_PATH" 2>/dev/null | jq -r '.[]? | "  " + (if .type == "dir" then "[dir]  " else "[file] " end) + .name' || echo "(Unable to fetch directory)"
else
    echo "Path: / (root)"
    gh "${GH_ARGS[@]}" "repos/$REPO/contents" 2>/dev/null | jq -r '.[]? | "  " + (if .type == "dir" then "[dir]  " else "[file] " end) + .name' || echo "(Unable to fetch directory)"
fi
echo ""

# 3. Get recent commits for this file
echo "## Recent Commits (last 5)"
gh "${GH_ARGS[@]}" "repos/$REPO/commits?path=$FILE_PATH&per_page=5" 2>/dev/null | jq -r '.[]? | "- " + .sha[0:7] + " " + (.commit.message | split("\n")[0])[0:60] + " (" + .commit.author.name + ", " + .commit.author.date[0:10] + ")"' || echo "(Unable to fetch commits)"
echo ""

# 4. Get contributors
echo "## Contributors"
gh "${GH_ARGS[@]}" "repos/$REPO/commits?path=$FILE_PATH&per_page=20" 2>/dev/null | jq -r '[.[]? | .commit.author.name] | unique | .[]' || echo "(Unable to fetch contributors)"
echo ""

# 5. Repository info
echo "## Repository Info"
gh "${GH_ARGS[@]}" "repos/$REPO" 2>/dev/null | jq -r '"Name: " + .name + "\nDescription: " + (.description // "N/A") + "\nDefault branch: " + .default_branch + "\nLanguage: " + (.language // "N/A") + "\nLast updated: " + .updated_at[0:10]' || echo "(Unable to fetch repo info)"
