---
name: comprehension-first-design
description: A product design framework focused on reducing cognitive load (glucose/ATP expenditure) rather than just clicks. Use this when designing onboarding, introducing complex features, or auditing a UI where users drop off due to confusion rather than effort.
---

# Comprehension-First Product Design

Product design is often mistakenly focused on reducing "friction" (the number of clicks or taps). However, for most unique products, the real barrier isn't effort—it's **comprehension**. If a user has to stop and think because they don't understand an option, they feel "stupid," creating an emotional debt that leads to churn.

## Core Principles

### 1. The Owner’s Delusion
Recognize that as a creator, you are "delusional" about the user's level of intent. 
- **The Reality:** Users have low intent, are likely late for a meeting, or are distracted by personal stress. 
- **The Application:** Do not force users to sit through "Ken Burns effect" intros or complex menus. Provide the "Street Address, Phone Number, and Menu" (the core value) immediately.

### 2. Focus on "Don't Make Me Think"
Every decision costs biological energy (glucose/ATP). 
- **Good Design:** 8 clicks that are "trivially easy" and require zero thought (fluidity).
- **Bad Design:** 2 clicks that require a "fraught decision" between poorly defined options.

### 3. Move Up the Utility Curve
Features are not binary; they exist on an S-curve.
- **The Shallow Start:** Initial effort yields zero value (e.g., creating a database table).
- **The Steep Hump:** The "Magic Threshold" where the feature becomes indispensable.
- **The Goal:** Invest enough in a feature to get it over the hump of comprehension so users actually reach the "Aha" moment. If you can't get it over the hump, don't build it.

---

## Tactical Implementation

### Use "Good Friction" for Comprehension
Sometimes, adding a step improves the experience by shaping behavior or preventing regret.
- **The Shouty Rooster Pattern:** When a user is about to do something high-impact (like @channel in a large Slack room), interrupt them with a warning ("This will notify 147 people in 8 time zones"). This "friction" builds comprehension of the tool's power and social cost.

### Apply Smart Defaults
If you don't set a default, most users will never use the feature.
- **Override Hierarchy:** Set a sensible system default (e.g., Do Not Disturb from 8 PM to 8 AM). Allow administrators to override it, and then allow end-users to override that. This introduces the feature to everyone without causing conflict.

### The "Other" Menu Strategy
Avoid "Choice Paralysis" by hiding complexity.
- Identify the top 2-3 most common actions.
- Place everything else behind an "Other" or "More" menu.
- Comparing 3 items is easy; comparing 15 is geometrically more expensive for the brain.

---

## Examples

### Example 1: Onboarding Authentication
**Context:** A user downloads a mobile app and needs to sign in.
**Input:** Traditional Username/Password fields.
**Application:** Apply "Don't Make Me Think." Typing a complex password on a phone is high friction and high cognitive load.
**Output:** Use a **Magic Link**. The user enters an email, clicks a link in their inbox, and the app automatically authenticates. It replaces "remembering/typing" with "clicking a button."

### Example 2: Time Zone Selection
**Context:** A user needs to set an event time in a different time zone.
**Input:** An alphabetical list of all 400+ global time zones.
**Application:** Combat the "Owner's Delusion." Most users only care about 10-12 major zones.
**Output:** Prioritize the 5 most likely zones based on the user's current location and past behavior (e.g., if in SF, show Pacific, Eastern, and London first). Use a sub-menu or search for the "long tail" (e.g., Newfoundland).

---

## Common Pitfalls
- **The Click-Count Trap:** Thinking that "fewer clicks" always equals "better UX." If those fewer clicks require 10 seconds of staring at the screen to understand, you’ve failed.
- **Optimizing "Junk":** Improving a feature that is still in the "shallow" part of the utility curve. If the feature handle is still "breaking on impact," making it slightly prettier doesn't matter.
- **Ignoring the "Stupid" Factor:** Designing icons or labels that require a manual to understand. If a user feels dumb using your software, they will eventually hate it.
- **Regression to Complexity:** Allowing "hyper-realistic work-like activities" (like A/B testing minor UI tweaks) to override clear product intuition. If an A/B test shows a 2% gain but makes the UI more confusing, reject it.