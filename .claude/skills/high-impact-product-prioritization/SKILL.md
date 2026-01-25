---
name: high-impact-product-prioritization
description: Identify and scope high-value product bets by bypassing early estimation traps. Use this when your roadmap is cluttered with incremental tasks, when teams are "playing it safe" due to technical uncertainty, or when engineering estimates are stalling innovative ideas.
---

Move past incrementalism by prioritizing for Reach and Impact first, then using "Appetite-based" scoping to force creative engineering solutions.

## Phase 1: The "No-C/E" Prioritization Hack
Standard RICE (Reach, Impact, Confidence, Effort) often kills innovation because high-impact ideas naturally have lower Confidence and higher perceived Effort.

1.  **Isolate R and I:** List all potential product bets. Score them *only* on Reach and Impact.
2.  **Ignore Confidence and Effort:** Temporarily remove "C" and "E" from the equation to prevent premature de-prioritization of "big" ideas.
3.  **The "One-Week Deep Dive":** Take the top 3-5 Reach/Impact bets. Give a cross-functional team (PM, Eng, Design) one week to explore these ideas earnestly.
4.  **Re-evaluate:** After one week of "making yes work," the team will have a much clearer understanding of actual Confidence and Effort. Now, add those scores back in to make a final decision.

## Phase 2: Appetite-Based Scoping
Shift from asking "How long will this take?" (Estimation) to "How much are we willing to spend?" (Appetite).

1.  **Set the Time-Box:** Determine a fixed "appetite" for a problem (e.g., "We are willing to spend 6 weeks on Cohort Analytics").
2.  **Apply the Scoping Hammer:** Instead of cutting quality, cut scope. Force the team to define what a *complete* solution looks like within that specific time-box.
3.  **The "Three-Window" Exercise:** Ask the team:
    *   "What does a complete solution look like in 4 weeks?"
    *   "What does it look like in 6 weeks?"
    *   "What does it look like in 8 weeks?"
4.  **Find the Efficient Frontier:** Choose the window that provides the highest impact-to-cost ratio and commit to not exceeding that time-box.

## Examples

**Example 1: Advanced Visualization Tool**
*   **Context:** The team wants to build a complex interactive chart. Early engineering estimates are "3-4 months," so it keeps getting buried.
*   **Application:** The PM sets a "6-week appetite." The team uses the "Scoping Hammer" to realize they can ship a highly valuable version by using a specific open-source library and limiting initial interactions to "Click-to-Filter" only.
*   **Output:** A high-impact feature is shipped in 6 weeks instead of being ignored for months.

**Example 2: Data Quality Dashboard**
*   **Context:** Customers are complaining about data trust. The solution seems massive and "un-estimatable."
*   **Application:** The team ignores C and E for one week. During the deep dive, an engineer discovers they can leverage existing server logs rather than building a new tracking ingestion service.
*   **Output:** The Confidence score jumps from 0.2 to 0.8, and the project is prioritized for the next sprint.

## Common Pitfalls
*   **Estimating Before Defining:** Don't ask for a "T-shirt size" until the problem is well-understood. Estimates given too early are almost always wrong and lead to "no" by default.
*   **Shipping "Milestone 1" (The Half-Baked Trap):** When scoping down to fit an appetite, ensure the result is a *complete, functional product*, not a broken fragment that requires a "Phase 2" to be useful.
*   **Mowing the Lawn While the House is on Fire:** If your core product has high churn, do not use this for "new ventures." Use it to solve the specific "table stakes" gaps that are causing customers to leave.
*   **The Defensive "No":** Engineers often say "no" to protect the system from maintenance debt. Counter this by asking them to "earnestly try to make 'yes' work" for a fixed, short period (e.g., 10 minutes in a meeting or 2 days in a spike).