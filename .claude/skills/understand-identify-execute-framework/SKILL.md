---
name: understand-identify-execute-framework
description: A 3-stage product development process designed to increase shipping velocity and success rates by de-risking ideas before building. Use this when facing flat metrics after major launches, entering a new problem space, or planning high-velocity growth sprints to ensure work is grounded in first principles rather than justification bias.
---

# Understand, Identify, Execute (UIE)

The "Understand, Identify, Execute" framework is a method for de-risking product development by treating "understanding" as a first-class citizen in the roadmap. Rather than shipping a volume of guesses, teams allocate specific bandwidth to uncovering root causes and funnels before committing to full execution.

## The Anti-Pattern: Identify, Justify, Execute
Many teams fall into the trap of deciding what they want to build first (**Identify**), then pulling data to support the decision (**Justify**), and sinking months into building it (**Execute**). This often results in "flat metrics" upon launch because the work wasn't grounded in a real user pain point or technical reality.

## The UIE Process

### 1. Understand (First Principles)
Create an "intentional affordance" in your sprint for work that doesn't involve shipping code. This is a line item on the roadmap, not background work.
- **Goal:** De-risk the project and close knowledge gaps.
- **Tactics:**
  - **Instrumentation:** If you don't have logging for an 8-step signup funnel, the "Understand" work is adding that logging.
  - **Funnel Analysis:** Mapping exactly where users drop off.
  - **User Archetypes:** Identify the "Adjacent User"—the person just outside your current user base who is struggling to use the product.
  - **Cross-functional Input:** Ask Engineering, "What do we need to understand about the codebase to scale this?" and Data Science, "What proxy metrics are we missing?"

### 2. Identify (Targeted Opportunity)
Based on the "Understand" phase, select the specific lever that will drive the most impact.
- Compare what you know with high confidence (data-backed) against what you are interested in (hypothesis-based).
- Focus on low-effort, high-likelihood wins discovered during the research.

### 3. Execute (Parallel Pathing)
Run execution and understanding in parallel. 
- **The Portfolio Approach:** A roadmap should not be 100% execution.
- **Initial Mix:** In a new problem space, aim for 60% Execution / 40% Understand work.
- **Mature Mix:** As confidence grows, shift to 85% Execution / 15% Understand work.
- **Feedback Loop:** Use the insights from this sprint’s "Understand" work to plan the next sprint’s "Execution" work.

## Examples

**Example 1: Instagram Signup Flow**
- **Context:** The team wanted to improve the signup rate but had no visibility into the 8-step funnel.
- **Understand:** The team spent a sprint doing nothing but instrumenting every step of the funnel and growth marketing schemas.
- **Identify:** The data showed a massive drop-off between account creation and friend discovery.
- **Execute:** Launched a "connections pivot" that prioritized human-to-human connections over celebrity recommendations, doubling retention over 18 months.

**Example 2: Instacart Reordering**
- **Context:** Retention was lower than expected for long-term users.
- **Understand:** PMs dogfooded the app as "Adjacent Users" (busy parents) and looked at cohort data. They found that after 5 orders, 90% of a user's cart was the same as previous weeks.
- **Identify:** The product made reordering difficult (requiring 7+ clicks to find previous items).
- **Execute:** Shipped a streamlined "Buy it Again" feature and "1-Click Reorder" for staples like milk and eggs, significantly increasing repeat order frequency.

## Common Pitfalls
- **Building to Justify:** Never pull data specifically to "win" an argument for a feature you’ve already decided to build.
- **Skipping the Affordance:** Assuming "Understand" work happens in the background. If it isn't a line item on the sprint board, it won't get done.
- **Analysis Paralysis:** Spending 100% of time on "Understand" work. You must always be shipping something to keep the feedback loop alive.
- **Ignoring the Adjacent User:** Designing only for "Power Users." Always test your flow as a brand-new user with no search history or pre-existing "graph" to see where the experience breaks.