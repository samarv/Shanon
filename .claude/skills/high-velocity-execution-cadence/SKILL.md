---
name: high-velocity-execution-cadence
description: A system for driving organizational intensity and output by shortening feedback loops, using high-fidelity demos, and implementing aggressive meeting audits. Use this when velocity is stalling, when team alignment is drifting, or when recurring meetings are crowding out "craft" time.
---

Maximize organizational output by increasing "kilojoules per minute" rather than total hours worked. This framework shifts leadership from passive oversight to active "problem-pairing" through specific cadences and high-fidelity communication.

## The Execution Rhythm

Implement these four overlapping cadences to maintain urgency and ensure leaders are unblocking teams in real-time.

### 1. Weekly "GSD" (Get Shit Done) Updates
Require every project lead to post a weekly update accessible to the entire organization.
*   **Prioritize Demos over Text:** Use video screen shares or "Spin" environments (internal dev environments) to show the actual product experience.
*   **Include Friction Logs:** Have PMs or leads record themselves using the product and narrating pain points.
*   **Force Progression:** Use the update to trigger "OK1" (director-level alignment) and "OK2" (VP-level architecture alignment) reviews immediately rather than waiting for monthly meetings.

### 2. Six-Week Review Cycles
Move away from quarterly or annual planning in favor of six-week deep dives.
*   **Focus on Unblocking:** These are not status reports. The goal is for leadership to identify where infra is missing or where a team is "wayfinding" (searching for a solution) instead of "building."
*   **Resource Realignment:** If a project is failing or the "trust battery" with a lead is low, use the six-week mark to pivot resources or change the approach.

### 3. Annual Meeting Armageddon
Once a year, at a random interval, delete every recurring meeting in the organization.
*   **The Criteria:** Delete all recurring meetings with more than two people that are internal-only.
*   **The Moratorium:** Ban the re-addition of recurring meetings for two weeks. 
*   **The Goal:** Force teams to justify the necessity of a meeting. Aim for individual contributors (ICs) to spend fewer than 3 hours per week in meetings.

### 4. Micromanagement as "Pairing"
Redefine management as an active, hands-on activity.
*   **Pair on Problems:** Instead of asking "Is it done?", ask "Can I work on this specific problem with you?" 
*   **Remove Infrastructure Blockers:** If a team is blocked by a third party or a technical limit, the leader should intervene immediately (e.g., messaging an API partner to increase context limits) rather than letting the team "chunk" the data to work around it.

## Technical Intensity Tactics

*   **The 1-Hour Design Rule:** When pair programming on a new feature, set a timer for one hour. If the problem isn't solved or the code isn't written in that hour, delete all the code, keep the tests, and start over. This forces the team to find a more elegant, simple design.
*   **Delete Code Club:** Regularly prioritize "deleting code" over "adding features." Simple codebases are more resilient and faster to change. Target deleting at least 10% of new code volume annually to reduce technical debt.
*   **Infrastructure over Features:** If a feature will take two weeks to build, but building a platform to allow *anyone* to build that feature in an hour takes two months, choose the two-month path. This is "putting gas in the tank" for future velocity.

## Examples

**Example 1: Unblocking via Executive Pairing**
*   **Context:** A team is building an AI-driven tool but is struggling because the LLM provider has a small output context window. The team is planning a 3-week "chunking" workaround.
*   **Application:** During a high-fidelity review, the lead identifies the bottleneck. Instead of approving the 3-week delay, the lead messages the LLM provider directly to request an undocumented limit increase.
*   **Output:** The limit is increased within an hour, the workaround is scrapped, and the feature ships two weeks early.

**Example 2: The Six-Week Pivot**
*   **Context:** A team is building a new point-of-sale (POS) interface. They are six weeks into a 6-month roadmap.
*   **Application:** During the six-week review, the team shares a video demo. Leadership notices the UI latency is high because of a "hedged" architectural choice (using two different frameworks for iOS and Android).
*   **Output:** Leadership directs the team to "choose the hard path"—delete the fragmented code and rebase everything onto a single high-performance framework (e.g., React Native), saving 18 months of future maintenance.

## Common Pitfalls

*   **Hedging Decisions:** Choosing a "middle ground" to reduce risk (e.g., building two versions of a product to see which works). This usually doubles the work and halves the velocity. Take the riskier, unified path instead.
*   **Status-Only Meetings:** Allowing reviews to become "theatre" where teams show green checkboxes. If there is no "pairing" on problems or "deleting" of bad ideas, the meeting is a waste.
*   **Sunk Cost Fallacy:** Refusing to delete code because "we spent months on it." If the design is wrong, deleting it immediately is the only way to regain velocity.
*   **Passive Leadership:** Assuming that "hiring smart people" means you should never look at their work. High intensity requires leaders to stay "API compatible" with the craft.