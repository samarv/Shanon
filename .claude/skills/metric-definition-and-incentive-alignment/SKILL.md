---
name: metric-definition-and-incentive-alignment
description: Define actionable metrics that drive long-term business outcomes by focusing on short-term inputs, simplicity, and common currency. Use this when setting quarterly team goals, resolving trade-offs between cross-functional departments, or diagnosing why a team's efforts aren't moving high-level KPIs.
---

# Metric Definition and Incentive Alignment

Analytics is a business impact function, not a service function. To drive impact, you must move beyond "answering the why" to "defining what to do next." This framework ensures metrics are simple enough for everyone to understand while being mathematically linked to long-term growth.

## Core Principles

### 1. Goal on Short-Term Inputs, Not Long-Term Outputs
Long-term outputs like "Retention" or "LTV" are terrible goals because they are impossible to move meaningfully in a 2-4 week sprint or even a quarter. Instead, identify the leading indicators (inputs) that mathematically drive those outputs.
- **Output:** Retention.
- **Input Proxies:** Order accuracy, delivery speed, price competitiveness, or selection (e.g., "Adding a Thai restaurant in Sacramento").

### 2. Prioritize Simplicity Over Mathematical "Perfection"
Avoid "Composite Metrics" (e.g., a "Merchant Health Score" of 0.35). If a team doesn't intuitively understand how to move the needle by 0.01, the metric is useless.
- **The Test:** If you tell a team the score dropped, do they know exactly which lever to pull? If not, break the composite into its individual components and goal on those instead.
- **Rule of Thumb:** It is better to have three simple, understandable metrics than one perfect, incomprehensible formula.

### 3. Establish a "Common Currency" for Trade-offs
To resolve conflicts between departments (e.g., Marketing vs. Logistics), translate all metrics into a single currency—usually Gross Order Value (GOV) or Volume.
- **Formula:** [1 minute reduction in delivery time] = [X% increase in GOV].
- **Application:** Use this to decide whether to spend $1M on a marketing campaign or $1M on onboarding more dashers to reduce wait times.

### 4. Goal on "Fail States" (Edge Cases)
Averages hide disasters. High-growth companies often reach a point where "improving the average" yields diminishing returns, but "eliminating the worst cases" yields massive gains in churn reduction.
- **Identify the "Never" State:** At DoorDash, this is the "Never Delivered" order.
- **The Strategy:** Create a dedicated goal to eradicate the fraction of a percent of orders that go completely wrong. These are disproportionately expensive and are the primary drivers of churn.

---

## Implementation Workflow

1.  **Map the Funnel:** Identify the long-term output you want to move (e.g., Annual Active Users).
2.  **Identify Levers:** List the inputs (Price, Selection, Quality) that contribute to that output.
3.  **Simplify:** Pick the top 1-3 inputs. Ensure they are "simple" (e.g., "Percent of merchants with photos" rather than "Merchant Engagement Index").
4.  **Translate to Currency:** Use historical data to calculate how much 1 unit of that input (e.g., 1% conversion) is worth in your common currency (e.g., $100k in GOV).
5.  **Assign Ownership:** Give the team a concrete target for that input.

---

## Examples

**Example 1: Merchant Success**
*   **Context:** A team wants to improve the quality of new merchants on a marketplace.
*   **Initial Input:** A "Merchant Health Score" weighting menu size, hours active, and photo coverage.
*   **Refined Input:** "Percentage of new merchants who receive their first order within 7 days."
*   **Result:** The team can clearly see that "Photo Coverage" and "Accurate Hours" are the fastest ways to hit the 7-day order goal.

**Example 2: Delivery Logistics**
*   **Context:** Deciding where to allocate engineering resources for the next quarter.
*   **Input A:** Reducing login errors by 5%.
*   **Input B:** Reducing average delivery time by 30 seconds.
*   **Application:** Translate both to GOV. If 5% fewer login errors = $500k GOV and 30 seconds faster delivery = $1.2M GOV, the resource allocation decision becomes objective.

---

## Common Pitfalls

*   **Goaling on Retention:** It’s a lagging indicator. By the time you see it drop, the "why" happened months ago.
*   **Ignoring the Denominator:** For example, measuring "Login Success Rate" might miss people who can't even open the app to attempt a login. Always ask: "What data are we *not* seeing?"
*   **Metric Fatigue:** Rotating a team through different metrics every three months. It takes time for a team to master the "levers" of a specific metric; keep them on it until the opportunity is exhausted.
*   **The "Average" Trap:** A 30-minute average delivery time sounds great, but if 2% of orders take 2 hours, those 2% are destroying your brand. Goal on the 2%, not the average.