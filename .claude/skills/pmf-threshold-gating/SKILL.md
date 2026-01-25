---
name: pmf-threshold-gating
description: A high-bar framework for measuring and achieving product-market fit (PMF) before scaling. Use this when validating a new product line, deciding if a beta is ready for a general release, or diagnosing why a product isn't generating organic word-of-mouth growth.
---

# PMF Threshold Gating

To drive massive organic word-of-mouth growth, you must move past "good enough" to "great enough." This framework uses a high-threshold Sean Ellis Score as a hard gate to prevent "scaling a small problem into a big mess." By demanding that 50% of users feel "very disappointed" if a product disappeared, you ensure the product is fundamentally different rather than incrementally better.

## The Pre-Build Gate: Mock Press Release
Before assigning engineering resources, validate the value proposition:
- Write a two-paragraph mock press release or customer announcement.
- If you cannot articulate why the target customer should care in two paragraphs, the strategy is not clear enough to build.
- **Rule:** "We may not be right, but at least we are clear."

## The PMF Measurement Workflow

### 1. The High-Bar Sean Ellis Survey
Ask a cohort of early users: *"How disappointed would you be if this product went away?"*
- **The Scale:** 1. Not disappointed, 2. Somewhat disappointed, 3. Very disappointed.
- **The Nubank Threshold:** 50% must answer "Very Disappointed."
- **Why 50%?** The standard 40% often includes "politeness bias." A 50% bar ensures the product is a "must-have" that drives fanaticism.

### 2. Identify the "Bullseye Cohort"
If your overall score is below 50%, find the segment where it is above 50%.
- Filter the data by usage patterns (e.g., "Users who used the feature 4+ times").
- Look for the common denominator among the "Very Disappointed" group.

### 3. The "Direct-Line" Investigation
Once the bullseye cohort is identified, the PM/Designer must skip the research department and call them directly.
- **The Rule of 10:** Call 10 customers from the bullseye cohort personally.
- **The Observation Method:** Ask indirect questions to find their pain points rather than asking if they like your solution.
- **Goal:** By the 5th or 6th call, you should be able to predict what the 7th person will say. This indicates you have found the "truth" behind the PMF.

### 4. Iterate to Scale
Do not scale the product to the mass market until the Sean Ellis score hits the threshold in the target segment. 
- If the score is low, use the direct call insights to adjust features until the 50% mark is cleared.
- **Mantra:** "We are not going to take a small problem and scale it."

## Examples

**Example 1: Payments Assistant (Assistente de Pagamentos)**
- **Context:** A bill-pay automation tool launched in Brazil.
- **Initial Result:** Sean Ellis score was borderline (40%).
- **Bullseye Cohort Discovery:** Analysis found a segment with 4+ commitments on 2+ different payment rails had a 70% score.
- **Application:** The team pivoted the roadmap to focus on multi-rail onboarding and automated registration for high-volume bill payers.
- **Output:** Grew from hundreds of thousands to over 10 million monthly actives.

**Example 2: High-Income Rewards Card (Ultravioleta)**
- **Context:** A premium card with a monthly fee and rewards.
- **Initial Result:** Mixed feedback. 
- **Bullseye Cohort Discovery:** Only users who spent enough to trigger the fee waiver loved the product fanatically.
- **Application:** The team spent 2 years in "the lab" iterating on the specific benefits for that segment (fee waiver transparency, specific rewards) before scaling.
- **Output:** Achieved decisive PMF in the high-income segment before mass marketing.

## Common Pitfalls
- **Scaling a "Leaky Bucket":** Scaling a product with a low Sean Ellis score usually results in high churn. You can "bounce a dead cat" (make metrics look good for months) using a large existing user base, but the product will eventually fail.
- **The "Lawyer" Mindset:** Becoming a lawyer for your hypothesis (defending it) instead of a judge (evaluating it objectively). Use customer anecdotes to trump your data.
- **Hedging the Strategy:** Trying to serve all customers at once. Startups must concentrate bets on a specific segment to build wealth; diversification is only for preserving it.
- **The Research Distance:** Relying on a third-party researcher to summarize findings. PMs must "feel" the customer's tone of voice via direct phone calls to understand the nuance of their pain.