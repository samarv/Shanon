---
name: long-term-growth-impact-assessment
description: Evaluate the true incremental value of product experiments by moving beyond short-term conversion rates to long-term cohort holdouts and absolute volume metrics. Use this when short-term wins aren't translating to revenue, when teams are "gaming" conversion rates by constricting the funnel, or when evaluating high-friction onboarding changes.
---

The Long-Term Growth Impact Assessment is a framework for ensuring growth experiments drive actual business value (like GMV or Gross Profit) rather than just "pulling forward" results or optimizing local conversion ratios. By using long-term holdouts and absolute metrics, you can identify which "wins" are illusory and which "neutral" experiments are actually long-term powerhouses.

## Core Principles

### 1. Optimize for Absolute Volume, Not Ratios
Avoid using conversion rates as a primary North Star. To increase a conversion rate, a team can implicitly make the previous step harder (e.g., adding friction to sign-up to ensure only "high-intent" users reach the next step). This makes the rate look better but reduces the total number of successful users.
- **The Rule:** Measure the absolute number of users who reach a "success" milestone.
- **The Mindset:** It is often better to have a lower conversion rate on a much larger pool of users than a high rate on a tiny, restricted pool.

### 2. Implement the "Long-Term Ping" Holdout
Don't stop measuring an experiment once it reaches statistical significance. 
- **The Mechanism:** When an experiment concludes, ship the winner to 100% of users, but maintain the metadata tags for the original treatment and control cohorts.
- **The Cadence:** Set automated reporting "pings" to re-evaluate the cohort's performance at 3, 6, 12, and 24 months.
- **The Metric:** Measure downstream business value (e.g., Total Revenue, GMV, or Net Profit) rather than the local metric the experiment was designed to move.

### 3. Account for the "Pull-Forward" Effect
Recognize that 30-40% of short-term growth wins are neutral after one year. Often, an experiment simply accelerates an action a user would have taken anyway. If the long-term holdout shows the control group eventually "catches up" to the treatment group, the experiment had no incremental value.

## Implementation Workflow

### Step 1: Design for Absolute Success
When setting up an experiment, define success as: `[Absolute Number of Users] x [Long-term Value Metric]`.
*   **Bad Goal:** "Increase the sign-up to activated conversion rate by 5%."
*   **Good Goal:** "Increase the absolute number of merchants reaching $1k in GMV within their first 90 days."

### Step 2: Identify and Reduce "Monetary Friction"
Look for friction points related to trial length, price points, or credits.
- **The Hypothesis:** Lowering monetary friction early (e.g., extending a trial or offering a discount) may look like it's "lowering quality" in the short term, but it provides the time necessary for a user to become successful.
- **Verification:** Use the long-term holdout to see if these "lower quality" users eventually convert into high-value customers.

### Step 3: Use Taste for "Neutral-Positive" Decisions
If an experiment's short-term results are neutral but it aligns with your long-term product vision (e.g., a better UI or a more modern technical architecture):
- **Action:** Ship the change based on "Taste."
- **Logic:** If the data can't distinguish between the two, choose the version that represents the best possible product for the next 100 years.

## Examples

**Example 1: The Dunning/Payment Failure Notification**
- **Context:** A growth team wants to reduce churn by sending aggressive email reminders when a credit card payment fails.
- **Short-term Result:** Significant lift in "recovered" payments. The team claims a major win.
- **Long-term Assessment (12 months):** The holdout shows no incremental lift in GMV. 
- **Insight:** Users who let their cards fail were already uncommitted; the reminders only "pulled forward" a few weeks of subscription fee before they eventually quit. The team stopped focusing on this area to chase "bigger fish."

**Example 2: Pre-configured Onboarding Templates**
- **Context:** Providing pre-filled sections (e.g., image banners, product collages) for new users building a store.
- **Short-term Result:** Neutral. No increase in the number of people who paid for a subscription.
- **Long-term Assessment (6 months):** Massive impact on the number of people producing sales/GMV.
- **Insight:** The templates didn't convince people to *buy* the software, but they helped those who did buy to build *better* stores. These stores converted more visitors, giving the owners early momentum and keeping them in business longer.

## Common Pitfalls
- **The Rate Trap:** Making a sign-up flow harder to "clean up" the leads for a sales team. This almost always results in fewer total customers.
- **Ignoring the "How":** Focusing only on "what" to build (the feature) and ignoring the technical architecture. Architecture determines your long-term ability to pivot and adapt.
- **Siloed Attribution:** In hybrid funnels (self-serve + sales), failing to credit a marketing ad for a user who signed up self-serve but eventually closed via a sales rep. This leads to under-investing in high-value channels.
- **Performance Review Bias:** Rewarding teams for 5% lifts that disappear after 6 months. Use the 12-month "ping" to retroactively validate team impact.