---
name: gist-evidence-guided-development
description: A meta-framework to move product teams from opinion-based decision making to evidence-guided execution. Use this when stakeholder debates are stuck on opinions, when roadmaps feel like "feature factories" disconnected from results, or when you need to justify pausing a high-effort project to run lower-cost validation.
---

The GIST (Goals, Ideas, Steps, Tasks) framework replaces the "Plan and Execute" model with a continuous discovery and delivery loop. It balances human judgment with empirical evidence to reduce waste and increase the probability of product success.

## The GIST Model

### 1. Goals (The End State)
Instead of starting with what to build, start with the value you want to create.
- **The Value Exchange Loop**: Measure both the value delivered to the user (**North Star Metric**) and the value captured by the business (**Top KPI**).
- **Metric Trees**: Break your North Star and Top KPI down into sub-metrics (e.g., Activation Rate, Retention, Churn) to identify the specific levers a team can influence.
- **Rule**: Limit goals to 1-2 objectives and a maximum of 4 key results per team per quarter.

### 2. Ideas (The Hypotheses)
Ideas are hypothetical ways to achieve goals. Evaluate them using the **ICE** framework:
- **Impact**: How much will this move the target metric?
- **Confidence**: How sure are we about our impact/ease estimates? (Use the Confidence Meter below).
- **Ease**: How easy or hard is this to implement?

### 3. Steps (The Validation Loops)
Break ideas into "Learning Milestones" rather than project phases. Move from low-cost to high-cost validation:
1.  **Assessment**: Goal alignment, ICE analysis, stakeholder reviews.
2.  **Fact-Finding**: User interviews, data mining, competitive analysis.
3.  **Tests (The "Fake It" Stage)**:
    *   **Fake Door/Smoke Test**: A button that leads to a "coming soon" page.
    *   **Wizard of Oz**: A facade of automation where humans do the work behind the scenes.
    *   **Concierge**: Manually performing the service for a small group.
4.  **Experiments**: AB tests, multivariate tests with a control group.
5.  **Release**: Percent rollouts, staged releases, and hold-back tests.

### 4. Tasks (The Execution)
Break the "Agile Cage" where developers only move tickets. Use a **GIST Board** to provide context:
- **Structure**: A board with three columns: [Goals] | [Ideas] | [Next Steps].
- **Meeting Cadence**: Review the GIST Board every two weeks. If a "Step" yields negative evidence, kill or pivot the "Idea" immediately.

## The Confidence Meter
Use this 0–10 scale to objectively rank how much evidence supports an idea.

| Confidence Score | Evidence Class | Description |
| :--- | :--- | :--- |
| **0.0 - 0.1** | **Opinions** | Your own conviction, pitch decks, or "AI is trendy." |
| **0.4 - 0.8** | **Reviews/Plans** | Stakeholder feedback or back-of-the-envelope calculations. |
| **1.0 - 1.5** | **Anecdotal Data** | Talking to 5 customers or seeing a competitor has the feature. |
| **2.0 - 3.0** | **Market Data** | Large-scale surveys or deep data analysis of existing behavior. |
| **4.0 - 5.0** | **Low-Fi Tests** | Usability tests, "Wizard of Oz" prototypes, or "Fake Doors." |
| **6.0 - 8.0** | **Medium-Fi Tests** | Early Adopter Programs, Alphas, or Dog-fooding. |
| **9.0 - 10.0** | **High-Fi Tests** | AB experiments with statistically significant positive results. |

## Examples

**Example 1: Gmail Tabbed Inbox**
- **Context**: The team wanted to help "passive" users organize cluttered inboxes.
- **Idea**: Sort social and promotional emails into separate tabs.
- **Step (Validation)**: Conducted a "Wizard of Oz" test. Designers manually sorted 50 emails in a user's inbox using a facade of HTML.
- **Outcome**: Users loved the manually sorted view. This high-confidence evidence justified building the machine-learning categorization engine.

**Example 2: Improving Onboarding Time**
- **Goal**: Reduce average onboarding from 5.5 days to < 2 days.
- **Idea**: An automated "Onboarding Wizard."
- **Next Steps**:
    1.  **Fact-Finding**: Analyze data to see where users currently drop off (Cost: Low).
    2.  **Test**: Run a usability test with clickable mockups (Cost: Medium).
    3.  **Experiment**: Build a rough version for an AB test on 5% of traffic (Cost: High).

## Common Pitfalls
- **The "Build the MVP" Trap**: Treating an MVP as a "Beta" (v1.0) rather than a validation step. Always ask: "What is the cheapest way to learn if this idea is bad?"
- **Expert Blindness**: Assuming a founder's or leader's opinion counts as high confidence (it is only 0.1 on the meter).
- **Over-investing in Low Confidence**: Moving straight to full-scale development for an idea that only has "opinion" or "thematic" support.
- **Output vs. Outcome**: Measuring success by "bits in production" rather than "movement in the North Star metric."