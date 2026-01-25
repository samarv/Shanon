---
name: landscape-first-product-strategy
description: A framework for drafting a high-conviction product strategy by mapping the market and technical landscape. Use this when facing "not strategic enough" feedback, during annual/quarterly planning, or when proposing a major product pivot.
---

This framework serves as the PM’s "homework" to build confidence in decision-making and align stakeholders through a logical chain of evidence. It shifts the conversation from "I don't agree with your idea" to "I don't agree with this specific point in the landscape."

## The Strategy Document Structure

Draft a comprehensive document (often reaching 10–20 pages) that moves from the high-level mission down to specific execution steps.

### 1. The Strategy Summary (The Minto Lead)
Before the deep dive, provide a one-page executive summary above the fold. 
- State the conclusion first.
- Summarize the top 3 bets.
- List the immediate next steps.

### 2. Context and Mission
- **Company Mission:** State the overarching point of the company.
- **Team Goals:** Define the current quarter's business goals and how your team fits into the larger framing.

### 3. The Landscape (The Evidence Layer)
This is the most critical section for building "strategic" credibility. 
- **Business Health:** Detail what is happening with your current products and business metrics.
- **Market POV:** Define your point of view on the market direction.
- **Competitor Analysis:** Perform a SWOT analysis. Include screenshots of competitor marketing sites or features.
- **Key Risks:** List the primary threats to the business in this space.

### 4. Honest Accounting of the Current State
- **Product Audit:** List what works and what doesn't.
- **Feedback Loop:** Aggregate bottoms-up feedback from support tickets, customer interviews, and sales calls.
- **Technical Hurdles:** Document tech debt, architectural limitations, and engineering "harps" (items the dev team consistently wants to invest in).

### 5. The Opportunity and "Where to Play"
- **Unique Advantage:** Based on the landscape, identify where the company has a unique competitive advantage.
- **The Bet:** Narrow down the 10 possible things you could do to the **top 1–3 opportunities** where you can win.

### 6. Challenges and Assumptions
- **The "What Must Be True" Test:** List the assumptions that must hold for this strategy to succeed.
- **Friction Points:** Identify the hardest parts of taking advantage of the opportunity.

### 7. The Solution and Sequence
- **The Solution:** Write a high-level description of what needs to be built.
- **The Sequence:** If you had no interference, how would you order the work?
- **Resource Needs:** Estimate the cost and team structure required to execute.

## Refinement Tactics

### The "Read Aloud" Test
Read the entire document out loud. If a sentence sounds overcomplicated or unnatural, rewrite it. 
- **Tip:** If you can't explain a section simply in conversation, use the phrase "What I am trying to say is..." and then type exactly what you said.

### The First Page Rule
In many strategy drafts, the first two paragraphs (or the first page) are "crapola" filler. Delete them. Start the document where the actual information begins.

### The Rule of Three
Never present more than three strategic priorities. If you have a fourth, either cut it or merge it into the top three. Anything beyond three dilutes focus and energy.

## Examples

**Example 1: Annual Planning for a Director of Product**
- **Context:** An executive asks for the 12-month roadmap for the "Growth" pillar.
- **Input:** Current churn data, competitor referral programs, and tech debt in the onboarding flow.
- **Application:** The PM maps the "Landscape" showing that while competitors have better referrals, the "Current State" audit shows 40% of users drop off due to a slow onboarding architectural bottleneck.
- **Output:** A strategy that prioritizes an "Onboarding Rewrite" as the primary "Opportunity" for the year, supported by the data in the Landscape section.

**Example 2: Proposing a Major Pivot**
- **Context:** A feature team is "treading water" with low engagement.
- **Input:** 10 user interviews, support tickets, and a new market entrant.
- **Application:** The PM uses the "Landscape" section to show a shift in user behavior documented in recent calls. They use the "What Must Be True" section to argue that the current feature's success assumes a user behavior that no longer exists.
- **Output:** A 15-page "Homework" doc that convinces the VP of Product to reallocate the team to a new opportunity.

## Common Pitfalls
- **Managing via Dashboard Only:** Relying solely on quantitative data without the "Why" from the landscape. You must talk to 10 users to understand the "Why" behind the numbers.
- **Keeping the Doc Secret:** Strategy fails if not shared. Send the draft to your Engineering and Design counterparts first. Invite them to "shred it" before showing it to executives.
- **Overcomplicating Small Features:** Do not use this 20-page framework for minor features. Only use it for high-level pillars, pivots, or annual cycles.
- **Ignoring Technical Debt:** A strategy that doesn't account for "Technical Hurdles" is a fantasy. If the engineers are harping on a specific debt, it must be in the "Current State" section.