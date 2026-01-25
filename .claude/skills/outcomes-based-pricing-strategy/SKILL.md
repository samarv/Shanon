---
name: outcomes-based-pricing-strategy
description: Transition from traditional seat-based or consumption-based SaaS pricing to a model where customers pay only for successful business results (resolutions). Use this when building AI agents, moving from tool-based software to outcome-oriented services, or when your product performs a job autonomously.
---

# Outcomes-Based Pricing Strategy

The AI market is shifting from "software as a tool" to "software as a worker." To capture the value of autonomous agents, you must move beyond seat-based or token-based pricing and align your revenue directly with the business outcomes your agent achieves.

## The Prerequisites for Outcome Pricing
Before implementing this model, your product must meet two criteria:
1.  **Autonomy:** The software must accomplish a job independently (e.g., resolving a customer ticket), rather than just helping a human be slightly more productive.
2.  **Measurability:** The result must be objective and attributable (e.g., a ticket was closed without human intervention, or a lead was qualified).

## Implementation Steps

### 1. Define the "Resolution" Unit
Identify the specific moment value is locked in. Avoid "usage" metrics (like tokens or minutes) that do not correlate with success.
*   **Customer Service:** A "contained" interaction where the user's problem is solved and no human agent is required.
*   **Sales:** A pre-qualified meeting booked or a commission-based sale.
*   **Engineering:** A pull request merged that passes all automated tests.

### 2. Align with the Existing Budget Line Item
Don't ask for a "new" budget. Identify the labor or legacy software cost you are replacing.
*   Find out the "Cost per Ticket" or "Cost per Lead" in the human-operated version of the process.
*   Price your agent at a rate that is significantly lower than the human cost but higher than traditional SaaS margins.

### 3. Establish a Verification System
Create a shared "Source of Truth" with the customer to prevent disputes over what counts as a success.
*   Use "Self-Reflection" agents: Have one AI model supervise another to audit outcomes.
*   Provide a "Resolution Dashboard" that shows the exact path the agent took to solve the problem.

### 4. Implement Context Engineering
To maintain the high resolution rates required for this pricing model to be profitable, you must continuously optimize the agent’s context.
*   **Perform Root Cause Analysis:** When an agent fails to resolve a task, don't just fix the code. Identify what *context* it lacked (e.g., a specific policy or data point).
*   **Update the Knowledge Base:** Feed the missing context back into the system so future outcomes are guaranteed.

## Examples

**Example 1: Customer Experience Agent (Sierra Model)**
*   **Context:** A consumer brand (e.g., Sonos or ADT) wants to automate their chat support.
*   **Input:** The agent handles technical troubleshooting and subscription changes.
*   **Application:** Instead of charging $50/seat/month, the provider charges a pre-negotiated fee (e.g., $5.00) only when the agent "contains" the call—meaning the customer does not call back within 24 hours and never spoke to a human.
*   **Output:** The customer sees an immediate 50% reduction in their "Cost per Ticket," and the software provider earns high-margin revenue based on performance.

**Example 2: AI Lead Generation**
*   **Context:** A B2B company needs to qualify thousands of inbound marketing leads.
*   **Input:** An AI agent emails leads to find "Intent to Buy."
*   **Application:** The provider charges $0 for the emails sent or the "tokens" used. Instead, they charge $100 per "Qualified Meeting" actually held by a human salesperson.
*   **Output:** The buyer’s risk is zero; they only pay when their sales pipeline actually grows.

## Common Pitfalls
*   **Pricing by Tokens:** This is the "lines of code" mistake. Just as more code doesn't mean better software, more tokens don't mean more value. It penalizes efficiency.
*   **Mismatched Buyer and User:** If you use a Product-Led Growth (PLG) motion for a product where the Finance Department is the buyer, you will fail. Use **Direct Sales** when the person benefiting from the outcome (the business owner) is different from the person setting up the agent.
*   **Waiting for Model Improvements:** Don't wait for the next LLM version to fix your resolution rate. If your agent is failing, it’s usually a context problem, not a reasoning problem. Use **Model Context Protocol (MCP)** or similar systems to feed specific business data to the agent.
*   **Ignoring the "Sizzle":** A product needs an "Enduring Value" (the outcome) and a "Reason to Use" (the sizzle). For Google Maps, the outcome was the map; the sizzle was satellite imagery. Ensure your agent has a viral "wow" feature to drive initial adoption.