---
name: systems-thinking-product-tradeoffs
description: A framework for navigating complex product decisions where multiple user segments and business incentives clash. Use this when a simple "user job" doesn't account for ecosystem health, when you need to prioritize new users over power users, or when business strategy requires making a feature slightly "worse" for a long-term competitive advantage.
---

Systems thinking replaces linear frameworks like Jobs-to-be-Done (JTBD) by analyzing the incentives of every agent in a product ecosystem. Instead of solving for a single user's "job," you balance the competing needs of different groups to ensure the entire system thrives.

## The Systems Thinking Process

### 1. Map the Agents
Identify every party affected by the feature. In social or marketplace products, this usually includes:
- **The New User:** Needs a "cold start" to find value.
- **The Power User:** Wants control, speed, and status.
- **The Business:** Needs data, defensibility, or growth.
- **The Competitor:** Gains if your system is too open or too closed.

### 2. Identify Incentive Clashes
Determine where one agent's "job" makes another's experience worse. 
- *The "People You May Know" Dilemma:* Showing a user a suggestion they didn't ask for (making their feed slightly worse/noisier) to help a new user find their first friend (making the network's retention better).

### 3. Apply the "A to D" Importance Spectrum
Borrowed from Mark Zuckerberg's review style, categorize your conviction on the trade-off:
- **Level A (Do it):** Founder/Exec-level conviction. The system requires this (e.g., algorithmic feeds over chronological).
- **Level B (High Interest):** You want this outcome but are open to being overruled if the team proves the friction is too high.
- **Level C (Low Interest):** Nice to have; the team has autonomy.
- **Level D (No Opinion):** Just an update.

### 4. Look for Psychological Levers (The "Streaks" Model)
Move past functional utility (the milkshake) to psychological retention. Ask: "What is the North Star metric for retention (e.g., Current User Retention Rate) and what 'ritual' drives it?"
- *Example:* Fire emojis and streaks in Duolingo aren't about the "job" of learning a language; they are a psychological system designed to drive a specific behavior.

## Examples

**Example 1: Social Network Onboarding**
- **Context:** A new user joins a platform with no friends.
- **Input:** Traditional JTBD might suggest the "job" is for the user to search for friends.
- **Application:** Use Systems Thinking. Realize the new user needs friends more than the existing user needs a clean notification tab. 
- **Output:** Launch "People You May Know." Even if it annoys the recipient (existing user), it performs the vital job of getting the new user to "10 friends in 14 days," which is the system's threshold for survival.

**Example 2: Competitive Data Privacy (The Amazon/Google Case)**
- **Context:** Deciding what data to include in a customer's shipping confirmation email.
- **Input:** User "job" is to see what is in their package without clicking a link.
- **Application:** Analyze the business incentive. Including the item names in the email gives Google (via Gmail) free data on Amazon's sales and customer preferences.
- **Output:** Make the user experience slightly worse (hide item names behind a link) to protect the business's long-term competitive moat.

## Common Pitfalls

- **The Power User Trap:** Over-optimizing for your most vocal users. Power users often prefer systems that are hard for new users to navigate because it protects their status/expertise.
- **Idealistic Product Building:** Assuming every feature must be a "win-win." Real-world product management at scale is almost always about "win-lose-win" (losing on one metric to win on a more important one).
- **Inheriting Decisions:** Failing to use "First Principles." Ask: "If the product didn't exist today, would we build it this way, or are we just carrying over old trade-offs that no longer apply?"
- **Using Linear Frameworks for Non-Linear Systems:** JTBD works for milkshakes (single user, single transaction); it fails for networks where one user's action affects 100 others.