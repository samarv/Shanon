# Name Verification Protocol

Protocol for verifying and correcting colleague names in meeting transcripts.

---

## Purpose

Transcription services often misspell or mishear names. Use `input/org/colleagues.json` to verify and correct names.

---

## When to Trigger Verification

**Check a name against colleagues.json when:**
- Name spelling looks phonetically plausible but unusual
- Name doesn't match any known colleague exactly
- Name appears in action item owner or stakeholder context
- Transcription shows hesitation markers near names

**Common transcription errors:**
| Transcribed | Error Type |
|-------------|------------|
| Missing special characters | Øyvind → "Oyvind" |
| Phonetic mishearing | Inderberg → "Innerberg" |
| C/K confusion | Carl → "Karl" |
| Partial names | Full name → first name only |

---

## Verification Process

```
1. Extract all names mentioned in transcript
2. For each name:
   a. Check exact match in colleagues.json → Use as-is
   b. If no exact match:
      - Check commonAliases in colleagues.json
      - Search for phonetically similar names
      - Look in relevant team context
   c. If match found with high confidence → Auto-correct
   d. If uncertain → Flag for user verification
```

---

## Using colleagues.json

**Structure quick reference:**
- `lookup.commonAliases`: Maps nicknames/shortened names to full names
- `lookup.userContext`: Current user's info
- Division teams contain `directReports` arrays

**Search order (for user's org context):**
1. Immediate team directReports
2. Broader team
3. Division
4. Full organization

---

## Correction Format

**Auto-corrected** (high confidence):
Just use the correct name, no notation needed.

**Uncertain correction**:
Note original: "[Corrected from: original transcription]"

---

## Verification Prompt

For each suspicious name, ask:
```
Does '[transcribed name]' match any colleague in colleagues.json?
1. Exact match?
2. Phonetic similarity to known colleagues?
3. Context clues (team mentioned, reporting relationship)?

If match found, use correct spelling. If uncertain, flag for user.
```

---

## Do NOT Verify

Skip verification for:
- External participants (customers, partners) not in org
- Generic references ("the team", "engineering")
- Names that exactly match colleagues.json entries

---

## Integration with Speaker Attribution

When attribution inference suggests a name:
1. Check against `input/org/colleagues.json`
2. Verify role/team alignment
3. If match found → Use correct spelling
4. If uncertain → Include both inference and verification question

---

## Anti-Patterns

- ❌ Using transcribed names verbatim when they look misspelled
- ❌ Guessing name corrections without checking colleagues.json
- ❌ Correcting names that are already correct
- ❌ Verifying every name (only check suspicious ones)
- ✅ Check colleagues.json when spelling seems off
- ✅ Use phonetic similarity to find likely matches
- ✅ Flag uncertain corrections for user verification
