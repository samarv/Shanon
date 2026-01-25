---
name: amped-lifecycle-tracking
description: A framework for measuring product velocity and output quality using standardized stage-gates (P-strat to P2) and binary quality triage. Use this when you need to identify team bottlenecks, align cross-functional teams (Analytics, Marketing, Product, Engineering, Design), or calibrate organizational standards for "what great looks like."
---

# The AMPED Lifecycle: Balancing Speed, Quality, and Value

The AMPED (Analytics, Marketing, Product, Engineering, Design) lifecycle is a system designed to ensure that product development is a "virtuous cycle" of improvement. It moves beyond simple "shipping" to track exactly how long value takes to reach the customer and whether that value meets a binary standard of excellence.

## The P-Gate Workflow
Categorize every project as **Small** (under 1 month), **Medium**, or **Large**. Track the time spent in each of the following phases:

1.  **P-Strat (Strategy):** The initial concept pitch. Align the project with the annual strategy white paper and define the "Chess Move" (how this makes the product better relative to competitors).
2.  **P0 (Problem Definition):** A one-page spec focused strictly on the user pain point and the metric to be moved.
3.  **P1 (Solution Definition):** The technical and design specification of the product to be built.
4.  **P2 (Value Validation):** Post-ship analysis. This phase is only complete when the original target metric from P0 is measured and moved.

## Operationalizing Velocity and Quality

### 1. Velocity Benchmarking (The "Golf" Method)
Treat velocity as a game of golf—compete only against your own past performance.
*   **Collect Cycle Data:** Record the duration of each P-gate across all 50+ feature teams.
*   **Calculate Medians:** Establish the median time for a "Small" project to move from P0 to P1.
*   **Identify Roadblocks:** If a team exceeds the median, leadership should not penalize them but instead "raise a hand" to remove technical or organizational blockers (e.g., dependency issues, lack of design resources).

### 2. Binary Quality Triage
Avoid long, subjective documents defining "quality." Use a classification system instead.
*   **Monthly Review:** Design leadership reviews every feature shipped in the last 30 days.
*   **Binary Labeling:** Categorize each ship as either **High Quality** or **Not High Quality**.
*   **Color Comparison:** Use these examples to train the org. Just as you learn "Pink vs. Red" by seeing them, PMs learn quality by seeing "High vs. Low" examples.
*   **Feedback Loop:** Share the "Not High Quality" list with teams to build "reinforcement learning" for future sprints.

### 3. The 80/50 Roadmap Rule
Maintain a rolling 6-month roadmap updated every 3 months to balance enterprise needs with agility:
*   **Months 1–3:** Commit to an **80% confidence level**. These items are nearly certain to ship.
*   **Months 4–6:** Commit to a **50% confidence level**. This allows the team to pivot based on new competitive threats or "hitting a brick wall" (learning a path is wrong) without breaking promises.

## Examples

**Example 1: Diagnosing a Slow Feature Launch**
*   **Context:** A team is building an asynchronous video tool (e.g., Talktrack).
*   **Input:** The project is tagged as "Medium" and is currently in the P1 phase.
*   **Application:** The PM notices the P0-to-P1 time has hit 45 days, while the org median for Medium projects is 20 days.
*   **Output:** The PM raises a hand in the Monday leadership meeting. They identify a "blocker" in engineering architecture. Leadership reallocates a senior engineer for 48 hours to resolve the bottleneck.

**Example 2: Calibrating Design Standards**
*   **Context:** A new "Sharing" flow is released.
*   **Input:** The design leadership triage.
*   **Application:** The flow is labeled "Not High Quality" because the button placement is inconsistent with the platform's core UI.
*   **Output:** The example is added to the "AMPED Quality Gallery." The feature team sees the specific comparison and adjusts the next iteration to meet the "High Quality" benchmark.

## Common Pitfalls
*   **Focusing on Speed over Value:** Shipping fast doesn't matter if the P2 phase shows the metric didn't move. Never close a project at "Ship"—only at "Impact."
*   **Over-Defining Quality:** Don't write 20-page "Quality Guidelines." People won't read them. Show them 10 examples of "High Quality" and 10 examples of "Not High Quality."
*   **Siloing Marketing:** If Marketing isn't in the "AMPED" loop from P-strat, the product might be functional but fail to "capture the imagination" of the market because the positioning is an afterthought.
*   **Competing Between Teams:** Using velocity data to rank teams against each other. Use data only to find where leadership needs to help unblock a team.