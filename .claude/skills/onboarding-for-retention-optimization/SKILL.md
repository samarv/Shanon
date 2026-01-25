---
name: onboarding-for-retention-optimization
description: Optimize the product onboarding experience to maximize long-term retention rather than just initial conversion. Use this when seeing high Day-7 churn, when launching new core features, or when the "brand promise" doesn't match the initial product experience.
---

Onboarding is the only part of a product that 100% of users touch. This framework shifts the focus from "getting users through the door" (conversion) to "setting users up for success" (retention) by using smart friction and opinionated defaults.

## The Onboarding Optimization Framework

### 1. Identify "High-Potential" Users Early
Don't treat every user the same. Use the "high-motivation window" at the start of the journey to gather data and segment users.
*   **Identify Proxies for Success:** Ask 1-3 high-leverage questions or use OAuth data (e.g., social media follower counts, audience engagement) to identify users with high LTV potential.
*   **Segmented Routing:** 
    *   **High Potential:** Route to a "concierge" or high-touch human experience to ensure they don't churn.
    *   **Standard:** Route to an automated, self-guided flow.
*   **Productize Human Learning:** Observe how humans guide users manually, then build those specific recommendations directly into the automated product flow.

### 2. Implement "Opinionated Defaults"
Instead of offering a blank slate, use "Smart Defaults" to guide users toward behaviors that correlate with long-term retention.
*   **Limit Choice Architecture:** Don't eliminate choice, but make it "hard to do the wrong thing and easy to do the right thing."
*   **The "Success" Template:** Pre-fill settings based on what your most successful power users do (e.g., pre-selecting a 3-tier pricing model or specific notification settings).
*   **Constructive Friction:** If a user tries to change a default to a setting known to reduce success, add an interstitial or tooltip explaining *why* the default was chosen.

### 3. Measure "Velocity to Value"
Long-term retention (Day 90) takes too long to measure for rapid experimentation. Use proxy metrics that indicate a user is forming a habit.
*   **Define the Milestone:** Identify the first "success" event (e.g., first payment processed, first file shared, first booking).
*   **Measure Velocity:** Track how many hours/days it takes from sign-up to that milestone.
*   **Evaluate the Trade-off:** If an onboarding change decreases conversion by 5% but increases the "Velocity to Value" for the remaining 95%, the experiment is likely a win for LTV.

---

## Examples

**Example 1: Creator Platform (Patreon)**
*   **Context:** New creators often struggle to price their memberships.
*   **Input:** Data showed creators with 3-5 tiers performed better than those with 1.
*   **Application:** Implemented "Opinionated Defaults" where the setup flow pre-populated three tiers with recommended price points ($5, $10, $25). 
*   **Output:** Creators reached their first $100 in revenue 25% faster.

**Example 2: Marketplace Host (Airbnb)**
*   **Context:** New hosts often had calendar sync issues, leading to cancelled first bookings and high churn.
*   **Input:** Professional hosts stayed on the platform longer than casual hosts.
*   **Application:** During onboarding, the system identified if a host was "professional" via their tool-set. For casual hosts, the "Instant Book" default was paired with a required calendar-blocker step to ensure they didn't get a booking they couldn't fulfill.
*   **Output:** Reduced "bad" first experiences, leading to higher host retention in the first 30 days.

---

## Common Pitfalls

*   **Optimizing for Conversion Only:** Making the flow "too easy" can let in low-intent users who will never retain. This creates "noise" in your data and wastes support resources.
*   **Redesigning Without an Insight:** Never redesign an onboarding flow for "freshness." Only redesign when you have a "hard-earned insight" about a new user behavior or a change in your growth model.
*   **Appealing Only to Logic:** Users start onboarding with an emotional frame (seeking a solution to a pain point). Don't just show them features; show them how you deliver the "brand promise" they were sold in the marketing.
*   **Ignoring the "Back-Channel":** Failing to look at what users do *immediately after* the flow ends. If they reach the dashboard and get stuck, your onboarding didn't actually finish.