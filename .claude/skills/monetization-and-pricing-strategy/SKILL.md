---
name: monetization-and-pricing-strategy
description: A framework for designing, testing, and evolving B2B pricing models. Use this skill when launching a new product, preparing a major feature release, or when revenue growth is lagging behind user growth.
---

Pricing is not a "set it and forget it" task; it is a core part of the product roadmap that must be revisited every 6–12 months to ensure the business is being appropriately compensated for the value it provides.

## The Pricing Committee
Establish a cross-functional pricing committee to own monetization. This prevents pricing from being "plucked out of thin air" and ensures buy-in across the organization.
- **Product/Growth:** To align pricing with user milestones and value metrics.
- **Data Science:** To analyze usage patterns and experiment results.
- **Finance/RevOps:** To ensure predictability and margin health.
- **Sales:** To provide feedback on customer pushback and willingness to pay.

## The "Day 1 vs. Day 100" Paywall Framework
Decide what stays free and what goes behind a paywall by mapping features to the user journey.

### Day 1 Features (The "Aha" Moment)
- **Goal:** Drive habit formation and collapse time-to-value.
- **Placement:** Keep these in the **Free/Starter tier**.
- **Criteria:** Anything required for the user to experience the core utility of the product for the first time.

### Day 100 Features (The Value Escalator)
- **Goal:** Monetize advanced usage and organizational scale.
- **Placement:** Move these to **Premium/Enterprise tiers**.
- **Criteria:** 
    - **Advanced Functionality:** Features that only provide value once a user is an expert.
    - **Scale/Data:** Features that become useful only after a certain volume of data is reached.
    - **Collaboration:** Administrative controls, security (SSO), and multiplayer workflows.

## Quantitative Pricing Research
Use these two specific survey methods to find the right price point and package structure.

### 1. The 100-Point Feature Question
To understand what features drive the most value:
1. Provide a list of features (current and roadmap).
2. Give the user 100 "points" to spend across them.
3. Analyze the distribution to see which 1–2 features are the primary conversion drivers.

### 2. The Van Westendorp Price Sensitivity Meter
Ask four specific questions to determine the acceptable price range:
1. At what price is the product so **cheap** that you doubt its quality?
2. At what price is the product a **good deal**?
3. At what price is the product **expensive**, but you'd still consider it?
4. At what price is the product **prohibitively expensive**?

## Pricing Experimentation Tactics
- **Geo-Fencing:** Test pricing changes in smaller markets (e.g., Canada or Australia) before rolling them out to the US or globally.
- **Value Metric Alignment:** Move away from pure seat-based pricing toward "usage-based" metrics (e.g., API calls, messages sent, terabytes stored) to create a natural revenue escalator.
- **The "High-End" Push:** In enterprise sales, intentionally increase the price for 20-30% of deals to find the "ceiling." If you have zero hesitation from buyers, you are wildly underpriced.

## Examples

**Example 1: Identifying the "Guilt" Signal**
- **Context:** A company with a single premium tier and a very popular free version.
- **Observation:** In user surveys, the top reason for upgrading is: "I feel guilty because I use it so much."
- **Application:** Recognize that "guilt" means the free version is too good.
- **Action:** Bifurcate the strategy. Create a "Prosumer" tier for heavy individual users and a "Team" tier for collaboration features (like Evernote's transition).

**Example 2: The 10X Enterprise Jump**
- **Context:** A founder-led sales call with a high-value prospect (e.g., Envoy's early days).
- **Application:** The founder senses high excitement and "goes out on a limb" by quoting 10X the standard price.
- **Output:** The prospect agrees instantly with no pushback. This provides immediate data that the current pricing is too low and the ceiling has not yet been hit.

## Common Pitfalls
- **The Guilt Driver:** If users pay out of obligation rather than to unlock a specific value, your free tier is cannibalizing your paid tier.
- **Ignoring Churn in Tests:** Pricing experiments take time. A test that increases revenue today might cause a massive churn spike in year two when renewal hits.
- **Optimizing for Individual Users in Multiplayer Tools:** Don't worry about monetizing the individual designer or engineer if their usage drives "wall-to-wall" adoption within an enterprise (the Figma model).
- **Single Premium Tiers:** Offering only one paid option leaves money on the table. Different personas always have different willingness-to-pay thresholds.