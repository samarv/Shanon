---
name: opportunity-solution-tree-mapping
description: A visual framework to align product discovery with business outcomes. Use this when shifting from a feature-factory output model to outcome-based goals, when prioritizing a messy backlog, or when needing to communicate product strategy to stakeholders.
---

The Opportunity Solution Tree (OST) provides a visual scaffolding to navigate the messy, unstructured problem of moving from a high-level business outcome to a concrete, validated product solution. It forces teams to stay in the "problem space" longer, ensuring that every feature built solves a real human need.

## The Tree Structure

Construct the tree from the top down, ensuring each level connects logically to the one above it.

1.  **Outcome (The Root):** Define a single, measurable business metric (e.g., "Increase average viewing hours per user").
2.  **Opportunities (The Branches):** Map unmet needs, pain points, or desires discovered through customer research.
    *   **Rule of Threes:** Keep 3-7 primary branches at the top level to maintain cognitive focus.
    *   **Vertical Deconstruction:** Break big opportunities into smaller, solvable ones. "I can't decide what to watch" becomes "I don't know if this show is good" which becomes "I want to see the cast list."
3.  **Solutions (The Leaves):** Brainstorm multiple ways to solve a specific, small opportunity. Never map a solution directly to an outcome; it must solve an opportunity first.
4.  **Assumption Tests:** The smallest possible experiments to validate the underlying risks of a solution.

## Step 1: Define the Opportunity Space
To avoid the common mistake of framing solutions as opportunities (e.g., "Add a search bar"), focus on the customer's experience.

*   **Create an Experience Map:** Visualize the steps a customer takes to achieve a goal (e.g., Deciding to watch -> Choosing a platform -> Evaluating a title -> Watching).
*   **Identify Friction:** Look for moments where the customer struggles, feels frustrated, or has an unmet desire within those steps.
*   **Frame Verbally:** Write opportunities as "I" statements or specific pain points: "I have a movie in mind but don't know if it's on this platform" vs. "Better search."

## Step 2: Elicit Stories to Feed the Tree
Opportunities emerge from customer stories, not direct questions. Use the "Last Time" technique to gather reliable data.

*   **Avoid Direct Questions:** Do not ask, "What do you want?" or "How do you decide what to watch?"
*   **Prompt for Stories:** Ask, "Tell me about the last time you [action]?" (e.g., "Tell me about the last time you watched a movie on your couch").
*   **Be the "Five-Year-Old":** Once they start the story, keep them in the moment by asking, "What happened next?" and "Set the scene for me—who were you with?"
*   **Listen for the "But":** Identify opportunities when the user describes a workaround or a moment of mediocrity they’ve become used to.

## Step 3: Automate Discovery Cadence
To keep the tree "live," you must talk to customers weekly without the overhead of manual recruiting.

*   **In-App Opt-ins:** Use tools like Intercom or Ethnio to trigger a simple "Do you have 20 minutes to talk to us?" prompt while users are actually using the product.
*   **Internal Team Triggers:** Give Sales or Support a scheduling link (Calendly). Instruct them: "If you talk to someone experiencing [Pain Point X], put them on our calendar."
*   **Goal:** Wake up on Monday with an interview already scheduled for the week with zero manual effort.

## Step 4: Rapid Assumption Testing
Instead of testing a whole "feature," break the solution into its riskiest assumptions:
*   **Desirability:** Do customers actually have the need?
*   **Usability:** Can they find and use the solution?
*   **Feasibility:** Can we build it?
*   **Viability:** Does it work for our business?

Run 6-12 small tests per week across 3 different solutions to compare and contrast which one solves the opportunity most effectively.

## Examples

**Example 1: Streaming Service**
*   **Outcome:** Increase retention.
*   **Opportunity:** "I struggle to enter passwords on my TV remote."
*   **Solutions:** 
    1. A mobile app remote.
    2. QR code login.
    3. Magic link via email.
*   **Assumption Test:** Measure how many users have their phone in their hand while the TV login screen is open (Desirability test for QR code/Mobile login).

**Example 2: Healthcare Badging System**
*   **Outcome:** Reduce time spent on charting.
*   **Opportunity:** "It's annoying to manually log in to every workstation while moving between patient rooms."
*   **Solution:** NFC-enabled badges for "tap-to-unlock."
*   **Assumption Test:** Observe if nurses currently keep their badges visible or tucked in pockets (Feasibility/Usability test).

## Common Pitfalls
*   **The "Solution-in-Disguise":** If your opportunity is "I need a search bar," it’s a solution. Reframe it to the underlying need: "I can't find the specific title I'm looking for."
*   **Zero-Data Decisions:** Don't wait for "perfect" data. One interview is better than zero. Use small qualitative signals to decide what to build, then use production data to see if it worked.
*   **The "Siloed" Tree:** Only the "Product Trio" (PM, Designer, Engineer) should build the tree together. If one person builds it alone, you lose the shared understanding required for fast execution.
*   **Testing Non-Core Features:** Do not over-discover "commodity" features (e.g., a "Forgot Password" flow). Save discovery for differentiators.