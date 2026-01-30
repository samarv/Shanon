---
name: gh-code-context
description: Search and discover code context across GitHub Enterprise organizations using gh CLI. Use when needing to find code implementations, understand how functions are used, trace dependencies, or gather context about deployed/developed code across multiple repositories. Triggers on requests like "find where X is implemented", "how is Y used across repos", "show me the auth code", or "find context for this feature".
---

# GitHub Code Context Discovery

Search for code across GitHub Enterprise and gather comprehensive context including file structure, git history, related files, and usage patterns.

## Prerequisites

Verify gh CLI authentication before any search:

```bash
gh auth status
```

Expected: Logged in to target host (github.com or your enterprise host).

If not authenticated, run `gh auth login --hostname <host>`.

## Workflow Decision Tree

```
User request about code
         │
         ▼
┌─────────────────────┐
│ What type of search?│
└─────────────────────┘
         │
    ┌────┼────┬────────────┐
    ▼    ▼    ▼            ▼
  Find  Find  Find      Understand
  code  usage related   file deeply
    │    │    files        │
    ▼    ▼    ▼            ▼
 search find_ search    get_file_
 _code  usages _code    context
   .sh   .sh    .sh       .sh
```

## Phase 1: Search - Find Relevant Code

Run `scripts/search_code.sh` to locate code matching the query.

```bash
# Basic search across enterprise
./scripts/search_code.sh "functionName" --host github.mycompany.com --org org-name

# With language filter
./scripts/search_code.sh "class AuthService" --host github.mycompany.com --language typescript --limit 20
```

**Options:**
- `--host`: GitHub hostname (e.g., github.mycompany.com for enterprise)
- `--org`: Organization to search within
- `--language`: Filter by programming language
- `--limit`: Max results (default: 10)

For query construction patterns, see [references/query-patterns.md](references/query-patterns.md).

## Phase 2: Expand - Get File Context

Once a relevant file is found, run `scripts/get_file_context.sh` for deep context.

```bash
./scripts/get_file_context.sh owner/repo src/path/to/file.ts --host github.mycompany.com
```

**Returns:**
- Full file content
- Directory structure (sibling files)
- Recent commits (last 5)
- Contributors list
- Repository metadata

## Phase 3: Trace - Find Usages

To understand how code is used elsewhere, run `scripts/find_usages.sh`.

```bash
# Find all usages of a symbol
./scripts/find_usages.sh "AuthService" --host github.mycompany.com --org org-name

# Exclude the definition file itself
./scripts/find_usages.sh "handleSubmit" --exclude-def --limit 30
```

**Options:**
- `--exclude-def`: Filter out files likely containing the definition
- `--limit`: Max results (default: 15)

## Common Workflows

### "Find where X is implemented"

1. Search for definition: `./scripts/search_code.sh "function X" --host github.mycompany.com`
2. Get context: `./scripts/get_file_context.sh repo path/file.ts --host github.mycompany.com`

### "How is Y used across our codebase"

1. Find usages: `./scripts/find_usages.sh "Y" --host github.mycompany.com --org org-name`
2. For each significant usage, get context if needed

### "Show me the auth/feature code"

1. Search broadly: `./scripts/search_code.sh "auth" --host github.mycompany.com --org org-name --limit 30`
2. Identify key files from results
3. Get deep context for main implementation file

### "Understand this file's context"

1. Direct context: `./scripts/get_file_context.sh owner/repo path/file.ts --host github.mycompany.com`
2. Find usages if it exports functions: `./scripts/find_usages.sh "exportedFunction" --host github.mycompany.com`

## Enterprise Host Reference

| Host | Usage |
|------|-------|
| `github.com` | Public/personal repos (default) |
| `github.mycompany.com` | Enterprise repos (example) |

Always specify `--host <your-enterprise-host>` for enterprise searches.

## Resources

- [gh-commands.md](references/gh-commands.md) - Quick reference for gh CLI commands
- [query-patterns.md](references/query-patterns.md) - Common search query patterns

## Troubleshooting

**"No results found"**
- Check auth: `gh auth status`
- Verify org name spelling
- Try broader search terms
- Check language filter matches actual file extensions

**"Rate limit exceeded"**
- Wait 1 minute, then retry
- Use smaller `--limit` values
- Check: `gh api rate_limit`

**"Could not resolve host"**
- Run: `gh auth login --hostname <your-enterprise-host>`
