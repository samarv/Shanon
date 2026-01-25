---
name: scientific-experimentation-framework
description: A method for transitioning product management from "packaged intuition" to a scientific discipline. Use this when facing conflicting stakeholder opinions (HIPPO), when product strategy feels stalled by guesswork, or when you need to democratize decision-making across a team.
---

# Scientific Experimentation Framework

The "science" of product management is not found in writing strategy decks or collecting ideas; it is found in the speed at which you move from hypothesis to data. By implementing a rigorous experimentation culture, you democratize performance and replace the "loudest voice in the room" with statistical truth.

## Core Principles

- **Strategy is Overrated:** For most product teams, "strategy" is often just packaged intuition. Real strategy is simply "doing more of what the data proves works."
- **Data > Ideas:** Follow the Jonathan Rosenberg (Google) rule: "If you come to me with ideas, we'll go with mine. If you come with data, we go with the truth."
- **Compound Learning:** Growth is the result of compounding wins. To accelerate growth, increase the frequency of your experiments.
- **Scientific Discipline:** Treat product management as a specialized discipline like accounting or engineering by requiring evidence before committing to long-term roadmaps.

## The Process

### 1. Formulate the Hypothesis
Instead of a feature request, define a testable statement.
- **Bad:** "We need to add a loyalty program to increase retention."
- **Good:** "By adding a [Specific Reward] at [Specific Onboarding Step], we will increase Day-30 retention for [Target Cohort] by [X]%, based on the assumption that users value immediate liquidity."

### 2. Isolate via Cohorts
Never look at global dashboards to judge an experiment. Global data is a mixture of users from different eras and behaviors.
- Segment by signup date (cohort-level development).
- Segment by geography and document type (e.g., "Driver's license acceptance in Kenya").
- Use control groups to hedge against macro shifts (e.g., a crypto market crash might lower absolute conversions, but the experiment variant may still outperform the control).

### 3. Minimize Time-to-Data
Avoid projects with 6–12 month launch cycles. You cannot control the macro environment over long periods (e.g., COVID, regulatory shifts).
- Break big bets into the smallest possible testable units.
- For reversible decisions, skip the "pre-work" and go straight to a live test.
- Use a "Daily Meeting" rhythm for urgent experiments to ensure decisions are never blocked for more than 24 hours.

### 4. Analyze the "Dopamine Hit"
Review results using a centralized experimentation dashboard (e.g., Statsig) to check:
- **P-value/Statistical Significance:** Is the result real or noise?
- **Metric Movement:** Did it move the primary KPI without cannibalizing secondary metrics?
- **User Behavior:** Does the data reflect the person at the end of the screen, or just a number?

## Examples

**Example 1: High-Friction Compliance**
- **Context:** A fintech product requires KYC (Know Your Customer) documents, causing a 98% drop-off.
- **Hypothesis:** Users in Kazakhstan fail because the imaging SDK doesn't recognize their specific passport format.
- **Application:** Run a localized experiment in Kazakhstan with a new imaging SDK against the control group.
- **Output:** A 15% lift in conversion for that specific cohort, which is then rolled out globally for similar document types.

**Example 2: Macro-Hedged Pricing**
- **Context:** Revenue is dropping due to rising interest rates.
- **Hypothesis:** Offering a high-interest savings sub-account will attract new deposits despite the down market.
- **Application:** Test a "Savings" variant against a "Standard Account" control.
- **Output:** Even if total signups are down 20% due to the economy, the Savings variant shows 2x higher LTV (Life-Time Value) than the control, proving the strategy works regardless of macro conditions.

## Common Pitfalls

- **Confusing Absolute Numbers with Experiment Results:** Absolute conversion might drop due to a market crash (macro), but your experiment can still be a "win" if it beats the control group.
- **The "Loudest Voice" Trap:** Accepting a senior stakeholder's "gut feeling" without a test plan. Use the experimentation framework as a shield to protect the roadmap.
- **Over-Engineering the V1:** Spending months building a perfect feature. Mayur Kamat recommends buying a cheap $50 device or using basic SDKs to get the first data point in days, not months.
- **Ignoring the "Why" in the Details:** If a driver's license acceptance rate falls in one specific country, don't ignore it as an outlier. Dig into the specific document cells—the devil (and the growth) is in the details.