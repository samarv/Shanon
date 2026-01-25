---
name: opportunity-framing
description: Frame customer opportunities as unmet needs, pain points, and desires rather than solutions. Use when writing opportunities for an Opportunity Solution Tree, validating opportunity statements, or training teams to distinguish problems from solutions. CRITICAL for avoiding the #1 OST failure - "98% of people write opportunities as solutions" (Teresa Torres). Triggers when user asks to "frame opportunities", "write opportunities", "validate opportunity statements", or "check if this is a need vs solution".
---

# Opportunity Framing

Transform feature requests and customer feedback into actionable, specific opportunities that represent true customer needs.

## Core Principle

**Opportunities are needs, not solutions.**

The #1 failure mode: "98% of people that write opportunities write them as solutions." - Teresa Torres

## Good vs Bad Opportunities

### Bad (Solutions Disguised as Needs)
- "We need a better login experience"
- "We need voice input for passwords"
- "I wish this was easier to use"
- "Add a calendar view"
- "Implement dark mode"

### Good (Specific Customer Needs)
- "It's hard to enter my password - selecting specific letters on the screen with the Apple TV remote"
- "I can't see who's in the cast before I start watching"
- "I don't know if this show is good without watching 3 episodes first"
- "I lose track of where I was when switching between devices"
- "I can't tell if I've already watched this episode"

## Quality Tests

Apply ALL three tests to validate an opportunity:

### Test 1: Is it specific and actionable?
- Bad: "Navigation is confusing" (too vague)
- Good: "I can't find the search button on the main screen" (specific)

### Test 2: Does it describe the problem, not the solution?
- Bad: "We need better filters" (solution)
- Good: "I can't narrow down results by release date" (problem)

### Test 3: Is it grounded in a real customer story?
- Bad: "Users want faster load times" (assumption)
- Good: "I gave up waiting for the page to load and closed the app" (story-based)

## Framing Process

### Step 1: Listen for the raw input
Customer says: "I wish there was a way to skip the intro automatically."

### Step 2: Strip away the solution language
Solution words to remove: "add", "implement", "build", "create", "should have", "I wish there was"

### Step 3: Find the underlying need
Ask: "What problem would that solution solve?"
Answer: "I waste time clicking 'skip intro' for every episode when binge-watching"

### Step 4: Make it specific
Generic: "Binge-watching is tedious"
Specific: "I have to click 'skip intro' 6+ times per hour when binge-watching a series"

### Step 5: Validate with the story
Can you trace this back to a real customer moment?
Yes: "Tell me about the last time you binge-watched something..."

## Vertical Depth Pattern

Opportunities should get smaller and more actionable as you move down the tree:

**Level 1 (Big)**: "I can't decide what to watch"

**Level 2 (Smaller)**: "I don't know if this show is good"

**Level 3 (Actionable)**: "I can't see who's in the cast"

Each level down should:
- Be more specific than the level above
- Be a contributing factor to the parent opportunity
- Be actionable enough to generate multiple solution ideas

## Red Flags

Watch for these indicators that you've written a solution, not an opportunity:

- Contains implementation language ("add", "build", "implement", "create")
- Describes a feature name or UI pattern ("dashboard", "calendar view", "notifications")
- Uses "should/could/would have" phrasing
- Lacks specificity (could apply to any product)
- Not traceable to a specific customer story
- Describes HOW rather than WHY or WHAT

## Transformation Examples

### Example 1: E-commerce
**Raw input**: "We need product recommendations"
**Bad opportunity**: "Users want personalized recommendations"
**Good opportunity**: "I don't know what else to buy after adding one item to my cart"

### Example 2: SaaS Tool
**Raw input**: "Add keyboard shortcuts"
**Bad opportunity**: "Power users need keyboard shortcuts"
**Good opportunity**: "I waste 5+ seconds per action reaching for my mouse when I'm in flow state"

### Example 3: Mobile App
**Raw input**: "Implement offline mode"
**Bad opportunity**: "Users need offline access"
**Good opportunity**: "I lose my work when I go through a tunnel on my commute"

## Common Patterns

### Pattern: "I wish there was..."
This is ALWAYS a solution in disguise.
1. Ask: "What problem does that solve?"
2. Ask: "Tell me about the last time you experienced that problem"
3. Write the opportunity from the story

### Pattern: Stakeholder feature requests
"Build feature X" → "Why?" → "To solve Y" → "Tell me about Y"

Example:
- Request: "Build a calendar view"
- Why?: "To help users see their schedule"
- Problem: "I can't tell if I'm double-booked without checking 3 different places"

## Validation Checklist

Before finalizing an opportunity, confirm:

- [ ] Written as a customer need, not a solution
- [ ] Specific and concrete (mentions actual UI, steps, or context)
- [ ] Traceable to a real customer story/interview
- [ ] Actionable (could generate 3+ different solution ideas)
- [ ] At appropriate depth (not too broad, not too narrow)
- [ ] No implementation language (add/build/implement/create)
- [ ] Passes all 3 quality tests above

## Working with Experience Maps

Opportunities should be organized by the customer's journey phases:

**Netflix Example:**
1. Trigger (deciding to watch something)
   - "I don't know what I'm in the mood for"
   - "I don't have much time and need something short"
2. Choosing what to watch
   - "I can't see who's in the cast"
   - "I don't know if this matches my mood"
3. Evaluating if it's good
   - "I can't tell if it's good without watching 3 episodes"
4. The viewing experience
   - "I have to click skip intro 6+ times per hour"
5. Post-viewing experience
   - "I forget what happened in previous seasons"

Each phase contains specific needs and pain points.

## Anti-Patterns

### "I want" vs "I can't"
- Bad: "I want to customize my dashboard" (expresses desire)
- Good: "I can't see my most important metrics without scrolling" (expresses problem)

### Generic vs Specific
- Bad: "The app is slow" (generic)
- Good: "The search results take 8+ seconds to load on my phone" (specific)

### Feature vs Need
- Bad: "Users need a dark mode" (feature)
- Good: "The bright screen hurts my eyes when using the app at night" (need)

## Coaching Prompts

When helping others frame opportunities, use these prompts:

1. "Can you tell me about a specific time when you experienced that?"
2. "What happened? Walk me through it step by step."
3. "What were you trying to do?"
4. "What made that difficult/frustrating?"
5. "What did you do next?"
6. "How did that feel?"

## Reference: Teresa Torres' Quality Standard

> "I've seen blog posts written about how they're using the opportunity solution tree, and I cry a little bit because their opportunity space is all solutions. I don't want to knock down somebody's blog post, but I also don't want this bad example out there in the world."

The bar is high. When in doubt:
1. Read the opportunity statement out loud
2. Ask: "Is this describing WHAT the customer is trying to do or HOW we might solve it?"
3. If there's any trace of HOW, rewrite it

## Output Format

When framing opportunities, use this format:

```
Opportunity: [Customer need statement in first person]
Evidence: [Quote or story from customer interview]
Context: [Journey phase this belongs to]
Parent opportunity: [If this is a sub-opportunity]
Confidence: [High/Medium/Low based on # of customer stories]
```

Example:
```
Opportunity: "I can't tell if I'm double-booked without checking 3 different places"
Evidence: "Last week I showed up to two meetings at the same time because my work calendar, personal calendar, and the team's shared calendar weren't synced." - User Interview #7
Context: Schedule management / Planning phase
Parent opportunity: "I can't manage my time effectively across multiple calendars"
Confidence: High (heard from 8/10 interview participants)
```
