---
name: maximally-accelerated-execution
description: A framework for collapsing delivery timelines and increasing the "resting heart rate" of a product team. Use this when launching breakthrough features, unblocking complex cross-functional projects, or when moving from a "research" phase to a "product" phase.
---

# Maximally Accelerated Execution

In high-uncertainty environments like AI, the only way to find out what is valuable is to bring it into the external world. Maximally accelerated execution is a mindset used to identify the true critical path by challenging every assumption about why a project cannot ship immediately.

## Core Principles

### Set the "Resting Heart Rate"
The speed of a team is a choice. As a leader, your role is to set a high baseline pace where daily or weekly shipping is the expectation, not an exception.

### The Punchline Mindset
When faced with a long roadmap, jump straight to the punchline. Ask: **"If this was the most important thing in the world, why can't we do it now?"** or **"Why can't we do it tomorrow?"** Use this to strip away non-critical blockers.

### Differentiate Speed from Process
- **High Speed (Product Development):** UI/UX, feature sets, and distribution should move at maximal acceleration to facilitate learning.
- **Rigorous Process (Safety/Infrastructure):** Areas with high stakes (e.g., AI safety red-teaming, HIPAA compliance) require a rigorous, non-accelerated process. Do not conflate the two.

## Implementation Workflow

1.  **Identify the Critical Path:** List every step currently standing between the current state and a public launch.
2.  **Challenge the Delay:** For every item on the list, ask: "What happens if we don't do this before shipping?" 
3.  **Deploy "Minimum Viable UI":** If the backend tech is ready, do not wait for a polished interface. Use "unpolished" solutions (like a simple dropdown menu or basic chat interface) to start gathering user data.
4.  **Gather Empirical Data:** Once live, stop "reasoning a priori." Use conversation classifiers or user data to see how people actually use the product.
5.  **Iterate Toward Polish:** Use the feedback from the "raw" launch to decide what to polish. Do not spend time polishing features that users might ignore.

## Examples

**Example 1: Pricing a New Product**
*   **Context:** A team is debating the optimal price for a new subscription tier for months.
*   **Traditional Approach:** Hire a pricing consultant, run conjoint analysis, and plan a Q3 rollout.
*   **Maximally Accelerated Application:** Send a 4-question Van Westendorp survey to a community Discord or email list today. Analyze the results in a Google Sheet tomorrow. 
*   **Output:** A $20/month price point launched within 48 hours to manage demand.

**Example 2: Turning a Research Demo into a Product**
*   **Context:** A breakthrough model exists in a lab, but the team is building a complex "Super Assistant" with many bespoke features (meeting bots, coding tools).
*   **Traditional Approach:** Build out the full feature set over six months.
*   **Maximally Accelerated Application:** Recognize that users want the raw power of the model. Strip the product down to a generic chat box. Decide on a Friday to ship it; go live the following Wednesday.
*   **Output:** ChatGPT-style launch that discovers 2,000+ unintended use cases in week one.

## Common Pitfalls

*   **Accelerating Fragile Operations:** Never "maximally accelerate" safety testing, red-teaming, or legal compliance. Use a "pink Slack emoji" or similar signal to clarify when the speed mandate applies and when it does not.
*   **The "Launch and Leave" Mistake:** Shipping early is only valuable if you follow through with polish. Shipping is a point on the journey, not the destination. Once you have data, you must invest in "cleaning up the UI."
*   **Ignoring the "Fail Whale":** If you accelerate distribution without scaling engineering systems (e.g., GPU capacity), you will hit downtime. Balance the waitlist/no-waitlist decision against your ability to keep the site up.
*   **Pipeline Recruiting:** Do not hire via generic pipelines. To maintain a high resting heart rate, hire "barrels" (individuals who can own a whole initiative from start to finish) rather than "ammunition" (people who need constant direction).