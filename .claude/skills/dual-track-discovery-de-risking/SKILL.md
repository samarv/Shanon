---
name: dual-track-discovery-de-risking
description: A framework for running simultaneous discovery and delivery tracks to de-risk high-stakes product ideas. Use this when your team is stuck on a "feature treadmill," when you need to innovate on high-risk features without stopping delivery, or when planning a roadmap that balances "big swings" with predictable updates.
---

# Dual-Track Discovery and De-risking

Dual-track agile allows product teams to move away from "feature factory" or waterfall models by running discovery (validating what to build) and delivery (building the software) in parallel. The core goal is to de-risk your most ambitious ideas early so they don't fail after months of engineering effort.

## The Framework Structure

### 1. Separate the Tracks
Do not treat discovery and delivery as sequential phases. They must happen simultaneously:
- **Discovery Track:** Focuses on de-risking assumptions regarding value, usability, feasibility, and business viability.
- **Delivery Track:** Focuses on building production-quality software that is scalable, performant, and secure.

### 2. Map the "Big Swings"
Use a 2x2 matrix to categorize all potential initiatives:
- **X-Axis:** Risk/Uncertainty (Low to High)
- **Y-Axis:** Potential Impact/Reward (Low to High)

### 3. Prioritize "High-Risk Discovery"
Traditional teams often "eat the frog" by doing the hardest engineering first. This framework suggests a different approach: **prioritize discovery for the high-risk, high-reward "Big Swings" first.**
- If you only work on low-risk/predictable tasks, you will never truly innovate.
- Use discovery to turn "High-Risk" ideas into "Low-Risk" execution items.

## Implementation Steps

1.  **Identify Riskiest Assumptions:** For any high-impact idea, list the reasons it might fail (e.g., "Users won't pay for this," "It’s technically impossible," "It violates copyright law").
2.  **Run Discovery Experiments:** Instead of building the full feature, use the smallest possible method to validate the assumption:
    - Painted-door tests (fake buttons to measure intent)
    - High-fidelity prototypes for usability
    - Technical spikes for feasibility
    - Concierge MVPs (manually doing the work behind the scenes)
3.  **Establish a "Definition of Ready":** An item only moves from the Discovery Track to the Delivery Track when it is sufficiently de-risked.
4.  **Continuous Cycle:** As one item moves to Delivery, the Discovery track immediately begins on the next high-risk/high-reward item.

## Examples

**Example 1: Artist Merch on Spotify**
- **Context:** An initiative to allow artists to sell exclusive merch directly to top fans.
- **High-Risk Assumption:** Fans won't buy merch through a streaming app; they prefer official websites.
- **Discovery Application:** Instead of building a full e-commerce backend, the team runs a "top listener" email campaign with a link to a simple checkout page for 3 artists.
- **Output:** High conversion rates prove the value; the item moves to the Delivery track for full integration.

**Example 2: Creator Financing/Advances**
- **Context:** Providing creators with cash advances based on their projected earnings.
- **High-Risk Assumption:** Creators won't trust the platform with their financial debt.
- **Discovery Application:** The PM and Designer conduct 15 deep-dive interviews with creators showing mock-ups of the terms and "contract" language.
- **Output:** Interviews reveal specific fears about interest rates; the team adjusts the product model and de-risks the "Trust" factor before a single line of code is written.

## Common Pitfalls

- **The "Waterfall in Disguise":** Waiting for the Discovery track to finish for the *entire* roadmap before starting Delivery. These must overlap.
- **Favoring the "Safe" Choice:** Only putting low-risk, incremental improvements into the Delivery column. This leads to stagnation. You must use Discovery to make "Big Swings" safe enough to build.
- **Discovery Without Engineering:** Excluding engineers from the Discovery track. Engineers should participate in Discovery to de-risk technical feasibility early.
- **Ignoring Discovery Signals:** Building the feature anyway after the Discovery track shows low user interest because "it's already on the roadmap."