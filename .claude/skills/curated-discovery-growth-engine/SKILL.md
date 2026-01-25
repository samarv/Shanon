---
name: curated-discovery-growth-engine
description: Design and implement a growth mechanism based on peer-to-peer curation rather than black-box algorithms. Use this when launching a new discovery feature, building a two-sided marketplace, or looking to unlock network effects without sacrificing user control.
---

# Curated Discovery Growth Engine

The Curated Discovery Growth Engine shifts the responsibility of discovery from a centralized algorithm to the platform's supply side (the creators or power users). This approach builds a social graph based on trust and goodwill rather than "sellable eyeballs," leading to higher-quality user acquisition and stronger network effects.

## The Core Principle: The Control Framework
When designing discovery features, prioritize the "Control Principle." Every decision should be evaluated by whether it grants more agency to the users or the platform:
- **Writer/Provider Control:** Do they choose who is recommended?
- **Reader/Consumer Control:** Is the source of the recommendation transparent?
- **Platform Role:** Facilitate the connection rather than forcing the match.

## Implementation Workflow

### 1. Identify Organic Cross-Pollination
Look for evidence that users are already trying to help each other grow.
- **Signals:** Are users manually linking to each other? Are they guest-posting or mentioning peers in comments?
- **Action:** Map these manual behaviors to identify where a native product feature could reduce friction.

### 2. Design the "Opt-in" Curation Flow
Instead of a "People You May Know" algorithm, create a curation tool for your power users.
- **Simplicity:** Allow users to pick 5-10 peers they genuinely admire.
- **Placement:** Insert the recommendation prompt at a high-intent moment (e.g., immediately after a user subscribes or completes a transaction).
- **Transparency:** Clearly state *why* the user is seeing the recommendation (e.g., "Lenny recommends these 3 newsletters").

### 3. Build the Viral Feedback Loop
Close the loop by notifying the person being recommended.
- **The "Goodwill" Notification:** Send an automated update to the user being recommended: "User X is now recommending you to their audience."
- **Reciprocity Trigger:** This notification serves as a natural prompt for the recipient to recommend the first user back, creating a self-sustaining growth loop.

### 4. Use the "Product Lab" Pilot Method
Before a wide release, test the feature with a hand-picked group of power users to ensure it doesn't "cheapen" the brand.
- Create a "Product Lab": A group of ~100 high-engagement users.
- Run the feature as an optional beta to see if it drives "low-intent" vs. "high-intent" growth.
- Monitor "Open Rates" or "Retention" of users acquired through this path to ensure quality remains high.

## Examples

**Example 1: Marketplace Recommendation**
- **Context:** An Etsy-like marketplace where sellers want to support other artisans.
- **Input:** A seller picks 5 other shops they personally buy from.
- **Application:** After a customer buys a ceramic mug, the "Thank You" page says, "The Maker of this mug also loves these 3 shops."
- **Output:** High-intent traffic flows between shops with similar aesthetics, increasing the "Network-driven" sales metric.

**Example 2: SaaS Integration Discovery**
- **Context:** A B2B tool with a developer ecosystem.
- **Input:** A developer of a popular plugin recommends 3 complementary plugins.
- **Application:** When a user installs the first plugin, a modal suggests the curated list.
- **Output:** Increased stickiness of the platform as users build a more robust, interconnected toolset based on developer trust.

## Common Pitfalls

- **Fearing "Too Many Steps":** Leaders often worry that an opt-in flow has too much friction compared to an automated algorithm. However, the "costly signal" of a manual recommendation often results in higher-quality conversions that outweigh the drop-off.
- **The "Low Intent" Myth:** Assuming that discovery-driven users will be low quality. If the recommendation comes from a trusted source (e.g., a writer the user just paid), the intent remains high.
- **Ignoring the Robin Hood Effect:** Failing to realize that early power users want to "share the wealth." If you don't provide a way for big players to boost smaller players, you miss out on a massive organic growth lever.
- **Over-Automating:** Avoid the temptation to "autocomplete" recommendations for users. This erodes the trust that makes the curated discovery engine work.