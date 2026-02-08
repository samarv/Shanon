---
name: people-profile-builder
description: Create and maintain individual colleague communication profiles in Markdown. Use when the user wants to document a person's communication style, tone preferences, decision style, sensitivities, channels, response cadence, or examples of good vs bad communication, and store it as a per-person profile under content/org/profiles/.
---

# People Profile Builder

## Overview

Create or update a per-person profile to help tailor communication and collaboration. Profiles are stored as Markdown files in `content/org/profiles/` using a consistent template.

## Workflow

### 1) Identify the person

- Use `content/org/colleagues.json` to confirm the canonical name and any aliases.
- If the name is ambiguous or missing, ask one question at a time until clear.
- Do not invent details; only use user-provided information.

### 2) Determine the file path

Store each profile at:

`content/org/profiles/<slug>.md`

Slug rules:

- Lowercase
- Spaces to hyphens
- Remove diacritics (for ascii-only filenames)
- Example: `Samarvir Bhayana` -> `samarvir-bhayana.md`

### 3) Create or update the profile

- If the file does not exist, create it using the template below.
- If it exists, update only the relevant sections and preserve existing content.
- If a section has no information yet, leave a `- TBD` placeholder.

## Profile Template

```
# <Full Name>

## Overview
- Role:
- Team:
- Relationship:

## Communication Style
- 

## Tone Preferences
- 

## Decision Style
- 

## Motivations
- 

## Sensitivities / Watch-outs
- 

## Preferred Channels
- 

## Response Cadence
- 

## Working With Them
- 

## Good Communication Examples
- 

## Bad Communication Examples
- 

## Notes / Examples
- 
```
