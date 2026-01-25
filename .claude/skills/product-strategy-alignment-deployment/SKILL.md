```yaml
---
name: product-strategy-alignment-deployment
description: A framework for connecting high-level business goals to tactical team execution to fix the "missing middle." Use this when teams are working hard but metrics aren't moving, when executives feel product is a "black box," or when stakeholders are constantly fighting over priorities.
---
```

This framework identifies and fixes the "missing middle"—the gap between high-level company vision and the daily tasks of product teams. It ensures that every feature built is an explicit bet toward a prioritized business outcome.

## The Strategy Stack
To deploy strategy effectively, information must flow through three distinct levels. If any level is skipped, teams lose context and default to "feature factory" behavior.

1.  **Strategic Intents (Business Level):** High-level business movers for the next 2–3 years (e.g., "Enter the European market," "Shift from SMB to Enterprise").
2.  **Product Initiatives (Director/VP Level):** Problem-oriented themes that address the Strategic Intents. These are "meaty" problems, usually spanning multiple epics (e.g., "Automate VAT compliance for EU customers").
3.  **Options (Team Level):** The specific solutions or experiments built to solve the Product Initiatives (e.g., "VAT calculation API integration").

## The Strategy Memo Template
Avoid 20-page PRDs. Instead, document the strategy in a 2-page memo that covers:

*   **The Vision:** A concrete, non-fluffy description of the future. Avoid taglines like "Be the backbone of X." Instead, describe exactly how the world looks different in 5 years.
*   **Positioning:** How the product differs from competitors. Explicitly state what the product is *not* going to do to prevent "copycat" roadmap syndrome.
*   **Current State:** A brutal assessment of the product today and the external market threats.
*   **Strategic Intents:** The prioritized list of 2-3 big business goals.
*   **Target Outcomes:** The specific business metrics and user behaviors that signify success.

## The Strategic Alignment Audit
Perform this "interrogation" to find where the strategy is breaking down:

1.  **The Team Test:** Ask 3–5 different teams: "What are you working on, and why does it matter to the business?"
    *   *Failure:* They describe the feature ("I'm building a login button").
    *   *Success:* They connect it to the intent ("I'm building this login flow to reduce churn in our new Enterprise segment").
2.  **The Executive Test:** Ask every executive: "What is the company vision?"
    *   *Failure:* You get five different answers or vague taglines.
    *   *Success:* You get a consistent story about the market and the product's unique value.

## Execution Cadence
Standardize the "interaction" between levels, not the team's internal work.
*   **Monthly Strategy Check-ins:** Review roadmaps against Strategic Intents.
*   **Quarterly Planning:** Adjust Product Initiatives based on data from the "Options" tested by teams.
*   **Data Inputs:** Ensure every team has access to a dedicated data analyst or a centralized dashboard to track their specific outcomes (OKRs).

## Examples

**Example 1: Fixing Misalignment**
*   **Context:** A healthcare SaaS company where teams are shipping features, but ARR is flat.
*   **Input:** CEO wants "to be the best in healthcare." Teams are building random feature requests from sales.
*   **Application:** The CPO writes a memo defining a Strategic Intent: "Reduce administrative overhead for clinics by 30%."
*   **Output:** Teams stop building "requested widgets" and start building an "Automated Billing Engine" because it directly ladders to the 30% reduction goal.

**Example 2: Managing Stakeholder Conflict**
*   **Context:** Sales wants "Feature A" for a new logo; Support wants "Feature B" for retention.
*   **Input:** Both stakeholders are shouting for priority.
*   **Application:** The PM points to the documented Strategic Intent: "This year our priority is 100% Retention, not New Logos."
*   **Output:** The trade-off conversation becomes objective. Feature B is prioritized because it aligns with the stated business goal of retention.

## Common Pitfalls
*   **The Fluffy Vision:** Using taglines instead of descriptions. If you can’t visualize the end state, it’s not a vision.
*   **The Missing Middle:** Jumping from "Vision" straight to "Backlog." This leaves teams with no criteria to prioritize one feature over another.
*   **Lack of "No":** A strategy that doesn't say what you *won't* do is just a wishlist. If you are copying every competitor feature, you have no strategy.
*   **Pitting Executives Against Each Other:** CEOs who give Sales and Product conflicting goals (e.g., "Total Revenue" vs. "Product Stability") without a shared Strategic Intent.