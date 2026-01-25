---
name: growth-model-construction
description: Create an analytical representation of how your business grows to assess opportunities and prioritize product roadmaps. Use this skill during quarterly planning, when evaluating new channel investments, or when deciding how to allocate resources across disparate product pods.
---

A growth model is a formulaic representation of your business, typically built in a spreadsheet, that maps how acquisition, retention, and monetization interact. Its primary value is not forecasting, but providing a "common currency" to compare the ROI of different product initiatives.

## The Construction Process

### 1. Build the SaaS Foundation
Start with the three linear building blocks. Even for non-SaaS businesses, these are the starting points:
- **Acquisition:** Map your channels (Paid, Organic, Viral). Define inputs: Traffic/Spend → Conversion Rate → New Users.
- **Retention:** Create a survival curve. Define: Activation Rate → Monthly/Annual Retention Rate.
- **Monetization:** Define the base revenue per user (e.g., Subscription Fee).

### 2. Layer Transactional Complexity
If the business is transactional (e.g., E-commerce, Marketplace), add the following variables:
- **Frequency:** Transactions per month/year per retained user.
- **Average Order Value (AOV):** Revenue per transaction.
- **Unit Economics:** Model the Contribution Margin (Revenue minus COGS and marginal costs like shipping or support).

### 3. Incorporate Non-Linear Loops
Identify where the output of the model feeds back into the input:
- **Virality:** (Existing Users) × (Referral Rate) × (Invite Conversion) = New Users.
- **Reinvestment:** (Contribution Margin) × (% Reinvested) / (CAC) = New Users.
- **The Payback Lever:** Measure "Time to Payback" rather than just LTV/CAC. The faster you get money back, the faster the reinvestment loop spins.

### 4. Model Marketplace Interdependence
For two-sided markets, you must include the "Interaction Variable":
- **Supply Constraints:** Model how adding one unit of supply (e.g., a new driver or product) incrementally increases demand conversion or retention.
- **Dual-Sided ROI:** When calculating the cost of a new user, include the "Loaded CAC" (Cost to acquire the user + the proportional cost to acquire the supply needed to serve them).

## Application in Planning
Use the model to perform "Zero-Based Accounting" during planning cycles:
1. **Gather Proposals:** Collect expected metric moves from every product pod (e.g., "Team A will move conversion by 5%," "Team B will move retention by 1%").
2. **Run Scenarios:** Input these changes into the growth model.
3. **Compare in Common Currency:** Evaluate which move creates the highest lift in long-term GMV or Contribution Margin.
4. **Allocate Resources:** Assign headcount to the pods with the highest modeled ROI.

## Examples

**Example 1: Prioritizing Retention vs. Conversion**
- **Context:** A local services marketplace (like Thumbtack) sees high SEO traffic but low repeat usage.
- **Input:** The team has two options: (A) Increase top-of-funnel conversion by 10% or (B) Increase repeat booking rate by 2%.
- **Application:** Running both through the growth model reveals that the 2% retention lift compounds, significantly lowering the "effective CAC" over 12 months.
- **Output:** The company shifts resources from the "Conversion Pod" to the "Lifecycle/Retention Pod."

**Example 2: Managing Marketplace Supply/Demand Balance**
- **Context:** A ride-sharing startup is deciding whether to spend on rider promos or driver bonuses.
- **Input:** Current wait times are 8 minutes. Data shows conversion drops off sharply after 5 minutes.
- **Application:** The model uses the "Liquidity Metric" (Wait Time) as a multiplier for demand conversion. It shows that $1,000 spent on driver supply to hit the 5-minute threshold yields 3x the riders of $1,000 spent on rider promos.
- **Output:** Investment is funneled into supply acquisition until the liquidity threshold (5 mins) is met.

## Common Pitfalls
- **The "Best User" Fallacy:** Assuming that because power users do "Action X," forcing new users to do "Action X" will turn them into power users. Focus instead on "Homogenizing the Experience"—ensuring no early user has a below-average first session.
- **Over-Complexity:** Stacking too many assumptions (junk in, junk out). If a variable is too hard to understand (like the exact relationship between supply depth and brand sentiment), keep it as a simple linear assumption.
- **Forecasting vs. Assessment:** Do not use this as a static finance forecast. It is a living tool for **opportunity assessment**. The absolute numbers matter less than the delta between scenarios.
- **Neglecting the Early User:** PMs often try to move retention by focusing on "resurrection" (getting churned users back). The growth model usually shows that improving the first-week experience has a 10x higher impact on the long-term survival curve.