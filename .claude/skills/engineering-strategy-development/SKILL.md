---
name: engineering-strategy-development
description: Create a technical strategy that prioritizes business impact over technical novelty. Trigger this when a team is overwhelmed by tool sprawl, debating major architectural shifts (like a rewrite), or failing to deliver customer value due to internal technical friction.
---

# Engineering Strategy Development

A good engineering strategy is often "boring." Its primary purpose is to constrain the team's options to ensure limited engineering capacity is spent on problems that actually matter to the business and customers. By standardizing the "Standard Kit" (your core tools), you free the team to innovate on features rather than infrastructure.

## The Strategy Framework
Apply Richard Rumelt’s three-part structure to any technical challenge:

1.  **Diagnosis:** An honest, data-driven assessment of the current status quo.
2.  **Guiding Policies:** A set of rules or constraints to address the diagnosis (e.g., "We only use our existing standard kit").
3.  **Coherent Actions:** Specific, non-negotiable steps to implement the policies (e.g., "Deprecate all non-standard databases by Q3").

## Step-by-Step Process

### 1. Conduct a "Stocks and Flows" Diagnosis
Before writing, model the reality of your current system using systems thinking:
- **Identify Stocks:** What is accumulating? (e.g., technical debt, number of languages, open incidents, hiring pipeline candidates).
- **Identify Flows:** What is the rate of change? (e.g., how fast are we shipping features vs. creating bugs?).
- **Locate the Friction:** Find where reality and your mental model conflict. If engineers feel "slow" but the DORA metrics (lead time, deployment frequency) look good, the friction may be in the *quality* or *relevance* of the work, not the velocity.

### 2. Define the "Standard Kit"
Create a "Boring Strategy" by documenting the authorized tools for the organization:
- List the primary programming language, database, and cloud provider.
- **The Policy:** "We only use the tools we have today." 
- **The Rationale:** Explain that while a new database might be 10% more efficient, the overhead of supporting it (hiring, security, monitoring) costs more than the efficiency gain.

### 3. Draft "Reversible" Guiding Policies
Ensure your strategies are not "Identity Values" (e.g., "We write good code"). A real strategy must be reversible—meaning a reasonable person could argue for the opposite:
- **Example Strategy:** "We run a Ruby monolith to minimize operational complexity." 
- **The Reverse:** "We use a microservices architecture to allow independent team scaling."
- If you can't imagine a sensible company doing the opposite, your strategy is just a platitude.

### 4. Commit to Implementation Actions
Strategy is inert without action. For every policy, define the "cut":
- If the policy is to reduce tech debt, the action must be: "Allocate 20% of every sprint to these specific 3 refactors" or "Shut down the legacy API by Dec 1st."

## Examples

**Example 1: The "No-Cloud" Strategy (Uber Era)**
- **Diagnosis:** We need to launch in markets like China where global cloud providers have no footprint or heavy restrictions.
- **Guiding Policy:** We run everything in our own data centers; no dependency on AWS/GCP.
- **Coherent Action:** Build custom server orchestration and physical hardware provisioning teams. 
- **Output:** The ability to spin up a fully functional data center in 3 months in restricted regions.

**Example 2: The Standardized Language Policy (Stripe/Carta)**
- **Context:** Engineers want to introduce Go and Rust for specific microservices.
- **Diagnosis:** Maintaining multiple build-pipelines and security patches across 4 languages is consuming 30% of the infra team’s time.
- **Guiding Policy:** Stripe/Carta is a Ruby/Java shop. 
- **Coherent Action:** Block all new repos using non-standard languages; migrate existing "experimental" Go services back to the monolith.
- **Output:** Unified tooling that allows any engineer to contribute to any part of the codebase without learning a new stack.

## Common Pitfalls

- **Strategy Cargo Culting:** Copying values like "Users First" from Amazon or Facebook without checking if they match your actual business model. 
- **Aspirational Diagnosis:** Building a strategy for the team you *wish* you had rather than the team you actually have (e.g., choosing a complex architecture that requires senior engineers you can't afford to hire).
- **Identity Values:** Mistaking "Integrity" or "Quality" for strategy. These are table stakes, not strategic choices that resolve trade-offs.
- **The "Victim/Villain" Mindset:** EMs and PMs arguing over "tech debt vs. features" without understanding the underlying incentives.
- **Failure to Write it Down:** Assuming the strategy exists because "everyone knows we use Ruby." If it isn't written, it can't be debugged or improved.