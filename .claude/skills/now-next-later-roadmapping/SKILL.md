---
name: now-next-later-roadmapping
description: Transition from date-driven Gantt charts to a problem-based roadmap that acknowledges uncertainty. Use this when stakeholders demand unrealistic deadlines, when long-term plans are frequently missed, or when your roadmap feels like a list of features rather than a strategy.
---

# Now-Next-Later Roadmapping

A roadmap is not a plan; it is a **prototype for your strategy**. Just as you prototype a feature to test design assumptions, you use a roadmap to test strategic assumptions. The goal is to shift the conversation from "When will this feature be done?" to "What problems are we solving and what are we learning?"

## The Framework

Instead of a timeline on the X-axis, use three buckets based on the **Cone of Uncertainty**:

### 1. Now (High Certainty)
*   **Timeframe:** Current work and the immediate next steps (typically the next few weeks).
*   **Granularity:** Detailed tasks and specific solutions.
*   **Focus:** Execution and delivery. These are things the team is actively working on or has fully refined.

### 2. Next (Medium Certainty)
*   **Timeframe:** The next few months.
*   **Granularity:** Problem statements and high-level ideas.
*   **Focus:** Discovery and validation. You know you want to solve these problems, but you haven't committed to the exact solution yet.

### 3. Later (Low Certainty)
*   **Timeframe:** 6+ months out.
*   **Granularity:** Broad themes and strategic goals.
*   **Focus:** Long-term vision. These are "fuzzy" areas where you need more data before committing resources.

## Implementation Steps

### Step 1: Shift to Problem-Based Items
For every item on your roadmap, don't just list a feature name. Require the team to answer:
*   What problem does this solve?
*   Why would we want to solve it now?
*   What is the desired outcome (metric/behavior change)?

### Step 2: Separate Soft Launch from Hard Launch
Decouple engineering delivery from marketing activities to reduce "date pressure":
*   **Soft Launch:** When the feature is functionally ready and released to a subset of users. This is for the engineering team.
*   **Hard Launch:** The marketing "bang"—testimonials, videos, and PR. This can happen days, weeks, or months after the soft launch once the feature is proven stable.

### Step 3: Manage Stakeholder Dates
If a stakeholder (CEO, Sales, Marketing) demands a hard date, use the "Sales Pipeline" analogy:
*   **The Analogy:** A VP of Sales doesn't promise a specific deal will close on a specific day; they promise a pipeline of experiments (calls) that will result in a revenue target by the end of the quarter.
*   **The Application:** Tell stakeholders you are investing $X into a team to run Y number of experiments. While you can't guarantee *which* experiment will work by Oct 15th, you can guarantee the team will move the target metric by the end of the quarter.

## Examples

**Example 1: E-commerce Checkout Optimization**
*   **Context:** Conversion is dropping at the payment step.
*   **Now:** Implement "One-Click Apple Pay" (Refining a specific, validated solution).
*   **Next:** Reduce friction in the "Guest Checkout" flow (Problem identified, specific UX solutions currently in discovery).
*   **Later:** Internationalization and multi-currency support (Strategic goal, but requires significant market research before defining requirements).

**Example 2: B2B SaaS Reporting**
*   **Context:** Large customers say they "can't see the value" of the tool.
*   **Now:** Build "Weekly Automated Email Digest" (Solution tested and ready for dev).
*   **Next:** Enable "Custom Dashboard Widgets" (Known need, but investigating which metrics are most requested).
*   **Later:** Predictive AI analytics (Visionary goal, checking technical feasibility in the background).

## Common Pitfalls

*   **Treating "Later" as a Junk Drawer:** Don't put things in "Later" just to be polite to stakeholders. If you have no intention of solving a problem, remove it. A roadmap should only contain assumptions you actually want to test.
*   **Adding Dates to Every Column:** Avoid the temptation to put months at the top of the columns (e.g., Now = January). This instantly turns the framework back into a Gantt chart and reinstates the "delivery trap."
*   **Neglecting the "Did it Work?" Step:** Many teams move items to "Done" and forget them. A healthy roadmapping process requires a retrospective on the outcome: "We launched this in 'Now'; did it actually solve the problem we identified when it was in 'Next'?"
*   **Over-planning the "Later" Bucket:** Spending weeks refining requirements for a "Later" item is a waste of resources. By the time you get there, the market or strategy will likely have shifted. Keep "Later" items as one-sentence themes.