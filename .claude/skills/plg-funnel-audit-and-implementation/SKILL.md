---
name: plg-funnel-audit-and-implementation
description: A framework for transitioning from a sales-led to a product-led growth motion. Use this when you need to audit an existing user journey for friction, define activation "Aha" moments, or set up the infrastructure for a self-serve revenue engine.
---

# PLG Funnel Audit and Implementation

Product-Led Growth (PLG) is fundamentally "Data-Led Growth" (DLG). This framework allows you to transition from traditional Sales-Led Growth (SLG) to a model where the product acts as the primary vehicle for acquisition, activation, and conversion.

## Phase 1: The Full-Funnel Audit
Perform a "pretend user" walkthrough to identify high-leverage friction points. Evaluate the journey against these four criteria:

1.  **Acquisition & Entry Point**: Does the website prioritize "Try for Free" over "Book a Demo"? The entry point must be low-barrier (e.g., free version, free trial, or open source).
2.  **Sign-up Flow**: Can a user create an account without boss approval or manual vetting? Remove unnecessary form fields that target only specific demographics (e.g., UK-only questions for US users).
3.  **Time to Value (Aha Moment)**: Does the user experience the core value within the first session? 
    *   **Do > Show > Tell**: Prioritize allowing users to take an action over showing a video or telling them about a feature.
    *   **Warm Starts**: Provide sample data or templates so users aren't staring at an empty state.
4.  **Self-Service Checkout**: Can the user buy the product without talking to sales? Ensure the pricing is simple and the payment processor supports the user's local currency/market.

## Phase 2: Defining the "Aha" Moment
Identify the specific correlation between early behavior and long-term retention. 

### Activation Milestone Formula
Combine user count, feature count, and time.
*   **GitLab Example**: 2 users + 2 features used within 14 days.
*   **Facebook Example**: 10 friends in 7 days.

### Identification Process
1.  **Brainstorm**: List 10 high-value actions (e.g., merging a PR, inviting a teammate, setting up a recurring deposit).
2.  **Correlation Analysis**: Compare users who took these actions against average 30-day retention and 90-day conversion rates.
3.  **Verify Causation**: Run experiments specifically designed to nudge users toward that action and measure if retention actually lifts.

## Phase 3: The Data-Led Growth (DLG) Stack
PLG fails without granular usage data. Implement the following infrastructure:

*   **Data Hub**: (e.g., Segment, mParticle) To collect and route data to different tools.
*   **Product Analytics**: (e.g., Amplitude, Mixpanel, PostHog) To visualize the funnel and identify drop-off points.
*   **Experimentation Engine**: (e.g., Eppo, Optimizely) To validate that product changes actually drive metrics.
*   **Lifecycle Marketing**: (e.g., Customer.io, HubSpot) To trigger emails or in-app messages based on specific product behaviors (e.g., "You haven't invited a teammate yet").
*   **Data Enrichment**: (e.g., Clearbit, ZoomInfo) To identify the company size and industry of your free users.

## Phase 4: Building the Initial Growth Squad
Start with a dedicated "Tiger Team" or a formal Growth Squad.

1.  **Growth PM**: Needs to be highly analytical and focused on funnel conversion rather than just feature building.
2.  **Data Analyst**: Often the most important first hire. They define the "Data Dictionary" and ensure every key action is instrumented correctly.
3.  **Engineers/Designers**: Ideally dedicated resources so the growth team doesn't have to "borrow" time from the core product roadmap.

---

**Example 1: B2B DevOps Platform**
*   **Context**: A complex developer tool moving from sales-led to PLG.
*   **Input**: High traffic but low conversion to paid plans.
*   **Application**: Audit reveals users are lost after sign-up. The team defines an "Aha" moment (running the first pipeline) and creates a "Warm Start" template that runs a sample pipeline automatically.
*   **Output**: Activation rate increases by 20%, leading to a higher volume of Product Qualified Leads (PQLs) for the sales team.

**Example 2: FinTech Investment App**
*   **Context**: A passive investment app where users "set and forget."
*   **Input**: High churn because users don't engage with the app after the first week.
*   **Application**: Data analysis shows that users who set up "Recurring Investments" retain 3x better. The Growth PM moves this feature to the first step of onboarding.
*   **Output**: Habit formation is built into the first session, stabilizing long-term retention.

---

## Common Pitfalls
*   **The "Launch and Leave" Mistake**: Treating PLG as just "adding a free trial CTA" and expecting revenue to follow. It requires a 1–2 year commitment to optimize the user journey.
*   **Garbage In, Garbage Out**: Implementing analytics tools without a "Data Dictionary." If event names are inconsistent, PMs and analysts will not trust the data.
*   **Complex Pricing Barriers**: Requiring a manual "quote" during a self-serve checkout. If the user has to wait for an email to know the price, the PLG loop is broken.
*   **Treating Retention as the Messy Middle**: Trying to fix retention before fixing activation. Most retention problems are actually onboarding (activation) problems.