---
name: command-of-details-investigation
description: A rigorous framework for investigating technical, physical, or regulatory constraints to find hidden product opportunities. Use this when a "standard" approach feels mediocre, when experts say a feature is impossible, or when building in highly regulated industries.
---

# Command of Details Investigation

This framework is used to bypass superficial "expert" advice and "asynchronous" industry norms to find the exact parameters where a product can be differentially better. It involves pushing past the first "no" until you reach the ultimate physical or regulatory constraint.

## The Core Principle
Do not stop investigating until you reach the "end" of the problem. Most teams stop at the "Expert Consensus"—the point where a tenured person says, "That’s just how it’s done." To build a category-defining product, you must reach the "Structural Truth"—the point where you understand the literal database fields, the laser settings on a machine, or the specific sentence in a 500-page regulation.

## The Investigation Workflow

### 1. Identify the "Wallpaper"
Look for the invisible constraints that everyone in the industry accepts as unchangeable.
- **Physical:** Manufacturing limits, shipping speeds, material textures.
- **Regulatory:** Compliance text, money movement laws, HIPAA requirements.
- **Data:** How fields are stored in the database and why certain values are "null."

### 2. Challenge the Tenure Trap
When an expert provides a constraint, evaluate if their expertise is based on current technical truth or simply a long history of doing things the old way.
- Ask: "What is the literal consequence if we do not follow this path?"
- Ask: "Is this a contractual obligation, a law, or a best practice from your previous company?"
- Action: Project the actual regulatory text or technical documentation on a screen. Highlight specific sentences and debate the interpretation with legal, engineering, and product in the room.

### 3. Run "1,000 Combinations" Testing
If the constraint is physical or technical, do not trust a vendor's standard output.
- Demand to see the raw settings of the machinery or API.
- Test the extremes: What happens if we increase power/speed by 10x? What if we reduce it to 1x?
- Iterate until you find a configuration that the vendor didn't know was possible.

### 4. Close the Execution Gap
The person in the execution role (PM or Engineer) must become the primary expert. They cannot outsource the "truth" to a consultant.
- **Trust but Verify:** Ask the lead to articulate exactly what breaks if a specific detail is changed.
- **Instrument the "Null":** If a data field is empty or inconsistent, investigate the human behavior at the clinic, warehouse, or app screen that caused that specific data entry.

## Examples

### Example 1: Physical Product Differentiation
**Context:** A team wants to create a unique debit card, but vendors provide "standard" plastic samples.
**Application:** Instead of picking from a catalog, the PM goes to the factory. They discover the laser-engraving machines have thousands of power and aperture combinations.
**Action:** The team tests hundreds of settings, discovering that a specific high-power/low-aperture setting creates a unique red, rough texture that no other card on the market has.
**Output:** A differentially better physical product that cuts through market clutter.

### Example 2: Regulatory Product Design
**Context:** A fintech team is told they cannot offer "Instant" cashing out because bank transfers take three days.
**Application:** The team sits with legal and compliance to read the "wallpaper" of money movement regulations. They find a specific highlightable section of the law that allows for "push to debit" as an alternative structure.
**Action:** They build a new money movement flow based on this specific regulatory interpretation rather than following the industry-standard ACH process.
**Output:** A feature that provides immediate value (instant access to funds) while competitors remain asynchronous.

## Common Pitfalls

- **Stopping at the "Expert":** Accepting a senior leader's opinion because they have "20 years in healthcare." You must verify if their knowledge applies to *your* specific technical stack or regulatory structure.
- **Investigating the Wrong Domain:** Applying this level of depth to a low-stakes problem. Only "go deep" on the 1-2 differentiators that actually matter to the end user (e.g., speed, texture, cost).
- **The "I can't because X said so" Excuse:** Allowing "X said so" to be the end of a conversation. Always demand the underlying "Why" (the contract, the law, or the physical limit).
- **Ignoring the "Null" Values:** Assuming data gaps are just "system errors." These gaps usually hide the exact edge cases where the product is failing or where a new opportunity exists.