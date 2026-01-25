---
name: friction-logging-and-ux-reviews
description: A systematic method for auditing user experiences by role-playing specific personas to identify "broken edges." Use this during product development, before major launches, or as a recurring audit to maintain a high bar for craft.
---

# Friction Logging and UX Reviews

Friction logging is the practice of systematically identifying every hurdle, point of confusion, and "broken edge" in a user flow. By adopting a specific user's mental model and recording a stream-of-consciousness log of the experience, teams move beyond abstract metrics to granular, actionable improvements that compound into a superior product.

## The Solo Friction Log Process

Perform this audit individually on a recurring basis (e.g., once a month) or when a new feature is ready for its first end-to-end test.

1.  **Define the Persona:** Choose a specific user profile to mental-model. Do not just "test the product"—be "an engineer at a large SaaS company integrating a billing API for the first time."
2.  **State the Goal:** Define exactly what the user is trying to achieve (e.g., "Set up a subscription with a 30-day trial").
3.  **Start the Stream of Consciousness:** Open a blank document. Record every thought, frustration, and moment of delight as you move through the flow.
4.  **Note the Details:** 
    *   **Context switching:** "I had to leave the dashboard to find a secret key in the docs."
    *   **Error handling:** "The error message was generic; it didn't tell me what field was missing."
    *   **Latency:** "This page took 3 seconds to load, making me wonder if it crashed."
5.  **Include Praise:** Explicitly mark things that work well. This reinforces high-quality patterns across the team.
6.  **Tag and Distribute:** Share the log with the relevant PMs and Engineering Managers. Tag specific owners for "paper cuts" (minor issues) and "blockers."

## Group Review: "Walking the Store"

For critical product flows, transition from solo logging to a collaborative review involving cross-functional leadership (Engineering, Product, Design, and Support).

1.  **Select the Flow:** Pick a high-stakes path, such as onboarding, checkout, or a complex API integration.
2.  **Shared Issue Log:** Create a live document or "crying octopus" (internal feedback) link where attendees can type issues in real-time while the leader walks through the flow.
3.  **The Walkthrough:** A PM or Engineer shares their screen and performs the task live. They should talk through their choices and assumptions.
4.  **Debate the "Bar":** Discuss identified issues immediately. Ask: "Does this meet our standard of being meticulous? If not, what is the fix?"
5.  **Establish Shared Language:** Use these sessions to calibrate the team’s definition of "good" so that future micro-decisions align with the company's craft standards.

## Friction Log Template

*   **User Persona:** [e.g., First-time developer at a startup]
*   **Task:** [e.g., Issuing a refund through the dashboard]
*   **Log:**
    *   [00:00] I’m looking for the 'Payments' tab. It was easy to find. (**Praise**)
    *   [00:01] I clicked 'Refund' but I'm not sure if it worked because there was no loading state. (**Friction**)
    *   [00:02] Received error code `ERR_742`. I have no idea what this means. I have to Google it. (**Friction**)
    *   [00:05] Found the fix. Why didn't the error message just link me to the right doc? (**Opportunity**)
*   **Summary of Fixes:** [List of actionable tickets]

## Examples

**Example 1: Improving API Error Messages**
*   **Context:** A developer is integrating an API and makes a syntax error.
*   **Observation:** The friction log noted that the developer spent 10 minutes searching documentation to interpret a cryptic error code.
*   **Application:** The team added code to the API error handler to detect the specific error and provide a direct URL to the relevant documentation page in the response.
*   **Output:** Reduced integration time and increased developer "delight."

**Example 2: Optimizing Checkout Flows**
*   **Context:** A user is checking out on a mobile device.
*   **Observation:** During a "Walk the Store" session, the team noticed a user had to click three times to select a saved payment method.
*   **Application:** The team prioritized removing clicks and reducing latency in the "payment element."
*   **Output:** A measured revenue uplift of 10.5% for users who migrated to the optimized flow.

## Common Pitfalls

*   **Testing as a "Power User":** Avoid using your internal knowledge to skip steps. If you know where a button is because you built it, you aren't logging real friction. You must maintain the "beginner's mind."
*   **Ignoring "Paper Cuts":** Small issues (like a typo or a slightly off-center icon) are often dismissed as "non-blocking." Collectively, they signal a lack of craft. Fix them to prevent "death by a thousand cuts."
*   **Lack of Persona Specificity:** Logging friction for a "general user" leads to vague feedback. Be specific (e.g., "A CFO at a Fortune 500 company trying to export a CSV") to uncover high-value nuances.
*   **Making it Punitive:** UX reviews can be stressful. If the culture becomes about "catching" mistakes rather than "co-creating" quality, teams will hide friction. Always start with the goal of helping the user.