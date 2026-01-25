---
name: product-intuition-and-simplification
description: Apply Dylan Field’s "intuition-led" framework to generate product hypotheses and enforce radical simplification. Use this when reviewing new feature requests, resolving UI complexity, or deciding between product quality and speed.
---

# Product Intuition and Simplification Framework

This framework treats product intuition not as a magical "sixth sense," but as a rigorous hypothesis generator. It combines high-craft standards with the principle of "irreducible complexity" to ensure products remain powerful yet simple.

## The Intuition-Led Workflow

### 1. Generate Intuition Hypotheses
Treat your initial product "gut feelings" as hypotheses rather than final decisions.
- **Injest broad data:** Scan support channels, social media mentions, and community feedback to identify friction points.
- **Formulate the "Why":** State the hypothesis clearly: "I feel that adding [Feature X] will solve [Problem Y] because [Reasoning]."
- **Identify the Root Need:** Distinguish between what users ask for (e.g., "I need Pages") and what they actually need (e.g., a way to organize complex design systems).

### 2. Pressure-Test through Concrete Artifacts
Avoid abstract debates. Dylan Field emphasizes that the more concrete an artifact is, the better the debate.
- **Create a prototype:** Build the "minimally awesome" version of the idea.
- **Debate the artifact:** Present the prototype to stakeholders. Ask follow-up questions until you hit first principles.
- **Seek the "Dense" Answer:** If a leader or peer is skeptical, find the specific data point or technical constraint that resolves the "denseness" of the disagreement.

### 3. Apply the Simplification Filter
Use the principle of **Irreducible Complexity**: Every added feature has a hidden cost to the coherence of the whole system.
- **The Golden Rule:** "Keep the simple things simple; make the complex things possible."
- **Evaluate Local vs. Systemic Decisions:** Review if a series of "correct" local decisions (adding specific buttons or settings) has created a "systemic monstrosity" (a cluttered UI).
- **The "Brow-Furrow" Test:** If a workflow requires more than a few seconds of thought to navigate, it is too complex. Insist on a simpler path.

## The "Minimally Awesome" Trade-off Triangle

When launching a new feature or product, you must choose exactly two of these three variables. If you try to pick all three, you will likely fail.

1.  **Quality:** The craft, polish, and "soul" of the product.
2.  **Features:** The breadth of functionality.
3.  **Deadline:** The speed of the ship date.

**The Strategy:** For B2B software where the bar is high, choose **Quality** and **Deadline**. Ship fewer features, but ensure those you do ship are "minimally awesome."

## Examples

### Example 1: Resolving Feature Bloat
- **Context:** A PM wants to add a complex permissions matrix to a document tool.
- **Application of Skill:** The Lead Designer furrows their brow at the 12-column matrix. Instead of "more settings," they apply the simplification filter. They realize the root problem is just "sharing with a team."
- **Output:** They ship a "Share with Team" toggle (Simple) but keep a hidden "Advanced Permissions" link for power users (Complex things possible).

### Example 2: Turning Intuition into Data
- **Context:** An engineer has a "hunch" that a new AI feature should be a floating sidecar rather than an integrated menu.
- **Application of Skill:** The engineer treats this as a hypothesis. They build a "Websim-style" hallucinated prototype of both versions. They share it in a Slack channel and track which version gets more "heart" reactions from the design team.
- **Output:** The "Sidecar" version wins the debate because the concrete artifact proved it interfered less with the core workspace.

## Common Pitfalls

- **Treating Process as the Product:** Focusing so much on the "how" (meetings, tickets, sprints) that you lose sight of the problem you are solving. Process supports outcomes; it is not the outcome itself.
- **Solving the Surface Request:** Building exactly what the user asks for without asking enough follow-up questions to find the "Y or Z" root problem.
- **Ignoring Systemic Complexity:** Making five "simple" updates that, when viewed together, make the overall product navigation impossible to understand.
- **Shipping Without "Soul":** Solving the utilitarian problem but removing the "art" or "creativity" that makes users love the tool. Aim for "Art applied to problem-solving."