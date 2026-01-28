# GitHub CLI Command Reference

Quick reference for gh commands used in code context discovery.

## Authentication

```bash
# Check auth status for all hosts
gh auth status

# Login to enterprise
gh auth login --hostname github.mycompany.com

# Switch between accounts
gh auth switch --hostname github.mycompany.com
```

## Code Search (via API)

The `gh search code` command may not be available in all gh versions. Use the API directly:

```bash
# Basic search via API
gh api "/search/code?q=query"

# Enterprise search
gh api --hostname github.mycompany.com "/search/code?q=query"

# Search within organization (use org: qualifier)
gh api "/search/code?q=query+org:my-org"

# Filter by language (use language: qualifier)
gh api "/search/code?q=query+language:typescript"

# Combine filters with limit
gh api --hostname github.mycompany.com "/search/code?q=handleAuth+org:my-org+language:typescript&per_page=20"
```

**Note:** URL-encode spaces as `+` or `%20` in the query string.

## Repository Content

```bash
# Get file content (base64 encoded)
gh api repos/owner/repo/contents/path/to/file

# Get directory listing
gh api repos/owner/repo/contents/path/to/dir

# Enterprise API
gh --hostname github.mycompany.com api repos/owner/repo/contents/path
```

## Git History

```bash
# Commits for a file
gh api "repos/owner/repo/commits?path=src/file.ts&per_page=10"

# All recent commits
gh api "repos/owner/repo/commits?per_page=20"

# Specific commit details
gh api repos/owner/repo/commits/SHA
```

## Repository Info

```bash
# Get repo metadata
gh repo view owner/repo --json name,description,defaultBranchRef

# Via API (more fields)
gh api repos/owner/repo

# List org repos
gh repo list my-org --limit 50
```

## Search Modifiers

| Modifier | Example | Description |
|----------|---------|-------------|
| `org:` | `org:my-org` | Search within organization |
| `repo:` | `repo:my-org/app` | Search specific repo |
| `path:` | `path:src/` | Filter by file path |
| `extension:` | `extension:ts` | Filter by file extension |
| `filename:` | `filename:config` | Filter by filename |
| `language:` | `language:python` | Filter by language |

## Combining Searches

```bash
# Function definition in TypeScript
gh search code "function authenticate" --language typescript --owner my-org

# Imports of a module
gh search code "import.*from.*@my-org/auth" --language typescript

# Config files only
gh search code "apiKey" --filename config
```

## Rate Limits

```bash
# Check rate limit status
gh api rate_limit

# Enterprise rate limit
gh --hostname github.mycompany.com api rate_limit
```

Rate limits: ~30 searches/minute for code search. Use `--limit` to reduce result count when exploring.
